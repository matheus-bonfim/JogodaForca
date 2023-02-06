import random

lista = []
with open ('words.txt', 'r', encoding='utf-8') as notas:
    for linha in notas:
        lista.append(linha.split()[0])
        lista.append(linha.split()[1])
        lista.append(linha.split()[2])




def geraWord(lista):
    a = random.randrange(len(lista))
    return lista[a]

def position(word, letter):
    pos = []
    for i in range(len(word)):
        if word[i] == letter:
            pos.append(i)
    return pos

def blank(word):
    a = []
    for x in range(len(word)):
        a.append('_')
    return a

def palavrador(lista):
    palavra = ''
    for i in range(len(lista)):
        palavra = palavra + lista[i] + ' '
    return palavra
k = 0


word = geraWord(lista)
pForca = blank(word)

while k < 8:
    
    letra = input("Digite uma letra: ")
    if letra in word:
        pos = position(word, letra)
        
        for i in range(len(pos)):
            pForca.pop(pos[i])
            pForca.insert(pos[i], letra)
        print(pForca)

        print("A palavra é: ",palavrador(pForca))
        if "_" not in pForca:
            print("Parabéns, seu lindo pescocinho está salvo!")
            exit()

    else:
        if k == 6:
            print("Você errou pela 6ª vez, última tentativa, idiota!")
            k = k + 1
        elif k == 7:
            print("Perdeu, imbecil! A palavra era",word)
            exit()
        else:     
            print(f"Você errou pela {k+1}ª vez. Tente de novo!")
            k = k + 1



