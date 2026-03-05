input_text = input()
cp1251_bytes = input_text.encode('cp1251')
codes = [byte for byte in cp1251_bytes]
print(' '.join(map(str, codes)))