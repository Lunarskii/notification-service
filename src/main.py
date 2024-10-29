import smtplib
from email.message import EmailMessage

from fastapi import (
    FastAPI,
    status,
    HTTPException,
)
import uvicorn

from settings import settings
from schemas import Mail
import utils


app = FastAPI(
    title="Mail Service",
    version="1.0",
)


@app.post("/send/", status_code=status.HTTP_200_OK)
async def send_mail(mail: Mail):
    email_message: EmailMessage = await utils.create_email_message(mail=mail)

    try:
        with smtplib.SMTP_SSL(settings.smtp_host, settings.smtp_port) as smtp:
            smtp.login(settings.smtp_user, settings.smtp_password)
            smtp.send_message(email_message)
    except smtplib.SMTPAuthenticationError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
