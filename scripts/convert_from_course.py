"""Convert the Introduction to Computing course folder into Carpentries Workbench episodes: one episode per week.
Each week page holds the week overview, its sections, the Concepts Bridge and the practice task as level-2
headings, so the Workbench menu shows Week N with 1.1, 1.2 ... underneath.

Model answers, quiz pools and other tutor-only files are never copied: the site is for learners.

Usage: python scripts/convert_from_course.py COURSE_FOLDER LESSON_FOLDER
       python scripts/convert_from_course.py ../intro-to-computing ."""
import os, posixpath, re, shutil, sys, zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wb_meta import WEEKS, TIME, SECTIONS, BRIDGES, PRACTICE, PRACTICE_Q, ASSETS

SRC, DST = sys.argv[1], sys.argv[2]
EP = os.path.join(DST, 'episodes')
ZIP_NAME = 'course-files.zip'
ZIP_ROOT = 'IntroToComputing'
PROBLEMS = []


# ---------------------------------------------------------------- names and link targets
def week_file(w): return f'week-{w}.md'


def web_name(f):
    """The site build turns links to .md files into .html pages, so Markdown worksheets are published as .txt."""
    return f[:-3] + '.txt' if f.endswith('.md') else f
def sec_anchor(s): return 'section-' + s.replace('.', '-')


TARGET = {}   # source path (relative to SRC, posix) -> (page or file, anchor)
for s, m in SECTIONS.items():
    TARGET['weeks/' + m['src']] = (week_file(int(s[0])), sec_anchor(s))
for w in WEEKS:
    TARGET[f'weeks/week-{w}/README.md'] = (week_file(w), f'week-{w}-overview')
    TARGET[f'weeks/week-{w}/bridge.md'] = (week_file(w), f'week-{w}-bridge')
    TARGET[f'weeks/week-{w}/practice/README.md'] = (week_file(w), f'week-{w}-practice')
    for f in PRACTICE[w]['files']:
        TARGET[f'weeks/week-{w}/practice/{f}'] = (f'files/week-{w}/{web_name(f)}', '')
    if 'extra_readme' in PRACTICE[w]:
        TARGET[f'weeks/week-{w}/practice/{PRACTICE[w]["extra_readme"]}'] = (week_file(w), f'week-{w}-case-study')
for a in ASSETS:
    TARGET[a] = ('files/' + a[len('assets/'):], '')


# ---------------------------------------------------------------- text helpers
def nice_label(label, target):
    """Replace a label that is a file name (such as bridge.md) with words a learner understands."""
    if not re.fullmatch(r'[\w./-]+\.md', label):
        return label
    if target.endswith('/bridge.md'):
        return 'the Concepts Bridge'
    if target.endswith('/practice/README.md'):
        return 'the practice task'
    return label


def links(t, src_rel, page):
    """Rewrite relative links in text from source file src_rel, for the week page `page`."""
    base = posixpath.dirname(src_rel)

    def fix(m):
        label, url = m.group(1), m.group(2)
        if re.match(r'^(https?:|mailto:|#)', url):
            return m.group(0)
        path, _, frag = url.partition('#')
        target = posixpath.normpath(posixpath.join(base, path))
        label = nice_label(label, target)
        if target in TARGET:
            name, anchor = TARGET[target]
            if name.startswith('files/'):
                return f'[{label}]({name})'
            anchor = anchor or frag
            if name == page:
                return f'[{label}](#{anchor})'
            return f'[{label}]({name}#{anchor})'
        if target == 'README.md':
            return f'[{label}](index.md)'
        inside = [k for k in TARGET if k.startswith(target.rstrip('/') + '/') and TARGET[k][0].startswith('files/')]
        if inside:   # a link to a folder: web hosts do not list folders, so link each file in it
            return label + ' (' + ', '.join(f'[{posixpath.basename(k)}]({TARGET[k][0]})' for k in sorted(inside)) + ')'
        PROBLEMS.append(f'unmapped link in {src_rel} -> {url}')
        return label
    return re.sub(r'(?<!!)\[([^\]]*)\]\(([^)\s]+)\)', fix, t)


def drop_nav(t):
    t = re.sub(r'^\[Back to[^\n]*\n?', '', t, flags=re.M)
    return re.sub(r'\s*·\s*\[Back to [^\]]*\]\([^)]*\)', '', t)


def strip_title(t):
    return re.sub(r'^# [^\n]*\n', '', t, count=1)


def strip_section_header(t):
    """Remove the title, the week line and the Contents list from a lesson section. Keep the Time line."""
    t = strip_title(t)
    t = re.sub(r'^\*\*Week \d:\*\*[^\n]*\n', '', t, flags=re.M)
    t = re.sub(r'^\*\*Contents\*\*\s*\n(?:\s*\n)*(?:- \[[^\n]*\n)+', '', t, flags=re.M)
    t = re.sub(r'^---\s*$', '', t, count=1, flags=re.M)
    return t


def exercises(t):
    """Wrap the Exercises section in a challenge block, with its Answers as a solution."""
    m = re.search(r'^## Exercises[^\n]*\n', t, flags=re.M)
    if not m:
        return t
    head, ex = t[:m.start()], t[m.end():]
    nxt = re.search(r'^(## |---\s*$)', ex, flags=re.M)    # stop at the next section or a reference list
    ex, tail = (ex[:nxt.start()], ex[nxt.start():]) if nxt else (ex, '')
    q, _, a = re.split(r'^(### Answers[^\n]*)\n', ex, maxsplit=1, flags=re.M) + ['', ''] if '### Answers' not in ex else re.split(r'^(### Answers[^\n]*)\n', ex, maxsplit=1, flags=re.M)
    block = f'::::::::::::::::::::::::::::::::::::: challenge\n\n## Exercises\n\n{q.strip()}\n\n'
    if a.strip():
        block += f':::::::::::::::: solution\n\n## Answers\n\n{a.strip()}\n\n:::::::::::::::::::::::::\n'
    block += '::::::::::::::::::::::::::::::::::::::::::::::::\n\n'
    return head.rstrip() + '\n\n' + block + tail


def bridge_blocks(t):
    """Turn the Activity section and its Model answer into a challenge with a solution."""
    m = re.search(r'^## (Activity[^\n]*)\n(.*?)^### (Model answers?[^\n]*)\n(.*?)(?=^## |\Z)', t, flags=re.M | re.S)
    if not m:
        PROBLEMS.append('bridge without an Activity and Model answer')
        return t
    block = (f'::::::::::::::::::::::::::::::::::::: challenge\n\n## {m.group(1)}\n\n{m.group(2).strip()}\n\n'
             f':::::::::::::::: solution\n\n## {m.group(3)}\n\n{m.group(4).strip()}\n\n:::::::::::::::::::::::::\n'
             f'::::::::::::::::::::::::::::::::::::::::::::::::\n\n')
    return t[:m.start()] + block + t[m.end():]


def callouts(t):
    """Turn '> **Title.** text' quote boxes into Workbench callouts."""
    def box(m):
        body = re.sub(r'^> ?', '', m.group(0), flags=re.M).strip()
        return f':::::::::::::::::::::::::::::::::::::::: callout\n\n{body}\n\n::::::::::::::::::::::::::::::::::::::::::::::::\n'
    return re.sub(r'(?:^>[^\n]*\n?)+', box, t, flags=re.M)


def demote(t, levels=1):
    """Push every markdown heading down `levels` levels (outside code blocks), so that only the
    week page's own level-2 headings appear in the Workbench menu."""
    out, fence = [], None
    for line in t.split('\n'):
        f = re.match(r'^\s*(```+|~~~+)', line)
        if f:
            fence = None if fence and f.group(1).startswith(fence[:3]) else (fence or f.group(1))
        elif fence is None:
            h = re.match(r'^(#{1,5}) ', line)
            if h:
                line = '#' * min(6, len(h.group(1)) + levels) + line[len(h.group(1)):]
        out.append(line)
    return '\n'.join(out)


def box(kind, items):
    body = '\n'.join(f'- {x}' for x in items)
    return f':::::::::::::::::::::::::::::::::::::: {kind}\n\n{body}\n\n::::::::::::::::::::::::::::::::::::::::::::::::\n'


SITE_WORDING = [   # course-folder wording that does not make sense on the website
    ('in `weeks/week-2/practice/mystery_files/`', 'in the mystery files (see the Week 2 practice task)'),
    ('from the course folder to your computer', 'from the Files box above to your computer'),
    ('It is in the course folder as [`assets/lmc/add.lmc`]', 'Download it as [`add.lmc`]'),
]


def site_wording(t):
    for a, b in SITE_WORDING:
        t = t.replace(a, b)
    return t


def clean(t, src_rel, page):
    return callouts(site_wording(links(drop_nav(t), src_rel, page))).strip() + '\n'


def read(rel):
    with open(os.path.join(SRC, rel), encoding='utf-8') as f:
        return f.read()


def write(name, text):
    path = os.path.join(EP, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def part(title, anchor, body):
    return f'## {title} {{#{anchor}}}\n\n{body.strip()}\n\n'


def zip_add(z, full, arcname):
    """Add a file with a fixed date, so the zip only changes when its contents change."""
    info = zipfile.ZipInfo(arcname, date_time=(2026, 1, 1, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    with open(full, 'rb') as f:
        z.writestr(info, f.read())


# ---------------------------------------------------------------- build
os.makedirs(EP, exist_ok=True)
for f in os.listdir(EP):          # remove episodes from earlier conversions
    if f.endswith('.md'):
        os.remove(os.path.join(EP, f))
for sub in ('files', 'data'):     # remove generated files, so renamed or deleted ones do not linger
    shutil.rmtree(os.path.join(EP, sub), ignore_errors=True)
os.makedirs(os.path.join(EP, 'files'))
os.makedirs(os.path.join(EP, 'data'))

for w, theme in WEEKS.items():
    watch, rp, bridge_min, build = TIME[w]
    secs = [s for s in SECTIONS if s.startswith(f'{w}.')]
    page = week_file(w)
    body = ''

    # overview
    rel = f'weeks/week-{w}/README.md'
    body += part(f'Week {w} overview', f'week-{w}-overview', demote(clean(strip_title(read(rel)), rel, page)))

    # sections
    for s in secs:
        m = SECTIONS[s]
        src = 'weeks/' + m['src']
        t = exercises(clean(strip_section_header(read(src)), src, page))
        body += part(f"{s} {m['title']}", sec_anchor(s), demote(t))

    # bridge
    rel = f'weeks/week-{w}/bridge.md'
    t = bridge_blocks(clean(strip_title(read(rel)), rel, page))
    body += part(f"Concepts Bridge: {BRIDGES[w]['title']}", f'week-{w}-bridge', demote(t))

    # practice task, with its files
    pm = PRACTICE[w]
    rel = f'weeks/week-{w}/practice/README.md'
    t = clean(strip_title(read(rel)), rel, page)
    files = '\n'.join(f'- [{posixpath.basename(web_name(f))}](files/week-{w}/{web_name(f)})' for f in pm['files'])
    t = (':::::::::::::::::::::::::::::::::::::::: callout\n\n### Files for this task\n\n'
         f'Download single files here, or every course file at once in the [course files zip](data/{ZIP_NAME}). '
         'Worksheets download as plain text (`.txt`): open one in any text editor, and save your copy with the name the task gives.\n\n'
         f'{files}\n\n:::::::::::::::::::::::::::::::::::::::::::::::::::\n\n') + t
    t = demote(t)
    if 'extra_readme' in pm:
        rel2 = f'weeks/week-{w}/practice/{pm["extra_readme"]}'
        title2 = re.match(r'# ([^\n]*)', read(rel2)).group(1)
        t += f'\n### {title2} {{#week-{w}-case-study}}\n\n' + demote(clean(strip_title(read(rel2)), rel2, page), 2)
    body += part(f'Practice task: {pm["title"]}', f'week-{w}-practice', t)

    for f in pm['files']:
        dst = os.path.join(EP, 'files', f'week-{w}', web_name(f))
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(os.path.join(SRC, 'weeks', f'week-{w}', 'practice', f), dst)

    # page metadata: the week's questions, objectives and key points
    q = [f'What will I learn in Week {w}, and how should I spend my 6 hours?']
    o = ['Plan your study time for the week using the time plan.']
    k = ['Each week has five blocks: Watch, Read & practise, Concepts Bridge, Build and Quiz.']
    for s in secs:
        q += SECTIONS[s]['q']; o += SECTIONS[s]['o']; k += SECTIONS[s]['k']
    q += BRIDGES[w]['q']; o += BRIDGES[w]['o']; k += BRIDGES[w]['k']
    pq, po, pk = PRACTICE_Q[w]
    q += pq; o += po; k += pk
    head = (f"---\ntitle: 'Week {w}: {theme}'\nteaching: {watch + round(rp * 0.6) + 20}\n"
            f"exercises: {round(rp * 0.4) + 10 + build}\n---\n\n")
    text = head + box('questions', q) + '\n' + box('objectives', o) + '\n' + body.strip() + '\n\n' + box('keypoints', k)
    if re.search(r'model[_ ]answer\.md|curriculum/quizzes|`weeks/|`assets/|course folder', text):
        PROBLEMS.append(f'{page} still mentions a tutor-only file')
    write(page, text)

# course files linked from lessons (for example the Week 4 add program)
for a in ASSETS:
    dst = os.path.join(EP, 'files', a[len('assets/'):])
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(os.path.join(SRC, a), dst)

# one zip of every learner file, keeping the week folders
with zipfile.ZipFile(os.path.join(EP, 'data', ZIP_NAME), 'w', zipfile.ZIP_DEFLATED) as z:
    for w in WEEKS:
        for f in PRACTICE[w]['files']:
            zip_add(z, os.path.join(SRC, 'weeks', f'week-{w}', 'practice', f), f'{ZIP_ROOT}/week-{w}/{f}')
    for a in ASSETS:
        zip_add(z, os.path.join(SRC, a), f'{ZIP_ROOT}/{a[len("assets/"):]}')

print(len(WEEKS), 'week episodes written')
for p in PROBLEMS:
    print('  PROBLEM:', p)
