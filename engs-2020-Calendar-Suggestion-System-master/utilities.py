import json


class Utilities:
    @staticmethod
    def load_from_json(json_path):
        with open(json_path, 'r') as file:
            data = json.load(file)
        return data

    @staticmethod
    def write_to_json(json_path, data):
        with open(json_path, 'w') as outfile:
            json.dump(data, outfile, indent=2)

    @staticmethod
    def add_student_to_hashtable(hashtable, data, CCL):
        for ix, student in enumerate(data['student']):
            s = CCL()
            s.ImportFromJSON(student)
            hashtable.put(str(ix), s)
        return hashtable

    @staticmethod
    def add_days_to_dll(dll, data, CCL):
        for month in data['month']:
            s = CCL()
            s.ImportFromJSON(month)
            dll.add(s)
        return dll

    @staticmethod
    def export_ht_data(hashtable, key):
        return {key: [hashitem.value.ExportToJSON({}) for hashitem in hashtable.slots if hashitem is not None]}

    @staticmethod
    def export_dll_data(dll, key):
        alldata = [dll.root.data.ExportToJSON({})]
        this_node = dll.root
        while this_node.has_next():
            this_node = this_node.get_next()
            alldata.append(this_node.data.ExportToJSON({}))
        return {key: alldata}
