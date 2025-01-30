from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

# os.environ.get('54367')

app = Flask(__name__)
CORS(app)  # Enable CORS to allow GET requests from any origin

# Load student data from the JSON file
with open("q-vercel-python.json") as f:
    students = json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    # Get names from query parameters
    names = request.args.getlist('name')
    
    # Retrieve the marks for the provided names
    marks = []
    for name in names:
        # Iterate over students list and check if the student's name matches
        student_found = False
        for student in students:
            if student.get('name') == name:
                marks.append(student.get('marks', "Marks not found"))
                student_found = True
                break
        
        if not student_found:
            marks.append("Student not found")
    
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run(debug=True)

