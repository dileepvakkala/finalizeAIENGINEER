from fastapi import FastAPI

app=FastAPI()

@app.get("/users/{user_name}")
def userdetails(user_name: str):
    return {
      "name":user_name,
      "id":206427
    }