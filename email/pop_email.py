import poplib

server_name = "pop.mydomain.com"

inbox = poplib.POP3(server_name, port=110)
print(inbox.getwelcome())
user = "mike@mydomain.com"
pw = "foobar"
inbox.user(user)
inbox.pass_(pw)
number_of_emails = len(inbox.list()[1])

print('-' * 25)
print(f"Number of emails: {number_of_emails}")
for num in range(number_of_emails):
    for msg in inbox.retr(num+1)[1]:
        print(msg)
    print("-" * 30)

inbox.quit()