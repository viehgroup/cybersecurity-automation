# Day 09 — WHOIS Information Extractor

A simple Python-based tool that retrieves WHOIS information for a target domain and provides basic domain intelligence.

---

## Features

- Retrieve domain registration details
- Display registrar information
- Show creation and expiration dates
- Display name servers
- Beginner-friendly implementation

---

## Technologies Used

- Python
- python-whois

---

## Installation

```bash
git clone <url>
cd Day-09-WHOIS-Information-Extractor
```

Install dependencies:

```bash
pip install python-whois
```

---

## Usage

```bash
python whois_lookup.py
```

Enter a target domain.

Example:

```text
google.com
```

---

## Example Output

```text
Enter Domain: google.com

Domain Name: GOOGLE.COM
Registrar: MarkMonitor Inc.

Creation Date:
1997-09-15

Expiration Date:
2028-09-14

Name Servers:
ns1.google.com
ns2.google.com
```

---

## What You Will Learn

- Domain intelligence gathering
- WHOIS fundamentals
- OSINT basics
- Python automation

---

## Challenge Task

Try improving this project by adding:

- Reverse WHOIS lookup
- Domain age calculation
- Export results to CSV
- Bulk domain analysis

---

## Disclaimer

This project is intended for educational and authorized security testing purposes only.

---

# 30 Days of Cybersecurity Automation by VIEH Group

Building practical cybersecurity tools
