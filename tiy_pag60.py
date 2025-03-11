#4-3. Counting to twenty
#for valor in range(1,21):
#    print(valor)

#4-4. One millon
#for contar in range(1,1000001):
#    print(contar)

#4-5. Summing a Millon
#millon = list(range(1,1000001))
#print(min(millon))
#print(max(millon))
#print(sum(millon))

#4-6. Odd numbers
#odd = list(range(1,20,2))
#print(odd)

#4-7. Threes
#for valor in range(0,31,3):
#    print(valor)

#4-8. Cubes
cubos = []
for valor in range(1,11):
    cubo = valor**3
    cubos.append(cubo)
print(cubos)


#4-9.Cube Comprehension
cube = [value**3 for value in range(1,11)]
print(cube)