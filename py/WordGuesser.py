print("hello world")
words = {'аллея', 'бомба', 'вверх', 'взрыв', 'внизу',
'вьюга', 'горох', 'готов', 'густо', 'давай',
'давно', 'книга', 'конец', 'лилия', 'линия',
'можно', 'назад', 'нравы', 'песец', 'песня',
'порох', 'порыв', 'потом', 'право', 'пусто',
'румба', 'скоро', 'супер', 'травы', 'тумба',
'тунец', 'фугас', 'шприц', 'щипок', 'щипцы'}
comand = ""
i = 0
letters = []
def func(letters, words):
    print(letters)
    length = len(letters)
    ans = filterWords(length)
    return ans

def filterWords(l):
    result = []
    for word in words:
        for i in range(0, l):
            char = word[i]
            if (char in letters[i] and i == l - 1):
                result.append(word)
            elif char in letters[i]:
                continue
            else:
                break
    return result

while comand != "stop":
    comand = input("Набор букв: ")
    i += 1
    if comand == "r":
        i = 0
        letters.clear()
    else:
        letters.append(comand)
    possibleAns = func(letters, words)
    print(possibleAns)
