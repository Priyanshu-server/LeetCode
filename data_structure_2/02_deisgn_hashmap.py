class MyHashMap:

    def __init__(self):
        self.table = [-1] * 1000001

    def put(self, key, value):
        self.table[key] = value
        

    def get(self, key):
        return self.table[key]
        

    def remove(self, key):
        self.table[key] = -1



# Your MyHashMap object will be instantiated and called as such:
key = 1
value = 2
obj = MyHashMap()
obj.put(key,value)
param_2 = obj.get(key)
obj.remove(key)




# Solution 2
# Applying using linked List

class ListNode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None

class MyHashMap:

    def __init__(self):
        self.m = 1000
        self.h = [None]*self.m
        

    def put(self, key, value):
        index = key % self.m
        if self.h[index] == None:
            self.h[index] = ListNode(key, value)
        else:
            cur = self.h[index]
            while True:
                if cur.pair[0] == key:
                    cur.pair = (key, value) #update
                    return
                if cur.next == None: break
                cur = cur.next
            cur.next = ListNode(key, value)
        

    def get(self, key):
        index = key % self.m
        cur = self.h[index]
        while cur:
            if cur.pair[0] == key:
                return cur.pair[1]
            else:
                cur = cur.next
        return -1
            
        

    def remove(self, key):
        index = key % self.m
        cur = prev = self.h[index]
        if not cur: return
        if cur.pair[0] == key:
            self.h[index] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.pair[0] == key:
                    prev.next = cur.next
                    break
                else:
                    cur, prev = cur.next, prev.next