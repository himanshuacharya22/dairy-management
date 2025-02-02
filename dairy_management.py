import database_tables
database_tables.code()
import option_1_Manage_live_assets as option_1
import option_2_fooder as option_2
import option_3_manage_products as option_3
import option_4_sale_products as  option_4
import option_5_lactation as option_5
import option_6_medical as option_6
import option_7_sales_records as option_7
import option_8_bill_section as option_8
import option_9_settings as option_9
while True:
    task_select=input("_"*41+"""
|Select a task                           |
|         1. Manage live assets          |
|         2. Mange fooder stock          |
|         3. Manage products             |
|         4. Sale products               |
|         5. Lactation records           |
|         6. Medical records             |
|         7. Analise sales records       |
|         8. Show bill                   |
|         9. Settings                    |
|         10. quit                       |
|"""+"_"*40+"""|
Enter your choice:- """)
    if task_select=="1":#Manage live assets 
        option_1.code()
    elif task_select=="2":#fooder
        option_2.code()
    elif task_select=="3":#manage products
        option_3.code()
    elif task_select=="4":#Sale products
        option_4.code()
    elif task_select=="5":#Lactation records
        option_5.code()
    elif task_select=="6":# Medical records
        option_6.code()
    elif task_select=="7":#Analise sales records
        option_7.code()
    elif task_select=="8":#Show bill
        option_8.code()
    elif task_select=="9":#Settings
        option_9.code()
    elif task_select=="10":
        break        
    else:
        print("Invalid choice")
