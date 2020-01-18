def percent():
    text = input('Введите текст: ')
    length = len(text)
    res = res_1 = 0
    for i in text:
        if 'a'<=i<='z':
            res += 1
        elif "A"<=i<='Z':
            res_1 += 1
    result = "%% строчных букв: %.2f" % (res/length * 100)
    result_2 = "%% прописных букв: %.2f" % (res/length * 100)
    return result, result_2

print(percent())


