import imaplib, re

mail = imaplib.IMAP4_SSL('imap.gmail.com')

def login():
	mail.login(input("E-mail address: "), input("Password: "))
	print("Logging in...")
	mail.list()
	mail.select("inbox") # connect to inbox

def check_unread():
	print("Checking unread messages...")
	status, response = mail.status('INBOX', '(UNSEEN)')
	regex = r'\d+'
	regex_eval = re.findall(regex, response[0].decode("utf-8"))
	print("Unread:", regex_eval[0])
