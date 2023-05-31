from tkinter import COMMAND, END, Button, Frame, Tk, Label, LabelFrame, Entry,messagebox
import Banco
import os

pastaApp = os.path.dirname(__file__)

def gravarDados():
    if (tb_nome.get()) and (tb_telefone.get()) and (tb_cpf.get()) and (tb_email.get()) and (tb_senha.get()) and (tb_csenha.get()) and (tb_endereco.get()) and (tb_numero.get()) and (tb_complemento.get()) and (tb_cep.get()) and (tb_bairro.get()) and (tb_senha.get() == tb_csenha.get()) != "" :
        vnome = tb_nome.get()
        vtelefone = tb_telefone.get()
        vcpf = tb_cpf.get()
        vemail = tb_email.get()
        vsenha = tb_senha.get()
        vcsenha = tb_csenha.get()
        vendereco = tb_endereco.get()
        vnumero = tb_numero.get()
        vcomplemento = tb_complemento.get()
        vcep = tb_cep.get()
        vbairro = tb_bairro.get()
        vquery = "INSERT INTO cadastro (nome_cadastro,telefone_cadastro,cpf_cadastro,email_cadastro,senha_cadastro,csenha_cadastro,endereco_cadastro,numero_cadastro,complemento_cadastro,cep_cadastro,bairro_cadastro) VALUES('"+vnome+"','"+vtelefone+"','"+vcpf+"','"+vemail+"','"+vsenha+"','"+vcsenha+"','"+vendereco+"','"+vnumero+"','"+vcomplemento+"','"+vcep+"','"+vbairro+"')"
        Banco.dml(vquery)
        tb_nome.delete(0,END)
        tb_telefone.delete(0,END)
        tb_cpf.delete(0,END)
        tb_email.delete(0,END)
        tb_senha.delete(0,END)
        tb_csenha.delete(0,END)
        tb_endereco.delete(0,END)
        tb_numero.delete(0,END)
        tb_complemento.delete(0,END)
        tb_cep.delete(0,END)
        tb_bairro.delete(0,END)
        messagebox.showinfo("Mensagem de Confirmacao","todos os dados foram cadastrados")
    else:
        messagebox.showerror("Mensagem de Erro","Confira se todos os campos foram preenchidos e Confira a senha")

def teste():
    gravarDados()

root = Tk()
root.title("Formulario")
root.geometry('530x400')

fr_quadro1 = LabelFrame(root,
                        borderwidth=1,
                        relief="solid",
                        text="Dados Pessoais")
fr_quadro1.place(x=10, y=10, width=490, height=90)


lb_nome = Label(fr_quadro1, text="Nome:")
lb_nome.grid(column=0, row=0)
tb_nome = Entry(fr_quadro1)
tb_nome.grid(column=1, row=0)

lb_telefone = Label(fr_quadro1, text="Telefone")
lb_telefone.grid(column=2, row=0)
tb_telefone = Entry(fr_quadro1)
tb_telefone.grid(column=3, row=0)

lb_cpf = Label(fr_quadro1, text="CPF:")
lb_cpf.grid(column=0, row=1)
tb_cpf = Entry(fr_quadro1)
tb_cpf.grid(column=1, row=1)

lb_email = Label(fr_quadro1, text="Email:")
lb_email.grid(column=2, row=1)
tb_email = Entry(fr_quadro1)
tb_email.grid(column=3, row=1)

lb_senha = Label(fr_quadro1, text="Senha:")
lb_senha.grid(column=0, row=2)
tb_senha = Entry(fr_quadro1)
tb_senha.grid(column=1, row=2)

lb_csenha = Label(fr_quadro1, text="Confirmar Senha:")
lb_csenha.grid(column=2, row=2)
tb_csenha = Entry(fr_quadro1)
tb_csenha.grid(column=3, row=2)

fr_quadro2 = LabelFrame(root,
                        borderwidth=1,
                        relief="solid",
                        text="Dados Residenciais")
fr_quadro2.place(x=10, y=100, width=490, height=65)

lb_endereco = Label(fr_quadro2, text="Endereco:")
lb_endereco.grid(column=0, row=0)
tb_endereco = Entry(fr_quadro2)
tb_endereco.grid(column=1, row=0)

lb_numero= Label(fr_quadro2, text="Numero:")
lb_numero.grid(column=2, row=0)
tb_numero = Entry(fr_quadro2,width=10)
tb_numero.grid(column=3, row=0)

lb_complemento= Label(fr_quadro2, text="Complemento:")
lb_complemento.grid(column=4, row=0)
tb_complemento = Entry(fr_quadro2,width=15)
tb_complemento.grid(column=5, row=0)

lb_cep = Label(fr_quadro2, text="CEP:")
lb_cep.grid(column=0, row=1)
tb_cep = Entry(fr_quadro2)
tb_cep.grid(column=1, row=1)

lb_bairro = Label(fr_quadro2, text="Bairro:")
lb_bairro.grid(column=2, row=1)
tb_bairro = Entry(fr_quadro2,width=10)
tb_bairro.grid(column=3, row=1)

confirmar = Button (root,width=5,height=2,text="gravar",command=teste)
confirmar.place(x=10,y=180)



root.mainloop()

