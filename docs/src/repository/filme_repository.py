from src.database.connection import connect


class FilmeRepository:

    def salvar(self, filme):

        conn = connect()

        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS filme (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT,
                duracao INTEGER,
                genero TEXT
            )
            """
        )

        cursor.execute(
            """
            INSERT INTO filme(titulo, duracao, genero)
            VALUES (?, ?, ?)
            """,
            (
                filme.titulo,
                filme.duracao,
                filme.genero
            )
        )

        conn.commit()

        conn.close()
