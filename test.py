# import smtplib

# smtp_server = 'smtp.live.com'  
# port = 587 
# # sender = 'ubmdfl.deepfake@gamil.com'  
# # password = 'lab2022#meter.'  
# # receiver = 'ubmdfl.deepfake@gamil.com'  
# sender = 'ubmdfl_deepfake@hotmail.com'  
# password = 'lab2022#ub.'  
# receiver = 'ubmdfl_deepfake@hotmail.com'  
# msg = "Test Message from SMTPLIB"  

# server = smtplib.SMTP(smtp_server, port)  
# server.starttls()  
# server.login(sender,password)  
# server.sendmail(sender, receiver, msg)  
# server.quit()

import email
import smtplib

msg = email.message_from_string('warning')
msg['From'] = "ubmdfl_deepfake@hotmail.com"
msg['To'] = "ubmdfl_deepfake@hotmail.com"
msg['Subject'] = "helOoooOo"

s = smtplib.SMTP("smtp.live.com",587)
s.ehlo() # Hostname to send for this command defaults to the fully qualified domain name of the local host.
s.starttls() #Puts connection to SMTP server in TLS mode
s.ehlo()
s.login('ubmdfl_deepfake@hotmail.com', 'lab2022#ub.')

s.sendmail("ubmdfl_deepfake@hotmail.com", "ubmdfl_deepfake@hotmail.com", msg.as_string())

s.quit()