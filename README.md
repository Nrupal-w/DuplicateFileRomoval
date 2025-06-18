# DuplicateFileRomoval

Duplicate File Remover
A Python automation script that detects and removes duplicate files from specified directories, with automated scheduling and email notifications.

Author
Nrupal Wakode

Features
Duplicate Detection: Uses MD5 checksums to identify duplicate files
Automated Deletion: Removes duplicate files while keeping one copy
Logging: Creates detailed log files with timestamps
Email Notifications: Sends log files via email at specified intervals
Scheduled Automation: Runs at user-defined intervals
Command Line Interface: Easy-to-use CLI with help options
Requirements
Python 3.x
Required Python modules (install via pip):
bash
pip install schedule
Built-in modules used: smtplib, email, os, datetime, hashlib, sys, time
Gmail account for email notifications (with app password enabled)
Installation
Clone or download the script
Install required dependencies:
bash
pip install schedule
Configure email settings in the script:
Add your Gmail address to your_email
Add your Gmail app password to your_password
Add sender email in the msg['From'] field
Usage
Command Line Arguments
The script accepts the following command line arguments:

bash
python script_name.py [DIRECTORY] [INTERVAL_HOURS] [EMAIL_ID]
Help Commands
--h or --H: Display help information
--u or --U: Display usage instructions
Examples
Get Help:
bash
python duplicate_remover.py --h
Get Usage Instructions:
bash
python duplicate_remover.py --u
Run Automated Cleanup:
bash
python duplicate_remover.py /path/to/directory 30 user@example.com
This will:
Scan /path/to/directory for duplicates
Run every 30 minutes
Send log files to user@example.com
How It Works
Duplicate Detection: The script calculates MD5 checksums for all files in the specified directory and subdirectories
File Removal: When duplicates are found, it keeps the first occurrence and deletes the rest
Logging: Creates timestamped log files in a Log_File_Folder directory
Email Notification: Sends the latest log file as an email attachment at the specified interval
Configuration
Email Setup
Before using the email feature, configure the following in the script:

python
# Email configuration
msg['From'] = 'your-email@gmail.com'  # Your Gmail address
your_email = 'your-email@gmail.com'   # Your Gmail address
your_password = 'your-app-password'   # Your Gmail app password
Gmail App Password Setup
Enable 2-factor authentication on your Gmail account
Generate an app password for the script
Use the app password (not your regular Gmail password) in the script
File Structure
project-directory/
│
├── duplicate_remover.py    # Main script
├── checkparameters.py      # Parameter validation module (if exists)
└── Log_File_Folder/        # Auto-created folder for log files
    ├── log_2024-01-15_14-30-25.txt
    ├── log_2024-01-15_15-30-25.txt
    └── ...
Log File Format
The log files contain:

Header with author information
List of deleted files with full paths
Total count of deleted files
Error messages (if any)
Footer with thank you message
Safety Features
Path Validation: Checks if the specified directory exists
Error Handling: Logs errors when files cannot be deleted
Backup Strategy: Always keeps at least one copy of each unique file
Limitations
Uses MD5 checksums (consider SHA-256 for enhanced security)
Requires Gmail for email functionality
No built-in backup before deletion (files are permanently deleted)
Email credentials are stored in plaintext (consider using environment variables)
Security Recommendations
Environment Variables: Store email credentials as environment variables:
python
import os
your_email = os.environ.get('GMAIL_USER')
your_password = os.environ.get('GMAIL_APP_PASSWORD')
Backup: Always backup important directories before running the script
Test Run: Test with a sample directory first
Troubleshooting
Common Issues
"Path does not exist": Ensure the directory path is correct and accessible
Email sending fails: Check Gmail credentials and app password
Permission denied: Ensure the script has write permissions for the target directory
Error Messages
Invalid interval: Interval must be a positive integer in minutes
File not found: Log file couldn't be located for email attachment
SMTP errors: Check internet connection and Gmail settings
Contributing
Feel free to submit issues, fork the repository, and create pull requests for any improvements.

License
This project is created by Nrupal Wakode. Please respect the author's work and provide appropriate attribution when using or modifying this script.

Disclaimer
⚠️ Warning: This script permanently deletes files. Always backup your data before running the script. The author is not responsible for any data loss.

