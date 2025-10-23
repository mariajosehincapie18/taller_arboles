from  arbol import BinaryTreeNode, printTree, insertnodeBT
def contar_rutas(root, target_sum, suma_actual= 0):

    if root is None:
        return 0
    
    suma_actual = suma_actual + root.data

    if root.leftchild is None and root.rightchild is None:
        if suma_actual == target_sum:
            return 1
        else:
            return 0
        
    return (contar_rutas(root.leftchild, target_sum, suma_actual) +
             contar_rutas(root.rightchild, target_sum, suma_actual) )



root = BinaryTreeNode(5)
root.leftchild = BinaryTreeNode(4)
root.rightchild = BinaryTreeNode(8)

root.leftchild.leftchild = BinaryTreeNode(11)

root.leftchild.leftchild.leftchild= BinaryTreeNode(7)
root.leftchild.leftchild.rightchild=BinaryTreeNode(2)

root.rightchild.leftchild = BinaryTreeNode(13)
root.rightchild.rightchild = BinaryTreeNode(4)
root.rightchild.rightchild.rightchild = BinaryTreeNode(1)

printTree(root)

resultado=contar_rutas(root, 22)
print("Rutas con suma 22: ", resultado)

        
root2 = BinaryTreeNode(5)
root2.leftchild = BinaryTreeNode(4)
root2.rightchild = BinaryTreeNode(8)

root2.leftchild.leftchild = BinaryTreeNode(11)

root2.leftchild.leftchild.leftchild= BinaryTreeNode(7)
root2.leftchild.leftchild.rightchild=BinaryTreeNode(2)

root2.rightchild.leftchild = BinaryTreeNode(13)
root2.rightchild.rightchild = BinaryTreeNode(4)
root2.rightchild.rightchild.rightchild = BinaryTreeNode(1)

printTree(root2)

resultado=contar_rutas(root2, 22)
print("Rutas con suma 22: ", resultado)
