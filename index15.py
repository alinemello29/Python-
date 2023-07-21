#sets - Exercício

#1. Verfique se 'Eric' e 'Jhon' existem em amigos
#2. Combinar ou adicionar os dois conjuntos
#3. Encontrar nomes que estão em ambos os conjuntos
#4. Encontrar nomes que estão apenas em amigos
#5. Mostrar apenas os nomes que aprecem  apenas em uma das listas
#6. Crie uma nova lista de acrros sem duplicatas

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

print('Eric' in friends and 'John' in friends)
print(my_friends.symmetric_difference(friends))
print(my_friends ^ friends)
cars_no_dupl =list(set(cars))
print(cars_no_dupl)