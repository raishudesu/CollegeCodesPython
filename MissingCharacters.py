def missingCharacters(s):
    alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    num = ['1', '2', '3', '4', '5', '6', '8', '9']

    list = []
    for i in s:
        list.append(i)

    for element in list:
        if element in alp:
            alp.remove(element)

    for element in list:
        if element in num:
            num.remove(element)

    x = ''.join(alp)
    y = ''.join(num)

    print(y + x)
        

s = input()

missingCharacters(s)
