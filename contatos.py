from tkinter import COMMAND, END, Button, Frame, Tk, Label, LabelFrame, Entry,ttk,messagebox
import Banco
import os

pastaApp = os.path.dirname(__file__)

def popular():
    tv.delete(*tv.get_children())
    vquery="SELECT * FROM contatos"
    linhas=Banco.dql(vquery)
    for i in linhas:
        tv.insert("","end",values=i)

def inserir():
    if vnome.get()=="" or vtelefone.get()=="":
        messagebox.showinfo(title="ERRO",message="Digite todos os dados")
        return
    try:
        vquery = "INSERT INTO contatos(nome_contato,telefone_contato,email_contato) VALUES('"+vnome.get()+"','"+vtelefone.get()+"','"+vemail.get()+"')"
        Banco.dml(vquery)
    except:
        messagebox.showinfo(title="ERRO",message="Erro ao inserir")
    popular()
    vnome.delete(0,END)
    vtelefone.delete(0,END)
    vemail.delete(0,END)
    vnome.focus()  


def deletar():
    vid=-1
    itemSelecionado = tv.selection()[0]
    valores=tv.item(itemSelecionado,"values")
    vid=valores[0]
    try:
        vquery="DELETE FROM contatos WHERE id_contato="+vid
        Banco.dml(vquery)
    except:
        messagebox.showerror(title="ERRO",message="Selecione um elemento para ser deletado")
        return
    tv.delete(itemSelecionado)

def pesquisar():
    tv.delete(*tv.get_children())
    vquery = "SELECT * FROM contatos WHERE nome_contato LIKE '%"+vnomepesquisa.get()+"%'"
    linhas = Banco.dql(vquery)
    for i in linhas:
            tv.insert("","end",values=i)

root = Tk()
root.title("Contatos")
root.geometry('580x500')

tv = ttk.Treeview(root,columns=['id','nome','telefone','email'],show='headings')

tv.column('id',minwidth=0,width=30)
tv.heading('id',text='ID')

tv.column('nome',minwidth=0,width=176)
tv.heading('nome',text='NOME')

tv.column('telefone',minwidth=0,width=178)
tv.heading('telefone',text='TELEFONE')

tv.column('email',minwidth=0,width=174)
tv.heading('email',text='EMAIL')
tv.pack()
popular()

fr_quadro1 = LabelFrame(root,
                        borderwidth=1,
                        relief="solid",
                        text="Cadastrar Contato")
fr_quadro1.place(x=10, y=230, width=565, height=90)

lb_nome = Label(fr_quadro1, text="Nome:")
lb_nome.grid(column=0, row=0)
vnome = Entry(fr_quadro1)
vnome.grid(column=1, row=0)

lb_telefone = Label(fr_quadro1, text="Telefone")
lb_telefone.grid(column=2, row=0)
vtelefone = Entry(fr_quadro1)
vtelefone.grid(column=3, row=0)

lb_email = Label(fr_quadro1, text="Email:")
lb_email.grid(column=4, row=0)
vemail = Entry(fr_quadro1)
vemail.grid(column=5, row=0)

confirmar = Button(fr_quadro1,width=10,height=2,text="Cadastrar",command=inserir)
confirmar.grid( column=0,row=1,padx=10)


fr_quadro2 = LabelFrame(root,
                        borderwidth=1,
                        relief="solid",
                        text="Pesquisar Contato")
fr_quadro2.place(x=10, y=320, width=565, height=90)

lb_nome_pesquisa = Label(fr_quadro2, text="Nome:")
lb_nome_pesquisa.grid(column=0, row=0)
vnomepesquisa = Entry(fr_quadro2)
vnomepesquisa.grid(column=1, row=0)

pesquisar = Button(fr_quadro2,width=10,height=2,text="Pesquisar",command=pesquisar)
pesquisar.grid(column=3,row=0,padx=10)

confirmar = Button(fr_quadro2,width=10,height=2,text="Mostrar Tudo",command=popular)
confirmar.grid(column=4,row=0,padx=10)

deletar = Button(root,width=10,height=2,text="Deletar",command=deletar)
deletar.place(x=100,y=420)

root.mainloop()