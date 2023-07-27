from fastapi import APIRouter, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates
from models.otas import OTA, OTAItem
from fastapi.responses import RedirectResponse

router = APIRouter()
ota_list = []

templates = Jinja2Templates(directory='templates/')

@router.post('/')
async def add_otas(request: Request, otas: OTA = Depends(OTA.as_form)) -> dict:
    otas.id = len(ota_list) + 1
    ota_list.append(otas)
    return RedirectResponse(url="http://localhost:8000/")

@router.get('/')
async def retrieve_otas(request: Request):
    return templates.TemplateResponse(
        "createOTA.html",
        {
            "request": request,
            "otas": ota_list
        }
    )

@router.get('/{ota_id}')
async def retrieve_otas(request: Request, ota_id: int) -> dict:
    for ota in ota_list:
        if ota.id == ota_id:
            return templates.TemplateResponse(
                "createOTA.html",
                {
                    "request": request,
                    "otas": ota_list
                    }
    )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Not In"
    )

# @router.post('/', status_code=status.HTTP_201_CREATED)
# async def add_otas(otas: OTA) -> dict:
#     ota_list.append(otas)
#     return {
#         "messages": "성공적인 저장!"
#     }
# @router.get('/')
# async def retrieve_otas():
#     return {
#         "otas": ota_list
#     }

# @router.get('/{ota_id}')
# async def retrieve_otas(ota_id: int) -> dict:
#     for ota in ota_list:
#         if ota.id == ota_id:
#             return {
#                 "ota": ota
#             }
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail="Not In"
#     )

# @router.put("/{ota_id}")
# async def update_ota(ota_data: OTAItem, ota_id: int) -> dict:
#     for ota in ota_list:
#         if ota.id == ota_id:
#             ota.title = ota.title if ota_data.title == "" else  ota_data.title
#             ota.storeName = ota.storeName if ota_data.storeName == "" else  ota_data.storeName
#             return {
#                 "ota": ota
#             }
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail="Not In"
#     )

# @router.delete('/')
# async def delete_ota_list() -> dict:
#     ota_list.clear()
#     return {
#         "message": "Deleted Successfully"
#     }

# @router.delete('/{ota_id}')
# async def delete_ota_list(ota_id: int) -> dict:
#     for i in range(len(ota_list)):
#         ota_item = ota_list[i]
#         if ota_item.id == ota_id:
#             ota_list.pop(i)
#             return {
#                 "message": "{}번째 오늘의 테이블이 삭제되었습니다.".format(ota_id)
#             }
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail="Not In"
#     )


##################

# from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
# from models.otas import OTAS, OTAItem
# from fastapi.templating import Jinja2Templates

# ota_list = []

# templates = Jinja2Templates(directory='templates/')

# router = APIRouter(
#     prefix="/otas",
#     tags = ["otas"],
#     responses={404: {"description": "Not found"}},
# )

# @router.get('/', tags=["otas"])
# async def get_otas() -> dict:
#     return {
#         "messages": "모든 오늘의 테이블 반환"
#     }

# @router.get('/{index}', tags=["otas"])
# async def get_otas(index: int) -> dict:
#     return {
#         "messages": "{}th 오늘의 테이블 반환".format(index)
#     }
