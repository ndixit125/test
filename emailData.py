from fastapi import FastAPI
from pydantic import BaseModel

class EmailData(BaseModel):
    emailSubject:str
    emailSenderName:str
    emailBody:str
