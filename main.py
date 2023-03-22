import tkinter as tk
from tkinter import ttk
from holders_info import get_results
from tkinter_gui import update_progress,output_csv,display_results,app,user_addresses,pair_address_entry,input_frame,result_label,progress,output_csv_var,table_frame

def start_program():
    pair_address_ = pair_address_entry.get()
    
    file_path = user_addresses.get()
    with open(file_path, "r") as file:
        address_list = [line.strip() for line in file.readlines()]

    progress["maximum"] = len(address_list)
    results = get_results(address_list, pair_address_, update_progress)
    
    if output_csv_var.get():
        output_csv(results)
        result_label.config(text="CSV file generated")
    else:
        display_results(results, table_frame)
        result_label.config(text="")

    
start_button = ttk.Button(input_frame, text="Start", command=start_program)
start_button.grid(row=2, column=1, sticky="e")

app.mainloop()

