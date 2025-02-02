from tkinter import messagebox
import res
from window import *
import mysql_helper as myhelp
import mycon

c = mycon.my.cursor()

lactation_frame = LabelFrame(win, text="Lactation records", height=850, width=885)


def fun_lactation():
    res.fun_clear_frame()
    child_frame_height = 550
    child_frame_width = 482
    child_frame_x = 10
    child_frame_y = 300
    lactation_frame.place(x=5, y=60)

    def get_table():
        lactation_table = myhelp.select_table("*", "lactation")
        global tree_view
        tree_view = myhelp.create_list(["Entry no", "Cattle code", "Date started", "Date stopped", "Period"],
                                       lactation_frame, lactation_table, [110, 170, 170, 180, 155])
        tree_view.place(x=10, y=60)

    get_table()

    def add_record_main():
        add_stock_frame = LabelFrame(lactation_frame, text="Add stock", height=child_frame_height,
                                     width=child_frame_width)
        add_stock_frame.place(x=child_frame_x, y=child_frame_y)

        date_started_entry = Entry(add_stock_frame, width=30)
        date_stopped_entry = Entry(add_stock_frame, width=30)

        li_entry = [date_started_entry, date_stopped_entry]
        li_label = ["Date started", "Date stopped", "Cattle code", "Period"]
        res.create_labels(add_stock_frame, li_label, li_entry, 160)

        def add_record():
            try:
                cattle_code = cattle_code_option_menu.get()
                entry_no = myhelp.get_primary_key("Entry_no", "lactation")
                date_started_add = date_started_entry.get()
                date_stopped_add = date_stopped_entry.get()
                period = period_option_menu.get()
                c.execute(
                    "insert into lactation values({},{},'{}','{}','{}')".format(entry_no, cattle_code, date_started_add,
                                                                                date_stopped_add, period))
                mycon.my.commit()
                fun_lactation()
                add_record_main()
            except:
                messagebox.showwarning("Warning", "wrong or missing input")

        period_option_menu = myhelp.get_distinct_optionMenu(add_stock_frame, "lactation", "period", cord=[160, 135],
                                                            new=["Calving", "Early lactation", "Mid lactation",
                                                                 "Late lactation", "Dry lactation"])
        cattle_code_option_menu = myhelp.get_distinct_optionMenu(add_stock_frame, "live_assets where type='cow'",
                                                                 "cattle_code,name", cord=[155, 90])
        Button(add_stock_frame, text="Add ", command=add_record).place(x=160, y=185)

    def change_record():
        change_stock_frame = LabelFrame(lactation_frame, text="Change stock", height=child_frame_height,
                                        width=child_frame_width)
        change_stock_frame.place(x=child_frame_x, y=child_frame_y)
        entry_no, date_started, date_stopped = StringVar(), StringVar(), StringVar()
        entry_no_entry = Entry(change_stock_frame, width=30, textvariable=entry_no)

        date_started_entry = Entry(change_stock_frame, width=30, textvariable=date_started)
        date_stopped_entry = Entry(change_stock_frame, width=30, textvariable=date_stopped)

        li_entry = [entry_no_entry, date_started_entry, date_stopped_entry]
        li_label = ["Entry no", "Date started", "Date stopped", "Cattle code", "Period"]

        period_option_menu = myhelp.get_distinct_optionMenu(change_stock_frame, "lactation", "period", cord=[160, 175],
                                                            new=["Calving", "Early lactation", "Mid lactation",
                                                                 "Late lactation", "Dry lactation"])
        cattle_code_option_menu = myhelp.get_distinct_optionMenu(change_stock_frame, "live_assets where type='cow'",
                                                                 "cattle_code,name", cord=[155, 130])
        res.create_labels(change_stock_frame, li_label, li_entry, 160)

        def get_row(event):
            try:
                item = tree_view.item(tree_view.focus())
                values = item['values']
                entry_no.set(values[0])
                cattle_code_option_menu.set(values[1])
                date_started.set(values[2])
                date_stopped.set(values[3])
                period_option_menu.set(values[4])
            except:
                pass

        tree_view.bind("<Double-1>", get_row)

        def update_record():
            try:
                cattle_code_update = cattle_code_option_menu.get()
                entry_no_update = entry_no_entry.get()
                date_started_update = date_started_entry.get()
                date_stopped_update = date_stopped_entry.get()
                period = period_option_menu.get()
                c.execute(
                    "update lactation set cattle_code={},date_started='{}',date_stoped='{}',period='{}' where "
                    "Entry_no={}".format(
                        cattle_code_update, date_started_update, date_stopped_update, period, entry_no_update))
                mycon.my.commit()
                fun_lactation()
                change_record()
            except:
                messagebox.showwarning("Warning", "wrong or missing input")

        def delete_record():
            try:
                entry_no_delete = entry_no_entry.get()
                c.execute("delete from lactation where Entry_no={}".format(entry_no_delete))
                mycon.my.commit()
                fun_lactation()
                change_record()
            except:
                pass

        Button(change_stock_frame, text="Update record", command=update_record).place(x=160, y=225)
        Button(change_stock_frame, text="Delete record", command=delete_record).place(x=30, y=225)

    Button(lactation_frame, text="Add records", command=add_record_main).place(x=10, y=5)
    Button(lactation_frame, text="Change existing records", command=change_record).place(x=140, y=5)
    add_record_main()
