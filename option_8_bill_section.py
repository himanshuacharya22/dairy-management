import con_file
import pandas as pd
import supporting_adjust_primary_key as adjust_customer_id  
def code(): 
    c=con_file.my.cursor()
    select_customer="select distinct(customer_id),customer_name from sales_record"
    execute_select_customer=pd.read_sql(select_customer,con_file.my)
    print("-"*40)
    print(execute_select_customer.to_string(index=False))
    print("-"*40)
    
    customer_name=input("Enter customer name or ID (default walk-in):- ")
    if customer_name=="":
        customer_name="WalkIn"
    if customer_name.isnumeric()  :
        where_clause_customer="customer_id"
    elif customer_name.isalpha():
        where_clause_customer="customer_name"
    
    li_product_code=[]
    li_product_name=[]
    query_select_date="select product_code from sales_record where {}='{}'".format(where_clause_customer,customer_name)
    c.execute(query_select_date)
    data=c.fetchall()
    df_data=pd.DataFrame(data)
    len_df=df_data.shape[0]
    for count in range(0,len_df):
        code=str(df_data[0][count])
        li_product_code.append(code)    
        query_select_sales="select product_name from products where product_code='{}'".format(code)
        c.execute(query_select_sales)
        data_name=c.fetchall()
        df_name=pd.DataFrame(data_name)
        name=str(df_name[0][0])
        li_product_name.append(name)
    li_dos=[]
    for count in range(0,len_df):
        code=str(df_data[0][count])
        li_product_code.append(code)    
        query_select_dos="select dos from sales_record where {}='{}'".format(where_clause_customer,customer_name)
        c.execute(query_select_dos)
        data_dos=c.fetchall()
        df_dos=pd.DataFrame(data_dos)
        dos=str(df_dos[0][count])
        li_dos.append(dos)
    li_price=[]
    for count in range(0,len_df):
        code=str(df_data[0][count])
        # li_product_code.append(code)    
        query_select_price="select price from products where product_code='{}'".format(code)
        c.execute(query_select_price)
        data_price=c.fetchall()
        df_price=pd.DataFrame(data_price)
        price=str(df_price[0][0])
        li_price.append(price)
        
    li_qty=[]
    for count in range(0,len_df):
        query_select_qty="select qty_purchased from sales_record where {}='{}'".format(where_clause_customer,customer_name)
        c.execute(query_select_qty)
        data_qty=c.fetchall()
        df_qty=pd.DataFrame(data_qty)
        # code=str(df_data[0][count])
        # li_product_code.append(code)    
        qty=str(df_qty[0][count])
        li_qty.append(qty)
        
    li_amount=[]
    for count in range(0,len_df):
        code=str(df_data[0][count])
        li_product_code.append(code)    
        query_select_amount="select amount from sales_record where product_code='{}'".format(code)
        c.execute(query_select_amount)
        data_amount=c.fetchall()
        df_amount=pd.DataFrame(data_amount)
        amount=int(df_amount[0][0])
        li_amount.append(amount)
    li_sr_no=[]
    for count in range(0,len(li_product_name)):
        li_sr_no.append(count+1)
        
    # print(li_sr_no)
    # print(li_product_name)
    # print(li_dos)
    bill=pd.DataFrame([li_sr_no,li_product_name,li_dos,li_price,li_qty,li_amount],index=['Sr no.','product name','dos','price','qty_purchased','amount'])
    if bill.empty :
        print("Customer doesn't exist or not purchaced anything...")
    else:
        print("-"*60)
        print(bill.T.to_string(index=False))
        print()
        print("Total amount to be paid:-\t",sum(li_amount))
        print("-"*60)
        query_select_name="select customer_name from sales_record where {}='{}'".format(where_clause_customer,customer_name)
        c.execute(query_select_name)
        data_name=c.fetchall()
        df_name=pd.DataFrame(data_name)
        fatched_name=df_name[0][0]
        if fatched_name!="WalkIn":
            ask_change_customer_name=input("Change to walkin (y/n) ?:- ")
            if ask_change_customer_name=="Y" or ask_change_customer_name=="y":
                query_select_id="select customer_id from sales_record where customer_name='WalkIn'"
                c.execute(query_select_id)
                customer_id=c.fetchall()[0][0]
                query_change_walkin="update sales_record set customer_name='WalkIn' , customer_id={} where {}='{}'".format(customer_id,where_clause_customer,customer_name)
                c.execute(query_change_walkin)
                con_file.my.commit()
                query_check_view="select status from settings where number=3"
                c.execute(query_check_view)
                data=c.fetchall()
                on_off=data[0][0]
                if on_off=="on":
                    adjust_customer_id.code("sales_record", "customer_id")
        else:
            exit_=input("Press enter to go back")
