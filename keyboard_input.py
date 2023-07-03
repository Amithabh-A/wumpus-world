from tkinter import *

class Keyboard_Input:

    #def __init__(self, master):
    def __init__(self):
        self.global_key_input = None
        self.root = Tk()#master

        # Get the screen width and height
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        #setting window widths
        self.window_width = 1
        self.window_height = 1

        # Set the window's dimensions and position
        self.window_x = self.window_width#self.screen_width - self.window_width
        self.window_y = self.window_height#self.screen_height - self.window_height
        self.root.geometry(f"{self.window_width}x{self.window_height}+{self.window_x}+{self.window_y}")

        self.key_input = StringVar()
        self.root.bind("<KeyPress>", self.on_key_press)
        self.root.focus_set()
        self.root.mainloop()
        self.root.quit()

    def on_key_press(self, event):
        global global_key_input
        if event.keysym == 'Up':
            self.key_input.set("u")
            print("up")
            self.global_key_input = self.key_input.get()
            self.root.quit()
        elif event.keysym == 'Down':
            print("down")
            self.key_input.set("d")
            self.global_key_input = self.key_input.get()
            self.root.quit()
        elif event.keysym == 'Left':
            print("left")
            self.key_input.set("l")
            self.global_key_input = self.key_input.get()
            self.root.quit()
        elif event.keysym == 'Right':
            print("right")
            self.key_input.set("r")
            self.global_key_input = self.key_input.get()
            self.root.quit()
        elif event.keysym == 'Escape':
            print("Exiting application")
            self.root.quit()
        self.root.destroy()
        #print("Key input:", self.global_key_input)
    
    def get_key(self):
        return self.global_key_input






#root.iconify()

#root.update()

#print("Global Key input:", global_key_input)