from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

#Validate the incoming JSON data using Pydantic
class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

inventory = {
}

@app.get("/get-item/{item_id}")
def order(item_id:int = Path(..., description="The ID of the item you would like")):
    return inventory[item_id]

#assigning query parameter (?) in FastAPI
@app.get("/get-name")
def name(*, name:Optional[str] = None):                # can't call endpoint if there are no query parameter (name:str) to not be required add (name:str=None)...
    for item_id in inventory:                          # add asterisk (*) - accepts unlimited positional args, and the rest as kwargs para sa arrangement.
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data":"Not found"}

@app.post("/create-item/{item_id}")
def create(item_id:int, item:Item):                  #item - Expect a JSON body that matches the Item class. Automatically parse it into an item object and make sure it’s valid
    if item_id in inventory:
        return {"Error": "Item ID already exists"}

    inventory[item_id] = item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update(item_id:int, item:UpdateItem):
    if item_id not in inventory:
        return {"Error": "Item ID does not exists"}

    if item.name:
        inventory[item_id].name = item.name
    if item.brand:
        inventory[item_id].brand = item.brand
    if item.price:
        inventory[item_id].price = item.price

    return inventory[item_id]

@app.delete("/delete-item/{item_id}")
def delete(item_id:int):
    if item_id not in inventory:
        return {"Error":"Item ID does not exist"}
    del inventory[item_id]
    return {"Success": "Item deleted"}


# Running the API:
# on terminal
# uvicorn main:app --reload           main = the name of the python file

# @app.get("/")            #depends on the method that you want to use (app.get/post/put/delete/...)
# def home():
#     return {"Data":"Testing"}

# @app.get("/about")
# def about():
#     return {"Data":"About"}
