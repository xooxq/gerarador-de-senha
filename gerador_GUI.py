import customtkinter as ct
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choice

#aqui estou definindo o tema do GUI. Tem disponíveis: dark blue, blue, green
ct.set_default_color_theme("green")

win=ct.CTk()
win.geometry("350x220")
win.title("Gerar Senha")
win.resizable(False, False)
#caso você não abaixar também o .ico que tá no meu git e colocar no mesmo lugar do .py, o sctript vai dar erro. Para resolver, você pode excluir o "win.iconbitmap()" ou passar o diretório do seu .ico
#win.iconbitmap()

def criar_senha(x=None):
    info = entry.get()
    #fazendo a verificação para que retorne um erro caso o user confirme um dado vazio.
    if not info.strip():
        msg_erro.configure(text="Este campo não pode ficar vazio.")
        msg_erro.place(x=73,y=42)
    else:
        try:
            x=int(info)
        except:
            #tratando a possibilidade do user digitar uma letra ou qualquer outra coisa menos um número inteiro (int)
            msg_erro.configure(text="Ensira apenas números.")
            msg_erro.place(x=100,y=42)
            return 0
        msg_erro.configure(text="")

        #na variável senha, tá contendo caracteres minusculo, maiúsculo, números e caracter especiais.
        senha = ascii_lowercase+ascii_uppercase+digits+punctuation
        lista_senha = []

        for numero in range(x):
            lista_senha.append(choice(senha))

        #aqui, coloquei a variável de "bloco" pois tava sem inspiração pra nomeKKKKKK
        bloco = ct.CTkTextbox(win, width=200, height=100, fg_color="dark cyan")
        bloco.insert("end", f"Sua senha: {''.join(lista_senha)}")
        bloco.configure(state="disabled")
        bloco.place(x=75,y=60)

def sair():
    #fecha a GUI
    win.quit()

entry = ct.CTkEntry(win, width=200, height=20, placeholder_text="Digitos para a senha", fg_color="dark cyan",
                    border_color="dark cyan")
entry.pack(pady=20)

#aqui não quis colocar a posição da mensagem de erro, pois já que em diferentes tipos de erro no script (que são apenas dois) tem diferentes posições (apenas muda o "x=")
msg_erro = ct.CTkLabel(win, text="", text_color="red", font=("Arial", 14))

btn=ct.CTkButton(win, width=30, height=25, text="Confirmar", command=criar_senha,
                fg_color="dark cyan").place(x=140,y=180)
#aqui coloquei para que, quando criar no "enter", ser a mesma coisa do que clicar no botão de confirmar.
win.bind("<Return>", criar_senha)

#o btn e btn_sair, tem o width diferente, porque o tamanho do seu caracter (o texto que você definiu) altera o width 
btn_sair=ct.CTkButton(win, width=60, height=25, text="Sair", command=sair,
                    fg_color="dark red").place(x=285,y=190)
win.mainloop()