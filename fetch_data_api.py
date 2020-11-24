from fastapi import FastAPI
from alibi.datasets import fetch_adult
import json

app = FastAPI()
adult=fetch_adult()

def jsonfy_person(features, data, category_map):
    json_data={}
    j=0
    for i in range(0,len(data)-1):
        if i in category_map.keys():
            json_data[features[i]]=str(category_map[i][data[list(category_map.keys())[j]]])
            j=j+1
        else:
            json_data[features[i]]=str(data[i])
    return json_data

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/person/{id}")
async def read_item(id: int):
    person = adult.data[id]
    return jsonfy_person(adult.feature_names, person, adult.category_map)

@app.get("/api/person/{id}/ml")
async def read_item(id: int):
    person = adult.data[id]
    model_input = {"instances":[person.tolist()]}
    return model_input

