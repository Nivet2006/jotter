import tkinter as tk
from tkinter import filedialog

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        self.textarea = tk.Text(self.root, undo=True)
        self.textarea.pack(fill=tk.BOTH, expand=True)
        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", accelerator="Ctrl+N", command=self.new_file)
        file_menu.add_command(label="Open", accelerator="Ctrl+O", command=self.open_file)
        file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menubar)

    def new_file(self, event=None):
        self.textarea.delete("1.0", tk.END)

    def open_file(self, event=None):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
            self.textarea.delete("1.0", tk.END)
            self.textarea.insert(tk.END, content)

    def save_file(self, event=None):
        content = self.textarea.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(content)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.bind("<Control-n>", notepad.new_file)
    root.bind("<Control-o>", notepad.open_file)
    root.bind("<Control-s>", notepad.save_file)
    notepad.run()
