import smtplib
from typing import Annotated

from pydantic import (
    Field,
    EmailStr,
)
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    smtp_host: Annotated[str, Field(alias="SMTP_HOST")]
    smtp_port: Annotated[int, Field(alias="SMTP_PORT")] = smtplib.SMTP_SSL_PORT
    smtp_user: Annotated[EmailStr, Field(alias="SMTP_USER")]
    smtp_password: Annotated[str, Field(alias="SMTP_PASSWORD")]


settings = Settings()
