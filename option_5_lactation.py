import pandas as pd
import con_file
def code():
    c=con_file.my.cursor()
    query_select_cattle="select cattle_code,name from live_assets where type='Cow'"
    c.execute(query_select_cattle)
    data_cow_id=c.fetchall()
    df_data_cow_id=pd.DataFrame(data_cow_id,columns=["cattle_code","cattle_name"])
    len_df=df_data_cow_id.shape[0]
    li_cattle_code=[]
    for count in range(0,len_df):
        li_cattle_code.append(str(df_data_cow_id['cattle_code'][count]))
    
    query_select_lactation="select * from lactation"
    df=pd.read_sql(query_select_lactation,con_file.my)
    empty_df=df.empty
    if empty_df==False:
        print("--"*30)
        print(df.to_string(index=False))
        print("--"*30)
    else :
        print("No lactation records...")
    ask_add_back=input("""1. Add records 
2. Update records
3. Back
Select one:- """)
    if ask_add_back=="1":
        print("-"*30)
        print(df_data_cow_id.to_string(index=False))
        print("-"*30)
        ci=input('Enter cow_id:- ')
        if ci not in  li_cattle_code:
            print("Not a cow")
        else:
            sql=pd.read_sql("select max(Entry_no) from lactation",con_file.my)
            df=pd.DataFrame(sql)
            try:
                entery_no=int(df[max(df)])+1
            except:
                entery_no=1
            while True:
                lactation_period=input("""Select period
            1. Calving
            2. Early lactation
            3. Mid lactation
            4. late lactation
            5. Dry lactation :-""")
                if lactation_period=="1":
                    lactation_period="Calving"
                    break
                elif lactation_period=="2":
                    lactation_period="Early lactation"
                    break
                elif lactation_period=="3":
                    lactation_period="Mid lactation"
                    break
                elif lactation_period=="4":
                    lactation_period="late lactation"
                    break
                elif lactation_period=="5":
                    lactation_period="late lactation"
                    break
            date_started=input('Enter date started:- ')
            date_stoped=input('Enter date stoped:- ')
            if date_stoped!="":
                query_check_validity="select {}<{}".format(date_started,date_stoped)
                c.execute(query_check_validity)
                data=c.fetchall()[0][0]
                if data==1:
                    insert='insert into lactation values({},{},"{}","{}","{}")' .format(entery_no,ci,date_started,date_stoped,lactation_period)  
                    c.execute(insert)
                    con_file.my.commit()
                else:
                    print("Date stoped can't be smaller then date statred !!")
            elif date_stoped=="":
                date_stoped="null"
                insert='insert into lactation values({},{},"{}",{},"{}")' .format(entery_no,ci,date_started,date_stoped,lactation_period)  
                c.execute(insert)
                con_file.my.commit()
    elif ask_add_back=="2": # update 
      entry_no=input("Enter entry number:-")
      query_selet="select * from Lactation where entry_no={}".format(entry_no)
      data=pd.read_sql(query_selet,con_file.my)
      if data.empty:
          print("Entry no number not found...")
      else:
          select_task=input("""
          1. Cattle code
          2. Date started
          3. Date stoped
          4. Period
Select one:- """)
          if select_task=="1":
            print("-"*30)
            print(df_data_cow_id.to_string(index=False))
            print("-"*30)
            cattle_code=input('Enter cow_id:- ')
            if cattle_code not in  li_cattle_code:
                print("not a cow")
            else:
                query_update_cattle_code="update lactation set cattle_code={} where entry_no={}".format(cattle_code,entry_no)
                c.execute(query_update_cattle_code)
                con_file.my.commit()
          elif select_task=="2":
              date_started=input('Enter date_started:- ')
              query_select_date_stoped="select date_stoped from Lactation where entry_no={}".format(entry_no)
              data=pd.read_sql(query_select_date_stoped)
              date_stoped=data[0][0]
              query_check_validity="select {}<{}".format(date_started,date_stoped)
              c.execute(query_check_validity)
              data=c.fetchall()[0][0]
              if data==1:
                  query_update_date_started="update lactation set date_started='{}' where entry_no={}".format(date_started,entry_no)
                  c.execute(query_update_date_started)
                  con_file.my.commit()
              else:
                 print("Date stoped can't be smaller then date statred !!")
          elif select_task=="3":
              date_ended=input('Enter date_started:- ')
              query_select_date_started="select date_started from Lactation where entry_no={}".format(entry_no)
              data=pd.read_sql(query_select_date_started)
              date_started=data[0][0]
              query_check_validity="select {}<{}".format(date_started,date_stoped)
              c.execute(query_check_validity)
              data=c.fetchall()[0][0]
              if data==1:
                  query_update_date_ended="update lactation set date_started='{}' where entry_no={}".format(date_ended,entry_no)
                  c.execute(query_update_date_ended)
                  con_file.my.commit()
              else:
                 print("Date stoped can't be smaller then date statred !!")

          elif select_task=="4":
               while True:
                    lactation_period=input("""Select period
                1. Calving
                2. Early lactation
                3. Mid lactation
                4. late lactation
                5. Dry lactation :-""")
                    if lactation_period=="1":
                        lactation_period="Calving"
                        break
                    elif lactation_period=="2":
                        lactation_period="Early lactation"
                        break
                    elif lactation_period=="3":
                        lactation_period="Mid lactation"
                        break
                    elif lactation_period=="4":
                        lactation_period="late lactation"
                        break
                    elif lactation_period=="5":
                        lactation_period="late lactation"
                        break
               query_update_date_ended="update lactation set period='{}' where entry_no={}".format(lactation_period,entry_no)
               c.execute(query_update_date_ended)
               con_file.my.commit()