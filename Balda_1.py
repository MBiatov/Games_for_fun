from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Balda")

textframe = Frame(root)   #фрейм с самой игрой, с ячейками
textframe.grid(row = 1, column = 1)
textfram1 = Frame(root) #фрейм со списками, куда выводятся слова и очки за каждео
textfram1.grid(row = 1, column = 2)


def go_balda():
    '''функция которая запускает игру, при стандартных настройках поля 5*5
    и собственно формирует само поле
    '''
    global HAND_SIZE  #глобально заданна сторона
    HAND_SIZE = 5
    lab1.destroy()  #убирает название игры
    a=[]
    for r in range(HAND_SIZE):
        a.append([])
        for c in range(HAND_SIZE):
            a[r].append(cell(r,c))

def setting():
    '''Функция настроек:
    вводится начальное слово и оно определяет размер поля
    должна менять размер поля, пока что может только увеличивать размер поля
    еще нужно как-то выводить начальное слово, но пока что, хз как
    '''
    win = Toplevel()  #создание всплывающего окна
    win.geometry()
    win.title('Choose your word')
    ent = Entry(win, width = 15, font=("Verdana", 10))  #поле для ввода стартового слова
    lab2 = Label(win, text = 'Add the word you want to start with: ', font=("Verdana", 10), background="#555", foreground="#ccc")  #подпись только надо вводить сразу число
    but1 = Button(win, text = 'Insert new value of field:', font=("Verdana", 10))   #кнопка изменения поля
    but2 = Button(win, text = 'Close', font=("Verdana", 10))   #закрытия окна

    but1.grid(row = 3, column = 1)
    but2.grid(row = 3, column = 3)
    lab2.grid(row = 2, column = 0,  columnspan = 2)
    ent.grid(row = 2,column = 3,  columnspan = 4)
    def handy(event):
        '''функция меняет размер самого поля и создает на месте старого большее поле
        работает только на увеличение размера
        '''

        ro = ent.get()
        rol = 0
        for l in ro:
            if l in 'абвгдеёжзийклмнопрстухфцщшыъьэюя':
                rol=len(ent.get())

        HAND_SIZE = rol
        a=[]
        for r in range(HAND_SIZE):
            a.append([])
            for c in range(HAND_SIZE):
                a[r].append(cell(r,c))


    def win_destroy(event):  #закрытие окна
        win.destroy()


    but1.bind('<Button-1>', handy)
    but2.bind('<Button-1>', win_destroy)
    ent.bind('<Return>', handy)




def message():   #всплывающее сообщение о игре и разработчике :)
    messagebox.showinfo('Something about this game :)' , ' Lolols' )

def quit():
    '''выход из игры, с всплывающим сообщение, о возможности отменить свой выбор
    '''
    mes = messagebox.askyesno('Are you sure?', 'Are you sure?')
    if mes == True:
        root.destroy()

m = Menu(root)  #верхние окошки меню
root.config(menu=m)
fm = Menu(activebackground = 'green', font=("Verdana", 10), tearoff=0, background="#555", foreground="#ccc")
fm1 = Menu(activebackground = 'green', font=("Verdana", 10), tearoff=0, background="#555", foreground="#ccc")
fm2 = Menu(activebackground = 'green', font=("Verdana", 10), tearoff=0, background="#555", foreground="#ccc")
m.add_cascade(label = 'New', menu = fm)
fm.add_command(label = 'New', command = go_balda)
fm.add_command(label = 'Settings', command = setting)
#fm.add_separator()
m.add_cascade(label="About", menu = fm2)
fm2.add_command(label="About", command=message)
m.add_cascade(label="Quit", menu = fm1)
fm1.add_command(label="Quit", command=quit)

lab1 = Label(root, text = 'BALDA!', font = ('Bodoni MT Black', 40 ), padx = 10, pady = 10)  #начальная эмблемка

lab1.grid( row = 1, column = 1)


m0 = 34 # размер ячеек

class cell():  #класс, который работает не совсем мне понятно:)
    def __init__(self, r, c): # при создании указываем номер строки и столбца, в который помещаем
        global list0   #списки глобальны, что бы я мог к ним обратится с верхнего окна
        global list1    #чудом работает
        list0 = Listbox(textfram1, height = HAND_SIZE*2, width =HAND_SIZE+10)
        list1 = Listbox(textfram1, height = HAND_SIZE*2, width =HAND_SIZE+10)
        self.lab1 = Label(textfram1, text = 'Player 1')
        self.scrl1 = Scrollbar(textfram1, command = list0.yview)
        self.scrl2 = Scrollbar(textfram1, command = list1.yview)
        self.lab2 = Label(textfram1, text = 'Player 2')
        self.r = r # Номер сторки в двумерном списке.
        self.c = c # Номер столбца ...
        self.let = Entry(textframe, width = 2, font = "Arial " + str(m0//2))
        global mas  #масив для вывода слов в списки
        mas = []
        global s1   #масив для подсчета очков за каждое слово
        s1 = []
        global s2   #масив для подсчета очков за каждое слово
        s2 = []
        global labe1    #вывод общегл кол-ва очков
        global labe2
        labe1 = Label(textfram1, font = "Arial " + str(m0//4))
        labe2 = Label(textfram1, font = "Arial " + str(m0//4))

        labe1.grid(row = 2, column = 1)
        labe2.grid(row = 2, column = 3)

        self.let.grid(row=r,column = c)
        self.let.bind('<Return>', self.doit)
        self.lab = Label(textframe, width = 2, font = "Arial " + str(m0//2))
        #self.paint()
        self.scrl1.grid(row = 1, column = 1, sticky ='e', ipady = 55)
        self.lab1.grid(row = 0, column = 1)
        list0.grid(row = 1, column = 1)
        self.scrl2.grid(row = 1, column = 3, sticky = 'e', ipady = 55)
        self.lab2.grid(row = 0, column = 3)
        list1.grid(row = 1, column = 3)
    def doit(self, event):
        '''функция ввода букв в ячейки, по нажатия энтр поверх выбранной ячейки создает лейбл, с буквой введеной в нее
        принимает буквы только русского алфавита
        '''
        if self.let.get() in 'абвгдеёжзийклмнопрстухфцщшыъьэюя': #проверка на алфавит
            self.lab.configure(text = self.let.get())
            self.lab.grid(row = self.r, column = self.c)
            win = Toplevel()  #создание окна для ввода построенного слова
            win.geometry()
            win.title('Add your word to the list')
            ent = Entry(win, width = 15, font = "Arial " + str(m0//2))
            ent.grid(row = 2,column = 1,  columnspan = 2)
            var=IntVar()   #метки для выбор какой игрок вводит слово
            var.set(1)      #по умолчанию 1ый

            check1 = Radiobutton(win, text = 'Player 1', value = 1, variable = var, padx = 15, pady = 10)
            check2 = Radiobutton(win, text = 'Player 2', value = 2, variable = var, padx = 15, pady = 10)

            check1.grid(row = 1, column = 1)
            check2.grid(row = 1, column = 2)
            def leftkey(event):
                var.set(1)
            def rightkey(event):  #смена метки
                var.set(2)
            win.bind('<Left>', leftkey)
            win.bind('<Right>', rightkey)


            def adding( *args):   #добавление слова в список
                mas.append(ent.get())

                #print(ent.get())
                if var.get() == 1:
                    list0.insert(END,  str(mas[-1]) + ' - ' + str(len(mas[-1])))
                    #print(mas, ent.get())
                    s1.append(len(mas[-1]))
                    labe1.configure(text = 'Total score = ' + str(sum(s1)))

                else:
                    list1.insert(END, str(mas[-1]) + ' - '  + str(len(mas[-1])))
                    s2.append(len(mas[-1]))
                    labe2.configure(text = 'Total score = ' + str(sum(s2)))
                win.destroy()

            ent.bind('<Return>', adding)
        else:
            self.let.delete(0, END)



'''
a = []
for r in range(HAND_SIZE): # n строк
    a.append([]) # создаем пустую строку
    for c in range(HAND_SIZE): # в каждой строке - n элементов
        a[r].append(cell(r,c)) # добавляем очередной элемент в строку
'''

root.mainloop()