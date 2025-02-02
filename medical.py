from tkinter import messagebox
import res
from window import *
import mycon
import mysql_helper as myhelp

c = mycon.my.cursor()
medical_frame = LabelFrame(win, text="Medical Management", height=850, width=885)


def fun_medical_stock():
    def get_table():
        medical_table = myhelp.select_table("*", "medical")
        global tree_view_medical
        tree_view_medical = myhelp.create_list(["Entry no", "cattle code", "Date of checkup", "Issues"], medical_frame,
                                               medical_table, [190, 220, 220, 210])
        tree_view_medical.place(x=1, y=70)

    child_frame_height = 440
    child_frame_width = 502

    child_frame_x = 10
    child_frame_y = 300
    res.fun_clear_frame()
    medical_frame.place(x=5, y=60)
    dop_ = myhelp.get_date()

    def add_record_main():
        get_table()
        add_stock_frame = LabelFrame(medical_frame, text="Add record", height=child_frame_height,
                                     width=child_frame_width)
        add_stock_frame.place(x=child_frame_x, y=child_frame_y)

        cattle_code_entry = Entry(add_stock_frame, width=30)

        date_checkup_entry = Entry(add_stock_frame, width=30)

        res.hint_text(date_checkup_entry, dop_)

        issues_entry = Entry(add_stock_frame, width=30)

        li_labels = ["Cattle code", "Date of checkup", "Issues"]
        li_entry = [cattle_code_entry, date_checkup_entry, issues_entry]
        res.create_labels(add_stock_frame, li_labels, li_entry, 180)

        def add_record():
            try:
                entry_no = myhelp.get_primary_key("Entry_no", "medical")
                c_code = cattle_code_entry.get()
                date_checkup = date_checkup_entry.get()
                issues = issues_entry.get()
                c.execute("insert into medical values({},{},'{}','{}')".format(entry_no, c_code, date_checkup, issues))
                mycon.my.commit()
                get_table()
                add_record_main()
            except:
                messagebox.showwarning("Warning", "wrong or missing input")

        Button(add_stock_frame, text="Add", command=add_record).place(x=180, y=130)

    def change_stock():
        get_table()
        change_stock_frame = LabelFrame(medical_frame, text="Change stock", height=child_frame_height,
                                        width=child_frame_width)
        change_stock_frame.place(x=child_frame_x, y=child_frame_y)

        entry_no, cattle_code, date_checkup, issues = StringVar(), StringVar(), StringVar(), StringVar()

        entry_no_entry = Entry(change_stock_frame, width=30, textvariable=entry_no)

        cattle_code_entry = Entry(change_stock_frame, width=30, textvariable=cattle_code)

        date_checkup_entry = Entry(change_stock_frame, width=30, textvariable=date_checkup)

        res.hint_text(date_checkup_entry, dop_)

        issues_entry = Entry(change_stock_frame, width=30, textvariable=issues)

        li_labels = ["Entry no", "Cattle code", "Date of checkup", "Issues"]
        li_entry = [entry_no_entry, cattle_code_entry, date_checkup_entry, issues_entry]
        res.create_labels(change_stock_frame, li_labels, li_entry, 180)

        def get_row():
            try:
                item = tree_view_medical.item(tree_view_medical.focus())
                values = item['values']
                entry_no.set(values[0])
                cattle_code.set(values[1])
                date_checkup.set(values[2])
                issues.set(values[3])
            except:
                pass

        tree_view_medical.bind("<Double-1>", get_row)

        def update():
            entry_no_update = entry_no_entry.get()
            c_code_update = cattle_code_entry.get()
            date_checkup_update = date_checkup_entry.get()
            issues_update = issues_entry.get()
            c.execute(
                "update medical set cattle_code={},date_of_checkup='{}',issues='{}' where Entry_no={}"
                .format(c_code_update, date_checkup_update, issues_update, entry_no_update))
            mycon.my.commit()
            change_stock()

        def delete():
            try:
                c.execute("delete from medical where entry_no={}".format(entry_no_entry.get()))
                mycon.my.commit()
                change_stock()
            except:
                pass

        Button(change_stock_frame, text="Update", command=update).place(x=180, y=170)
        Button(change_stock_frame, text="Delete", command=delete).place(x=90, y=170)

    Button(medical_frame, text="Add new stock", command=add_record_main).place(x=10, y=5)
    Button(medical_frame, text="Change existing stock", command=change_stock).place(x=150, y=5)
    add_record_main()
