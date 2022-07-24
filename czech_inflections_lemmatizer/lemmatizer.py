import sqlite3


class Lemmatizer():
    """A class that uses the database to give find inflections for a lemma and to find lemmas for an inflection"""
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()

    def find_inflections(self, lemma):
        """Finds inflections for a lemma"""
        self.c.execute("""SELECT inflection FROM lemma_inflection WHERE lemma = ?""", (lemma,))
        # Convert to proper list
        inflections = [row[0] for row in self.c.fetchall()]
        return inflections

    def find_lemma(self, inflection):
        """Finds lemmas for an inflection"""
        self.c.execute("""SELECT lemma FROM lemma_inflection WHERE inflection = ?""", (inflection,))
        # Convert to proper list
        lemmas = [row[0] for row in self.c.fetchall()]
        return lemmas