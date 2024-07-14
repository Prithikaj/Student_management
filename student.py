import pymongo
from bson.objectid import ObjectId

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["student_management"]
collection = db["students"]

def add_student(student_data):
    # Insert a new student record into the database
    result = collection.insert_one(student_data)
    return result.inserted_id

def get_student(student_id):
    # Retrieve a student record by their MongoDB ObjectId
    student = collection.find_one({"_id": ObjectId(student_id)})
    return student

def update_student(student_id, new_data):
    # Update an existing student record
    collection.update_one({"_id": ObjectId(student_id)}, {"$set": new_data})

def delete_student(student_id):
    # Delete a student record
    collection.delete_one({"_id": ObjectId(student_id)})

if __name__ == "__main__":
    while True:
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            name = input("Enter Student Name: ")
            age = int(input("Enter Student Age: "))
            student_data = {"name": name, "age": age}
            student_id = add_student(student_data)
            print(f"Student added with ID: {student_id}")

        elif choice == "2":
            student_id = input("Enter Student ID: ")
            student = get_student(student_id)
            if student:
                print(f"Student Name: {student['name']}, Age: {student['age']}")
            else:
                print("Student not found")

        elif choice == "3":
            student_id = input("Enter Student ID: ")
            new_name = input("Enter New Name: ")
            new_age = int(input("Enter New Age: "))
            new_data = {"name": new_name, "age": new_age}
            update_student(student_id, new_data)
            print("Student updated successfully")

        elif choice == "4":
            student_id = input("Enter Student ID: ")
            delete_student(student_id)
            print("Student deleted successfully")

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")
