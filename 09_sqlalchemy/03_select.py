# 03_select.py

from models import students, engine


select_sql = students.select()
print(select_sql)

with engine.connect() as conn:
    result = conn.execute(select_sql)
    # for idx, row in enumerate(result):
    #     print(idx, row)
    # 1件1件取り出す
    # print(result.fetchone())
    # print(result.fetchone())

    # 全件取り出し
    # print(result.fetchall())

    # 複数件指定
    rows = result.fetchmany(3)
    print(rows)
    print(rows[0], type(rows[0]))

    # 一部のカラムだけ取り出し
    print(rows[0].first_name)

    # 1件だけ取り出したい場合
    print(result.first())
    # print(result.fetchone())

    # where
    where_sql = students.select().where(students.c.first_name=='Taro')
    print(where_sql)
    print(where_sql.compile().params)
    print(conn.execute(where_sql).fetchall())
