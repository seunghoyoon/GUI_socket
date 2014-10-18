# -*- encoding:utf-8 -*-
from Tkinter import *
import tkMessageBox
#=====================================================================================
class APP:
      
    def __init__(self,root):
        #================================== 
        t_frame = Frame(root,width='200')
        t_frame.pack(fill=X,padx='40',pady='10')
        
        self.label = Label(t_frame,text='IP주소')
        self.label.pack(side=LEFT)
        
        self.txt1 = Entry(t_frame)
        self.txt1.pack(side=LEFT)
        
        btn1 = Button(t_frame,text='확인',command=self.getIp)
        btn1.pack(side=LEFT)
        
        #================================== 
        b_frame = Frame(root)
        b_frame.pack(fill=X,padx='40',pady='10')
   
        self.txt2 = Entry(b_frame,width='180')
        self.txt2.pack(side=LEFT)
    
    def getIp(self):    
        msg = self.txt1.get()
        self.txt2.insert(0, msg)
        
        
        
        
        
        
        
        
        
    def alert(self,msg):    
        tkMessageBox.showinfo('�˸�', msg)        
                
                
                
                
#=====================================================================================
if __name__ == '__main__':
    root = Tk()
    root.title('메일서버 추적기')
    root.geometry('300x100')
    APP(root)
    root.mainloop()