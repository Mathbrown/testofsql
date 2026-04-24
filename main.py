def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    return num1 / num2

start = False

while(True):
    if start == False:
        print("Seja bem vindo a calculadora")
        start = True
    else:
        print("Seja bem vindo novamente a calculadora hahahhaha")

    val_num1 = input("Digite o primeiro numero:")
    val_num1 = int(val_num1)

    val_op = input("Informe a operação (+ - * /):");

    val_num2 = input("Digite o segundo numero:")
    val_num2 = int(val_num2)

    val_re = None

    if(val_op == "+"):
        val_re = somar(val_num1, val_num2)
    elif(val_op == "-"):
        val_re = subtrair(val_num1, val_num2)
    elif(val_op == "*"):
        val_re = multiplicar(val_num1, val_num2)
    elif(val_op == "/"):
        val_re = dividir(val_num1, val_num2)
    else:
        print("Operador não aceito")
        continue

    print(f"Resultado do calculo: {val_re} \n\n\n\n")