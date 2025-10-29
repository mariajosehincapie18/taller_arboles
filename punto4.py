from  arbol import BinaryTreeNode, printTree,insertnodeBST

def k_esimo_mas_pequeño(root, k, cont= 0):
    if root is None:
        return (None, cont)
    
    resultado, cont = k_esimo_mas_pequeño(root.leftchild, k, cont)
    if resultado is  not None:
        return (resultado,cont)
    
    cont = cont + 1
    if cont == k:
        return (root.data, cont)
    
    resultado,cont = k_esimo_mas_pequeño(root.rightchild, k, cont)
    return(resultado, cont)


root = BinaryTreeNode(20)
insertnodeBST(root,10)
insertnodeBST(root,11)
insertnodeBST(root,12)
insertnodeBST(root,4)
insertnodeBST(root,5)
insertnodeBST(root,22)
insertnodeBST(root,21)
insertnodeBST(root,30)
insertnodeBST(root,35)
insertnodeBST(root,50)
printTree(root)
valor, _ = k_esimo_mas_pequeño(root, 8)
print("El 8tavo valor más pequeño es:", valor)