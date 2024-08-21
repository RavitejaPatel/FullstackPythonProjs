from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
 1: {
  "name":"Sam",
  "age":"22",
  "year":"2000"
 }
}

class Student(BaseModel):
 name: str
 age: int
 year: str

class UpdateStudent(BaseModel):
 name: Optional[str] = None
 age: Optional[int] = None
 year: Optional[str] = None

@app.get("/")
def index():
 return {"name": "Raviteja"}

# path param example
@app.get("/getStudent/{student_id}")
def getStudent(student_id: int = Path(description="The ID of the student you want to view", gt=0)):
 return students[student_id]

# query param example - google.com/results?search=python
@app.get("/getByName")
def getByName(name: Optional[str]=None):
 for student_id in students:
  if students[student_id]["name"]==name:
   return students[student_id]
  return {"Data": "Not found"}
 
  # combining path and query params
@app.get("/get_by_name/{student_id}")
def get_Student(*, student_id: int, name: Optional[str]=None ):
 for student_id in students:
  if students[student_id]["name"]==name:
   return students[student_id]
  return {"Data": "Not found"}
 

@app.post("/create_student/{student_id}")
def create_Student(student_id: int, student : Student):
    if student_id in students:
      return {"message": "A student with ID already exist"}
    students[student_id] = student_id
    return {"Message": "Response 200, created successfully"}

@app.put("/update_student/{student_id}")
def update_Student(student_id: int, student : UpdateStudent):
    if student_id not in students:
      return {"message": "A student with ID not exist"}
    students[student_id] = student
    return {"Message": "Response 200, updates successfully"}