from pydantic import Field
from datetime import datetime, timedelta
from beanie import Document, PydanticObjectId

class OTA(Document):
    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id")
    createdAt: datetime = Field(default_factory=lambda: datetime.now() + timedelta(hours=9))
    title: str
    authorName: str
    storeName: str
    memberCount: int = 1

    class Settings:
        name = "otas"
