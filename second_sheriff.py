def second_task():
    input_string = input()

    letters = {'s': 0, 'h': 0, 'e': 0, 'r': 0, 'i': 0, 'f': 0}
    letters_keys = list(letters.keys())

    for s in input_string:
        if s in letters_keys:
            letters[s] += 1

    min_words = min(list(letters.values()))

    if letters['f'] >= min_words*2:
        print(min_words)
    else:
        print(min_words - 1)


if __name__ == '__main__':
    second_task()
