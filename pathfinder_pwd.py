import tkinter as tk
from tkinter import messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Modifier la couleur de fond de la fenêtre
        self.configure(bg="#282828")

        # Black #141414 / Black #282828 / Black Olive #3c3c3c / Arsenic #3c3c50 / Gunmetal #28283c

        self.title("MRVN - Pathfinder")
        
        # Calculer les nouvelles dimensions de la fenêtre
        new_width = int(self.winfo_screenwidth() * 0.4)
        new_height = int(self.winfo_screenheight() * 0.4)
        
        self.geometry(f"{new_width}x{new_height}")

        # Charger icone
        icon = tk.PhotoImage(file="./Icon/path_icon.png")
        # Charger l'icone en tant qu'icone fenetre et de barre windows
        self.iconphoto(False, icon, icon)
        
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

        # Rendre les écritures blanches pour tous les widgets
        text_color = "white"
        button_color = "#141414" #noir profond
        button_hover_color = "#282828" #noir sombre
        button_border_color = "#3c3c3c" #gris sombre

        # Font et taille
        font_family = "Oswald"
        font_size = 24
        
        self.title_label = tk.Label(self, text="- Mobile Robotic Versatile eNtity -", font=(font_family, font_size), fg=text_color, bg="#282828")
        self.title_label.pack(pady=(65,0))

        self.subtitle_label = tk.Label(self, text="Gestionnaire de mot de passe", font=(font_family, 18), fg=text_color, bg="#282828")
        self.subtitle_label.pack(pady=(0,65))

        # Création du cadre pour placer les éléments côte à côte
        frame = tk.Frame(self, bg="#282828")
        frame.pack(pady=(15, 30), padx=20)

        self.code_label = tk.Label(frame, text="Code d'authentification créateur:", font=(font_family, 14), fg=text_color, bg="#282828")
        self.code_label.pack(side="left", padx=(0, 10))

        self.code_entry = tk.Entry(frame, show="*", bg="#282828", highlightbackground="#3c3c3c", font=(font_family, 16), fg=text_color, width=8)
        self.code_entry.pack(side="right", padx=(10, 0))
        
        # Configuration du bouton avec des effets de survol
        self.submit_button = tk.Button(self, text=" ".join("IMC Verification"), command=self.check_code, font=(font_family, 10), fg=text_color, bg=button_color, width=30)
        self.submit_button.pack(pady=5)
        self.submit_button.bind("<Enter>", lambda event: self.on_enter(event, button_color, button_color))
        self.submit_button.bind("<Leave>", lambda event: self.on_leave(event, button_hover_color, button_border_color))
        
        
        self.error_label = tk.Label(self, text="", font=(font_family, 12), fg="#3c3c3c", bg="#282828")
        self.error_label.pack()
        
        self.credit_label = tk.Label(self, text="credit to R.Silvers", font=("Helvetica", 8), fg=text_color, bg="#282828")
        self.credit_label.place(relx=1, rely=1, anchor='se')

    def on_enter(self, event, hover_color, border_color):
        event.widget.config(bg=hover_color)
        event.widget.config(highlightbackground=border_color)

    def on_leave(self, event, normal_color, border_color):
        event.widget.config(bg=normal_color)
        event.widget.config(highlightbackground=border_color)
        
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
                self.after(4000, lambda: self.show_second_msg(texte))
                self.after(10000, self.quit)

        self.code_entry.delete(0, 'end')

    def show_second_msg(self, text):
        self.error_label.config(text=text)
        
    def mdp_page(self):
        self.clear_window()

        # Rendre les écritures blanches pour tous les widgets
        text_color = "white"
        button_color = "#141414"
        button_hover_color = "#282828"
        button_border_color = "#3c3c3c"
        # Font et taille
        font_family = "Oswald"
        font_size = 24

        # Création du label pour la gestion des mots de passe
        self.mdp_label = tk.Label(self, text="Gestion des mots de passe", font=(font_family, font_size), fg=text_color, bg="#282828")
        self.mdp_label.pack(pady=10)

        # Création du sous-titre
        self.subtitle_label = tk.Label(self, text="I'm Marvin, but my best friends call me Pathfinder.", font=(font_family, 10), fg=text_color, bg="#282828")
        self.subtitle_label.pack()



        # Création de la zone de recherche
        self.search_entry = tk.Entry(self, bg="#282828", fg=text_color)
        self.search_entry.pack(pady=5)

        # Création de la liste des applications disponibles
        self.apps_listbox = tk.Listbox(self, bg="#282828", fg=text_color, font=(font_family, 12), selectbackground="#3c3c3c", selectforeground=text_color, height=10)
        self.apps_listbox.pack(pady=10, padx=10, fill="both", expand=True)

        # Ajout de quelques applications fictives à la liste
        applications = ["Application 1", "Application 2", "Application 3", "Application 4", "Application 5"]
        for app in applications:
            self.apps_listbox.insert(tk.END, app)

        # Création du bouton de sélection
        self.select_button = tk.Button(self, text="Sélectionner", command=self.select_app, fg=text_color, bg=button_color, font=(font_family, 16))
        self.select_button.pack(pady=10)

        # Liaison de l'événement de double clic à la fonction pour remplir l'entrée
        self.apps_listbox.bind("<Double-Button-1>", self.fill_entry)

        # Création du crédit
        self.credit_label = tk.Label(self, text="credit to R.Silvers", font=("Helvetica", 8), fg=text_color, bg="#282828")
        self.credit_label.place(relx=1, rely=1, anchor='se')


    def fill_entry(self, event):
        # Obtenir l'application sélectionnée dans la liste
        selected_app = self.apps_listbox.get(self.apps_listbox.curselection())
        
        # Remplir l'entrée avec le nom de l'application sélectionnée
        self.search_entry.delete(0, tk.END)
        self.search_entry.insert(0, selected_app)

        # Afficher le bouton "Sélectionner"
        self.select_button.pack(pady=10)

    def select_app(self):
        # Obtenir l'application sélectionnée dans l'entrée
        selected_app = self.search_entry.get()

        # Vérifier si l'application sélectionnée existe
        if selected_app in self.apps_listbox.get(0, tk.END):
            # Afficher la page de l'application sélectionnée
            self.app_page(selected_app)
        else:
            # Afficher un message d'erreur si l'application sélectionnée n'existe pas
            messagebox.showerror("Erreur", "L'application sélectionnée n'existe pas.")



    def app_page(self, selected_app):
        # Afficher la page de l'application sélectionnée
        print("Page de l'application:", selected_app)

        def on_enter(self, event, hover_color, border_color):
            event.widget.config(bg=hover_color, highlightbackground=border_color)

        def on_leave(self, event, color, border_color):
            event.widget.config(bg=color, highlightbackground=border_color)
        

if __name__ == "__main__":
    app = App()
    app.mainloop()