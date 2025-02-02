import con_file
import supporting_adjust_primary_key as adjust_f_code
import pandas as pd
def code():
    c=con_file.my.cursor()
    
    f_code_update=input("Enter fooder code:- ")
    query_select="select * from fooder where f_code="+f_code_update
    df=pd.read_sql(query_select,con_file.my)
    if df.empty:
        print("fooder code not fount")
    else:
        f_name_update=input("Enter name/default old :- ")
        if  f_name_update=="00":
                query_delete="delete from fooder where f_code={}".format(f_code_update)
                c.execute(query_delete)
                con_file.my.commit()
                query_check_view="select status from settings where number=2"
                c.execute(query_check_view)
                data=c.fetchall()
                on_off=data[0][0]
                if on_off=="on":
                    adjust_f_code.code("fooder","f_code")
                
        else:
            price_update=input("Enter price/default old:- ")
            qty_avialable_update=input("Enter qty avialable/default old:- ")
            vendor_update=input("Enter vendor/default old:- ")
            while True:
                mode_of_payment=input("""Mode of payment
                    1. Cash
                    2. Credit
                    3. Old:- """)
                if mode_of_payment=="1":
                    mode_of_payment="Cash"
                    break
                elif mode_of_payment=="2":
                    mode_of_payment="Credit"
                    break
                elif mode_of_payment=="3":
                    query_select_mode_of_payment="select mode_of_payment from fooder where f_code="+f_code_update
                    c.execute(query_select_mode_of_payment)
                    fooder_mode_of_payment=c.fetchall()
                    df_fooder_mode_of_payment_sql=pd.DataFrame(fooder_mode_of_payment)
                    print(df_fooder_mode_of_payment_sql)
                    mode_of_payment=df_fooder_mode_of_payment_sql[0][0]
                    break
                else:
                    pass
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
               weights_standard=input("Enter weights standard:- ")
               break     
            elif int(select_unit)<=max_key:
               weights_standard=dict_units[int(select_unit)]
               break
            else:
                print("Try again")
                pass
            
        
        if qty_avialable_update=="":
              query_select_qty_avialable="select stock_avi from fooder where f_code="+f_code_update
              c.execute(query_select_qty_avialable)
              fooder_qty_avialable_sql=c.fetchall()
              df_fooder_qty_avialable_sql=pd.DataFrame(fooder_qty_avialable_sql)
              qty_avialable_update=df_fooder_qty_avialable_sql[0][0]     
           
        if f_name_update=="":
              query_select_name="select name from fooder where f_code="+f_code_update
              c.execute(query_select_name)
              f_name_sql=c.fetchall()
              df_f_name_sql=pd.DataFrame(f_name_sql)
              f_name_update=df_f_name_sql[0][0]
        if price_update=="":
            query_select_price="select price from fooder where f_code="+f_code_update
            c.execute(query_select_price)
            price_sql=c.fetchall()
            price_update=price_sql[0][0]
        while True:
            dop_update=input("""Enter date of purchase
            1.Old
            2.Today
            3.Add new 
            choose one:- """)
            if dop_update=="1": #old
                query_select_dop="select purchase_on from fooder where f_code="+f_code_update
                c.execute(query_select_dop)
                dop_sql=c.fetchall()
                dop_update=dop_sql[0][0]   
                break
            elif dop_update=="2": #today
                query_select_curdate="select curdate()"
                c.execute(query_select_curdate)
                fetch_curdate=c.fetchall()
                df_select_curdate=pd.DataFrame(fetch_curdate)
                dop_update=str(df_select_curdate[0][0])  
                break
            elif dop_update=="3": #custom
                dop_update=input("Enter date of purchase (yyyy-mm-dd):-")
                break
            else:
                print("Try again")
                pass
            
        if vendor_update=="":
            query_select_vendor="select vendor from fooder where f_code="+f_code_update
            c.execute(query_select_vendor)
            vendor_sql=c.fetchall()
            vendor_update=vendor_sql[0][0]
        query_update_product="update fooder set name='{}',price={},purchase_on='{}',vendor='{}',mode_of_payment='{}',stock_avi={},unit='{}' where f_code={}".format(f_name_update,price_update,dop_update,vendor_update,mode_of_payment,qty_avialable_update,weights_standard,f_code_update)
        c.execute(query_update_product)
        con_file.my.commit()
        print("Record updated sussesfully...")
    