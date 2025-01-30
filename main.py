from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI()

# Enable CORS to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load the CSV file into memory
def load_students_data():
    students = []
    with open("students.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({
                "studentId": int(row["studentId"]),
                "class": row["class"]
            })
    return students

# Endpoint to get student data
@app.get("/api")
def get_students(classes: list[str] = Query(default=[], alias="class")):
    students_data = load_students_data()
    
    # Filter students by class if classes are provided
    if classes:
        filtered_students = [student for student in students_data if student["class"] in classes]
        return {"students": filtered_students}
    
    # Return all students if no class filter is applied
    return {"students": students_data}

# Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)