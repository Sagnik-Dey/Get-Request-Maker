from tkinter import *
import requests
from html5print import HTMLBeautifier

def send_req():
    url = entry0.get()
    entry1.delete(1.0, END)

    if (url != ""):
        try:
            response = requests.get(url)

        except Exception as error:
            entry1.insert(END, error)
        
        else:
            status_label.config(text="Status : " + str(response.status_code))

            content_label.config(text="Content-Type : " +
                                 response.headers["Content-type"])

            if (response.headers["Content-type"] == "text/html; charset=ISO-8859-1"):
                html_content = HTMLBeautifier.beautify(response.content)
                entry1.config(wrap=NONE)
            else:
                html_content = response.text
                entry1.config(wrap=WORD)

            entry1.insert(END, html_content)

    else:
        entry1.insert(END, "Enter an url to send request !")
        status_label.config(text="Status ")
        content_label.config(text="Content-Type ")


def create_window():
    # TODO: Make the variables global
    global entry0, status_label, content_label, entry1

    window = Tk()

    window.title("API Tester - Get Request Maker")
    window.geometry("700x628+200+20")
    window.configure(bg="#ffffff")

    canvas = Canvas(
        window,
        bg="#ffffff",
        height=628,
        width=700,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"background.png")
    background = canvas.create_image(
        350.0, 314.0,
        image=background_img)

    canvas.create_text(
        58.0, 225.5,
        text="Url",
        fill="#000000",
        font=("Poppins-Regular", int(15.0)))

    canvas.create_text(
        176.5, 161.0,
        text="Make Get Requests :",
        fill="#48abe3",
        font=("Poppins", int(20.0), "bold"))

    canvas.create_text(
        93.5, 370.0,
        text="Result :",
        fill="#48abe3",
        font=("Poppins", int(20.0), "bold"))

    entry0_img = PhotoImage(file=f"img_textBox0.png")
    entry0_bg = canvas.create_image(
        378.0, 229.0,
        image=entry0_img)

    entry0 = Entry(
        bd=0,
        bg="#c4c4c4",
        highlightthickness=0,
        font=("Poppins", 13))

    entry0.place(
        x=107.0, y=214,
        width=542.0,
        height=28)

    img0 = PhotoImage(file=f"img0.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=send_req,
        relief="flat")

    b0.place(
        x=48, y=272,
        width=611,
        height=35)

    entry1_img = PhotoImage(file=f"img_textBox1.png")
    entry1_bg = canvas.create_image(
        349.0, 520.0,
        image=entry1_img)

    entry1 = Text(
        bd=0,
        bg="#c4c4c4",
        highlightthickness=0,
        font=("Poppins", 13),
        wrap=NONE)

    entry1.place(
        x=49.0, y=431,
        width=600.0,
        height=176)

    canvas.create_rectangle(
        0, 335, 0+700, 335+1,
        fill="#2f96cf",
        outline="")

    canvas.create_text(
        350.5, 47.0,
        text="Test Your Api ",
        fill="#0057ff",
        font=("Courgette", int(30.0)))

    status_label = Label(
        text="Status",
        foreground="#000000",
        font=("Poppins", int(15.0), "bold"),
        background="#DFDFDF")
    status_label.place(x=73.5, y=392)

    content_label = Label(
        text="Content-Type",
        foreground="#000000",
        font=("Poppins", int(15.0), "bold"),
        background="#DFDFDF")
    content_label.place(x=247.0,  y=392)

    window.resizable(False, False)
    window.mainloop()


if __name__ == "__main__":
    create_window()
