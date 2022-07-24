from load_lemma_file import remove_duplicates
from lemmatizer import Lemmatizer


if __name__ == "__main__":
    lemm = Lemmatizer("lemma_inflection.db")
    print(lemm.find_inflections("červenat"))
    print(lemm.find_lemma("lesa"))