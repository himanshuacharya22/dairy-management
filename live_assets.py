from tkinter import messagebox
import res
from window import *
import mysql_helper as myhelp
import mycon

c = mycon.my.cursor()
live_assets_frame = LabelFrame(win, text="Live assets", height=850, width=885)


def fun_live_assets():
    def get_table():
        live_assets_table = myhelp.select_table("*", "live_assets")
        global tree_view
        tree_view = myhelp.create_list(["Cattle_code", "Name", "Breed", "Date of purchase", "Type"], live_assets_frame,
                                       live_assets_table, [110, 170, 170, 180, 155])
        tree_view.place(x=10, y=60)

    child_frame_height = 350
    child_frame_width = 575

    child_frame_x = 10
    child_frame_y = 300
    res.fun_clear_frame()
    live_assets_frame.place(x=5, y=60)
    dop_ = myhelp.get_date()

    def add_stock():
        def add_stock_sub():

            dop = dop_entry.get()
            # print(breed)
            name = name_entry.get()
            type_ = type_radio.get()
            cattle_code = myhelp.get_primary_key("cattle_code", "live_assets")
            if name != "":
                try:
                    breed_entry.place_info()['x']
                    breed_ = breed_entry.get()
                    query_add = "insert into live_assets values({},'{}','{}','{}','{}')".format(cattle_code, name,
                                                                                                breed_, dop, type_)
                except:
                    query_add = "insert  into live_assets values({},'{}','{}','{}','{}')".format(cattle_code, name,
                                                                                                 breed, dop, type_)

                c.execute(query_add)
                mycon.my.commit()
                get_table()
                fun_live_assets()

            else:
                messagebox.showwarning("Warning", "Wrong or missing input")

        add_stock_frame = LabelFrame(live_assets_frame, text="Add stock", height=child_frame_height,
                                     width=child_frame_width)
        add_stock_frame.place(x=child_frame_x, y=child_frame_y)

        name_entry = Entry(add_stock_frame, width=30)

        # breed_entry=Entry(add_stock_frame,width=30)

        global breed_entry
        breed_entry = Entry(add_stock_frame, width=20)
        breed_entry.place(x=270, y=90)

        dop_entry = Entry(add_stock_frame, width=30)
        res.hint_text(dop_entry, dop_)
        li_entry = [name_entry, dop_entry]
        li_labels = ["Name", "Date of purchase", "Breed", "type"]
        res.create_labels(add_stock_frame, li_labels, li_entry, 160)
        type_radio = res.create_radio(add_stock_frame, ["cow", "bull", "calf"], [160, 130])
        Button(add_stock_frame, text="Add", command=add_stock_sub).place(x=160, y=200)

        def optionMenu_clicked(event):
            global breed
            breed = type_optionMenu.get()

            if breed == "new":
                breed_entry.place(x=270, y=90)
                breed = breed_entry.get()
            else:
                try:
                    breed_entry.place_forget()
                except:
                    pass

        type_optionMenu = myhelp.get_distinct_optionMenu(add_stock_frame, "live_assets", "breed", optionMenu_clicked,
                                                         [160, 85], ['new'])

    def change_stock():
        code, name, breed, type_, dop = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
        change_stock_frame = LabelFrame(live_assets_frame, text="Change stock", height=child_frame_height,
                                        width=child_frame_width)
        change_stock_frame.place(x=child_frame_x, y=child_frame_y)

        code_entry = Entry(change_stock_frame, width=30, textvariable=code)

        name_entry = Entry(change_stock_frame, width=30, textvariable=name)

        global breed_entry
        breed_entry = Entry(change_stock_frame, width=20, textvariable=breed)
        breed_entry.place(x=270, y=130)

        dop_entry = Entry(change_stock_frame, width=30, textvariable=dop)
        res.hint_text(dop_entry, dop_)
        li_entry = [code_entry, name_entry, dop_entry]
        li_labels = ["Cattle code", "Name", "Date of purchase", "Breed", "Type"]
        res.create_labels(change_stock_frame, li_labels, li_entry, 160)
        type_radio = res.create_radio(change_stock_frame, ["cow", "bull", "calf"], [160, 170])

        def optionMenu_clicked(event):
            global breed
            breed = type_optionMenu.get()

            if breed == "new":
                breed_entry.place(x=270, y=130)
                breed = breed_entry.get()
            else:
                try:
                    breed_entry.place_forget()
                except:
                    pass

        type_optionMenu = myhelp.get_distinct_optionMenu(change_stock_frame, "live_assets", "breed", optionMenu_clicked,
                                                         [155, 120], ['new'])

        def get_row(event):
            try:
                item = tree_view.item(tree_view.focus())
                values = item['values']
                code.set(values[0])
                name.set(values[1])
                type_optionMenu.set(values[2])
                dop.set(values[3])
                type_radio.set(values[4])
                breed_entry.place_forget()
            except:
                pass

        tree_view.bind("<Double-1>", get_row)

        def update():
            dop_update = dop_entry.get()
            if dop_update == "":
                dop_update = myhelp.get_date()
            try:
                breed_entry.place_info()['x']
                breed_ = breed_entry.get()
                update_query = "update live_assets set name='{}',breed='{}',date_of_purchase='{}',type='{}' where " \
                               "cattle_code={}".format(name_entry.get(), breed_, dop_update, type_radio.get(),
                                                       code_entry.get())
            except:
                update_query = "update live_assets set name='{}',breed='{}',date_of_purchase='{}',type='{}' where " \
                               "cattle_code={}".format(name_entry.get(), type_optionMenu.get(), dop, type_radio.get(),
                                                       code_entry.get())
            try:
                c.execute(update_query)
                mycon.my.commit()
                get_table()
                change_stock()
            except:
                messagebox.showwarning("Warning", "wrong or missing input")

        def delete_live():
            try:
                myhelp.delete("live_assets", "cattle_code", code_entry.get())
                get_table()
                change_stock()
            except:
                messagebox.showwarning("Warning", "wrong or missing input")

        Button(change_stock_frame, text="Delete item", command=delete_live).place(x=60, y=250)
        Button(change_stock_frame, text="Update changes", command=update).place(x=190, y=250)

    Button(live_assets_frame, text="Add new stock", command=add_stock).place(x=10, y=5)
    Button(live_assets_frame, text="Change existing stock", command=change_stock).place(x=150, y=5)
    get_table()
    add_stock()


fun_live_assets()
