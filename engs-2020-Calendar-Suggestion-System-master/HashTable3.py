from utilities import Utilities


class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:

    def __init__(self):
        self.size = 256
        self.slots = [None for i in range(self.size)]
        self.count = 0

    def _hash(self, key):
        multiplayer = 1
        hash_value = 0
        for character in key:
            hash_value += multiplayer * ord(character)
            multiplayer += 1
        return hash_value % self.size

    def put(self, key, value):
        item = HashItem(key, value)
        hash_value = self._hash(key)
        while self.slots[hash_value] is not None:
            if self.slots[hash_value].key is key:
                break
            hash_value = (hash_value + 1) % self.size
        if self.slots[hash_value] is None:
            self.count += 1
        self.slots[hash_value] = item

    def get(self, key):
        hash_value = self._hash(key)
        while self.slots[hash_value] is not None:
            if self.slots[hash_value].key is key:
                return self.slots[hash_value].value
            hash_value = (hash_value + 1) % self.size
        return None

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)


class Student:
    def __init__(self):
        self.realName = ''
        self.Admincode = ''
        self.Queready = 'No'
        self.Name = ''
        self.Password = ''
        self.StudentThatApealedDates = []

    def ImportFromJSON(self, jsonElement):
        self.realName = jsonElement['realName']
        self.Admincode = jsonElement['Admincode']
        self.Name = jsonElement['name']
        self.Password = jsonElement['password']

    def ExportToJSON(self, jsonElement):
        jsonElement['realName'] = self.realName
        jsonElement['Admincode'] = self.Admincode
        jsonElement['Queready'] = self.Queready
        jsonElement['name'] = self.Name
        jsonElement['password'] = self.Password
        jsonElement['student that apealed dates'] = self.StudentThatApealedDates
        return jsonElement

    def GetElements(self):
        return vars(self)


def creator():
    data = Utilities.load_from_json('student.json')
    k1 = input("please write real name")
    l1 = input("please input random letters and numbers to genrate the Admincode")
    HT = Utilities.add_student_to_hashtable(HashTable(), data, Student)
    S = Student()
    S.Admincode = str(HT._hash(l1))
    S.Queready = "Yes"
    S.realName = k1
    HT.put("key1", S)
    S.ExportToJSON({})
    Utilities.write_to_json('student.json', Utilities.export_ht_data(HT, 'student'))


def adder():
    data = Utilities.load_from_json('student.json')
    HT = Utilities.add_student_to_hashtable(HashTable(), data, Student)
    l2 = input("please enter your real name")
    l3 = input("please enter AdminCode provided to you")
    found = False
    for student in HT.slots:
        if student is not None:
            s = student.value
            if l2 == s.realName and l3 == s.Admincode:
                found = True
                k4 = input("please write user name")
                k5 = input("please enter your password")
                s.Name = k4
                s.Password = k5
                s.Queready = "No"
    print(f"student {l2} not found") if found == False else print("success")
    Utilities.write_to_json('student.json', Utilities.export_ht_data(HT, 'student'))


def deleter():
    data = Utilities.load_from_json('student.json')
    HT = Utilities.add_student_to_hashtable(HashTable(), data, Student)
    l2 = input("please enter your real name")
    l3 = input("please enter AdminCode provided to you")
    found = False
    for key, student in enumerate(HT.slots):
        if student is not None:
            s = student.value
            if l2 == s.realName and l3 == s.Admincode:
                found = True
                HT.slots[key] = None
    print(f"student {l2} not found") if found == False else print("success")
    Utilities.write_to_json('student.json', Utilities.export_ht_data(HT, 'student'))
