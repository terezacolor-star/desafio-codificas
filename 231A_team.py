n = int(input())

contador = 0

for i in range(n):
    petya, vasya, tonya = map(int, input().split())

    if petya + vasya + tonya >= 2:
        contador += 1

print(contador)
