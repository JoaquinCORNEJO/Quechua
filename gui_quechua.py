import tkinter as tk

class Quechua(tk.Frame):
    def __init__(self, parent= None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.pack()
        self.set_constants()
        self.make_canvas()
        self.make_title_frame()
        self.make_mode_list()
        

    def set_constants(self):
        # Set window dimensions
        self.__HEIGHT = 450
        self.__WIDTH = 600  

    def make_canvas(self):
        self.winfo_toplevel().title('Quechua')
        self.canvas = tk.Canvas(self, height= self.__HEIGHT, width= self.__WIDTH)
        self.canvas.pack()
        
        self.img = tk.PhotoImage(file= './lanscape.png') 
        self.bg = self.canvas.create_image(0.1, 0.1, image= self.img, anchor = "nw")

    def make_title_frame(self): 
        self.frame_title = tk.Frame(self, bg= '#80c1ff', bd= 5)
        self.frame_title.place(relx= 0.5, rely= 0.05, relwidth= 0.75, relheight= 0.15, anchor= 'n')

        text = tk.StringVar()
        text.set('Bienvenido!\nVamos a aprender quechua jugando')
        self.text_title = tk.Label(self.frame_title, textvariable= text, font= ('Arial', 14))
        self.text_title.place(relwidth= 1, relheight= 1)

    # ----------------
    def sel(self, var):
        selection = "You selected the option " + str(var.get())
        print(selection)

    def make_mode_list(self): 
        # Set variable 
        var = tk.IntVar()

        # Dictionary to create multiple buttons
        values = {"Quechua a español" : "1",
                "Español a quechua" : "2"}
        
        # Loop is used to create multiple Radiobuttons
        # rather than creating each button separately
        for (text, value) in values.items():
            tk.Radiobutton(self, text = text, variable= var,
                            command= lambda: self.sel(var), value = value).pack()

root = tk.Tk()
Quechua(root)
root.mainloop()

