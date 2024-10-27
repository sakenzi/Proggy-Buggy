A)def calculate(Max: str, Min: str) -> int:
    max_power = len(Max) - 1
    min_power = -(len(Min) - 2)

    s = max_power - min_power

    return s

Max = input().strip()
Min =  input().strip()

print(calculate(Max, Min))