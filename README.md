# 🍯 HONEYPY - Multi-Protocol Honeypot System

A modular, graphic-based honeypot to capture IP addresses, usernames, passwords, and commands from various protocols (SSH & HTTP supported right now). Written in Python.

## 🎯 Overview

HONEYPY is a lightweight, customizable honeypot framework that simulates SSH and HTTP services to detect and log malicious activity. It creates decoy services that appear vulnerable, allowing you to monitor attack patterns and collect threat intelligence without risking real systems.

## ✨ Features

### 🔐 SSH Honeypot
- Simulates realistic SSH service with basic shell emulation
- Logs authentication attempts and executed commands
- Tracks attacker IPs, usernames, and passwords
- **Tarpit Mode**: Security mechanism to slow down brute-force attacks by sending endless SSH banners

### 🌐 HTTP Honeypot
- Impersonates default WordPress wp-admin login page using Python Flask
- Collects username/password pairs
- Default credentials (admin/deeboodah) lead to Rick Roll gif
- Runs on port 5000 by default

### 📊 Dashboard
- Web-based interface to view statistics
- Top 10 metrics: IP addresses, usernames, passwords, commands
- Tabular format for all data
- Country code lookup using CleanTalk API (optional)
- Built with Python Dash, Dash Bootstrap Components, and Pandas

## 🚀 Installation

### 1) Clone Repository
```bash
git clone https://github.com/Nuwan-droid/Honey_Pot.git
```

### 2) Set Permissions
Move into ssh_honeypy folder and ensure main.py has proper permissions:
```bash
chmod 755 honeypy.py
```

### 3) Generate SSH Key
Create a new folder and generate RSA key:
```bash
mkdir static
cd static
ssh-keygen -t rsa -b 2048 -f server.key
```

An RSA key must be generated for the SSH server host key. Ensure the key is titled `server.key` and resides in the same relative directory to the main program.

### 4) Install Dependencies
```bash
pip install -r requirements.txt
```

**For root user (required for privileged ports):**
```bash
sudo su
pip install -r requirements.txt
```

> ⚠️ **Note**: To run with sudo, the root account must have access to all Python libraries used in this project. This will install all packages for the root user but will affect the global environment.

## 📋 Usage

### Basic Command
```bash
python3 honeypy.py -a 0.0.0.0 -p 2223 --ssh
```

HONEYPY requires a bind IP address (`-a`) and network port to listen on (`-p`). Use `0.0.0.0` to listen on all network interfaces. The protocol type must also be defined.

### Required Arguments
- `-a` / `--address`: Bind address
- `-p` / `--port`: Port
- `-s` / `--ssh` OR `-wh` / `--http`: Declare honeypot type

### Optional Arguments
- `-u` / `--username`: Username
- `-w` / `--password`: Password
- `-t` / `--tarpit`: For SSH-based honeypots, trap sessions inside the shell by sending endless SSH banner

### Examples

**SSH Honeypot:**
```bash
python3 honeypy.py -a 0.0.0.0 -p 2223 --ssh
```

**SSH with Credentials and Tarpit:**
```bash
python3 main.py -a 0.0.0.0 -p 2223 --ssh -u admin -w admin --tarpit
```

**HTTP Honeypot:**
```bash
python3 honeypy.py -a 0.0.0.0 -p 2223 --http
```

**HTTP with Custom Credentials:**
```bash
python3 honeypy.py -a 0.0.0.0 -p 2223 --http -u admin -w password
```

> 💡 **Important**: If HONEYPY is set up to listen on a privileged port (22), the program must be run with sudo or root privileges. No other services should be using the specified port.

> ❗ **Port Conflict**: If port 22 is being used as the listener, the default SSH port must be changed. Refer to Hostinger's "How to Change the SSH Port" guide.

## 📁 Log Files

HONEYPY has three loggers configured. Log files are located in `../ssh_honeypy/log_files/..`

### `cmd_audits.log`
Captures IP address, username, password, and all commands supplied.

### `creds_audits.log`
Captures IP address, username, and password, comma separated. Used to see how many hosts attempt to connect to SSH_HONEYPY.

### `http_audit.log`
Captures IP address, username, password from HTTP honeypot.

## 🕸️ Honeypot Types

This honeypot was written with modularity in mind to support future honeypot types (Telnet, HTTPS, SMTP, etc). As of right now there are two honeypot types supported.

### SSH
Emulates a basic shell and supports tarpit mode to delay attacker attempts.

> 💡 **Tarpit**: A tarpit is a security mechanism designed to slow down or delay the attempts of an attacker trying to brute-force login credentials. The only way to get out of the session is by closing the terminal.

### HTTP
Uses Python Flask to provision a simple web service that impersonates a default WordPress wp-admin login page.

> 💡 **Note**: There is currently not a dashboard panel supported for HTTP-based results. This will be a future addition.

## 📊 Dashboard

Run the dashboard in a separate terminal session:
```bash
python3 web_app.py
```

Access at: `http://127.0.0.1:2223` (default Dash port is 2223)

### Features
- Top 10 IP addresses, usernames, passwords, commands
- All data in tabular format
- Country code lookup using IP address (optional)

> 💡 **Note**: Dashboards do not dynamically update as new entries are added to log files. The dashboard must be run every time to re-populate with the most up-to-date information.

### Country Code Lookup

The dashboard includes country code lookup using the CleanTalk API (`ipinfo()`). Due to rate limiting constraints, CleanTalk can only lookup 1000 IP addresses per 60 seconds.

By default, country code lookup is set to `False`. Set the `COUNTRY` environment variable to `True` in `public.env` if you would like to enable this feature.

If receiving rate limiting errors, change the `COUNTRY` environment variable to `False`.

## 🏗️ Project Structure
```
ssh_honeypy/
├── honeypy.py              # Main application
├── web_app.py              # Dashboard application
├── requirements.txt        # Dependencies
├── public.env              # Environment configuration
├── static/
│   └── server.key         # SSH host key (generated)
├── log_files/
│   ├── cmd_audits.log     # Command logs
│   ├── creds_audits.log   # Credential logs
│   └── http_audit.log     # HTTP logs
└── modules/
    ├── ssh_honeypot.py    # SSH service
    └── http_honeypot.py   # HTTP service
```

## 🔧 Technologies Used

- **Python**: Core programming language
- **Paramiko**: SSH protocol implementation
- **Flask**: HTTP web framework


