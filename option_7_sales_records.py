import con_file
import pandas as pd
import matplotlib.pyplot as pl
def code():
    c=con_file.my.cursor()
    query_select_sales="select Entry_no,DOS,product_code,qty_purchased from sales_record"
    sales=pd.read_sql(query_select_sales,con_file.my)
    print(sales)
    show_graph=input("""show graphical representation on the Daily basis  :-""")
    li_sales_per_day=[]
    li_dates=[]
    query_select_date="select distinct(dos) from sales_record"
    c.execute(query_select_date)
    data=c.fetchall()
    df_data=pd.DataFrame(data)
    len_df=df_data.shape[0]
    for a in range(0,len_df):
        dates=str(df_data[0][a])
        li_dates.append(dates)    
        query_select_sales="select sum(qty_purchased) from sales_record where dos='{}'".format(dates)
        c.execute(query_select_sales)
        data_sum=c.fetchall()
        sums=int(data_sum[0][0])
        li_sales_per_day.append(sums)
    pl.plot(li_dates,li_sales_per_day)
    pl.show()
    