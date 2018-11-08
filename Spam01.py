#spamgondola@gmail.com
#gondola2000

import smtplib
sender = "spamgondola@gmail.com"
recipient = "goodmorningsam66@gmail.com"
password = "gondola2000"
subject = "TEST MESSAGE"
text = "TEST 01 UAHHAHAH"
smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
smtp_server.login(sender, password)
message = "Subject: {}\n\n{}".format(subject, text)
smtp_server.sendmail(sender, recipient, message)
smtp_server.close()