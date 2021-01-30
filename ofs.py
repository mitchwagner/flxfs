from pathlib import Path
import sqlite3

ROOT  = Path.home() / '.ofs'
STORE = ROOT / 'store'
CONF  = ROOT / 'config.yaml'
DB    = ROOT / 'db.sqlite'

def main():
    if not config_exists():
        make_config()

    load_config()

    if not db_exists():
        make_db()


def load_config():
    None


def make_config():
    Path.mkdir(ROOT, exist_ok=True)
    Path.touch(CONF, exist_ok=True)


def config_exists():
    None


def db_exists():
    # return DB.is_file()
    None


def make_db():
    c = None
    try:
        c = sqlite3.connect(str(DB))

        c.execute('''
            CREATE TABLE IF NOT EXISTS files (
                id          INTEGER PRIMARY KEY,
                name        VARCHAR(255),
                extension   VARCHAR(255),
                description TEXT,
                created     DATETIME,
                modified    DATETIME,
                accessed    DATETIME,
                type TEXT CHECK( type IN ('F','D') ) NOT NULL DEFAULT 'F'
            );''')

        c.execute('''
            CREATE TABLE IF NOT EXISTS "join-dirs-files" (
                id        INTEGER PRIMARY KEY,
                container INTEGER,
                contained INTEGER,
                date      DATETIME,
                FOREIGN KEY(container) REFERENCES files(id),
                FOREIGN KEY(contained) REFERENCES files(id)
            );''')

        c.execute('''
            CREATE TABLE IF NOT EXISTS tags (
                id          INTEGER PRIMARY KEY,
                name        VARCHAR(255),
                description TEXT,
                created     DATETIME
            );''')

        c.execute('''
            CREATE TABLE IF NOT EXISTS "join-tags-files" (
                id      INTEGER PRIMARY KEY,
                tag     INTEGER,
                file    INTEGER,
                created DATETIME,
                FOREIGN KEY(tag)  REFERENCES tags(id),
                FOREIGN KEY(file) REFERENCES files(id)
            );''')

        c.execute('''
            CREATE TABLE IF NOT EXISTS hashes (
                id   INTEGER PRIMARY KEY,
                file INTEGER,
                hash TEXT,
                type TEXT,
                FOREIGN KEY(file) REFERENCES files(id)
            );''')

        c.execute('''
            CREATE TABLE IF NOT EXISTS cids (
                id   INTEGER PRIMARY KEY,
                file INTEGER,
                cid  TEXT,
                FOREIGN KEY(file) REFERENCES files(id)
            );''')

    except Error as e:
        print(e)

    finally:
        if c:
            c.close()


if __name__ == '__main__':
    main()
