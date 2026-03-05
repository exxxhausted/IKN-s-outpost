input_str = input()
codes = [int(code) for code in input_str.split() if 0 <= int(code) <= 255]
koi8_bytes = bytes(codes)
utf8_text = koi8_bytes.decode('koi8-r')  
print(utf8_text)