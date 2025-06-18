# 🔁 Duplicate File Remover

> A Python automation script that detects and removes duplicate files from specified directories, with automated scheduling and email notifications.

---

## 👤 Author

**Nrupal Wakode**

---

## ✨ Features

- 🔍 **Duplicate Detection** – Uses MD5 checksums to identify duplicates
- 🗑️ **Automated Deletion** – Keeps one copy and deletes the rest
- 📝 **Logging** – Detailed logs with timestamped filenames
- 📧 **Email Notifications** – Sends log files via email
- ⏱️ **Scheduled Automation** – Runs at user-defined intervals
- 💻 **Command Line Interface** – CLI with help and usage flags

---

## 📦 Requirements

- **Python 3.x**

### 🐍 Built-in Modules Used

- `smtplib`
- `email`
- `os`
- `datetime`
- `hashlib`
- `sys`
- `time`

### 📦 External Module

- `schedule` (Install via pip)

```bash
pip install schedule
```

### 📧 Gmail Configuration

- Gmail account with **App Passwords** enabled
- Enable 2FA in Gmail → Generate an App Password → Use in script

---

## ⚙️ Installation

1. **Clone or download the repository**

2. **Install dependencies:**
   ```bash
   pip install schedule
   ```

3. **Configure Email Credentials in the script:**
   ```python
   msg['From'] = 'your-email@gmail.com'
   your_email = 'your-email@gmail.com'
   your_password = 'your-app-password'
   ```

---

## 🚀 Usage

```bash
python duplicate_remover.py [DIRECTORY_PATH] [INTERVAL_IN_HOURS] [EMAIL_ID]
```

### 🔹 Command Line Help Flags

| Flag | Description |
|------|-------------|
| `--h` or `--H` | Display help message |
| `--u` or `--U` | Show usage instructions |

---

## 🧪 Examples

### 📘 Help
```bash
python duplicate_remover.py --h
```

### 📘 Usage
```bash
python duplicate_remover.py --u
```

### 🧹 Run Cleanup and Email Logs
```bash
python duplicate_remover.py "C:\\Users\\Example\\Documents" 2 someone@example.com
```

**This:**
- ✅ Scans the folder for duplicates
- ✅ Deletes them every 2 hours
- ✅ Emails the latest log to `someone@example.com`

---

## 🧠 How It Works

### 🔍 Duplicate Detection
- Calculates **MD5 checksums** for all files recursively in the given directory

### 🗑️ File Removal
- Keeps the **first file**, deletes all others with matching checksum

### 📝 Logging
- Generates a log file in `Log_File_Folder/` with:
  - Deleted file paths
  - Timestamp
  - Total deleted
  - Errors (if any)

### 📧 Email Notification
- Attaches and sends the latest log file to the given email at scheduled intervals

---

## 🗂️ Project Structure

```
project-directory/
│
├── duplicate_remover.py      # Main script
├── checkparameters.py        # (Optional) Parameter validation
├── README.md
└── Log_File_Folder/          # Auto-created log folder
    ├── log_2024-06-18_14-30-00.txt
    └── ...
```

---

## 📄 Sample Log Format

```
------------------------------------------------------
----------- Nrupal Wakode -----------
------------------------------------------------------
Deleted file: C:\Users\Example\Documents\duplicate1.txt
Deleted file: C:\Users\Example\Documents\duplicate2.txt
...

Total files deleted: 5
------------------------------------------------------
Thank you for using our script
----------- Nrupal Wakode -----------
------------------------------------------------------
```

---

## 🔐 Security Recommendations

1. **Use environment variables** to store credentials:
   ```python
   import os
   your_email = os.environ.get('GMAIL_USER')
   your_password = os.environ.get('GMAIL_APP_PASSWORD')
   ```

2. **Back up directories** before running

3. **Never hardcode passwords** in public scripts

4. **Test on sample folders** first

---

## ⚠️ Limitations

- ❌ Uses MD5 (fast but less secure than SHA256)
- ❌ Gmail-only support for email
- ❌ Credentials stored in plaintext (unless secured manually)
- ❌ No built-in backup system
- ❌ Files are **permanently deleted** (no recycle bin)

---

## 🛠️ Troubleshooting

| Issue | Fix |
|-------|-----|
| `Path does not exist` | Use a valid absolute path |
| `Email sending fails` | Check app password and Gmail security settings |
| `Permission denied` | Run as admin or give write access |
| `Log file not found` | Wait for log to be generated |
| `SMTP errors` | Check network connection / credentials |
| `Invalid interval` | Use positive integer for hours |

---

## 🔧 Advanced Configuration

### 📧 Email Settings

```python
# SMTP Configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# For other email providers:
# Outlook: smtp-mail.outlook.com, port 587
# Yahoo: smtp.mail.yahoo.com, port 587
```

### 🔐 Environment Variables Setup

**Windows:**
```cmd
set GMAIL_USER=your-email@gmail.com
set GMAIL_APP_PASSWORD=your-app-password
```

**Linux/Mac:**
```bash
export GMAIL_USER="your-email@gmail.com"
export GMAIL_APP_PASSWORD="your-app-password"
```

---

## 🧪 Testing

### 🔹 Test with Sample Files

1. Create a test directory with duplicate files
2. Run the script with a short interval (1-2 hours)
3. Verify logs and email notifications
4. Check that duplicates are properly removed

### 🔹 Validation Steps

- ✅ Directory path exists and is accessible
- ✅ Email credentials are working
- ✅ Log files are created properly
- ✅ Only duplicate files are deleted
- ✅ At least one copy of each file remains

---

## 📊 Performance Notes

- **Small files** (< 1MB): Very fast processing
- **Large files** (> 100MB): May take time for checksum calculation
- **Network folders**: Slower due to network latency
- **SSD vs HDD**: SSD provides faster file operations

---

## 🤝 Contributing

1. **Fork** this repository
2. **Create your branch:** `git checkout -b feature-name`
3. **Commit changes:** `git commit -am 'Add feature'`
4. **Push to the branch:** `git push origin feature-name`
5. **Submit a pull request**

### 🔹 Contribution Ideas

- [ ] Add SHA-256 checksum option
- [ ] Support for other email providers
- [ ] GUI interface
- [ ] Undo functionality
- [ ] Progress bar for large directories
- [ ] Configuration file support

---

## 📚 Dependencies Details

| Package | Version | Purpose |
|---------|---------|---------|
| `schedule` | Latest | Task scheduling |
| `smtplib` | Built-in | Email sending |
| `hashlib` | Built-in | File checksums |
| `os` | Built-in | File operations |


## 📜 License

This project is created by **Nrupal Wakode**.
Please provide appropriate attribution when using or modifying this script.

---

## ⚠️ Disclaimer

> **Warning:** This script permanently deletes files. Please test on sample folders and back up critical data before use. The author is not responsible for any accidental data loss.

---

## 📞 Support

If you encounter issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Create an issue in the repository
3. Provide error logs and system information

---

## 🎯 Roadmap

- [ ] **v2.0**: GUI interface with PyQt/Tkinter
- [ ] **v2.1**: Multiple hash algorithm support
- [ ] **v2.2**: Cloud storage integration
- [ ] **v2.3**: Batch processing for multiple directories
- [ ] **v2.4**: Real-time duplicate monitoring

---

**📌 Next Steps:**
- Save this content as `README.md` in your project folder
- Configure your email credentials
- Test with a sample directory
- Push to GitHub using Git

---
