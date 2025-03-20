from fastapi import APIRouter

router = APIRouter()

@router.get("/compare")
async def compare_teams():
    return {"message": "Comparison results"}
