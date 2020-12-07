import HashTable3


def main():
    print("you as an administrator body can add and delete students for the start of the cycle of exam day starts")
    type = input("if you need to add student from list please enter Add in opposite case please enter Delete")
    if type == "Add":
        HashTable3.creator()
    elif type == "Delete":
        HashTable3.deleter()
    else:
        print("something went wrong proggram ends")
