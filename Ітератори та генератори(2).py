def прості_числа(n):
    for число in range(2, n):
        є_простим = True
        for дільник in range(2, число):
            if число % дільник == 0:
                є_простим = False
                break
        if є_простим:
            yield число
print("Прості числа менші за 20:")
for х in прості_числа(20):
    print(х)