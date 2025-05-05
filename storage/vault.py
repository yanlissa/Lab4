import os
import sqlite3
from cryptography.fernet import Fernet

KEY_FILE = "storage/key.key"

def load_or_create_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        return key
    
def init_db():
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT,
            login TEXT,
            password_encrypted TEXT
        )
    ''')
    conn.commit()
    conn.close()
    
def save_password(service, login, password_plain):
    encrypted = cipher.encrypt(password_plain.encode()).decode()
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("INSERT INTO passwords (service, login, password_encrypted) VALUES (?, ?, ?)",
              (service, login, encrypted))
    conn.commit()
    conn.close()

def load_passwords():
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("SELECT id, service, login, password_encrypted FROM passwords")
    rows = c.fetchall()
    conn.close()
    return [(r[0], r[1], r[2], cipher.decrypt(r[3].encode()).decode()) for r in rows]

key = load_or_create_key()
cipher = Fernet(key)