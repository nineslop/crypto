class Crypt_A52:
    def __init__(self, scramle: str, key: str, mode=1):
        if mode == 1:
            self.scrable = scramle[::-1]
            self.key = key
        else:
            self.scrable = scramle
            self.key = key
        self.alp = "qабвгдежзийклмнопрстуфхцчшщъыьэюя"


    def generate_gamma(self, message: str) -> list[int]:
        message = message.replace('ё', 'е').replace('.', 'тчк').replace(',', 'зпт').replace(" ", '').lower()
        indexes = []
        x1 = [self.key[-1]]
        s = [self.key]
        for i in range(len(self.scrable)):
            if self.scrable[i] == '1':
                indexes.append(i)
        while len(s) != len(message) * 6:
            curr = 0
            for i in indexes:
                curr ^= int(s[-1][i])
            s.append(str(curr) + s[-1][:-1])
            x1.append(s[-1][-1])
        print(s)
        print(f"PERIOD - {2 ** len(self.scrable) - 1}", end=" ")
        return list(map(int, x1))

    def total_xor(self, gamma_first: list[int], gamma_second: list[int]):
        res = []
        for i in range(len(gamma_first)):
            res.append(gamma_first[i] ^ gamma_second[i])
        return res


    def encypt(self, gamma: list[int], message: str):
        message = message.replace('ё', 'е').replace('.', 'тчк').replace(',', 'зпт').replace(" ", '').lower()
        res = []
        arr = ""
        for word in message:
            tmp = bin(self.alp.index(word))[2:]
            while len(tmp) != 6:
                tmp = "0" + tmp
            arr += (tmp)
        for i in range(len(arr)):
            res.append(int(arr[i]) ^ gamma[i])
        return res


    def standart_output(self, message: list[int]) -> None:
        tmp = []
        while message:
            if len(tmp) == 5:
                print("".join(tmp), end=" ")
                tmp = []
            tmp.append(str(message.pop(0)))
        if tmp:
            print("".join(tmp))


    def decrypt(self, gamma: list[int], encrypt_message: str):
        res = []
        for i in range(len(encrypt_message)):
            res.append(int(encrypt_message[i]) ^ gamma[i])
        tmp = []
        message = ""
        while res:
            if len(tmp) == 6:
                message += self.alp[int(''.join(tmp), 2)]
                tmp = []
            tmp.append(str(res.pop(0)))
        if tmp:
            message += self.alp[int(''.join(tmp), 2)]
        print(message)
        print(f'DECRYPT MESSAGE - {message.replace("тчк", ".").replace("зпт", ",")}')



if __name__ == "__main__":
    message = "Плохой работник никогда не найдёт хорошего инструмента."
    c = Crypt_A52("10010", "01011")
    gamma1 = c.generate_gamma(message)
    print(f'GAMMA1 - \t  {gamma1}')
    c1 = Crypt_A52("1001", "0101")
    gamma2 = c1.generate_gamma(message)
    print(f'GAMMA2 - \t  {gamma2}')
    gamma = c.total_xor(gamma1, gamma2)
    print(f'TOTAL GAMMA - {gamma}')
    c.standart_output(c.encypt(gamma, message))
    c.decrypt(gamma, "00111 11001 01100 10101 01111 10110 11101 10010 01010 11111 01110 10111 11010 10011 10100 00110 01000 00110 00010 01001 11111 00010 01100 00101 01100 10101 00111 11000 10101 00101 01100 01001 00111 00110 01001 00000 01100 01011 01010 01101 01110 11001 01000 10111 01100 10011 11001 11001 10011 10101 00100 00100 00011 10111 10101 01111 01011 00000 00001 00100 10011 1".replace(" ", ''))
