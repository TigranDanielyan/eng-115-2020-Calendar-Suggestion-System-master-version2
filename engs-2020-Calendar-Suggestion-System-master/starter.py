import student
import teacher
import student2
import administrator
import administration2
import DoubleLinkListAndTeacher2
import Queue

print("information date that got take downs: ")
student2.main()
DoubleLinkListAndTeacher2.main()
print("information about Students ready to be registered: ")
Queue.main()

ask = input("If you want to enter Teacher system please enter teacher. If you are a studnet pleas enter student.If you are Administrator please enter administrator. In you Are a student waiting to get your account enter register.  ")
if ask == "teacher":
    print("starting teacher operations")
    teacher.main()

elif ask == "student":
    print ("starting student operations")
    student.main()
elif ask == "administrator":
    print("starting administrator operations")
    administrator.main()

elif ask == "register":
    print ("starting register operations")
    administration2.main()

else:
    print(f"There is no command like {ask}")