import smtplib         

# Email configuration
sender_email = "sender email"
sender_password = "password"       
receiver_email = "reciever mail"
subject = "Hello from Python"
message = "This is a test email sent from Python."

# Connect to the SMTP server
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)   # Use the SMTP server for your email provider
    server.starttls()  # Start a secure connection
    server.login(sender_email, sender_password)

    # Compose the email
    email_text = f"Subject: {subject}\n\n{message}"

    # Send the email
    server.sendmail(sender_email, receiver_email, email_text)
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {str(e)}")                                                                                                                    





                                                                                                                                                                                                                                                          
