import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

COMPANY_EMAIL = "ks9379657@gmail.com"
APP_PASSWORD = "izln mrqm ombj xvre"

def lambda_handler(event, context):

    try:

        body = json.loads(event["body"])

        name = body["name"]
        email = body["email"]
        phone = body["phone"]
        subject = body["subject"]
        message = body["message"]

        # SMTP CONNECTION
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(COMPANY_EMAIL, APP_PASSWORD)

        # COMPANY EMAIL
        company_msg = MIMEMultipart()
        company_msg["From"] = COMPANY_EMAIL
        company_msg["To"] = COMPANY_EMAIL
        company_msg["Subject"] = f"New Contact Form: {subject}"

        company_body = f"""
Name: {name}

Email: {email}

Phone: {phone}

Subject: {subject}

Message:
{message}
"""

        company_msg.attach(MIMEText(company_body, "plain"))

        server.sendmail(
            COMPANY_EMAIL,
            COMPANY_EMAIL,
            company_msg.as_string()
        )

        # CUSTOMER CONFIRMATION EMAIL
        customer_msg = MIMEMultipart()

        customer_msg["From"] = COMPANY_EMAIL
        customer_msg["To"] = email
        customer_msg["Subject"] = "Thank You for Contacting Us"

        customer_body = f"""
Hello {name},

Thank you for contacting Demo Company.

We have received your enquiry and will respond shortly.

Regards,
Demo Company
"""

        customer_msg.attach(MIMEText(customer_body, "plain"))

        server.sendmail(
            COMPANY_EMAIL,
            email,
            customer_msg.as_string()
        )

        server.quit()

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Methods": "*"
            },
            "body": json.dumps({
                "message": "Emails sent successfully"
            })
        }

    except Exception as e:

        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "error": str(e)
            })
        }

