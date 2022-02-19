import psycopg2 as pg
from connect import config

def run_cmd(cmd):
    conn = None
    re_val = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = pg.connect(**params)
        cur = conn.cursor()
        # create table one by one
        if isinstance(cmd, list) or isinstance(cmd, tuple):
            for command in cmd:
                cur.execute(command)
        else:
            cur.execute(cmd)
        re_val = cur.fetchone()
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, pg.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return re_val

if __name__ == "__main__":
    comm = ''' 
    '''
    check = run_cmd(comm)
    print(check)