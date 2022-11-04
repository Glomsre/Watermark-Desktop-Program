from tkinter import *
from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog


name_new_image = "new-image.png"


def edit_text():
    global f
    global name_new_image

    current_image = Image.open(f)
    current_image = current_image.resize((400, 320))

    my_font = ImageFont.truetype("arial.ttf", 11)
    my_text = input_text.get()
    edit_image = ImageDraw.Draw(current_image)
    edit_image.text((11, 11), my_text, fill=(0, 0, 0), font=my_font)
    current_image.show()
    current_image.save(name_new_image)
    input_text.delete(0, END)
    msg_status()


def msg_status():
    label_info.config(text=f'The {name_new_image} was saved successfully')
    label_img.config(image='')
    window.after(3000, window.destroy)


def upload_image():
    filename = filedialog.askopenfilename(title='Open')
    return filename


f = upload_image()

window = Tk()
window.title("Image Watermark App")
window.config(padx=30, pady=30)

label_info = Label(text='')
label_info.grid(row=0, columnspan=6, pady=(10, 10))


img_file = PhotoImage(file=f)
label_img = Label(window, image=img_file)
label_img.grid(row=1, columnspan=6)


label_text = Label(text='Enter your logo/name or website')
label_text.grid(row=2, columnspan=6, pady=(10, 10))
input_text = Entry(window, width=30)
input_text.grid(row=3, columnspan=6, pady=(10, 10))


button_entry = Button(window, text='Add Text',
                      bg='white',
                      fg='blue',
                      activebackground='lightblue',
                      command=edit_text)
button_entry.grid(row=4, columnspan=6, pady=(10, 10))


window.mainloop()
