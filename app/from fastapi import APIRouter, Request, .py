from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
from firebase_admin import auth
from starlette.middleware.sessions import SessionMiddleware

router = APIRouter()

def get_current_user(request: Request):
    user = request.session.get("user")
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return user

@router.post("/login")
async def login(request: Request):
    data = await request.json()
    id_token = data.get("idToken")
    if not id_token:
        raise HTTPException(status_code=400, detail="Missing ID token")
    
    try:
        decoded_token = auth.verify_id_token(id_token)
        request.session["user"] = decoded_token
        return JSONResponse(content={"message": "Login successful"})
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.post("/logout")
async def logout(request: Request):
    request.session.clear()
    return JSONResponse(content={"message": "Logged out successfully"})

@router.get("/user")
async def get_user(user: dict = Depends(get_current_user)):
    return JSONResponse(content=user)
