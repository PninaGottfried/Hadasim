file_name = 'text.txt'
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'purple', 'pink', 'silver', 'gold', 'beige',
          'brown', 'grey', 'gray', 'black', 'white']
gramer_words = ['am', 'is', 'are', 'don\'t', 'that', 'the', 'and', 'of', 'to', 'a', '\n', '']


def func(file):
    lines = file.readlines()
    words1 = [line.split(' ') for line in lines]
    words = []
    for w in words1:
        words += w

    ex1 = len(lines)

    ex2 = len(words)

    ex3 = ex2

    ex5_1 = ''
    ex5_1_cnt = 0
    ex5_2 = ''
    ex5_2_cnt = 0

    words_dict = {}
    for word in words:
        if word in words_dict.keys():
            words_dict[word] += 1
            ex3 -= 1

            if words_dict[word] > ex5_1_cnt:
                ex5_1 = word
                ex5_1_cnt = words_dict[word]
            if word not in gramer_words and words_dict[word] > ex5_2_cnt:
                ex5_2 = word
                ex5_2_cnt = words_dict[word]
        else:
            words_dict[word] = 1

    ex4_max = max(line.count(' ') for line in lines)
    ex4_average = len(words) / len(lines)
    ex4 = (ex4_average, ex4_max)

    ex5 = (ex5_1, ex5_2)

    ex6 = 0
    cnt = 0
    for word in words:
        if 'k' in word:
            ex6 = max(ex6, cnt)
            cnt = 0
        else:
            cnt += 1

    ex7 = None

    ex8 = []
    for color in colors:
        if color in words_dict.keys():
            ex8.append((color, words_dict[color]))

    ex9 = None

    return ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8, ex9


with open(file_name, 'r') as file:
    result = func(file)
    print('1:: ', result[0], 'lines')
    print('2:: ', result[1], 'words')
    print('3:: ', result[2], 'unique words')
    print('4:: ', result[3][0], '- average line length,', result[3][1], '- maximal line length')
    print('5:: ', "'" + result[4][0] + "'", 'the most popular word,', "'" + result[4][1] + "'", 'without grammer')
    print('6:: ', result[5], 'consecutive words without \'K\'')
    print('8:: ', end=' ')
    for color, times in result[7]:
        print(color, times, 'times', end=', ')
