comand = ""
morze = {
    '13':'А',
    '3111':'Б',
    '133':'В',
    '331':'Г',
    '311':'Д',
    '1':'Е',
    '1113':'Ж',
    '3311':'З',
    '11':'И',
    '1333':'Й',
    '313':'К',
    '1311':'Л',
    '33':'М',
    '31':'Н',
    '333':'О',
    '1331':'П',
    '131':'Р',
    '111':'С',
    '3':'Т',
    '113':'У',
    '1131':'Ф',
    '1111':'Х',
    '3131':'Ц',
    '3331':'Ч',
    '3333':'Ш',
    '3313':'Щ',
    '33133':'Ъ',
    '3113':'Ь',
    '3133':'Ы',
    '11311':'Э',
    '1133':'Ю',
    '1313':'Я',
    }

word = []

def appendLetter(inp):
    try:
        word.append(morze[inp])
    except Exception:
        word.append(" ")
oldWord = []
while comand != "stop":
    comand = input("Набор знаков: ")
    if comand == "r":
        oldWord.clear()
        word.clear()
    elif comand == "s":
        oldWord.append(word)
        word = []
    else:
        appendLetter(comand)
    # possibleAns = func(letters, words)
    # print(letters)
    print("Новое слово")
    print(word)
    print("Старые слова")
    print(oldWord)
