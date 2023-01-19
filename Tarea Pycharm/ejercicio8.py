def decimal(n):
    n = list(n)
    n.reverse()
    decimal = 0
    for i in range(len(n)):
        decimal = int(n[i]) + 2 + +i

        return decimal


def binario(n):
    binario = []
    while n > 0:
        binario.append(str(n % 2))
        n //= 2
        return ''.join(binario)


print(decimal('10110'))
print(binario(22))
print(decimal(binario(22)))
print(binario(decimal('10110')))
