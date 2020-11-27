# Collection

A utility data structure for python! This enpowers the power of dicts to the next level!<br/>
This module is inspired from discordjs collections

## Links

- [GitHub](https://github.com/Scientific-Guy/python-collection)
- [Pypi](https://pypi.org/project/python-collection/)
- [Discord Support Server](https://discord.gg/FrduEZd)

# Usage

```py
from Collection import Collection

mycol = Collection()

mycol.set('key', 'value')
print(mycol.get('key')) # Prints 'value'!
```

# Properties

```py
col.dict # The data stored in dict
col.size # The size of the dict len(self.dict)
col.keys # Returns the array of keys of dict
col.values # Returns the array of values of dict
col.items # Returns the items of values of dict [(key, value), ...]
```

# Basic methods

```py
col.set(key, value) # Sets a value to the dict
col.get(key) # Returns the value of the key, if no value then returns None
col.clear() # Similar to dict.clear()
col.has(key) # Returns a boolean wheater the key has its value!
```

# Utility methods

```py
col.first() # Returns the first value of the dict
col.first(2) # Returns the array of values of the dict from first to second
col.last() # Returns the last value of the dict 
col.last(2) # Returns the array of values of the dict from last to second last
col.random() # Returns a random value of the dict
col.random(2) # Returns a array of 2 random values of dict 

# Similar to the above functions there are methods to get the keys of it

col.firstkey() # Returns the first key of the dict
col.firstkey(2) # Returns the array of keys of the dict from first to second
col.lastkey() # Returns the last key of the dict 
col.lastkey(2) # Returns the array of keys of the dict from last to second last
col.randomkey() # Returns a random key of the dict
col.randomkey(2) # Returns a array of 2 random keys of dict 
```

# Extending a Collection

Extend the collection

```py
col1 = Collection()
col2 = Collection()

col1.set('key', 'value')
col2.extend(col1)

print(col2.get('key')) # Will return value
```

Will work with dicts too

```py
col = Collection()

col.extend({ 'key': 'value' })

print(col.get('key')) # Will return value
```

# Cloning

Will return a duplicate collection of the current collection

```py
print(col.clone())
```

# To a object

Convert the collection dict to object

```py
col = Collection()

col.set('key', 'value')
obj = col.to_object()

print(obj.key) # Returns value
```

# List methods

### Find

Find an item in the items of dict

```py
def find(key, value):
    return key == 'key'

print(col.find(find)) # Returns an item (key, value)
```

### Some

Verifies if the callback satisfies any of the items in the dict

```py
def some(key, value):
    return key == 'key'

print(col.some(some)) # Returns boolean stating the existence of the key which satisfies the callback
```

### Find

Find an item in the items of dict

```py
def find(key, value):
    return key == 'key'

print(col.find(find)) # Returns an item (key, value)
```

### FindMany

Find array of items which satisfies the callback

```py
def findmany(key, value):
    return key == 'key'

print(col.findmany(findmany)) # Returns an array of items (key, value)
```

### Sweep

Removes the item of the dict which satisfies the callback

```py
def sweep(key, value):
    return key == 'key'

print(col.sweep(sweep)) # Returns nothing
```

### Filter

Similar to sweep but instead returns a new duplicate collection and filters it

```py
def sweep(key, value):
    return key == 'key'

print(col.sweep(sweep)) # Returns a new collection
```

### Sweep

Removes the item of the dict which satisfies the callback

```py
def sweep(key, value):
    return key == 'key'

print(col.sweep(sweep)) # Returns an item (key, value)
```

### Maps

Maps the values of the dict and returns a duplicate collection

```py
col.set(1, 5) # Current value = { 1: 5 }

def map(key, value):
    return value + 1

print(col.map(map)) # Returns an collection
# Collection with value { 1: 6 }
```

### ForEach

Will run the function on each item

```py
def foreach(key, value):
    print(key)

print(col.foreach(foreach)) # Returns an item (key, value)
```

### Concat

Will return a duplicate collection by concatting the both collection

```py
col1 = Collection()
col2 = Collection()

col1.set('key', 'value')
print(col2.concat(col1)) # Will return value
```

Will work with dicts too

```py
col = Collection()

print(col.extend({ 'key': 'value' })) # Will print value
```