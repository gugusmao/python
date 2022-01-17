import sys

"""
    Site de origem                                  - link encurtado
    https://url.gratis/                             - https://url.gratis/4QOZ2o
    https://abre.ai/                                - https://abre.ai/dqWT
    https://www.encurtador.com.br/url-encurtada.php - encurtador.com.br/beGJ2
    https://tinyurl.com/app/myurls                  - https://tinyurl.com/yu97rcsp
    https://bityli.com/                             - https://bityli.com/RjPFhH
    https://www.shorturl.at/shortener.php           - shorturl.at/przC9
    https://free-url-shortener.rb.gy/               - https://rb.gy/zsjd1i    
"""

"""
    - O padrão que dá para buscar mesmo é o nome do site que faz o processo de encurtar o link. 
    O script busca o arquivo e abre o html como texto, faço o loop para cada linha checando se 
    algum dos nomes da lista que criei está naquela linha, se sim, executa o print da linha.
"""

#função para procurar os encurtadores
def localizar_encurtador(matches, text_file):
    contem = False #variavel que serve para controlar se há ou não o url encurtado

    for line in text_file:                          #loop para ir linha por linha no html
        line = str(line)                            #why not  :)
        #print(line)    
        if any(word in line for word in matches):   #Aqui checamos linha por linha se contém algum dos nomes 
            print(line)                             #que estão na lista que criei acima, se sim, execut ao print da linha 
            contem = True                                        #atual do loop
            

    if contem == False:
        print("O HTML não contém encurtador de link, pode seguir para produção.")
    else:
        print("Pro favor, retirar os links encurtados do HTML. Checar novamente após a retidada para confirmar a remoção total.")                                                
                                                         


#Abre o arquivo
while(True):
    try:
        file_name = input("Qual arquivo deseja verificar?(Path) ")
        #text_file = open('C:\Users\est.gustavoag\Votorantim\CRM JS+ - Documentos\CAMPANHAS\JID-001531\HTML\index.html', 'r')
        #text_file = open('C:\Users\est.gustavoag\Votorantim\CRM JS+ - Documentos\General\projeto_automacao_encurtador_HTML\index.html','r')
        text_file = open(file_name, 'r')
        print(text_file) #teste para checar como está as propriedade da variável
        break
    except:
        print("Digite um caminho válido, por favor!")
        continue  


#lista com os nomes de encurtadores mais usados que encontrei, e podendo dar mais inputs dentro dela
matches = ["url.gratis", "abre.ai", "encurtador","tinyurl", "bityli", "shorturl", "rb.gy"]
confirm = True
print("Por padrão, estamos verificando os seguintes domínios: 'url.gratis', 'abre.ai', 'encurtador', 'tinyurl', 'bityli', 'shorturl' e 'rb.gy'.")
print("Digite o nome do dominio de encurtador que gostaria de verificar no html. ")
            
while(confirm == True):
    url_names = input("(Digite 'Verificar' para executar a análise): ")
    if url_names.lower() == 'verificar':
        break
    else:
        matches.append(url_names)
        #print(matches)

localizar_encurtador(matches, text_file)