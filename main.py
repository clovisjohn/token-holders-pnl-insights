import csv
import pandas as pd
import tkinter as tk
from tkinter import ttk, filedialog
from pandastable import Table
from holders_info import get_results
from api_requests import get_dexscreener_price_usd

def start_program():
    global pair_address
    pair_address = pair_address_entry.get()
    
    file_path = user_addresses.get()
    with open(file_path, "r") as file:
        address_list = [line.strip() for line in file.readlines()]

    progress["maximum"] = len(address_list)
    results = get_results(address_list, pair_address, update_progress)
    
    if output_csv_var.get():
        output_csv(results)
        result_label.config(text="CSV file generated")
    else:
        display_results(results, table_frame)
        result_label.config(text="")

def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)
    
def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        user_addresses.set(file_path)


def output_csv(results):
    file_path = "results.csv"
    with open(file_path, "w", newline="") as csvfile:
        fieldnames = results[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)

def display_results(results, table_frame):
    results_dataframe = pd.DataFrame(results)
    table = Table(table_frame, dataframe=results_dataframe)
    table.show()
    
        
app = tk.Tk()
app.title("Token Info")

# Configure the row and column weights of the app
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

input_frame = ttk.Frame(app, padding="10")
input_frame.grid(row=0, column=0, sticky="nsew")

pair_address_label = ttk.Label(input_frame, text="Pair Address:")
pair_address_label.grid(row=0, column=0, sticky="w")
pair_address_entry = ttk.Entry(input_frame, width=50)
pair_address_entry.grid(row=0, column=1)

# Bind right-click event to the pair address entry field
pair_address_entry.bind("<Button-3>", show_context_menu)

user_address_label = ttk.Label(input_frame, text="Holders Addresses:")
user_address_label.grid(row=1, column=0, sticky="w")
user_addresses = tk.StringVar()
user_addresses_entry = ttk.Entry(input_frame, width=50, textvariable=user_addresses, state='readonly')
user_addresses_entry.grid(row=1, column=1)

load_addresses_button = ttk.Button(input_frame, text="\U0001F4C1", command=open_file_dialog)
load_addresses_button.grid(row=1, column=2)

output_csv_var = tk.BooleanVar()
output_csv_checkbox = ttk.Checkbutton(input_frame, text="Output CSV", variable=output_csv_var)
output_csv_checkbox.grid(row=2, column=0, sticky="w")

start_button = ttk.Button(input_frame, text="Start", command=start_program)
start_button.grid(row=2, column=1, sticky="e")

result_label = ttk.Label(input_frame, text="")
result_label.grid(row=3, column=0, columnspan=2)

progress = ttk.Progressbar(input_frame, orient="horizontal", length=300, mode="determinate")
progress.grid(row=4, column=0, columnspan=2, pady=(10, 0))

def update_progress(value):
    progress["value"] = value
    progress.update()

table_frame = tk.Frame(app, bg='#FFFFFF', bd=1, relief='solid', padx=10, pady=10)
table_frame.grid(row=1, column=0, sticky="nsew")

# Configure the row and column weights of the table_frame
app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(0, weight=1)

# Create context menu
context_menu = tk.Menu(app, tearoff=0)
context_menu.add_command(label="Cut", command=lambda: app.focus_get().event_generate("<<Cut>>"))
context_menu.add_command(label="Copy", command=lambda: app.focus_get().event_generate("<<Copy>>"))
context_menu.add_command(label="Paste", command=lambda: app.focus_get().event_generate("<<Paste>>"))

app.mainloop()

