# Go Fish Game (Python + Tkinter)

This project implements the card game **Go Fish** as a desktop GUI application using Python's `tkinter` library. The game logic closely follows the classic rules of Go Fish, and the GUI reflects user actions in real-time.

---

## How to Play
- Two players (Player 1 and Player 2) take turns.
- On your turn, click one of your visible cards — this sets the rank to ask for.
- Click the **Ask** button to ask the opponent for that rank.
- If the opponent has cards of that rank:
  - All matching cards are transferred to your hand.
- If not:
  - You "Go Fish" — draw one card from the deck.
- After receiving or drawing a card, any **pair** of cards with the same rank is removed and counted.
- The turn switches.

---

## Game Logic

### 1. **Card Display and GUI Layout**
- Player 1 and Player 2 hands are displayed in separate sections.
- Current player’s hand is visible.
- Opponent’s hand is shown **briefly** when asked.
- Cards are buttons; clicking one updates the dropdown for rank selection.

### 2. **Ask Mechanism**
- When a player clicks **Ask**:
  - Opponent’s hand is revealed.
  - All matching cards of the requested rank are transferred, if any.
  - Otherwise, one card is drawn from the deck.

### 3. **Pairing System**
- After each action, the player’s hand is checked for pairs.
- If two cards of the same rank exist, they are removed, and pair count increases.

### 4. **Turn Switching**
- A short delay follows each turn (1000ms), then control switches to the other player.

### 5. **Game End**
- If either player runs out of cards:
  - A popup displays:
    - Who ran out of cards
    - Final pair counts
    - Winner announcement
  - The game exits after showing the result.

---

## Technologies Used
- **Python 3**
- **tkinter** (for GUI)
- **random** (for shuffling the deck)

---

## How It’s Structured
- `deck`: 52 shuffled cards
- `player1_hand`, `player2_hand`: lists of cards
- `current_turn`: integer tracking whose turn it is
- GUI is rebuilt dynamically with `build_gui()`
- Actions are tied to buttons and dropdowns

---

## Code Explanation by Function

### `build_gui(show_opponent=False)`
- Draws all UI elements: hands, pair labels, dropdown, buttons.
- If `show_opponent=True`, reveals both hands temporarily.
- Dynamically rebuilds the screen after every move.

### `get_current_player_ranks()`
- Returns a list of rank values (e.g. 'A', '4', 'K') from the current player's hand to populate the dropdown.

### `set_selected_rank(card)`
- Called when a card is clicked.
- Extracts the rank from the card and sets it as the selected rank in the dropdown.

### `ask_for_card()`
- Main gameplay function called when player clicks **Ask**.
- Checks opponent’s hand for the selected rank:
  - If found, transfers matching cards.
  - If not, draws one from the deck.
- Checks for and removes any pairs.
- Calls `build_gui(show_opponent=True)` to display both hands briefly.
- After 1000ms, calls `finish_turn()`.

### `check_for_pairs(hand, player)`
- Scans a hand and removes any two cards of the same rank.
- Increments the player’s pair counter (`player1_pairs` or `player2_pairs`).

### `finish_turn()`
- Called after the brief pause at the end of a turn.
- Switches the turn to the other player.
- Calls `build_gui()` again.
- Also checks if any player has an empty hand → if yes, calls `show_game_over()`.

### `show_game_over(winner)`
- Pops up a messagebox displaying who won the game, who ran out of cards, and the final pair counts.
- Ends the game by closing the window with `root.quit()`.

