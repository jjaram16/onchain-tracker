import sqlite3
from pathlib import Path

DB_PATH = Path("tracker.db")

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_db():
    with get_conn() as conn, open("schema.sql","r") as f:
        conn.executescript(f.read())
        cur = conn.execute("SELECT COUNT(*) FROM blocks_seen WHERE id=0;")
        if cur.fetchone()[0] == 0:
            conn.execute("INSERT INTO blocks_seen (id, last_block) VALUES (0, 0);")

def get_last_block():
    with get_conn() as conn:
        (h,) = conn.execute("SELECT last_block FROM blocks_seen WHERE id=0;").fetchone()
        return h

def set_last_block(h: int):
    with get_conn() as conn:
        conn.execute("UPDATE blocks_seen SET last_block=? WHERE id=0;", (h,))

def upsert_wallets(addresses):
    with get_conn() as conn:
        conn.executemany("INSERT OR IGNORE INTO wallets(address) VALUES (?)",
                         [(a.lower(),) for a in addresses])
