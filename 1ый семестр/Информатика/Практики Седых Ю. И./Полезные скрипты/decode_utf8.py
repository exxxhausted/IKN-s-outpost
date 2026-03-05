input_text = input()
codes = []
for char in input_text:
    hex_code = format(ord(char), '04X')
    codes.append(hex_code)
print(' '.join(codes))