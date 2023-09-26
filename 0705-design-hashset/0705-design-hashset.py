class MyHashSet(object):

    def __init__(self):
        self.maxHash = 1000
        self.hash_table=[[] for i in range(self.maxHash)]


    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.contains(key):
            return
        else:
            subKey = key%self.maxHash
            self.hash_table[subKey].append(key)
        
        
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if not self.contains(key):
            return
        else:
            subKey = key%self.maxHash
            self.hash_table[subKey].remove(key)

        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        subKey = key%self.maxHash
        for i in self.hash_table[subKey]:
            if key == i:
                return True
        return False
        

        
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)