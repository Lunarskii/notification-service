from email.message import EmailMessage

from schemas import Mail
from settings import settings


async def create_email_message(mail: Mail):
    email_message = EmailMessage()
    email_message["Subject"] = mail.subject
    email_message["From"] = settings.smtp_user
    email_message["To"] = mail.recipient
    email_message.set_content(
        mail.message,
        subtype=mail.message_format,
    )

    return email_message
