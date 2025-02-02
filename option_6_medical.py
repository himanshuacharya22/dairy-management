import con_file
import pandas as pd
def code():
    c=con_file.my.cursor()
    query_select_cattle="select cattle_code,name from live_assets "
    c.execute(query_select_cattle)
    data_cow_id=c.fetchall()
    df_data_cow_id=pd.DataFrame(data_cow_id,columns=["cattle_code","cattle_name"])
    len_df=df_data_cow_id.shape[0]
    li_cattle_code=[]
    for count in range(0,len_df):
        li_cattle_code.append(str(df_data_cow_id['cattle_code'][count]))
    select_cows="select * from medical"
    c.execute(select_cows)
    data=c.fetchall()
    df=pd.DataFrame(data,columns=["entry_no","Cattle_id"," date_of_checkup"," medical_sickness"])
    if df.empty:
        print("No medical records")
    else:
        print(df.to_string(index=False))
    ask_add_record=input("""Select one 
1. Add record
2. Update record
3. Back:-""")
    if ask_add_record=="1" :
        if df_data_cow_id.empty:
            print("Add a live asset first..")
        else:
            print("-"*30)
            print(df_data_cow_id.to_string(index=False))
            print("-"*30)
            cattle_code=input('Enter cow_id:- ')
            if cattle_code not in  li_cattle_code:
                print("Cattle code not found")
            else:
                sql=pd.read_sql("select max(Entry_no) from medical",con_file.my)
                df=pd.DataFrame(sql)
                try:
                    entry_no=int(df[max(df)])+1
                except:
                    entry_no=1
                date=input('enter date_of_checkup /default today (yyyy-mm-dd):')
                if date=="":
                    q="select curdate()"
                    c.execute(q)
                    data=c.fetchall()
                    date_df=pd.DataFrame(data)
                    date=date_df[0][0]
                query_select_issues="select distinct(issues) from medical"
                c.execute(query_select_issues)
                data_issues=c.fetchall()
                len_issues=len(data_issues)
                dict_issues={1: 'ketosis', 2: 'acidosis', 3:'cattle_heat_stress' , 4: 'respiratory_diseases'}
                index_val=[]
                for count in range(0,len_issues):
                    if data_issues[count][0] not in dict_issues.values() :
                        dic_max_key=max(dict_breed.keys())
                        dict_issues[dic_max_key+1]=data_issues[count][0]
                        index_val.append(dic_max_key+1)
                max_key=max(dict_issues.keys())
                dict_issues[max_key+1]='other'
                Series_issues=pd.Series(dict_issues)
                print(Series_issues)
               
                while True:
                    select_issues=input("select one:- ")
                    if select_issues=="":
                        print("Try again")
                        pass
                    elif int(select_issues)==max_key+1:
                       medical_sicknes=input("Enter issues:- ")
                       break     
                    elif int(select_issues)<=max_key:
                       medical_sicknes=dict_issues[int(select_issues)]
                       break
                    else:
                        print("Try again")
                insert="insert into medical values("+str(entry_no)+","+cattle_code+",'"+str(date)+"','"+medical_sicknes+"')"
                c.execute(insert)
                con_file.my.commit()
    elif ask_add_record=="2":
        entry_no=input("Enter entry no")
        query_select="select * from medical where Entry_no={}".format(entry_no)
        df=pd.read_sql(query_select,con_file.my)
        if df.empty:
            print("Record not found..")
        else:
            select_update=input("""Select one
1. Cattle id
2. Date of checkup
3. Medical sickness:- """)
            if select_update=="1":
                print("-"*30)
                print(df_data_cow_id.to_string(index=False))
                print("-"*30)
                cattle_code=input('Enter cow_id:- ')
                if cattle_code not in  li_cattle_code:
                    print("Cattle code not found")
                else:
                    query_update_id="update medical set cattle_code='{}' where Entry_no={}".format(cattle_code,entry_no)
                    c.execute(query_update_id)
                    con_file.my.commit()
            elif select_update=="2":
                date=input('enter date_of_checkup /default today (yyyy-mm-dd):')
                if date=="":
                    q="select curdate()"
                    c.execute(q)
                    data=c.fetchall()
                    date_df=pd.DataFrame(data)
                    date=date_df[0][0]
                query_update_date="update medical set date_of_checkup='{}' where Entry_no={}".format(date,entry_no)
                c.execute(query_update_date)
                con_file.my.commit()
            elif select_update=="3":
                query_select_issues="select distinct(issues) from medical"
                c.execute(query_select_issues)
                data_issues=c.fetchall()
                len_issues=len(data_issues)
                dict_issues={1: 'ketosis', 2: 'acidosis', 3:'cattle heat stress' , 4: 'respiratory diseases'}
                index_val=[]
                for count in range(0,len_issues):
                    count1=count
                    if data_issues[count][0] not in dict_issues.values() :
                        dic_max_key=max(dict_issues.keys())
                        dict_issues[dic_max_key+1]=data_issues[count][0]
                        index_val.append(dic_max_key+1)
                max_key=max(dict_issues.keys())
                dict_issues[max_key+1]='other'
                Series_issues=pd.Series(dict_issues.values(),index=dict_issues.keys())
                print(Series_issues)
               
                while True:
                    select_issues=input("select one:- ")
                    if select_issues=="":
                        print("Try again")
                        pass
                    elif int(select_issues)==max_key+1:
                       medical_sicknes=input("Enter issues:- ")
                       break     
                    elif int(select_issues)<=max_key:
                       medical_sicknes=dict_issues[int(select_issues)]
                       break
                    else:
                        print("Try again")
                query_update_issues="update medical set issues='{}' where Entry_no={}".format(medical_sicknes,entry_no)
                c.execute(query_update_issues)
                con_file.my.commit()
            