# Solving this problem with set might cause O(n) time complexity when there will be hash collision
# Also random.choice doesn't work for set, we need to convert the set into list, which will cause O(n) Time
import random
class RandomizedSet:

    def __init__(self):
        # The randomized set. We will work with dictionary
        self.map = {}
        # Use a list to track the elements
        self.tracker = []

    def insert(self, val: int) -> bool:
        if val in self.map: # If the value already exists we return False
            return False
        # Otherwise we add the value
        self.map[val] = len(self.tracker) # Tracking the index of the value. Index will be last len(arr)+1
        self.tracker.append(val) # Adding the value in the tracker list

        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        # We will swap the item with the last item of the tracker. --> Remove O(1) from the last index.

        # 1--> Find the index of the item that should be removed
        valPosition = self.map[val]
        # 2 --> Set this position to the last value of the tracker list as we are going to swap the last element
        self.map[self.tracker[-1]] = valPosition

        # 3--> Swap with the last element
        self.tracker[valPosition],self.tracker[-1] = self.tracker[-1],self.tracker[valPosition]

        # Now remove the value
        self.map.pop(val)
        self.tracker.pop()

        return True
    def getRandom(self) -> int:
        return random.choice(self.tracker)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()