import json

def main():
    type = input("do you what to start new exam (yes or no) ")
    if type == "yes":
        type = input("do you want to find a slot or you have a date ")
        if type == "find":
            print("empty days are")
            with open('teacher.json') as file_data:
                data = json.load(file_data)
                for month in data ["month"]:
                    if (month["filled"]) == "No":
                        print (month["day"])
        else:
            if type == "date":
                with open('teacher.json') as file_data:
                    data = json.load(file_data)
                    type = input ("please enter the day of the exam from 1-31 ")
                    for month in data["month"]:
                        if type == (month["day"]):
                            if (month["filled"]) == "Yes":
                                print("sorry it is taken, take another")
                                with open('teacher.json') as file_data:
                                    data = json.load(file_data)
                                    for index in range(len(data["month"])):
                                        month = data["month"][index]
                                        if (month["day"] == type and data["month"][index-1]["filled"] == "No"):
                                            print(data["month"][index-1]["day"])
                                        if (month["day"] == type and data["month"][index+1]["filled"] == "No"):
                                            print(data["month"][index+1]["day"])
                                        else:
                                            if (month["day"] == type and data["month"][index - 1]["filled"] == "Yes") and (month["day"] == type and data["month"][index+1]["filled"] == "Yes"):
                                                print("the day before and after were taken no free slots are near")


                            else:
                                if (month["filled"]) == "No":
                                    print(month["day"], "is free, you took it")
                                    month["filled"] = "Yes"

                    file = open("teacher.json", "w")
                    file.write(json.dumps(data, indent=2))
                    file.close()
    else:
        if type == "no":
            print("shutdown")
