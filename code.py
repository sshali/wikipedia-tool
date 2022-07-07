from tkinter import *
from tkinter import ttk

import googletrans
import pyperclip
import wikipedia


# coded by kc emma
# A python programmer


def search():
    question = my_entry.get()
    language = combobox.get()
    wikipedia.set_lang('en')  # setting the default language to English Language
    for k, v in lang_dict.items():
        if language == v:
            wikipedia.set_lang(k)
    textarea.delete(0.0, END)
    page = wikipedia.page(question)
    textarea.config(state=NORMAL)
    textarea.insert(END, page.content)
    textarea.config(state=DISABLED)


def edit():
    textarea.config(state=NORMAL)


def copy():
    content = textarea.get(0.0, END)
    pyperclip.copy(content)


def clear():
    textarea.config(state=NORMAL)
    textarea.delete(0.0, END)
    textarea.config(state=DISABLED)
    my_entry.delete(0, END)

    combobox.set('Select Language')


lang_dict = googletrans.LANGUAGES

root = Tk()

root.geometry('700x670+200+10')
root.title('Wikipedia Search Bar')

root.config(bg='red4')

my_label = LabelFrame(root, text='Search Wikipedia', bg='red')
my_label.pack(pady=20, padx=22)

my_entry = Entry(my_label, font=('arial', 20, 'bold'))
my_entry.pack(pady=10, padx=20)

combobox = ttk.Combobox(my_label, font=('times new roman ', 20, 'bold'), justify=CENTER, width=15, state='readalone')
combobox.pack()

combobox['values'] = [e for e in lang_dict.values()]
combobox.set('Select Language')

search_box = Button(my_label, text='SEARCH', font=('Helvetica', 20, 'bold'), command=search)
search_box.pack(padx=20, pady=10)

my_frame = Frame(my_label)
my_frame.pack(pady=5)

# text_scroll bar
text_scrol = Scrollbar(my_frame)
text_scrol.pack(side=RIGHT, fill=Y)

# text area
textarea = Text(my_frame, yscrollcommand=text_scrol.set, wrap='word',
                font=('Helvetica', 20), height=12, bg='red4', fg='white', state=DISABLED)
textarea.pack()

# making the scroll bar to be align with the text_bar
text_scrol.config(command=textarea.yview)

button_frame = Frame(my_label, bg='red4')
button_frame.pack()

# clear button
clear_button = Button(button_frame, text='CLEAR', font=('Helvetica', 20, 'bold'), bg='red4', fg='white', command=clear)
clear_button.grid(row=0, column=0, padx=0)

# copy button
copy_button = Button(button_frame, text='COPY', font=('Helvetica', 20, 'bold'), fg='white', bg='red4', command=copy)
copy_button.grid(row=0, column=1, padx=20)

# clear button
clear_button = Button(button_frame, text='EDIT', font=('Helvetica', 20, 'bold'), fg='white', bg='red4', command=edit)
clear_button.grid(row=0, column=3, padx=20)

root.mainloop()
