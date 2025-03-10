### contextlib
db 세션 객체 생성 후 `db.close()`를 호출하지 않는다면 -> SQLAlchemy가 사용하는 컨넥션 풀에 db 세션이 반환되지 않아 문제가 생긴다

contextlib -> 자동화 가능하도록 만듦


