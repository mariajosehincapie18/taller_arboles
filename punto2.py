from  arbol import BinaryTreeNode, printTree, insertnodeBT

def contar_hojas_nivel_par(root, nivel = 0):
    if root is None:
        return 0
    
    if root.leftchild is None and root.rightchild is None:
        if nivel %2 == 0:
            return 1
        else:
            return 0
        
    izquierda= contar_hojas_nivel_par(root.leftchild, nivel +1)
    derecha = contar_hojas_nivel_par(root.rightchild, nivel +1)
    return izquierda + derecha


root = BinaryTreeNode(10)
insertnodeBT(root, 5)
insertnodeBT(root, 15)
insertnodeBT(root, 3)
insertnodeBT(root, 7)
insertnodeBT(root, 12)
insertnodeBT(root, 18)
insertnodeBT(root, 1)
insertnodeBT(root, 4)
print("ARBOL ANTES")
printTree(root)
hojas = contar_hojas_nivel_par(root)
print("Arbol despues", hojas)


