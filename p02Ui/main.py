import customtkinter as tk
from ui.InicioGui import InicioGui
from ui.OllamaUi import OllamaUi
class App(tk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Panel de Usuario")
        self.geometry("300x200")

        
        #fragmentos
        self.container=tk.CTkFrame(self)
        self.container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.paginas={}
        self.crearPaginas()
        self.mostrarPagina("pagina1")
            
    def crearPaginas(self):
        self.paginas["pagina1"]=InicioGui(parent=self.container, controller=self)
        self.paginas["pagina2"]=OllamaUi(parent=self.container, controller=self)
        #botones
        for pagina in self.paginas.values():
            pagina.place(relx=0, rely=0, relwidth=1, relheight=1)
    def mostrarPagina(self, pagina,titulo="Sha 256"):
        self.title(titulo)
        pagina=self.paginas[pagina]
        pagina.tkraise()
if __name__ == "__main__":
    app = App()
    app.mainloop()