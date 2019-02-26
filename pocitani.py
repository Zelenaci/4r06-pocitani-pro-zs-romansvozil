import tkinter as tk
from tkinter import ttk
import random

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Pocitani pro ZS')
        self.master.geometry('300x100')
        self.grid()

        self.options = '+-/*'
        self.status = [0, 0]

        self.gui()
        self.novy_priklad()

    def gui(self):
        #popisek
        self.popisek = tk.Label(self.master, text='Znamenka: ')
        self.popisek.grid(row=0, column=0)

        #vstup znamenek
        self.var_znamenka = tk.StringVar()
        self.var_znamenka.set('+')
        self.znamenka = tk.Entry(self.master, textvariable=self.var_znamenka)
        self.znamenka.bind('<Key-Return>', self.reset_vseho)
        self.znamenka.grid(row=0, column=1)

        #priklad
        self.var_priklad = tk.StringVar()
        self.var_priklad.set(' 0 + 0 ')
        self.priklad = tk.Label(self.master, textvariable=self.var_priklad)
        self.priklad.grid(row=1, column=0)

        #vysledek
        self.var_vysledek = tk.StringVar()
        self.var_priklad.set('0')
        self.vysledek = tk.Entry(self.master, textvariable=self.var_vysledek)
        self.vysledek.bind('<Key-Return>', self.potvrzeni_vysledku)
        self.vysledek.grid(row=1, column=1)

        #spravnost
        self.var_spravnost = tk.StringVar()
        self.uprav_status()
        self.spravnost = tk.Label(self.master, textvariable=self.var_spravnost)
        self.spravnost.grid(row=2, column=1)

    def reset_vseho(self, event):
        self.status = [0, 0]
        self.uprav_status()
        self.novy_priklad()

    def uprav_status(self, event='reset'):
        if event == 'spravne':
            self.status[0] += 1
            self.status[1] += 1
        elif event == 'spatne':
            self.status[1] += 1
        elif event == 'reset':
            self.status = [0, 0]
        spravnost = ' {0} / {1} '.format(self.status[0], self.status[1])
        self.var_spravnost.set(spravnost)

    def potvrzeni_vysledku(self, event):
        try:
            if int(self.var_vysledek.get()) == self.vysledek:
                self.uprav_status('spravne')
            else:
                self.uprav_status('spatne')
            self.novy_priklad()
        except:
            self.var_vysledek.set('')
            print('Neplatne cislo.. ')

    def novy_priklad(self):
        self.var_vysledek.set('')
        znamenka = list(self.var_znamenka.get())
        new_znamenka = []
        for znamenko in znamenka:
            if znamenko in self.options:
                new_znamenka.append(znamenko)
        znamenka = new_znamenka

        if znamenka == []:
            znamenka.append('+')
            self.var_znamenka.set('+')

        nahodny_vyber = random.choice(znamenka)

        if nahodny_vyber == '+':
            a = random.randint(0, 100)
            b = random.randint(0, 100)
            vysledek = a + b

        elif nahodny_vyber == '-':
            a = random.randint(0, 100)
            b = random.randint(0, a)
            vysledek = a - b

        elif nahodny_vyber == '*':
            a = random.randint(0, 10)
            b = random.randint(0, 10)
            vysledek = a * b

        elif nahodny_vyber == '/':
            a = random.randint(0, 10)
            b = random.randint(1, 10)
            a = a * b
            vysledek = a / b

        self.var_priklad.set(' {0} {1} {2} = '.format(a, nahodny_vyber, b))
        self.vysledek = vysledek

master = tk.Tk()
app = Application(master)
app.mainloop()
