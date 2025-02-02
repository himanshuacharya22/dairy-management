from tkinter import messagebox
import res
from window import *
import mycon
import mysql_helper as myhelp

c = mycon.my.cursor()
fooder_frame = LabelFrame(win, text="Fooder Management", height=850, width=885)


def fun_fooder_stock():
    def get_table():
        fooder_table = myhelp.select_table("*", "fooder")
        global tree_view_fooder
        tree_view_fooder = myhelp.create_list(
            ["fooder code", "item name", "purchase date", "vendor", "mode of payment", "stock available",
             "Weights standard", "price"], fooder_frame, fooder_table, [100, 130, 130, 120, 105, 100, 90, 70])
        tree_view_fooder.place(x=1, y=70)

    child_frame_height = 440
    child_frame_width = 502

    child_frame_x = 10
    child_frame_y = 300
    res.fun_clear_frame()
    fooder_frame.place(x=5, y=60)
    dop_ = myhelp.get_date()

    def fun_add_stock():
        def add_stock():

            dop = dop_entry.get()
            f_code = myhelp.get_primary_key("f_code", "fooder")

            try:
                unit_entry.place_info()['x']
                # unit=unit_entry.get()
                query_add = "insert into fooder values({},'{}','{}','{}','{}',{},'{}',{})".format(f_code,
                                                                                                  name_entry.get(), dop,
                                                                                                  vendor_entry.get(),
                                                                                                  payment_type.get(),
                                                                                                  stock_avi_entry.get(),
                                                                                                  unit_entry.get(),
                                                                                                  price_entry.get())
            except:
                query_add = "insert into fooder values({},'{}','{}','{}','{}',{},'{}',{})".format(f_code,
                                                                                                  name_entry.get(), dop,
                                                                                                  vendor_entry.get(),
                                                                                                  payment_type.get(),
                                                                                                  stock_avi_entry.get(),
                                                                                                  unit,
                                                                                                  price_entry.get())

            try:
                c.execute(query_add)
                mycon.my.commit()
                get_table()
                fun_add_stock()
            except:
                messagebox.showwarning("Warning", "wrong or missing input")

        add_stock_frame = LabelFrame(fooder_frame, text="Add stock", height=child_frame_height, width=child_frame_width)
        add_stock_frame.place(x=child_frame_x, y=child_frame_y)

        name_entry = Entry(add_stock_frame, width=30)

        vendor_entry = Entry(add_stock_frame, width=30)

        dop_entry = Entry(add_stock_frame, width=30)
        res.hint_text(dop_entry, dop_)

        stock_avi_entry = Entry(add_stock_frame, width=30)

        price_entry = Entry(add_stock_frame, width=30)

        global unit_entry
        unit_entry = Entry(add_stock_frame, width=20)
        unit_entry.place(x=285, y=210)

        li_entry = [name_entry, vendor_entry, dop_entry, stock_avi_entry, price_entry]
        li_labels = ["Name", "Vendor", 'Date of purchase', "Stock available", "Price", "Weights standard",
                     "Mode of payment"]
        res.create_labels(add_stock_frame, li_labels, li_entry, 180)
        payment_type = res.create_radio(add_stock_frame, ["Cash", "Credit"], [180, 250])

        def option_menu_clicked(event):
            global unit
            unit = unit_option_menu.get()
            if unit == "new":
                unit_entry.place(x=285, y=210)
                unit = unit_entry.get()
            else:
                try:
                    unit_entry.place_forget()
                except:
                    pass

        unit_option_menu = myhelp.get_distinct_optionMenu(add_stock_frame, "fooder", "unit", option_menu_clicked,
                                                          [180, 205], ['new'])
        Button(add_stock_frame, text="Add", command=add_stock).place(x=180, y=320)

    def change_stock():
        change_stock_frame = LabelFrame(fooder_frame, text="Change stock", height=child_frame_height,
                                        width=child_frame_width)
        change_stock_frame.place(x=child_frame_x, y=child_frame_y)

        code, name, vendor, payment_type, dop = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
        stock_avi, unit, price = StringVar(), StringVar(), StringVar()

        fooder_code_entry = Entry(change_stock_frame, width=30, textvariable=code)

        name_entry = Entry(change_stock_frame, width=30, textvariable=name)

        vendor_entry = Entry(change_stock_frame, width=30, textvariable=vendor)

        dop_entry = Entry(change_stock_frame, width=30, textvariable=dop)
        res.hint_text(dop_entry, dop_)

        stock_avi_entry = Entry(change_stock_frame, width=30, textvariable=stock_avi)

        global unit_entry
        unit_entry = Entry(change_stock_frame, width=20, textvariable=unit)
        unit_entry.place(x=285, y=250)

        price_entry = Entry(change_stock_frame, width=30, textvariable=price)

        def optionMenu_clicked(event):
            global unit
            unit = unit_optionMenu.get()

            if unit == "new":
                unit_entry.place(x=285, y=250)
                unit = unit_entry.get()
            else:
                try:
                    unit_entry.place_forget()
                except:
                    pass

        unit_optionMenu = myhelp.get_distinct_optionMenu(change_stock_frame, "fooder", "unit", optionMenu_clicked,
                                                         [180, 245], ['new'])
        li_entry = [fooder_code_entry, name_entry, vendor_entry, dop_entry, stock_avi_entry, price_entry]
        li_labels = ["Fooder code", "Name", "Vendor", 'Date of purchase', "Stock available", "Price",
                     "Weights standard", "Mode of payment"]
        res.create_labels(change_stock_frame, li_labels, li_entry, 180)
        payment_type = res.create_radio(change_stock_frame, ["Cash", "Credit"], [180, 290])

        def get_row(event):
            try:
                item = tree_view_fooder.item(tree_view_fooder.focus())
                values = item['values']
                code.set(values[0])
                name.set(values[1])
                dop.set(values[2])
                vendor.set(values[3])
                payment_type.set(values[4])
                stock_avi.set(values[5])
                unit_optionMenu.set(values[6])
                unit_entry.place_forget()
                price.set(values[7])
            except:
                messagebox.showwarning("Warning", "Wrong or missing input")

        tree_view_fooder.bind("<Double-1>", get_row)

        def update_stock():
            if unit_optionMenu.get() != "new":
                unit_update = unit_optionMenu.get()
            else:
                unit_update = unit_entry.get()
            dop_update = dop_entry.get()
            try:
                c.execute(
                    "update fooder set name='{}',purchase_on='{}',vendor='{}',mode_of_payment='{}',stock_avi={},"
                    "unit='{}',price='{}' where f_code={}".format(
                        name_entry.get(), dop_update, vendor_entry.get(), payment_type.get(), stock_avi_entry.get(),
                        unit_update, price_entry.get(), fooder_code_entry.get()))
                mycon.my.commit()
                get_table()
                change_stock()

            except:
                messagebox.showwarning("Warning", "Wrong or missing input")
                raise

        def delete_stock():
            try:
                myhelp.delete("fooder", "f_code", fooder_code_entry.get())
                get_table()
                change_stock()
            except:
                messagebox.showwarning("Warning", "wrong or missing input")
                raise

        Button(change_stock_frame, text="Update record", command=update_stock).place(x=190, y=340)

        Button(change_stock_frame, text="Delete record", command=delete_stock).place(x=50, y=340)

    Button(fooder_frame, text="Add new stock", command=fun_add_stock).place(x=10, y=5)
    Button(fooder_frame, text="Change existing stock", command=change_stock).place(x=150, y=5)
    fun_add_stock()
    get_table()
