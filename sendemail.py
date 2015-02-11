import smtplib

fromaddr = '6200.info3180@gmail.com'

toaddr = '6200.info3180@gmail.com'

message = """From: {} <{}>

To: {} <{}>

Subject: {}

{}

"""

messagetosend = message.format(

 fromname,

 fromaddr,

 toname,

 toaddr,

 subject,

 msg)

# Credentials (if needed)

username = ''

password = '{}''

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username,password)

server.sendmail(fromaddr, toaddrs, messagetosend)

server.quit()