n = int(input())

for i in range(n):
    palavra = input()

    if len(palavra) > 10:
        print(palavra[0] + str(len(palavra) - 2) + palavra[-1])
    else:
        print(palavra)

