import tkinter as tk
from tkinter import messagebox


def adicionar():
    try:
        resultado.set(float(entrada1.get()) + float(entrada2.get()))
    except ValueError:
        messagebox.showerror("erro","por favor, insira numeros validos.")

def subitrair():
    try:
        resultado.set(float(entrada1.get()) - float(entrada2.get()))
    except ValueError:
        messagebox.showerror('erro','por favor, insira numeros validos.')

def multiplicacao():
    try:
        resultado.set(float(entrada1.get()) * float(entrada2.get()))
    except ValueError:
        messagebox.showerror('erro','por favor, insira numeros validos.')

def divisao():
    try:
        if float(entrada2.get()) == 0:
            raise ZeroDivisionError
        resultado.set(float(entrada1.get()) / float(entrada2.get()))
    except ValueError:
        messagebox.showerror('erro', 'por favor, insira numeros validos.')
    except ZeroDivisionError:
        messagebox.showerror('erro','divisão por zero não é permitido')



root = tk.Tk()

root.title('calculadora hackeada')

entrada1 = tk.StringVar()
entrada2 = tk.StringVar()
resultado = tk.StringVar()

tk.Label(root,text='primeiro numero: ').grid(row=0, column=0)
tk.Entry(root,textvariable=entrada1).grid(row=0, column=1)


tk.Label(root,text='segundo numero: ').grid(row=1, column=0)
tk.Entry(root,textvariable=entrada2).grid(row=1, column=1)
button_style = {
    'font': ('Arial', 16),
    'bg': "#4caf50",
    'fg': '#ffffff',
    "relief": "raised",
    'bd': 3,
    'width': 1,
    'height': 1,
}

tk.Button(root,text='+', command=adicionar, **button_style).grid(row=0, column=2)
tk.Button(root,text='-', command=subitrair, **button_style).grid(row=0, column=3)
tk.Button(root,text='x', command=multiplicacao, **button_style).grid(row=1, column=2)
tk.Button(root,text=':', command=divisao, **button_style).grid(row=1, column=3)

tk.Label(root, text='resultado: ').grid(row=2,column=0)
tk.Entry(root, textvariable=resultado, state='readonly').grid(row=3, column=1)

root.mainloop()