import tkinter as tk
from tkinter import scrolledtext
from tkinter.font import Font
import subprocess


class CodeEditor(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Crear un texto monoespaciado
        font = Font(family="Courier New", size=12)

        # Frame para la numeración de líneas
        self.line_numbers = tk.Text(self, width=4, padx=5, takefocus=0, border=0,
                                    background="#f0f0f0", state="disabled", font=font)
        self.line_numbers.pack(side="left", fill="y")

        # Widget principal de edición de código
        self.text = tk.Text(self, wrap="none", font=font, undo=True, border=0,
                            background="#1e1e1e", foreground="#dcdcdc", insertbackground="white")
        self.text.pack(side="right", fill="both", expand=True)

        # Scrollbar sincronizado
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.sync_scroll)
        self.scrollbar.pack(side="right", fill="y")
        self.text.config(yscrollcommand=self.scrollbar.set)

        # Evento para actualizar numeración de líneas
        self.text.bind("<KeyRelease>", self.update_line_numbers)
        self.text.bind("<MouseWheel>", self.update_line_numbers)

        # Inicializa numeración
        self.update_line_numbers()

    def sync_scroll(self, *args):
        """Sincroniza el scroll del editor y la numeración de líneas."""
        self.text.yview(*args)
        self.line_numbers.yview(*args)

    def update_line_numbers(self, event=None):
        """Actualiza la numeración de líneas."""
        self.line_numbers.config(state="normal")
        self.line_numbers.delete("1.0", "end")
        lines = self.text.get("1.0", "end").split("\n")
        line_numbers = "\n".join(str(i) for i in range(1, len(lines)))
        self.line_numbers.insert("1.0", line_numbers)
        self.line_numbers.config(state="disabled")

    def get_code(self):
        """Obtiene el código del editor."""
        return self.text.get("1.0", "end").strip()

    def set_code(self, code):
        """Establece el contenido del editor."""
        self.text.delete("1.0", "end")
        self.text.insert("1.0", code)


def ejecutar_codigo():
    # Obtén el código del editor
    codigo = editor.get_code()

    # Ejecuta main.py con el código como entrada
    try:
        result = subprocess.run(
            ['python3', 'main.py'],  # Llama al archivo principal
            input=codigo,
            text=True,
            capture_output=True
        )
        output_area.delete("1.0", tk.END)
        if result.returncode == 0:
            output_area.insert(tk.END, result.stdout)  # Muestra la salida estándar
        else:
            output_area.insert(tk.END, f"Errores:\n{result.stderr}")  # Muestra errores si los hay
    except Exception as e:
        output_area.delete("1.0", tk.END)
        output_area.insert(tk.END, f"Error al ejecutar el código:\n{e}")


# Crear la ventana principal
root = tk.Tk()
root.title("Editor de Julia Simplificada")
root.geometry("800x600")

# Editor de código
editor = CodeEditor(root)
editor.pack(fill="both", expand=True, padx=5, pady=5)

# Botón para ejecutar el código
execute_button = tk.Button(root, text="Ejecutar", command=ejecutar_codigo)
execute_button.pack(pady=10)

# Salida para el resultado
output_area = scrolledtext.ScrolledText(root, height=10, width=50, background="#1e1e1e",
                                        foreground="#dcdcdc", insertbackground="white", font=("Courier New", 12))
output_area.pack(fill="x", padx=5, pady=5)

# Ejecuta la ventana principal
root.mainloop()
