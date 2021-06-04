def rows_to_dict(cursor):
    hasil = None
    columns = [i[0].lower() for i in cursor.description]
    for row in cursor:
        hasil = dict(zip(columns, row))
    return hasil

def rows_to_dict_list(cursor):
    hasil = None
    columns = [i[0].lower() for i in cursor.description]
    for row in cursor:
        hasil = [dict(zip(columns, row))]
    return hasil

def responseJSON(flag, message, result):
    resp = {}
    resp['flag'] = flag
    resp['message'] = message
    resp['result'] = result
    return resp