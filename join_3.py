import sqlite3

conexao = sqlite3.connect("Biblioteca.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS autor(
    id INTEGER PRIMARY KEY,
    nome TEXT
    )
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS livro(
    id INTEGER PRIMARY KEY,
    autor_id INTEGER,
    titulo TEXT,
    FOREIGN KEY (autor_id) REFERENCES autor(id)
    )
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS genero(
    id INTEGER PRIMARY KEY,
    livro_id INTEGER,
    genero TEXT,
    FOREIGN KEY (livro_id) REFERENCES livro(id)
    )
""")

cursor.execute("INSERT INTO autor(nome) VALUES('George Orwell'),('Manuel Bandeira'),('Mário Quintana')")
cursor.execute("""INSERT INTO livro(autor_id, titulo) VALUES
               (1,'1984'),
               (1,'A Revolução dos Bichos'),
               (2,'Estrela da Manhã'),
               (4,'Dagon')
""")

cursor.execute("""INSERT INTO genero(livro_id, genero) VALUES
               (1,'Ficção'),
               (1,'Literatura'),
               (2,'Ficção'),
               (4,'Horror')
""")

# JOIN COM INNER -> REGISTROS QUE CASAM NAS DUAS TABELAS 
cursor.execute("""
SELECT
  l.titulo       AS livro,
  a.nome         AS autor,
  b.genero       AS genero
FROM livro AS l
  INNER JOIN autor AS a
    ON l.autor_id = a.id
  INNER JOIN genero AS b
    ON b.livro_id = l.id;
""")

for livro, autor, genero in cursor.fetchall():
    print(f"\"{livro}\" de {autor} — Gênero: {genero}")

conexao.commit()
conexao.close()
