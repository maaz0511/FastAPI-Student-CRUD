from pydantic import BaseModel, Field
from typing import Annotated

class MarksSchema(BaseModel):
    english: Annotated[int, Field(..., 
                                  ge=0,
                                  le=100,
                                  title="English Subject Marks")]
    hindi: Annotated[int, Field(..., 
                                  ge=0,
                                  le=100,
                                  title="Hindi Subject Marks")]
    maths: Annotated[int, Field(..., 
                                  ge=0,
                                  le=100,
                                  title="Math Subject Marks")]
    computer: Annotated[int, Field(..., 
                                  ge=0,
                                  le=100,
                                  title="Computer Subject Marks")]




class StudentSchema(BaseModel):
    id: Annotated[int, Field(...,
                             gt=0,
                             title="Student ID",
                             description="Unique ID of Student",
                             examples=[101,102,103])]
    
    name: Annotated[str, Field(...,
                               min_length=3,
                               max_length=50,
                               title="Student Name",
                               description="Name of student between 3 and 50 characters.")]
    
    age: Annotated[int, Field(..., gt=3, title="Student Age", description="Age of the student")]

    roll_num: Annotated[int, Field(..., gt=0, title="Student Roll Number", description="Roll Number of the student")]

    std_class: Annotated[int, Field(..., gt=0, title="Student Class", description="Class of the student")]

    marks: Annotated[MarksSchema, Field(..., title="Student Marks", description="Marks of the student")]

    contact: Annotated[int, Field(..., title="Student Contact", description="Contact of the student")]



class ResponseMessage(BaseModel):
    message: str
    student_information: StudentSchema