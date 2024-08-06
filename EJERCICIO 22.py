#Capitulo 4. Ejercicio propuesto 22

import tkinter as tk
from tkinter import messagebox

def calcular_salario():
    try:
        nombre = entry_nombre.get()
        salario_por_hora = float(entry_salario_por_hora.get())
        horas_trabajadas = int(entry_horas_trabajadas.get())
        salario_mensual = salario_por_hora * horas_trabajadas

        resultado = f"Nombre: {nombre}"
        if salario_mensual > 450000:
            resultado += f"\nSalario mensual: ${salario_mensual:}"

        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores válidos.")

ventana = tk.Tk()
ventana.title("Cálculo de Salario")

tk.Label(ventana, text="Nombre del empleado:").grid(row=0, column=0)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1)

tk.Label(ventana, text="Salario básico por hora:").grid(row=1, column=0)
entry_salario_por_hora = tk.Entry(ventana)
entry_salario_por_hora.grid(row=1, column=1)

tk.Label(ventana, text="Horas trabajadas al mes:").grid(row=2, column=0)
entry_horas_trabajadas = tk.Entry(ventana)
entry_horas_trabajadas.grid(row=2, column=1)

tk.Button(ventana, text="Resultado", command=calcular_salario).grid(row=3, column=0, columnspan=2)

ventana.mainloop()
