from pydantic import Field
from fastapi import Form
from datetime import datetime
from beanie import Document, PydanticObjectId

class OTA(Document):
    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id")
    createdAt: datetime = datetime.now()
    title: str
    authorName: str
    storeName: str
    memberCount: int = 1

    @classmethod
    def as_form(
        cls,
        title: str = Form(...),
        authorName: str = Form(...),
        storeName: str = Form(...),
    ):
        return cls(title=title, authorName=authorName,
                   storeName=storeName)
    class Settings:
        name = "otas"

