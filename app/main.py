from fastapi import FastAPI
from app.routes import teams, compare,drivers

app = FastAPI()

# Include the routers
app.include_router(teams.router)
app.include_router(compare.router)
app.include_router(drivers.router)

@app.get("/")
async def home():
    return RedirectResponse(url="/index.html")

@app.get("/dashboard")
async def dashboard():
    """ This page should only be accessible after login. """
    return {"message": "Welcome to the Dashboard!"}
