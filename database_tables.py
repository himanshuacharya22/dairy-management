import mysql.connector as sqltor
def code():
    my=sqltor.connect(host='localhost',
    user='root',password='1234')
    c=my.cursor()
    query_1="create database if not exists dairy_management"
    c.execute(query_1)
    query_2="use dairy_management"
    c.execute(query_2)
    query_3="create table if not exists fooder (f_code int primary key,name char(30),purchase_on date,vendor char(20),mode_of_payment char(6),stock_avi int,unit char(20),price int)"
    c.execute(query_3)
    query_4="create table if not exists live_assets (cattle_code int primary key,name char(20),breed char(20),date_of_purchase date,type char(20))"
    c.execute(query_4)
    query_5="create table if not exists products(product_code int primary key,product_name char(50) unique,price int,qty_avialable int,weights_standard char(20))"
    c.execute(query_5)
    query_6='create table if not exists sales_record(Entry_no int primary key,customer_id int ,customer_name char(20),DOS date,product_code int,qty_purchased int,amount int,foreign key(product_code) references products(product_code))'
    c.execute(query_6)
    query_7="create table if not exists medical(Entry_no int primary key,cattle_code int,date_of_checkup date,issues char(50),foreign key(cattle_code) references live_assets(cattle_code))"
    c.execute(query_7)
    query_8="create table if not exists lactation(Entry_no int primary key,cattle_code int,date_started date,date_stoped date,period char(20),foreign key(cattle_code) references live_assets(cattle_code))"
    c.execute(query_8)
    query_9="create table if not exists settings (number int primary key,discription char(90) unique,status char(3))"
    c.execute(query_9)
    query_10="insert ignore  into settings  values(1,'Classified view in live stock menu','off')"
    c.execute(query_10)
    query_11='insert ignore into settings values(2,"Adjust fooder code","on")'
    c.execute(query_11)
    query_12='insert ignore into settings values(3,"Adjust customer_id","on")'
    c.execute(query_12)
    query_12='insert ignore into settings values(4,"Selective update fooder","on")'
    c.execute(query_12)
    my.commit()
