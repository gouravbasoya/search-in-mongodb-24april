from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from typing import List

app = FastAPI()

# MongoDB setup
client = MongoClient("mongodb+srv://gouravbasoya3:6fU2JcfOWJ3FQUd3@grocery.ikbmetg.mongodb.net/")
db = client["groceries"]
units_collection = db["units"]

@app.get("/search/", response_model=List[str])
def search_units(query: str):
    query_lower = query.lower()

    # Find where query exists in any all_related_units array
    result = units_collection.find_one({"all_related_units": {"$in": [query_lower]}})
    if result:
        return result["all_related_units"]

    raise HTTPException(status_code=404, detail="Unit not found")
