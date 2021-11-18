import poplib
from email import parser

server_name = "pop.mydomain.com"

inbox = poplib.POP3(server_name, port=110)
print(inbox.getwelcome())
user = "mike@mydomain.com"
pw = "password"
inbox.user(user)
inbox.pass_(pw)

messages = [inbox.retr(i) for i in range(1, len(inbox.list()[1]) + 1)]

# decode messages
messages = ['\n'.join(map(bytes.decode, msg[1])) for msg in messages]

# Parse messages
messages = [parser.Parser().parsestr(msg) for msg in messages]

for message in messages:
    print(f"Subject: {message['subject']}")
    print(f"FROM: {message['from']}")
    for part in message.walk():
        if part.get_content_type():
            body = part.get_payload(decode=True)
            print(body)

inbox.quit()