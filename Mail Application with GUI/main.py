from tkinter import *
import smtplib

# Main Screen
screen = Tk()
screen.title("Mail Application with GUI")

# Graphics
Label(screen, text="Mail Application", font=("Calibri", 15)).grid(row=0, sticky=N)
Label(screen, text="Use the form below to send the Email", font=("Calibri", 11)).grid(row=1, sticky=W, padx=5)

# Labels in our Application
Label(screen, text="Email", font=("Calibri", 11)).grid(row=2, sticky=W, padx=5)
Label(screen, text="Password", font=("Calibri", 11)).grid(row=3, sticky=W, padx=5)
Label(screen, text="To ", font=("Calibri", 11)).grid(row=4, sticky=W, padx=5)
Label(screen, text="Subject", font=("Calibri", 11)).grid(row=5, sticky=W, padx=5)
Label(screen, text="Body", font=("Calibri", 11)).grid(row=6, sticky=W, padx=5)

notify = Label(screen, text="", font=("Calibri", 11))
notify.grid(row=7, sticky=S, padx=5)

# storage
temp_username = StringVar()
temp_password = StringVar()
temp_receiver = StringVar()
temp_subject = StringVar()
temp_body = StringVar()

# Entries
username_entry = Entry(screen, textvariable=temp_username)
username_entry.grid(row=2, column=0)
password_entry = Entry(screen, show="*", textvariable=temp_password)
password_entry.grid(row=3, column=0)
receiver_entry = Entry(screen, textvariable=temp_receiver)
receiver_entry.grid(row=4, column=0)
Subject_entry = Entry(screen, textvariable=temp_subject)
Subject_entry.grid(row=5, column=0)
Body_entry = Entry(screen, textvariable=temp_body)
Body_entry.grid(row=6, column=0)


# Functions

# Send Function
def send():
    try:
        username = temp_username.get()
        password = temp_password.get()
        to = temp_receiver.get()
        subject = temp_subject.get()
        body = temp_body.get()
        if username == "" or password == "" or to == "" or subject == "" or body == "":
            notify.config(text="All Fields are required", fg="red")
            return
        else:
            finalMessage = 'Subject: {}\n\n{}'.format(subject, body)
            server = smtplib.SMTP('smtp.gmail.com', port=587)
            server.starttls()
            server.login(username, password)
            server.sendmail(username, to, finalMessage)
            notify.config(text="Email has been sent", fg="green")
    except:
        notify.config(text="Error sending email", fg="red")


# Reset Function
def reset():
    username_entry.delete(0, 'end')
    password_entry.delete(0, 'end')
    receiver_entry.delete(0, 'end')
    Subject_entry.delete(0, 'end')
    Body_entry.delete(0, 'end')


# Buttons
Button(screen, text="Send", command=send).grid(row=7, sticky=W, pady=15, padx=5)
Button(screen, text="Reset", command=reset).grid(row=7, sticky=W, pady=45, padx=45)

screen.mainloop()