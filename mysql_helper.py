from tkinter import ttk
from window import *

import mycon

# import sqlite3 as sql
# mycon=sql.connect('dairy_management_android')
c = mycon.my.cursor()


def get_tables():
    c.execute(
        "create table if not exists fooder (f_code int primary key,name char(30),purchase_on date,vendor char(20),"
        "mode_of_payment char(30),stock_avi int,unit char(30),price int)")

    c.execute(
        "create table if not exists live_assets (cattle_code int primary key,name char(30),breed char(30),"
        "date_of_purchase char(30),type char(30))")

    c.execute(
        "create table if not exists products(product_code int primary key,product_name char(30) unique,price int,"
        "qty_available int,weights_standard char(30))")

    c.execute(
        'create table if not exists sales_record(Entry_no int primary key,customer_name char(30),DOS char(30),'
        'product_code int,product_name char(30),qty_purchased int,amount int,foreign key(product_code) references '
        'products(product_code))')

    c.execute(
        "create table if not exists medical(Entry_no int primary key,cattle_code int,date_of_checkup char(30),"
        "issues char(30),foreign key(cattle_code) references live_assets(cattle_code))")

    c.execute(
        "create table if not exists lactation(Entry_no int primary key,cattle_code int,date_started char(30),"
        "date_stopped char(30),period char(30),foreign key(cattle_code) references live_assets(cattle_code))")

    c.execute("create table if not exists settings (number int primary key,description char(90) unique,status char(3))")

    c.execute("insert  ignore  into settings  values(1,'Classified view in live stock menu','off')")

    c.execute('insert  ignore into settings values(2,"Adjust fooder code","on")')

    c.execute('insert  ignore into settings values(3,"Adjust customer_id","on")')

    c.execute('insert ignore into settings values(4,"Selective update fooder","on")')
    mycon.my.commit()


get_tables()

get_tables()


def select_table(columns='', table_name=''):
    c.execute("select {} from {}".format(columns, table_name))
    return c.fetchall()


def create_list(columns=None, frame="", rows="", column_width=None):
    if column_width is None:
        column_width = []
    if columns is None:
        columns = []
    number_column = ()
    for a in range(1, len(columns) + 1):
        number_column += (a,)
    tree_view = ttk.Treeview(frame, columns=number_column, show="headings")
    increment = 1
    a = 0
    for w in column_width:
        a += 1
        tree_view.column(a, width=w)
    for column in columns:
        tree_view.heading(increment, text=column)
        increment += 1
    for i in rows:
        tree_view.insert("", 'end', values=i)
    return tree_view


def get_primary_key(primary_col="", table=""):
    try:
        c.execute("select max({}) from {}".format(primary_col, table))
        return c.fetchone()[0] + 1
    except:
        return 1


def get_date():
    c.execute("select curdate()")
    return c.fetchone()[0]


def delete(table="", column="", code=""):
    c.execute("delete from {} where {}={}".format(table, column, code))
    mycon.my.commit()


def get_distinct_optionMenu(frame="", table="", column="", com="", cord=None, new=None):
    if new is None:
        new = []
    if cord is None:
        cord = []
    c.execute("select distinct {} from {}".format(column, table))
    x = c.fetchall()
    items = []
    var = StringVar()
    for data in x:
        items.append(data[0])
    for new_items in new:
        if new_items not in items:
            items.append(new_items)
    try:
        var.set(items[-1])
        OptionMenu(frame, var, *items, command=com).place(x=cord[0], y=cord[1])
    except:
        pass
    return var
# get_distinct_optionMenu(win,"sales_record","customer_name").pack()
# win.mainloop()
