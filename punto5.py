from  arbol import BinaryTreeNode, printTree, insertnodeBT

def  max_robo(root):
   if root is None:
      return(0,0)
   
   si_robar_izd, no_robar_izq = max_robo(root.leftchild)

   si_robar_der, no_robar_der = max_robo(root.rightchild)

   no_robar_en_root= max(si_robar_izd,no_robar_izq) +  max(si_robar_der,no_robar_der)

   robar_en_root= root.data + no_robar_izq + no_robar_der

   return(robar_en_root,no_robar_en_root)

root = BinaryTreeNode(3)
insertnodeBT(root,4)
insertnodeBT(root,5)
insertnodeBT(root,1)
insertnodeBT(root,3)
insertnodeBT(root, 1)
printTree(root)

si_robar_root, no_robar_en_root = max_robo(root)
print(si_robar_root,no_robar_en_root)
print("maximo valor robado", max(si_robar_root,no_robar_en_root))