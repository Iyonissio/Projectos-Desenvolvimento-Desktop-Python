import tkinter as tk
from tkinter import*
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter.scrolledtext import *
from tkinter import messagebox

import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS Func
                 (nome text, sobrenome text,email text,cargo text,ano text)''')

def add_data(nome,sobrenome,email,cargo,anos):
    c.execute('INSERT INTO Func(nome,sobrenome,email,cargo,ano) VALUES (?,?,?,?,?)',(nome,sobrenome,email,cargo,ano))
    conn.commit()
    conn.close()

def view_all_users():
    c.execute('SELECT * FROM Func')
    data = c.fetchall()
    for row in data:
        tree.insert("",tk.END,values=row)

def get_single_user(nome):
    c.execute('SELECT * FROM Func WHERE nome="{}"'.format(nome))
    data = c.fetchall()
    return data

def clear_text():
    entry_fname.delete('0',END)
    entry_fname2 .delete('0', END)
    entry_fname3.delete('0', END)
    entry_fname4.delete('0', END)
    entry_fname5.delete('0', END)

def add_details():
    nome = str(entry_fname.get())
    sobrenome = str(entry_fname2.get())
    email = str(entry_fname3.get())
    cargo = str(entry_fname4.get())
    ano = str(entry_fname5.get())
    add_data(nome,sobrenome,email,cargo,ano)
    result = '\nNome:{},\nSobrenome:{},\nEmail:{},\nCargo:{},\nAnos:{}'
    tab1_display.insert(tk.END,result)
    messagebox.showinfo(title="Registro Funcionarios", message="Submitterd to Database")

def clear_display_result():
    tab1_display.delete('1.0',END)

def search_user_by_name():
    nome = str(entry_search.get())
    result = get_single_user(nome)
   # tab2_display.insert(tk.END, result)

def clear_display_view():
    tab2_display.delete('1.0', END)

def clear_entered_search():
    entry_search.delete('1.0', END)

window = Tk()
window.title(" SISTEMA DE REGISTRO DE FUNCIONARIOS ")
window.geometry("750x450")

style = ttk.Style(window)
style.configure("lefttab.TNotebook", tabposition='wn')

tab_control = ttk.Notebook(window, style='lefttab.TNotebook')

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)

tab_control.add(tab1, text=f'{"Principal":^20s}')
tab_control.add(tab2, text=f'{"View":^20s}')
tab_control.add(tab3, text=f'{"Pesquisar":^20s}')
tab_control.add(tab4, text=f'{"Export":^20s}')
tab_control.add(tab5, text=f'{"Sobre":^20s}')

tab_control.pack(expand=1,fill="both")

create_table()

label1 = Label(tab1, text= 'Registro de Funcionarios', padx=5, pady=5)
label1.grid(column=0, row=0)

label2 = Label(tab2, text= 'Views', padx=5, pady=5)
label2.grid(column=0, row=0)

label3 = Label(tab3, text= 'Pesquisar', padx=5, pady=5)
label3.grid(column=0, row=0)

label4 = Label(tab4, text= 'Exportar', padx=5, pady=5)
label4.grid(column=0, row=0)

label5 = Label(tab5, text= 'About', padx=5, pady=5)
label5.grid(column=0, row=0)
#___________________________________________________________

l1 = Label(tab1, text="Nome do Funcionario", padx=5, pady=5)
l1.grid(column=0, row=1)
fname_raw_entry = StringVar()
entry_fname = Entry(tab1, textvariable=fname_raw_entry,width=50)
entry_fname.grid(row=1, column=1)

l2 = Label(tab1, text="Sobrenome", padx=5, pady=5)
l2.grid(column=0, row=2)
fname_raw_entry2 = StringVar()
entry_fname2 = Entry(tab1, textvariable=fname_raw_entry2,width=50)
entry_fname2.grid(row=2, column=1)

l3 = Label(tab1, text="Email", padx=5, pady=5)
l3.grid(column=0, row=3)
fname_raw_entry3 = StringVar()
entry_fname3 = Entry(tab1, textvariable=fname_raw_entry3,width=50)
entry_fname3.grid(row=3, column=1)

l4 = Label(tab1, text="Cargo/Funcao", padx=5, pady=5)
l4.grid(column=0, row=4)
fname_raw_entry4 = StringVar()
entry_fname4 = Entry(tab1, textvariable=fname_raw_entry4,width=50)
entry_fname4.grid(row=4, column=1)

l5 = Label(tab1, text="Anos de Servico", padx=5, pady=5)
l5.grid(column=0, row=5)
fname_raw_entry5 = IntVar()
entry_fname5= Entry(tab1, textvariable=fname_raw_entry5,width=50)
entry_fname5.grid(row=5, column=1)

button1 = Button(tab1, text="Add", width=12, bg="#03A9F4", fg="#fff", command=add_data)
button1.grid(row=8, column=0,padx=5, pady=5)

button2 = Button(tab1, text="Clear", width=12, bg="#03A9F4", fg="#fff", command=clear_text)
button2.grid(row=8, column=1,padx=5, pady=5)

#___________________Display Informacoes
tab1_display = ScrolledText(tab1, height=5)
tab1_display.grid(row=10, column=1, padx=5, pady=5, columnspan=3)

button3 = Button(tab1, text="Clear Results", width=12, bg="#03A9F4", fg="#fff", command= clear_display_result)
button3.grid(row=12, column=1,padx=10, pady=10)

#_________________________views
button_V = Button(tab2, text="Ver Todos", width=12, bg="#03A9F4", fg="#fff", command=view_all_users())
button_V.grid(row=1, column=0,padx=10,pady=10)
tree= ttk.Treeview(tab2, column=("column1", "column2","column3","column4", "column5","column6",), show='headings')
tree.heading("#1", text="First Name")
tree.heading("#2", text="First Name")
tree.heading("#3", text="First Name")
tree.heading("#1", text="First Name")
tree.heading("#2", text="First Name")
tree.heading("#3", text="First Name")
tree.grid(row=10, column=0, columnspan=3, padx=5, pady=5)
#________________________Pesquisa___________

label_view1 = Label(tab3, text="Pesquisar Nome Funcionario",padx=5, pady=5 )
label_view1.grid(column=0,row=1)
search_raw_entry = StringVar()
entry_search = Entry(tab3,textvariable=search_raw_entry, width=30)
entry_search.grid(row=1, column=1)

button_view3 = Button(tab3, text="Clear Pesquisas" , width=12, bg="#03A9F4", fg="#fff",command=clear_entered_search)
button_view3.grid(row=2, column=1,padx=10, pady=10)

button_view4 = Button(tab3, text="Clear Results", width=12, bg="#03A9F4", fg="#fff",command=clear_display_result())
button_view4.grid(row=2, column=2,padx=10, pady=10)

button_view5 = Button(tab3, text="Pesquisar", width=12, bg="#03A9F4", fg="#fff", )#command=search_user_by_name())
button_view5.grid(row=1, column=2,padx=10, pady=10)

tab2_display = ScrolledText(tab3, height=5)
tab2_display.grid(row=10, column=0, padx=5, pady=5, columnspan=3)


#________________________________________________________________

window.mainloop()

















