import smtplib
def send_mail():
    try:
        print("Sending email")
        server = smtplib.SMTP('smtp.gmail.com', 587) #gmail server location and port
        server.starttls()
        server.login("simran.netman@gmail.com", "netmanLab2") # username and password
        msg = "test mail"
        print(msg)
        server.sendmail("simran.netman@gmail.com", "simran.netman@gmail.com", msg) #from, to, msg
        print("Mail sent successfully")
        server.quit()
    except Exception:
        print("Error. Unable to send email.")

send_mail()
