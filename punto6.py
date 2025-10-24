from  arbol import BinaryTreeNode, printTree, insertnodeBT

def suma_rutas(root, numero_actual = 0):
    if root is None:
        return 0
    
    numero_actual = numero_actual * 10 + root.data
    if root.leftchild is None and root.rightchild is None:
        return numero_actual
    

    suma_izquierda = suma_rutas(root.leftchild, numero_actual)
    suma_derecha = suma_rutas(root.rightchild, numero_actual)

    return suma_izquierda + suma_derecha




root= BinaryTreeNode(4)
insertnodeBT(root,9)
insertnodeBT(root,0)
insertnodeBT(root,5)
insertnodeBT(root,1)
printTree(root)
resultado =suma_rutas(root)
print("RESULTADO: ", resultado)