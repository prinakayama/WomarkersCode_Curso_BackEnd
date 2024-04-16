# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa 
# sobre um crime. As perguntas são:""Telefonou para a vítima?"" , 
# ""Esteve no local do crime?"", ""Mora perto da vítima?"", 
# ""Devia para a vítima?"" ""Já trabalhou com a vítima?"" 
# O programa deve no final emitir uma classificação sobre a participação
# da pessoa no crime. Se a pessoa responder positivamente a 2 questões 
# ela deve ser classificada como ""Suspeita"",entre 3 e 4 como ""Cúmplice""
# e 5 como ""Assassino"". Caso contrário, ele será classificado como ""Inocente"".


telefonou_para_vitima = False
esteve_no_local_do_crime = False
mora_perto_da_vitima = False
devia_para_a_vitima = False
ja_trabalhou_com_a_vitima = False


telefonou_para_vitima = input("Telefonou para a vítima? (s/n): ") == "s"
esteve_no_local_do_crime = input("Esteve no local do crime? (s/n): ") == "s"
mora_perto_da_vitima = input("Mora perto da vítima? (s/n): ") == "s"
devia_para_a_vitima = input("Devia para a vítima? (s/n): ") == "s"
ja_trabalhou_com_a_vitima = input("Já trabalhou com a vítima? (s/n): ") == "s"


num_respostas_positivas = int(telefonou_para_vitima) + int(esteve_no_local_do_crime) + int(mora_perto_da_vitima) + int(devia_para_a_vitima) + int(ja_trabalhou_com_a_vitima)

if num_respostas_positivas == 2:
    classificacao = "Suspeita"
elif num_respostas_positivas >= 3 and num_respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif num_respostas_positivas == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"


print("Classificação:", classificacao)