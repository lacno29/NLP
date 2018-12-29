from tkinter import *
import et
import os

class Translator:
    _bg = "#5d737e"

    def __TranslateET(self):
        ans = str(et.translate(self.txtInput.get(1.0,END),True))
        self.txtOutput.delete(1.0,END)
        self.txtOutput.insert(END,ans)
    def __TranslateTE(self):
        try:
            os.remove("output.txt")
        except FileNotFoundError:
            pass
        file = open("inputParagraph.txt","w")
        file.write(self.txtInput.get(1.0,END))
        file.close()
        import te
        ans = open("output.txt").read()
        self.txtOutput.delete(1.0,END)
        self.txtOutput.insert(END,ans)
    
    def __init__(self,top=None):
        top.geometry("700x500+100+10")
        top.title("Translator")
        top.configure(bg=self._bg)

        #####################
        self.northFrame = Frame(top,
            bg = self._bg,
            padx = 5,
            pady = 5,
        )
        self.northFrame.place(relx=0,rely=0,relwidth=1,relheight=0.45)
        
        self.txtInput = Text(self.northFrame,
            bg = "#eeeeee",
            fg = "black",
            padx = 5,
            pady = 3,
            wrap = None,
            relief = FLAT
        )
        self.txtInput.place(
            relx = 0,
            rely = 0,
            relwidth = 1,
            relheight = 1
         )

        #########################
        self.centerFrame = Frame(top,padx = 5,pady=5,bg=self._bg)
        self.centerFrame.place(relx=0,rely=0.45,relwidth=1,relheight=0.1)

        self.toggleMode = Button(self.centerFrame,text="English->Tagalog",font=("Helvetica"),command=self.__TranslateET)
        self.toggleMode.pack(side=LEFT,fill=BOTH,padx=10)

        self.btnTranslate = Button(self.centerFrame,text="Tagalog->English",font=("Helvetica"),command=self.__TranslateTE)
        self.btnTranslate.pack(side=LEFT,fill=BOTH)

        ##########################
        self.southFrame = Frame(top,padx=5,pady=5,bg=self._bg)
        self.southFrame.place(relx=0,rely=0.55,relwidth=1,relheight=0.45)

        self.txtOutput = Text(self.southFrame,
            bg = "#eee",
            fg = "black",
            padx = 5,
            pady = 3,
            wrap = None,
            relief = FLAT
        )
        self.txtOutput.place(
            relx = 0,
            rely = 0,
            relwidth = 1,
            relheight = 1
         )
        
def main():
    root = Tk()
    top = Translator(root)
    root.mainloop()

main()
