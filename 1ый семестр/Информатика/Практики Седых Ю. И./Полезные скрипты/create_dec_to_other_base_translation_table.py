import sys

def convert_number(decimal, base):
    expressions = []
    quotients = []
    remainders = []
    
    symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    current = decimal
    while current > 0:
        quotient = current // base
        remainder = current % base
        expressions.append(f"${current} \\div {base}$")
        quotients.append(str(quotient))
        remainders.append(symbols[remainder])
        current = quotient
    
    print("," * len(expressions))
    print(f"Выражение,{','.join(expressions)}")
    print(f"Частное,{','.join(quotients)}")
    print(f"Остаток,{','.join(remainders)}")

decimal = int(sys.argv[1])
base = int(sys.argv[2])
convert_number(decimal, base)