import con_file 
import pandas as pd
import matplotlib.pyplot as pl
def code():
    c=con_file.my.cursor()
    ask_type=input("""select type
    1. Cows
    2. Bulls
    3. calves""")
    while ask_type not in ['1','2','3']:
        print("select a valid choice")
        ask_type=input("""select type
1. Cows
2. Bulls
3. calves""")
    if ask_type=="1":
        ask_type="Cow"
    elif ask_type=="2":
        ask_type="Bulls"
    elif ask_type=="3":
        ask_type="Calves"
    query_select_cattle="select cattle_code,name,breed,date_of_purchase from live_assets where type='{}'".format(ask_type)
    data_df=pd.read_sql(query_select_cattle,con_file.my)
    if data_df.empty:
        print("No records")
    else:
        print("-"*50)
        print(data_df.to_string(index=False))
        print("-"*50)
    
    
    ask_new_or_existing=input("""1. Add new stock
2. change existing stock
3. Delete Record
4. Analyze live stock
5. Back
Choose one:- """)
    if ask_new_or_existing=="1"  :#Add new stock
             name_new_entry=input("Enter name:- ")
             query_select_breed="select distinct(breed) from live_assets"
             c.execute(query_select_breed)
             data_breed=c.fetchall()
             len_breed=len(data_breed)
             dict_breed={1: 'rathi', 2: 'Shaiwal', 3:'american' , 4: 'jersey'}
             index_val=[]
             for count in range(0,len_breed):
                 count1=count
                 if data_breed[count][0] not in dict_breed.values() :
                     dic_max_key=max(dict_breed.keys())
                     dict_breed[dic_max_key+1]=data_breed[count][0]
                     index_val.append(dic_max_key+1)
             max_key=max(dict_breed.keys())
             dict_breed[max_key+1]='other'
             Series_breed=pd.Series(dict_breed.values(),index=dict_breed.keys())
             print(Series_breed)
            
             while True:
                 select_breed=input("select one:- ")
                 if select_breed=="":
                     print("Try again")
                     pass
                 elif int(select_breed)==max_key+1:
                    breed_new_entry=input("Enter breed:- ")
                    break     
                 elif int(select_breed)<=max_key:
                    breed_new_entry=dict_breed[int(select_breed)]
                    break
                 else:
                     print("Try again")
             date_of_purchase=input("Enter date of purchase/default today (yyyy-mm-dd):- ")

             if date_of_purchase=="":
                query_select_curdate="select curdate()"
                c.execute(query_select_curdate)
                fetch_curdate=c.fetchall()
                df_select_curdate=pd.DataFrame(fetch_curdate)
                date_of_purchase=str(df_select_curdate[0][0])
             query_select_max_cattle_code=pd.read_sql("select max(cattle_code) from live_assets",con_file.my)
             df=pd.DataFrame(query_select_max_cattle_code)
             try:
                 add_cattle_code=int(df[max(df)])+1
             except:
                 add_cattle_code=1000
             query_insert_live_assets="insert into live_assets values({},'{}','{}','{}' ,'{}')".format(add_cattle_code,name_new_entry,breed_new_entry,date_of_purchase,ask_type)
             c.execute(query_insert_live_assets)
             con_file.my.commit()
            
    elif ask_new_or_existing=="2":#change existing stock
           cattle_code=input("Enter cattle code:- ")
           query_check_record="select * from live_assets where cattle_code={}".format(cattle_code)
           c.execute(query_check_record)
           data=c.fetchall()
           len_data=len(data)
           if  len_data>0:
               name_update=input("Enter name/default old  :- ")
               query_select_breed="select distinct(breed) from live_assets"
               c.execute(query_select_breed)
               data_breed=c.fetchall()
               len_breed=len(data_breed)
               dict_breed={1: 'rathi', 2: 'Shaiwal', 3:'american' , 4: 'jersey'}
               index_val=[]
               for count in range(0,len_breed):
                   if data_breed[count][0] not in dict_breed.values() :
                       dic_max_key=max(dict_breed.keys())
                       dict_breed[dic_max_key+1]=data_breed[count][0]
                       index_val.append(dic_max_key+1)
               max_key=max(dict_breed.keys())
               dict_breed[max_key+1]='other'
               Series_breed=pd.Series(dict_breed.values(),index=dict_breed.keys())
               print(Series_breed)
               
               while True:
                   select_breed=input("select one:- ")
                   if select_breed=="":
                       print("Try again")
                       pass
                   elif int(select_breed)==max_key+1:
                      breed_update=input("Enter breed:- ")
                      break     
                   elif int(select_breed)<=max_key:
                      breed_update=dict_breed[int(select_breed)]
                      break
                   else:
                       print("Try again")
               date_of_purchase_update=input("""Enter date of purchase(yyyy-mm-dd)
                                      1.old
                                      2.today
                                      3.add new 
                                      choose one:- """)
               
               if date_of_purchase_update=="1":
                   query_select_name="select date_of_purchase from live_assets where cattle_code="+cattle_code
                   c.execute(query_select_name)
                   purchase_date_sql=c.fetchall()              
                   df_purchase_date_sql=pd.DataFrame(purchase_date_sql)
                   date_of_purchase= df_purchase_date_sql[0][0]
               elif date_of_purchase_update=="2":
                   query_select_curdate="select curdate()"
                   c.execute(query_select_curdate)
                   fetch_curdate=c.fetchall()
                   df_select_curdate=pd.DataFrame(fetch_curdate)
                   date_of_purchase=str(df_select_curdate[0][0])
               elif date_of_purchase_update=="3":
                   date_of_purchase=input("Enter date of purchase(yyyy-mm-dd) :- ")
               if name_update=="":
                    query_select_name="select name from live_assets where cattle_code="+cattle_code
                    c.execute(query_select_name)
                    cattle_name_sql=c.fetchall()
                    df_cattle_name_sql=pd.DataFrame(cattle_name_sql)
                    name_update=df_cattle_name_sql[0][0]
               query_update_entry="update live_assets set name='"+name_update+"',breed='"+breed_update+"',date_of_purchase='"+str(date_of_purchase)+"' where cattle_code="+cattle_code
               c.execute(query_update_entry)
               con_file.my.commit()
           else:
            print("Cattle code not found..")
    elif ask_new_or_existing=="3": #Delete record
        cattle_code=input("Enter cattle code:- ")
        query_check_record="select * from live_assets where cattle_code={}".format(cattle_code)
        c.execute(query_check_record)
        data=c.fetchall()
        len_data=len(data)
        if  len_data>0:
            query_delete_record="delete from live_assets where cattle_code={}".format(cattle_code)
            c.execute(query_delete_record)
            con_file.my.commit()
        else:
            print("cattle code not found..")
    elif ask_new_or_existing=="4":# graph
            ask_graph=input("""1. Number of cattle
2. Combination of cattle:- """)
            select_cow="select count(cattle_code) from live_assets where type='cow' "
            c.execute(select_cow)
            data=c.fetchall()
            df_data=pd.DataFrame(data)
            cows_number=df_data[0][0]
            
            select_bulls="select count(cattle_code) from live_assets where type='bulls' "
            c.execute(select_bulls)
            data=c.fetchall()
            df_data=pd.DataFrame(data)
            bulls_number=df_data[0][0]
            
            select_calves="select count(cattle_code) from live_assets where type='calves' "
            c.execute(select_calves)
            data=c.fetchall()
            df_data=pd.DataFrame(data)
            calves_number=df_data[0][0]
            data_type=['cows','bulls','calves']
            data_numbes=[cows_number,bulls_number,calves_number]
            if ask_graph=="1":
                pl.bar(data_type,data_numbes,width=[0.2,0.2,0.2])
                pl.xlabel("Number of cattle")
                pl.ylabel("Type of cattle")
                pl.show()
            elif ask_graph=="2":
                pl.pie(data_numbes,labels=data_type)
                pl.legend()
                pl.show()
