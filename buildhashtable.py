class HashTableEntries:
    def __init__(self, key, item):
        self.key = key
        self.item = item


class HashMap:
    def __init__(self, start_capacity=10):
        self.map = []
        for i in range(start_capacity):
            self.map.append([])

    def _get_hash(self, key):
        bucket = int(key) % len(self.map)
        return bucket

    def retrieve(self, key):
        hash_key = self._get_hash(key)
        if self.map[hash_key] is not None:
            for pair in self.map[hash_key]:
                if pair[0] == key:
                    return pair[1]
                return None

    def insert(self, key, value):
        hash_key = self._get_hash(key)
        key_value = [key, value]

        if self.map[hash_key] is None:
            self.map[hash_key] = list([key_value])
            return True
        else:
            for pair in self.map[hash_key]:
                if pair[0] == key:
                    pair[1] = key_value
                    return True
                self.map[hash_key].append(key_value)
                return True

    def update(self, key, value):
        hash_key = self._get_hash(key)
        if self.map[hash_key] is not None:
            for pair in self.map[hash_key]:
                if pair[0] == key:
                    pair[1] = value
                    print(pair[1])
                    return True
        else:
            print('Update error with key: ' + key)

    def remove(self, key):
        hash_key = self._get_hash(key)
        if self.map[hash_key] is None:
            return False
        for i in range(0, len(self.map[hash_key])):
            if self.map[hash_key][i][0] == key:
                self.map[hash_key].pop(i)
                return True
        return False
