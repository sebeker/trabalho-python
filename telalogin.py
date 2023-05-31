import os
from sqlite3 import Cursor
from tkinter import COMMAND, END, Button, Frame, Tk, Label, LabelFrame, Entry, ttk,messagebox
import Banco

pastaApp = os.path.dirname(__file__)

def cadastrar():
    exec(open(pastaApp+"//formulario.py").read())

def entrar():
    nome = tb_login.get()
    senha = tb_senha.get()
    try:
        vquery = ("SELECT senha_cadastro FROM cadastro WHERE nome_cadastro = '{}'".format(nome))
        linhas = Banco.dql(vquery)
    except:
        messagebox.showerror("ERROR","Login ou senha invalida")

    if senha == linhas[0][0]:
        import contatos
        exec(open(pastaApp+"//contatos.py").read())
    else:
        messagebox.showerror("ERROR","Login ou Senha invalida")

if __name__ == "__main__":

    root = Tk()
    root.title("Tela de Login")
    root.geometry('530x400')

    lb_login = Label(root, text="Login:")
    lb_login.pack()
    tb_login = Entry(root)
    tb_login.pack()

    lb_senha = Label(root, text="Senha:")
    lb_senha.pack()
    tb_senha = Entry(root,show="*")
    tb_senha.pack()

    logar = Button (root,width=5,height=2,text="Logar",command=entrar)
    logar.pack()

    cadastrar = Button (root,width=8,height=2,padx=10,text="Cadrastar",command=cadastrar)
    cadastrar.pack()


    root.mainloop()