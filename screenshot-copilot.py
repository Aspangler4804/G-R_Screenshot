import pyautogui
import os
from tkinter import *
from tkinter import ttk
from PIL import Image
import time
from datetime import datetime

######################################
# Maximum of 1 screenshot per second
#####################################
# The executable and internal folder need to be zipped together before being distributed
#####################################


class Start_Screen:

    #Small popup to start timer/ initialize files
    def __init__(self):
        #save root for later
        root = Tk()
        self.root = root
        root.wm_attributes("-topmost", 1)
        #Init temp frame and button/label
        self.tempPage = ttk.Frame(root, width = 200)
        self.tempPage.grid(column = 0, row = 0)
        ttk.Button(self.tempPage, text= "START", command = self.success).grid(column = 0, row = 0)
        ttk.Label(self.tempPage, text = "Click start to begin the assignment").grid(column = 0, row = 1)
        
        #Init files
        self.initFiles()
        root.mainloop()

        
    def initFiles(self):
        #Create files with the time right now
        cur_date = datetime.now()
        

        formatted_date = cur_date.strftime("%b%d-%I-%M")

        #Get user directory, change cwd to scripts dir
        script_dir = os.path.dirname(os.path.abspath(__file__))
        cwd = os.chdir(script_dir)
        cwd = os.getcwd()


        self.project_dir = os.path.join(cwd, 'Research_Project')
        os.path.normcase(self.project_dir)
        #print(cwd)
        
        print(self.project_dir)

        #If alrdy has project dir, dont make again
        if os.path.isdir(self.project_dir):
            pass
        else:
            os.mkdir(self.project_dir)

        
        #Build seperate folders for red/green click
        self.g_dir = os.path.join(self.project_dir, 'green_click('+str(formatted_date)+')')
        self.r_dir = os.path.join(self.project_dir, 'red_click('+str(formatted_date)+')')
        os.mkdir(os.path.normcase(self.g_dir))
        os.mkdir(os.path.normcase(self.r_dir))
        #os.mkdir(self.r_dir)


    def success(self):        
        #Start the main program
        self.tempPage.destroy()
        File_Buttons(self.root, self.project_dir, self.g_dir, self.r_dir)



class File_Buttons:
    
    def __init__(self, root, cwd, g_d, r_d):
        #initialize root, and style for main
        self.root = root

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
        # eB = ttk.Button(self.mainframe, text = "Click when finished", command = self.exit_click, width = 25, style = 'E.TButton', takefocus = False)
        # eB.grid(column = 3, row = 0, sticky = "NSEW")
        #eB.bind('<Double-1>', self.exit_click)

        #make the cwd accessible
        self.cwd = cwd
        self.g_d = g_d
        self.r_d = r_d

        #Start timer
        self.start_time = time.time()


    def exit_click(self):
        
        try:
            #Build a small screen to verify exit
            final_check = Toplevel(self.mainframe, bg = 'white')
            final_check.grid()
            final_check.wm_attributes("-topmost", 1)
            #focus screen, display options
            final_check.grab_set()
            VF = ttk.Button(final_check, text = "Yes I am finished", command = self.kill_program)
            VF.grid(row = 0, column = 0)
            NF = ttk.Button(final_check, text = "I am not finished", command = lambda:self.revert(VF, NF, final_check))
            NF.grid(row = 0, column = 1)
            final_check.mainloop()
        except KeyboardInterrupt:
            pass

    def green_click(self):
        try:
            im = pyautogui.screenshot()
            cur_time = time.time()
            #print(cur_time - self.start_time)
            im.save(os.path.normcase(os.path.join(self.g_d, "G_C_"+ str(int(cur_time - self.start_time))+ ".pdf")))
        except FileNotFoundError:
            print("Please delete the research folder and try again")
            pass


    def red_click(self):
        
        try:
            im = pyautogui.screenshot()
            cur_time = time.time()
            im.save(os.path.normcase(os.path.join(self.r_d, "R_C_"+ str(int(cur_time - self.start_time))+ ".pdf")))
        except FileNotFoundError:
            print("Please delete the research folder and try again")
            pass
    
    def kill_program(self):
        try:
            self.root.destroy()
        except KeyboardInterrupt:
            pass

    def revert(self, b1, b2, tl):
        #destroy popup, revert to normal screen
        b1.destroy()
        b2.destroy()
        tl.destroy()


def main():  
    Start_Screen() 
    



if __name__ == "__main__":
    main()
    