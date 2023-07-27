from pydantic import BaseModel
from typing import List, Optional
from fastapi import Form
from datetime import datetime

class Replys(BaseModel):
    voteID: Optional[int] = None
    createdAt: datetime
    updatedAt: datetime
    content: str
    author: str
    voteAuthorID: str
    passwd: str

    class Config:
        schema_extra = {
            "example": {
                "voteID": 1,
                "createdAt": "2023-07-27",
                "updatedAt": "2023-07-27",
                "content": "샘플 댓글 내용",
                "author": "John Doe",
                "voteAuthorID": "john_doe",
                "passwd": "샘플 비밀번호",
            }
        }