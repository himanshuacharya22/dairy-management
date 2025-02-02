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
        print("        "+"_"*20+"""
        |1.Fooder name      |
        |2.Purchase date    |
        |3.Vendor           |
        |4.Mode of payment  |
        |5.Stock avialable  |
        |6.Unit             |
        |7.Price            |
        |8.Delete record    |
        |"""+"_"*19+"|")
        select_item=input("Select one:-")
        if select_item=="1":
            f_name_update=input("Enter name:- ")
            query_update_name="update fooder set name='{}' where f_code={}".format(f_name_update,f_code_update)
            c.execute(query_update_name)
            con_file.my.commit()
        elif select_item=="2":
            while True:
                dop_update=input("""Enter date of purchase
                        1.Today
                        2.Add new 
                        choose one:- """)
                if dop_update=="1": #today
                    query_select_curdate="select curdate()"
                    c.execute(query_select_curdate)
                    fetch_curdate=c.fetchall()
                    df_select_curdate=pd.DataFrame(fetch_curdate)
                    dop_update=str(df_select_curdate[0][0])  
                    break
                elif dop_update=="2": #custom
                    dop_update=input("Enter date of purchase (yyyy-mm-dd):-")
                    break
                else:
                    print("Try again")
                    pass
            query_update_name="update fooder set purchase_on='{}' where f_code={}".format(dop_update,f_code_update)
            c.execute(query_update_name)
            con_file.my.commit()
        elif select_item=="3":
            vendor_update=input("Enter vendor:- ")
            query_update_vendor="update fooder set vendor='{}' where f_code={}".format(vendor_update,f_code_update)
            c.execute(query_update_vendor)
            con_file.my.commit()
        elif select_item=="4":
            while True:
                mode_of_payment=input("""Mode of payment
                        1. Cash
                        2. Credit:- """)
                if mode_of_payment=="1":
                        mode_of_payment="Cash"
                        break
                elif mode_of_payment=="2":
                        mode_of_payment="Credit"
                        break
                else:
                    pass
            query_update_mode_of_payment="update fooder set  mode_of_payment='{}' where f_code={}".format(mode_of_payment,f_code_update)
            c.execute(query_update_mode_of_payment)
            con_file.my.commit()
        elif select_item=="5":
            qty_avialable_update=input("Enter qty avialable:- ")
            query_update_stock="update fooder set  stock_avi={} where f_code={}".format(qty_avialable_update,f_code_update)
            c.execute(query_update_stock)
            con_file.my.commit()
        elif select_item=="6":
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
            print('max_key:-',max_key)
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
            query_update_unit="update fooder set  unit='{}' where f_code={}".format(weights_standard,f_code_update)
            c.execute(query_update_unit)
            con_file.my.commit()
        elif select_item=="7":
            price_update=input("Enter price:- ")
            query_update_price="update fooder set  price='{}' where f_code={}".format(price_update,f_code_update)
            c.execute(query_update_price)
            con_file.my.commit()
        elif select_item=="8":
            query_delete_record="delete from  fooder where f_code={}".format(f_code_update)
            c.execute(query_delete_record)
            con_file.my.commit()
            query_check_view="select status from settings where number=2"
            c.execute(query_check_view)
            data=c.fetchall()
            on_off=data[0][0]
            if on_off=="on":
                adjust_f_code.code("fooder","f_code")
            