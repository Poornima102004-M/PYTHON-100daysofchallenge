class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def add(self, key, value):
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, value)
                    break
            else:
                self.table[index].append((key, value))

    def get(self, key):
        index = self._hash_function(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        raise KeyError(key)

    def remove(self, key):
        index = self._hash_function(key)
        if self.table[index] is not None:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    break
            else:
                raise KeyError(key)
        else:
            raise KeyError(key)

# Example usage
hash_table = HashTable(10)
hash_table.add("apple", 5)
hash_table.add("banana", 7)
hash_table.add("orange", 3)

print(hash_table.get("banana"))  # Output: 7

hash_table.remove("banana")
try:
    print(hash_table.get("banana"))
except KeyError as e:
    print(f"KeyError: {e}")  # Output: KeyError: 'banana'
