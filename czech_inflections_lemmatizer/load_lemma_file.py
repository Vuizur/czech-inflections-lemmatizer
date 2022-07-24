import csv
import sqlite3

def create_sqllite_db(db_path):
    """Creates an sqlite database with one table and two rows: lemma and inflection"""
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("""CREATE TABLE iF NOT EXISTS lemma_inflection (
                lemma TEXT,
                inflection TEXT)""")
    conn.commit()
    conn.close()

def create_indices(db_path):
    """Creates indices for the lemma and inflection columns"""
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("""CREATE INDEX lemma_index ON lemma_inflection (lemma)""")
    c.execute("""CREATE INDEX inflection_index ON lemma_inflection (inflection)""")
    conn.commit()
    conn.close()

def fix_lemma(word):
    """Remove everything in the string after (and including) the first _"""
    if word.find('_') != -1:
        return word[:word.find('_')]
    else:
        return word

def load_lemma_file(lemma_file_path, database_path):
    """Loads the lemma TSV """
    conn = sqlite3.connect(database_path)
    c = conn.cursor()

    with open(lemma_file_path, 'r', encoding='utf-8') as lemma_file:
        lemma_file_reader = csv.reader(lemma_file, delimiter='\t')
        for row in lemma_file_reader:
            # Fix the lemma
            lemma = fix_lemma(row[0])
            # Write into database
            c.execute("""INSERT INTO lemma_inflection (lemma, inflection) VALUES (?, ?)""", (lemma, row[2]))
            # Print every 100 000 rows
            if (lemma_file_reader.line_num % 100000 == 0):
                print("Loaded {} rows".format(lemma_file_reader.line_num))
        conn.commit()    

def remove_duplicates(database_path):
    """Removes duplicates from the database"""
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("""CREATE TABLE temp_table as SELECT DISTINCT * FROM lemma_inflection;""")
    c.execute("""DELETE FROM lemma_inflection;""") 
    c.execute("""INSERT INTO lemma_inflection SELECT * FROM temp_table""")
    c.execute("""DROP TABLE temp_table;""")
    # Vacuum
    c.execute("""VACUUM""")
    conn.commit()
    conn.close()

def create_and_fill_database(lemma_file_path, database_path):
    """Creates and fills the database"""
    create_sqllite_db(database_path)
    load_lemma_file(lemma_file_path, database_path)
    print("Creating indices...")
    create_indices(database_path)
    print("Removing duplicates...")
    try:
        remove_duplicates(database_path)
    except:
        print("Could not remove duplicates")


if __name__ == "__main__":
    lemma_tsv_path = "D:/programming_resources/czech-morfflex-2.0.tsv"
    db_path = 'lemma_inflection.db'

    print("Test")
    #create_and_fill_database(lemma_tsv_path, db_path)