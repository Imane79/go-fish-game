import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Go Fish - First to Empty Hand Wins")
root.geometry("500x400")

# ===== Player 1 =====
p1_frame = tk.Frame(root)
p1_frame.pack(pady=10)

tk.Label(p1_frame, text="Player 1's Hand:", font=(
    'Arial', 12, 'bold'), fg='blue').pack()
p1_hand_frame = tk.Frame(p1_frame)
p1_hand_frame.pack()
# Sample cards for now
for symbol in ['A♠', '4♦', 'Q♥']:
    tk.Button(p1_hand_frame, text=symbol, width=4).pack(side=tk.LEFT, padx=2)

tk.Label(p1_frame, text="Player 1's Pairs: 2").pack()

# ===== Player 2 =====
p2_frame = tk.Frame(root)
p2_frame.pack(pady=10)

tk.Label(p2_frame, text="Player 2's Hand:", font=(
    'Arial', 12, 'bold'), fg='blue').pack()
p2_hand_frame = tk.Frame(p2_frame)
p2_hand_frame.pack()
# Hidden cards
for _ in range(5):
    tk.Button(p2_hand_frame, text='🂠', width=4).pack(side=tk.LEFT, padx=2)

tk.Label(p2_frame, text="Player 2's Pairs: 1").pack()

# ===== Turn Info =====
action_frame = tk.Frame(root)
action_frame.pack(pady=10)

turn_label = tk.Label(
    action_frame, text="Player 1's turn - select a rank to ask for", fg='blue')
turn_label.pack()

# ===== Ask Dropdown and Button =====
ask_frame = tk.Frame(action_frame)
ask_frame.pack()

tk.Label(ask_frame, text="Ask for:").pack(side=tk.LEFT)

# Dynamically updated based on hand in future
ask_var = tk.StringVar()
ask_dropdown = ttk.Combobox(
    ask_frame, textvariable=ask_var, state="readonly", width=5)
ask_dropdown['values'] = ['A', '4', 'Q']  # Hardcoded for now
ask_dropdown.current(0)
ask_dropdown.pack(side=tk.LEFT, padx=5)

tk.Button(ask_frame, text="Ask").pack(side=tk.LEFT)

# ===== Show Opponent Cards Button =====
tk.Button(root, text="Show Opponent's Cards").pack(pady=5)

root.mainloop()
