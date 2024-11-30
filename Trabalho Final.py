#Recebendo informações do cliente para efetuar o cadastro.
print("--- Cadastro do Cliente ---")
nome = input("Digite seu nome: ")
tel = int(input("Digite seu telefone: "))
saldo = float(input("Informe o valor do seu saldo: "))

#Dicionario criado parar armazenar todos as marcas, modelos e preços dos carros disponiveís da concessonária.
fipe = {
"Corolla": 1000,
"Hilux": 1500,
"RAV4": 2000,

"Golf": 2500,
"Polo": 3000,
"Tiguan": 3500,

"Civic": 4000,
"HR-V": 4500,
"CR-V": 5000,

"Fiesta":5500,
"Fusion":6000,
"Ranger":6500,

"Onix": 7000,
"S10": 7500,
"Cruze": 8000,
}

carros = {
"Toyota": ["Corolla","Hilux","RAV4"],
"Volkswagen": ["Golf","Polo","Tiguan"],
"Honda": ["Civic","HR-V","CR-V"],
"Ford": ["Fiesta","Fusion","Ranger"],
"Chevrolet": ["Onix","S10","Cruze"],
}

#Tabela que vai armanezar os carros da concessonária que vai me vender os carros.
carrosC = {
"Toyota": ["Corolla","Hilux","RAV4"],
"Volkswagen": ["Golf","Polo","Tiguan"],
"Honda": ["Civic","HR-V","CR-V"],
"Ford": ["Fiesta","Fusion","Ranger"],
"Chevrolet": ["Onix","S10","Cruze"],
}

#Inicializo a variável com valor zero para poder iniciar a estrutura de repetição.
opcao = 0

#Faço a condição de parada da minha estrutura de repetição estar ligada a 4° opção da minha tabela (Ja que a 4° opção é a de sair do sistema).
while opcao != 4:
    print("--- bem vindo ao sistema de Compra, Venda e Aluguel de Veículos ---")
    opcao = int(input("1- Venda de veículo.\n2- Compra de veículo.\n3- Aluguel de veículo.\n4- Sair.\nEscolha uma opção: "))
    
    #Uso a estrutura de condição para efetuar uma determinada ação de acordo com a opção escolhida pelo usuário.
    if opcao == 1:

     print("-- Vendas de veículos --")
     #Uso o "for" para percorrer o dicionário e exibir as marcas dos carros para que o usuário escolha a que ele quer, e leio a marca escolhida por ele.
     for exibir in carrosC:
         print(exibir)
       
     exibir = input("Escolha uma marca: ")

     #Uso o "for" para percorrer minha tabela FIPE, exibindo os modelos disponiveís da marca que o usuário escolheu, e assim, leio o modelo que ele deseja comprar e faço o calculo do desconto.
     for modelo in fipe:
       print(carrosC[exibir])
       modelo = input("Escolha um modelo: ")
       
       #Verifico se o modelo escolhido esta disponível, se não estiver o sistema exibe uma mensagem de erro
       if modelo in carrosC[exibir]:       
         desconto = fipe[modelo] * 0.12
         valorf = fipe[modelo] - desconto
         print("O valor da proposta será de: ",valorf)
         conf = input("Deseja fechar esse acordo(S/N)?: ")
       else: 
           print("Veículo indisponível.")
           break

       #Confirmo se o usuário deseja fechar negócio ou cancela-lo,verifico se, se sim, a venda é realizada e o preço do modelo é somado ao meu saldo e então o novo saldo é exibido.
       if conf == "S":
         #Verifico se o saldo é suficiente para realizar a venda,
         if saldo >= valorf:
          saldo = saldo + valorf     
          print("Compra realizada com sucesso.\nSeu saldo atual é de: ",saldo)
          break
     
         else:
          print("Erro, saldo insuficiente!")
          break

       elif conf == "N":
         print("Negociação cancelada.")
         break

    #O mesmo de antes vale para esses "if" e "for" de agora e os que vierem depois e não estiverem comentados, os "breaks" foram usados para parar a estrutura de repetição caso certa condição aconteça, assim o menu de opções reaperece.
    if opcao == 2:
      print("-- Compra de veículos --")
      
      for e in carros:
           print(e)       
      e = input("Escolha uma marca: ")

      for marcas in fipe: 
        print(carros[e])
        modelo = input("Escolha uma modelo acima: ")
        
        if modelo in carros[e]: 
         acrescimo = fipe[modelo] * 0.25
         compra = fipe[modelo] + acrescimo
         print("O valor da compra será de: ",compra)
         resposta = (input("Deseja fechar negócio?(S/N): "))
         
        else:
           print("Veículo indisponível.")
           break

        if resposta == "S":
          #Verifico se o saldo é suficiente para compra, se for, o saldo é subtraido pelo valor da compra, o modelo é removido da tabela e não estará mais disponível para compra.
           if saldo >= compra:
             saldo = saldo - compra
             carros[e].remove(modelo)
             print("O seu saldo agora é de:",saldo)
             break

           else: 
             print("Erro, saldo insuficiente!")
             break

        elif resposta == "N":
          print("Negociação cancelada.")    
          break

    if opcao == 3:
       print("- Aluguel de veículos --")
      
       for m in carros:
           print(m)       
       m = input("Escolha uma marca: ")

       for marcas in fipe: 
        print(carros[m])
        modelo = input("Escolha uma modelo acima: ")
        dias = int(input("Informe a quantidade de dias que ficará com o carro: "))
        
        #Para o aluguel, o calculo é feito a partir da multiplicação dos dias que o cliente estará com carro vezes a taxa de aluguel diária
        if modelo in carros[m]:          
         v_alug = dias * 77
         print("O valor do aluguel será de: ",v_alug)
         resposta = (input("Deseja fechar negócio?(S/N): "))
         
        else:
           print("Veículo indisponível.")
           break

        if resposta == "S":

           if saldo >= v_alug:
             saldo = saldo - v_alug
             carros[m].remove(modelo)
             print("Aluguel realizado com sucesso!\nO seu saldo agora é de:",saldo)
             break

           else: 
             print("Erro, saldo insuficiente!")
             break
        
        elif resposta == "N":
          print("Negociação cancelada.")    
          break
     
    if opcao == 4:
      print("Fim do sistema.")
