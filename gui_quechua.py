import tkinter as tk
from tkinter import LEFT
class Quechua(tk.Frame):
    def __init__(self, parent= None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.pack()
        self.set_constants()

        # Set canvas
        self.make_canvas()

        # Set question frame
        self.question_frame = self.make_question_frame()

        # Set frame options
        self.frame_options = self.make_option_frame()
        self.make_mode_list(self.frame_options)
        self.make_subject_list(self.frame_options)

        # Set title frame and play button
        self.make_title_frame()

    def selection_mode(self, var):
        self.mode = var.get()

    def selection_subject(self, var):
        self.subject = var.get()

    def refresh(self, master):
        master.destroy()
        self.make_question_frame()

    def start(self, master): 
        self.refresh(master)
        print('Empezamos a jugar')

    def set_constants(self):
        # Set window dimensions
        self.__HEIGHT = 450
        self.__WIDTH = 600  

    def make_canvas(self):
        self.winfo_toplevel().title('Quechua')
        self.canvas = tk.Canvas(self, height= self.__HEIGHT, width= self.__WIDTH)
        self.canvas.pack()
        
        self.img = tk.PhotoImage(file= './lanscape.png') 
        self.bg = self.canvas.create_image(0, 0, image= self.img, anchor = "nw")

    def make_title_frame(self): 
        frame_title = tk.Frame(self, bg= '#80c1ff', bd= 5)
        frame_title.place(relx= 0.5, 
                            rely= 0.2, 
                            relwidth= 0.5, 
                            relheight= 0.15, 
                            anchor= 'n')

        text = tk.StringVar()
        text.set('Bienvenido!\nVamos a aprender quechua')
        text_title = tk.Label(frame_title, 
                                textvariable= text, 
                                font= ('Arial', 12))
        text_title.place(relwidth= 0.80, 
                            relheight= 1)

        button = tk.Button(frame_title, text= 'Jugar !', 
                            bg= '#5dabd9',
                            font= ('Arial', 10), 
                            command= lambda: self.start(self.question_frame),
                            )
        button.place(relx= 0.81, 
                    relwidth= 0.18, 
                    relheight= 1)
        return frame_title

    def make_option_frame(self): 
        frame_options = tk.Frame(self, bd= 5)
        frame_options.place(relx= 0.5, 
                            rely= 0.0, 
                            relwidth= 1, 
                            relheight= 0.10, 
                            anchor= 'n')
        return frame_options

    def make_mode_list(self, master): 
        # Set variable 
        var = tk.IntVar()

        values = {"Quechua a español" : "1",
                  "Español a quechua" : "2"}
        
        for (text, value) in values.items():
            tk.Radiobutton(master, 
                            text = text, 
                            variable= var,
                            command= lambda: self.selection_mode(var), 
                            value = value).pack(side=LEFT, anchor= 'w')

    def make_subject_list(self, master): 
        # Set variable 
        var = tk.IntVar()

        values = {"Sustantivos" : "1",
                  "Verbos" : "2", 
                  "Frases" : "3"}
        
        for (text, value) in values.items():
            tk.Radiobutton(master, text = text, 
                            variable= var,
                            command= lambda: self.selection_subject(var), 
                            bg= '#80c1ff',
                            value = value).pack(side=LEFT, anchor= 'w')
    
    def make_question_frame(self): 
        frame_question = tk.Frame(self, 
                                bg= 'white', 
                                bd= 5)
        frame_question.place(relx= 0.5, 
                            rely= 0.4, 
                            relwidth= 0.8, 
                            relheight= 0.4, 
                            anchor= 'n')
        return frame_question
        




root = tk.Tk()
Quechua(root)
root.mainloop()

