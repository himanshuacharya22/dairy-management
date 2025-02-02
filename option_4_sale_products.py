import con_file
import pandas as pd
def code():
    c=con_file.my.cursor()
     
    select_customer="select distinct(customer_id),customer_name from sales_record"
    execute_select_customer=pd.read_sql(select_customer,con_file.my)
    if execute_select_customer.empty:
        print("None of customers recorded")
    else:
        print("-"*40)
        print(execute_select_customer.to_string(index=False))
        print("-"*40)
    
    customer_name=input("Enter customer name or ID (default walk-in):- ")
    
    # if where_clause_customer=="customer_id":
    #     query_check_customer_id="select * from sales_record where customer_id={}".format(customer_name)
    #     c.execute(query_check_customer_id)
    #     data=c.fetchall()
    #     print(len(data))
        
    qrery_select_products="select * from products"
    execute_select_products=pd.read_sql(qrery_select_products,con_file.my)
    if execute_select_products.empty:
        print("Add a product first..")
    else:
        print("-"*80)
        print(execute_select_products.to_string(index=False))
        print("-"*80)
        product_name=input("Enter product name or code:- ")
        if product_name.isnumeric():
            select_data="select * from products where product_code={}".format(product_name)
            if_product_exist=pd.read_sql(select_data,con_file.my)
        elif product_name.isalpha():
            select_data="select * from products where product_name='{}'".format(product_name)
            if_product_exist=pd.read_sql(select_data,con_file.my)
        if if_product_exist.empty:
           print( "product code or name doesn't exist... ")
        else:
            qty_purchased=int(input("Enter qty purchased:- "))
            if customer_name.isnumeric()  :
                where_clause_customer="customer_id"
                customer_id=customer_name
            elif customer_name.isalpha():
                where_clause_customer="customer_name"
            elif customer_name=="":
                customer_name="WalkIn"
                where_clause_customer="customer_name"
                
            if product_name.isnumeric():
                where_clause_product="product_code"
            elif product_name.isalpha():
                where_clause_product="product_name"
                query_select_product_id="select product_code from products where "+where_clause_product+" = '"+product_name+"'"
                c.execute(query_select_product_id)
                data=c.fetchall()
                df=pd.DataFrame(data)
                product_name=df[0][0]
                print("product_code",product_name)
            query_select_old_qty="select qty_avialable from products where product_code={}".format(product_name)
            c.execute(query_select_old_qty)
            qty_avialable=int(c.fetchall()[0][0])
            if qty_avialable<qty_purchased:
                print("qty not avialable")
            else:
                date_of_purchase=input("Enter date of purchase/default today (yyyy-mm-dd):- ")
                if date_of_purchase=="":
                        query_select_curdate="select curdate()"
                        c.execute(query_select_curdate)
                        fetch_curdate=c.fetchall()
                        df_select_curdate=pd.DataFrame(fetch_curdate)
                        date_of_purchase=str(df_select_curdate[0][0])
                    
                sql=pd.read_sql("select max(entry_no) from sales_record",con_file.my)
                df=pd.DataFrame(sql)
                try:
                    add_entry_no=int(df[max(df)])+1
                except:
                    add_entry_no=1
                query_select_customer_distinct="select distinct("+where_clause_customer+") from sales_record "
                c.execute(query_select_customer_distinct)
                data_customers=c.fetchall()
                df_customers=pd.DataFrame(data_customers)
                li=[]
                for count in range(0,len(df_customers)):
                    li.append(str(df_customers[0][count]))
                query_select_price="select price from products where product_code='"+str(product_name)+"'"
                c.execute(query_select_price)
                data_price_product=c.fetchall()
                df_data_price_product=pd.DataFrame(data_price_product)
                price=int(df_data_price_product[0])
                amount=str(price*qty_purchased)
                # print(amount)
                
                
                if customer_name in li:
                    if  where_clause_customer=="customer_id":
                        
                        query_select_customer_name="select distinct(customer_name) from sales_record where customer_id="+customer_name
                        c.execute(query_select_customer_name)   
                        data_customer_name=c.fetchall()
                        df_data_customer_name=pd.DataFrame(data_customer_name)
                        customer_name=df_data_customer_name[0][0]
                    elif where_clause_customer=="customer_name":
                        query_select_custmer_id="select distinct(customer_id) from sales_record where customer_name"+"='"+customer_name+"'"
                        c.execute(query_select_custmer_id)
                        data_customers_id=c.fetchall()
                        df_customers_id=pd.DataFrame(data_customers_id)
                        customer_id=str(df_customers_id[0][0])
                        
                        
                    query_insert_record="insert into sales_record values("+str(add_entry_no)+","+str(customer_id)+",'"+str(customer_name)+"','"+str(date_of_purchase)+"',"+str(product_name)+","+str(qty_purchased)+","+str(amount)+")"
                    c.execute(query_insert_record)
                    con_file.my.commit()
                    query_update_stock="update products set qty_avialable=qty_avialable-"+str(qty_purchased)+" where product_code='"+str(product_name)+"'"
                    c.execute(query_update_stock)
                    con_file.my.commit()
                    print("Record inserted sussesfully...")
                    
                    
                elif customer_name not in li and where_clause_customer=="customer_name" :
                    query_read_last_cID=pd.read_sql("select max(customer_id) from sales_record",con_file.my)
                    df=pd.DataFrame(query_read_last_cID)
                    try:
                        add_customer_id=int(df[max(df)])+1
                    except:
                        add_customer_id=1
                    query_insert_sales="insert into sales_record values("+str(add_entry_no)+","+str(add_customer_id)+",'"+customer_name+"','"+date_of_purchase+"','"+str(product_name)+"',"+str(qty_purchased)+","+str(amount)+")"
                    c.execute(query_insert_sales)
                    con_file.my.commit()
                    query_update_stock="update products set qty_avialable=qty_avialable-"+str(qty_purchased)+"  where product_code ="+str(product_name)
                    c.execute(query_update_stock)
                    con_file.my.commit()
                    print("Record inserted sussesfully...")
                else:
                    print("Please enter new customer name")
            