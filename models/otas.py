from pydantic import BaseModel
from typing import List, Optional
from fastapi import Form
from datetime import datetime

class OTA(BaseModel):
    id: Optional[int] = None
    createdAt: datetime = datetime.now()
    title: str
    authorName: str
    storeName: str

    @classmethod
    def as_form(
        cls,
        title: str = Form(...),
        authorName: str = Form(...),
        storeName: str = Form(...),
    ):
        return cls(title=title, authorName=authorName,
                   storeName=storeName)

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "createdAt": 1,
                "title": "str",
                "authorName": "str",
                "storeName": "str"
            }
        }

class OTAItem(BaseModel):
    title: str
    storeName: str
    class Config:
        json_schema_extra = {
            "example": {
                "title": "str",
                "storeName": "str"
            }
        }

# class OTA2(BaseModel):
#     createdAt: int
#     title: str
#     authorName: str
#     storeName: str

# class OTAItems(BaseModel):
#     ota_lists: List[OTA2]


# from pydantic import BaseModel
# from typing import List, Optional
# from fastapi import Form
# from .replys import Replys
# from datetime import datetime

# class OTAS(BaseModel):
#     id: Optional[int]
#     item: str
#     createdAt: datetime
#     updatedAt: datetime
#     title: str
#     content: str
#     authorName: str
#     postAuthorID: str
#     passwd: str
#     storeName: str
#     storeCategory: str
#     replys: Optional[List[Replys]] = None

#     class Settings:
#         name = "users"

#     def as_form(
#         cls,
#         item: str = Form(...)
#     ):
#         return cls(item=item)
    
#     class Config:
#         schema_extra = {
#             "example": {
#                 "id": "번호를 정수로 입력하세요",
#                 "item": "샘플 스키마",
#                 "replys": [],
#             }
#         }

# class OTAItem(BaseModel):
#     item: str
#     updatedAt: datetime
#     title: str
#     content: str
#     authorName: str
#     storeName: str
#     storeCategory: str
#     class Config:
#         schema_extra = {
#             "example": {
#                 "item": "변경할 내용을 작성해 주세요"
#             }
#         }

# class OTAList(BaseModel):
#     otalists: List[OTAItem]

#     class Config:
#         schema_extra = {
#             "example": {
#                 "Todo List": [
#                     {"item": "Example Schema 1"},
#                     {"item": "Example Schema 2"}
#                 ]
#             }
#         }

    