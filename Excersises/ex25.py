def break_words(stuff):
    """This function will break up wwords for us"""
    words=stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_last_word(words):
    """Prints the last word after popping it off"""
    word=words.pop(-1)
    print (word)

def print_first_word(words):
    """Prints the first word after popping it off"""
    print(words.pop(0))

def sort_sentence(sentence):
    """takes a full sentence and returns sorted words"""
    words=break_words(sentence)
    return (sort_words(words))

def print_first_and_last_sorted(sentence):
    words=sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
