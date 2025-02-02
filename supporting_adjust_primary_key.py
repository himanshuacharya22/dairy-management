import con_file
def code(table_name,column_name):
    tb=table_name
    cn=column_name
    c=con_file.my.cursor()
    query_select_f_code="select distinct("+cn+") from "+tb+" order by "+cn
    c.execute(query_select_f_code)
    df=c.fetchall()
    li_correct_order=[]
    li_wrong_order=[]
    for count in range(0,len(df)):
        li_correct_order.append(count+1)
        li_wrong_order.append(df[count][0])
    while li_wrong_order!=li_correct_order:
        _query_select_f_code="select "+cn+" from "+tb+" order by "+cn
        c.execute(_query_select_f_code)
        _df=c.fetchall()
        _count_f_code=1
        for count in range(0,len(df)):
            if _df[count][0]!=_count_f_code:
                query_back_f_code="update "+tb+" set "+cn+"="+cn+"-1 where "+cn+">"+str(_count_f_code)
                c.execute(query_back_f_code)
                con_file.my.commit()
                query_select_f_code="select distinct("+cn+") from "+tb+" order by "+cn
                c.execute(query_select_f_code)
                df=c.fetchall()
                li_wrong_order=[]
                for count in range(0,len(df)):
                     li_wrong_order.append(df[count][0])
                break
            _count_f_code+=1
