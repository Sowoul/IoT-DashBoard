import json
import os
from flask import jsonify

class DBManager:

    def __init__(self, filename="store.json") -> None:
        self.data = []
        self.filename = filename
        self.load()
    
    def add(self, data):
        self.data.append(data)

    def get_data(self):
        return self.data

    def get_last(self):
        return self.data[-1]

    def add_at_idx(self,idx,data):
        if idx==None:
            self.data.append(data)
            return jsonify({'status': 'success'})
        self.data.insert(idx,data)
        self.save()
        return jsonify({'status': 'success'})

    def remove_at_idx(self,idx):
        if idx==None:
            return jsonify({'status': 'failure'})
        self.data.pop(idx)
        self.save()
        return jsonify({'status': 'success'})

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)

    def load(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = []

    def clear(self):
        self.data = []
        self.save()

if __name__ == '__main__':
    db = DBManager()
    print(db.get_data())
