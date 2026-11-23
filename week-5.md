---
title: 'Week 5: Networks, the internet and online safety'
teaching: 139
exercises: 176
---

:::::::::::::::::::::::::::::::::::::: questions

- What will I learn in Week 5, and how should I spend my 6 hours?
- How does data travel across networks and the internet?
- What happens between my browser and a web server?
- What are the common online threats, and how do I protect against them?
- What happens, step by step, when I open a web page?
- Can I investigate how real websites are found, reached and secured?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Plan your study time for the week using the time plan.
- Explain LANs, WANs, routers and switches.
- Describe IP addresses, DNS, ports, TCP and UDP.
- Read a URL and find its real domain.
- Read requests, status codes and certificates in the browser.
- Explain the CIA triad.
- Spot common phishing clues.
- Tell encoding, encryption and hashing apart.
- Describe the eight steps from typing a URL to seeing the page.
- Match an error to the step that failed.
- Read DNS records, status codes and certificates, and write a safety checklist.

::::::::::::::::::::::::::::::::::::::::::::::::

## Week 5 overview {#week-5-overview}

**Theme:** how data travels across networks and the internet, what really happens when you open a web page, and how to stay safe online.


### What you will be able to do this week

- Explain the difference between a LAN, a WAN and the internet, and what routers and switches do.
- Describe what IP addresses, DNS, ports and protocols do, and look up DNS records.
- Explain the difference between HTTP and HTTPS, and read requests, status codes and certificates in your browser.
- Recognise common online threats, and the habits that reduce them.

### Time plan (under 6 hours)

| Block | What you do | Time |
|---|---|---|
| Watch | 4 videos | 0 h 50 m |
| Read & practise | Sections 5.1, 5.2 and 5.3, with the exercises | 1 h 55 m |
| Concepts Bridge | [What happens when you type a web address](#week-5-bridge) | 0 h 30 m |
| Build | [Network investigation and online safety checklist](#week-5-practice), your portfolio item for this week | 2 h 00 m |
| Quiz | Canvas quiz, 6 questions | 0 h 15 m |
| **Total** | | **5 h 30 m** |

Suggested order: videos 1 and 2, then Section 5.1; video 3, then Section 5.2; video 4, then Section 5.3. Do the Bridge, Build and Quiz last.

**You do not need to install anything.** This week uses your browser's own developer tools and certificate viewer, plus three free websites: Google Admin Toolbox Dig, Google's phishing quiz and CyberChef. None needs an account.

### Watch (0 h 50 m)

| # | Video | Length | Look for |
|---|---|---|---|
| 1 | CC#28 [Computer Networks](https://www.youtube.com/watch?v=3QhU9jd03a0&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye) | 12:20 | What a LAN is, and how devices share one network without talking over each other. |
| 2 | CC#29 [The Internet](https://www.youtube.com/watch?v=AEaKrq3SpW8&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye) | 11:58 | Packets, routers, IP addresses, TCP, UDP and DNS. |
| 3 | CC#30 [The World Wide Web](https://www.youtube.com/watch?v=guvsH5OFizE&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye) | 11:37 | The difference between the web and the internet, URLs and HTTP. |
| 4 | CC#31 [Cybersecurity](https://www.youtube.com/watch?v=bPVaOlJ6ln0&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye) | 12:30 | Confidentiality, integrity and availability, and the three kinds of authentication. |

**Video total: about 48 minutes.**

### Read & practise (1 h 55 m)

| Order | Section | Time | What to do |
|---|---|---|---|
| 1 | [Section 5.1: Networks and the internet](#section-5-1) | about 40 min | Read all of it. Do exercises 1 to 6. |
| 2 | [Section 5.2: The web, HTTP and HTTPS](#section-5-2) | about 30 min | Read all of it. Try the developer tools, the certificate viewer and the DNS lookup. Do exercises 1 to 4. |
| 3 | [Section 5.3: Online safety and cyber security basics](#section-5-3) | about 45 min | Read all of it. Try CyberChef. Do exercises 1 to 5. |

Total: 40 + 30 + 45 = 115 minutes (1 h 55 m).

### Concepts Bridge (0 h 30 m)

Open [the Concepts Bridge](#week-5-bridge). It follows one web address, step by step, from the moment you press Enter to the page appearing, and joins up everything in this week's lessons.

### Build (2 h)

Open the [practice task](#week-5-practice). You will investigate two real websites (their DNS records, requests, status codes and certificates), draw the path of a web request, take a phishing quiz, and write an online safety checklist for new staff. This is your portfolio item for this week.

### Quiz (0 h 15 m)

Take the Canvas quiz for Week 5 after you finish the Build. It has 6 questions drawn from a pool. It is marked automatically.

### Portfolio this week

Submit at the end of the week:

- `network_investigation.md` (or a Word or PDF copy): your completed [worksheet](files/week-5/network_investigation_worksheet.txt), with your diagram, screenshots and reflection.

Your tutor marks the portfolio. The quiz is marked automatically.

### Optional

Nothing here is required. Try these if you want more.

- CC#32 [Hackers & Cyber Attacks](https://www.youtube.com/watch?v=_GzE99AmAQU&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye) (11:53)
- CC#33 [Cryptography](https://www.youtube.com/watch?v=jhXCTbFnK8o&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye) (12:33)
- Australian Cyber Security Centre, *Secure your accounts* and the other guides for individuals at https://www.cyber.gov.au/
- If your work laptop allows the Command Prompt, try `ping www.abc.net.au`, `tracert www.abc.net.au` and `nslookup abc.net.au`. (On a Mac, use Terminal and `traceroute` instead of `tracert`.)

## 5.1 Networks and the internet {#section-5-1}

**Time:** about 40 minutes (30 minutes reading, 10 minutes exercises).


### What a network is

A **network** is two or more devices connected so they can share data.

| Type | What it covers | Example |
|---|---|---|
| **LAN** (local area network) | One home, office or building | The office Wi-Fi and the printers on it |
| **WAN** (wide area network) | A large area, joining LANs together | A company linking its Perth and Sydney offices |
| **The internet** | A worldwide network of networks | Billions of devices, joined by agreed rules |

The internet is not owned by one company. It works because every connected network follows the same **protocols**: agreed rules for how data is formatted and sent.

### Network devices

| Device | What it does |
|---|---|
| **Switch** | Connects devices inside a LAN, and sends each piece of data only to the device it is meant for |
| **Router** | Connects different networks together (for example your LAN to the internet), and chooses the path for data to travel |
| **Wireless access point** | Lets devices join the LAN by Wi-Fi |
| **Modem / NBN connection box** | Connects your network to your internet service provider (ISP) |
| **Firewall** | Checks traffic coming in and going out, and blocks what is not allowed |

At home, one small box usually does the jobs of the router, switch, access point and firewall together.

### Packets

Data does not travel across a network in one piece. It is split into small chunks called **packets**. Each packet carries:
- a piece of the data
- the **source** address (where it came from)
- the **destination** address (where it is going)
- a number, so the pieces can be put back in order

Routers pass each packet along, hop by hop, towards its destination. Different packets may take different routes. The receiving computer puts them back together. This is called **packet switching**. If a route is broken, packets simply go another way, which makes the internet very resilient.

### IP addresses

Every device on a network needs an address, called its **IP address** (Internet Protocol address).

**IPv4** addresses look like `192.168.1.25`: four numbers separated by dots. Each number is one **byte**, so it is between 0 and 255 (remember Week 2). That gives about 4.3 billion possible addresses, which is not enough for today's devices.

**IPv6** addresses are much longer and written in hex, for example `2403:4800:9003:2::794f:7f41`. There are enough IPv6 addresses for every device we could ever build.

**Public and private addresses**

- A **public** IP address is unique on the whole internet. Your home or office usually has one public address, given by the ISP.
- A **private** IP address is used only inside a LAN, and the same private address can be reused in millions of homes. Private IPv4 addresses start with:
  - `10.`
  - `172.16.` to `172.31.`
  - `192.168.`

The router swaps between the private and public addresses as data goes in and out.

:::::::::::::::::::::::::::::::::::::::: callout

**Privacy:** your public IP address can show roughly where you are. Do not post it, or put it in your course work.

::::::::::::::::::::::::::::::::::::::::::::::::

**Subnets.** A large network is often divided into smaller parts called **subnets**: for example, one for staff computers and one for guest Wi-Fi. That keeps them apart, and it is a common security control. In an address such as `192.168.1.25/24`, the `/24` means the first 24 bits (the first three numbers, `192.168.1`) identify the subnet, and the last number identifies the device. You do not need to calculate subnets in this course.

### DNS: names for addresses

People remember names like `abc.net.au`. Computers need IP addresses. The **Domain Name System (DNS)** is the internet's address book: it turns a **domain name** into an IP address. This is called **resolving** the name.

DNS stores several kinds of **record**:

| Record | What it holds | Example use |
|---|---|---|
| **A** | An IPv4 address for the name | Where to find the website |
| **AAAA** | An IPv6 address for the name | The same, for IPv6 |
| **MX** | The mail servers that accept **email** for the domain | Where to deliver email sent to `someone@abc.net.au` |
| **CNAME** | Another name this name points to (an alias) | `www.abc.net.au` points to a content delivery network |

Attackers sometimes try to tamper with DNS, so that a real name leads to a fake site. That is one reason DNS matters to cyber security.

### Ports and protocols

An IP address gets data to the right **device**. A **port number** gets it to the right **program** on that device, as a flat number gets mail to the right door in an apartment block.

| Port | Protocol | What it is for |
|---|---|---|
| 22 | SSH | Logging in to another computer securely, using the command line |
| 25 | SMTP | Sending email between mail servers |
| 53 | DNS | Looking up names |
| 80 | HTTP | Web pages, not encrypted |
| 443 | HTTPS | Web pages, encrypted |

Security analysts check which ports are open on a device. Every open port is a door that an attacker might try.

### TCP and UDP

Two protocols carry most data across the internet.

| | **TCP** (Transmission Control Protocol) | **UDP** (User Datagram Protocol) |
|---|---|---|
| How it works | Sets up a connection first, numbers every packet, and resends any that go missing | Just sends the packets, with no checking |
| Strength | **Reliable**: everything arrives, in order | **Fast**, with low delay |
| Used for | Web pages, email, file downloads | Video calls, online games, live streaming, most DNS lookups |

A dropped frame in a video call does not matter much. A missing piece of a bank transfer does. That is why each kind of app uses a different protocol.

### The layer model

Network jobs are split into **layers**. Each layer does one job and relies on the layer below. The **TCP/IP model** has four:

| TCP/IP layer | Job | Examples | OSI layers (another model you will meet later) |
|---|---|---|---|
| **Application** | What the user's program wants to send | HTTP, HTTPS, DNS, SMTP | 7 Application, 6 Presentation, 5 Session |
| **Transport** | Delivery between programs, using ports | TCP, UDP | 4 Transport |
| **Internet** | Addressing and routing between networks | IP | 3 Network |
| **Link** | Moving data across one physical link | Ethernet cable, Wi-Fi | 2 Data link, 1 Physical |

The seven-layer **OSI model** is often used in networking and security courses. You only need to know that it exists and lines up with the four TCP/IP layers like this.

::::::::::::::::::::::::::::::::::::: challenge

### Exercises

About 10 minutes. Answers are at the end.

1. LAN, WAN or the internet? (a) the Wi-Fi in a café; (b) a bank linking all its branches; (c) watching a video from an overseas website.
2. Which device: (a) joins your home network to the internet and chooses paths; (b) connects the computers inside an office?
3. Why can't `192.168.1.300` be a valid IPv4 address?
4. Public or private: (a) `10.0.0.5`; (b) `121.79.127.65`; (c) `192.168.0.10`?
5. Which DNS record tells the world where to deliver email for a domain?
6. Would you use TCP or UDP for (a) downloading a PDF; (b) a live video call? Why?

:::::::::::::::: solution

### Answers

1. (a) LAN; (b) WAN; (c) the internet.
2. (a) a router; (b) a switch.
3. Each part is one byte, so it must be from 0 to 255. 300 is too big.
4. (a) private; (b) public; (c) private.
5. The MX record.
6. (a) TCP, because the file must arrive complete and in order; (b) UDP, because speed matters more than an occasional lost packet.

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## 5.2 The web, HTTP and HTTPS {#section-5-2}

**Time:** about 30 minutes (15 minutes reading, 15 minutes trying the tools).


### The internet and the web are different

The **internet** is the network: the cables, routers and protocols that move packets. The **World Wide Web** is one service that runs **on** the internet: pages linked together and shown in a browser. Email, video calls and online games also use the internet, but they are not the web.

### The parts of a web address

A web address is called a **URL** (uniform resource locator).

```
https://www.abc.net.au/news/science?page=2
```

| Part | Example | Meaning |
|---|---|---|
| Scheme | `https` | The protocol to use |
| Host (domain name) | `www.abc.net.au` | The server to contact; DNS turns it into an IP address |
| Path | `/news/science` | Which page or file on that server |
| Query | `?page=2` | Extra information sent to the server |

**Read the domain carefully.** In `abc.net.au.login-check.com`, the real domain is `login-check.com`. Everything before it is just a label that its owner chose. Phishing links often use this trick (Section 5.3).

### Requests and responses

The web uses **HTTP** (Hypertext Transfer Protocol). Your browser sends a **request**, and the server sends back a **response**.

A request has a **method**:

- **GET** asks for something, such as a page or an image.
- **POST** sends something, such as a form you filled in.

Every response starts with a **status code**:

| Code | Meaning | When you see it |
|---|---|---|
| **200** OK | It worked | Almost every normal page and image |
| **301** Moved permanently | Go to a different address instead | `http://abc.net.au` redirects to `https://www.abc.net.au` |
| **403** Forbidden | You are not allowed | A page you have no permission for |
| **404** Not found | It does not exist | A mistyped address |
| **500** Internal server error | Something broke on the server | A fault in the website itself |

A rule of thumb: codes in the 200s mean success, 300s mean redirect, 400s mean a problem with the request, and 500s mean a problem on the server.

One web page is rarely one request. The browser first gets the HTML page, then makes **dozens of further requests** for images, styles, scripts and fonts, often from other servers.

### HTTPS and certificates

Plain HTTP is sent as readable text. Anyone on the path, such as someone on the same public Wi-Fi, could read or change it.

**HTTPS** is HTTP sent inside an encrypted connection, using a protocol called **TLS**. It gives three protections:

1. **Confidentiality:** the data is **encrypted**, so people on the path cannot read it.
2. **Integrity:** if anyone changes the data on the way, it is detected.
3. **Authentication:** the server proves who it is with a **certificate**.

A **certificate** is a digital document that says "this public key belongs to `www.abc.net.au`". It is signed by a trusted **certificate authority (CA)**, and it has an expiry date. Your browser checks the certificate every time. If something is wrong, it shows a full-page warning. Do not click past these warnings.

:::::::::::::::::::::::::::::::::::::::: callout

**The padlock means "encrypted", not "safe".** Scammers can get certificates for their own fake sites too. A padlock on `abc-net-au-login.com` only proves you have a private, encrypted line to a scammer. Always check the domain name.

::::::::::::::::::::::::::::::::::::::::::::::::

### Try it: your browser's developer tools

Every modern browser has **developer tools** that show each request a page makes. These steps are for Chrome or Edge; Firefox and Safari are similar.

1. Open a new tab and go to `https://www.abc.net.au`.
2. Press **F12**, or **Ctrl + Shift + I** (Windows) or **Cmd + Option + I** (Mac). Choose the **Network** tab.
3. Press **F5** (or **Cmd + R**) to reload the page, so the requests are recorded.
4. Each row is one request. Look at the **Name**, **Status**, **Type** and **Size** columns. The first row (type `document`) is the page itself.
5. Click a row, then **Headers**, to see its **Request URL**, **Request Method** and **Status Code**.
6. Now go to `https://www.abc.net.au/this-page-does-not-exist` and look at the first row's status. It should be **404**.

**If developer tools are blocked** on your work laptop, use a home or library computer. If you have none, see the alternative in the practice task.

**View a certificate:**

1. Click the icon to the left of the address (a padlock or a "tune" icon).
2. Choose **Connection is secure**.
3. Choose **Certificate is valid**.
4. Note **Issued to**, **Issued by** and the **Valid to** (expiry) date.

### Try it: look up DNS records

1. Go to **Google Admin Toolbox Dig**: https://toolbox.googleapps.com/apps/dig/. It runs in your browser, with no account.
2. Type `abc.net.au` in the box, and choose the record type **A**. The answer lists one or more IPv4 addresses.
3. Choose **MX**. The answer lists the mail servers. The number in front of each (for example `10`) is its **priority**: lower numbers are tried first.
4. Try `www.abc.net.au` with **CNAME**. It points to another name, which belongs to the network that delivers the site's content.

DNS records change over time, so your answers may not match a classmate's exactly.

::::::::::::::::::::::::::::::::::::: challenge

### Exercises

About 5 minutes. Answers are at the end.

1. In `https://shop.example.com.au/cart?item=42`, what are the host, the path and the query?
2. What do these status codes mean: (a) 404; (b) 301; (c) 500?
3. A site shows a padlock. Does that prove the site is honest? Explain.
4. In the URL `https://mygov.au.secure-login.net/signin`, what is the real domain?

:::::::::::::::: solution

### Answers

1. Host: `shop.example.com.au`. Path: `/cart`. Query: `?item=42`.
2. (a) not found; (b) moved permanently (a redirect); (c) an error on the server.
3. No. It proves the connection is encrypted and the certificate matches the name in the address bar. A scammer can get a certificate for their own domain.
4. `secure-login.net`. It is not the real myGov domain.

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## 5.3 Online safety and cyber security basics {#section-5-3}

**Time:** about 45 minutes (30 minutes reading, 5 minutes in CyberChef, 10 minutes exercises).


### The CIA triad

Cyber security protects three things about information, known as the **CIA triad**:

| Goal | Meaning | What breaks it |
|---|---|---|
| **Confidentiality** | Only the right people can see the information | A stolen password lets a stranger read your email |
| **Integrity** | The information is accurate and has not been changed without permission | An attacker changes the bank account number on an invoice |
| **Availability** | The information and systems work when needed | Ransomware locks every file, so the business cannot trade |

Almost every security control you will study protects one or more of these.

### Common threats

| Threat | What it is |
|---|---|
| **Malware** | Any harmful software. The general term for the threats below. |
| **Virus** | Malware that attaches to files and spreads when they are opened |
| **Worm** | Malware that spreads across a network by itself |
| **Trojan** | Malware disguised as something useful, such as a "free" program |
| **Spyware** | Malware that secretly watches you, for example recording what you type |
| **Ransomware** | Malware that encrypts your files and demands payment to unlock them |
| **Phishing** | Fake messages (email, text or call) that trick you into clicking, paying or giving away details. Texts are sometimes called **smishing**. |
| **Social engineering** | Manipulating people rather than computers, for example pretending to be IT support |
| **Scams** | Fraud that tricks people out of money: fake invoices, fake investments, fake parcels |

Most successful attacks start with a person being tricked, not with clever code. That is why awareness matters as much as technology.

### Spotting phishing

Common clues:

1. **Urgency or fear:** "Your account will be closed in 24 hours."
2. **A sender address that is slightly wrong**, such as `support@rnygov.com` (r-n, not m) or a free email address for a "bank".
3. **Links that go somewhere else.** Hover over a link (or press and hold on a phone) to see the real address, then read the domain as you learned in Section 5.2.
4. **Requests for passwords, codes or payment.** Real organisations do not ask for your password or your multi-factor code.
5. **Unexpected attachments**, especially archives or files whose real type does not match their name (remember `invoice.pdf` in Week 2).
6. **Changed bank details** on an invoice. Always confirm with a phone number you already have, not one in the email.
7. **Generic greetings and odd wording**, although modern scams are often well written, so do not rely on spelling mistakes.

### Passwords and multi-factor authentication

**Authentication** means proving who you are. It can use:
- something you **know** (a password or PIN)
- something you **have** (a phone, a security key)
- something you **are** (a fingerprint or your face)

**Good passwords:**

- **Long beats complicated.** A **passphrase** of four or more random words (for example `crystal onion clay pretzel`) is much harder to guess than `P@ssw0rd1`, and easier to remember.
- **Unique for every account.** When one website is breached, attackers try the stolen email and password on many other sites. This is called **credential stuffing**.
- **Use a password manager** to create and remember unique passwords. You then only need to remember one strong passphrase.

**Multi-factor authentication (MFA)** asks for a second kind of proof, such as a code from an app, as well as your password. Even if your password is stolen, the attacker cannot log in without the second factor. Turn it on for email, banking and social media first.

### Encoding, encryption and hashing

These three are often confused. They all change how data looks, but for different reasons:

| | **Encoding** | **Encryption** | **Hashing** |
|---|---|---|---|
| Purpose | Store or send data in a different format | Keep data **secret** | Check data has **not changed**, or store passwords safely |
| Can it be reversed? | Yes, by anyone, with no key | Yes, but **only with the key** | **No**. It is one-way. |
| Example | ASCII, hex, Base64 | HTTPS, an encrypted laptop drive | A SHA-256 fingerprint of a file; how websites store passwords |

A **hash** is a fixed-length "fingerprint" of any data. Change one letter of the input and the hash changes completely.

Websites should store a **hash** of your password, never the password itself. When you log in, they hash what you typed and compare the two hashes.

**Try it (5 minutes).** **CyberChef** (https://gchq.github.io/CyberChef/) is a free tool made by the UK's signals intelligence agency, GCHQ. It runs entirely in your browser: what you type is not sent anywhere. Do not type real passwords into it anyway.

1. Type `ADCI` in the **Input** box.
2. From the **Operations** list on the left, drag **To Base64** into the **Recipe** column. The output is `QURDSQ==`. This is encoding. Drag in **From Base64** below it, and you get `ADCI` back.
3. Clear the recipe (the bin icon), and drag in **SHA2**. Set its **Size** to **256**. The output is a 64-character hash starting `37ca1ddb`.
4. Change the input to `ADCJ`, which differs by one letter. The hash changes completely: it now starts `afb60119`. There is no "From SHA2" operation, because hashing cannot be reversed.

In Introduction to Programming, Part 2 Week 3, you will hash data in Python.

### Everyday protections

- **Install updates promptly**, for the operating system, browser and apps (Week 3).
- **Back up** important files, and keep at least one copy that ransomware cannot reach: a drive you disconnect after each backup, or a cloud backup that keeps earlier versions. (A folder that simply syncs to the cloud can be encrypted along with your files.)
- **Public Wi-Fi:** HTTPS protects your web traffic, but avoid banking on unknown networks if you can, and never ignore certificate warnings. Your phone's hotspot is safer.
- **Lock your screen** when you walk away, and use a PIN or biometric on your phone.
- **Think before you share:** details you post can be used to guess passwords or make a scam convincing.

### Reporting

In Australia:

- Report cybercrime to the **Australian Cyber Security Centre** through **ReportCyber**: https://www.cyber.gov.au/report-and-recover/report
- Report scams to **Scamwatch**: https://www.scamwatch.gov.au/
- At work, report suspicious messages to your IT or security team **straight away**. Reporting quickly, even after you clicked, limits the damage.

::::::::::::::::::::::::::::::::::::: challenge

### Exercises

About 10 minutes. Answers are at the end.

1. Which part of the CIA triad is harmed? (a) A website is knocked offline. (b) Customer records are leaked online. (c) An attacker changes the grades in a school system.
2. Name the threat: (a) a free game that secretly installs a keylogger; (b) malware that locks files and demands payment; (c) a caller pretending to be from IT asking for your password.
3. An email from "Australia Post" says a parcel is held, and gives a link to `auspost.parcel-redelivery.info`. List two clues that it is phishing.
4. Why is `crystal onion clay pretzel` a better password than `Tr0ub4dor&3`?
5. Encoding, encryption or hashing? (a) a laptop drive that needs a key to read; (b) a fingerprint used to check a downloaded file has not been changed; (c) turning text into Base64 to send it in an email.

:::::::::::::::: solution

### Answers

1. (a) availability; (b) confidentiality; (c) integrity.
2. (a) a trojan (carrying spyware); (b) ransomware; (c) social engineering.
3. Any two: the real domain is `parcel-redelivery.info`, not `auspost.com.au`; it creates urgency about a parcel; it was unexpected; it asks you to click a link.
4. It is longer, so there are far more possible combinations to guess, and it is easier to remember. Swapping letters for numbers and symbols adds little, because attackers' tools already try those swaps.
5. (a) encryption; (b) hashing; (c) encoding.

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## Concepts Bridge: What happens when you type a web address {#week-5-bridge}

**Time:** about 30 minutes (15 minutes reading, 15 minutes activity).

### Why this matters

"What happens when you type a web address and press Enter?" is a classic question in IT and cyber security job interviews, because a good answer touches almost every layer of computing. It is also the map an analyst uses to work out **where** something went wrong: a DNS problem, a network problem, a certificate problem or a server problem.

### The big idea: eight steps

You type `https://www.abc.net.au` into your browser and press **Enter**.

| Step | What happens | Week and section |
|---|---|---|
| 1. **Input** | The keyboard sends the keystrokes; the browser reads the URL and sees the scheme `https` and the host `www.abc.net.au`. | Week 1 (IPOS), Section 5.2 |
| 2. **DNS lookup** | The browser needs an IP address. It checks its own memory (cache) first, then asks a DNS server (often your router or ISP). `www.abc.net.au` turns out to be an alias (CNAME) for a content delivery network, which finally gives an A record: an IP address. | Section 5.1 |
| 3. **Find the route** | Your computer sees that the address is not on your LAN, so it sends the packets to your **router**, which passes them to your ISP, and from router to router across the internet. | Section 5.1 |
| 4. **TCP connection** | The browser opens a TCP connection to port **443** on that server, so that nothing will be lost on the way. | Section 5.1 |
| 5. **TLS handshake** | The server sends its **certificate**. The browser checks that it was signed by a trusted certificate authority, matches `www.abc.net.au` and has not expired. They agree on encryption keys. From now on everything is encrypted. | Section 5.2 |
| 6. **HTTP request** | The browser sends `GET /` inside the encrypted connection. | Section 5.2 |
| 7. **HTTP response** | The server replies with status **200** and the HTML of the page. | Section 5.2 |
| 8. **Render (output)** | The browser reads the HTML, then makes **dozens more requests** (steps 2 to 7 again) for images, styles and scripts, and draws the page on the screen. | Week 1 (output) |

All of this usually happens in under a second.

### Where things go wrong

| Symptom | Most likely step |
|---|---|
| "This site can't be reached: server IP address could not be found" | 2: DNS |
| The page spins and times out; other sites fail too | 3: the network or route |
| A full-page "Your connection is not private" warning | 5: the certificate (expired, wrong name, or someone is intercepting) |
| "404 Not Found" | 7: the server is reachable but has no such page |
| "500 Internal Server Error" | 7: a fault on the server |

::::::::::::::::::::::::::::::::::::: challenge

### Activity (15 minutes)

1. Without looking at the table above, write the eight steps in your own words, in order. Then check your list against the table.
2. For each problem below, say which step most likely failed and what you would check first:
   - (a) A colleague can open every site except one, which gives "server IP address could not be found".
   - (b) On hotel Wi-Fi, every site shows "Your connection is not private".
   - (c) A link in an old email gives "404 Not Found".
3. In two or three sentences: at which step does HTTPS protect you on public Wi-Fi, and what does it **not** protect you from?

:::::::::::::::: solution

### Model answer

1. Any wording that keeps the order is fine: input; DNS lookup; route through the router; TCP connection; TLS handshake and certificate check; HTTP request; HTTP response; display the page and fetch the rest of its parts.
2. Suggested answers:
   - (a) Step 2, DNS. Check that the name is spelled correctly, then look it up in a DNS tool to see whether it resolves.
   - (b) Step 5, certificates. The hotel network may be intercepting connections, often a login page or, in a worse case, an attack. Do not click past the warning; use your phone's hotspot instead.
   - (c) Step 7. The server works, but the page has moved or been deleted. Search the site for it.
3. From step 5 onwards, everything is encrypted, so others on the Wi-Fi cannot read or change the pages and passwords you send. HTTPS does **not** protect you from a fake website with its own valid certificate (phishing), from malware already on your device, or from someone seeing which site you visited.

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## Practice task: Network investigation and online safety checklist {#week-5-practice}

:::::::::::::::::::::::::::::::::::::::: callout

#### Files for this task

Download single files here, or every course file at once in the [course files zip](data/course-files.zip). Worksheets download as plain text (`.txt`): open one in any text editor, and save your copy with the name the task gives.

- [network_investigation_worksheet.txt](files/week-5/network_investigation_worksheet.txt)

:::::::::::::::::::::::::::::::::::::::::::::::::::

**Time:** about 2 hours. This is your portfolio item for Week 5. Your tutor marks it at the end of the week.

### Goal

Investigate how two real websites are found, reached and secured. Then turn what you learned about online safety into practical advice for a new staff member.

Work in the [worksheet](files/week-5/network_investigation_worksheet.txt). Save your copy as `network_investigation.md`. Any text editor works, or you can copy it into Word or Google Docs and save it as a PDF.

**The two websites** (both public Australian organisations):

- **Site A:** ABC, domain `abc.net.au`, website `https://www.abc.net.au`
- **Site B:** CSIRO, domain `csiro.au`, website `https://www.csiro.au`

:::::::::::::::::::::::::::::::::::::::: callout

**Privacy.** Do not record your own public IP address, or anything from your own email or accounts. Everything you need comes from the two public websites.

::::::::::::::::::::::::::::::::::::::::::::::::

DNS records and certificates change from time to time, so your values may differ from a classmate's. That is fine, as long as you explain what each one means.

### Part 1: DNS records (about 20 minutes)

Use **Google Admin Toolbox Dig** (https://toolbox.googleapps.com/apps/dig/), as in [Section 5.2](#section-5-2).

For **each** domain (`abc.net.au` and `csiro.au`):

1. Look up the **A** record and record the IP address or addresses.
2. Look up the **MX** record and record the mail servers and their priority numbers.
3. Say whether the IP address is **public or private**, and how you know.

Then, in two or three sentences: what would go wrong for each organisation if its **MX** records were deleted? What if its **A** record pointed to the wrong address?

### Part 2: requests and status codes (about 20 minutes)

Use your browser's **developer tools**, **Network** tab, as in Section 5.2.

1. Open `https://www.abc.net.au` with the Network tab open, and reload. Record **three** requests: the main page (type `document`), one image and one script. For each, record the method, status code, type and size.
2. Look at the total number of requests at the bottom of the Network tab. Record it, and explain in one sentence why one page needs so many.
3. Visit `https://www.csiro.au/this-page-does-not-exist` and record the status code of the main request.
4. Visit `http://abc.net.au` (note: **http**, without www). Record the status code of the first request and the address it sends you to. Explain what happened and why the site does this.

**If developer tools are blocked** on your computer: for steps 3 and 4, enter the addresses into **httpstatus.io** (https://httpstatus.io/), which shows each status code and redirect. For steps 1 and 2, write "developer tools blocked" and describe what you would expect to see. Your tutor will not mark you down for this.

### Part 3: certificates (about 10 minutes)

For **each** website (`https://www.abc.net.au` and `https://www.csiro.au`), open the certificate viewer as in Section 5.2 and record:

- **Issued to** (the common name);
- **Issued by** (the certificate authority);
- **Valid to** (the expiry date).

Then answer: if the certificate's name did not match the address bar, what would the browser do, and why?

### Part 4: the path of a request (about 20 minutes)

Draw a diagram (in diagrams.net, as in Week 4, or by hand) showing what happens when you open `https://www.csiro.au`. Include and label:

- your device, your router, the internet (as a cloud), a DNS server and the CSIRO web server;
- the **DNS lookup** (question and answer);
- the **HTTPS request** on **port 443** using **TCP**, and the response with a **status code**;
- where the connection is **encrypted**.

Use the [Concepts Bridge](#week-5-bridge) to help. Add the image to the worksheet.

### Part 5: phishing quiz (about 15 minutes)

1. Take Google's **Phishing Quiz** (https://phishingquiz.withgoogle.com/). It uses made-up example emails. Click **Take the quiz**. When it asks for a name and email address, it only uses them to fill in the pretend emails, so type a made-up name and address, not your own.
2. Record your score.
3. Describe **two clues** you learned to spot, and give an example of each from the quiz.

### Part 6: online safety checklist (about 20 minutes)

Harbour Street Physio, the office from Week 3, has a new receptionist starting on Monday. Write a **ten-point online safety checklist** for them. Each point must be:

- **an action** they can actually do, for example "Turn on multi-factor authentication for your work email on day one", not "Be careful online";
- **one line**, with a short reason in brackets.

Cover at least: passwords or passphrases, MFA, phishing, updates, public Wi-Fi, locking the screen, and **how and where to report** a suspicious message.

### Part 7: reflection (about 15 minutes, including tidying)

Write **100 to 150 words**:

1. What surprised you most about what happens behind one web page?
2. Which part of the CIA triad does HTTPS protect, and which part does a backup protect?
3. How could DNS records, status codes or certificates help a cyber security analyst or a data analyst at work?

### Check your work

- [ ] Part 1: A and MX records for both domains, public or private explained, and the "what would go wrong" answer.
- [ ] Part 2: three requests recorded, the total count explained, the 404 recorded, and the http-to-https redirect explained.
- [ ] Part 3: issued to, issued by and expiry for both sites, and the name-mismatch answer.
- [ ] Part 4: a labelled diagram with DNS, port 443, TCP, the status code and the encrypted part.
- [ ] Part 5: the quiz score and two clues with examples.
- [ ] Part 6: ten practical, one-line points, including how to report.
- [ ] The reflection is 100 to 150 words and answers all three questions.

### How it is marked

Your tutor marks each criterion as **meets**, **partly** or **not yet**:

| Criterion | What the tutor looks for |
|---|---|
| Accurate | The records, status codes and certificate details are read and explained correctly. The diagram is in the right order. |
| Complete | Every item on the checklist is done. |
| Evidence | The recorded values and the diagram show the tools were used. |
| Explanation | The explanations, the checklist and the reflection are in your own words and practical. |

:::::::::::::::::::::::::::::::::::::: keypoints

- Each week has five blocks: Watch, Read & practise, Concepts Bridge, Build and Quiz.
- Data travels in packets, passed from router to router.
- DNS turns names into IP addresses.
- HTTPS encrypts the connection; a padlock does not mean a site is honest.
- Status codes tell you what happened to each request.
- Most attacks start with a person being tricked.
- Long unique passphrases and MFA stop most account takeovers.
- DNS comes first; HTTPS encryption starts with the TLS handshake.
- DNS, status codes and certificates are evidence you can check yourself.

::::::::::::::::::::::::::::::::::::::::::::::::
