from config import CONN, CURSOR

class Song:

    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """

        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song
    

        

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.album))
        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]
        CONN.commit()

Song.create_table()
song = Song.create("Hello2", "26")
song.name
# => "Hello"
song.album
# => "25"
hello = Song("Hello", "25")
hello.save()

despacito = Song("Despacito", "Vida")
despacito.save()

hello.id
# => 1
despacito.id
CURSOR.execute('SELECT * FROM songs')
songs = CURSOR.fetchall()
print(songs)

# query = "DROP TABLE IF EXISTS song;"
# CURSOR.execute(query)

# # Commit the changes and close the connection
# CONN.commit()
# CONN.close()
