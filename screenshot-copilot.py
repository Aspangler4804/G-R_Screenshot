#need to check for version/os compatibility
import pyautogui
from tkinter import *
from tkinter import ttk
from PIL import Image

#To do:
    #make the start screen, shouldnt be too hard
    #make file system
    #send photos to files

    #if have time, some sort of exporting functionality


class Start_Screen:
    def __init__(self, root):
        self.tempPage = ttk.Frame(root, )
        #make a small popup that gets the name and ufid and then sends to a txt file in a new folder that creates 2 empty folders one 
        #for good clicks and one for red clicks
        root.title("Name UFID")
        #test
        #entry widget here
        # make sure to validate here, tehre is a validate command configurarion option
        

    def validate(self, name, ufid):
        try:
            print("Better be valid id and name")
            self.success
        except:
            print("fail!!")

    def success(self):
        self.tempPage.destroy()
        File_Buttons(self.root)

class File_Buttons:
    def __init__(self, root):
        #initialize root, and style for main
        root.title("Copilot Use") 
        root.rowconfigure(0, weight =1)
        root.columnconfigure(0, weight =1)       
        Style = ttk.Style()
        Style.theme_use('clam')
        Style.configure('Main.Tframe', background = 'red', relief = 'raised')
        
        #create mainframe, and build seperators
        self.mainframe = ttk.Frame(root, width = 400, style = 'Main.TFrame')
        self.mainframe.grid(sticky = "NSEW")
        ttk.Frame(self.mainframe, borderwidth = 5, width = 50).grid(column = 2, row = 0, sticky = "NSEW")
        ttk.Frame(self.mainframe, borderwidth = 5, width = 50).grid(column = 4, row = 0, sticky = "NSEW")
        
        #set self.mainframe to dynamically respond to change in size
        self.mainframe.columnconfigure(0, weight = 1, minsize=25)
        self.mainframe.columnconfigure(1, weight = 1, minsize=25)
        self.mainframe.columnconfigure(2, weight = 1, minsize=25)
        self.mainframe.columnconfigure(3, weight = 1, minsize = 10)
        self.mainframe.columnconfigure(4, weight = 1, minsize=25)
        self.mainframe.columnconfigure(5, weight = 1, minsize=25)
        self.mainframe.columnconfigure(6, weight = 1, minsize= 25)
        self.mainframe.rowconfigure(0, weight = 1)
        
        #Build button styles, and insert buttons with functionality
        Style.configure('G.TButton', font = ('calibri', 10, 'bold', 'underline'), background = "green", foreground = 'black', borderwidth = 1)
        Style.configure('R.TButton', font = ('calibri', 10, 'bold', 'underline'), background = 'red', foreground = 'black')
        Style.configure('E.TButton', font = ('calibri', 10, 'bold', 'underline'), background = 'black', foreground = 'white')
        ttk.Button(self.mainframe, text = "Green Button", command = self.green_click, width = 50, style = 'G.TButton', takefocus = False).grid(column = 0, columnspan = 2, row = 0, sticky = "NSEW")
        ttk.Button(self.mainframe, text = "Red Button", command = self.red_click, width = 50, style = 'R.TButton', takefocus = False).grid(column = 5, columnspan = 2, row = 0, sticky = "NSEW")
        eB = ttk.Button(self.mainframe, text = "Click when finished", command = self.exit_click, width = 25, style = 'E.TButton', takefocus = False)
        eB.grid(column = 3, row = 0, sticky = "NSEW")
        #eB.bind('<Double-1>', self.exit_click)

    def exit_click(self):
        #pause timer, open a window to double check
        #timer.pause
        try:
            
            final_check = Toplevel(self.mainframe, bg = 'white')
            final_check.grid()
            final_check.grab_set()
            #focus screen
            #make questions appear
            VF = ttk.Button(final_check, text = "Yes I am finished", command = self.kill_program)
            VF.grid(row = 0, column = 0)
            NF = ttk.Button(final_check, text = "I am not finished", command = lambda:self.revert(VF, NF, final_check))
            NF.grid(row = 0, column = 1)
            final_check.mainloop()
        except KeyboardInterrupt:
            pass

    def green_click(self):
        try:
            
            print("Green Click")
        except KeyError:
            pass


    def red_click(self):
        
        try:
            print("Red click")
        except KeyError:
            #change this to an appropriate error
            pass
    
    def kill_program(self):
        try:
            print("Saving files")
        except KeyboardInterrupt:
            pass

    def revert(self, b1, b2, tl):
        #destroy popup, revert to normal screen
        b1.destroy()
        b2.destroy()
        tl.destroy()


def main():  
    root = Tk()
    Start_Screen(root) 
    root.mainloop()
    



if __name__ == "__main__":
    main()
    