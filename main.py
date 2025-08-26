from fastapi import FastAPI, HTTPException
from schemas import StudentSchema, ResponseMessage
from logic import load_data, save_data

app = FastAPI(title="Student CRUD API", description="A simple FastAPI project demonstrating CRUD operations for managing student records.")

# 1. Home Route
@app.get("/")
def home():
    """Return a welcome message for the Student CRUD API."""
    return {"message":"Welcome to FastAPI project that shows CRUD operation.",
            "Swagger_UI":"https://fastapi-student-crud-3tpn.onrender.com/docs",
            "ReDoc_UI":"https://fastapi-student-crud-3tpn.onrender.com/redoc"}

# 2. View All Students Data
@app.get("/students", response_model=list[StudentSchema])
def view_students():
    """Retrieve and return all students sorted by ID."""
    data = load_data()
    data = sorted(data, key=lambda student: student["id"]) # display sorted details
    return data

# 3. View Student By Id
@app.get("/students/{student_id}", response_model=StudentSchema)
def view_student(student_id: int):
    """Retrieve a single student record by its ID."""
    data = load_data()
    for student in data:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student Not Found !!!")

# 4. Add Student 
@app.post("/students", response_model=ResponseMessage)
def add_student(student_detail: StudentSchema):
    """Add a new student record to the database."""
    data = load_data()
    for student in data:
        if student["id"] == student_detail.id:
            raise HTTPException(status_code=409,detail="Student Already Exists !!!")
    data.append(student_detail.model_dump())
    save_data(data)
    return {"message":"Student Added",
                    "student_information":student_detail}

# 5. Update Student
@app.put("/students/{student_id}", response_model=ResponseMessage)
def update_student(student_id: int, updated_detail: StudentSchema):
    """Update an existing student record by its ID."""
    data = load_data()
    for index, student in enumerate(data):
        if student["id"] == student_id:
            data[index] = updated_detail.model_dump()
            save_data(data)
            return {"message":"Student Updated",
                    "student_information":updated_detail}
    
    raise HTTPException(status_code=404, detail="Student Not Found !!!")

# 6. Delete Student Detail
@app.delete("/students/{student_id}", response_model=ResponseMessage)
def delete_student(student_id: int):
    """Delete a student record from the database by its ID."""
    data = load_data()
    for index, student in enumerate(data):
        if student["id"] == student_id:
            deleted_student = data.pop(index)
            save_data(data)
            return {"message":"Student Deleted",
                    "student_information":StudentSchema(**deleted_student)}
    
    raise HTTPException(status_code=404, detail="Student Not Found !!!")