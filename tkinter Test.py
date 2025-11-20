from tkinter import *
from cryptography.fernet import Fernet

def generate_fernet_key(generate_key_input: Entry):
    generated_fernet_key = Fernet.generate_key()
    generate_key_input.insert(0, generated_fernet_key.decode())
    

app = Tk()
app.title('Tkinter Test')
app.geometry('512x256')
app_frame = Frame(app)
app_frame.pack(fill=BOTH, expand=True)

generate_key_label = Label(app_frame, text='Generate Fernet Key')
generate_key_label.pack()
generate_key_input = Entry(app_frame)
generate_key_input.pack()
generate_key_button = Button(app_frame, text='Generate', command=lambda: generate_fernet_key(generate_key_input))
generate_key_button.pack()

app.mainloop()