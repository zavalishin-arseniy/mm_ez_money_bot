import json

class pas(object):
    def __init__(self,Id):
        self.id = Id
        self.d = []

    def distinct(self,name):
        for i in self.d:
            if i[0] == name:
                return False
        return True

    def add(self,name,score):
        if self.distinct(name):
            self.d.append((name,score))
            return True
        return False

    def get_list(self):
        s = ''
        for i in self.d:
            s += i[0] + '\n'
        return s

    def delete(self,name):
        for i in range(len(self.d)):
            if self.d[i][0] == name:
                del self.d[i]
                return True
        return False

    def delete_all(self):
        self.d = []

    def total(self):
        return sum([i[1] for i in self.d])

    def __str__(self):
        return str(self.d)

class db_obj(object):
    def __init__(self):
        self.index = []

    def append(self,pas):
        self.index.append(pas)
    
    def __getitem__(self,key):
        for pas in self.index:
            if pas.id == key:
                return pas
        return None

    def __setitem__(self,key,value):
        for i in range(len(self.index)):
            if self.index[i].id == key:
                self.index[i] = value
    
    def save(self):
        s = {}
        for pas in self.index:
            s[pas.id] = pas.d
        with open('db.json', 'w') as write_file:
            json.dump(s,write_file,indent=2)