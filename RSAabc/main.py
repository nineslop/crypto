def gcd(a, b): # Greatest common divisor
    while b:
        a, b = b, a % b
    return a

def comparison(comp: list[int]) -> int: # Returns the solve of comparison y ≡ g^x(mod p)
    for y in range(10000):
        if ((comp[0] * y) % comp[2]) == (comp[1] % comp[2]):
            return y

p = 47
q = 43
n = p * q
fi = (p - 1) * (q - 1)
e = [i for i in range(fi) if gcd(fi, i) == 1][5]
d = comparison([e, 1, fi])

alphabet = ['q', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
open_text = "Тот, кто ложится на два стула, падает на ребра.".replace("ё", "е").replace(".", "тчк").replace(",", "зпт").replace("-", "тире").replace(" ", "").lower()
# open_text = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя".replace("ё", "е").replace(".", "тчк").replace(",", "зпт").replace("-", "тире").replace(" ", "").lower()
cypher_text = ""

for let in open_text:
    cypher_text += str((alphabet.index(let) ** e) % n) + " "



print(cypher_text)



