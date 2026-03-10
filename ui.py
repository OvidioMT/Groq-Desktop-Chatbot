import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
from config import PERSONALIDADES
from chatbot import Chatbot

class ChatbotUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot con Groq")
        self.root.configure(bg="#23272e")
        self.resize()

        self.personalidad_actual = tk.StringVar(value="Amigable")
        self.chatbot = Chatbot(self.personalidad_actual.get())
        self.personalidad_actual.trace_add('write', self.cambiar_personalidad)

        self.menu_frame = tk.Frame(self.root, bg="#23272e")
        self.menu_frame.pack(fill=tk.X, padx=10, pady=5)
        tk.Label(self.menu_frame, text="Personalidad:", bg="#23272e", fg="#f1f1f1", font=("Arial", 12)).pack(side=tk.LEFT)
        personalidad_menu = tk.OptionMenu(self.menu_frame, self.personalidad_actual, *PERSONALIDADES.keys())
        personalidad_menu.config(bg="#23272e", fg="#f1f1f1", font=("Arial", 12))
        personalidad_menu.pack(side=tk.LEFT, padx=5)

        self.chat_area = scrolledtext.ScrolledText(self.root, bg="#181a20", fg="#f1f1f1", font=("Arial", 13), wrap=tk.WORD)
        self.chat_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.chat_area.config(state='disabled')
        self.chat_area.tag_config('user_right', foreground='#00b4d8', font=("Arial", 13, "bold"), justify='right', lmargin1=300, lmargin2=300, spacing1=5, spacing2=5, spacing3=8)
        self.chat_area.tag_config('bot_left', foreground='#f9c74f', font=("Arial", 13), justify='left', lmargin1=10, lmargin2=10, spacing1=5, spacing2=5, spacing3=8)
        self.chat_area.tag_config('error', foreground='red', font=("Arial", 13, "italic"))

        self.entry_frame = tk.Frame(self.root, bg="#23272e")
        self.entry_frame.pack(fill=tk.X, padx=10, pady=5)
        self.entry = tk.Text(self.entry_frame, height=3, font=("Arial", 13), bg="#23272e", fg="#f1f1f1", insertbackground="#f1f1f1", wrap=tk.WORD)
        self.entry.pack(fill=tk.X, padx=5, pady=5, expand=True)
        self.entry.bind('<Return>', self.send_message)

        self.btn_frame = tk.Frame(self.root, bg="#23272e")
        self.btn_frame.pack(pady=5, fill=tk.X)
        send_btn = tk.Button(self.btn_frame, text="Enviar", command=self.send_message, bg="#00b4d8", fg="white", font=("Arial", 12, "bold"))
        send_btn.pack(side=tk.LEFT, padx=5)
        clear_btn = tk.Button(self.btn_frame, text="Limpiar", command=self.clear_chat, bg="#f94144", fg="white", font=("Arial", 12))
        clear_btn.pack(side=tk.LEFT, padx=5)
        save_btn = tk.Button(self.btn_frame, text="Guardar", command=self.save_chat, bg="#43aa8b", fg="white", font=("Arial", 12))
        save_btn.pack(side=tk.LEFT, padx=5)

    def resize(self):
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.geometry(f"{int(width*0.6)}x{int(height*0.85)}")

    def send_message(self, event=None):
        user_input = self.entry.get("1.0", tk.END).strip()
        if not user_input:
            return
        self.chat_area.config(state='normal')
        if float(self.chat_area.index('end-1c')) > 1.0:
            self.chat_area.insert(tk.END, "")
        self.chat_area.insert(tk.END, f"Tú: {user_input}\n\n\n", 'user_right')
        self.chatbot.add_user_message(user_input)
        self.entry.delete("1.0", tk.END)
        try:
            respuesta = self.chatbot.get_response()
            self.chat_area.insert(tk.END, f"Bot: {respuesta}\n\n\n", 'bot_left')
        except Exception as e:
            self.chat_area.insert(tk.END, f"Error: {e}\n", 'error')
        self.chat_area.config(state='disabled')
        self.chat_area.see(tk.END)
        if event:
            return 'break'

    def clear_chat(self):
        self.chat_area.config(state='normal')
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.config(state='disabled')
        self.chatbot.clear()

    def cambiar_personalidad(self, *args):
        self.chatbot.set_personalidad(self.personalidad_actual.get())
        self.clear_chat()

    def save_chat(self):
        conv = self.chat_area.get(1.0, tk.END)
        file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(conv)
            messagebox.showinfo("Guardado", "Conversación guardada correctamente.")
