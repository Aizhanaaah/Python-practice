from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Салам, SanaSave иштеп жатат!"}

@app.get("/today")
def content():
    return {"income" : 0}
