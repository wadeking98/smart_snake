class node:
    def __init__(self, item):
        """
        @param (Generic<T>) item that the node holds
        """
        self.item = item
        self.parent = None
        self.children = []

    def attach(self, n):
        """
        @param (Node) n, the node being attached
        """
        n.parent = self
        self.children.append(n)

    def traceback(self):
        """
        iterates up the tree until it finds the root
        @return (list), the path of the traceback
        """
        path = []
        curr = self
        while curr is not None:
            path.insert(0,curr.item)
            curr = curr.parent
        return path

    def __str__(self):
        string = ""
        if self.children == []:
            return self.item.__str__()
        else:
            string += self.item.__str__()+"["
            for child in self.children:
                string += child.__str__()
            string += "]"
            return string
