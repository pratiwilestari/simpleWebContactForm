from swcf import dbConnect
from swcf.others.format import responseJSON, rows_to_dict, rows_to_dict_list

def selectOne():
    conn = dbConnect()
    try:
        cursor = conn.cursor()
        query = '''SELECT 1 '''
        cursor.execute(query, )
        data = rows_to_dict(cursor)
        return responseJSON('T', 'sukses select', data) 
    except Exception as err:
        return responseJSON('F', str(err), data)
    finally:
        if(conn):
            conn.close()

def insertPost(name, email, issue, content):
    conn = dbConnect()
    try:
        cursor = conn.cursor()
        query = '''INSERT INTO post VALUES(
                        SELECT COALESCE(MAX(id), 1) FROM post,
                        %s, %s, %s, %s); '''
        cursor.execute(query, (name, email, issue, content, ))
        data = rows_to_dict(cursor)
        return responseJSON('T', 'sukses select', None) 
    except Exception as err:
        return responseJSON('F', str(err), None)
    finally:
        if(conn):
            conn.close()