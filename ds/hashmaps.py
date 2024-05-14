from typing import Optional, Union, List


class HashMap():
    def __init__(self, capacity: int=100):
        self.capacity: int = capacity
        self.size = 0
        self.array: List = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.array[index]
        for idx, (k, v) in enumerate(bucket):
            if k == key:
                bucket[idx] = (key, value)
                return
        
        bucket.append((key, value))
        self.size += 1

    def get(self, key):
        index = self._hash(key)
        bucket = self.array[index]
        for (k, v) in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self._hash(key)
        bucket = self.array[index]
        for idx, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[idx]
                self.size += 1
                return v
        return None


class DynamicHashMap(object):
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.array = [None for _ in range(self.capacity)]
    
    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        index = self._hash(key)
        array_value = self.array[index]
        if array_value and array_value[0] != key:
            self._rehash(key, value)
            return
        if array_value and array_value[0] == key:
            self.array[index] = (key, value)
            return
        self.array[index] = (key, value)
        self.size += 1

    def get(self, key):
        index = self._hash(key)
        value = self.array[index]
        return value[1] if isinstance(value, tuple) else None

    def _rehash(self, key, value):
        self.capacity = self.capacity * 4
        tmp = [None for _ in range(self.capacity)]
        for element in self.array:
            if not element:
                continue
            k, v = element
            index = self._hash(k)
            tmp[index] = (k, v)
        index = self._hash(key)
        tmp[index] = (key, value)
        self.size += 1
        self.array = tmp

    def delete(self, key):
        index = self._hash(key)
        value = self.array[index]
        del self.array[index]
        return value[1] if isinstance(value, tuple) else None
