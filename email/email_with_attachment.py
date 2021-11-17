import smtplib
import sys

from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate

# ----------------------------------------------------------------------
def send_email_with_attachment(subject, body_text, to_emails, file_to_attach):
    """
    Send an email with an attachment
    """
    header = f"Content-Disposition", "attachment; filename={file_to_attach}"

    # extract server and from_addr from config
    host = "smtp.your_isp.com"
    from_addr = "mike@domain.com"

    # create the message
    msg = MIMEMultipart()
    msg["From"] = from_addr
    msg["Subject"] = subject
    msg["Date"] = formatdate(localtime=True)
    if body_text:
        msg.attach(MIMEText(body_text))

    msg["To"] = ", ".join(to_emails)

    attachment = MIMEBase("application", "octet-stream")
    try:
        with open(file_to_attach, "rb") as fh:
            data = fh.read()
        attachment.set_payload(data)
        encoders.encode_base64(attachment)
        attachment.add_header(*header)
        msg.attach(attachment)
    except IOError:
        msg = "Error opening attachment file %s" % file_to_attach
        print(msg)
        sys.exit(1)

    emails = to_emails

    server = smtplib.SMTP(host)
    server.sendmail(from_addr, emails, msg.as_string())
    server.quit()


if __name__ == "__main__":
    emails = ["mike@some_domain.org"]

    subject = "Test email with attachment from Python"
    body_text = "This email contains an attachment!"
    path = "some_path/to/file"
    send_email_with_attachment(subject, body_text, emails, cc_emails, bcc_emails, path)
