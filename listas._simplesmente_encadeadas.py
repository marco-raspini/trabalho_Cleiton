class Node:
    def __init__(self, valAtual=None):
        self.valorAtual = valAtual
        self.proximoValor = None

class ListaSimplesmenteEnc:
    def __init__(self):
        self.valorCabeca = None


    def listprint(self):
        printValor = self.valorCabeca
        while printValor is not None:
            print (printValor.valorAtual)
            printValor = printValor.proximoValor



list1 = ListaSimplesmenteEnc()
list1.valorCabeca = Node("Marco")
e2 = Node("Gustavo")
e3 = Node("Pedro")




# Encadeando o primeiro nó com o segundo nó
list1.valorCabeca.proximoValor = e2

# Encadeando o segundo nó com o terceito nó
e2.proximoValor = e3


list1.listprint()