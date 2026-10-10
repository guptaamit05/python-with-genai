def capitalize_words(text):
    return "".join(word.capitalize() for word in text)

def reverse_string(text):
    return "".join(reversed(text))

def word_count(text):
    return len(text.split())