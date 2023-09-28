class UnionFind:
    def __init__(self, n):
        #n is the number of nodes of our graph
        #For every node, we want to keep track of what the parent is
        #For every tree we also want to keep track of the rank. By rank we mean the height. This is because we want thhe height to be as small as possible which will make our find to be more efficient
        self.par = {}
        self.rank = {}

        # Initialize the parent as itself
        # Initialize the rank to 0
        for i in range(1, n + 1):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, n):
        # To find the root parent  of e.g 4, we would go first to its parent
        p = self.par[n]
        # Keep traversing up while p != to it's parent
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]] # path compression
            p = self.par[p]
        return p
    
    # Given two nodes, we want to union them together to form a single set
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        # Union by rank/height

        # if height of p1 is larger, p1 should be the parent of p2
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        # if height of p2 is larger, p2 should be the parent of p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        # if both heights are equal
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True

# Time complexity: O(nlogn)