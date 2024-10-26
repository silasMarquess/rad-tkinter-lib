from tkinter import *;
from tkinter import ttk;
from asteval import Interpreter;

color={
    'bg-primary-color':'#222222',
    'bg-buttons-color':'#414141'
}

class MainForm():
    def __init__(self) -> None:
        self.root =  Tk();
        self.SetTitle();
        self.CreateFrame();
        self.CreateButtons();
        self.CreateInput();
        self.root.mainloop();
        pass

    def SetTitle(self):
       self.root.title('Titulo da Janela')
       self.root.configure(background='#800080')
       self.root.geometry('560x600')
       self.root.resizable(True,True)

    def CreateFrame(self):
        self.frame1 = Frame(self.root,border=2,bg=color['bg-primary-color'])
        self.frame1.place(relx=0.10, rely=0.10,relwidth=0.8, relheight=0.8)
    
    def CreateButtons(self):
        #configurar Style
        self.style = ttk.Style();
        self.style.configure('HoverButton',font=('Roboto',15))

        self.style.map("HoverButton",
                       background=[("active", color['bg-primary-color'])],  # Cor ao passar o mouse
                       relief=[("pressed", "sunken"), ("!pressed", "raised")]) 
        
        #LINHA 01
        self.button_soma = Button(self.frame1,text='+',border=0,bg=color['bg-buttons-color'],fg='white', command=lambda : self.inputVisio.insert(END,'+'))
        self.button_soma.place(relx=0, rely=0.167,relwidth=0.25, relheight=0.167)

        self.button_sub = Button(self.frame1,text='-',highlightthickness=0,bg=color['bg-buttons-color'],fg='white',command=lambda : self.inputVisio.insert(END,'-'))
        self.button_sub.place(relx=0.25, rely=0.167,relwidth=0.25, relheight=0.167)

        self.button_mult = Button(self.frame1,text='*',border=0,bg=color['bg-buttons-color'],fg='white',command=lambda : self.inputVisio.insert(END,'*'))
        self.button_mult.place(relx=0.50, rely=0.167,relwidth=0.25, relheight=0.167)

        self.button_div = Button(self.frame1,text='/',border=0,bg=color['bg-buttons-color'],fg='white',command=lambda : self.inputVisio.insert(END,'/'))
        self.button_div.place(relx=0.75, rely=0.167,relwidth=0.25, relheight=0.167)

        #LINHA 02
        self.button_7 = Button(self.frame1,text='7',border=0,bg=color['bg-buttons-color'],fg='white',command=lambda : self.inputVisio.insert(END,'7'))
        self.button_7.place(relx=0, rely=0.32,relwidth=0.25, relheight=0.167)

        self.button_8 = Button(self.frame1,text='8',border=0,bg=color['bg-buttons-color'],fg='white',command=lambda : self.inputVisio.insert(END,'8'))
        self.button_8.place(relx=0.25, rely=0.32,relwidth=0.25, relheight=0.167)

        self.button_9 = Button(self.frame1,text='9',border=0,bg=color['bg-buttons-color'],fg='white',command=lambda : self.inputVisio.insert(END,'9'))
        self.button_9.place(relx=0.50, rely=0.32,relwidth=0.25, relheight=0.167)

        self.button_Calc = Button(self.frame1,text='=',border=0,bg='#d936d9', fg='white',
                                  command=self.Calc)
        self.button_Calc.place(relx=0.75, rely=0.32,relwidth=0.25, relheight=0.68)

        #LINHA 03
        self.button_4 = Button(self.frame1,text='4',border=0,bg=color['bg-buttons-color'],fg='white',command=lambda : self.inputVisio.insert(END,'4'))
        self.button_4.place(relx=0, rely=0.48,relwidth=0.25, relheight=0.167)

        self.button_5 = Button(self.frame1,text='5',border=0,bg=color['bg-buttons-color'],fg='white',command=lambda : self.inputVisio.insert(END,'5'))
        self.button_5.place(relx=0.25, rely=0.48,relwidth=0.25, relheight=0.167)

        self.button_6= Button(self.frame1,text='6',border=0,bg=color['bg-buttons-color'],fg='white',command=lambda : self.inputVisio.insert(END,'6'))
        self.button_6.place(relx=0.50, rely=0.48,relwidth=0.25, relheight=0.167)

        #LINHA 04
        self.button_1 = Button(self.frame1,text='1',border=0,bg=color['bg-buttons-color'],fg='white',command=lambda : self.inputVisio.insert(END,'1'))
        self.button_1.place(relx=0, rely=0.64,relwidth=0.25, relheight=0.167)

        self.button_2 = Button(self.frame1,text='2',border=0,bg=color['bg-buttons-color'],fg='white',command=lambda : self.inputVisio.insert(END,'2'))
        self.button_2.place(relx=0.25, rely=0.64,relwidth=0.25, relheight=0.167)

        self.button_3 = Button(self.frame1,text='3',border=0,bg=color['bg-buttons-color'],fg='white',command=lambda : self.inputVisio.insert(END,'3'))
        self.button_3.place(relx=0.50, rely=0.64,relwidth=0.25, relheight=0.167)

        #LINHA 05
        self.button_0 = Button(self.frame1,text='0',border=0,bg=color['bg-buttons-color'],fg='white',command=lambda : self.inputVisio.insert(END,'0'))
        self.button_0.place(relx=0, rely=0.80,relwidth=0.25, relheight=0.20)

        self.button_ponto = Button(self.frame1,text='.',border=0,bg=color['bg-buttons-color'],fg='white',command=lambda : self.inputVisio.insert(END,'.'))
        self.button_ponto.place(relx=0.25, rely=0.80,relwidth=0.25, relheight=0.20)

        self.button_ac = Button(self.frame1,text='AC',border=0,bg=color['bg-buttons-color'],fg='white',command=lambda : self.inputVisio.delete(0,END))
        self.button_ac.place(relx=0.50, rely=0.80,relwidth=0.25, relheight=0.20)
    
    def CreateInput(self):
         self.inputVisio = Entry(self.frame1,highlightbackground='blue', highlightthickness=0, bg=color['bg-primary-color'], fg="#ADD8E6",font=('Prociono',24));
         self.inputVisio.place(relx=0, rely=0, relwidth=1,relheight=0.167)

    def Calc(self):
        eval = Interpreter();
        try:
            expression = self.inputVisio.get()
            result = eval(expression);
            self.inputVisio.delete(0, END);
            self.inputVisio.insert(END,result)
        except Exception as e:
            return f'erro: {e}'






