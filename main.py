import tkinter as tk
from tkinter import ttk
import random

root = tk.Tk()
root.title("Go Fish - First to Empty Hand Wins")
root.geometry("600x500")

# ====== Deck Setup ======
suits = ['♠', '♣', '♦', '♥']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = [f"{rank}{suit}" for suit in suits for rank in ranks]
random.shuffle(deck)

# ====== Game State ======
player1_hand = [deck.pop() for _ in range(3)]
player2_hand = [deck.pop() for _ in range(5)]
player1_pairs = 0
player2_pairs = 0
current_turn = 1  # 1 = Player 1, 2 = Player 2
selected_rank = tk.StringVar()

# ====== GUI Layout ======


def build_gui():
    global p1_frame, p2_frame, ask_dropdown, p1_hand_frame, p2_hand_frame, turn_label, show_button
    for widget in root.winfo_children():
        widget.destroy()

    # Player 1
    p1_frame = tk.Frame(root)
    p1_frame.pack(pady=10)
    tk.Label(p1_frame, text="Player 1's Hand:", font=(
        "Arial", 12, "bold"), fg='blue').pack()
    p1_hand_frame = tk.Frame(p1_frame)
    p1_hand_frame.pack()
    if current_turn == 1:
        for card in player1_hand:
            btn = tk.Button(p1_hand_frame, text=card, width=4,
                            command=lambda c=card: set_selected_rank(c))
            btn.pack(side=tk.LEFT, padx=2)
    else:
        for _ in player1_hand:
            tk.Button(p1_hand_frame, text='🂠', width=4).pack(
                side=tk.LEFT, padx=2)
    tk.Label(p1_frame, text=f"Player 1's Pairs: {player1_pairs}").pack()

    # Player 2
    p2_frame = tk.Frame(root)
    p2_frame.pack(pady=10)
    tk.Label(p2_frame, text="Player 2's Hand:",
             font=("Arial", 12, "bold")).pack()
    p2_hand_frame = tk.Frame(p2_frame)
    p2_hand_frame.pack()
    if current_turn == 2:
        for card in player2_hand:
            btn = tk.Button(p2_hand_frame, text=card, width=4,
                            command=lambda c=card: set_selected_rank(c))
            btn.pack(side=tk.LEFT, padx=2)
    else:
        for _ in player2_hand:
            tk.Button(p2_hand_frame, text='🂠', width=4).pack(
                side=tk.LEFT, padx=2)
    tk.Label(p2_frame, text=f"Player 2's Pairs: {player2_pairs}").pack()

    # Turn label
    action_frame = tk.Frame(root)
    action_frame.pack(pady=10)
    turn_text = f"Player {current_turn}'s turn - select a rank to ask for"
    turn_label = tk.Label(action_frame, text=turn_text, fg='blue')
    turn_label.pack()

    # Ask section
    ask_frame = tk.Frame(action_frame)
    ask_frame.pack()
    tk.Label(ask_frame, text="Ask for:").pack(side=tk.LEFT)
    ask_dropdown = ttk.Combobox(
        ask_frame, textvariable=selected_rank, state="readonly", width=5)
    ask_dropdown['values'] = get_current_player_ranks()
    if ask_dropdown['values']:
        ask_dropdown.set(ask_dropdown['values'][0])
    ask_dropdown.pack(side=tk.LEFT, padx=5)
    tk.Button(ask_frame, text="Ask", command=ask_for_card).pack(side=tk.LEFT)

    # Show Opponent Button
    show_button = tk.Button(
        root, text="Show Opponent's Cards", command=swap_turn)
    show_button.pack(pady=10)


def get_current_player_ranks():
    hand = player1_hand if current_turn == 1 else player2_hand
    # extract ranks only
    return list(sorted(set([card[:-1] for card in hand])))


def set_selected_rank(card):
    rank = card[:-1]
    selected_rank.set(rank)
    ask_dropdown.set(rank)


def ask_for_card():
    global player1_hand, player2_hand, current_turn
    rank = selected_rank.get()
    if current_turn == 1:
        match = [card for card in player2_hand if card.startswith(rank)]
        if match:
            for card in match:
                player2_hand.remove(card)
                player1_hand.append(card)
        else:
            if deck:
                player1_hand.append(deck.pop())
        check_for_pairs(player1_hand, 1)
    else:
        match = [card for card in player1_hand if card.startswith(rank)]
        if match:
            for card in match:
                player1_hand.remove(card)
                player2_hand.append(card)
        else:
            if deck:
                player2_hand.append(deck.pop())
        check_for_pairs(player2_hand, 2)

    swap_turn()


def swap_turn():
    global current_turn
    current_turn = 2 if current_turn == 1 else 1
    build_gui()


def check_for_pairs(hand, player):
    global player1_pairs, player2_pairs
    rank_counts = {}

    # Count ranks
    for card in hand:
        rank = card[:-1]
        rank_counts[rank] = rank_counts.get(rank, 0) + 1

    # Check for pairs
    for rank in list(rank_counts.keys()):
        while rank_counts[rank] >= 2:
            # Remove two cards with this rank
            removed = 0
            for card in hand[:]:  # iterate over copy
                if card.startswith(rank):
                    hand.remove(card)
                    removed += 1
                    if removed == 2:
                        break
            # Update pair counter
            if player == 1:
                player1_pairs += 1
            else:
                player2_pairs += 1
            rank_counts[rank] -= 2


# Start the game
build_gui()
root.mainloop()
