message = "тотзптктоложитсянадвастулазптпадаетнаребратчк"
russian_alp = "qабвгдежзийклмнопрстуфхцчшщъыьэюя"
arr = []
E = 3
N = 33
D = 7
for ch in message:
    n = russian_alp.index(ch)
    print(n, end = " ")
    print
    string = str((n ** E) % N)
    while len(string) < len(str(N)):
        string = '0' + string
    arr.append(string)
print('/n')
print(arr)
for i in arr:
    print(russian_alp[(int(i) ** D) % N], end=" ")
