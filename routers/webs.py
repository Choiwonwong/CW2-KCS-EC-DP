from fastapi import APIRouter, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates
from models.otas import OTA, OTAItem
from routers.otas import ota_list

router = APIRouter()

templates = Jinja2Templates(directory='templates/')

@router.get('/')
@router.post('/')
async def retrieve_otas(request: Request):
    return templates.TemplateResponse(
        "main.html",
        {
            "request": request,
            "otas": ota_list
        }
    )