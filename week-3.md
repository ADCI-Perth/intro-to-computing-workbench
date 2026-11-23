---
title: 'Week 3: Software and operating systems'
teaching: 134
exercises: 176
---

:::::::::::::::::::::::::::::::::::::: questions

- What will I learn in Week 3, and how should I spend my 6 hours?
- What is the difference between application software and system software?
- What does an operating system do?
- How are files and folders organised?
- How do I control a computer by typing commands?
- Why should people only have the access they need?
- Can I audit software and use the command line on a real log?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Plan your study time for the week using the time plan.
- Sort software into applications, operating systems and utilities.
- Explain why updates matter.
- Describe the main jobs of an operating system.
- Read absolute and relative file paths.
- Move around folders and manage files with Linux commands.
- Search a log file with grep.
- Read and set file permissions.
- Apply least privilege to files and accounts.
- Sort software, search a server log and lock down private files.

::::::::::::::::::::::::::::::::::::::::::::::::

## Week 3 overview {#week-3-overview}

**Theme:** the software that runs a computer, what an operating system does, and how to manage files from the command line.


### What you will be able to do this week

- Tell system software (operating systems, drivers, utilities) from application software, with examples.
- Explain the main jobs of an operating system.
- Create, copy, move, delete and search files from the Linux command line.
- Read and change file permissions, and explain why they matter for security.

### Time plan (under 6 hours)

| Block | What you do | Time |
|---|---|---|
| Watch | 4 videos | 0 h 45 m |
| Read & practise | Sections 3.1, 3.2 and 3.3, with the exercises | 1 h 55 m |
| Concepts Bridge | [Least privilege](#week-3-bridge) | 0 h 30 m |
| Build | [Software audit and command-line lab](#week-3-practice), your portfolio item for this week | 2 h 00 m |
| Quiz | Canvas quiz, 6 questions | 0 h 15 m |
| **Total** | | **5 h 25 m** |

Suggested order: video 1, then Sections 3.1 and 3.2; videos 2, 3 and 4, then Section 3.3. Do the Bridge, Build and Quiz last.

**You do not need to install anything.** The command line runs in your browser using **JSLinux**, a free Linux system with no account needed. Section 3.3 shows you how to start it.

### Watch (0 h 45 m)

| # | Video | Length | Look for |
|---|---|---|---|
| 1 | CC#18 [Operating Systems](https://www.youtube.com/watch?v=26QPDBe-NB8&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye) | 13:36 | Why operating systems were invented, and how they share the CPU and memory between programs. |
| 2 | CC#22 [Keyboards & Command Line Interfaces](https://www.youtube.com/watch?v=4RPtJ9UyHS0&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye) | 11:24 | Where the command line came from, and why it is still used. |
| 3 | [NetworkChuck] [60 Linux Commands you NEED to know (in 10 minutes)](https://www.youtube.com/watch?v=gd7BXuUQ91w) | 10:50 | A fast tour. Focus on `pwd`, `ls`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `rm`, `cat`, `grep` and pipes. You do not need `sudo`, installing software or networking commands this week. |
| 4 | [Travis Media] [Linux File Permissions in 5 Minutes](https://www.youtube.com/watch?v=LnKoncbQBsM) | 6:03 | How to read `rwx`, and what the numbers in `chmod` mean. |

**Video total: about 42 minutes.**

### Read & practise (1 h 55 m)

| Order | Section | Time | What to do |
|---|---|---|---|
| 1 | [Section 3.1: Software](#section-3-1) | about 35 min | Read all of it. Look at the software on your own computer. Do exercises 1 to 4. |
| 2 | [Section 3.2: Operating systems and file management](#section-3-2) | about 35 min | Read all of it. Do exercises 1 to 5. |
| 3 | [Section 3.3: The Linux command line](#section-3-3) | about 45 min | Start JSLinux and type every example. Do practice tasks 1 to 6. |

Total: 35 + 35 + 45 = 115 minutes (1 h 55 m).

### Concepts Bridge (0 h 30 m)

Open [the Concepts Bridge](#week-3-bridge). It explains **least privilege**, the idea that every person and program should have only the access it needs. It is the first rule of system security, and it explains why you should not work as `root`.

### Build (2 h)

Open the [practice task](#week-3-practice). You will audit the software on your own computer, then use the command line to set up folders for an invented office, search a server log for errors and lock down private files. This is your portfolio item for this week.

### Quiz (0 h 15 m)

Take the Canvas quiz for Week 3 after you finish the Build. It has 6 questions drawn from a pool. It is marked automatically.

### Portfolio this week

Submit at the end of the week:

- `week3_lab.md` (or a Word or PDF copy): your completed [worksheet](files/week-3/week3_lab_worksheet.txt), with your software audit, command log, screenshot and reflection.

Your tutor marks the portfolio. The quiz is marked automatically.

### Optional

Nothing here is required. Try these if you want more.

- CC#26 [Graphical User Interfaces](https://www.youtube.com/watch?v=XIGSJshYb90&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye) (12:59): how the GUI was invented.
- CC#20 [Files & File Systems](https://www.youtube.com/watch?v=KN8YgJnShPM&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye) (12:03): you watched this in Week 2. Rewatch the second half on file systems.
- Try `sort`, `uniq` and `cut` on the server log. For example, `grep "Failed login" server.log | sort`.
- **Killercoda** (https://killercoda.com/playgrounds) offers a fuller Ubuntu playground in the browser. It needs a free sign-up, so it is optional.

## 3.1 Software {#section-3-1}

**Time:** about 35 minutes (25 minutes reading, 10 minutes practice and exercises).


### What software is

In Week 1 you met **hardware**: the physical parts. **Software** is the set of instructions, called **programs**, that tell the hardware what to do. Software comes in two broad kinds:

| Kind | What it is for | Examples |
|---|---|---|
| **System software** | Runs and looks after the computer itself | Windows, macOS, Linux, device drivers, antivirus, backup tools |
| **Application software** (apps) | Helps a person do a task | Word, Excel, a web browser, Zoom, a payroll system |

A simple test: **if you removed it, would the computer still work?** Without the operating system, nothing works. Without Excel, the computer still works; you just cannot open spreadsheets.

### System software

System software has three main parts.

**1. The operating system (OS).** The most important program on the computer. It manages the hardware and lets every other program run. Section 3.2 covers it in detail.

**2. Device drivers.** A **driver** is a small program that lets the operating system talk to one piece of hardware, such as a printer, a graphics card or a webcam. Each make and model needs its own driver. When a new printer "doesn't work", the cause is often a missing or out-of-date driver.

**3. Utilities.** A **utility** is a tool that maintains, protects or tidies the computer. Common utilities:

| Utility | What it does | Examples |
|---|---|---|
| Antivirus (anti-malware) | Finds and removes harmful software | Microsoft Defender, XProtect on macOS |
| Firewall | Controls which network traffic can come in and go out | Windows Defender Firewall |
| Backup | Copies files so they can be restored after a failure | File History, Time Machine, OneDrive backup |
| Disk clean-up | Removes temporary and unwanted files to free space | Windows Storage Sense |
| Compression | Packs files into a smaller archive | Built-in "Compress to ZIP file" |
| Software updater | Downloads and installs fixes | Windows Update, macOS Software Update |

The **firmware** (BIOS or UEFI) you met in Week 1 sits underneath all of this. It starts the computer and then hands over to the operating system.

### Application software

Application software is what most people mean by "programs" or "apps":

- **Productivity:** word processors, spreadsheets, presentations, email (Microsoft 365, Google Workspace).
- **Web browsers:** Edge, Chrome, Firefox, Safari. More and more applications now run *inside* the browser.
- **Communication:** Teams, Zoom, Slack.
- **Business systems:** payroll, accounting, customer records.
- **Specialist tools:** data analysis tools for data scientists; security monitoring tools for cyber security analysts.

Applications can be **installed** on the computer, or used as a **web app** through the browser (for example, Excel on the web). Week 6 explains the cloud services that make web apps possible.

### Software licences

You rarely *own* software. You buy a **licence**: permission to use it on certain terms.

| Licence type | What it means | Example |
|---|---|---|
| **Proprietary (commercial)** | Paid for. The source code is secret. | Microsoft Windows, Adobe Photoshop |
| **Subscription** | Paid monthly or yearly. It stops working if you stop paying. | Microsoft 365 |
| **Freeware** | Free to use, but the source code is secret | Zoom's free plan |
| **Open source** | Free to use, and the **source code** (the program's instructions) is public, so anyone can check or improve it | Linux, Firefox, LibreOffice |

Using software without a valid licence is illegal, and "free" copies from unofficial sites are a common way to spread malware.

### Updates and patches

Software contains mistakes, called **bugs**. Some bugs are **vulnerabilities**: weaknesses an attacker can use to get in. Software makers release **updates** (also called **patches**) to fix them.

- Installing updates quickly is one of the most effective security habits there is. "Patch applications" and "patch operating systems" are two of the Australian Cyber Security Centre's **Essential Eight** strategies, which you will meet in Week 6.
- Software that no longer receives updates is called **unsupported** or **end of life**. For example, Windows 10 reached end of support in October 2025. Using unsupported software is a security risk.

### See the software on your computer

Try this now. You will need it for the Build. Do not record user names or device names.

**Windows 11**

- Installed applications: **Settings > Apps > Installed apps**.
- Running programs and background processes: press **Ctrl + Shift + Esc** to open **Task Manager**, then choose **Processes**. *Apps* are things you opened; *background processes* include many system programs.
- Utilities: search the Start menu for **Windows Security** (antivirus and firewall), **Windows Update** and **Storage Sense**.

**macOS**

- Installed applications: open **Finder > Applications**.
- Running programs and processes: open **Activity Monitor** (search for it with Spotlight, **Cmd + Space**).
- Utilities: open **Finder > Applications > Utilities**, and **System Settings > General > Software Update**.

If Settings or Task Manager is blocked on a work laptop, use a home or library computer, or use what you can see in the Start menu or Applications folder.

::::::::::::::::::::::::::::::::::::: challenge

### Exercises

About 5 minutes. Answers are at the end.

1. Label each one system software or application software: (a) macOS; (b) Excel; (c) a printer driver; (d) Microsoft Defender; (e) Chrome; (f) a backup tool.
2. Your new webcam is not recognised. Which kind of system software is most likely missing?
3. What is the difference between freeware and open source software?
4. Why is it risky to keep using an operating system that has reached end of support?

:::::::::::::::: solution

### Answers

1. (a) system (operating system); (b) application; (c) system (driver); (d) system (utility); (e) application; (f) system (utility).
2. A device driver.
3. Both are free to use. Open source also makes its source code public, so anyone can inspect and improve it. Freeware keeps its code secret.
4. It no longer receives security updates, so newly found vulnerabilities are never fixed, and attackers can use them.

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## 3.2 Operating systems and file management {#section-3-2}

**Time:** about 35 minutes (25 minutes reading, 10 minutes exercises).


### What an operating system does

The **operating system (OS)** sits between the hardware and everything else. Applications never control the hardware directly; they ask the OS. The OS has six main jobs:

| Job | What it means | Example you can see |
|---|---|---|
| **Process management** | A running program is a **process**. The OS shares the CPU's cores between hundreds of processes, switching between them so fast they seem to run at once. This is **multitasking**. | Task Manager or Activity Monitor lists the processes. |
| **Memory management** | Gives each process its own part of RAM and stops processes reading each other's memory. When RAM is full, it moves some data out to storage. | The *Memory* graph in Task Manager. |
| **File management** | Organises storage into files and folders, and keeps track of where each file's bytes are on the drive. | File Explorer or Finder. |
| **Device management** | Uses drivers to control the keyboard, screen, printer, network card and other devices. | Plugging in a USB drive and seeing it appear. |
| **User management and security** | Keeps separate **user accounts**, checks passwords, and decides who may open which files. | The sign-in screen. |
| **User interface** | Gives people a way to use the computer. | The desktop, or a command line. |

### The kernel and the shell

The **kernel** is the core of the operating system. It is always running and does the low-level jobs: processes, memory and devices.

The **shell** is the part you talk to. It takes your instructions and passes them to the kernel. There are two kinds of interface:

- A **graphical user interface (GUI)** uses windows, icons, menus and a pointer. It is easy to learn.
- A **command-line interface (CLI)** uses typed commands. It takes longer to learn, but it is faster for repeated tasks, it can be **scripted** (saved and repeated automatically), and it works over a network on computers with no screen, such as servers.

Most servers, cloud systems and security tools are run from the command line. That is why cyber security and data science students learn it early. You will use one in [Section 3.3](#section-3-3).

### Common operating systems

| Operating system | Where it is used |
|---|---|
| **Windows** | Most office desktops and laptops |
| **macOS** | Apple computers |
| **Linux** | Most web servers, cloud systems and supercomputers; popular with security and data professionals. It is open source and comes in many versions, called **distributions** (Ubuntu, Debian, Alpine and others). |
| **Android** | Most smartphones (it is built on the Linux kernel) |
| **iOS / iPadOS** | iPhones and iPads |

### Files, folders and paths

A **file** is a named sequence of bytes (Week 2). A **folder** (also called a **directory**) holds files and other folders. Folders inside folders form a **tree**.

A **path** is the address of a file in the tree:

- **Windows:** `C:\Users\Olivia\Documents\budget.xlsx`. It starts with a drive letter, and the folders are separated by **backslashes** `\`.
- **macOS and Linux:** `/home/olivia/documents/budget.xlsx` on Linux, or `/Users/olivia/Documents/budget.xlsx` on a Mac. It starts at the **root** folder `/`, and the folders are separated by **forward slashes** `/`. On **Linux**, names are **case-sensitive**: `Budget.xlsx` and `budget.xlsx` are different files. (Windows and, normally, macOS treat them as the same file.)

There are two kinds of path:

- An **absolute path** starts from the top of the tree, for example `/home/olivia/documents/budget.xlsx`. It works from anywhere.
- A **relative path** starts from the folder you are in now. If you are in `/home/olivia`, the relative path `documents/budget.xlsx` points to the same file.

Two special names appear in relative paths:

- `.` means "this folder".
- `..` means "the folder one level up".

**Good file management** at work means:
- clear names, for example `2026-11_budget_v2.xlsx` rather than `final FINAL.xlsx`
- a sensible folder structure
- regular backups
- not saving sensitive files where everyone can open them

### File systems

A **file system** is the method the OS uses to organise and keep track of files on a drive.

| File system | Used by |
|---|---|
| **NTFS** | Windows |
| **APFS** | macOS |
| **ext4** | Linux |
| **exFAT**, **FAT32** | USB drives and SD cards, because almost every device can read them |

This is why a drive formatted on a Mac may not open on a Windows PC: each OS reads its own file system best.

### Users and permissions

An operating system keeps a separate **account** for each user. Each file has an **owner**, and **permissions** that say who may do what with it. On Linux and macOS there are three permissions:

| Permission | Letter | On a file it means | On a folder it means |
|---|---|---|---|
| Read | `r` | Open and look at the file | List what is in the folder |
| Write | `w` | Change or delete the file | Add or remove files in the folder |
| Execute | `x` | Run the file as a program | Go into the folder |

Each permission is set separately for three groups of people:
- the **owner (user)**
- the owner's **group** (for example, the HR team)
- **others** (everyone else)

Every system also has a powerful **administrator** account. On Linux it is called **root**. Root can read, change and delete anything. That power is why the [Concepts Bridge](#week-3-bridge) argues that people should use it as little as possible.

You will read and change permissions in Section 3.3.

::::::::::::::::::::::::::::::::::::: challenge

### Exercises

About 10 minutes. Answers are at the end.

1. Which OS job is happening in each case? (a) You type your password at the sign-in screen. (b) Spotify plays music while you write an email. (c) You plug in a printer and it works straight away. (d) A program is stopped from reading another program's memory.
2. Give two reasons why system administrators use a command line rather than a GUI.
3. You are in the folder `/home/jack`. Write the absolute path of the file that the relative path `reports/march.txt` points to.
4. You are in `/home/jack/reports`. Which folder does `..` point to?
5. On Linux, are `Report.txt` and `report.txt` the same file?

:::::::::::::::: solution

### Answers

1. (a) user management and security; (b) process management (multitasking); (c) device management (drivers); (d) memory management.
2. Any two of: it is faster for repeated tasks; commands can be saved and run automatically (scripted); it works on servers with no screen and over a network; it uses fewer resources.
3. `/home/jack/reports/march.txt`
4. `/home/jack`
5. No. Linux names are case-sensitive.

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## 3.3 The Linux command line {#section-3-3}

**Time:** about 45 minutes. Type every example yourself; that is how the commands stick.


### Start Linux in your browser

**JSLinux** runs a small, real Linux system (Alpine Linux) inside your web browser. There is nothing to install and no account.

1. Go to https://bellard.org/jslinux/.
2. In the first row of the table (**x86_64, Alpine Linux, Console**), choose **click here** in the *Startup Link* column.
3. Wait about 30 seconds. When you see the prompt `localhost:~#`, Linux is ready.
4. Click inside the black terminal window, and type.

**Four things to know about JSLinux:**

- **Everything is wiped when you close or reload the page.** Keep your notes (and your command log for the Build) in a separate document as you go.
- **To paste** into the terminal, right-click and choose **Paste**. Paste no more than about 15 lines at a time; JSLinux can drop characters from very long pastes. To copy, select text with the mouse, then right-click and choose **Copy**.
- **To upload a file** from your computer, click the **up arrow** below the terminal. The file is copied to your home folder.
- **You are logged in as `root`**, the all-powerful administrator. That is convenient for learning, but it is exactly what you should *not* do on a real system. The [Concepts Bridge](#week-3-bridge) explains why.

### How a command works

At the prompt you type a **command**, then press **Enter**. Most commands follow the same pattern:

```
command  -options  arguments
```

For example, `ls -l office` means: run the `ls` (list) command, with the `-l` (long) option, on the `office` folder. Commands and file names are **case-sensitive**, and spaces matter.

The prompt `localhost:~#` tells you three things:
- the computer's name is `localhost`
- you are in `~` (your **home folder**)
- `#` means you are root (normal users see `$`)

### Where am I? Moving around

| Command | What it does |
|---|---|
| `pwd` | **P**rint **w**orking **d**irectory: shows the folder you are in |
| `ls` | **L**i**s**t the files and folders here |
| `ls -l` | List in **long** form: permissions, owner, size and date |
| `cd folder` | **C**hange **d**irectory: move into `folder` |
| `cd ..` | Move up one level |
| `cd ~` or `cd` | Go back to your home folder |
| `clear` | Clear the screen |

Try it:

```
pwd
ls
```

You should see that you are in `/root` (root's home folder) and that a few example files are already there, such as `readme.txt`.

### Making and managing files

| Command | What it does | Example |
|---|---|---|
| `mkdir name` | Make a new folder | `mkdir office` |
| `mkdir -p a/b` | Make a folder and any folders above it that are missing | `mkdir -p office/hr` |
| `touch file` | Create an empty file | `touch office/hr/staff.txt` |
| `cp from to` | **C**o**p**y a file | `cp a.txt b.txt` |
| `mv from to` | **M**o**v**e a file, or rename it | `mv b.txt c.txt` |
| `rm file` | **R**e**m**ove (delete) a file | `rm c.txt` |

:::::::::::::::::::::::::::::::::::::::: callout

**Warning:** `rm` does not use a Recycle Bin. A deleted file is gone. On a real system, check twice before pressing Enter.

::::::::::::::::::::::::::::::::::::::::::::::::

Try it:

```
mkdir -p practice/drafts
touch practice/drafts/plan.txt
ls practice/drafts
mv practice/drafts/plan.txt practice/plan.txt
ls practice
```

### Looking inside files

| Command | What it does |
|---|---|
| `cat file` | Print the whole file to the screen |
| `head file` / `tail file` | Show the first or last 10 lines |
| `wc -l file` | **W**ord **c**ount with `-l`: count the **lines** |
| `grep word file` | Show only the lines that contain `word` |
| `grep -c word file` | **Count** the lines that contain `word` |
| `grep -i word file` | Ignore upper and lower case when searching |

`grep` is one of the most useful tools in cyber security and data work. With it, an analyst can pull a few important lines out of a log file with millions of lines.

### Redirection and pipes

Normally a command's output goes to the screen. You can send it somewhere else:

| Symbol | What it does | Example |
|---|---|---|
| `>` | Send the output to a file, **replacing** what was in it | `echo "Hello" > note.txt` |
| `>>` | Send the output to a file, **adding** to the end | `echo "Again" >> note.txt` |
| `\|` (pipe) | Send the output of one command **into** the next command | `grep ERROR app.log \| wc -l` |

`echo` simply prints the text you give it.

The **pipe** is what makes the command line powerful. Each command does one small job, and you join them together like building blocks. For example, `grep ERROR app.log | wc -l` means "find the lines containing ERROR, then count them".

Try it:

```
echo "Line one" > practice/note.txt
echo "Line two" >> practice/note.txt
cat practice/note.txt
grep two practice/note.txt
cat practice/note.txt | wc -l
```

### Reading and changing permissions

`ls -l` shows permissions at the start of each line:

```
-rw-r--r--    1 root     root            18 Nov 20 16:23 note.txt
```

Read the first ten characters like this:

| Characters | Meaning |
|---|---|
| `-` | A file. A `d` here would mean a directory (folder). |
| `rw-` | The **owner** can read and write. |
| `r--` | The **group** can only read. |
| `r--` | **Others** can only read. |

The next columns are the owner (`root`), the group (`root`), the size in bytes, the date and the name.

**Changing permissions with `chmod`.** Each permission has a number:

| Permission | Number |
|---|---|
| Read (`r`) | 4 |
| Write (`w`) | 2 |
| Execute (`x`) | 1 |

Add the numbers for each group, then write the three totals in the order owner, group, others:

| Setting | Owner | Group | Others | Typical use |
|---|---|---|---|---|
| `chmod 600 file` | read and write (6) | none (0) | none (0) | Private files, such as HR records |
| `chmod 640 file` | read and write (6) | read (4) | none (0) | Shared with your team only |
| `chmod 644 file` | read and write (6) | read (4) | read (4) | Public notices anyone may read |
| `chmod 755 file` | all (7) | read and execute (5) | read and execute (5) | Programs and folders others may use |

Try it:

```
chmod 600 practice/note.txt
ls -l practice
```

The line for `note.txt` should now start `-rw-------`.

:::::::::::::::::::::::::::::::::::::::: callout

**Note:** because you are root in JSLinux, you can still open the file whatever the permissions say. Root ignores permissions. On a real system, an ordinary user could not.

::::::::::::::::::::::::::::::::::::::::::::::::

### Getting help and seeing your history

- `ls --help` (and `--help` after most commands) prints the command's options. JSLinux does not include the `man` (manual) pages found on most Linux systems.
- `history` lists every command you have typed in this session, numbered. You will copy this into your command log for the Build.
- Press the **up arrow** key to bring back the last command, so you can edit it and run it again.

### Practice

About 10 minutes, in JSLinux. Answers are at the end.

1. In your home folder, make a folder called `test`, go into it, and show the full path of where you are.
2. Create a file `a.txt` that contains the line `apple`, then add a second line `banana`. Show the file.
3. Count the lines in `a.txt` with one command.
4. Copy `a.txt` to `b.txt`, then delete `a.txt`. List the folder to check.
5. Make `b.txt` readable and writable by its owner only. What do the first ten characters of `ls -l` show?
6. What does `grep -c an b.txt` print, and why?

#### Answers

1. `mkdir test`, then `cd test`, then `pwd`, which shows `/root/test`.
2. `echo "apple" > a.txt`, then `echo "banana" >> a.txt`, then `cat a.txt`.
3. `wc -l a.txt` (it shows `2 a.txt`).
4. `cp a.txt b.txt`, then `rm a.txt`, then `ls` (it shows only `b.txt`).
5. `chmod 600 b.txt`. `ls -l` shows `-rw-------`.
6. It prints `1`. Only the line `banana` contains the letters `an`; `apple` does not.

## Concepts Bridge: Least privilege {#week-3-bridge}

**Time:** about 30 minutes (12 minutes reading, 18 minutes activity).

### Why this matters

In Section 3.3 you worked as `root`, the user who can do anything. That is fine in a throwaway practice system. On a real system it is one of the most common causes of serious security incidents.

The **principle of least privilege** says:

:::::::::::::::::::::::::::::::::::::::: callout

Every person, and every program, should have only the access it needs to do its job, and no more, for no longer than needed.

::::::::::::::::::::::::::::::::::::::::::::::::

You will meet this idea in almost every cyber security unit, and data scientists meet it every time they ask for access to a dataset.

### The big idea: keys in an office

Think of an office building:

- The cleaner has a key to every floor but not to the safe.
- The HR officer has a key to the HR filing cabinet but not to the server room.
- Only the manager has the key to the safe.

If the cleaner's keys are stolen, the thief still cannot open the safe. **The damage is limited by what the stolen key could open.**

Computer accounts work the same way. If an attacker tricks someone into running malware, the malware gets **that person's** permissions:

- If the person was using an **ordinary account**, the malware can only reach that person's files.
- If the person was using an **administrator (root) account**, the malware can reach everything: it can turn off antivirus, read every user's files and hide itself.

### Least privilege in practice

| Where | What least privilege looks like |
|---|---|
| Your own computer | Use a standard account day to day. Only use an administrator account (or approve an administrator prompt) when you install software or change settings. |
| Files and folders | HR files are readable only by HR (`chmod 640` with the HR group, or `600`). Public notices can be read by everyone (`644`). |
| Phone apps | A torch app does not need your location or contacts. Deny the permissions an app does not need. |
| Data science | An analyst gets **read-only** access to the sales data, not the power to change or delete it, and no access to unrelated HR data. |
| Organisations | "Restrict administrative privileges" is one of the Australian Cyber Security Centre's **Essential Eight** strategies (Week 6). |

**For no longer than needed** matters too. A contractor's account should be switched off when the contract ends. Someone who changes team should lose access to their old team's files.

### Worked example: the invented office

The office in this week's Build has three folders. Here is a least-privilege plan for them:

| Folder | Who needs it | Owner | Group | Others | `chmod` |
|---|---|---|---|---|---|
| `hr` | HR staff only | read, write, enter | none | none | `700` (or `750` if the HR team shares a group) |
| `finance` | Finance staff; managers need to read | read, write, enter | read, enter | none | `750` |
| `public` | Everyone may read; only the office manager edits | read, write, enter | read, enter | read, enter | `755` |

These are **folders**, so each group that may use a folder also needs **execute** (`x`), which on a folder means "go into it" (Section 3.2). That is why folder numbers end in 7 or 5, where the same rules for a file would be 6 or 4 (for example `600`, `640`, `644`).

::::::::::::::::::::::::::::::::::::: challenge

### Activity (18 minutes)

1. **Your phone (8 minutes).** Open your phone's app permission settings:
   - Android: **Settings > Security and privacy > Privacy > Permission manager**. The menu names vary between brands.
   - iPhone: **Settings > Privacy & Security**.

   Look at **Location** and **Camera**. Find **two** apps that have a permission they do not seem to need. For each, write the kind of app (for example "a torch app"; you do not need to name it), the permission, and whether you would remove it and why. You do not have to change anything.
2. **An office plan (6 minutes).** A small accounting firm has these folders: `client_tax_returns`, `staff_rosters` and `marketing_images`. For each one, say who should be able to read it, who should be able to change it, and which `chmod` number you would use.
3. **Explain (4 minutes).** In two or three sentences, explain to a non-technical manager why staff should not use administrator accounts for email and web browsing.

:::::::::::::::: solution

### Model answer

1. Answers will vary. A good answer names a clear mismatch, for example "a calculator app with location access: remove it, because a calculator does not need to know where I am, and location data can be sold or leaked."
2. For example:

   | Folder | Read | Change | `chmod` |
   |---|---|---|---|
   | `client_tax_returns` | The accountants (owner and their group) | The accountants | `770`, so others get nothing. It holds sensitive personal and financial information. (`700` if only one person should use it.) |
   | `staff_rosters` | All staff | The office manager | `755` |
   | `marketing_images` | All staff | The marketing staff | `755`, or `775` if the marketing group needs to edit |

   (These are folders, so everyone who may use one also needs `x`. `775` gives the owner and group read, write and enter, and others read and enter. Answers that give the matching file numbers, such as `660`, `644` and `664`, with a note that they are for the files inside, are also fine.)
3. For example: "Email and websites are the most common way attackers get malware onto a computer. If staff browse with an administrator account, any malware they open gets full control of the computer and can switch off our protections. With a standard account, the damage is limited to that one person's files."

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## Practice task: Software audit and command-line lab {#week-3-practice}

:::::::::::::::::::::::::::::::::::::::: callout

#### Files for this task

Download single files here, or every course file at once in the [course files zip](data/course-files.zip). Worksheets download as plain text (`.txt`): open one in any text editor, and save your copy with the name the task gives.

- [week3_lab_worksheet.txt](files/week-3/week3_lab_worksheet.txt)
- [server.log](files/week-3/lab_files/server.log)

:::::::::::::::::::::::::::::::::::::::::::::::::::

**Time:** about 2 hours. This is your portfolio item for Week 3. Your tutor marks it at the end of the week.

### Goal

Audit the software on a real computer. Then use the Linux command line to set up the folders for an invented small office (Harbour Street Physio), search its server log for problems, and lock down its private files.

Work in the [worksheet](files/week-3/week3_lab_worksheet.txt). Save your copy as `week3_lab.md`. Any text editor works, or you can copy it into Word or Google Docs and save it as a PDF.

:::::::::::::::::::::::::::::::::::::::: callout

**Privacy.** In Part 1, do not record user names, device names or anything you would not want your tutor to see. The kind of software is enough; you do not need version numbers.

::::::::::::::::::::::::::::::::::::::::::::::::

### Part 1: software audit (about 30 minutes)

Use **"See the software on your computer"** in [Section 3.1](#section-3-1).

1. List **five application programs** on your computer, and say in a few words what each is for.
2. List **five pieces of system software**:
   - the operating system and its version
   - at least **two utilities** (for example antivirus, backup, firewall, updater)
   - any others you can find (for example a driver)

   Say in a few words what each one does.
3. Look at **Windows Update** or **Software Update**. Is the operating system up to date? Write yes, no or "can't tell", and one sentence on why updates matter.

### Part 2: command-line lab (about 60 minutes)

**Before you start:**

- **JSLinux is wiped when the page reloads.** Do the whole lab in one sitting, and copy your work into the worksheet before you close the tab.
- If something goes wrong, you can always start again from step 1.

#### Step 1: start Linux and load the log file

1. Start JSLinux as in [Section 3.3](#section-3-3) (x86_64 Alpine Linux, Console).
2. Load the office's log file, [`lab_files/server.log`](files/week-3/lab_files/server.log), in one of two ways:
   - **Upload (easiest):** download `server.log` from the Files box above to your computer. In JSLinux, click the **up arrow** below the terminal and choose the file. It is copied to your home folder.
   - **Paste:** JSLinux can drop characters if you paste too much at once, so paste in **two blocks**. Copy block 1, right-click in the terminal and choose **Paste**, and wait for the prompt `localhost:~#` to come back. Then do the same with block 2. Press **Enter** if the prompt does not come back.

**Block 1** (creates the file with the first 10 lines):

```
cat > server.log << 'END'
2026-11-02 08:01:12 INFO User olivia.thompson logged in
2026-11-02 08:03:40 ERROR Disk usage above 90 percent on /data
2026-11-02 08:15:05 WARNING Failed login for user admin
2026-11-02 08:15:09 WARNING Failed login for user admin
2026-11-02 08:15:14 WARNING Failed login for user admin
2026-11-02 08:20:31 INFO User jack.wilson logged in
2026-11-02 09:02:47 INFO Backup started
2026-11-02 09:44:18 ERROR Backup failed: storage device not found
2026-11-02 10:10:02 INFO User priya.nair logged in
2026-11-02 11:30:55 WARNING Failed login for user jack.wilson
END
```

**Block 2** (adds the last 10 lines; note the `>>`):

```
cat >> server.log << 'END'
2026-11-02 11:31:20 INFO User jack.wilson logged in
2026-11-02 12:05:33 INFO Software update installed: printer driver 4.2
2026-11-02 13:47:09 ERROR Printer offline: OFFICE-PRN-01
2026-11-02 14:22:41 WARNING Failed login for user admin
2026-11-02 14:22:46 WARNING Failed login for user admin
2026-11-02 15:00:00 INFO Backup started
2026-11-02 15:38:12 INFO Backup completed
2026-11-02 16:59:58 INFO User olivia.thompson logged out
2026-11-02 17:04:23 ERROR Antivirus definitions out of date
2026-11-02 17:30:00 INFO User jack.wilson logged out
END
```

3. Check it worked: `ls` should list `server.log`, and `wc -l server.log` should show `20 server.log`. If it shows fewer lines, type `rm server.log` and load it again.

#### Step 2: build the office folders

Using commands only:

1. Make a folder `office` with three folders inside it: `finance`, `hr` and `public`.
2. Create two empty files in `hr`: `staff_list.txt` and `leave_requests.txt`.
3. Create one empty file in `finance`: `budget_2026.txt`.
4. Create `public/notice.txt` containing the line `Office closed on 26 January`. Use `echo` and `>`.
5. Move `server.log` into the `office` folder.
6. Go into `office`, and list everything with `ls -R`. The `-R` option lists the folders inside too.

#### Step 3: copy, rename and delete

1. Copy `public/notice.txt` into `finance`.
2. Rename the copy in `finance` to `notice_copy.txt`.
3. Delete `finance/notice_copy.txt`.
4. Check with `ls finance` that only `budget_2026.txt` is left.

#### Step 4: investigate the server log

Run commands that answer these questions. Record each command **and** its answer in the worksheet.

1. How many lines does the log have?
2. Show only the `ERROR` lines.
3. How many `ERROR` lines are there?
4. How many failed logins were there? Search for `Failed login`.
5. How many of those failed logins were for the user `admin`?
6. Save all the `ERROR` lines into a new file called `errors.txt`, then show that file.

#### Step 5: lock down the files

1. Make both `hr` files readable and writable by their owner only.
2. Make `public/notice.txt` readable by everyone but writable only by its owner.
3. Show the result with `ls -l hr public`.
4. Take **one screenshot** of the `ls -l` output.
   - Windows: press **Windows + Shift + S**.
   - macOS: press **Cmd + Shift + 4**.

#### Step 6: save your command log

1. Type `history`.
2. Select the output with the mouse, right-click, choose **Copy**, and paste it into the worksheet.
3. Next to each command, write **one line** on what it did. You may leave out typing mistakes.

### Part 3: what the log tells you (about 15 minutes)

The office manager is not technical. In the worksheet, write **three short points** telling them what the log shows and what they should do. Think about:
- the repeated failed logins for `admin`
- the failed backup
- the out-of-date antivirus

### Part 4: reflection (about 15 minutes, including tidying)

Write **100 to 150 words**:

1. What did you find hardest about the command line, and what helped?
2. Why did you set the HR files to owner-only? Use the words **least privilege**.
3. Give one example of how a cyber security analyst or a data analyst could use `grep` at work.

### Check your work

- [ ] Part 1 lists five application programs and five pieces of system software (including two utilities), and says whether the computer is up to date.
- [ ] The folders and files from Step 2 exist, and `ls -R` shows them.
- [ ] Step 3 shows a copy, a rename and a delete.
- [ ] All six log questions in Step 4 have a command and an answer, and `errors.txt` was made.
- [ ] The permissions are set, and the screenshot shows `ls -l hr public`.
- [ ] The command log is pasted in, with one line per command.
- [ ] Part 3 has three points for the office manager.
- [ ] The reflection is 100 to 150 words and answers all three questions.

### How it is marked

Your tutor marks each criterion as **meets**, **partly** or **not yet**:

| Criterion | What the tutor looks for |
|---|---|
| Accurate | Software is sorted correctly. The commands work and give the right answers. The permissions are right. |
| Complete | Every item on the checklist is done. |
| Evidence | The command log and the screenshot show the work was done in the terminal. |
| Explanation | The command notes, the manager points and the reflection are in your own words. |

:::::::::::::::::::::::::::::::::::::: keypoints

- Each week has five blocks: Watch, Read & practise, Concepts Bridge, Build and Quiz.
- System software runs the computer; application software helps a person do a task.
- Installing updates quickly is one of the best security habits.
- The operating system manages the hardware, programs, files and users.
- A path is the address of a file in the folder tree.
- The command line is precise, repeatable and widely used in cyber security and data work.
- Permissions control who can read, write and run each file.
- Give every person and program only the access they need, and no more.
- grep and permissions are everyday tools for analysts.

::::::::::::::::::::::::::::::::::::::::::::::::
