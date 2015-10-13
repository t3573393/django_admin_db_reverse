#coding:utf8
from db_reverse.dbpool import dbpool
from MySQLdb.cursors import DictCursor


def get_db_all_info():
    result = {}
    tables = get_all_table()
    for a_table in tables:
        table_name = a_table['TABLE_NAME']
        columns = get_all_column_by_table_name(table_name)
        constraints = get_table_constraints(table_name)
        result[table_name] = {
            'comment': a_table['TABLE_COMMENT'],
            'columns': columns,
            'constraints': constraints
        }
    return result


def get_all_table():
    conn = dbpool.connection()
    sqlstr = '''
    SELECT
      TABLE_NAME, TABLE_COMMENT
    FROM
        information_schema.TABLES
    WHERE
        TABLE_SCHEMA = DATABASE()
            and Table_type = 'BASE TABLE'
    '''
    cursor = conn.cursor(cursorclass=DictCursor)
    cursor.execute(sqlstr)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
    # return [result[0]]


def get_all_column_by_table_name(table_name):
    conn = dbpool.connection()
    sqlstr = """SELECT  `COLUMN_NAME` ,`DATA_TYPE` , `COLUMN_TYPE`,
    CHARACTER_MAXIMUM_LENGTH, NUMERIC_PRECISION, NUMERIC_SCALE, COLUMN_COMMENT, IS_NULLABLE
    FROM information_schema.`COLUMNS`
    where TABLE_SCHEMA= DATABASE() AND TABLE_NAME = '%s' """ % table_name
    cursor = conn.cursor(cursorclass=DictCursor)
    cursor.execute(sqlstr)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def get_table_constraints(table_name):
    sql = """SELECT k.COLUMN_NAME, t.CONSTRAINT_TYPE, t.CONSTRAINT_NAME
                FROM information_schema.table_constraints t
                JOIN information_schema.key_column_usage k
                USING ( constraint_name, table_schema, table_name )
                WHERE t.table_schema =  DATABASE()
                AND t.table_name =  '%s'
        """ % table_name
    conn = dbpool.connection()
    cursor = conn.cursor(cursorclass=DictCursor)
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

