class BSTnode:
    def __init__(self,value=None):
        self.value = value
        self.left = self.right = None

    def print_center(self):
        if self.value:
            if self.left:
                self.left.print_center()
            print(self.value, end=' ')
            if self.right:
                self.right.print_center()
    
    def insert(self, value):
        if not self.value:
            self.value = value
        elif value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTnode(value)
        elif value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTnode(value)

t = BSTnode()
t.insert(10)
t.insert(30)
t.insert(20)
t.insert(5)
t.insert(8)
t.insert(3)
t.print_center()