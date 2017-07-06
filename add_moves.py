#!/usr/bin/python

import sqlite3 as db
conn = db.connect('thedb.sqlite')
cur = conn.cursor()

add_move_sql = """
    insert into LearnableMoves
    values ("{0}", "{1}", "{2}")
    ;
"""

adding_moves = True
form = raw_input("Form:")
move = raw_input("Move:")
method = raw_input("Method:")
if move == "" or method == "":
    adding_moves = False

while adding_moves:
    cur.execute(add_move_sql.format(form, move, method))
    conn.commit()
    move = raw_input("Move:")
    method = raw_input("Method:")
    if move == "" or method == "":
        adding_moves = False
