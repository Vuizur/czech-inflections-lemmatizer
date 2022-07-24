# Czech lemmatizer and inflection finder

This project uses the data from https://ufal.mff.cuni.cz/morfflex to generate a SQLITE database that can then be used to:

* Find the lemma of a word
* Find all inflections of a word

Warning: The created database is more than 10 GB large.

### Install

You need to download the file under https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-3186/czech-morfflex-2.0.tsv.xz, unpack it, and then run load_lemma_file.py (while editing the constants there to the correct paths).

Then you can use everything like this:

### Usage
```
lemm = Lemmatizer("lemma_inflection.db")
print(lemm.find_inflections("červenat"))
print(lemm.find_lemma("lesa"))
```