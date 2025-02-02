import con_file 
import pandas as pd 
import supporting_update_fooder as update_fooder 
import supporting_update_fooder_style_2 as update_fooder_2
c=con_file.my.cursor()
#create connection object
def add_new_stock():
    category=input("Enter category:- ")
    date_of_purchase=input("Enter date of purchase /default today (yyyy-mm-dd):- ")
    if date_of_purchase=="":
        query_select_curdate="select curdate()"
        c.execute(query_select_curdate)
        fetch_curdate=c.fetchall()
        df_select_curdate=pd.DataFrame(fetch_curdate)
        date_of_purchase=str(df_select_curdate[0][0])
    vendor=input("Enter vendor name:- ")
    while True:
        mode_of_payment=input("""Select mode of payment
        1. Cash
        2. Credit:- """)
        if mode_of_payment=="1":
            mode_of_payment="Cash"
            break
        elif mode_of_payment=="2":
            mode_of_payment="Credit"
            break
        else :
            print("Try agin")
            pass
    stock_bought=input("Enter qty:- ")
    query_select_max_fooder_code=pd.read_sql("select max(f_code) from fooder",con_file.my)
    df=pd.DataFrame(query_select_max_fooder_code)
    try:
        add_fooder_code=int(df[max(df)])+1
    except:
      
        add_fooder_code=1
    query_select_unit="select distinct(unit) from fooder"
    c.execute(query_select_unit)
    data_unit=c.fetchall()
    len_data=len(data_unit)
    dict_units={1: 'kg', 2: 'grams', 3: 'liters', 4: 'piece'}
    
    for count in range(0,len_data):
        if data_unit[count][0] not in dict_units.values() :
            dic_max_key=max(dict_units.keys())
            dict_units[dic_max_key+1]=data_unit[count][0]
    max_key=max(dict_units.keys())
    dict_units[max_key+1]='other'
    Series_units=pd.Series(dict_units)
    print(Series_units)
    
    while True:
        select_unit=input("select one:- ")
        if select_unit=="":
            print("Try again")
            pass
        elif int(select_unit)==max_key+1:
           unit=input("Enter weights standard:- ")
           break     
        elif int(select_unit)<=max_key:
           unit=dict_units[int(select_unit)]
           break
        else:
            print("else Try again")
            pass
    price=input("Enter price:- ") 
    query_enter_data="insert into fooder values("+str(add_fooder_code)+",'"+category+"','"+date_of_purchase+"','"+vendor+"','"+mode_of_payment+"',"+stock_bought+",'"+unit+"',"+price+")"
    c.execute(query_enter_data)
    con_file.my.commit()

def code():
    query_select_fooder="select * from fooder"
    
    data_df=pd.read_sql(query_select_fooder,con_file.my)
    if data_df.empty:
        print("No record found")
    else:
        print("-"*90)
        print(data_df.to_string(index=False))
        print("-"*90)
        
    ask_new_stock=input("""1. Add new stock
2. Update existing stock
3. Back:- """)
    if ask_new_stock=="1":
         add_new_stock()
    elif ask_new_stock=="2":
        query_check_view="select status from settings where number=4"
        c.execute(query_check_view)
        data=c.fetchall()
        on_off=data[0][0]
        if on_off=="off":
            update_fooder.code()
        elif on_off=="on":
          update_fooder_2.code()
