from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from beanie import PydanticObjectId 
from database.connection import Database
from models.otas import OTA

router = APIRouter()
ota_database = Database(OTA)

templates = Jinja2Templates(directory='templates/')

@router.get('/')
@router.post('/')
@router.delete('/')
async def mainPage(request: Request):
    otas = await ota_database.get_all()
    return templates.TemplateResponse(
        "main.html",
        {
            "request": request,
            "otas": otas
        }
    )