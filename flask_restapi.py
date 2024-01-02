from flask import Flask, request, jsonify
from flask import Api, Resource
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['university_db']
faculty_collection = db['faculty']

class FacultyResource(Resource):
    def get(self, employee_id=None):
        if employee_id:
            faculty = faculty_collection.find_one({"Employee Id": employee_id})
            if faculty:
                return jsonify(faculty)
            else:
                return {"message": "Faculty not found"}, 404
        else:
            faculties = list(faculty_collection.find())
            return jsonify(faculties)

    def post(self):
        faculty_data = request.json
        faculty_collection.insert_one(faculty_data)
        return {"message": "Faculty added successfully"}, 201

    def put(self, employee_id):
        faculty_data = request.json
        faculty_collection.update_one({"Employee Id": employee_id}, {"$set": faculty_data})
        return {"message": "Faculty updated successfully"}

    def delete(self, employee_id):
        faculty_collection.delete_one({"Employee Id": employee_id})
        return {"message": "Faculty deleted successfully"}

class FacultyPost(Resource):
    def post(self):
        faculty_data = request.json
        faculty_collection.insert_one(faculty_data)
        return {"message": "Faculty added successfully"}, 201

# Add the FacultyResource and FacultyPost to the Flask API
api.add_resource(FacultyResource, '/api/faculty', '/api/faculty/<employee_id>')
api.add_resource(FacultyPost, '/api/faculty/post')

if __name__ == '__main__':
    app.run(debug=True)
