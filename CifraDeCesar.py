import string

def alfabeto():
    return list(string.ascii_uppercase)

def cifrar(mensagem, chave, operacao):
    vetor= alfabeto()
    resp = []
    vetor_msg = list(mensagem)
    
    if(operacao == 1):
        for i in range(len(vetor_msg)):
            if(vetor_msg[i] == " "):
                resp.append(" ")
            
            for a in range(len(vetor)):
                if(vetor_msg[i] == vetor[a]):
                    resp.append(vetor[(a + chave)%26])
    elif(operacao == 2):
        for i in range(len(vetor_msg)):
            if(vetor_msg[i] == " "):
                resp.append(" ")
            
            for a in range(len(vetor)):
                if(vetor_msg[i] == vetor[a]):
                    resp.append(vetor[(a - chave)%26])
                
    return "".join(resp)
    

while(True):
    operacao = int(input("** CIFRAR - 1 | DECIFRAR - 2 ** "))
    mensagem = input("INSIRA A MENSAGEM: ")
    chave    = int(input("INSIRA A CHAVE (ex. 1,2,3...): "))

    if(operacao == 1):
        print("MENSAGEM CIFRADA: ", cifrar(mensagem.upper(), chave, operacao))
    elif(operacao == 2):
        print("MENSAGEM DECIFRADA: ", cifrar(mensagem.upper(), chave, operacao))
        
    resp = input("NOVAMENTE? S / N ")
    
    if(resp.upper() == "S"):
        continue
    else:
        print("PROGRAMA ENCERRADO :)")
        break

