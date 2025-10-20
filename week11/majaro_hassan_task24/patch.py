from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()

# creating instance for fastapi
app = FastAPI(title= 'Second FastAPI App', version= '1.0.0')

# creating a data file to display
data = [
    {"name": "John Doe",  "age": 20, "track": "AI Engineering"}, 
    {"name": "John Smith",  "age": 21, "track": "Cybersecurity Analyst"},
    {"name": "Jane Doe",  "age": 22, "track": "SOC Analyst"}
]


# creating a validation for the response type expected
class item(BaseModel):
    name: str = Field (..., example = 'Hassan')        # the "..." makes each field required
    age: int = Field(..., example = 23)
    track: str = Field(..., example = 'AI Engineer')

class Update_item(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    track: Optional[str] = None


# creating patch to update and give it a desciption for the user to see
@app.patch("/update-data/{id}", description = "This is for updating file")
def update_data(id: int, input: Update_item):
    updated_file = data[id].update(input.model_dump(exclude_unset = True))
    print(updated_file)
    return {'Message': 'Data Updated', 'Data': data}


# Creating the delete action
@app.delete("/remove-data/{id}")
def delete_data(id: int):
    data.remove(data[id])
    return {'Message': 'Data Removed', 'Data': data}


if __name__ == "__main__":
    print(os.getenv("host"))
    print(os.getenv("port"))
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port")))