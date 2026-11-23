---
title: 'Week 4: Algorithms and programming basics'
teaching: 141
exercises: 174
---

:::::::::::::::::::::::::::::::::::::: questions

- What will I learn in Week 4, and how should I spend my 6 hours?
- What is an algorithm, and how do I design one?
- What are the building blocks every program uses?
- How do searching algorithms compare?
- How does a CPU run a program, one instruction at a time?
- How does a program in a language like Python reach the CPU?
- Can I design and test an algorithm before any code is written?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Plan your study time for the week using the time plan.
- Break a problem into steps.
- Write an algorithm in pseudocode and as a flowchart.
- Use sequence, selection and repetition in pseudocode.
- Trace an algorithm with a trace table.
- Compare linear and binary search.
- Run and change a Little Man Computer program in a browser simulator.
- Explain compilers and interpreters.
- Write pseudocode and a flowchart, trace them, compare searches and change an LMC program.

::::::::::::::::::::::::::::::::::::::::::::::::

## Week 4 overview {#week-4-overview}

**Theme:** how to solve a problem step by step, describe the solution so a computer could follow it, and see how those steps become instructions the CPU runs. No programming language is needed.


### What you will be able to do this week

- Break a problem into steps and write an algorithm as pseudocode and as a flowchart.
- Use variables, selection (`IF`), repetition (loops) and functions in an algorithm.
- Check an algorithm by hand with a trace table, and compare linear and binary search.
- Run a short machine-level program on a model CPU and watch it work.

### Time plan (under 6 hours)

| Block | What you do | Time |
|---|---|---|
| Watch | 5 videos | 0 h 55 m |
| Read & practise | Sections 4.1, 4.2 and 4.3, with the exercises | 1 h 50 m |
| Concepts Bridge | [How code becomes something the CPU can run](#week-4-bridge) | 0 h 30 m |
| Build | [Algorithm design](#week-4-practice), your portfolio item for this week | 2 h 00 m |
| Quiz | Canvas quiz, 6 questions | 0 h 15 m |
| **Total** | | **5 h 30 m** |

Suggested order: video 1, then Section 4.1; videos 2 and 3, then Section 4.2; videos 4 and 5, then Section 4.3. Do the Bridge, Build and Quiz last.

**You do not need to install anything.** This week uses diagrams.net (flowcharts) and the Little Man Computer simulator. Both run in your browser with no account.

### Watch (0 h 55 m)

| # | Video | Length | Look for |
|---|---|---|---|
| 1 | CC#13 [Intro to Algorithms](https://www.youtube.com/watch?v=rL8X2mlNHPM&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye) | 11:44 | What makes a good algorithm, and why some are much faster than others. Do not worry about the "Big O" notation. |
| 2 | CC#12 [Programming Basics: Statements & Functions](https://www.youtube.com/watch?v=l26oaHV7D40&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye) | 11:57 | Variables, `if` statements, loops and functions, shown in a simple game. The code is just an example; you do not need to learn it. |
| 3 | CC#14 [Data Structures](https://www.youtube.com/watch?v=DuDz6B4cqVc&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye) | 10:07 | Arrays (lists) and their index numbers. Stop at trees and graphs if you are short of time. |
| 4 | CC#8 [Instructions & Programs](https://www.youtube.com/watch?v=zltgXvg6r3k&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye) | 10:36 | Instructions are stored in memory as numbers, just like data. |
| 5 | [Andy Dolinski] [LMC (Little Man Computer) -- Tutorial 1 -- What is it?](https://www.youtube.com/watch?v=kCyyZI1GgsQ) | 9:57 | The parts of the Little Man Computer and what each one is for. |

**Video total: about 54 minutes.**

### Read & practise (1 h 50 m)

| Order | Section | Time | What to do |
|---|---|---|---|
| 1 | [Section 4.1: Problem solving and algorithms](#section-4-1) | about 35 min | Read all of it. Open diagrams.net and try one shape. Do exercises 1 to 3. |
| 2 | [Section 4.2: The building blocks of programs](#section-4-2) | about 40 min | Read all of it. Do exercises 1 to 5. |
| 3 | [Section 4.3: Down to the hardware: the Little Man Computer](#section-4-3) | about 35 min | Run the add program in the simulator. Do exercises 1 to 5. |

Total: 35 + 40 + 35 = 110 minutes (1 h 50 m).

### Concepts Bridge (0 h 30 m)

Open [the Concepts Bridge](#week-4-bridge). It shows how a program written by a person (source code) is translated into the machine code you saw in the Little Man Computer, and explains the difference between a **compiler** and an **interpreter**.

### Build (2 h)

Open the [practice task](#week-4-practice). You will design an algorithm for a café loyalty card, draw it as a flowchart, test it with a trace table, race linear search against binary search, and change a Little Man Computer program. This is your portfolio item for this week.

### Quiz (0 h 15 m)

Take the Canvas quiz for Week 4 after you finish the Build. It has 6 questions drawn from a pool. It is marked automatically.

### Portfolio this week

Submit at the end of the week:

- `algorithm_design.md` (or a Word or PDF copy): your completed [worksheet](files/week-4/algorithm_design_worksheet.txt), with your flowchart image, LMC screenshot and reflection.

Your tutor marks the portfolio. The quiz is marked automatically.

### Optional

Nothing here is required. Try these if you want more.

- CC#11 [The First Programming Languages](https://www.youtube.com/watch?v=RU1u-js7db8&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye) (11:52): the history behind this week's Concepts Bridge.
- CC#16 [Software Engineering](https://www.youtube.com/watch?v=O753uuutqH8&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye) (10:35): how large programs are planned and built by teams.
- In the LMC simulator, choose **SELECT > add/subtr** to load a built-in example, and work out what it does.
- Learn the branch instructions (`BRA`, `BRZ`, `BRP`) from the simulator's **HELP** button, and write a program that outputs the larger of two numbers.

## 4.1 Problem solving and algorithms {#section-4-1}

**Time:** about 35 minutes (25 minutes reading, 10 minutes exercises).


### What an algorithm is

An **algorithm** is a precise, step-by-step set of instructions for solving a problem. A recipe is an algorithm; so are the steps for resetting a password or working out someone's pay.

A good algorithm is:

- **clear**: each step means only one thing;
- **ordered**: the steps happen in a set order;
- **finite**: it always finishes.

Computers can only follow algorithms. They cannot guess what you meant. A **program** is an algorithm written in a **programming language** (such as Python) so a computer can run it. This week you will design algorithms **without** a programming language, using pseudocode and flowcharts. In Introduction to Programming you will turn ideas like these into Python.

### Computational thinking

**Computational thinking** is a set of four habits for turning a messy problem into an algorithm.

| Habit | What it means | Example: planning a staff roster |
|---|---|---|
| **Decomposition** | Break the problem into smaller parts | Collect availability; count shifts; assign people; check the rules; publish |
| **Pattern recognition** | Spot what repeats or is similar | Every weekday needs the same shifts |
| **Abstraction** | Keep only the details that matter, and ignore the rest | A person's availability matters; their favourite colour does not |
| **Algorithm design** | Write the steps in order | "For each shift, choose an available person with the fewest shifts so far" |

Data scientists use these habits to plan an analysis. Cyber security analysts use them to plan how to investigate an incident.

### Writing algorithms as pseudocode

**Pseudocode** is structured plain English that looks a little like code. It has no strict rules, but this course uses the keywords below, written in capitals, so everyone's pseudocode looks alike.

| Keyword | What it does | Example |
|---|---|---|
| `INPUT` | Get a value from the user | `INPUT hours` |
| `OUTPUT` | Show a result | `OUTPUT "Total: ", total` |
| `SET ... TO` | Store a value in a variable | `SET pay TO hours * rate` |
| `IF ... THEN ... ELSE ... END IF` | Choose between two paths | see below |
| `WHILE ... END WHILE` | Repeat while a condition is true | see Section 4.2 |
| `FOR EACH ... IN ... END FOR` | Repeat once for every item in a list | see Section 4.2 |
| `FUNCTION ... END FUNCTION`, `RETURN` | A named, reusable set of steps | see Section 4.2 |

Indent the steps inside an `IF`, a loop or a function, so the structure is easy to see.

**Example: a parking fee.** Parking costs $3 an hour, with a daily maximum of $15.

```
INPUT hours
SET fee TO hours * 3
IF fee > 15 THEN
    SET fee TO 15
END IF
OUTPUT "Fee: $", fee
```

### Drawing algorithms as flowcharts

A **flowchart** shows the same algorithm as a diagram. Each kind of step has its own shape, and arrows show the order.

| Shape | Name | Used for |
|---|---|---|
| Rounded rectangle (oval) | **Terminator** | Start and End |
| Parallelogram | **Input / output** | `INPUT` and `OUTPUT` |
| Rectangle | **Process** | Calculations and `SET` |
| Diamond | **Decision** | A yes/no question; it has two arrows out, labelled Yes and No |
| Arrow | **Flow line** | The order of the steps |

Here is the parking fee as a flowchart:

```
        ( Start )
            |
     / INPUT hours /
            |
  [ SET fee TO hours * 3 ]
            |
      < fee > 15 ? > --Yes--> [ SET fee TO 15 ]
            |                        |
            No                       |
            |<-----------------------+
     / OUTPUT fee /
            |
         ( End )
```

**Making flowcharts in diagrams.net.** **diagrams.net** (https://app.diagrams.net/) is a free diagram tool that runs in your browser, with no account.

1. Open it. A blank page appears. If you are asked where to save, choose **Device** or **Decide later**.
2. Open the shapes panel, search for **flowchart**, and drag shapes onto the page.
3. Double-click a shape to type in it.
4. Hover over a shape and drag one of its small arrows to connect it to the next shape.
5. To save a picture, use the menu: **File > Export as > PNG**. In the simple layout, the menu is under the **⋯** button.

You can also draw flowcharts by hand and photograph them.

::::::::::::::::::::::::::::::::::::: challenge

### Exercises

About 10 minutes. Answers are at the end.

1. Use decomposition to break "organise a team lunch" into four smaller steps.
2. Which flowchart shape would you use for: (a) `INPUT age`; (b) "Is age 18 or over?"; (c) `SET total TO total + price`; (d) the end of the algorithm?
3. Write pseudocode that asks for a temperature in Celsius and outputs "Hot" if it is over 30, and "Not hot" otherwise.

:::::::::::::::: solution

### Answers

1. For example: find out who is coming; choose a place that suits everyone's diet; book a table; tell everyone the time and place.
2. (a) parallelogram (input/output); (b) diamond (decision); (c) rectangle (process); (d) rounded rectangle (terminator).
3. For example:

   ```
   INPUT celsius
   IF celsius > 30 THEN
       OUTPUT "Hot"
   ELSE
       OUTPUT "Not hot"
   END IF
   ```

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## 4.2 The building blocks of programs {#section-4-2}

**Time:** about 40 minutes (25 minutes reading, 15 minutes exercises).


### Variables

A **variable** is a named place that stores a value, such as `total` or `stamps`. Think of a labelled box: you can put a value in, look at it, and replace it.

```
SET total TO 0
SET total TO total + 5
```

After these two lines, `total` holds 5. The second line means "work out `total + 5`, then put the answer back into `total`".

Choose names that say what the value is (`hours_worked`, not `x`). Each variable holds one type of data, the types you met in Week 2: integer, float, text or Boolean.

### Sequence, selection and repetition

Every algorithm, however large, is built from just three structures.

**1. Sequence:** steps that run one after another, in order.

**2. Selection:** choosing a path with `IF`. The condition is a **Boolean** test (true or false), like the logic gates in Week 2.

```
IF age >= 18 THEN
    OUTPUT "Adult ticket"
ELSE
    OUTPUT "Child ticket"
END IF
```

**3. Repetition** (also called **iteration** or a **loop**): doing steps again and again.

- A **condition-controlled** loop repeats **while** something is true:

  ```
  SET attempts TO 0
  SET correct TO false
  WHILE correct = false AND attempts < 3
      INPUT password
      SET attempts TO attempts + 1
      IF password = stored_password THEN
          SET correct TO true
      END IF
  END WHILE
  ```

  This is how a login stops after three wrong tries.
- A **count-controlled** loop repeats once for **each** item:

  ```
  FOR EACH price IN prices
      SET total TO total + price
  END FOR
  ```

### Functions

A **function** is a named set of steps that you can use again and again. It can take values in (called **parameters**) and give a value back with `RETURN`.

```
FUNCTION gst(amount)
    RETURN amount * 0.1
END FUNCTION

SET tax TO gst(250)
```

Here `tax` becomes 25. Functions keep algorithms short and tidy. You write the steps once, give them a clear name, and **call** them whenever you need them. You can also fix a mistake in one place.

### Basic data structures

A **data structure** is a way of organising several values together.

| Structure | What it is | Example |
|---|---|---|
| **List** (or **array**) | Values in order, each with a numbered position called an **index** | `names = ["Ahmed", "Brown", "Chen"]`. In this course, position 1 is `"Ahmed"` (many programming languages start counting at 0). |
| **Record** | One item with several named fields | A customer: name, email, stamps |
| **Table** | Many records with the same fields: rows and columns | A spreadsheet of customers |
| **Dictionary** (or **map**) | Values looked up by a **key** instead of a position | `"Olivia" → 7 stamps`, `"Jack" → 2 stamps` |

Data scientists spend much of their time choosing and reshaping data structures, and Introduction to Programming covers Python's versions of each.

### Checking an algorithm with a trace table

A **trace table** tracks the value of each variable, step by step, as you work through an algorithm by hand. It is how you find mistakes before any code is written.

**Example:** total the list of prices `[4, 5, 5]`.

```
SET total TO 0
FOR EACH price IN prices
    SET total TO total + price
END FOR
OUTPUT total
```

| Step | price | total | Output |
|---|---|---|---|
| Start | – | 0 | |
| Loop 1 | 4 | 4 | |
| Loop 2 | 5 | 9 | |
| Loop 3 | 5 | 14 | |
| End | | | 14 |

Choose **test cases** that check the tricky parts too: an empty list, a value right on a boundary (exactly 15 in the parking example), or the moment a rule changes.

### Searching: linear and binary search

Searching is one of the most common jobs a computer does. There are two classic algorithms.

**Linear search:** check each item in turn, from the start, until you find the target or reach the end.

- It works on **any** list, sorted or not.
- In a list of 1,000 items it may take up to **1,000** checks.

**Binary search:** only for a **sorted** list.

1. Look at the **middle** item. If the list has an even number of items, use the left one of the two middle items.
2. If it is the target, stop.
3. If the target comes **before** it, throw away the right half. If the target comes **after** it, throw away the left half.
4. Repeat on the half that is left, until you find the target or nothing is left.

Each check halves what is left, so binary search is very fast on large lists:

| Items in the list | Most checks, linear search | Most checks, binary search |
|---|---|---|
| 16 | 16 | 5 |
| 1,000 | 1,000 | 10 |
| 1,000,000 | 1,000,000 | 20 |

**Example:** find **Chen** in this sorted list of 8 names, using binary search:

| Position | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Name | Ahmed | Brown | Chen | Davis | Evans | Garcia | Huang | Jones |

1. Positions 1 to 8. The middle is position 4 (Davis). Chen comes before Davis, so keep positions 1 to 3.
2. The middle of 1 to 3 is position 2 (Brown). Chen comes after Brown, so keep position 3.
3. Position 3 is Chen. **Found in 3 checks.** Linear search would also take 3 checks here, because Chen is near the start.

The trade-off: binary search needs the list to be **sorted** first, and sorting takes work. For a list you search many times, it is worth it.

::::::::::::::::::::::::::::::::::::: challenge

### Exercises

About 15 minutes. Answers are at the end.

1. Which structure (sequence, selection or repetition) does each describe? (a) "Repeat for every invoice." (b) "If the invoice is overdue, send a reminder." (c) "Open the file, then read the first line."
2. Complete a trace table for this algorithm with the list `[3, 8, 2]`:

   ```
   SET biggest TO 0
   FOR EACH n IN numbers
       IF n > biggest THEN
           SET biggest TO n
       END IF
   END FOR
   OUTPUT biggest
   ```

3. Write a function `area(width, height)` that returns the area of a rectangle, and use it to set `room` to the area of a 4 × 5 room.
4. Using binary search on the 8 names above, how many checks does it take to find **Huang**? List the names you check.
5. Why can't binary search be used on an unsorted list?

:::::::::::::::: solution

### Answers

1. (a) repetition; (b) selection; (c) sequence.
2. Trace table:

   | Step | n | biggest | Output |
   |---|---|---|---|
   | Start | – | 0 | |
   | Loop 1 | 3 | 3 | |
   | Loop 2 | 8 | 8 | |
   | Loop 3 | 2 | 8 | |
   | End | | | 8 |

3. For example:

   ```
   FUNCTION area(width, height)
       RETURN width * height
   END FUNCTION

   SET room TO area(4, 5)
   ```

   `room` is 20.
4. 3 checks: Davis (position 4), then Garcia (position 6, the middle of 5 to 8), then Huang (position 7).
5. Binary search decides which half to throw away by comparing with the middle item. That only works if everything before the middle is smaller and everything after is larger, which is true only for a sorted list.

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## 4.3 Down to the hardware: the Little Man Computer {#section-4-3}

**Time:** about 35 minutes (15 minutes reading, 20 minutes in the simulator).


### From algorithm to machine instructions

In Week 1 you learned that the CPU repeats the **fetch-decode-execute** cycle. But what exactly does it fetch? The answer is **machine instructions**: very small steps such as "load a number", "add a number" or "store a number". Each is stored in memory as a number.

Your pseudocode in Sections 4.1 and 4.2 had big steps like `FOR EACH price IN prices`. A real CPU cannot do that in one go. Every big step must be broken down into many tiny machine instructions. The [Concepts Bridge](#week-4-bridge) explains how that translation happens. In this section you will write the tiny instructions yourself.

### The Little Man Computer

The **Little Man Computer (LMC)** is a simple model of a CPU, made for teaching. It works like a real computer, but it has only:

- **100 memory locations** (called **mailboxes**), numbered 00 to 99, each holding a three-digit number;
- an **accumulator**: a single register where all the arithmetic happens;
- a **program counter**: the register that holds the address of the next instruction;
- an **instruction register** and an **address register**, which hold the instruction being worked on and the mailbox it uses;
- an **INPUT** box and an **OUTPUT** box.

You will use Peter Higginson's free online LMC simulator, https://peterhigginson.co.uk/lmc/. It runs in your browser, with no account.

### The instruction set

The LMC understands only a handful of instructions. Each one has a short name called a **mnemonic**. Writing programs with mnemonics is called **assembly language**.

| Mnemonic | Machine code | What it does |
|---|---|---|
| `INP` | 901 | Take a number from the INPUT box and put it in the accumulator |
| `OUT` | 902 | Copy the accumulator to the OUTPUT box |
| `STA x` | 3xx | **St**ore the **a**ccumulator into mailbox `x` |
| `LDA x` | 5xx | **L**oa**d** the number in mailbox `x` into the **a**ccumulator |
| `ADD x` | 1xx | Add the number in mailbox `x` to the accumulator |
| `SUB x` | 2xx | Subtract the number in mailbox `x` from the accumulator |
| `HLT` | 000 | Halt: stop the program |
| `DAT` | – | Not an instruction: it reserves a mailbox to hold data |

(There are also three **branch** instructions, `BRA`, `BRZ` and `BRP`, which jump to another instruction. They make selection and loops possible. They are optional this week.)

A **label** is a name you give to a mailbox, such as `FIRST`, so you do not have to work out its number. The simulator works out the numbers for you when it **assembles** the program, that is, turns the mnemonics into machine code.

### Reading the add program

This program adds two numbers. Download it as [`add.lmc`](files/lmc/add.lmc).

```
        INP
        STA FIRST
        INP
        ADD FIRST
        OUT
        HLT
FIRST   DAT
```

Read it as a sequence:

| Line | Instruction | What happens |
|---|---|---|
| 1 | `INP` | Read the first number into the accumulator |
| 2 | `STA FIRST` | Store it in the mailbox labelled `FIRST`, so it is not lost |
| 3 | `INP` | Read the second number into the accumulator |
| 4 | `ADD FIRST` | Add the first number to it |
| 5 | `OUT` | Output the answer |
| 6 | `HLT` | Stop |
| 7 | `FIRST DAT` | Mailbox 06 is reserved for the first number |

When assembled, the program becomes these numbers in mailboxes 00 to 06: `901 306 901 106 902 000 000`. That is the machine code. `306` means "store (3) into mailbox 06", and `106` means "add (1) mailbox 06".

Compare it with pseudocode: four lines of pseudocode (`INPUT a`, `INPUT b`, `SET total TO a + b`, `OUTPUT total`) became six machine instructions, plus a mailbox. Real programs become millions of instructions.

### Running it in the simulator

1. Open https://peterhigginson.co.uk/lmc/.
2. Click in the **Assembly Language Code** box on the left and type (or paste) the add program. Use spaces to line up the columns; upper-case letters are safest.
3. **Submit** and **Cancel** buttons appear under the code box. Click **Submit**. The program is assembled: the machine code appears in mailboxes 00 to 06.
4. Click **RUN**. The simulator animates each fetch-decode-execute cycle. Click **>>** a few times to speed it up, or **<<** to slow it down.
5. When the message says **INPUT required**, click in the **INPUT** box, type `7` and press **Enter**. Do the same with `5` when asked again.
6. Watch the **accumulator**, the **program counter** and the mailboxes change. The answer `12` appears in the **OUTPUT** box, and the message says the program has **HALTED**.
7. To step through one instruction at a time, use **STEP** instead of **RUN**. To start again, click **RESET**.

As it runs, notice the message at the bottom: **FETCH CYCLE** (get the instruction, add 1 to the program counter), then the execute step. This is the cycle from Week 1, made visible.

::::::::::::::::::::::::::::::::::::: challenge

### Exercises

About 10 minutes, using the simulator. Answers are at the end.

1. Run the add program with the inputs 20 and 22. What is the output?
2. After the program halts, which mailbox holds the first number you typed?
3. What is the program counter's value just after the `HLT` instruction is fetched, and why?
4. What machine code would `SUB FIRST` become, if `FIRST` is mailbox 06?
5. Predict the output of this program with the input 6, then check it in the simulator:

   ```
           INP
           STA A
           ADD A
           OUT
           HLT
   A       DAT
   ```

:::::::::::::::: solution

### Answers

1. 42.
2. Mailbox 06, the one labelled `FIRST`.
3. 06. During the fetch cycle the program counter goes up by 1, ready for the next instruction, so after fetching the `HLT` in mailbox 05 it holds 06. (Accept 6.)
4. 206 (2 for subtract, 06 for the mailbox).
5. 12. It stores 6 in A, then adds A to the accumulator (which still holds 6), so it outputs 6 + 6. The program doubles any number.

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## Concepts Bridge: How code becomes something the CPU can run {#week-4-bridge}

**Time:** about 30 minutes (15 minutes reading, 15 minutes activity).

### Why this matters

In Section 4.3 you wrote instructions so simple that the CPU could run them almost directly. Real software is written in languages such as Python, Java or C, which people can read. Something has to translate between the two. Knowing how this works explains:

- why Python programs need Python installed to run, while a downloaded `.exe` program does not;
- why cyber security analysts sometimes study machine code, to find out what a suspicious program really does when nobody has its source code;
- why the same program may need a different version for Windows, macOS or a phone.

### The big idea: levels of language

| Level | Example | Who reads it |
|---|---|---|
| **High-level language** | Python: `total = price * 2` | People. It looks a little like English and maths. |
| **Assembly language** | LMC: `LDA PRICE`, `ADD PRICE`, `STA TOTAL` | Specialists. One line per machine instruction, using mnemonics. |
| **Machine code** | `510 110 311` | The CPU. Only numbers (in a real computer, binary). |

One line of a high-level language usually becomes **many** machine instructions. The program a person writes is called **source code**.

Each kind of CPU has its own machine code. The CPU in most Windows laptops (x86) and the CPU in a phone or recent Mac (ARM) speak different "languages". That is why software is made in separate versions.

### Two ways to translate: compilers and interpreters

**A compiler** translates the **whole program** into machine code **before** it runs, and saves the result as a new file, such as an `.exe`.

- It is like translating a whole book into English once, then printing it. Readers never need the translator again.
- The finished program runs fast, and the user does not need the source code or the compiler.
- If you change the source code, you must compile it again.
- Examples: C, C++, Rust, Go.

**An interpreter** translates and runs the program **one statement at a time, every time it runs**.

- It is like a live interpreter at a meeting, translating each sentence as it is spoken.
- It is easy to test small changes straight away, but it is usually slower, and the user needs the interpreter installed.
- Examples: Python, JavaScript (in your web browser), PHP.

Some languages use a mix. Java and C#, for example, compile to an in-between form that a "virtual machine" then runs. You do not need the details for this course.

**An assembler** is the simplest translator of all: it turns assembly language into machine code, one line to one instruction. When you clicked **Submit** in the LMC simulator, an assembler turned `STA FIRST` into `306`.

### Worked example

This Python line:

```
total = price + price
```

could become these LMC instructions:

```
        LDA PRICE      load price into the accumulator
        ADD PRICE      add price again
        STA TOTAL      store the result in total
```

which the assembler turns into machine code, if `PRICE` is mailbox 10 and `TOTAL` is mailbox 11:

```
510 110 311
```

One readable line became three instructions, then three numbers.

::::::::::::::::::::::::::::::::::::: challenge

### Activity (15 minutes)

1. Sort these into **compiled** or **interpreted**, using the examples above: (a) a Python script (`.py` file); (b) a game you download as an `.exe`; (c) JavaScript on a website.
2. In three or four sentences, explain to a friend why you need Python installed to run a `.py` file, but you can run most `.exe` programs straight away.
3. Write LMC instructions for the Python line `total = price - discount`. Use the labels `PRICE`, `DISCOUNT` and `TOTAL`. Then give the machine code, if `PRICE` is mailbox 10, `DISCOUNT` is 11 and `TOTAL` is 12.

:::::::::::::::: solution

### Model answer

1. (a) interpreted; (b) compiled; (c) interpreted.
2. For example: "A `.py` file is source code. It has to be translated each time it runs, and the program that does that translating, the Python interpreter, must be on your computer. An `.exe` was compiled before it was given to you. It is already machine code that your CPU can run, so no translator is needed."
3. Assembly and machine code:

   ```
           LDA PRICE
           SUB DISCOUNT
           STA TOTAL
   ```

   The machine code is `510 211 312`.

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## Practice task: Algorithm design {#week-4-practice}

:::::::::::::::::::::::::::::::::::::::: callout

#### Files for this task

Download single files here, or every course file at once in the [course files zip](data/course-files.zip). Worksheets download as plain text (`.txt`): open one in any text editor, and save your copy with the name the task gives.

- [algorithm_design_worksheet.txt](files/week-4/algorithm_design_worksheet.txt)

:::::::::::::::::::::::::::::::::::::::::::::::::::

**Time:** about 2 hours. This is your portfolio item for Week 4. Your tutor marks it at the end of the week.

### Goal

Design, draw and test an algorithm for a real business rule. Then compare two search algorithms, and change a machine-level program.

Work in the [worksheet](files/week-4/algorithm_design_worksheet.txt). Save your copy as `algorithm_design.md`. Any text editor works, or you can copy it into Word or Google Docs and save it as a PDF.

### The problem: the Bean There café loyalty card

The Bean There café (an invented business) wants an algorithm for its loyalty card. The rules are:

- A coffee costs **$5.00**. On **Tuesdays** it costs **$4.00**.
- Each coffee the customer **pays for** earns **one stamp**.
- When the card already has **9 stamps**, the next coffee is **free**, and the card goes back to **0 stamps**. A free coffee does not earn a stamp.
- The algorithm is given the customer's **starting number of stamps** and a **list of the days** they buy a coffee, one coffee per day in the list.
- It must output a message for each free coffee, then the **total amount paid** and the **number of stamps left** on the card.

### Part 1: pseudocode (about 30 minutes)

1. **Decompose** the problem. List three or four smaller parts.
2. Write the algorithm in pseudocode, using the keywords from [Section 4.1](#section-4-1). It must use:
   - at least two **variables** (for example `stamps` and `total`);
   - a **loop** over the list of days;
   - an **IF** decision;
   - a **function** `price_for(day)` that returns the price for a given day.

### Part 2: flowchart (about 25 minutes)

Draw the same algorithm as a flowchart in **diagrams.net** (https://app.diagrams.net/), or by hand.

- Use the correct shapes: terminator, input/output, process and decision.
- Label the Yes and No arrows from each decision.
- Show the loop with an arrow that goes back up.

Export it as a PNG (**File > Export as > PNG**) or photograph it, and add it to the worksheet. You may show the `price_for` function as a single process box, "work out price for day".

### Part 3: trace tables (about 25 minutes)

Test your pseudocode by hand with the two test cases below. Fill in a trace table for each, showing `day`, `price`, `stamps`, `total` and any output on every pass of the loop.

| Test | Starting stamps | Days |
|---|---|---|
| 1 | 0 | Monday, Tuesday, Wednesday |
| 2 | 7 | Tuesday, Wednesday, Thursday, Friday |

If your trace shows a result that breaks the café's rules, fix your pseudocode and trace it again. Say what you changed.

### Part 4: linear search compared with binary search (about 15 minutes)

Here is a **sorted** list of 16 customer surnames:

| Position | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Name | Ahmed | Brown | Chen | Davis | Evans | Garcia | Huang | Jones |

| Position | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|
| Name | Kelly | Lee | Martin | Nguyen | Patel | Smith | Taylor | Wilson |

For **Patel** and for **Brown**:

1. Count the checks that **linear search** takes.
2. Use **binary search**, following the steps in [Section 4.2](#section-4-2). Remember: with an even number of items, the middle is the left one of the two middle items. List each name you check, and count the checks.
3. In two or three sentences: which search was faster for each name, and why is binary search still the better choice for a long, sorted list?

### Part 5: change a Little Man Computer program (about 15 minutes)

1. Open the [add program](files/lmc/add.lmc) in the LMC simulator (https://peterhigginson.co.uk/lmc/), as in [Section 4.3](#section-4-3), and run it once with 7 and 5 to check it outputs 12.
2. Change it so it **subtracts** the second number from the first. Hint: `SUB` takes away a mailbox's value from the accumulator, so the first number must be in the accumulator and the second number in a mailbox. You will need a second `DAT` mailbox.
3. Run your program with **9 and 4** (expected output 5) and with **3 and 9** (expected output −6).
4. Paste your program into the worksheet, and take **one screenshot** after the 3 and 9 run, showing the output.

### Part 6: reflection (about 10 minutes, plus tidying)

Write **100 to 150 words**:

1. Did your trace tables find a mistake? If so, what was it? If not, how did you check carefully?
2. What surprised you about how many machine instructions a simple task needs?
3. How might you use algorithm design (decomposition, pseudocode, trace tables) in cyber security or data science?

### Check your work

- [ ] The decomposition lists three or four parts.
- [ ] The pseudocode uses variables, a loop, an IF and the `price_for` function, and follows the café's rules.
- [ ] The flowchart uses the correct shapes, labels Yes and No, and shows the loop.
- [ ] Both trace tables are complete, with the right totals and stamps.
- [ ] Both searches show the checks for Patel and Brown, with a short comparison.
- [ ] The LMC subtract program is pasted in, gives 5 and −6, and the screenshot shows −6.
- [ ] The reflection is 100 to 150 words and answers all three questions.

### How it is marked

Your tutor marks each criterion as **meets**, **partly** or **not yet**:

| Criterion | What the tutor looks for |
|---|---|
| Accurate | The algorithm follows the rules. The traces, search counts and LMC output are correct. |
| Complete | Every item on the checklist is done. |
| Evidence | The trace tables, flowchart image and LMC screenshot are included. |
| Explanation | The search comparison and the reflection are in your own words. |

:::::::::::::::::::::::::::::::::::::: keypoints

- Each week has five blocks: Watch, Read & practise, Concepts Bridge, Build and Quiz.
- An algorithm is a precise, step-by-step solution.
- Pseudocode and flowcharts let you plan before you code.
- Every program is built from sequence, selection and repetition.
- Binary search is much faster, but only works on sorted data.
- Each instruction is fetched, decoded and executed in turn.
- Real programs are made of many simple instructions like these.
- Compilers and interpreters translate code into instructions the CPU can run.
- Test an algorithm by hand with a trace table before you trust it.

::::::::::::::::::::::::::::::::::::::::::::::::
