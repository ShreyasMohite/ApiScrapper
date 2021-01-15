from tkinter import *
import json
import requests
from bs4 import BeautifulSoup
import tkinter.messagebox
import threading




class jsonScrapper:
    def __init__(self,root):
        self.root=root
        self.root.title("Json Scrapper")
        self.root.geometry("400x400")
        self.root.iconbitmap("logo66.ico")
        self.root.resizable(0,0)



        url=StringVar()
        savename=StringVar()





#=======================hover on button================#
        def on_enter1(e):
            downBut['background']="black"
            downBut['foreground']="cyan"
  
        def on_leave1(e):
            downBut['background']="SystemButtonFace"
            downBut['foreground']="SystemButtonText"

        def on_enter2(e):
            clearBut['background']="black"
            clearBut['foreground']="cyan"
  
        def on_leave2(e):
            clearBut['background']="SystemButtonFace"
            clearBut['foreground']="SystemButtonText"




#=======================methonds on button==============#


        def clear():
            url.set("")
            savename.set("")  


        def download():
            try:

                if (len(url.get())!=0):
                    if(len(savename.get())!=0):

                        response=requests.get(url.get())
                        loadData=json.loads(response.text)
                        dataInJson=json.dumps(loadData,indent=4)

                        with open(f"{savename.get()}.json","w") as data:
                            data.write(dataInJson)

                        
                        tkinter.messagebox.showinfo("Success","Data Downloaded Successfully")
                    else:
                        tkinter.messagebox.showerror("Error","Please Enter Name to save")
                else:
                    tkinter.messagebox.showerror("Error","please enter proper url")

            except Exception as e:
                tkinter.messagebox.showerror("Error","Network Error")
                print(e)


        
        def downloadData():
            t=threading.Thread(target=download)
            t.start()




#https://api.covid19api.com/summary



#=================frame=============================

        mainframe=Frame(self.root,width=400,height=400,relief="ridge",bd=3,bg="gray68")
        mainframe.place(x=0,y=0)

#====================================================





     

#==================label=============================
        
        urlLab=Label(mainframe,text="Please Enter Url",font=('times new roman',14),bg="gray68")
        urlLab.place(x=130,y=10)

        saveAsLab=Label(mainframe,text="Save As Name",font=('times new roman',14),bg="gray68")
        saveAsLab.place(x=130,y=100)


#=====================================================




#=============Entry===================================#
        
        urlEnt=Entry(mainframe,width=40,font=('times new roman',14),relief="ridge",bd=3,textvariable=url)
        urlEnt.place(x=12,y=45)

        saveAsEnt=Entry(mainframe,width=20,font=('times new roman',14),relief="ridge",bd=3,justify="center",textvariable=savename)
        saveAsEnt.place(x=100,y=135)


#======================================================#




#=======================button========================#
          
        downBut=Button(mainframe,text="Download",font=('times new roman',14),width=14,cursor="hand2",command=downloadData)
        downBut.place(x=20,y=240)
        downBut.bind("<Enter>",on_enter1)
        downBut.bind("<Leave>",on_leave1)



        clearBut=Button(mainframe,text="Clear",font=('times new roman',14),width=14,cursor="hand2",command=clear)
        clearBut.place(x=220,y=240)
        clearBut.bind("<Enter>",on_enter2)
        clearBut.bind("<Leave>",on_leave2)

        





if __name__=="__main__":
    root=Tk()
    jsonScrapper(root)
    root.mainloop()