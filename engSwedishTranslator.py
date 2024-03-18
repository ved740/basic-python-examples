trans_dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
def translate(b_dict,list_words):
    wordList = list_words.split(' ')
    wordListSwed = [trans_dict[x] for x in wordList if x in trans_dict]
    print(wordListSwed)
    return ' '.join(wordListSwed)
print(translate(trans_dict, "merry christmas and happy new year 2024"))