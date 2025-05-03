"""Una prueba pequeñita y humilde"""

import operations as db
import ui_widgets as ui
import tkinter as tk
from tkinter import ttk

def update_treeview():
    for row in treeview.get_children():
        treeview.delete(row)

    for data in db.read_data():
        treeview.insert("", index=0, values=data)

def add_sensor(sensor_variable, data_variable):
    db.insert_data(sensor_variable.get(), data_variable.get())
    update_treeview()

def update_sensor(home_variable, sensor_variable, data_variable):
    db.update_data(sensor_variable.get(), data_variable.get(), home_variable.get())
    update_treeview()

def delete_sensor(home_variable):
    db.delete_data((home_variable.get(),))
    update_treeview()

def main():
    # root
    root = tk.Tk()
    root.title("Prueba")
    root.geometry("800x800")
    root.resizable(False, False)

    # treeview
    global treeview

    treeview = ttk.Treeview(
        root,
        columns=("home_id", "sensor_name", "data"),
        show="headings"
    )

    treeview.heading("home_id", text="Casa")
    treeview.heading("sensor_name", text="Sensor")
    treeview.heading("data", text="Lectura")
    treeview.pack()
    update_treeview()

    # variables
    add_sensor_variable = tk.StringVar()
    add_data_variable = tk.DoubleVar()
    updt_home_variable = tk.IntVar()
    updt_sensor_variable = tk.StringVar()
    updt_data_variable = tk.DoubleVar()
    del_home_variable = tk.IntVar()
    
    # añadir fila
    lb_frame_add = ui.FrameMenu(parent=root, text="Añadir sensor")
    lb_frame_add.add_field(text="Nombre", textvariable=add_sensor_variable)
    lb_frame_add.add_field(text="Lectura", textvariable=add_data_variable)
    lb_frame_add.set_button_name(text="Añadir")
    lb_frame_add.set_button_command(command=lambda:
                                    add_sensor(add_sensor_variable, add_data_variable))
    
    # actualizar fila
    lb_frame_updt = ui.FrameMenu(parent=root, text="Modificar sensor")
    lb_frame_updt.add_field(text="Casa", textvariable=updt_home_variable)
    lb_frame_updt.add_field(text="Nombre", textvariable=updt_sensor_variable)
    lb_frame_updt.add_field(text="Lectura", textvariable=updt_data_variable)
    lb_frame_updt.set_button_name(text="Actualizar")
    lb_frame_updt.set_button_command(command=lambda:
                                     update_sensor(updt_home_variable, updt_sensor_variable, updt_data_variable))

    # eliminar fila
    lb_frame_del = ui.FrameMenu(parent=root, text="Eliminar sensor")
    lb_frame_del.add_field(text="Casa", textvariable=del_home_variable)
    lb_frame_del.set_button_name(text="Eliminar")
    lb_frame_del.set_button_command(command=lambda:
                                    delete_sensor(del_home_variable))

    # run
    root.mainloop()

if __name__ == "__main__":
    main()