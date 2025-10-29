from  arbol import BinaryTreeNode,Queue, printTree, insertnodeBT

def valor_izquierdo_ultimo_nivel(root):
    if root is None:
        return None
    
    cola= Queue()
    cola.enqueue(root)
    ultimo_izquierdo = root.data

    while  not cola.is_empty():
        tamaño_nivel= cola.len()
        for i in range(tamaño_nivel):
            current= cola.dequeue()
            if i == 0:
                ultimo_izquierdo = current.data
            if current.leftchild is not None:
                cola.enqueue(current.leftchild)
            if current.rightchild is not None:
                cola.enqueue(current.rightchild)

    return ultimo_izquierdo



root = BinaryTreeNode(1)
root.leftchild = BinaryTreeNode(2)
root.rightchild = BinaryTreeNode(3)
root.leftchild.leftchild = BinaryTreeNode(4)
root.rightchild.leftchild = BinaryTreeNode(5)
root.rightchild.rightchild = BinaryTreeNode(6)
root.rightchild.leftchild.leftchild = BinaryTreeNode(7)

printTree(root)
print("Más a la izquierda del último nivel:", valor_izquierdo_ultimo_nivel(root))