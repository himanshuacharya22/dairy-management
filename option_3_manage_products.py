import con_file
import pandas as pd
def code():
    c=con_file.my.cursor()
    
    query_select_fooder="select * from products"
    fixed_assets_data=pd.read_sql(query_select_fooder,con_file.my)
    if fixed_assets_data.empty:
        print("record not found..")
    else:
        print("-"*80)
        print(fixed_assets_data.to_string(index=False))
        print("-"*80)
    
    ask_edit_products=input("""1. Add new stock
2. Change existing record
3. Delete
4. Back:-""")
    if ask_edit_products=="1" : #Add new stock
        name=input("Enter name of product:- ")
        price=input("Enter price of product:- ")
        qty_avialable=input("Enter quantity avialable:- ")
        
        sql=pd.read_sql("select max(product_code) from products",con_file.my)
        df=pd.DataFrame(sql)
        try:
            add_product_code=int(df[max(df)])+1
        except:
            add_product_code=1
            
        query_select_unit="select distinct(weights_standard) from products"
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
                print("Try again")
                pass
        
        
        
        quary_add_products="insert into products values({},'{}',{},{},'{}')".format(add_product_code,name,price,qty_avialable,unit)
        c.execute(quary_add_products)
        con_file.my.commit()
    elif ask_edit_products=="2": #Change existing record
        product_code=input("Enter product code:- ")
        query_select="select * from products where product_code={}".format(product_code)
        data=pd.read_sql(query_select,con_file.my)
        if data.empty:
            print("Product code not found...")
        else:
                   
            name_update=input("Enter name/default old :- ")
            price_update=input("Enter price/default old:- ")
            query_select_unit="select distinct(weights_standard) from products"
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
                    print("Try again")
                    pass
            qty_avialable_update=input("Enter qty avialable/default old:- ")
            if qty_avialable_update=="":
                 query_select_qty_avialable="select qty_avialable from products where product_code="+product_code
                 c.execute(query_select_qty_avialable)
                 product_qty_avialable_sql=c.fetchall()
                 df_product_qty_avialable_sql=pd.DataFrame(product_qty_avialable_sql)
                 qty_avialable_update=df_product_qty_avialable_sql[0][0]     
           
            if name_update=="":
                 query_select_name="select product_name from products where product_code="+product_code
                 c.execute(query_select_name)
                 product_name_sql=c.fetchall()
                 df_product_name_sql=pd.DataFrame(product_name_sql)
                 name_update=df_product_name_sql[0][0]
            if price_update=="":
               query_select_price="select price from products where product_code="+product_code
               c.execute(query_select_price)
               price_sql=c.fetchall()
               price_update=price_sql[0][0]
             
            query_update_product="update products set product_name='{}',price={},qty_avialable={},weights_standard='{}'where product_code={}".format(name_update,price_update,qty_avialable_update,unit,product_code)
            c.execute(query_update_product)
            con_file.my.commit()
    elif ask_edit_products=="3":# delete
        product_code=input("Enter product code:- ")
        query_select="select * from products where product_code={}".format(product_code)
        data=pd.read_sql(query_select,con_file.my)
        if data.empty:
            print("Product code not found...")
        else:
            query_delete="delete from products where product_code={}".format(product_code)
            c.execute(query_delete)
            con_file.my.commit()
        
