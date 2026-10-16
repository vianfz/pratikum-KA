
from flask import Flask
import sqlite3
import os

app = Flask(__name__)

DATABASE = os.environ.get(
    "DATABASE_PATH",
    os.path.join(os.path.dirname(__file__), "app.db")
)


def init_db():
    os.makedirs(os.path.dirname(DATABASE) or ".", exist_ok=True)

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mahasiswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            jurusan TEXT NOT NULL
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM mahasiswa")
    if cursor.fetchone()[0] == 0:
        cursor.execute(
            "INSERT INTO mahasiswa (nama, jurusan) VALUES (?, ?)",
            ("Vian", "Sistem Informasi")
        )

    conn.commit()
    conn.close()


@app.route("/")
def home():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nama, jurusan FROM mahasiswa")
    data = cursor.fetchall()
    conn.close()

    hasil = "<h1>Data Mahasiswa</h1><ul>"
    for mahasiswa in data:
        hasil += f"<li>{mahasiswa[1]} - {mahasiswa[2]}</li>"
    hasil += "</ul><p>Database berhasil terhubung!</p>"

    return hasil


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
