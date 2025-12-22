# 🍯 HoneyPy - Multi-Protocol Honeypot System

A lightweight, customizable honeypot framework that simulates SSH and HTTP services to detect and log malicious activity.

## 🎯 Overview

HoneyPy is a security tool designed to attract attackers and log their activities. It creates decoy SSH and HTTP services that appear vulnerable, allowing you to monitor attack patterns and collect threat intelligence without risking real systems.

## ✨ Features

### 🔐 SSH Honeypot
- Simulates realistic SSH service
- Logs authentication attempts → `audit.log`
- Logs executed commands → `cmd_audit.log`
- Tracks attacker IPs, usernames, and passwords

### 🌐 HTTP Honeypot
- Web-based honeypot for detecting web attacks
- Logs HTTP requests, headers, and payloads
- Simulates vulnerable web endpoints

### ⚙️ Dynamic Configuration
- Argument parser for flexible deployment
- Customize ports, log directories, and services
- Enable/disable modules on demand

## 🚀 Quick Start
```bash
# Clone repository
git clone https://github.com/yourusername/honeypy.git
cd honeypy

# Install dependencies
pip install -r requirements.txt

# Run with both SSH and HTTP honeypots
sudo python honeypy.py --ssh --http

# Custom configuration
sudo python honeypy.py --ssh --ssh-port 2222 --http --http-port 8080 --log-dir /var/log/honeypy
```

## 📋 Usage Examples
```bash
# SSH honeypot only (port 22)
sudo python honeypy.py --ssh

# HTTP honeypot only (port 80)
sudo python honeypy.py --http

# Both services with custom ports
sudo python honeypy.py --ssh --ssh-port 2222 --http --http-port 8080 --verbose
```

## 🌍 Deployment

### Recommended: VPS Deployment

1. **Provision a VPS** (Hostinger, DigitalOcean, Linode, etc.)
2. **Use Linux OS** (Ubuntu 20.04+ recommended)
3. **Setup environment:**
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python
sudo apt install python3 python3-pip git -y

# Clone and setup
git clone https://github.com/yourusername/honeypy.git
cd honeypy
pip install -r requirements.txt

# Configure firewall
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw enable

# Run honeypot
sudo python honeypy.py --ssh --http
```

### Run as Service (Optional)
```bash
# Create systemd service
sudo nano /etc/systemd/system/honeypy.service
```
```ini
[Unit]
Description=HoneyPy Honeypot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/home/user/honeypy
ExecStart=/usr/bin/python3 honeypy.py --ssh --http
Restart=always

[Install]
WantedBy=multi-user.target
```
```bash
# Enable and start
sudo systemctl enable honeypy
sudo systemctl start honeypy
```

## 📊 Log Analysis
```bash
# View authentication attempts
tail -f logs/audit.log

# View executed commands
tail -f logs/cmd_audit.log

# Top 10 attacking IPs
cat logs/audit.log | grep -oP 'IP: \K[^ ]+' | sort | uniq -c | sort -nr | head -10

# Most common passwords
cat logs/audit.log | grep -oP 'Pass: \K[^ ]+' | sort | uniq -c | sort -nr | head -10
```

## 🔒 Security Notes

⚠️ **Important:**
- Deploy on isolated VPS instances only
- Never use on production networks
- Ensure compliance with local laws
- Monitor logs regularly
- Keep system updated

## 📁 Project Structure
```
honeypy/
├── honeypy.py              # Main application
├── modules/
│   ├── ssh_honeypot.py     # SSH service
│   └── http_honeypot.py    # HTTP service
├── logs/
│   ├── audit.log           # Login attempts
│   └── cmd_audit.log       # Command logs
└── requirements.txt        # Dependencies
```

## 🤝 Contributing

Contributions welcome! Feel free to open issues or submit pull requests.


---

**⚠️ Disclaimer:** For educational and research purposes only. Use responsibly and legally.
