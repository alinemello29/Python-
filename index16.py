#Sets - Exercício

#1- verficarr se 'Eric' e 'john' existem em amigos
#2- combinar ou adicionar os dois conjuntos
#3- encontrat nomes que estão em ambos os conjuntos
#4- encontrar nomes que estão apenas em amigos
#5- mostrar apenas os nomes que aparecem apenas em uma das listas
#6- crie uma lista de carros sem duplicatas

friends= {'jhon','michael','terry','erci','graham'}
my_friends={'ali' , 'loretta' ,'colin' , 'jhon' , 'keke'}
cars=['900','420','v70','911','996','v90','911']

print('eric' in frineds and 'jhon' in friends)
print(my_friends.symmetric_difference(friends))
print(friends-my_friends)
cars_no_dupl=list(set(cars))
print(cars_no_dupl)
