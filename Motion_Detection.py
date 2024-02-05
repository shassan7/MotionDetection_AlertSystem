from gpiozero import MotionSensor
import RPi.GPIO as GPIO
import time

import ssl
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

#setting up GPIO for sensor and led
pir = MotionSensor(21)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.LOW)

#setting up gmail smtp web server
smtp_port = 587
smtp_server = 'smtp.gmail.com'

email_sender = 'motiondetectionlh@gmail.com'
email_password= 'fceikzhogjjhksxe'
email_receiver = 'motiondetectionlh@gmail.com'

subject = "Alert! Alert!"

body = """
Motion has been Detected at Raspberry Pi Location.

"""
#creating the email message packaged together
msg = MIMEMultipart()
msg['From'] = email_sender
msg['To'] = email_receiver
msg['Subject'] = subject

msg.attach(MIMEText(body, 'plain'))

text = msg.as_string()

simple_email_context = ssl.create_default_context()

#While loop for sensing motion and sending email
while True:
    #Motion detection
    pir.wait_for_motion()
    print("Motion detected")
    GPIO.output(18, GPIO.HIGH)
    
    #Connect to the simple mail transport protocol
    print("connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls(context=simple_email_context)
    TIE_server.login(email_sender,email_password)
    print("connected to server")
   
   #send email after motion detection
    print()
    print(f"sending email to - {email_receiver}")
    TIE_server.sendmail(email_sender, email_receiver, text)
    print(f"email successful")
   
    #turn off motion detection after 5s delay and turn off LED
    time.sleep(5)
    pir.wait_for_no_motion()
    GPIO.output(18, GPIO.LOW)
