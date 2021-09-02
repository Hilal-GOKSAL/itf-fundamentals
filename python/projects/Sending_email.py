# Sending email with Python;
import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)          # default mail submission port: Port 587

server.starttls()

my_password = "abc"

server.login("email(before @ sign)", my_password)

message = "\n This is my test mail to distinguished trainee.\nHave a nice day!"

address = ["abc@gmail.com", "yzv@gmail.com"]

server.sendmail("abc@gmail.com", address, message)

server.quit()