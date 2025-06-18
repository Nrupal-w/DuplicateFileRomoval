import smtplib
from email.message import EmailMessage
import os
import datetime
import hashlib
import schedule
import time
import sys
import checkparameters

def creatfolder():
    folder = "Log_File_Folder"
    if not os.path.exists(folder):
        os.makedirs(folder)
    return os.path.abspath(folder)

def creatlogfile():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    foldername = creatfolder()
    filename = f"log_{timestamp}.txt"
    return os.path.join(foldername, filename)

def calculatecheksum(path, blocksize=1024):
    with open(path, 'rb') as fobj:
        hobj = hashlib.md5()
        buffer = fobj.read(blocksize)
        while buffer:
            hobj.update(buffer)
            buffer = fobj.read(blocksize)
    return hobj.hexdigest()

def finddublicate(dirname):
    dirname = os.path.abspath(dirname) 

    if not os.path.exists(dirname):
        print("Path does not exist")
        exit()

    dublicate = {}

    for foldername,subfolder, filesname in os.walk(dirname):
        for fname in filesname:
            path = os.path.join(foldername, fname)
            cheksum = calculatecheksum(path)
            dublicate.setdefault(cheksum, []).append(path)
    
    return dublicate


def deletedublicate(dirname):
    logfilepath = creatlogfile()
    with open(logfilepath, "w") as fobj:
        border = "-" * 54
        fobj.write(border + "\n")
        fobj.write("----------- Nrupal Wakode -----------\n")
        fobj.write(border + "\n")

        result = list(filter(lambda x: len(x) > 1, finddublicate(dirname).values()))
        delete_count = 0

        for group in result:
            for file in group[1:]:  
                try:
                    os.remove(file)
                    print("Deleted file:", file)
                    fobj.write(f"Deleted file: {file}\n")
                    delete_count += 1
                except Exception as e:
                    fobj.write(f"Error deleting file: {file} - {e}\n")

        fobj.write(f"\nTotal files deleted: {delete_count}\n")
        fobj.write(border + "\n")
        fobj.write("Thank you for using our script\n")
        fobj.write("----------- Nrupal Wakode -----------\n")
        fobj.write(border + "\n")

def get_latest_file(dirname="Log_File_Folder"):
    files = [os.path.join(dirname, f) for f in os.listdir(dirname)
             if os.path.isfile(os.path.join(dirname, f))]
    if not files:
        return None
    return max(files, key=os.path.getctime)

def send_email(emailid):
    msg = EmailMessage()
    msg['Subject'] = 'Hourly Log File Update'
    msg['From'] = ''# Recivers email id     
    msg['To'] = emailid
    tim = datetime.datetime.now().strftime("%H:%M:%S")

    msg.set_content(f'''
Start Time of the Scanning: {tim}
    ''')

    file_path = get_latest_file()
    file_name = os.path.basename(file_path) if file_path else "log.txt"

    try:
        with open(file_path, "rb") as f:
            doc_data = f.read()
            msg.add_attachment(
                doc_data,
                maintype="application",
                subtype="octet-stream",
                filename=file_name
            )
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    your_email = ''#input ur name
    your_password = ''  #input ur password

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(your_email, your_password)
            server.send_message(msg)
        print('Email sent successfully!')
    except Exception as e:
        print('Error:', e)


def main():
    boder="-"*54
    print(boder)
    print("--------------- Nrupal  Wakode ----------------")
    print(boder)
    
    if len(sys.argv)==2:
        if(sys.argv[1]=="--h")or(sys.argv[1]=="--H"):
            print("This application is for deleting dublicate files from a folder")
            print("This is a directory automation script")
        

        elif (sys.argv[1]=="--u")or(sys.argv[1]=="--U"):
            print("Use the given script as ")
            print("NameOfDirctory FileDirectory Durations_in_which_process_should_automate Email_ID")
            print("Please provide valid absolute path")
    

    if len(sys.argv)==4:
           
        dirname = sys.argv[1]
        interval_str = sys.argv[2]
        emailid = sys.argv[3]
        
        try:
            interval = int(interval_str)
            if interval <= 0:
                raise ValueError
        except ValueError:
            print("Interval must be a positive integer (in minutes).")
            return

        # Validate directory path
        if not os.path.exists(dirname):
            print(f"The specified path does not exist: {dirname}")
            return

        
        schedule.every(interval).minutes.do(deletedublicate, dirname=dirname)
        schedule.every(interval).minutes.do(send_email, emailid=emailid)

        print(f"Scheduled deletion and email every {interval} minute(s) from: {dirname}")
        print("Logs will be emailed to:", emailid)
        print("Press Ctrl+C to stop the script.")

        while True:
            schedule.run_pending()
            time.sleep(1)

        


    else :
            print("Invalid number of coomand line arguments")
            print("Use the given flags as : ")
            print("--h : Used to display the help")
            print("--u : Used to display the usage")


    print(boder)
    print("----------- Thank you for using our script -----------")
    print("---------------- Nrupal Wakode --------------")
    print(boder)
    
    



if __name__=="__main__":
    main()