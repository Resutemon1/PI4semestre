variavel=input("Digite a primeira unidade ")
variavel2=float(input("Digite o valor a ser convertido "))
variavel3=input("Digite a segunda unidade ")
import conversao
if (variavel.lower() == "jarda"):
    if variavel3.lower() == "metro" or variavel3.lower() == "metros":
        c = conversao.jardasParaMetros(variavel2)
        print(c)

    elif(variavel3.lower() == "pe" or variavel3.lower()=="pé"):
        b = conversao.jardasParaPes(variavel2)
        print(b)
    else:
        print("Não é possivel converter")
elif (variavel.lower() == "metro" or variavel.lower()=="metros"):
    d = conversao.metrosParaPe(variavel2)
    print(d)
elif (variavel.lower() == "pe" or variavel.lower()=="pé"):
    e = conversao.converterPesParaMetros(variavel2)
    print(e)
else:
    print("Não é possivel resolver")
