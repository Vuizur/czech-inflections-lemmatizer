import sqlite3
from lemmatizer import Lemmatizer

def test_vecer():
    con = sqlite3.connect("lemma_inflection.db")
    cur = con.cursor()
    # Write a request to the database for all words that are like večer%, order by lemma length
    cur.execute("SELECT * FROM lemma_inflection WHERE lemma LIKE 'večer%' ORDER BY LENGTH(lemma)")


    # Print to a tsv file
    with open("večer.tsv", "w", encoding = "utf-8") as f:
        for row in cur:
            f.write("\t".join(row) + "\n")
    
    #cur.execute("SELECT * FROM lemma_inflection WHERE lemma LIKE 'večer%'")
    con.close()

if __name__ == "__main__":
    lemm = Lemmatizer("lemma_inflection.db")
    print(lemm.find_inflections("večer"))
    print(lemm.find_lemma("lesa"))

