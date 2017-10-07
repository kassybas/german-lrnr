import yaml
import random
words = {}

class WordPair(object):
    def __init__(self, ger, eng):
        self.ger = ger
        self.eng = eng

def load_words():
    words = list()
    with open('words.yaml') as f:
        d = yaml.load(f)
        for k, v in d.items():
            words.append(WordPair(k,v))
        return words


def main():
    d = load_words()
    limit = len (d)
    for i in range(10):
        print("\n - - - - - - - - - - -")
        print(i+1)
        x = random.randrange(0, limit)
        print("->Eng: " + d[x].eng)
        input("Guess: ")
        print("-<Ger: " + d[x].ger)
        print("\n - - - - - - - - - - -")

if __name__=="__main__":
    main()

