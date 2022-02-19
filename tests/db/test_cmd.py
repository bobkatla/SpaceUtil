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
        check = []
        if isinstance(cmd, list) or isinstance(cmd, tuple):
            for command in cmd:
                cur.execute(command)
                check.append(cur.fetchone())
        else:
            cur.execute(cmd)
            check = cur.fetchone()
        re_val = check
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, pg.DatabaseError) as error:
        print("ERROR")
        return error
    finally:
        if conn is not None:
            conn.close()
    return re_val

if __name__ == "__main__":
    comm = [
    "SELECT version()", "select * from test"]
    check = run_cmd(comm)
    print(check)