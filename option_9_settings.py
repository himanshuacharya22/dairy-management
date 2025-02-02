import con_file
import pandas as pd

def code():
    c=con_file.my.cursor()
    query_select="select discription,status from settings"
    c.execute(query_select)
    data=c.fetchall()
    df_status=pd.DataFrame(data)
    df_shape=df_status.shape[0]
    print("-"*30)
    print("      --settings--     ")
    for count in range(0,df_shape):
        df_descri=str(df_status[0][count])
        df_on_off=str(df_status[1][count])
        print("")
        print(str(count+1)+". "+df_descri+":- "+df_on_off)
    ask_revolve=input("Enter number to revolve:- ")
    if ask_revolve!="":
        query_select_one="select status from settings where number="+ask_revolve
        c.execute(query_select_one)
        old=c.fetchall()
        old_condition=old[0][0]
        if old_condition=="on" and ask_revolve!="" :
            new_condition="off"
            query_update="update settings set status='{}' where number={}".format(new_condition,ask_revolve)
            c.execute(query_update)
            con_file.my.commit()
        elif old_condition=="off" and ask_revolve!="":
            new_condition="on"
            query_update="update settings set status='{}' where number={}".format(new_condition,ask_revolve)
            c.execute(query_update)
            con_file.my.commit()