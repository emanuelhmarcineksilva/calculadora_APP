# importanto tkinter
from tkinter import *
from tkinter import ttk

# Cores
cor1 = "#3b3b3b" # black/preta 
cor2 = "#feffff" # white/branca 
cor3 = "#38576b" # Azul carregado 
cor4 = "#ECEFF1" # cizenta 
cor5 = "#FFAB40" # Orange/laranja

# Esse "Tk()" vem do "tkinter" qeu foi importado.
janela =Tk()
janela.title("Calculadora")
# Largura e altura da janela.
janela.geometry("235x310")
# Colocando cor na janela.
# O código'config' altera a configuração do que inserir dentro dos parenteses.
janela.config(bg=cor1)

# Dividindo a tela usando Frame.
# O código frame pede os atributos, Nome (do que vai dividir), largura, altura.
# O código 'bg' é o backgraund.
frame_janela = Frame(janela, width=235, height=50, bg=cor3)
# Faz alguma ação nas linas 0 (primeira) e coluna 0 (primeira).
frame_janela.grid(row=0, column=0)

# Segundo frame.
frame_corpo = Frame(janela, width=235, height=260)
frame_corpo.grid(row=1, column=0)


# Variavel todos valores.
todos_valores = ''

# Criando um função
# O 'event' recebe um valor que pode ser posto nas ativações dessa função.
def entrar_valores(event):

    # Colocando 'global' na frente de uma variavel criamos uma variavel global, e assim os valores que ela porarserão os mesmos onde ela for colocada.
    global todos_valores

    # O código 'str()' define o que estiver dentro dela como uma string. Pois o código 'eval' só aceita string.
    todos_valores = todos_valores + str(event)

    #passando valor para label
    # O código 'set' vai atribuir ou configurar um valor a uma propriedade ou variável de um objeto
    valor_texto.set(todos_valores)



# Criando label.
# Aqui será criada a caixa de resposta.

# O código 'padx=' é um padding (espaçamento interno) no eixo da abissisa (x).
# O código 'pady=' é um padding (espaçamento interno) no eixo da ordenada (y).
# O código 'relief=FLAT' é para deixar a label toda lisa.
# O código 'anchor' deixa o texto fixo em um lado e o "e" é como se fosse o exit para deixar no final.
# O código 'justify=RIGHT' passa tudo para a direita.
# O código 'fg=' define a cor do texto.
# O código 'StringVar()' cria uma varivel de valor string, que ira receber um valor variavel.
# O código 'textvariable=' permite que os valores dele sejam alterados dinamicamente.
valor_texto = StringVar()
app_label = Label(frame_janela, textvariable=valor_texto, width=14, height=1, padx=5, pady=7, font=('Ivy 20'), relief=FLAT, anchor="e", justify=RIGHT, bg=cor3, fg=cor2)
app_label.place(x=0, y=0)


# Fazendo os botões.

# O código 'Button()' é porque estamos criando um botão, dento dos parenteses colocamos os parametros, onde ele vai estar que será no 'frame_corpo', e em seguidas outros parametros definindo o que qeuremos.
# O código 'font=()' define a fonte que será a 'Ivy', o tamanho que será 13q, e podera definir se estará em negrito com 'bold'.
# O código 'relief=' define o estilo que será um que da a impreção que o botão sobe um pouco para frente, o RAISED, se você escrever sem as aspas deixe o nome com todas as letras maiúsculas, se for com as aspas deixe com as letras minúsculas.
# O código 'overrelief' faz com que o botão execute uma ação quando o mouse passar por cima do botão, que no caso é a RIDGE.
b_1 = Button(frame_corpo, height=2, width=11, text="C", bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
# O código 'place()' indica onde estara a posição na tela indicada.
b_1.place(x=0, y=0)
# O código 'command' executa o código quando uma ação é feita, exemplo, quando apertão o botão.
# o código 'lambda' nos permite executar codigos em uma única linha, ela cria uma função anonima.
b_2 = Button(frame_corpo, height=2, width=5, command= lambda: entrar_valores('%'), text="%", bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=120, y=0)
b_3 = Button(frame_corpo, height=2, width=5, command= lambda: entrar_valores('/'), text="/", bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=180, y=0)

b_4 = Button(frame_corpo, height=2, width=5, command= lambda: entrar_valores('7'), text="7", bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_corpo, height=2, width=5, command= lambda: entrar_valores('8'), text="8", bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=52)
b_6 = Button(frame_corpo, height=2, width=5, command= lambda: entrar_valores('9'), text="9", bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=120, y=52)
b_7 = Button(frame_corpo, height=2, width=5, command= lambda: entrar_valores('*'), text="*", bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=180, y=52)

b_8 = Button(frame_corpo, height=2, width=5, command= lambda: entrar_valores('4'), text="4", bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_corpo, height=2, width=5, command= lambda: entrar_valores('5'), text="5", bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=60, y=104)
b_10 = Button(frame_corpo, height=2, width=5, command= lambda: entrar_valores('6'), text="6", bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=120, y=104)
b_11 = Button(frame_corpo, height=2, width=5, command= lambda: entrar_valores('-'), text="-", bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=180, y=104)


b_12 = Button(frame_corpo, height=2, width=5, command= lambda: entrar_valores('1'), text="1", bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_corpo, height=2, width=5, command= lambda: entrar_valores('3'), text="3", bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=60, y=156)
b_14 = Button(frame_corpo, height=2, width=5, command= lambda: entrar_valores('4'), text="4", bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=120, y=156)
b_15 = Button(frame_corpo, height=2, width=5, command= lambda: entrar_valores('+'), text="+", bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=180, y=156)

b_16 = Button(frame_corpo, height=2, width=11, command= lambda: entrar_valores('0'), text="0", bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_corpo, height=2, width=5, command= lambda: entrar_valores('.'), text=".", bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=120, y=208)
b_18 = Button(frame_corpo, height=2, width=5, command= lambda: entrar_valores('='), text="=", bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=180, y=208)

# Configurando os calculos
# O código 'eval()' resolve calculos que são passados para dentro dela.
a = eval('8/2')
print(a)
# o resultado aparece no terminal


janela.mainloop()
