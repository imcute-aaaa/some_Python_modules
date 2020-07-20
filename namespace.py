#<using namespace <module>;>#
class NameSpace:
    def __init__(self):
        self.definednames = []
        self.names = {}
        self.lennames = 0

    def name(self, name=''):
        if name:
            return self.names[name]
        return self.names

    def appendname(self, name, val):
        self.names[name] = val
        if name not in self.definednames:
            self.lennames += 1
            self.definednames.append(name)

    def deletename(self, name):
        self.names[name] = None
        if name in self.definednames:
            self.lennames -= 1
            self.definednames.remove(name)
