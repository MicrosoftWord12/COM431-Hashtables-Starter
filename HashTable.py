from docutils.utils.math.latex2mathml import modulo_functions

import linkedlist
import random
import math
TupleLinkedList = linkedlist.TuplesLinkedList

class HashTable:
    def __init__(self):
        self.buckets = [None] * 127
        # self.buckets = [TupleLinkedList() for i in range(127)]

    def __hash(self, key):
        hashNumber = 0
        for i in range(len(key)):
            hashNumber += ord(key[i]) * (31 ** i)

        return hashNumber


    def put(self, key: str, value: any):
        # keyHashCode = ((2 * key) + 3) % 17
        keyHashCode = self.__hash(key)
        modulo = math.floor(keyHashCode % len(self.buckets))
        # modulo = len(self.buckets) % keyHashCode

        if self.buckets[modulo] is None:
            self.buckets[modulo] = (key, value)
        else:
            secondaryHash = keyHashCode % 17
            self.buckets[secondaryHash] = (key, value)


    def get(self, key: str):
        bucketReturns = []
        keyHashCode = self.__hash(key)
        # modulo = len(self.buckets) % keyHashCode
        modulo = keyHashCode % len(self.buckets)
        secondaryHash = keyHashCode % 17

        if self.buckets[modulo] is None:
            return

        if self.buckets[modulo] is not None:
            bucket = self.buckets[modulo]
            if bucket[0] == key:
                bucketReturns.append(bucket[1])

        if self.buckets[secondaryHash] is not None:
            bucket = self.buckets[secondaryHash]
            if bucket[0] == key:
                bucketReturns.append(bucket[1])

        return bucketReturns




HashTable = HashTable()

HashTable.put("w", "Dog")
HashTable.put("for", "Dog")
# HashTable.put("w", 23)
# HashTable.put("w", 23)

print(HashTable.get("w"))
print(HashTable.buckets)
# print(HashTable.get("dog"))