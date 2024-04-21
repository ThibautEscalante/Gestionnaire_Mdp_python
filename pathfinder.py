import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Pathfinder")
        
        # Calculer les nouvelles dimensions de la fenêtre
        new_width = int(self.winfo_screenwidth() * 0.4)
        new_height = int(self.winfo_screenheight() * 0.2)
        
        self.geometry(f"{new_width}x{new_height}")
        
        # Centrer la fenêtre
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'+{x}+{y}')
        
        self.home_page()
        
    def home_page(self):
        self.clear_window()
        
        self.title_label = tk.Label(self, text="Bienvenue sur Pathfinder", font=("Helvetica", 16))
        self.title_label.pack(pady=10)
        
        self.code_label = tk.Label(self, text="Entrez votre code d'authentification :", font=("Helvetica", 12))
        self.code_label.pack()
        
        self.code_entry = tk.Entry(self, show="*")
        self.code_entry.pack(pady=5)
        
        self.submit_button = tk.Button(self, text="Valider", command=self.check_code)
        self.submit_button.pack(pady=5)
        
        self.error_label = tk.Label(self, text="", fg="red")
        self.error_label.pack()
        
        self.credit_label = tk.Label(self, text="credit to RR", font=("Helvetica", 8))
        self.credit_label.place(relx=1, rely=1, anchor='se')
        
    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        
    def check_code(self):
        texte="I'm only looking for my creator. You don't know where my creator is, do you?"
        code = self.code_entry.get()
        
        if code == "00000000":
            self.mdp_page()
        else:
            if hasattr(self, 'attempt'):
                self.attempt += 1
            else:
                self.attempt = 1
            
            if self.attempt == 1:
                self.error_label.config(text="Trying is 55.5% of the battle.")
            elif self.attempt == 2:
                self.error_label.config(text="That was close!")
            elif self.attempt == 3:
                self.error_label.config(text="You did a really mediocre job, friend! If I had a heart, it would be racing right now.")
            elif self.attempt == 4:
                self.error_label.config(text="Great moves, friend! Sorry, you lost. Don't beat yourself up. Leave that to me! That was a joke!")
                self.after(2000, self.show_second_msg(texte))
                self.after(1000, self.quit)  # Ferme l'application après 2 secondes
        
        self.code_entry.delete(0, 'end')

    def show_second_msg(self, text):
        self.error_label.config(text=text)
        
    def mdp_page(self):
        self.clear_window()
        
        self.mdp_label = tk.Label(self, text="Page MDP", font=("Helvetica", 16))
        self.mdp_label.pack(pady=10)
        
        self.credit_label = tk.Label(self, text="credit to RR", font=("Helvetica", 8))
        self.credit_label.place(relx=1, rely=1, anchor='se')
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
