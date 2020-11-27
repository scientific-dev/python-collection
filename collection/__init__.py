import random

class CollectionObject():

    def __init__(self, _dict):
        self.__dict__.update(_dict)

class Collection():

    def __init__(self):
        self.dict = {}

    def set(self, key, value):
        self.dict[key] = value

    def get(self, key):
        if key not in self.dict: return None
        return self.dict[key]

    def delete(self, key):
        self.dict.pop(key)

    def clear(self):
        return self.dict.clear()

    def has(self, key):
        return key in self.dict.keys()

    @property
    def size(self):
        return len(self.dict)

    @property
    def keys(self):
        return list(self.dict.keys())

    @property
    def values(self):
        return list(self.dict.values())

    @property
    def items(self):
        return list(self.dict.items())

    def first(self, amount = None): 
        values = self.values

        if not amount:
            if self.size == 0: return None
            return self.dict[values[0]]
        
        items = values[0:(amount+1)]
        result = []
        for i in items: result.append(self.dict[i])
        return result

    def last(self, amount = None):
        values = self.values
        lastnum = self.size

        if not amount:
            if self.size == 0: return None
            return self.dict[values[lastnum-1]]
        
        items = values[(lastnum-amount):lastnum]
        result = []
        for i in items: result.append(self.dict[i])
        return result

    def random(self, amount = None):
        values = self.values

        if self.size == 0: return None
        if not amount: return self.dict[random.choice(values)]
        
        result = []
        for i in range(amount): result.append(self.dict[random.choice(values)])
        return result

    def firstkey(self, amount = None):
        keys = self.keys

        if not amount:
            if self.size == 0: return None
            return self.dict[keys[0]]
        
        items = keys[0:(amount+1)]
        result = []
        for i in items: result.append(self.dict[i])
        return result

    def lastkey(self, amount = None):
        keys = self.keys
        lastnum = self.size

        if not amount:
            if self.size == 0: return None
            return self.dict[keys[lastnum-1]]
        
        items = keys[(lastnum-amount):lastnum]
        result = []
        for i in items: result.append(self.dict[i])
        return result

    def randomkey(self, amount = None):
        keys = self.keys

        if self.size == 0: return None
        if not amount: return self.dict[random.choice(keys)]
        
        result = []
        for i in range(amount): result.append(self.dict[random.choice(keys)])
        return result

    def find(self, fn):
        if not callable(fn): raise TypeError('invalid function provided!')

        for i in self.items: 
            if fn(i[0], i[1]): return i

        return None

    def some(self, fn):
        if not callable(fn): raise TypeError('invalid function provided!')

        for i in self.items: 
            if fn(i[0], i[1]): return True

        return False

    def findmany(self, fn):
        if not callable(fn): raise TypeError('invalid function provided!')
        result = []

        for i in self.items: 
            if fn(i[0], i[1]): result.append(i)

        return result

    def sweep(self, fn):
        if not callable(fn): raise TypeError('invalid function provided!')

        for i in self.items: 
            if fn(i[0], i[1]): self.delete(i[0])
    
    def filter(self, fn):
        if not callable(fn): raise TypeError('invalid function provided!')
        result = Collection()
        result.extend(self)

        for i in self.items: 
            if fn(i[0], i[1]): result.delete(i[0])

        return result

    def map(self, fn):
        if not callable(fn): raise TypeError('invalid function provided!')

        col = Collection()
        col.extend(self)
        values = self.values
        keys = self.keys

        for i in range(self.size-1):
            col.set(keys[i], fn(keys[i], values[i]))

        return col

    def foreach(self, fn):
        if not callable(fn): raise TypeError('invalid function provided!')
        for i in self.items: fn(i[0], i[1])

    def concat(self, *args):
        x = Collection()

        for collection in args:
            items = collection.items
            if(isinstance(collection, dict)): items = collection.items()

            for i in items:
                x.set(i[0], i[1])

        return x

    def extend(self, *args):
        for collection in args:
            items = collection.items
            if(isinstance(collection, dict)): items = collection.items()

            for i in items:
                self.set(i[0], i[1])

    def clone(self):
        col = Collection()
        col.extend(self.dict)
        return col

    def to_object(self):
        return CollectionObject(self.dict)

    def __str__(self):
        return 'Collection({size}) {dict}'.format(size = self.size, dict = str(self.dict))