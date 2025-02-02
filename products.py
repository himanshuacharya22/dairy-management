from tkinter import messagebox
import res
from window import *
import mysql_helper as myhelp
import sell_product
import mycon

c = mycon.my.cursor()

product_frame = LabelFrame(win, text="Products", height=850, width=885)

li_heads = ["Product code", "Product name", "Price", "Qty available", "Weights standard"]


def get_table():
    product_table = myhelp.select_table("*", "products")
    global tree_view_product
    tree_view_product = myhelp.create_list(li_heads, product_frame, product_table, [152, 182, 182, 172, 157])
    tree_view_product.place(x=1, y=70)


def fun_product():
    res.fun_clear_frame()

    child_frame_height = 350
    child_frame_width = 502
    child_frame_x = 10
    child_frame_y = 300
    product_frame.place(x=5, y=60)

    get_table()

    def add_stock_main():
        add_stock_frame = LabelFrame(product_frame, text="Add stock", height=child_frame_height,
                                     width=child_frame_width)
        add_stock_frame.place(x=child_frame_x, y=child_frame_y)

        name_entry = Entry(add_stock_frame, width=30)

        stock_avi_entry = Entry(add_stock_frame, width=30)

        unit_entry = Entry(add_stock_frame, width=20)
        unit_entry.place(x=290, y=130)

        price_entry = Entry(add_stock_frame, width=30)

        li_entry = [name_entry, price_entry, stock_avi_entry]
        res.create_labels(add_stock_frame, li_heads[1:], li_entry, 180)

        def option_menu_clicked(event):
            global unit
            unit_option_menu.get()

            if unit == "new":
                unit_entry.place(x=290, y=130)
            else:
                try:
                    unit_entry.place_forget()
                except:
                    pass

        unit_option_menu = myhelp.get_distinct_optionMenu(add_stock_frame, "products", "weights_standard",
                                                          option_menu_clicked, [180, 125],
                                                          ["liter", "kilo gram", 'new'])

        def add_stock():
            p_code = myhelp.get_primary_key("product_code", "products")
            if unit_option_menu.get() == "new":
                unit_ = unit_entry.get()
            else:
                unit_ = unit_option_menu.get()
            try:
                c.execute("insert into products values({},'{}',{},{},'{}')".format(p_code, name_entry.get(),
                                                                                   price_entry.get(),
                                                                                   stock_avi_entry.get(), unit_))
                mycon.my.commit()
                get_table()
                add_stock_main()
            except:
                messagebox.showwarning("Warning", "Wrong or missing input")

        Button(add_stock_frame, text="Add", command=add_stock).place(x=180, y=190)

    def change_stock():
        change_stock_frame = LabelFrame(product_frame, text="Change stock", height=child_frame_height,
                                        width=child_frame_width)
        change_stock_frame.place(x=child_frame_x, y=child_frame_y)
        code, name, stock_avi, unit, price = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()

        code_entry = Entry(change_stock_frame, width=30, textvariable=code)

        name_entry = Entry(change_stock_frame, width=30, textvariable=name)

        stock_avi_entry = Entry(change_stock_frame, width=30, textvariable=stock_avi)

        unit_entry = Entry(change_stock_frame, width=20, textvariable=unit)
        unit_entry.place(x=290, y=170)

        price_entry = Entry(change_stock_frame, width=30, textvariable=price)
        li_entry = [code_entry, name_entry, price_entry, stock_avi_entry]
        res.create_labels(change_stock_frame, li_heads, li_entry, 180)

        def option_menu_clicked(event):
            global unit
            unit = unit_option_menu.get()

            if unit == "new":
                unit_entry.place(x=290, y=170)
            else:
                try:
                    unit_entry.place_forget()
                except:
                    pass

        unit_option_menu = myhelp.get_distinct_optionMenu(
            change_stock_frame, "products", "weights_standard", option_menu_clicked, [180, 165],
            ['new', "liter", "kilo gram"])

        def get_row():
            try:
                item = tree_view_product.item(tree_view_product.focus())
                values = item['values']
                code.set(values[0])
                name.set(values[1])
                price.set(values[2])
                stock_avi.set(values[3])
                unit_option_menu.set(values[4])
                unit_entry.place_forget()

            except:
                pass

        tree_view_product.bind("<Double-1>", get_row)

        def update_stock():
            if unit_option_menu.get() == "new":
                unit_ = unit_entry.get()
            else:
                unit_ = unit_option_menu.get()
            try:
                c.execute(
                    "update products set product_name='{}',qty_available={},weights_standard='{}',price='{}' where "
                    "product_code={}".format(
                        name_entry.get(), stock_avi_entry.get(), unit_, price_entry.get(), code_entry.get()))
                mycon.my.commit()
                get_table()
                change_stock()

            except:
                messagebox.showwarning("Warning", "Wrong or missing input")

        def delete_stock():

            try:
                myhelp.delete("products", "product_code", code_entry.get())
                get_table()
                change_stock()
            except:
                messagebox.showwarning("Warning", "Wrong or missing input")

        Button(change_stock_frame, text="Update record", command=update_stock).place(x=190, y=220)
        Button(change_stock_frame, text="Delete record", command=delete_stock).place(x=50, y=220)

    def sell():
        sell_product.sale_stock()

    Button(product_frame, text="Add new stock", command=add_stock_main).place(x=10, y=5)
    Button(product_frame, text="Change existing stock", command=change_stock).place(x=160, y=5)
    Button(product_frame, text="Sale product", command=sell).place(x=360, y=5)
    add_stock_main()
