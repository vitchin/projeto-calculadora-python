class Calculadora:
    def __init__(self, n1, n2, operador):
        self.numero1 = n1
        self.numero2 = n2
        self.operador = operador
    
    def soma(self):
        return print(f'A soma dos valores é: {self.numero1 + self.numero2}')
        
    def subtracao(self):
        return print(f'A subtração dos valores é: {self.numero1 - self.numero2}')
    
    def divisao(self):
        return print(f"A divisao dos valores é: {self.numero1 / self.numero2}")
    
    def multiplicacao(self):
        return print(f"a multiplicação dos valores é: {self.numero1 * self.numero2}")
    

if __name__ == "__main__":
    
    val1 = int(input("Digite o primero valor: "))
    val2 = int(input("Digite o segundo valor: "))
    
    operacao = input("Digite um operador: ")
    
    obj = Calculadora(val1, val2, operacao)

    if(operacao == "+"):
        obj.soma()
    elif(operacao == "-"):
        obj.subtracao()
    elif(operacao == "/"):
        obj.divisao()
    elif(operacao == "*"):
        obj.multiplicacao()
    else:
        "Operador inválido!"