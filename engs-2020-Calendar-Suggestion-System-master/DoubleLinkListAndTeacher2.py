from utilities import Utilities


class Node(object):

    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_prev(self):
        return self.prev_node

    def set_prev(self, p):
        self.prev_node = p

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d

    def to_string(self):
        return "day" + str(self.data)

    def has_next(self):
        if self.get_next() is None:
            return False
        return True


class DoublyLinkedList(object):

    def __init__(self, r=None):
        self.root = r
        self.last = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, d):
        if self.size == 0:
            self.root = Node(d)
            self.last = self.root
        else:
            new_node = Node(d, self.root)
            self.root.set_prev(new_node)
            self.root = new_node
        self.size += 1

    def remove(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.get_data() == d:
                if this_node.get_prev() is not None:
                    if this_node.has_next():
                        this_node.get_prev().set_next(this_node.get_next())
                        this_node.get_next().set_prev(this_node.get_prev())
                    else:
                        this_node.get_prev().set_next(None)
                        self.last = this_node.get_prev()
                else:
                    self.root = this_node.get_next()
                    this_node.get_next().set_prev(self.root)
                self.size -= 1
                return True
            else:
                this_node = this_node.get_next()
        return False

    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.get_data() == d:
                return d
            elif this_node.get_next() == self.root:
                return False
            else:
                this_node = this_node.get_next()

    def print_list(self):
        print("Print Days List..........")
        if self.root is None:
            return
        this_node = self.root
        print(this_node.to_string())
        while this_node.has_next():
            this_node = this_node.get_next()
            print(this_node.to_string())


class Month():
    def __init__(self):
        self.day = ""
        self.filled = "No"
        self.apeal = ""

    def ImportFromJSON(self, jsonElement):
        self.day = jsonElement['day']
        self.apeal = jsonElement['apeal']

    def ExportToJSON(self, jsonElement):
        jsonElement['day'] = self.day
        jsonElement['filled'] = self.filled
        jsonElement['apeal'] = self.apeal
        return jsonElement

def main():
    data = Utilities.load_from_json('teacher.json')
    apealed_days = DoublyLinkedList()
    dll = Utilities.add_days_to_dll(DoublyLinkedList(),data,Month)
    this_node = dll.root
    while this_node.has_next():
        if this_node.data.apeal == 20:
            apealed_days.add(this_node.data.day)
            this_node.data.apeal = 0
        this_node = this_node.get_next()
    if apealed_days.get_size() > 0:
        apealed_days.print_list()
        print(f'Appeal was made for {apealed_days.get_size()} days this month')
    Utilities.write_to_json('teacher.json', Utilities.export_dll_data(dll, "month"))

main()