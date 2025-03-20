from fastapi import APIRouter, HTTPException
from app.database import add_driver, get_all_drivers
from app.models import Driver

router = APIRouter()

@router.post("/drivers")
async def create_driver(driver: Driver):
    try:
        add_driver(driver)
        return {"message": "Driver added successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/drivers")
async def list_drivers():
    return get_all_drivers()
