"""
A hash set implementation in python using List DS. 
"""


class MyHashSet:

    def __init__(self):
        self.list = []

    def add(self, key: int) -> None:
        if (key not in self.list):
            self.list.append(key)

    def remove(self, key: int) -> None:
        if key in self.list:
            self.list.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return (key in self.list)


# MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
obj.add(2)
print(obj.contains(1))
print(obj.contains(3))
obj.add(2)
print(obj.contains(2))
obj.remove(2)
print(obj.contains(2))
