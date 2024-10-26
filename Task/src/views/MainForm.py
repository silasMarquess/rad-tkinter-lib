#from .style.sheet import *
from tkinter import *
from tkinter import ttk
from ..controllers.taskControler import Functions
taskControl = Functions();

colors1 = {
    'primary-bg-color':'#363636',
    'colors-bg-buttons':'#089523',
    'colors-bg-frames':'#414141',
    'colors-font-':'teste',
    'color-border-frame':"#787878",
    'fonts-color':'#22ee16',
    'background_entrys':'#4F4F4F'
}


class MainForm(Functions):
    id_taskUpdate = None;
    def __init__(self):
        self.root = Tk();
        self.displayConfig();
        self.CreateFrame();
        self.CreateLabels();
        self.CreateInputs();
        self.CreateButtons();
        self.CreateTreeView();
        self.root.mainloop();

    def displayConfig(self):
        self.root.title('Task Manager')
        self.root.config(background=colors1['primary-bg-color'])
        self.root.geometry('900x560');
        #self.root.maxsize('1000x600')

    def CreateFrame(self):
         self.frame1 = Frame(self.root,border=2, bg=colors1['colors-bg-frames'],highlightbackground=colors1['color-border-frame'],highlightthickness=1)
         self.frame1.place(relx=0.01,rely=0.03,relwidth=0.98, relheigh=0.12);#opções de alinhamento

         self.frame2 = Frame(self.root,border=2, bg=colors1['colors-bg-frames'],highlightbackground=colors1['color-border-frame'],highlightthickness=1)
         self.frame2.place(relx=0.01,rely=0.16,relwidth=0.98, relheigh=0.69);#opções de alinhamento

         self.frame3 = Frame(self.root,border=2, bg=colors1['colors-bg-frames'],highlightbackground=colors1['color-border-frame'],highlightthickness=1)
         self.frame3.place(relx=0.01,rely=0.87,relwidth=0.98, relheigh=0.10);#opções de alinhamento

    def CreateButtons(self):
         self.button_create = Button(self.frame1, text='SAVE',border=0,highlightthickness=0,bg=colors1['colors-bg-buttons'],fg='white',
                                      font=('Raleway',10),command=lambda: (self.CreateOrUpdate(),self.IndexTreeview()))
         
         self.button_create.place(relx=0.39, rely=0.338,relwidth=0.08,relheight=0.5)

         self.button_index = Button(self.frame1, text='GET',border=0,bg=colors1['colors-bg-buttons'],fg='white',highlightthickness=0,
                                      font=('Raleway',10), command=self.IndexTreeview)
         
         self.button_index.place(relx=0.9, rely=0.338,relwidth=0.08,relheight=0.5)


         self.button_delete = Button(self.frame3, text='Delete',border=0,bg=colors1['colors-bg-buttons'],fg='white',highlightthickness=0,
                                      font=('Raleway',10), command=lambda:(self.Delete(),self.IndexTreeview()))
         
         self.button_delete.place(relx=0.01, rely=0.26,relwidth=0.08,relheight=0.60)

         self.button_update = Button(self.frame3, text='Update',border=0,bg=colors1['colors-bg-buttons'],fg='white',highlightthickness=0,
                                      font=('Raleway',10),command=lambda: self.getInforUpdate())
         self.button_update.place(relx=0.1, rely=0.26,relwidth=0.08,relheight=0.60)

         self.button_set_right = Button(self.frame2, text='->',border=0,bg=colors1['colors-bg-buttons'],fg='white',font=('Raleway',10),highlightthickness=0,
                                       command=lambda:(taskControl.update_status(
                                           id=self.treeView1.selection()[0],
                                           status=True
                                       ),self.IndexTreeview())
                                    );
        
         self.button_set_right.place(relx=0.47, rely=0.46,relwidth=0.07,relheight=0.07)

         self.button_set_left = Button(self.frame2, text='<-',border=0,bg=colors1['colors-bg-buttons'],fg='white',font=('Raleway',10),highlightthickness=0,
                                      command=lambda:(taskControl.update_status(
                                           id=self.treeView2.selection()[0],
                                           status=False
                                       ),self.IndexTreeview())
                                    );
         self.button_set_left.place(relx=0.47, rely=0.52,relwidth=0.07,relheight=0.07)

    def CreateLabels(self):
         self.label_task = Label(self.frame1,text='TASK/DESCRIPTION',fg=colors1['fonts-color'],
                                 font=('Raleway',11), background=colors1['colors-bg-frames']);
         self.label_task.place(relx=0.01,rely=0.01)

         self.label_task_Treeview1 = Label(self.frame2,text='TASK-PENDING',fg=colors1['fonts-color'],font=('Raleway',11), background=colors1['colors-bg-frames']);
         self.label_task_Treeview1.place(relx=0.01,rely=0.01)

         self.label_task_Treeview2 = Label(self.frame2,text='TASK COMPLETED',fg=colors1['fonts-color'],
                                 font=('Raleway',11), background=colors1['colors-bg-frames']);
         self.label_task_Treeview2.place(relx=0.55,rely=0.01)
    
    def CreateInputs(self):
         self.inputTask = Entry(self.frame1,highlightbackground='blue', highlightthickness=0, bg=colors1['background_entrys'], fg="white",
                                font=('Raleway',11));
         self.inputTask.place(relx=0.01, rely=0.33, relwidth=0.38, relheight=0.5)

    def CreateTreeView(self):
        estyle = ttk.Style()
        estyle.configure("Treeview",font=('Roboto',12),bg='gray')
#LISTA 1

        self.treeView1 = ttk.Treeview(self.frame2,heigh=3,
                                        columns=(
                                          'ID',
                                          'descryption',
                                          'completed'
                                        ),show="headings",style='Treeview')
        
        self.treeView1.heading('ID',text='ID')
        self.treeView1.heading('descryption',text='Description Task')
        self.treeView1.heading('completed',text='Resolved?')

        self.treeView1.column("ID",width=15)
        self.treeView1.column("descryption",width=260)
        self.treeView1.column("completed",width=120)

        self.treeView1.place(relx=0.01,rely=0.07,relwidth=0.47, relheigh=0.9)
        self.scroolBar = ttk.Scrollbar(self.frame2,orient='vertical')
        self.treeView1.configure(yscrollcommand=self.scroolBar.set)
        self.scroolBar.place(relx=0.47,rely=0.07,relwidth=0.016,relheight=0.9)   
#   LISTA 2
        self.treeView2 = ttk.Treeview(self.frame2,heigh=3,
                                        columns=(
                                          'ID',
                                          'descryption',
                                          'completed'
                                        ),show="headings",style="Treeview")
        
        self.treeView2.heading('ID',text='ID')
        self.treeView2.heading('descryption',text='Description')
        self.treeView2.heading('completed',text='Resolved?')

        self.treeView2.column("ID",width=15)
        self.treeView2.column("descryption",width=260)
        self.treeView2.column("completed",width=120)

        self.treeView2.place(relx=0.53,rely=0.07,relwidth=0.46,relheigh=0.91)

        self.scroolBar = ttk.Scrollbar(self.frame2,orient='vertical')
        self.treeView2.configure(yscrollcommand=self.scroolBar.set)
        self.scroolBar.place(relx=0.98,rely=0.07,relwidth=0.016,relheight=0.91)

        pass

    def IndexTreeview(self):
         lista = taskControl.index();

         for i in self.treeView1.get_children():
              self.treeView1.delete(i)
              
         for i in self.treeView2.get_children():
              self.treeView2.delete(i)
        
         for dado in lista:
              completed = dado.completed;
              if(not completed):
                self.treeView1.insert("",END,iid=dado.id,values=(dado.id,dado.descryption,dado.completed));
              else:
                self.treeView2.insert("",END,iid=dado.id,values=(dado.id,dado.descryption,dado.completed));
     
    def CreateOrUpdate(self):
        task_descryption = self.inputTask.get();
        if MainForm.id_taskUpdate != None:
            taskControl.update(MainForm.id_taskUpdate,{
                'descryption':task_descryption,
                'completed':False
            })
            MainForm.id_taskUpdate = None;
        else:
            taskControl.story({'descryption':task_descryption,'completed':False})
            pass;
        self.inputTask.delete(0,END)
   
    def Delete(self):
        id = None
        if  self.treeView1.selection():
            id = self.treeView1.selection()[0]
        else:
            id = self.treeView2.selection()[0]
        taskControl.delete(id);

    def getInforUpdate(self):
         id = None
         if  self.treeView1.selection():
            id = self.treeView1.selection()[0]
         else:
            id = self.treeView2.selection()[0]

         task_update = taskControl.show(id)
         self.inputTask.delete(0, END)
         self.inputTask.insert(END,task_update.descryption);
         MainForm.id_taskUpdate = id;


c = MainForm();