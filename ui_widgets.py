"""Contiene widgets personalizados para evitar duplicación de código"""

import tkinter as tk
from tkinter import ttk

class FrameMenu:
    def __init__(self, parent, text=None):
        label_frame = ttk.LabelFrame(
            parent,
            text=text
        )

        label_frame.rowconfigure(0, weight=1)
        label_frame.columnconfigure(0, weight=1)
        label_frame.pack(padx=5, pady=5)

        button = ttk.Button(
            label_frame
        )

        button.grid(row=2, padx=5, pady=5)

        self.fields = 0
        self.parent = parent
        self.button = button
        self.label_frame = label_frame

    def add_field(self, text=None, textvariable=None):
        field_label = ttk.Label(
            self.label_frame,
            text=text
        )

        field_entry = ttk.Entry(
            self.label_frame,
            textvariable=textvariable
        )

        field_label.grid(row=0, column=self.fields, padx=5, pady=5)
        field_entry.grid(row=1, column=self.fields, padx=5, pady=5)

        self.fields += 1
        self.button.grid(columnspan=self.fields)

    def set_button_name(self, text=None):
        self.button.config(text=text)

    def set_button_command(self, command=None):
        self.button.config(command=command)

def main():
    pass

if __name__ == "__main__":
    main()