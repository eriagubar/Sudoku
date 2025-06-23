import random
import sys
from copy import deepcopy
from typing import List, Tuple, Optional

import tkinter as tk

# Crear ventana
ventana = tk.Tk()
ventana.title("Sudoku")

# Crear cuadritos para escribir números (9x9)
entradas = []
for fila in range(9):
    fila_entradas = []
    for col in range(9):
        entrada = tk.Entry(ventana, width=2, font=("Arial", 18), justify="center")
        entrada.grid(row=fila, column=col)
        fila_entradas.append(entrada)
    entradas.append(fila_entradas)

# Mostrar la ventana
ventana.mainloop()
