from fastapi import FastAPI
from enum import Enum

app = FastAPI()



class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    kokogambo = "kokogambo"



@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": {model_name}, "message": "Deep Learning FTW!"}
    
    if model_name.value == model_name.kokogambo.value:
        return {"model_name": {model_name}, "message": "LEARN X in world"}
    
    if model_name.value ==  "resnet":
        return {"model_name": {model_name}, "message": "LeCNN all the images"}
    
    return {"model_name": {model_name}, "message": "Have some residuals"}


