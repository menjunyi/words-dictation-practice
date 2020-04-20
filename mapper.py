import pymysql.cursors
# 连接数据库
connect = pymysql.Connect(
    host='rm-m5edlv0j8j79uj088co.mysql.rds.aliyuncs.com',
    port=3306,
    user='root',
    passwd='Mjy19950411',
    db='words',
    charset='utf8'
)


def insert(data):
    cursor = connect.cursor()
    sql = "INSERT INTO ietls_listening_material_answers (chapter, unit, sort, word) VALUES ( %d, %d, %d, '%s')"
    result = cursor.execute(sql % data)
    connect.commit()
    print(result)
    cursor.close()


def insert_practise(data):
    cursor = connect.cursor()
    sql = "INSERT INTO ietls_listening_material_record(chapter, unit, sort, time, speed, word, right_word, is_right )" \
          "VALUES ( %d, %d, %d, %d, '%s', '%s', '%s', '%s')"
    result = cursor.execute(sql % data)
    connect.commit()
    print(result)
    cursor.close()


def update(data):
    cursor = connect.cursor()
    # 修改数据
    sql = "UPDATE trade SET saving = %.2f WHERE account = '%s' "
    data = (8888, '13512345678')
    cursor.execute(sql % data)
    connect.commit()
    print('成功修改', cursor.rowcount, '条数据')


def get_wrong_words(time):
    cursor = connect.cursor()
    # 修改数据
    data = time
    sql = "select * from ietls_listening_material_record where time= %d and is_right = 0 order by unit,sort;"
    cursor.execute(sql % data)
    return cursor.fetchall()



def get_rate(time):
    cursor = connect.cursor()
    data = (time, time)
    sql = "select" \
        " a.cnt / b.cnt as rate, a.unit" \
        " from" \
        " (select count(*) cnt, unit" \
        " from ietls_listening_material_record where" \
        " is_right = 1 and time = %d" \
        " group by unit) a" \
        " join(select count(*) cnt, unit" \
        " from ietls_listening_material_record where" \
        " time = %d" \
        " group by unit) b" \
        " on" \
        " a.unit = b.unit"
    result = cursor.execute(sql % data)
    for row in cursor.fetchall():
        print("%s\t%s" % row)
    print('共查找出', cursor.rowcount, '条数据')
    cursor.close()


def get_answers(data):
    cursor = connect.cursor()
    sql = "SELECT word FROM ietls_listening_material_answers WHERE chapter = %d and unit = %d order by sort"
    cursor.execute(sql % data)
    return cursor.fetchall()


def delete_all_record(chapter, time):
    cursor = connect.cursor()
    sql = "DELETE FROM ietls_listening_material_record WHERE time =" + str(time) + " and chapter = " + str(chapter)
    cursor.execute(sql)
    connect.commit()
    print('成功删除', cursor.rowcount, '条数据')


def delete_answer(chapter):
    cursor = connect.cursor()
    sql = "DELETE FROM ietls_listening_material_answers WHERE chapter =" + str(chapter)
    cursor.execute(sql)
    connect.commit()
    print('成功删除', cursor.rowcount, '条数据')