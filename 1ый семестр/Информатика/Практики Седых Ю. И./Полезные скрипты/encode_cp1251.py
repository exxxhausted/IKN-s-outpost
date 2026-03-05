input_str = input()
codes = [int(code) for code in input_str.split() if 0 <= int(code) <= 255]
cp1251_bytes = bytes(codes)
utf8_text = cp1251_bytes.decode('cp1251')  
print(utf8_text)