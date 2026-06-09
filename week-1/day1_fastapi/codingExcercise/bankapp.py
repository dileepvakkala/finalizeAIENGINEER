from fastapi import FastAPI

app=FastAPI()

@app.get("/account/{acc_number}")
def getAccountNumber(acc_number: int):
    print("Entered into api")
    return {
    "account number": acc_number
    }
@app.get("/account")
def getAcctNumber(accounName: str):
    return {
    "name": accounName
    }