# Synomnymizer
# Myles Scholz

import re
import random as r

def lookup(words, string):
    synonyms = []
    for word in words:
        if word[0] == string and word[2] != "(noun)":
            synonyms.extend(word[3:-1])
    
    for i in range(len(synonyms)):
        terms = ["\n", " (generic term)", " (related term)", " (similar term)"]
        for term in terms:
            synonyms[i] = synonyms[i].replace(term, "")
    
    return synonyms

def run():
    thes = open("Thesaurus_a-z.csv")
    words = thes.readlines()
    for i in range(len(words)):
        words[i] = words[i].split(",")

    text = input("Text: ").lower()
    text = re.sub("[,;.!?]", "", text)
    text_words = text.split(" ")
    
    for i in range(len(text_words)):
        synonyms = lookup(words, text_words[i])
        if synonyms != []:
            j = r.randint(0, len(synonyms) - 1)
            text_words[i] = synonyms[j]

    out = " ".join(text_words).lower()
    print(out)

run()
