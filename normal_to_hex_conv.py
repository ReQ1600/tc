# konwertuje zwykłe liczby na zapis w hexie do logisima
# jest w pythonie bo to z czata a on pythona lepiej ogarnia
# Definicja słownika do mapowania cyfr na odpowiednie kody
code_map = {
    '0': 'fc',
    '1': '60',
    '2': 'da',
    '3': 'f2',
    '4': '66',
    '5': 'b6',
    '6': 'bf',
    '7': 'e0',
    '8': 'fe',
    '9': 'f7'
}

# Funkcja, która konwertuje liczbę na kodowaną reprezentację
def encode_number(number):
    str_num = f"{number:03d}"  # Upewniamy się, że liczba jest trzycyfrowa
    return code_map[str_num[0]] + code_map[str_num[1]] + code_map[str_num[2]]

# Generowanie listy zakodowanych liczb od 000 do 999
encoded_numbers = [encode_number(i) for i in range(1000)]

# Zapisywanie wyników do pliku, 8 liczb na wiersz
with open('encoded_numbers.txt', 'w') as file:
    for i in range(0, len(encoded_numbers), 8):
        file.write(' '.join(encoded_numbers[i:i+8]) + '\n')
