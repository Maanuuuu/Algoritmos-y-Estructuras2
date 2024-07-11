class Node:
    def __init__(self, key,):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_altura(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_altura(node.left) - self.get_altura(node.right)

    def derecha_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_altura(y.left), self.get_altura(y.right))
        x.height = 1 + max(self.get_altura(x.left), self.get_altura(x.right))
        return x

    def iquierda_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_altura(x.left), self.get_altura(x.right))
        y.height = 1 + max(self.get_altura(y.left), self.get_altura(y.right))
        return y

    def insert(self, node, key):
        if not node:
            return Node(key)
        elif key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        node.height = 1 + max(self.get_altura(node.left), self.get_altura(node.right))
        balance = self.get_balance(node)

        if balance > 1 and key < node.left.key:
            return self.derecha_rotate(node)
        if balance < -1 and key > node.right.key:
            return self.iquierda_rotate(node)
        if balance > 1 and key > node.left.key:
            node.left = self.iquierda_rotate(node.left)
            return self.derecha_rotate(node)
        if balance < -1 and key < node.right.key:
            node.right = self.derecha_rotate(node.right)
            return self.iquierda_rotate(node)

        return node

    def pre_order(self, root):
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.pre_order(root.left)
        self.pre_order(root.right)

    def min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.min_value_node(node.left)

    def delete(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        if root is None:
            return root
        self.update_height(root)
        balance = self.get_balance(root)
        if balance > 1:
            if self.get_balance(root.left) >= 0:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        if balance < -1:
            if self.get_balance(root.right) <= 0:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        return root
    
    def search(self, root, key):
        if root is None or root.key == key:
            return root

        if root.key < key:
            return self.search(root.right, key)

        return self.search(root.left, key)
    
    def update_task_status(self, root, key, new_status):
        task_node = self.search(root, key)
        if task_node:
            task_node.status = new_status
            print(f"Tarea {key} status actualizado {new_status}.")
        else:
            print(f"Tarea {key} no encontrada.")

tree = AVLTree()
root = None
root = tree.insert(root, 10)
root = tree.insert(root, 20)
root = tree.insert(root, 30)
root = tree.insert(root, 40)
root = tree.insert(root, 50)
root = tree.insert(root, 25)

print("Preorder traversal of the constructed AVL tree is")
tree.pre_order(root)