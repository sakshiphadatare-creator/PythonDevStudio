import smtplib as smtp

my_email = "phadataresakshi2710@yahoo.com"
password = "#$akshi@1809"
connection = smtp.SMTP("smtp.gmail.com")
connection.starttls()    # this line make the connection secure [email]
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="sakshiphadatare2024@gmail.com", msg = "hello")
connection.close()