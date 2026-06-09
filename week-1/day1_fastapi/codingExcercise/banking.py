from fastapi import FastAPI

app=FastAPI()
print("BANKING APP LOADED")
@app.get("/")
def home():
    return "welcome to banking application"

@app.get("/users/{user_id}")
def getUserDetails(user_id: int):
    return {
    "account number": user_id
    }
@app.get("/search")
def getDetails(userName: str):
    return {
    "name":userName
    }