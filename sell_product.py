from tkinter import messagebox
import products
import mysql_helper as myhelp
import res
from window import *
import mycon

c = mycon.my.cursor()

customer_frame = LabelFrame(win, text="Customer Records", height=850, width=885)


def sale_stock():
    child_frame_height = 350
    child_frame_width = 502
    child_frame_x = 10
    child_frame_y = 300
    dos_ = myhelp.get_date()
    sale_stock_frame = LabelFrame(products.product_frame, text="Sale stock", height=child_frame_height,
                                  width=child_frame_width)
    sale_stock_frame.place(x=child_frame_x, y=child_frame_y)

    p_code, name, qty, dos = StringVar(), StringVar(), StringVar(), StringVar()

    p_code_entry = Entry(sale_stock_frame, width=30, textvariable=p_code)

    dos_entry = Entry(sale_stock_frame, width=30, textvariable=dos)
    res.hint_text(dos_entry, dos_)

    name_entry = Entry(sale_stock_frame, width=30, textvariable=name)

    global customer_name_entry
    customer_entry = Entry(sale_stock_frame, width=20)
    customer_entry.place(x=260, y=175)

    qty_entry = Entry(sale_stock_frame, width=30, textvariable=qty)

    def get_row():
        try:
            item = products.tree_view_product.item(products.tree_view_product.focus())
            global values
            values = item['values']
            p_code.set(values[0])
            name.set(values[1])
        except:
            pass

    products.tree_view_product.bind("<Double-1>", get_row)
    li_entry = [p_code_entry, name_entry, qty_entry, dos_entry]
    li_labels = ["product code", "Product name", "Qty", "Date of sale", "customer"]
    res.create_labels(sale_stock_frame, li_labels, li_entry, 150)

    def option_menu_clicked(event):
        global customer
        customer = customer_name_option_menu.get()

        if customer == "new":
            customer_entry.place(x=270, y=90)
        else:
            try:
                customer_entry.place_forget()
            except:
                pass

    def product_purchased():
        try:
            entry_no = myhelp.get_primary_key("Entry_no", "sales_record")
            dos_purchase = dos_entry.get()
            qty_purchase = qty_entry.get()
            amount = int(qty_purchase) * int(values[2])
            c.execute("select qty_available from products where product_code={} and product_name='{}'".format(
                p_code_entry.get(), name_entry.get()))
            check = c.fetchone()[0]
            if int(qty_purchase) <= int(check):

                if customer_name_option_menu.get() == "new":
                    customer_ = customer_entry.get()
                else:
                    customer_ = customer_name_option_menu.get()

                c.execute("insert into sales_record values({},'{}','{}',{},'{}',{},{})".format(entry_no, customer_,
                                                                                               dos_purchase,
                                                                                               p_code_entry.get(),
                                                                                               name_entry.get(), qty,
                                                                                               amount))
                c.execute("update products set qty_available=qty_available-{} where product_code={}"
                          .format(qty, p_code_entry.get()))
                mycon.my.commit()
                products.get_table()
                sale_stock()
            else:
                messagebox.showwarning("Warning", "Insufficient quantity")
        except:
            messagebox.showwarning("Warning", "Wrong or missing input")

    def customer_record():

        products.product_frame.place_forget()
        customer_frame.place(x=2, y=60)
        bill_table = myhelp.select_table("product_name,dos,qty_purchased,amount",
                                         "sales_record where customer_name='walk in'")
        bill_table_tree_view = myhelp.create_list(["product_name", "date of sale", "quantity purchased", "amount"],
                                                  customer_frame, bill_table, [250, 250, 150, 150])
        bill_table_tree_view.place(x=1, y=10)
        bill_table = myhelp.select_table("sum(amount)", "sales_record where customer_name='walk in'")
        global total_label
        price_frame = LabelFrame(customer_frame, text="Total Amount", height=60, width=250)
        price_frame.place(x=10, y=261)
        total_label = Label(price_frame, text=bill_table)
        total_label.place(x=120, y=0.1)

        def back():
            for widget in customer_frame.winfo_children():
                widget.destroy()
            products.fun_product()
            sale_stock()

        back_button = Button(customer_frame, text="Back", command=back)
        back_button.place(x=230, y=390)

        def move_record():
            c.execute("update sales_record set customer_name='walk in' where customer_name='{}'".format(
                customer_name_option_menu.get()))
            mycon.my.commit()
            customer_record()

        def option_menu_customer_clicked(event):
            price_frame.place(x=10, y=261)
            selected_customer = customer_name_option_menu.get()
            bill_table_option_menu = myhelp.select_table("product_name,dos,qty_purchased,amount",
                                                         "sales_record where customer_name='{}'".format(
                                                             selected_customer))
            bill_table_tree_view_option_menu = myhelp.create_list(["product_name", "dos", "qty_purchased", "amount"],
                                                                  customer_frame, bill_table_option_menu,
                                                                  [250, 250, 150, 150])
            bill_table_tree_view_option_menu.place(x=1, y=10)
            total = myhelp.select_table("sum(amount)",
                                        "sales_record where customer_name='{}'".format(selected_customer))
            total_label.config(text=total)

        res.create_labels(customer_frame, ["Select customer"], [], 10, cordinate_y=335)

        customer_name = myhelp.get_distinct_optionMenu(customer_frame, "sales_record", "customer_name",
                                                       option_menu_customer_clicked, [170, 330], ['walk in'])
        customer_name.set("walk in")
        move_record_button = Button(customer_frame, text="Move record as walk in", command=move_record)
        move_record_button.place(x=10, y=390)

    customer_name_option_menu = myhelp.get_distinct_optionMenu(sale_stock_frame, "sales_record", "customer_name",
                                                               option_menu_clicked, [150, 170], ['new', 'walk in'])
    Button(sale_stock_frame, text="Done", command=product_purchased).place(x=150, y=230)
    Button(sale_stock_frame, text="Customer record", command=customer_record).place(x=230,
                                                                                    y=230)
