class BST():
    def __init__(self, parent, value):
        self.value = value
        self.parent = parent
        self.left_child = None
        self.right_child = None

    def render(self):
        print("            |{}|            ".format(self.value))
        print("     |{}|               |{}|    ".format(
            self.left_child.value if self.left_child != None else " ",
            self.right_child.value if self.right_child != None else " ",
            )
        )
        if self.left_child != None:
            print("  |{}|     |{}|   ".format(
                self.left_child.left_child.value if self.left_child.left_child != None else " ",
                self.left_child.right_child.value if self.left_child.right_child != None else " ",
                ), end=""
            )
        if self.right_child != None:
            print("    |{}|     |{}|  ".format(
                self.right_child.left_child.value if self.right_child.left_child != None else " ",
                self.right_child.right_child.value if self.right_child.right_child != None else " ",
                )
        )
        print()

    def height(self):
        height = 1
        return height + max(
                self.left_child.height() if self.left_child != None else 0, 
                self.right_child.height() if self.right_child != None else 0
                )

    def contains(self, value):
        if value == self.value:
            return True
        elif value < self.value:
            return False if self.left_child == None else self.left_child.contains(value)
        elif value > self.value:
            return False if self.right_child == None else self.right_child.contains(value)

    def add(self, value):
        if value < self.value:
            # Left
            if self.left_child == None:
                new_bst = BST(self, value)
                self.left_child = new_bst 
                self.render()
                return new_bst
            else:
                new_bst = self.left_child.add(value)
                self.render()
                return new_bst
        elif value > self.value:
            # Right
            if self.right_child == None:
                new_bst = BST(self, value)
                self.right_child = new_bst
                self.render()
                return new_bst
            else:
                new_bst = self.right_child.add(value)
                self.render()
                return new_bst 
        else:
            print("The value " + str(value) + " aready exists in the tree")

    def remove(self, value):
        if self.contains(value):
            if value == self.value:
                if self.left_child != None:
                    possible_replacement = self.left_child
                    replacement = None
                    while possible_replacement != None:
                        replacement = possible_replacement
                        possible_replacement = replacement.right_child
                    self.value = replacement.value
                    replacement.remove(replacement.value)
                elif self.right_child != None:
                    possible_replacement = self.right_child
                    replacement = None
                    while possible_replacement != None:
                        replacement = possible_replacement
                        possible_replacement = replacement.left_child
                    self.value = replacement.value
                    replacement.remove(replacement.value)
                else:
                    if self.parent != None:
                        if self == self.parent.left_child:
                            self.parent.left_child = None
                        else:
                            self.parent.right_child = None
                    else:
                        print("You cannot remove the root of the bst")
            elif value < self.value:
                self.left_child.remove(value)
            else:
                self.right_child.remove(value)
        else:
            print("The value " + str(value) + " is not contained in the tree")
        self.render()

    def in_order_traversal(self):
        values = []
        if self.left_child != None:
            for x in self.left_child.in_order_traversal():
                values.append(x)
        values.append(self.value)
        if self.right_child != None:
            for x in self.right_child.in_order_traversal():
                values.append(x)
        return values

    def breadth_order_traversal(self):
        values = []
        queue = [self]

        while len(queue) > 0:
            # Process node
            values.append(queue[0].value)
            
            if queue[0].left_child != None:
               queue.append(queue[0].left_child) 
            if queue[0].right_child != None:
                queue.append(queue[0].right_child)

            queue.remove(queue[0])

        return values

def create_tree():
    bst = BST(None, 5)
    bst.add(7)
    bst.add(3)
    bst.add(4)
    bst.add(9)
    bst.remove(5)

create_tree()
