from pydantic import (
    BaseModel,
    EmailStr,
)


class Mail(BaseModel):
    subject: str
    message: str
    recipient: EmailStr
    message_format: str = "text/plain"
