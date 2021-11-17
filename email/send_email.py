import smtplib

HOST = "smtp.mydomain.com"
SUBJECT = "Test email from Python"
TO = "mike@mydomain.com"
FROM = "python@mydomain.com"
text = "blah blach blah"
BODY = "\r\n".join((
    f"From: {FROM}",
    f"To: {TO}",
    f"Subject: {SUBJECT}",
    "",
    text)
)
server = smtplib.SMTP(HOST)
server.sendmail(FROM, [TO], BODY)
server.quit()

