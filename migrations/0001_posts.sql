CREATE TABLE IF NOT EXISTS posts (
  id INTEGER PRIMARY KEY AUTOINCREMENT, created_at TEXT NOT NULL, course TEXT NOT NULL DEFAULT 'chung', lesson TEXT NOT NULL DEFAULT 'chung',
  kind TEXT NOT NULL CHECK (kind IN ('kho-khan','y-tuong','ket-qua','gop-y')), body TEXT NOT NULL,
  visibility TEXT NOT NULL CHECK (visibility IN ('cong-khai-ten','cong-khai-an-danh','rieng-tu')), display_name TEXT, region TEXT, child_ages TEXT,
  status TEXT NOT NULL DEFAULT 'cho-duyet' CHECK (status IN ('cho-duyet','da-duyet','tu-choi')), reviewed_at TEXT, review_note TEXT, reply TEXT);
