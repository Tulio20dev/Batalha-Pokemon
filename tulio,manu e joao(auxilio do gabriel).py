import random

print('Bem Vindo')
print('escolha seu Pokemon')
print('1-Charmander')
print('2-Squirtle')
print('3-Bulbassaur')

j1 = (int(input('>> '))) -1 

j2 = random.randint(0,2)

PokeDisponiveis = [{'nome':"Charmander","dano":40,"vida":80,"dfs":20,"mododedfs":"inativo"},{'nome':"Squirtle","dano":35,"vida":100,"dfs":30,"mododedfs":"inativo"},{'nome':"Bulbassaur","dano":30,"vida":110,"dfs":30,"mododedfs":"inativo"}]

pokej1 = PokeDisponiveis[j1]

pokej2 = PokeDisponiveis[j2]

print('Seu pokemon é : ',pokej1['nome'])

print('Pokemon do adversario é : ',pokej2['nome'])

print('<<<<<<<<<<<<<<<<<<<<Agora vai começar o derramamento!!!>>>>>>>>>>>>>>>>>>>')

while pokej1["vida"] >=0 and pokej2["vida"] >=0 :
    print("escolha uma ação: ")
    print('1 : atacar')
    print('2 : defender')
    print('3 : fugir')
    escj1 = int(input('Qual sua escolha? '))
    if escj1 == 1 :
        if  pokej2['mododedfs'] == "ativo" :
            dano = (pokej1['dano']-pokej2['dfs'])/2
            pokej2['vida']=pokej2['vida']-dano
            print("você atacou e tirou",dano,"do adversario")
        else : 
            pokej2['mododedfs'] == "ativo" 
            dano = (pokej1['dano']-pokej2['dfs'])
            pokej2['vida']=pokej2['vida']-dano
            print("você atacou e tirou",dano,"do adversario")
    elif escj1 == 2 : 
        pokej1['mododedfs'] == 'ativo'
        print('Você defendeu!!')
    else : 
        break

    pokej2['mododedfs'] = 'inativo'
    
    escj2 = random.randint (1,2)

    if escj2 == 1:
        if  pokej1['mododedfs'] == "ativo" :
            dano = (pokej2['dano']-pokej1['dfs'])/2
            pokej1['vida']=pokej1['vida']-dano
            print("Adversario atacou e tirou",dano,"do seu",pokej1["nome"])
        else : 
            pokej1['mododedfs'] == "ativo"
            dano = (pokej1['dano']-pokej2['dfs'])
            pokej1['vida']=pokej1['vida']-dano
            print("Adversario atacou e tirou",dano,"do seu",pokej1["nome"])
    elif escj2 == 2 : 
        pokej2['mododedfs'] == 'ativo'
        print('Adversario defendeu!!')
    pokej1["mododedfs"] = 'inativo'   
    print('Sua vida ',pokej1['vida']) 
    print('Vida do adversario é',pokej2['vida'])
if pokej1['vida'] > pokej2['vida'] :
    print("Você ganhou, Parabéns!!!!")
else :
    print('Você perdeu ;-;, melhore!!')