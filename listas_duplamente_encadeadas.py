class Node:
    def __init__(self, valAtual=None):
        self.valorAtual = valAtual
        self.proximoValor = None
        self.valorAnterior = None


class ListaDuplamenteEnc:
    def __init__(self):
        self.valorCabeca = None


    def listprint(self):
        printValor = self.valorCabeca
        while printValor is not None:
            print (printValor.valorAtual)
            printValor = printValor.proximoValor



list1 = ListaDuplamenteEnc()
list1.valorCabeca = Node("Marco")
e2 = Node("Gustavo")
e3 = Node("Pedro")




# Encadeando o primeiro nó com o segundo nó
list1.valorCabeca.proximoValor = e2

# Encadeando o segundo nó com o primeiro e com o terceiro nó 
e2.valorAnterior = list1.valorCabeca
e2.proximoValor = e3




list1.listprint()