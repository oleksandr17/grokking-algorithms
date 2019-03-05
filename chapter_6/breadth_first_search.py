from collections import deque


class Node:

    def __init__(self, alias, isDeveloper = False, neighbours = None):
        self.alias = alias
        self.isDeveloper = isDeveloper
        if not neighbours:
            self.neighbours = []

    def addNeighbours(self, neighbours):
        self.neighbours += neighbours

    def __str__(self):
        neighbours = [neighbour.alias for neighbour in self.neighbours]
        return f"{self.alias}, {self.isDeveloper}, {neighbours}"

    def findFirstDeveloper(self):
        if self.isDeveloper:
            return self

        neighbours = deque(self.neighbours)
        checked_neighbours = []

        while len(neighbours) > 0:
            neighbour = neighbours.popleft()
            if neighbour in checked_neighbours:
                continue

            if neighbour.isDeveloper:
                return neighbour
            else:
                neighbours += neighbour.neighbours
            
            checked_neighbours.append(neighbour)
        return None

if __name__ == "__main__":
    me = Node("me")
    bob = Node("bob")
    alice = Node("alice")
    claire = Node("claire")
    anuj = Node("anuj")
    peggy = Node("peggy")
    thon = Node("thon", isDeveloper=True)
    jonny = Node("jonny")

    me.addNeighbours([bob, alice, claire])
    bob.addNeighbours([anuj, peggy])
    alice.addNeighbours([peggy])
    claire.addNeighbours([thon, jonny])

    print(f"First developer: {me.findFirstDeveloper()}")
