from utilities import Utilities


class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


class Students():
    def __init__(self):
        self.realName = ""
        self.Queready = ""

    def ImportFromJSON(self, jsonElement):
        self.realName = jsonElement['realName']
        self.Queready = jsonElement['Queready']


def main():
    data = Utilities.load_from_json('student.json')
    d = Deque()
    print("status of students ready to get registered:", d.isEmpty())
    for student in data['student']:
        s = Students()
        s.ImportFromJSON(student)
        d.addFront(s)
    for i in d.items:
        if i.Queready == "Yes":
            print(i.realName)
