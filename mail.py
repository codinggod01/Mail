import smtplib
#create smtp session
s = smtplib.SMTP('smtp.gmail.com',587)
#start tls for sec
s.starttls()

#authenticate

s.login("tilakbhat201@gmail.com","diamond@123")

message = "hi nice to meet you"

s.sendmail("tilakbhat201@gmail.com", "2019kucp1078@iiitkota.ac.in",message)

s.quit()
