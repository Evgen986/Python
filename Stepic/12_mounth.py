# Решите уравнение в натуральных числах 28n + 30 k + 31 m = 365
for a in range(1, 15):
    for b in range(1, 15):
        for c in range(1, 15):
            for d in range(1, 15):
                for e in range(1, 15):
                    if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                        print(f'(a = {a}) + (b = {b}) + (c = {c}) + (d = {d}) = (e = {e})')
