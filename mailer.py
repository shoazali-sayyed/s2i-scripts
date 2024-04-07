import smtplib

YOUR_EMAIL = "sami.testpython@gmail.com"
YOUR_PASSWORD = "vjhk wuge xlyv teow"
TO_ADDR = input("Enter your email address:")
message = f"This is test mail"
YOUR_SMTP_ADDRESS= "smtp.gmail.com"
with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
    connection.starttls()
    result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
    connection.sendmail(
        from_addr=YOUR_EMAIL,
        to_addrs=TO_ADDR,
        msg=f"Subject:Test\n\nThis is test mail".encode("utf-8")
    )
