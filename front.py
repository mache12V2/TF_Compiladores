import tkinter as tk
from tkinter import scrolledtext
from tkinter.font import Font
import subprocess


class CodeEditor(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        font = Font(family="Courier New", size=12)

        self.line_numbers = tk.Text(self, width=4, padx=5, takefocus=0, border=0,
                                    background="#f0f0f0", state="disabled", font=font)
        self.line_numbers.pack(side="left", fill="y")

        self.text = tk.Text(self, wrap="none", font=font, undo=True, border=0,
                            background="#1e1e1e", foreground="#dcdcdc", insertbackground="white")
        self.text.pack(side="right", fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.sync_scroll)
        self.scrollbar.pack(side="right", fill="y")
        self.text.config(yscrollcommand=self.scrollbar.set)

        self.text.bind("<KeyRelease>", self.update_line_numbers)
        self.text.bind("<MouseWheel>", self.update_line_numbers)

        self.update_line_numbers()

    def sync_scroll(self, *args):
        self.text.yview(*args)
        self.line_numbers.yview(*args)

    def update_line_numbers(self, event=None):
        self.line_numbers.config(state="normal")
        self.line_numbers.delete("1.0", "end")
        lines = self.text.get("1.0", "end").split("\n")
        line_numbers = "\n".join(str(i) for i in range(1, len(lines)))
        self.line_numbers.insert("1.0", line_numbers)
        self.line_numbers.config(state="disabled")

    def get_code(self):
        return self.text.get("1.0", "end").strip()

    def set_code(self, code):
        self.text.delete("1.0", "end")
        self.text.insert("1.0", code)


def ejecutar_codigo():
    codigo = editor.get_code()

    try:
        result = subprocess.run(
            ['python3', 'main.py'],  
            input=codigo,
            text=True,
            capture_output=True
        )

        output_area.delete("1.0", tk.END)
        if result.returncode == 0:
            output_area.insert(tk.END, "Sintaxis válida. Ejecutando el código...\n")
            ejecutar_codigo_real(codigo)
        else:
            output_area.insert(tk.END, f"Errores de sintaxis:\n{result.stderr}")
    except Exception as e:
        output_area.delete("1.0", tk.END)
        output_area.insert(tk.END, f"Error al validar el código:\n{e}")


def ejecutar_codigo_real(codigo):
    try:
        result = subprocess.run(
            ['python3', '-c', codigo],  
            text=True,
            capture_output=True
        )
        if result.returncode == 0:
            output_area.insert(tk.END, f"Salida:\n{result.stdout}")
        else:
            output_area.insert(tk.END, f"Errores de ejecución:\n{result.stderr}")
    except Exception as e:
        output_area.insert(tk.END, f"Error al ejecutar el código:\n{e}")


root = tk.Tk()
root.title("Editor de Julia Simplificada")
root.geometry("800x600")

editor = CodeEditor(root)
editor.pack(fill="both", expand=True, padx=5, pady=5)

execute_button = tk.Button(root, text="Ejecutar", command=ejecutar_codigo)
execute_button.pack(pady=10)

output_area = scrolledtext.ScrolledText(root, height=10, width=50, background="#1e1e1e",
                                        foreground="#dcdcdc", insertbackground="white", font=("Courier New", 12))
output_area.pack(fill="x", padx=5, pady=5)


root.mainloop()
