# SSH BruteForce Tool Documentation

[Tool Link](https://github.com/aashishsec/SSH-Bruteforcer)

This document provides comprehensive information on using the SSH BruteForce tool, a script designed for guessing the correct password for a given username on an SSH server.

## Table of Contents

- [Introduction](#introduction)
- [Author](#author)
- [Github Repository](#github-repository)
- [Features](#features)
- [Usage](#usage)
- [Prerequisites](#prerequisites)
- [Command-line Arguments](#command-line-arguments)
- [Example Usage](#example-usage)
- [Output](#output)
- [Wordlist](#wordlist)
- [Concurrency Limit](#concurrency-limit)
- [Exception Handling](#exception-handling)

## Introduction

SSH BruteForce is a Python script developed to perform brute force attacks on SSH servers by attempting various passwords for a specified username. The tool aims to assist in testing the security of SSH configurations by attempting to find the correct password.

## Author

- **Author:** Aashish💕💕
- **Github:** [https://github.com/aashish36](https://github.com/aashish36)

## Features

- Password guessing for a specified username on an SSH server.
- Utilizes asyncio for asynchronous execution, enhancing performance.
- Color-coded output for a visually appealing and informative display.
- Supports customization through command-line arguments.

## Usage

1. **Clone the Repository:**
   - Clone the GitHub repository: `git clone https://github.com/aashish36/SSH-BruteForce.git`

2. **Navigate to the Directory:**
   - Change into the script directory: `cd SSH-BruteForce`

3. **Install Dependencies:**
   - Ensure that the required dependencies are installed. Install missing dependencies using `pip install asyncssh colorama termcolor`.

4. **Run the Script:**
   - Execute the script using: `python ssh_bruteforce.py -t <TARGET_HOST> -p <PORT> -w <WORDLIST_PATH> -u <USERNAME>`

## Prerequisites

Before using the script, ensure the following prerequisites are met:

- Python 3.x
- `asyncssh`, `colorama`, `termcolor` Python libraries

## Command-line Arguments

- `-t, --target`: Host to attack on (e.g., `10.10.10.10`).
- `-p, --port`: Port to attack on (Default: 22).
- `-w, --wordlist`: Path to the wordlist for brute force.
- `-u, --username`: Username to perform the brute force attack.

## Example Usage

```bash
python ssh_bruteforce.py -t 10.10.10.10 -p 22 -w wordlist.txt -u admin
```

## Output

- Color-coded output indicating success or failure of login attempts.
- Displays the host, login, and password upon successful authentication.

## Wordlist

- The tool requires a wordlist containing potential passwords for the specified username.
- Ensure the wordlist is in the correct format and contains passwords to be tested.

## Concurrency Limit

- The script uses asyncio with a concurrency limit to control the number of simultaneous login attempts.
- Adjust the `concurrency_limit` variable in the script based on system resources and target server limitations.

## Exception Handling

- The script handles exceptions gracefully and provides informative output about the progress of the brute force attack.
- Failed attempts are logged, and the script reports when the correct password is found.

---
