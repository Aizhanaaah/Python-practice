from fastapi import FastAPI, Response, status, HTTPException
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
        

def find_index_post(id):
    for i, p in enumerate(inputs):
        if p["id"] == id:
            return i




@app.get("/")
def home():
    return {"message": "Hello! Welcome to Alps, and discover breathtaking places in Kyrgyzstan"}

@app.get("/post")
def content():
    return {"inputs" : inputs}


@app.post("/createpost", status_code=status.HTTP_201_CREATED)
def create(post: Post):
    post_dict = post.dict()
    for item in inputs:
        if item.get("Name") == post_dict["Name"] and item.get("City") == post_dict["City"]:
            return {"message": "This post already exists."}
    post_dict["id"] = randrange(0, 10000000)
    inputs.append(post_dict)
    return {"data": post_dict}



@app.get("/post/latest")
def get_lates_post():
    post = inputs[len(inputs)-1]
    return {"detail" : post}


@app.get("/post/{id}")
def get_post(id: int, respose: Response):
    post = findpost(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"message" : f"post with id: {id} was not found"})
       #respose.status_code = status.HTTP_404_NOT_FOUND
       #return {"message" : f"post with id: {id} was not found"}
    return {"post_detail" : post}


@app.delete("/post/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    #deleting post
    #find the index in the array that has required
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} doesn't exist")
    inputs.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/post/{id}")
def update_post(id: int, post: Post):

    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} doesn't exist")
        inputs.pop(index)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    post_dict = post.dict()
    post_dict['id'] = id
    inputs[index] = post_dict
    return {'data' : post_dict}
