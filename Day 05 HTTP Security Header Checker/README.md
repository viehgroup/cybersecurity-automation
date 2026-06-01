# Day 05 - HTTP Security Header Checker

A simple Python-based tool that analyzes a website's HTTP security headers and identifies missing security protections.

---

## Features

- Checks common security headers
- Detects missing protections
- Simple website security assessment
- Beginner-friendly implementation
- Fast and lightweight

---

## Technologies Used

- Python
- Requests

---

## Installation

```bash
git clone url
cd filename
```

Install dependencies:

```bash
pip install requests
```

---

## Usage

```bash
python header_checker.py
```

Enter a target website URL.

Example:

```text
https://example.com
```

---

## Example Output

```text
Enter URL: https://example.com

Checking Security Headers...

[+] Strict-Transport-Security Found
[+] X-Frame-Options Found
[-] Content-Security-Policy Missing
[-] Permissions-Policy Missing
[+] X-Content-Type-Options Found
```

---

## What You Will Learn

- HTTP security headers
- Web security fundamentals
- Python requests library
- Basic security automation

---

## Challenge Task

Try improving this project by adding:

- Security score calculation
- Export report to PDF
- Multiple URL scanning
- Header recommendations

---

## Disclaimer

This project is intended for educational and authorized security testing purposes only.

---

# 30 Days of Cybersecurity Automation by VIEH Group

Building practical cybersecurity tools
