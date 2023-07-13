from tkinter import *
global_key_input=None
class Keyboard_Input:

    #def __init__(self, master):
    def __init__(self,root):
        
        self.root = root#master

        '''# Get the screen width and height
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()'''

        #setting window widths
        self.window_width = 1
        self.window_height = 1

        # Set the window's dimensions and position
        '''self.window_x = self.window_width#self.screen_width - self.window_width
        self.window_y = self.window_height#self.screen_height - self.window_height
        self.root.geometry(f"{self.window_width}x{self.window_height}+{self.window_x}+{self.window_y}")'''

        self.key_input = StringVar()
        self.root.bind("<KeyPress>", self.on_key_press)
        self.root.focus_set()
        '''self.root.mainloop()
        self.root.quit()'''
    def initial(self):
        global global_key_input
        global_key_input = None
    def on_key_press(self, event):
        global global_key_input
        if event.keysym == 'Up':
            self.key_input.set("u")
            print("up")
            global_key_input = "u"
            #self.root.quit()
        elif event.keysym == 'Down':
            print("down")
            self.key_input.set("d")
            global_key_input = "d"
            #self.root.quit()
        elif event.keysym == 'Left':
            print("left")
            self.key_input.set("l")
            global_key_input = "l"
            #self.root.quit()
        elif event.keysym == 'Right':
            print("right")
            self.key_input.set("r")
            global_key_input = "r"
            #self.root.quit()
        elif event.keysym == 'Escape':
            print("Exiting application")
            self.root.quit()
        #return self.key_input.get()
        #self.root.destroy()
        #print("Key input:", self.global_key_input)
    
    def get_key(self):
        return global_key_input






#root.iconify()

#root.update()

#print("Global Key input:", global_key_input)
