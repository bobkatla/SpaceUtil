import psycopg2 as pg
from connect import config

def run_cmd(cmd):
    conn = None
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
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, pg.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    comm = '''CREATE TABLE test (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    )
    '''
    run_cmd(comm)