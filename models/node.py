from .genre import Genre
from .film import Film


class Node:
    nodes = []
    def __init__(self, data: Film, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
    def print(self):
        if self.left:
            self.left.print()
        print(self.data)
        if self.right:
            self.right.print()

    def print_by_genre(self, genre: Genre):
        if self.left:
            self.left.print_by_genre(genre)
        if self.data.genre == genre:
            print(self.data)
        if self.right:
            self.right.print_by_genre(genre)

    def find_minimum(self, node):
        while node.left:
            node = node.left
        return node

    def add(self, data: Film):

        if self.data is not None:
            if data.name < self.data.name:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.add(data)
            elif data.name > self.data.name:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.add(data)
        else:
            self.data = data

    def delete(self, root, data: Film):

        parent = None
        curr = root

        while curr and curr.data != data:
            parent = curr

            if data.name < curr.data.name:
                curr = curr.left
            else:
                curr = curr.right

        if curr is None:
            return root

        if curr.left is None and curr.right is None:
    
            if curr != root:
                if parent.left == curr:
                    parent.left = None
                else:
                    parent.right = None
            else:
                root = None
        elif curr.left and curr.right:
            successor = self.find_minimum(curr.right)
            val = successor.data
            self.delete(root, successor.data)
            curr.data = val
        else:
            if curr.left:
                child = curr.left
            else:
                child = curr.right

            if curr != root:
                if curr == parent.left:
                    parent.left = child
                else:
                    parent.right = child
            else:
                root = child
    
        return root

    def find_by_studio(self, studio: str):
        if self.left:
            self.left.find_by_studio(studio)
        if studio == self.data.studio:
            self.nodes.append(self.data)
        if self.right:
            self.right.find_by_studio(studio)

    def find_node(self, studio: str):
        if self.data.studio == studio:
            return self.data
        left_result = None
        right_result = None
        if self.left:
            left_result = self.left.find_node(studio)
        if self.right:
            right_result = self.right.find_node(studio)
        return left_result if left_result else right_result

    def delete_by_studio(self, studio: str):
        self.nodes = []
        while True:
            node = self.find_node(studio)
            if node is not None:
                self.delete(self, node)
            else:
                break