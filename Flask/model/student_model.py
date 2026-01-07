import json
import os

Datafile = os.path.join("data","student.json")

def read_students():
    with open(Datafile,'r') as f:
        return json.load(f)
    
def write_student(data):
    with open(Datafile,'w') as f:
        json.dump(data,f,indent=4)

def add_student(student):
    students = read_students() #from file studnets
    students.append(student)
    write_student(students)

def delete_student(id):
    students = read_students()
    for s in students:
        if s["id"]!=id:
            students.append(s)
    write_student(students)

   