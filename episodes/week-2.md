---
title: 'Week 2: Data representation and logic'
teaching: 137
exercises: 178
---

:::::::::::::::::::::::::::::::::::::: questions

- What will I learn in Week 2, and how should I spend my 6 hours?
- Why do computers use binary?
- How do I convert between decimal, binary and hexadecimal?
- How are text, colours and whole files stored as numbers?
- How can simple on-off switches make decisions and add numbers?
- Why does a 1 TB drive show less than 1,000 GB?
- Can I read data the way a computer stores it?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Plan your study time for the week using the time plan.
- Convert numbers between decimal, binary and hexadecimal.
- Use ASCII and Unicode to encode text.
- Read RGB colour codes.
- Identify a file by its signature in a hex viewer.
- Complete truth tables for AND, OR, NOT and XOR.
- Build a half adder in a logic simulator.
- Convert between storage units and work out download times.
- Convert numbers, decode a hex message, unmask a disguised file and build a half adder.

::::::::::::::::::::::::::::::::::::::::::::::::

## Week 2 overview {#week-2-overview}

**Theme:** how a computer stores numbers, text, pictures and files using only 0s and 1s, and how simple logic gates do arithmetic.


### What you will be able to do this week

- Convert numbers between decimal, binary and hexadecimal.
- Explain how text, colours and images are stored as numbers.
- Tell a file's real type from its signature, not just its name.
- Build a simple circuit from logic gates that adds two bits.

### Time plan (under 6 hours)

| Block | What you do | Time |
|---|---|---|
| Watch | 4 videos | 0 h 45 m |
| Read & practise | Sections 2.1, 2.2 and 2.3, with the exercises | 2 h 00 m |
| Concepts Bridge | [Bits, bytes and units](#week-2-bridge) | 0 h 30 m |
| Build | [Data detective](#week-2-practice), your portfolio item for this week | 2 h 00 m |
| Quiz | Canvas quiz, 6 questions | 0 h 15 m |
| **Total** | | **5 h 30 m** |

Suggested order: videos 1 and 2, then Section 2.1; video 3, then Section 2.2; video 4, then Section 2.3. Do the Bridge, Build and Quiz last.

**You do not need to install anything.** This week uses two free browser tools, HexEd.it and CircuitVerse. Neither needs an account.

### Watch (0 h 45 m)

| # | Video | Length | Look for |
|---|---|---|---|
| 1 | CC#4 [Representing Numbers and Letters with Binary](https://www.youtube.com/watch?v=1GSjbWt0c9M&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye) | 10:46 | How place value works in binary, and how letters become numbers (ASCII, Unicode). |
| 2 | [Corey Schafer] [Understanding Binary, Hexadecimal, Decimal (Base-10), and more](https://www.youtube.com/watch?v=ZL-LhaaMTTE) | 10:44 | Why one hex digit stands for four bits. You can skip any part on octal (base 8). |
| 3 | CC#20 [Files & File Systems](https://www.youtube.com/watch?v=KN8YgJnShPM&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye) | 12:03 | A file is just bytes. How text, sound and image files are laid out, and what the start of a file (the header) is for. |
| 4 | CC#3 [Boolean Logic & Logic Gates](https://www.youtube.com/watch?v=gI-qXk7XojA&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye) | 10:07 | The AND, OR, NOT and XOR gates and their truth tables. You do not need the transistor wiring details. |

**Video total: about 44 minutes.**

### Read & practise (2 h 00 m)

Read each section and do its exercises. Have paper and a pen ready. The answers are at the end of each section.

| Order | Section | Time | What to do |
|---|---|---|---|
| 1 | [Section 2.1: Binary and hexadecimal](#section-2-1) | about 45 min | Read all of it. Do exercises 1 to 6. |
| 2 | [Section 2.2: Text, images and files](#section-2-2) | about 40 min | Read all of it. Open `file_a.png` in HexEd.it. Do exercises 1 to 6. |
| 3 | [Section 2.3: Logic and logic gates](#section-2-3) | about 35 min | Read all of it. Build one AND gate in CircuitVerse. Do exercises 1 to 4. |

Total: 45 + 40 + 35 = 120 minutes (2 h 00 m).

### Concepts Bridge (0 h 30 m)

Open [the Concepts Bridge](#week-2-bridge). It answers two everyday puzzles: why a new "1 TB" drive shows only about 931 GB, and why a "50 megabit" internet connection does not download 50 megabytes a second.

### Build (2 h)

Open the [practice task](#week-2-practice). You will convert numbers, decode a hidden message, find a disguised file, explain colour codes and build a half adder. This is your portfolio item for this week.

### Quiz (0 h 15 m)

Take the Canvas quiz for Week 2 after you finish the Build. It has 6 questions drawn from a pool. It is marked automatically.

### Portfolio this week

Submit at the end of the week:

- `data_detective.md` (or a Word or PDF copy): your completed [worksheet](files/week-2/data_detective_worksheet.txt), including your HexEd.it and CircuitVerse screenshots and your reflection.

Your tutor marks the portfolio. The quiz is marked automatically.

### Optional

Nothing here is required. Try these if you want more.

- CC#5 [How Computers Calculate - the ALU](https://www.youtube.com/watch?v=1I5ZMmrOfnA&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye) (11:10): how adders like yours become a full ALU.
- CC#6 [Registers and RAM](https://www.youtube.com/watch?v=fpnE6UAfbtU&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye) (12:17): how gates can remember a bit.
- CC#21 [Compression](https://www.youtube.com/watch?v=OtDxDvCpPL4&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye) (12:48): how JPEG and ZIP make files smaller.
- In CircuitVerse, join two half adders and an OR gate to make a **full adder**, which also takes a carry in.
- Read the optional note on floating point at the end of the Data types part of Section 2.1.

## 2.1 Binary and hexadecimal {#section-2-1}

**Time:** about 45 minutes (30 minutes reading, 15 minutes exercises). Have paper and a pen ready.


### Why computers use binary

In Week 1 you saw that a computer is built from billions of tiny switches (transistors). A switch has two states: **off** or **on**. We write these as **0** and **1**.

- One 0 or 1 is called a **bit** (short for *binary digit*).
- Eight bits make a **byte**, for example `01000001`.

Everything a computer stores (numbers, text, photos, music, programs) is in the end a long row of bits. This week shows how.

### Place value

You already know place value from everyday numbers. In the number **352**, the 3 means 3 hundreds, the 5 means 5 tens and the 2 means 2 ones. Each place is worth **10 times** the place to its right. This is **base 10**, or **decimal**, and it uses ten digits (0 to 9).

**Binary** is **base 2**. It uses only two digits (0 and 1), and each place is worth **2 times** the place to its right. Here are the eight places of one byte:

| Place value | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|---|---|---|---|---|---|---|---|---|

Learn this row. You will use it all week.

### Binary to decimal

To turn binary into decimal, write the place values above the bits and **add up the place values that have a 1**.

**Example:** what is `00101101` in decimal?

| Place value | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|---|---|---|---|---|---|---|---|---|
| Bit | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 |

32 + 8 + 4 + 1 = **45**

The largest number one byte can hold is `11111111` = 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = **255**. So one byte holds 256 different values, 0 to 255.

### Decimal to binary

To turn decimal into binary, work from the **left** of the place-value row. For each place, ask: *does this place value fit into what is left?* If it does, write 1 and subtract it. If not, write 0.

**Example:** what is 100 in binary?

| Place value | Fits into what is left? | Bit | Left over |
|---|---|---|---|
| 128 | No (100 is less than 128) | 0 | 100 |
| 64 | Yes | 1 | 100 − 64 = 36 |
| 32 | Yes | 1 | 36 − 32 = 4 |
| 16 | No | 0 | 4 |
| 8 | No | 0 | 4 |
| 4 | Yes | 1 | 4 − 4 = 0 |
| 2 | No | 0 | 0 |
| 1 | No | 0 | 0 |

100 = **`01100100`**. Check it: 64 + 32 + 4 = 100.

### Adding in binary

Binary addition works like decimal addition, but you carry when a column reaches **2** instead of 10. The four rules are:

| Sum | Result | Write | Carry |
|---|---|---|---|
| 0 + 0 | 0 | 0 | 0 |
| 0 + 1 | 1 | 1 | 0 |
| 1 + 1 | 2 | 0 | 1 |
| 1 + 1 + 1 (with a carry) | 3 | 1 | 1 |

**Example:** `0101` (5) + `0011` (3)

```
  carry   1 1 1
          0 1 0 1
        + 0 0 1 1
        ---------
          1 0 0 0
```

The answer is `1000`, which is 8. You will build a circuit that does the first column of this sum in [Section 2.3](#section-2-3).

### Hexadecimal

Long rows of 0s and 1s are hard for people to read. **Hexadecimal** (or **hex**) is **base 16**: a short way to write binary.

Hex needs 16 digits, so after 0 to 9 it uses the letters A to F:

| Decimal | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hex | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F |
| Binary | 0000 | 0001 | 0010 | 0011 | 0100 | 0101 | 0110 | 0111 | 1000 | 1001 | 1010 | 1011 | 1100 | 1101 | 1110 | 1111 |

**The key trick:** one hex digit stands for exactly **four bits**, so one byte is always **two hex digits**.

**Binary to hex:** split the byte into two groups of four, then look each group up.

`11011010` → `1101` `1010` → **D** **A** → `DA`

**Hex to binary:** do the reverse. `A7` → `1010` `0111` → `10100111`

**Hex to decimal:** a two-digit hex number is (first digit × 16) + second digit.

`3F` → (3 × 16) + 15 = **63**

**Decimal to hex:** divide by 16. The whole-number answer is the first digit and the remainder is the second.

200 ÷ 16 = 12 remainder 8 → C, 8 → **`C8`**

Hex is often written with `0x` in front (`0xC8`) or `#` for colours (`#FF0000`), so people know it is not decimal. You will see hex all through cyber security and data work: in colour codes, memory addresses, network (MAC) addresses, file contents and hash values.

### Data types

The same bits can mean different things. `01000001` could be the number 65, or the letter A, or part of a photo. The computer knows which because the program says what **type** of data it is. The four basic types are:

| Type | What it holds | Example |
|---|---|---|
| **Integer** | Whole numbers | `42`, `-7` |
| **Floating point (float)** | Numbers with a decimal point | `3.14`, `0.5` |
| **Text (string)** | Letters, digits and symbols | `"Perth"` |
| **Boolean** | Only true or false | `true` |

The number of bits limits what a type can hold. One byte can hold whole numbers from 0 to 255. If a program adds 1 to 255 in a single byte, the answer will not fit. It "wraps round" to 0. This is called an **overflow**, and it has caused real software failures.

:::::::::::::::::::::::::::::::::::::::: callout

**Optional: why 0.1 + 0.2 is not exactly 0.3.** Some decimal fractions, like 0.1, cannot be written exactly in binary, just as 1/3 cannot be written exactly in decimal (0.3333…). So computers store a very close approximation, and 0.1 + 0.2 comes out as 0.30000000000000004. This is why money is often stored in cents, as whole numbers.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises

About 15 minutes. Show your working. Answers are at the end.

1. Convert binary to decimal: (a) `00001010`; (b) `10000001`; (c) `11111111`.
2. Convert decimal to binary (8 bits): (a) 9; (b) 50; (c) 128.
3. Convert binary to hex: (a) `00111100`; (b) `11111111`.
4. Convert hex to decimal: (a) `1A`; (b) `FF`.
5. Add in binary: `0110` + `0011`. Check your answer in decimal.
6. What type would you use for: (a) a person's age in years; (b) a temperature such as 36.8; (c) whether a user is logged in; (d) a suburb name?

:::::::::::::::: solution

### Answers

1. (a) 10; (b) 129; (c) 255.
2. (a) `00001001`; (b) `00110010`; (c) `10000000`.
3. (a) `0011` `1100` → `3C`; (b) `FF`.
4. (a) 1 × 16 + 10 = 26; (b) 15 × 16 + 15 = 255.
5. `1001`. In decimal, 6 + 3 = 9, and `1001` = 8 + 1 = 9.
6. (a) integer; (b) float; (c) Boolean; (d) text (string).

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## 2.2 Text, images and files {#section-2-2}

**Time:** about 40 minutes (25 minutes reading, 15 minutes practice and exercises).


### Text: ASCII and Unicode

To store text, a computer gives every character a number, called its **code**, and stores that number in binary. The list of codes is called a **character set**.

**ASCII** (American Standard Code for Information Interchange) is the oldest character set still in use. It has 128 codes, enough for English letters, digits, punctuation and a few control codes. Here are some you will use this week:

| Character | Decimal | Hex | Binary |
|---|---|---|---|
| space | 32 | 20 | 00100000 |
| `0` | 48 | 30 | 00110000 |
| `3` | 51 | 33 | 00110011 |
| `A` | 65 | 41 | 01000001 |
| `B` | 66 | 42 | 01000010 |
| `Z` | 90 | 5A | 01011010 |
| `a` | 97 | 61 | 01100001 |

Notice the patterns:

- The capital letters are in order: A is 41 in hex, B is 42, C is 43, and so on up to Z at 5A.
- Each lower-case letter is exactly 32 more than its capital (`a` is 97, `A` is 65).
- The digit `3` is **not** stored as the number 3. It is stored as code 51. Text that looks like a number is still text.

**Hex codes for capital letters (use this for the Build):**

| A | B | C | D | E | F | G | H | I | J | K | L | M |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 4A | 4B | 4C | 4D |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4E | 4F | 50 | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 | 5A |

128 codes are not enough for the world's languages, or for symbols like € and emoji. **Unicode** gives a code to more than 150,000 characters, in almost every writing system. **UTF-8** is the most common way to store Unicode. It uses **one byte** for the ASCII characters (so plain English text is the same in ASCII and UTF-8), and **two to four bytes** for everything else. An emoji such as 😀 takes four bytes.

:::::::::::::::::::::::::::::::::::::::: callout

In Introduction to Programming, Part 2 Week 1, you will look at text encoding again, using Python.

::::::::::::::::::::::::::::::::::::::::::::::::

### Images: pixels and colour

A digital image is a grid of tiny dots called **pixels**. The number of pixels across and down is the **resolution**, for example 1920 × 1080.

Each pixel's colour is made by mixing **red, green and blue (RGB)** light. Each of the three is stored as one byte, from 0 (none) to 255 (full). So one pixel uses **3 bytes**, or 24 bits.

| Colour | Red | Green | Blue | Hex colour code |
|---|---|---|---|---|
| Red | 255 | 0 | 0 | `#FF0000` |
| Green | 0 | 255 | 0 | `#00FF00` |
| Blue | 0 | 0 | 255 | `#0000FF` |
| White | 255 | 255 | 255 | `#FFFFFF` |
| Black | 0 | 0 | 0 | `#000000` |
| Teal | 0 | 128 | 128 | `#008080` |

A **hex colour code**, used in websites and design tools, is simply the three bytes written in hex: **`#RRGGBB`**. For example, in `#008080`, `00` is the red, `80` (128) is the green and `80` is the blue.

**How big is a photo?** A 1920 × 1080 image has 2,073,600 pixels. At 3 bytes each, that is 6,220,800 bytes, about **6.2 MB**. Most photos are smaller than this on disk because they are **compressed**: formats such as JPEG and PNG find patterns and store them in fewer bytes.

Try it: open any online colour picker (search "colour picker"), choose a colour and read off its RGB values and hex code.

### Files

A **file** is a named sequence of bytes kept in storage. The bytes can be text, a picture, a program or anything else.

The **file extension** at the end of the name (`.pdf`, `.png`, `.docx`) is a hint to people and to the operating system about which program should open the file. But the extension is only part of the **name**. Anyone can rename `holiday.exe` to `holiday.jpg`, and the bytes inside do not change.

A more reliable clue is the **file signature** (sometimes called the **magic number**): a fixed pattern of bytes at the very start of most file types.

| File type | First bytes (hex) | Same bytes as text |
|---|---|---|
| PNG image | `89 50 4E 47 0D 0A 1A 0A` | `.PNG....` |
| JPEG image | `FF D8 FF` | (not readable) |
| PDF document | `25 50 44 46` | `%PDF` |
| ZIP archive (and .docx, .xlsx, which are ZIP files inside) | `50 4B 03 04` | `PK..` |
| Windows program (.exe) | `4D 5A` | `MZ` |

**Why this matters for cyber security:** attackers often disguise harmful files by giving them a harmless-looking extension, for example an `invoice.pdf` that is really a program or an archive. Security tools, and analysts, check the signature, not just the name. **Data analysts** use the same check to make sure a file really is what a system claims.

### Looking inside a file with HexEd.it

**HexEd.it** (https://hexed.it/) is a **hex viewer**: it shows the bytes inside any file, in hex, in your browser. The file is opened inside your browser and is not uploaded. No account is needed.

1. Go to https://hexed.it/ and close any welcome message.
2. Choose **Open file** and pick a file. Use one of the course files in the mystery files (see the Week 2 practice task), not a personal document.
3. The middle column shows the bytes in hex, 16 to a row. The right-hand column shows the same bytes as text, with a dot where a byte is not a printable character.
4. Read the first few bytes and compare them with the signature table above.

Try it now with `file_a.png`. The first row should start `89 50 4E 47`, and the text column should show `PNG`.

::::::::::::::::::::::::::::::::::::: challenge

### Exercises

About 10 minutes. Answers are at the end.

1. Using the tables above, write the hex codes for the word `CAB`.
2. What word is `48 49`?
3. The ASCII code for `a` is 97. What is the code for `d`?
4. What colour is `#FFFF00`? Hint: mix full red and full green light.
5. A file is named `photo.jpg`, but its first bytes are `25 50 44 46`. What kind of file is it really?
6. How many bytes does an uncompressed 100 × 100 pixel RGB image need?

:::::::::::::::: solution

### Answers

1. `43 41 42`.
2. `HI`.
3. 100 (`a` = 97, `b` = 98, `c` = 99, `d` = 100).
4. Yellow (full red + full green + no blue).
5. A PDF document (`%PDF`). The extension does not match the signature.
6. 100 × 100 × 3 = 30,000 bytes.

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## 2.3 Logic and logic gates {#section-2-3}

**Time:** about 35 minutes (20 minutes reading, 15 minutes practice and exercises).


### Boolean logic

**Boolean logic** works with only two values: **true** and **false**. Computers use 1 for true and 0 for false. It is named after George Boole, a mathematician who described it in the 1850s, long before electronic computers.

You already use Boolean logic every day:

- "I'll take an umbrella if it is raining **or** the forecast says rain."
- "The door opens if you have a key card **and** it is during office hours."
- "Send a reminder if the bill is **not** paid."

### The four basic gates

A **logic gate** is a tiny circuit, made from transistors, that takes one or two bits in and gives one bit out. A **truth table** lists the output for every possible input.

**AND:** the output is 1 only if **both** inputs are 1.

| A | B | A AND B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**OR:** the output is 1 if **at least one** input is 1.

| A | B | A OR B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

**NOT:** one input. The output is the **opposite** of the input.

| A | NOT A |
|---|---|
| 0 | 1 |
| 1 | 0 |

**XOR (exclusive OR):** the output is 1 if the inputs are **different**.

| A | B | A XOR B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

### Combining gates

Gates can be joined so the output of one becomes the input of another. With enough gates you can build anything a computer does, including the ALU you met in Week 1.

**Example:** an office alarm should sound if the door is open (D = 1) **and** the alarm is **not** switched off (S = 0). This is `D AND (NOT S)`:

| D | S | NOT S | D AND (NOT S) |
|---|---|---|---|
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 1 | 0 | 1 | **1** (alarm sounds) |
| 1 | 1 | 0 | 0 |

### The half adder

In [Section 2.1](#section-2-1) you added binary numbers one column at a time. For each column you need two outputs: the **sum** bit to write down, and the **carry** bit to pass to the next column.

| A | B | Sum | Carry |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

Compare the columns with the truth tables above:

- **Sum** matches **XOR**.
- **Carry** matches **AND**.

So two gates, an XOR and an AND fed by the same two inputs, add two bits. This circuit is called a **half adder**. Chaining many adders together lets a CPU add whole numbers. This is the start of the ALU.

### Getting started in CircuitVerse

**CircuitVerse** (https://circuitverse.org/simulator) is a free logic simulator that runs in your browser. You can use it as a guest, without an account. As a guest you cannot save your circuit, so take a screenshot when you finish.

1. Open https://circuitverse.org/simulator. If a guided tour appears, read it or close it.
2. In the **Circuit Elements** panel on the left:
   - open **Input** and click **Input** to place a switch (it shows 0 or 1)
   - open **Gates** and click the **AND** gate (hover over a gate to see its name)
   - open **Output** and click **Output** to place a display
3. Drag the parts into position.
4. To join two parts, drag from the small dot on one part to the dot on the other. A wire appears.
5. Click an **Input** to change it between 0 and 1. The **Output** updates straight away.

Try it now: build one AND gate with two inputs and one output, and check all four rows of the AND truth table.

:::::::::::::::::::::::::::::::::::::::: callout

CircuitVerse also has a ready-made **Adder** element. Do not use it in the Build. The point is to build the adder from gates yourself.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises

About 10 minutes. Answers are at the end.

1. What is the output of: (a) 1 AND 0; (b) 1 OR 0; (c) NOT 0; (d) 1 XOR 1?
2. A website lets a user download a report if they are logged in (L) **and** they are a manager (M) **or** an auditor (U). Write this as a logic expression.
3. Complete the truth table for `NOT (A AND B)` (this is called a NAND gate).
4. Which two gates make a half adder, and which output does each one give?

:::::::::::::::: solution

### Answers

1. (a) 0; (b) 1; (c) 1; (d) 0.
2. `L AND (M OR U)`. The brackets matter: the user must be logged in in every case.
3. A = 0, B = 0 → 1; A = 0, B = 1 → 1; A = 1, B = 0 → 1; A = 1, B = 1 → 0.
4. XOR gives the sum; AND gives the carry.

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## Concepts Bridge: Bits, bytes and units {#week-2-bridge}

**Time:** about 30 minutes (15 minutes reading, 15 minutes activity). A calculator helps.

### Why this matters

Sizes and speeds appear on every device box, every cloud plan and every internet bill, and they are easy to misread. Cyber security analysts estimate how long a stolen file took to leave a network. Data scientists estimate whether a dataset will fit in memory. Both need to get the units right.

### Bits and bytes

- A **bit** (written with a small **b**) is one 0 or 1.
- A **byte** (written with a capital **B**) is 8 bits.

So **Mb** (megabits) and **MB** (megabytes) are different: 1 MB = 8 Mb.

**Storage** (files, drives, RAM) is usually measured in **bytes**. **Network speed** is usually measured in **bits per second**.

### Two ways to count: 1,000 or 1,024

Because computers work in powers of 2, there are two ways to count large amounts.

| Decimal (powers of 1,000) | Size | Binary (powers of 1,024) | Size |
|---|---|---|---|
| kilobyte (KB) | 1,000 bytes | kibibyte (KiB) | 1,024 bytes |
| megabyte (MB) | 1,000,000 bytes | mebibyte (MiB) | 1,048,576 bytes |
| gigabyte (GB) | 1,000,000,000 bytes | gibibyte (GiB) | 1,073,741,824 bytes |
| terabyte (TB) | 1,000,000,000,000 bytes | tebibyte (TiB) | about 1.1 trillion bytes |

Drive makers use the **decimal** units. Windows counts in **binary** units but labels them "GB". That is why the numbers do not match.

### Worked example 1: the "missing" storage

A new drive is sold as **1 TB** = 1,000,000,000,000 bytes.

Windows divides by 1,073,741,824 (one GiB):

1,000,000,000,000 ÷ 1,073,741,824 ≈ **931**

So Windows shows about **931 GB**. Nothing is missing: the same number of bytes is being counted in a different unit. This is also why the 512 GB drive in the Week 1 model answer showed as about 477 GB.

### Worked example 2: download time

How long does a **2 GB** file take to download on a **50 Mbps** (megabits per second) connection?

1. Change bytes to bits: 2 GB = 2,000 MB = 2,000 × 8 = **16,000 megabits**.
2. Divide by the speed: 16,000 ÷ 50 = **320 seconds**.
3. 320 seconds is **5 minutes 20 seconds**.

In real life it takes a little longer, because some of the connection is used to manage the transfer and other devices share it. But the size of the answer is right.

**The common mistake** is to forget step 1 and divide 2,000 by 50, which gives 40 seconds: eight times too fast.

::::::::::::::::::::::::::::::::::::: challenge

### Activity (15 minutes)

Show your working. Use decimal units (powers of 1,000) unless the question says otherwise.

1. A phone says it has **128 GB** of storage. About how many GiB is that? (Divide 128,000,000,000 by 1,073,741,824.)
2. How long would a **500 MB** video take to download on a **25 Mbps** connection?
3. Your cloud plan gives you **2 TB**. Your photos average **4 MB** each. About how many photos fit?
4. A security alert says **800 MB** of data left the office network in **10 minutes**. What average speed, in Mbps, is that?

:::::::::::::::: solution

### Model answer

1. 128,000,000,000 ÷ 1,073,741,824 ≈ **119 GiB**. Windows would show "119 GB".
2. 500 MB × 8 = 4,000 megabits. 4,000 ÷ 25 = **160 seconds** (2 minutes 40 seconds).
3. 2 TB = 2,000,000 MB. 2,000,000 ÷ 4 = **500,000 photos**.
4. 800 MB × 8 = 6,400 megabits. 10 minutes = 600 seconds. 6,400 ÷ 600 ≈ **10.7 Mbps**.

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## Practice task: Data detective {#week-2-practice}

:::::::::::::::::::::::::::::::::::::::: callout

#### Files for this task

Download single files here, or every course file at once in the [course files zip](data/course-files.zip). Worksheets download as plain text (`.txt`): open one in any text editor, and save your copy with the name the task gives.

- [data_detective_worksheet.txt](files/week-2/data_detective_worksheet.txt)
- [file_a.png](files/week-2/mystery_files/file_a.png)
- [file_b.pdf](files/week-2/mystery_files/file_b.pdf)
- [invoice.pdf](files/week-2/mystery_files/invoice.pdf)

:::::::::::::::::::::::::::::::::::::::::::::::::::

**Time:** about 2 hours. This is your portfolio item for Week 2. Your tutor marks it at the end of the week.

### Goal

Use what you learned this week to convert numbers, decode a hidden message, find a file in disguise, read colour codes and build a circuit that adds.

Work in the [worksheet](files/week-2/data_detective_worksheet.txt). Save your copy as `data_detective.md`. Any text editor works, or you can copy it into Word or Google Docs and save it as a PDF. **Show your working**: the working is marked, not only the answer.

You need paper and a pen for the conversions. Do not use an online converter for Part 1. You may use one afterwards to check your answers.

### Part 1: conversions (about 35 minutes)

Complete the 10 conversions in the worksheet using the methods in [Section 2.1](#section-2-1). For each one, show your place-value table or the steps you used.

### Part 2: the hidden message (about 15 minutes)

Decode this message, written as hex ASCII codes. Use the capital-letter table in [Section 2.2](#section-2-2). `20` is a space and `33` is the digit 3.

```
53 45 45 20 59 4F 55 20 49 4E 20 57 45 45 4B 20 33
```

Then write your **first name** as hex ASCII codes.

### Part 3: the file in disguise (about 25 minutes)

The folder `mystery_files/` ([file_a.png](files/week-2/mystery_files/file_a.png), [file_b.pdf](files/week-2/mystery_files/file_b.pdf), [invoice.pdf](files/week-2/mystery_files/invoice.pdf)) holds three files: `file_a.png`, `file_b.pdf` and `invoice.pdf`. **One of them is not what its name says.**

1. Open each file in **HexEd.it** (https://hexed.it/). The files are opened in your browser and are not uploaded.
2. For each file, record the first four bytes in hex.
3. Use the signature table in Section 2.2 to identify each file's **real** type.
4. Say which file is disguised, and explain how you know.
5. In two or three sentences: why might an attacker give a file the wrong extension, and why should a security tool check the signature?
6. Take one screenshot of HexEd.it showing the start of the disguised file.

All three files are harmless and were made for this course.

### Part 4: colour codes (about 10 minutes)

For each hex colour code in the worksheet, write the red, green and blue values in decimal, and name the colour. Then pick a colour of your own in an online colour picker and record its hex code and RGB values.

### Part 5: build a half adder (about 25 minutes)

In **CircuitVerse** (https://circuitverse.org/simulator), as a guest:

1. Place two **Inputs** (A and B), one **XOR** gate, one **AND** gate and two **Outputs** (Sum and Carry).
2. Wire both inputs into both gates. Wire the XOR output to Sum and the AND output to Carry.
3. Click the inputs through all four combinations (00, 01, 10, 11) and fill in the truth table in the worksheet from what the outputs show.
4. Take a screenshot with **both inputs set to 1**.

Do not use CircuitVerse's ready-made Adder element. See [Section 2.3](#section-2-3) if you are stuck.

### Part 6: reflection (about 10 minutes, plus tidying)

Write **100 to 150 words**:

1. Which part of this week's work was hardest, and what helped you understand it?
2. Give one example of where a cyber security analyst or a data analyst would use hex or file signatures.
3. How does your half adder connect to the CPU you met in Week 1?

### Check your work

- [ ] All 10 conversions are done, with working shown.
- [ ] The hidden message is decoded, and your first name is written in hex.
- [ ] The first four bytes of each mystery file are recorded, with its real type.
- [ ] The disguised file is named, with an explanation, and the screenshot shows its first bytes.
- [ ] All three colour codes are converted to RGB and named, and your own colour is added.
- [ ] The half adder truth table has all four rows, and the screenshot shows inputs 1 and 1.
- [ ] The reflection is 100 to 150 words and answers all three questions.

### How it is marked

Your tutor marks each criterion as **meets**, **partly** or **not yet**:

| Criterion | What the tutor looks for |
|---|---|
| Accurate | Conversions, the decoded message, file types, RGB values and the truth table are correct. |
| Complete | Every item on the checklist is done. |
| Evidence | Working is shown. The screenshots show the disguised file's bytes and the working circuit. |
| Explanation | The file-signature explanation and the reflection are in your own words. |

:::::::::::::::::::::::::::::::::::::: keypoints

- Each week has five blocks: Watch, Read & practise, Concepts Bridge, Build and Quiz.
- Each binary digit is a bit; 8 bits make a byte.
- One hex digit stands for 4 bits, so a byte is two hex digits.
- Text, images and files are all stored as numbers.
- A file signature reveals the real type of a file, whatever its name says.
- Logic gates combine bits using simple rules.
- An XOR gate and an AND gate together add two bits.
- Network speeds are in bits per second; file sizes are in bytes.
- A file's first bytes tell you what it really is.

::::::::::::::::::::::::::::::::::::::::::::::::
