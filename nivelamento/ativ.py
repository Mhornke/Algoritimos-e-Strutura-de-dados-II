
def DigitosPares():
    while True:
        print("ℹ️ Se quiser Sair digite #sair")
        print("\nDigitos pares")
        print("Entre com algum digito interiro:")
        numString = input()       
           
        if numString == "#sair":
            break
        
        quant = 0
        for i in numString:
            num = int(i) 
            if num %2 == 0:
                quant += 1
        print(f"Quantidade de numerios positivos: {quant}\n")
        
def Vogais():

    while True:
        print("\n Teste de vogais")
        print("ℹ️ Se quiser Sair digite #sair")
        print("\n ")
        print("Digite apenas uma palavra por vez: (sem espaço, caracteres e numeros) ")
        entradaTexto = input("")
       
        testeIN_alph = entradaTexto.isalpha()       
       
        if entradaTexto == "#sair":
            break
        
        caixaBaixa = entradaTexto.lower() 
        tabelaVogais = ("a","e","i","o","u")

     
        quant = 0
        novaPalavra = ""
        vogal = ""
        if testeIN_alph == True:
            
            for letra in caixaBaixa:  
                # print(f"letra da palavra entrada: {letra}\n")               
                
                novaPalavra += letra
                for i in tabelaVogais:           
                    filto = letra in i
                    #print(f"teste da vogal {i}: {filto}\n")
                    if filto:                            
                        novaPalavra = novaPalavra.replace( i, '*') 
                                    
                        quant += 1
                                        
            
            print(f" {quant}: {novaPalavra}\n")
            
        else:
            print("ℹ️ Digite somente palavras, sem caracteres, numeros ou espaço")
            

        # palavras = []
        # for i in vogais:
        #     palavras.append
      
def lembrar():
   
    pesquisa = [
        {
        "id":1,
       "conteudo":"null",
        "link": "https://pythoniluminado.netlify.app/"
        },
        {
            "id":2,
            "conteudo":"como eu descubro que tem um letra em uma palavra, eu lembro que tinha algo a ver com 'in' ai a variavel",
            "resposta":["image1.png","image2.png"]


            }
    ]
    print(pesquisa)        
     
def RemoverElementosNegativos():
    print(f"\nNumerios Negativos") 
    print("Me diga até quanto quer ver: (10, 20 ou 30 ...)")
    numero = int(input()) +1
  
    negativos = ""
    numeros = ""
    for i in range(numero):
        string = str(i) 
        numeros += string + ", "
        if i %2 == 1:
            negativos += string + ", "
       
  
    print(f"Numeros negativos: {negativos}")
    print(f"Numeros : {numeros}")
    print("\n") 
   
def ListarContatos():
    print("Digite o nome que deseja buscar: " )
    entrada = input()
    lista = []
    with open("contatos.csv", 'r', encoding='utf-8') as arq:
        
        for linha in arq:
            
            for i in linha:
               
            lista.append(linha) 
        
        
    for i in lista:
        if i in entrada:    
            print(f"{i}")
            print(f"{entrada}")
        else:
            print("O nome não foi encrontrado")
                   
                    
        
# opcao = 0
# print(opcao)
while True:
    print("======= Menu de questões =======")
    print("Questão #1: Numeros Positivos")
    print("Questão #2: Vogais")
    print("Questão #8: Listar contatos")
    print("Questão #5: Numeros Negativos")
    print("Lembrar #7")
    print("SAIR #5")
    opcao = int(input())       

    opcoes ={
    1 : DigitosPares,
    2 : Vogais,
    5 : RemoverElementosNegativos,
    8 : ListarContatos,
    7 : lembrar,
    
    }
    BuscaDef = opcoes.get(opcao)

    if opcao == 10:
        break
    elif opcao:
        BuscaDef()
    else:
        print("Escolha uma opção do menu")
        
    # if opcao = 1:
    #     Positivos()
    # elif opcao == 2:
    #     vogais() 
    # elif opcao == 7:
    #     vozesDaMinhaCabeça()

        

    # elif opcao == 5:
    #     opcao == 5