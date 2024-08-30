import tkinter as tk
from bfs_search import bfs
from validation import load_breeding_data, validate_pals
import json

# Load the breeding data for validation
breeding_data = load_breeding_data('breeding_data.json')

# Function to start breeding based on user input from the GUI
def start_breeding():
    initial_pals = initial_pals_var.get().split(", ")
    target_pal = target_pal_var.get()
    
    # Validate the entered Pals
    is_valid, invalid_pals = validate_pals(initial_pals + [target_pal], breeding_data)
    
    if not is_valid:
        result = f"Invalid Pals found: {', '.join(invalid_pals)}"
        result_label.config(text=result)
        return
    
    path = bfs(graph, initial_pals, target_pal)
    if path:
        result = "BFS Path: " + " -> ".join([f"{p[0]} + {p[1]} = {p[2]}" for p in path])
    else:
        result = f"No path found to breed {target_pal} with the current Pals"
    
    result_label.config(text=result)

# Load the breeding graph data
with open('breeding_graph.json', 'r') as f:
    graph = json.load(f)

# Set up the main GUI window
root = tk.Tk()
root.title("Pal Breeding Path Finder")

# Initial Pals input
tk.Label(root, text="Enter Your Current Pals (comma-separated):").pack()
initial_pals_var = tk.StringVar(value="Lamball, Lifmunk, Chikipi, Kitsun")
initial_pals_entry = tk.Entry(root, textvariable=initial_pals_var, width=50)
initial_pals_entry.pack()

# Target Pal input
tk.Label(root, text="Enter Your Target Pal:").pack()
target_pal_var = tk.StringVar(value="Leezpunk")
target_pal_entry = tk.Entry(root, textvariable=target_pal_var, width=50)
target_pal_entry.pack()

# Button to start the breeding path search
tk.Button(root, text="Find Breeding Path", command=start_breeding).pack()

# Label to display the result
result_label = tk.Label(root, text="", wraplength=500)
result_label.pack()

# Start the GUI loop
root.mainloop()
