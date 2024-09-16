#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:24:57 2024

@author: rsheissa
"""

import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Create the main window
root = tk.Tk()
root.title("Embedding Matplotlib in Tkinter with Scrollbar")

# Create a canvas
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Add a scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the canvas
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Create a frame inside the canvas
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Function to create and embed a Matplotlib figure
def create_matplotlib_figure():
    fig = Figure(figsize=(8, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot([0, 1, 2, 3], [0, 1, 4, 9])
    return fig

# Embed multiple figures
for i in range(5):  # Increase the number of figures to test scrolling
    fig = create_matplotlib_figure()
    figure_canvas = FigureCanvasTkAgg(fig, master=frame)
    figure_canvas.draw()
    figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Start the Tkinter main loop
root.mainloop()
