import heapq
from collections import defaultdict, Counter

# Словарь кодов Хаффмана для декодирования
codes: dict[str, str] = {
    '1111': 'A',
    '011100': 'B',
    '01000': 'C',
    '11011': 'D',
    '100': 'E',
    '01001': 'F',
    '00001': 'G',
    '0101': 'H',
    '1010': 'I',
    '110100000': 'J',
    '110100011': 'K',
    '01111': 'L',
    '00011': 'M',
    '1100': 'N',
    '1110': 'O',
    '110101': 'P',
    '1101000101': 'Q',
    '1011': 'R',
    '0110': 'S',
    '001': 'T',
    '00010': 'U',
    '1101001': 'V',
    '011101': 'W',
    '110100001': 'X',
    '00000': 'Y',
    '1101000100': 'Z'
}

# Обратный словарь для кодирования (символ -> код)
encode_codes = {v: k for k, v in codes.items()}

# Сортировка ключей словаря по длине для декодирования (от длинных к коротким)
els = sorted(codes.keys(), key=len, reverse=True)

def huffman_encode(text):
    if not text:
        return "", {}
    
    # Кодирование текста с использованием фиксированного словаря
    try:
        encoded = "".join(encode_codes[char] for char in text.upper() if char in encode_codes)
        return encoded, encode_codes
    except KeyError:
        raise ValueError("Ошибка: Текст содержит символы, отсутствующие в словаре кодов.")

def huffman_decode(code: str) -> str:
    output: list[str] = []
    code = code.replace(" ", "")  # Удаляем пробелы из входного кода
    while code:
        found = False
        for e in els:
            if code.startswith(e):
                output.append(codes[e])
                code = code[len(e):]
                found = True
                break
        if not found:
            raise ValueError(f"Не удалось расшифровать: неизвестный префикс в '{code}'")
    return ''.join(output)

def main():
    mode = input("Выберите режим (1 - кодирование, 2 - декодирование): ")
    
    if mode == "1":
        text = input("Введите английский текст для кодирования: ")
        if not text.isascii() or not text.replace(" ", "").isalpha():
            print("Ошибка: Введите текст, содержащий только английские буквы и пробелы.")
            return
        
        try:
            encoded, generated_codes = huffman_encode(text)
            print("Сжатый текст (двоичный код):", encoded)
            print("Коды Хаффмана (для информации):", generated_codes)
        except ValueError as e:
            print("Ошибка:", e)
        
    elif mode == "2":
        encoded = input("Введите двоичный код (через пробелы или без): ")
        try:
            decoded = huffman_decode(encoded)
            print("Декодированный текст:", decoded)
        except ValueError as e:
            print("Ошибка:", e)
        
    else:
        print("1 or 2?")

if __name__ == "__main__":
    main()