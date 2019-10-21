import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def autoreply(toaddr):
	"""SEnd reply to contact submission."""

	fromaddr = "batchbvjti@gmail.com"
<<<<<<< HEAD
	the_pwd = "vjti@123b"
=======
	the_pwd="vjti@123b"
>>>>>>> 16c0f4ffad00d65ab2f99f3a18d2a7311841d23b
	msg = MIMEMultipart()

	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "CookMyShow Autoreply "

	body = "Thanks for contacting us. We will get back to you after processing your submission."

	msg.attach(MIMEText(body, 'plain'))

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, the_pwd)
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()