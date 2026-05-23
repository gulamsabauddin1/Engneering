from fastapi import FastAPI
from pydantic import BaseModel  
from typing import List

app = FastAPI()


class Student_info(BaseModel):
    pin:int
    name:str
    cource:str
    
#creating a list which stores the student information with datatypes defined in the Student_info class    
student:List[Student_info] = []

#get()=> to show data sent from server on website
#post()=> to send data from website to server
#put()=> to update data on server from website
#delete()=> to delete data on server from website 



@app.get("/")
def read_root():
    return{"Welcome":"Welcome to FastAPI!"}

@app.get("/students")
def read_students():
    return student

@app.post("/students")
def add_student(input:Student_info):
    student.append(input)
    return student
    print("Student added successfully!")
    return {"message":"Student added successfully!"}

@app.put("/students/{pin}")
def update_student(pin:int, input:Student_info):
    for i in range(len(student)):
        if student[i].pin == pin:
            student[i] = input
            return {"message":"Student updated successfully!"}
    return {"message":"Student not found!"}

@app.delete("/students/{pin}")
def delete_student(pin:int):
    for i in range(len(student)):
        if student[i].pin == pin:
            student.pop(i)
            return{"message":"Student deleted successfully!"}
    return {"message":"Student not found!"}
