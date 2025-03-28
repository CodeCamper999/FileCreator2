import ttkbootstrap as ttk
import random
import datetime
import shutil

# Socials: 
# Instagram: https://www.instagram.com/wrlddisciple999
# Twitter: https://x.com/wrlddisciple999


Main = ttk.Window(themename="vapor")
# I created a new GUI using ttkbootstrap
Main.geometry("450x600")
Main.title("File Creator 2")

Main.columnconfigure((0,1,2,3,4,5,6), minsize=5)
Main.columnconfigure(3, minsize=2)
Main.rowconfigure((0,1,2,3,4,5,6), minsize=5)
# I configured the rows and columns for the GUI

def Temp1(e):
    Name_File.delete(0, "end")  
def Temp2(e):
    int_Files.delete(0, "end")
def Temp3(e):
    Directoy.delete(0, "end")
def Temp4(e):
    File_Content.delete(0, "end")
    # When the user click in the entry box it would delete the pre existing text automatically 
# I created functions that allow us to add pre existing text 

def Create_Files():

    Number_Files = Get_Number.get()
    File_Name = Get_Name.get()
    File_Directory = File_Dir.get()
    Write_File = Content.get()
    # In order to get the information needed to create the files I use get() to get the user entry 
    with open("DirectoryList.txt", "w") as writeFile:
        writeFile.write(File_Directory + "/" + File_Name)
    # Once I get the directory and the file name I created a file which saves that information which I can use to copy existing files
    
    for i in range(Number_Files):
        # I am using range to stop the loop at the desired number the user inputs 
        Random = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","P","q","s","t","u","v","w","x","y","z"]
        Get_end = random.choice(Random[0:]) 
        # with this for loop I get a random ending from the list, which are all 26 letters of the alphabet 
            
        with open(File_Directory + "/" + File_Name + Get_end + ".txt", "w") as create:
            create.write(Write_File)
            # I can write the user data they put into the small entry box
        # for each letter of the alphabet or each python loops through this we will create another file over and over again with a new ending
        
            
def Copy():
    Input_window = ttk.Toplevel(Main)
    # Once the button is pressed another window will open up that is why we use ttk.toplevel
    Input_window.geometry("700x300")
    Input_window.title("Copy From Directory")
    Random = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","P","q","s","t","u","v","w","x","y","z"]
    
    
    def Temp(e):
        Get_Copy.delete(0, "end")
    # This function is exactly the same as the last once and serve the same purpose 
    def Transfer_Content():
        # This function will allow us to transfer text from one txt file to another
        Get_File = SaveCopy.get()
        # This will allow the user to enter what file they want to copy from 
        
        
        with open("DirectoryList.txt", "r") as readFile:
            Get_Information = readFile.read()
        # In order to paste the text from the file the user choose,
        # to the new ones we are going back to the saved directory which we created when the user put the directory in 
        Number = 30
        
        
        for i in range(Number):
            Get_end = random.choice(Random[0:]) 
            Source = open(Get_File, "r")
            
            paste = open(Get_Information + Get_end + ".txt", "w+")
            shutil.copyfileobj(Source, paste)
            # This for loop would get random letters from the list and copy the text from the file the user entered
            # Once python has that information it would paste it inside every file that already exist 
            print(i)
            
            
    SaveCopy = ttk.StringVar()
    # We are saving the information the user entered 
    Get_Copy = ttk.Entry(master=Input_window, textvariable=SaveCopy, width=60)
    Get_Copy.insert(0, "Please name the directory of the file you want to copy...")
    Get_Copy.bind("<FocusIn>", Temp)
    # In order for the pre existing text to disappear we need to add the text then specifiy the event that would trigger the command 
    # self explanatory to all the code at the end 
    
    Transfer = ttk.Button(master=Input_window, text="Copy", command=Transfer_Content, style="danger.TButton")
    
    Get_Copy.pack(ipady=10, pady=20)
    Transfer.pack(pady=10, ipadx=10)

Welcoming = ttk.Label(master=Main, text="CodeCamper999", font="ComicSansMS 20 normal", foreground="Magenta")

Get_Name = ttk.StringVar()
Get_Number = ttk.IntVar()
Name_File = ttk.Entry(master=Main, width=30, textvariable=Get_Name)
Name_File.insert(0, "Create the Name...")
Name_File.bind("<FocusIn>", Temp1)
int_Files = ttk.Entry(master=Main, textvariable=Get_Number, width=30)
int_Files.insert(0, "Number Of Files...")
int_Files.bind("<FocusIn>", Temp2)
File_Dir = ttk.StringVar()
Directoy = ttk.Entry(master=Main, textvariable=File_Dir, width=30)
Directoy.insert(0, "Please List File Directory...[N/A for Defualt]")
Directoy.bind("<FocusIn>", Temp3)
Enter = ttk.Button(master=Main, text="Create Files", style="danger.TButton", command=Create_Files)
Content = ttk.StringVar()
File_Content = ttk.Entry(master=Main, width=30, textvariable=Content)
File_Content.insert(0, "File Content?(Make short)")
File_Content.bind("<FocusIn>", Temp4)
Copy_File = ttk.Button(master=Main, text="Copy File", command=Copy)
Date = ttk.Label(master=Main, text="hi", font="ComicSansMS 20 normal", foreground="Magenta")

Welcoming.grid(row=0, column=2, sticky="news", padx=135)
Name_File.grid(row=1, column=2, ipadx=10, ipady=10, padx=10, pady=45)
int_Files.grid(row=2, column=2, ipadx=10, ipady=10, padx=5, pady=2)
Directoy.grid(row=3, column=2, ipadx=10, ipady=10, padx=5, pady=45)
Enter.grid(row=6, column=2, ipadx=10, ipady=10, padx=5, pady=2)
File_Content.grid(row=4, column=2, ipadx=10, ipady=10, padx=5, pady=2)
Copy_File.grid(row=5, column=2, ipadx=10, ipady=10, padx=5, pady=10)




Main.mainloop()