from fastapi import APIRouter, HTTPException
from app.database import add_team, get_all_teams
from app.models import Team

router = APIRouter()

@router.post("/teams")
async def create_team(team: Team):
    try:
        add_team(team)
        return {"message": "Team added successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/teams")
async def list_teams():
    return get_all_teams()
