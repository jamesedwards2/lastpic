# ~ def emailer():
	# ~ import smtplib

	# ~ # For guessing MIME type
	# ~ import mimetypes

	# ~ # Import the email modules we'll need
	# ~ import email
	# ~ import email.mime.application

	# ~ # Create a text/plain message
	# ~ msg = email.mime.Multipart.MIMEMultipart()
	# ~ msg['Subject'] = 'Greetings'
	# ~ msg['From'] = 'jam3s.3dwards@gmail.com'
	# ~ msg['To'] = 'jam3s.3dwards@gmail.com'

	# ~ # The main body is just another attachment
	# ~ body = email.mime.Text.MIMEText("""Hello, how are you? I am fine.
	# ~ This is a rather nice letter, don't you think?""")
	# ~ msg.attach(body)

	# ~ # PDF attachment
	# ~ filename='/home/james/Documents/grey.pdf'#replace with filename from program
	# ~ fp=open(filename,'rb')
	# ~ att = email.mime.application.MIMEApplication(fp.read(),_subtype="pdf")
	# ~ fp.close()
	# ~ att.add_header('Content-Disposition','attachment',filename=filename)
	# ~ msg.attach(att)

	# ~ # send via Gmail server
	# ~ # NOTE: my ISP, Centurylink, seems to be automatically rewriting
	# ~ # port 25 packets to be port 587 and it is trashing port 587 packets.
	# ~ # So, I use the default port 25, but I authenticate. 
	# ~ s = smtplib.SMTP('smtp.gmail.com')
	# ~ s.starttls()
	# ~ s.login('jam3s.3dwards@gmail.com','N1n10d0gs5423118419')
	# ~ s.sendmail('jam3s.3dwards@gmail.com',['jam3s.3dwards@gmail.com'], msg.as_string())
	# ~ s.quit()


import os
import sys


try:
	n = sys.argv[1]
except:
	n = "1"
try:
	m = sys.argv[2]
except:
	m = False

if m == "e" or m == "email":
	print("email")

if n == "1":
	a = os.popen("ls -t /home/james/Pictures | head -1")
else:
	a = os.popen("ls -t /home/james/Pictures | head -" + n + " | tail -1")

l = a.read()
#.split(".png")

#g = "xdg-open /home/james/Pictures/'" + l[0] + ".png'"
g = "xdg-open /home/james/Pictures/'" + l.rstrip() + "'"
qq = l.rstrip().split(" ")
qqq = "\ ".join(qq)
print("xdg-open /home/james/Pictures/" + qqq)

os.system(g + " && sleep 0.7 && xdotool getwindowfocus windowsize 400 400 windowmove 1350 650 mousemove --sync 1397 683 && sleep 0.1 && xdotool click 3 click 3 && sleep 0.1 && xdotool mousemove --sync 1417 783 click 1")

# ~ emailer()
	
