import sqlite3

def init_db():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    
    # テーブル作成
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            is_read INTEGER,
            title TEXT,
            author TEXT
        )
    ''')

    # memo.txtの読み込みとデータ挿入
    with open('memo.txt', 'r', encoding='utf-8') as f:
        for line in f:
            # データのパース (1,タイトル/著者)
            is_read, rest = line.strip().split(',', 1)
            title, author = rest.split('/')
            cursor.execute('INSERT INTO books (is_read, title, author) VALUES (?, ?, ?)',
                           (int(is_read), title, author))
    
    conn.commit()
    conn.close()
    print("Database initialized successfully!")

if __name__ == '__main__':
    init_db()