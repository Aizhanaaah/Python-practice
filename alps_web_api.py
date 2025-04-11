from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange


class Post(BaseModel):
    Name: str
    City: str
    price: int
    rating : Optional[int] = None

app = FastAPI()

inputs = [{"Name" : "Peak Lenin", "City" : "Bishkek", "price":5000, "id" : 1}, {"Name" : "Tian-Shan", "City" : "Naryn", "price" : 3800, "id" : 2}]

def findpost(id):
    for p in inputs:
        if p["id"] == id:
            return p

@app.get("/")
def home():
    return {"message": "Hello! Welcome to Alps, and discover breathtaking places in Kyrgyzstan"}

@app.get("/post")
def content():
    return {"inputs" : inputs}


@app.post("/createpost")
def create(post: Post):
    post_dict = post.dict()
    for item in inputs:
        if item.get("Name") == post_dict["Name"] and item.get("City") == post_dict["City"]:
            return {"message": "This post already exists."}
    post_dict["id"] = randrange(0, 10000000)
    inputs.append(post_dict)
    return {"data": post_dict}

@app.get("/post/{id}")
def get_post(id: int):
    post = findpost(id)
    print(post)
    return {"post_detail" : post}
