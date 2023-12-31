from typing import Any, List, Optional
from beanie import init_beanie, PydanticObjectId 
from models.otas import OTA
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings
import os

MONGODB_ROOT_USERNAME = open("/run/secrets/mongodb_root_username", "r").read().strip()
MONGODB_ROOT_PASSWORD = open("/run/secrets/mongodb_root_password", "r").read().strip()

class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None
    DATABASE_NAME: Optional[str] = "webdb"

    async def initialize_database(self):
	self.DATABASE_URL = f"mongodb://{MONGODB_ROOT_USERNAME}:{MONGODB_ROOT_PASSWORD}@mongodb:27017/?authSource=admin"
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database=client[self.DATABASE_NAME], document_models=[OTA])

class Database:
    def __init__(self, model):
        self.model = model

    # 생성처리(레코드 하나[문서의 인스턴스]를 데이터베이스 컬렉션에 추가한다
    async def save(self, document: Any) -> None:
        await document.create()
        return None
    
    # 조회 처리(get_all은 인수가 없고 컬렉션의모든 레코드를 불러온다)
    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False
    
    async def get_all(self) -> List[Any]:
        docs = await self.model.find_all().to_list()
        return docs
    
    async def delete(self, id: PydanticObjectId) -> bool:
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True    
