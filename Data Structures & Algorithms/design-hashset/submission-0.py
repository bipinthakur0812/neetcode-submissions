class MyHashSet:

    def __init__(self):
        # Using a prime number for space minimizes hash collisions
        self.key_space = 2069
        # Initialize an array where each bucket is an empty list
        self.buckets = [[] for _ in range(self.key_space)]

    def _hash(self, key: int) -> int:
        # A simple modulo hash function
        return key % self.key_space

    def add(self, key: int) -> None:
        bucket_idx = self._hash(key)
        # Only add the key if it doesn't already exist (Sets don't allow duplicates)
        if key not in self.buckets[bucket_idx]:
            self.buckets[bucket_idx].append(key)

    def remove(self, key: int) -> None:
        bucket_idx = self._hash(key)
        # If the key is found in its designated bucket, remove it
        if key in self.buckets[bucket_idx]:
            self.buckets[bucket_idx].remove(key)

    def contains(self, key: int) -> bool:
        bucket_idx = self._hash(key)
        # Instantly check the relevant bucket for the key
        return key in self.buckets[bucket_idx]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)