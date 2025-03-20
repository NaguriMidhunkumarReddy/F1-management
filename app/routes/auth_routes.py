from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.responses import JSONResponse, RedirectResponse
from firebase_admin import auth
import requests
from app.config import settings  # Ensure settings include FIREBASE_API_KEY

router = APIRouter()

def verify_firebase_token(token: str):
    """ Verify Firebase authentication token. """
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception:
        return None

@router.post("/register")
async def register_user(request: Request):
    """ Registers a new user in Firebase Authentication. """
    data = await request.json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        raise HTTPException(status_code=400, detail="Email and password are required")

    try:
        user = auth.create_user(email=email, password=password)
        return JSONResponse(content={"message": "User created successfully", "uid": user.uid})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
async def login_user(request: Request, response: Response):
    """ Logs in the user and sets session cookie. """
    data = await request.json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        raise HTTPException(status_code=400, detail="Email and password are required")

    try:
        # Authenticate with Firebase
        firebase_response = requests.post(
            "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword",
            params={"key": settings.FIREBASE_API_KEY},
            json={"email": email, "password": password, "returnSecureToken": True},
        )
        result = firebase_response.json()

        if "idToken" not in result:
            raise HTTPException(status_code=400, detail=result.get("error", {}).get("message", "Login failed"))

        # Store session token as a secure cookie
        response.set_cookie(key="firebase_token", value=result["idToken"], httponly=True)

        # Redirect user to home or dashboard
        return RedirectResponse(url="/dashboard", status_code=303)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/logout")
async def logout_user(response: Response):
    """ Clears the user's session by deleting the authentication cookie. """
    response.delete_cookie("firebase_token")
    return JSONResponse(content={"message": "Logged out successfully"})

