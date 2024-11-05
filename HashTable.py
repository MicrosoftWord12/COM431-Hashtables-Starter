import linkedlist

TupleLinkedList = linkedlist.TuplesLinkedList

class HashTable:
    def __init__(self):
        # self.buckets = [None] * 127
        self.buckets = [TupleLinkedList() for i in range(127)]

    def __hash(self, key):
        hashNumber = 0
        for i in range(len(key)):
            hashNumber += ord(key[i]) * (31 ** i)

        return hashNumber


    def put(self, key: str, value: any):
        # keyHashCode = ((2 * key) + 3) % 17
        keyHashCode = self.__hash(key)

        modulo = keyHashCode % len(self.buckets)

        bucket = self.buckets[modulo]
        bucket.add(key, value)


    def get(self, key: str):
        keyHashCode = self.__hash(key)
        # modulo = len(self.buckets) % keyHashCode
        modulo = keyHashCode % len(self.buckets)

        if self.buckets[modulo] is None:
            print("Cannot find Bucket")

        value = self.buckets[modulo].find(key)

        return value




HashTable = HashTable()

HashTable.put("w", "Dog")
HashTable.put("dog", 23)

print(HashTable.get("w"))
print(HashTable.get("dog"))