#!/usr/bin/python

import sqlite3 as db
conn = db.connect('thedb.sqlite')
cur = conn.cursor()

html_output={}
html_output['family_html'] = "<b>{0} Family:</b> "
html_output['footer'] = "</body></html>"

file = open('html_build/header.html','r')
html_output['header'] = file.read()
file.close()

file = open('html_build/show_form_stats.html','r')
html_output['form_html'] = file.read()
file.close()

file = open('html_build/move_detail.html','r')
html_output['move detail'] = file.read()
file.close()

file = open('html_build/move_list.html','r')
html_output['move list'] = file.read()
file.close()


def html_forms():
    print "<h1>Forms</h1>"
    sql = """select * from Forms order by Name"""
    cur.execute( sql )
    forms = cur.fetchall()
    for form in forms:
        print html_output['form_html'].format(
            name = form[0],
            nextform = form[1],
            method = form[2],
            type1 = form[3],
            type2 = form[4],
            hp = form[5],
            atk = form[6],
            defn = form[7],
            satk = form[8],
            sdef = form[9],
            spd = form[10])
        html_learnable_moves(form[0])

def html_form_in_family(kind):
    sql = """select * from Forms where Name is '{0}'"""
    cur.execute( sql.format(kind) )
    form = cur.fetchone()
    print form_html.format(form[0], form[1], form[2], form[3], form[4], form[5], form[6], form[7])

def html_families():
    cur.execute("select distinct name from Families order by name")
    families = cur.fetchall()
    for family in families:
        print html_output['family_html'].format(family[0])
        cur.execute("select Form from Families where Name is '{0}'".format(family[0]))
        forms = cur.fetchall()
        for form in forms:
            html_form_in_family(form[0])

def html_list_families():
    print "<h1>Families</h1>"
    cur.execute("select distinct name from Families order by name")
    families = cur.fetchall()
    print "<table>"
    for family in families:
        cur.execute("select Form from Families where Name is '{0}'".format(family[0]))
        forms = cur.fetchall()
        print "<tr><td><b>{0}:</b></td>".format(family[0])
        for form in forms:
            print "<td><a href='#{0}'>{0}</a></td>".format(form[0])
        print "</tr>"
    print "</table>"


def html_list_moves():
    cur.execute("select * from Moves order by name")
    moves = cur.fetchall()
    for move in moves:
        print html_output['move detail'].format(move[0], move[1], move[2], move[3],
                                        move[4], move[5], move[6])

def html_learnable_moves(form):
    cur.execute("select move, method from LearnableMoves where Form is \"{0}\"".format(form))
    moves = cur.fetchall()
    for move in moves:
        print html_output['move list'].format(move[0], move[1])

def print_html_output():
    print html_output['header']
    html_forms()
    html_list_families()
    html_list_moves()
    print html_output['footer']

def main():
    print_html_output()

if __name__ == '__main__':
    main()
