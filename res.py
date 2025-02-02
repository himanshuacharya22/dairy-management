from tkinter import *
import live_assets
import fooder_stock
import products
import sell_product
import lactation
import medical


def fun_clear_frame():
    li_frames = [medical.medical_frame, sell_product.customer_frame, fooder_stock.fooder_frame, products.product_frame,
                 lactation.lactation_frame, live_assets.live_assets_frame]

    for frames in li_frames:
        try:
            frames.place_forget()

        except not frames:
            continue


def create_labels(frame="", labels=None, li_entry=None, cordinate_x=0, cordinate_y=10):
    if li_entry is None:
        li_entry = []
    if labels is None:
        labels = []
    for label in labels:
        Label(frame, text=label).place(x=10, y=cordinate_y)
        cordinate_y += 40
    cordinate_y = 10

    try:
        for entry in li_entry:
            entry.place(x=cordinate_x, y=cordinate_y)
            cordinate_y += 40
    except:
        raise


def create_radio(frame="", texts=None, cord=None):
    if cord is None:
        cord = []
    if texts is None:
        texts = []
    var = StringVar()
    var.set(texts[0])
    for tex in texts:
        Radiobutton(frame, text=tex, value=tex, variable=var).place(x=cord[0], y=cord[1])
        cord[0] += 90
    return var


def hint_text(entry="", text=""):
    def s():
        entry.delete(0, END)

    entry.insert(0, text)
    entry.bind("<Button-1>", s)
