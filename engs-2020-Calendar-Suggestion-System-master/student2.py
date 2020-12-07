import json

def main():
    with open('teacher.json') as file_data:
        data = json.load(file_data)
        for month in data["month"]:
            with open('student.json') as file_data:
                student_data = json.load(file_data)
                for student in student_data["student"]:
                    if str(month["apeal"]) == "20":
                        if (month["day"]) in (student["student that apealed dates"]):
                            print("we want to inform that exam was taken down by your students")
                            student["student that apealed dates"].remove(month["day"])
                            break

            file = open("student.json","w")
            file.write(json.dumps(student_data, indent=2))
            file.close()



