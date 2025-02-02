from tkinter import *

win = Tk()
win.geometry("1050x900")
win.title("Dairy Management")
win.resizable(True, True)  # width,height


def fun_clear_frame():
    try:
        navigation_frame.place_forget()
    except:
        pass
    try:
        frame.place_forget()
    except:
        pass
    try:
        live_assets_frame.place_forget()
    except:
        pass
    try:
        fooder_frame.place_forget()
    except:
        pass
    try:
        product_frame.place_forget()
    except:
        pass
    try:
        lactation_frame.place_forget()
    except:
        pass


def adj_place():
    try:
        frame.place_info()['x'] == "10"
        frame.place(x=160, y=3)
    except:
        pass
    try:
        live_assets_frame.place_info()['x'] == "10"
        live_assets_frame.place(x=160, y=3)
    except:
        pass
    try:
        fooder_frame.place_info()['x'] == "10"
        fooder_frame.place(x=160, y=3)
    except:
        pass
    try:
        product_frame.place_info()['x'] == "10"
        product_frame.place(x=160, y=3)
    except:
        pass
    try:
        lactation_frame.place_info()['x'] == "10"
        lactation_frame.place(x=160, y=3)
    except:
        pass


def fun_frame_welcome():
    fun_clear_frame()
    global frame
    frame = LabelFrame(win, text="Welcome screen", height=850, width=885)
    option_button = Button(frame, text="Options", command=fun_navigation)
    frame.place(x=10, y=3)
    option_button.place(x=5, y=5)


def fun_live_assets():
    fun_clear_frame()
    child_frame_height = 550
    child_frame_width = 482
    global live_assets_frame
    live_assets_frame = LabelFrame(win, text="Live assets", height=850, width=885)
    live_assets_frame.place(x=10, y=3)

    def add_stock():
        LabelFrame(live_assets_frame, text="Add stock", height=child_frame_height,
                   width=child_frame_width).place(x=10, y=40)

    def change_stock():
        LabelFrame(live_assets_frame, text="Change stock", height=child_frame_height,
                   width=child_frame_width).place(x=10, y=40)

    Button(live_assets_frame, text="Add new stock", command=add_stock).place(x=10, y=5)
    Button(live_assets_frame, text="Change existing stock", command=change_stock).place(x=110, y=5)
    Button(live_assets_frame, text="Options", command=fun_navigation).place(x=250, y=5)
    add_stock()


def fun_fooder_stock():
    fun_clear_frame()
    child_frame_height = 550
    child_frame_width = 482
    global fooder_frame
    fooder_frame = LabelFrame(win, text="Fooder Management", height=850, width=885)
    fooder_frame.place(x=10, y=3)

    def add_stock():
        LabelFrame(fooder_frame, text="Add stock", height=child_frame_height,
                   width=child_frame_width).place(x=10, y=40)

    def change_stock():
        LabelFrame(fooder_frame, text="Change stock", height=child_frame_height,
                   width=child_frame_width).place(x=10, y=40)

    Button(fooder_frame, text="Add new stock", command=add_stock).place(x=10, y=5)
    Button(fooder_frame, text="Change existing stock", command=change_stock).place(x=110, y=5)
    Button(fooder_frame, text="Options", command=fun_navigation).place(x=250, y=5)
    add_stock()


def fun_product():
    fun_clear_frame()
    child_frame_height = 550
    child_frame_width = 482
    global product_frame
    product_frame = LabelFrame(win, text="Products", height=850, width=885)
    product_frame.place(x=10, y=3)

    def add_stock():
        LabelFrame(product_frame, text="Add stock", height=child_frame_height,
                   width=child_frame_width).place(x=10, y=40)

    def change_stock():
        LabelFrame(product_frame, text="Change stock", height=child_frame_height,
                   width=child_frame_width).place(x=10, y=40)

    def sale_stock():
        LabelFrame(product_frame, text="Sale stock", height=child_frame_height,
                   width=child_frame_width).place(x=10, y=40)

    Button(product_frame, text="Add new stock", command=add_stock).place(x=10, y=5)
    Button(product_frame, text="Change existing stock", command=change_stock).place(x=110, y=5)
    Button(product_frame, text="Sale product", command=sale_stock).place(x=250, y=5)
    Button(product_frame, text="Options", command=fun_navigation).place(x=340, y=5)
    add_stock()


def fun_lactation():
    fun_clear_frame()
    child_frame_height = 550
    child_frame_width = 482
    global lactation_frame
    lactation_frame = LabelFrame(win, text="Lactation records", height=850, width=885)
    lactation_frame.place(x=10, y=3)

    def add_record():
        LabelFrame(lactation_frame, text="Add stock", height=child_frame_height,
                   width=child_frame_width).place(x=10, y=40)

    def change_record():
        LabelFrame(lactation_frame, text="Change stock", height=child_frame_height,
                   width=child_frame_width).place(x=10, y=40)

    Button(lactation_frame, text="Add records", command=add_record).place(x=10, y=5)
    Button(lactation_frame, text="Change existing records", command=change_record).place(x=100, y=5)
    Button(lactation_frame, text="Options", command=fun_navigation).place(x=255, y=5)
    add_record()


def fun_navigation():
    global navigation_frame
    navigation_frame = Frame(win, height=840, width=150)
    navigation_frame.place(x=10, y=3)
    adj_place()
    live_assets_button = Button(navigation_frame, text="Manage live assets", command=fun_live_assets)
    live_assets_button.place(x=5, y=5)

    fooder_stock_button = Button(navigation_frame, text="Manage fooder stock", command=fun_fooder_stock)
    fooder_stock_button.place(x=5, y=35)

    products_button = Button(navigation_frame, text="Manage products", command=fun_product)
    products_button.place(x=5, y=65)

    lactation_button = Button(navigation_frame, text="Lactation records", command=fun_lactation)
    lactation_button.place(x=5, y=95)

    medical_button = Button(navigation_frame, text="Medical records")
    medical_button.place(x=5, y=125)

    settings_button = Button(navigation_frame, text="Settings")
    settings_button.place(x=5, y=155)

    home_button = Button(navigation_frame, text="Home", command=fun_frame_welcome)
    home_button.place(x=5, y=185)


fun_frame_welcome()
win.mainloop()
