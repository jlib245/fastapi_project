### contextlib
db 세션 객체 생성 후 `db.close()`를 호출하지 않는다면 -> SQLAlchemy가 사용하는 컨넥션 풀에 db 세션이 반환되지 않아 문제가 생긴다

contextlib -> 자동화 가능하도록 만듦


### mypy
파이썬 비표준 라이브러리
`mypy XXX.py` 형태로 타입 어노테이션 검사


### Depends from FastAPI 
db: Session = Depends(get_db)의 db 객체에는 get_db 제너레이터 함수가 yield를 통해 생성한 세션 객체가 주입된다