import json

def main():
  type = input("give us your name")
  with open('student.json') as file_data:
    student_data = json.load(file_data)
    for student in student_data["student"]:
      if type == (student["name"]):
         type = input("give us your password")
         if type == (student["password"]):
           type = input("do what to see exams dates and cancel exam date (yes or no)? ")
           if type == "yes":
             print("starting showing exam dates")
             print("here are all exam dates")
             with open('teacher.json') as file_data:
               teacher_data = json.load(file_data)
               for month in teacher_data["month"]:
                   if (month["filled"] == "Yes"):
                       print(month["day"])
               type = input("choose the date you want to apeal (if there is none please press 0)")
               for month in teacher_data["month"]:
                    if type == (month["day"]):
                       if type not in (student["student that apealed dates"]):
                           student["student that apealed dates"].append(type)
                           print("startinng apeal")
                           month["apeal"] = month["apeal"] + 1
                           break
                       else:
                           if type in (student["student that apealed dates"]):
                               print("you can't Apeal the same date")
                               break
                    else:
                       if type =="0":
                           print("sorry for there being no exams")
                           break

               file = open("student.json", "w")
               file.write(json.dumps(student_data, indent=2))
               file.close()

               file = open("teacher.json", "w")
               file.write(json.dumps(teacher_data, indent=2))
               file.close()

           if type == "no":
              print("shutdown")
              break

           break

