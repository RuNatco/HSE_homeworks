# hash table with linear probing for strings
class HashTable:
    def __init__(self, size = 42):
        self.size = size
        self.table = [None] * size

    def polynomial_hash(self, key, p=10**9+7, x=257):
        hash_value = 0
        for char in key:
            hash_value = (hash_value * x + ord(char)) % p
        return hash_value % self.size

    def insert(self, key, value):
        if self.needs_resize():
            self.resize()
        index = self.polynomial_hash(key)
        if self.table[index] is None:
            self.table[index] = []

        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                self.table[index][i] = (key, value)
                return

        self.table[index].append((key, value))
    

    def search(self, key):
        index = self.polynomial_hash(key)
        if self.table[index] is not None:
            for item in self.table[index]:
                if item[0] == key:
                    return item[1]
        return None
    

    def delete(self, key):
        index = self.polynomial_hash(key)
        if self.table[index] is not None:
            for i, item in enumerate(self.table[index]):
                if item[0] == key:
                    self.table[index].pop(i)
                    return True
        return False
    

    def resize(self):
        new_size = self.size * 2
        new_table = [None] * new_size
        old_table = self.table
        self.table = new_table
        self.size = new_size
        for chain in old_table:
            if chain is not None:
                for key, value in chain:
                    index = self.polynomial_hash(key)
                    if self.table[index] is None:
                        self.table[index] = []
                    self.table[index].append([key, value])

    def needs_resize(self):
        num_elements = sum(len(item) for item in self.table if item is not None)
        return num_elements > self.size * 0.7
    

    