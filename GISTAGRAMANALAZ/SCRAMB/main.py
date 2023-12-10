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
        # for i in range(len(s)):
        #     print(i + 1, s[i])
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
            arr += tmp
        # print(arr)
        print("CODING MESSAGE WITH BIN MAP (CODING MESSAGE):")
        for i in range(len(arr)):
            if (i + 1) % 6 == 0:
                print(arr[i], end=" ")
            else:
                print(arr[i], end="")
        for i in range(len(arr)):
            res.append(int(arr[i]) ^ gamma[i])
        return res

    def standart_output(self, message: list[int]) -> None:
        tmp = []
        print()
        print("CODE BIN REPRESENTING - (ЭТО ВСТАВЛЯТЬ)")
        while message:
            if len(tmp) == 5:
                print("".join(tmp), end=" ")
                tmp = []
            tmp.append(str(message.pop(0)))
        if tmp:
            print("".join(tmp))
        print()

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

        print(f'DECRYPT MESSAGE - {message.replace("тчк", ".").replace("зпт", ",")}')


if __name__ == "__main__":
    message = "."
    c = Crypt_A52("01101", "10010")  # x^5 + x^3 + x ^ 2 + x + 1
    gamma1 = c.generate_gamma(message)
    print(f'GAMMA1 - \t  {gamma1}')
    c1 = Crypt_A52("10101", "10100")  # x^4 + x^2 + 1
    gamma2 = c1.generate_gamma(message)
    print(f'GAMMA2 - \t  {gamma2}')
    gamma = c.total_xor(gamma1, gamma2)
    print(f'TOTAL GAMMA - {gamma}')
    c.standart_output(c.encypt(gamma, message))

    output = "11111 10111 10110 01111 11100 00111 10000 00001 10100 11001 00010 00010 11001 11001 00110 11011 10010 10000 11101 10110 10111 01111 01010 00111 00100 11111 01001 01100 10010 01011 00000 00110 10111 00101 10001 10110 10010 01010 01010 00010 01101 00101 01100 11100 10011 10011 00110 11100 01111 11111 01110 00010 01111 00001"
    output = output.split()
    main_output = ""
    print("DECIMAL REPRESENTING - ")
    for i in output:
        tmp = str(int(i, 2))
        while len(tmp) != 2:
            tmp = "0" + tmp
        main_output += tmp
    for i in range(len(main_output)):
        if (i + 1) % 5 == 0:
            print(main_output[i], end=" ")
        else:
            print(main_output[i], end="")
    print()
    tmp_encrypt_messsage = ""
    encrypt_messsage = list(
        "31232 21528 07160 12025 02022 52506 27181 62922 23151 00704 31091 21811 00062 30517 22181 01002 13051 22819 19062 81531 14021 501".replace(
            " ", ''))
    tmp_char = ""
    while encrypt_messsage:
        if len(tmp_char) == 2:
            x = bin(int(tmp_char))[2:].zfill(5)
            tmp_encrypt_messsage += x
            # print(x)
            tmp_char = ""
        tmp_char += encrypt_messsage.pop(0)
    if tmp_char:
        tmp_encrypt_messsage += bin(int(tmp_char))[2:]

    c.decrypt(gamma, tmp_encrypt_messsage)