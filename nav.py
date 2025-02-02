from window import *
import live_assets
import fooder_stock
import products
import lactation
import medical

navigation_frame = Frame(win, height=50, width=1050)


def fun_navigation():
    def exit_button():
        win.destroy()

    navigation_frame.place(x=10, y=3)
    Button(navigation_frame, text="Manage live assets", command=live_assets.fun_live_assets).place(x=5, y=5)

    Button(navigation_frame, text="Manage fooder stock", command=fooder_stock.fun_fooder_stock).place(x=185, y=5)

    Button(navigation_frame, text="Manage products", command=products.fun_product).place(x=385, y=5)

    Button(navigation_frame, text="Lactation records", command=lactation.fun_lactation).place(x=555, y=5)

    Button(navigation_frame, text="Medical records", command=medical.fun_medical_stock).place(x=715, y=5)

    # settings_button=Button(navigation_frame,text="Settings").place(x=865,y=5)

    Button(navigation_frame, text="Exit", command=exit_button).place(x=865, y=5)
