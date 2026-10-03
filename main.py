import tkinter as tk
from tkinter import messagebox
import json
import os

# --- PALETTE CONFIGURATION (Retro Game Boy / 16-Bit Colors) ---
COLOR_BG = "#1a1a24"        # Deep retro arcade dark background
COLOR_PANEL = "#2d2d3a"     # Lighter block frame
COLOR_TEXT = "#00ff66"      # Neon matrix/arcade green
COLOR_ACCENT = "#ff0055"    # Cyberpunk magenta
COLOR_WHITE = "#ffffff"

FONT_RETRO_LARGE = ("Courier", 20, "bold")
FONT_RETRO_SMALL = ("Courier", 12, "bold")

JSON_FILE = "flashcards.json"
flashcards = []
current_card_idx = 0
showing_front = True

def show_page(page_frame):
    page_frame.tkraise()

def select_deck():
    load_deck()
    if flashcards:
        show_card_state()
        show_page(frame_study_page)
    else:
        messagebox.showwarning("DECK EMPTY", "PLEASE ADD CARDS")     

def load_deck():
    global flashcards
    if os.path.exists(JSON_FILE):
        try:
            with open(JSON_FILE, "r") as f:
                flashcards = json.load(f)
        except Exception as e:
            print(f"Error reading JSON file, loading defaults: {e}")
            flashcards = []
    else:
        flashcards = [
            {"front": "What is FLASH!?", "back": "A flashcard app intended to gamify the studying process"},
            {"front": "What is FLASH! made with?", "back": "Python"}
        ]

        save_deck()

def save_deck():
    try:
        with open(JSON_FILE, "w") as f:
            json.dump(flashcards, f, indent=4)
        print("DECK SAVED!")
    except Exception as e:
        messagebox.showerror("SYSTEM ERROR", f"COULD NOT SAVE FILE:\n{e}")

def show_card_state():
    global showing_front
    showing_front = True
    btn_flip.config(text="[ FLIP CARD ]")

    if flashcards:
        lbl_card_text.config(text=flashcards[current_card_idx]["front"], fg=COLOR_WHITE)
    else:
        lbl_card_text.config(text="NO CARDS FOUND", fg=COLOR_ACCENT)

def flip_card():
    global showing_front, current_card_idx
    if not flashcards: return
    if showing_front:
        lbl_card_text.config(text=flashcards[current_card_idx]["back"], fg=COLOR_TEXT)
    else:
        current_card_idx = (current_card_idx + 1) % len(flashcards)
        show_card_state()

root = tk.Tk()
root.title("Flash!")
root.geometry("800x600")
root.configure(bg=COLOR_BG)

root.grid_rowconfigure(0, weight= 1)
root.grid_columnconfigure(0, weight= 1)

frame_menu_page = tk.Frame(root, bg=COLOR_BG)
frame_study_page = tk.Frame(root, bg=COLOR_BG)

for frame in (frame_menu_page, frame_study_page):
    frame.grid(row=0, column=0, sticky="nsew")

try:
    img_logo =tk.PhotoImage(file="FLASH!_neon.png")
    lbl_title_image = tk.Label(frame_menu_page, image=img_logo, font=FONT_RETRO_LARGE, fg=COLOR_TEXT, bg=COLOR_BG, bd=0)
    lbl_title_image.pack(pady=15)
except Exception as e:
    lbl_title = tk.Label(frame_menu_page, text="=== FLASH! ===", font=FONT_RETRO_LARGE, fg=COLOR_TEXT, bg=COLOR_BG)
    lbl_title.pack(pady=15)

btn_select_deck = tk.Button(frame_menu_page, text="[ LOAD DEFAULT DECK ]", command=select_deck, bg=COLOR_TEXT, fg=COLOR_BG, font=FONT_RETRO_SMALL, bd=0, padx=20, pady=15, cursor="hand2")
btn_select_deck.pack(pady=25)

def add_cards():
    cards = tk.Toplevel(root)
    cards.title("Add Cards")
    cards.geometry("500x400")
    cards.configure(bg=COLOR_PANEL)
    cards.transient(root)
    cards.grab_set()

    label_front = tk.Label(cards, text="[ ENTER QUESTION ]", fg=COLOR_TEXT, bg=COLOR_PANEL, font=FONT_RETRO_SMALL)
    label_front.pack(pady=15)

    entry_front = tk.Entry(cards, font=FONT_RETRO_SMALL, bg=COLOR_BG, fg=COLOR_WHITE, insertbackground=COLOR_WHITE, bd=3, relief="flat", width=40)
    entry_front.pack(pady=5)

    label_back = tk.Label(cards, text="[ ENTER ANSWER ]", fg=COLOR_TEXT, bg=COLOR_PANEL, font=FONT_RETRO_SMALL)
    label_back.pack(pady=15)

    entry_back = tk.Entry(cards, font=FONT_RETRO_SMALL, bg=COLOR_BG, fg=COLOR_WHITE, insertbackground=COLOR_WHITE, bd=3, relief="flat", width=40)
    entry_back.pack(pady=5)

    def save_flashcard():
        question = entry_front.get()
        answer = entry_back.get()

        if not question or not answer:
            messagebox.showwarning("ERROR", "PLEASE FILL OUT ALL FIELDS")
            return

        confirm = messagebox.askyesno("CONFIRM", f"SAVE THIS CARD?\n\nQ: {question}\nA: {answer}")

        if confirm:
            print(f"Saved card! Q: {question} | A: {answer}")
            flashcards.append({"front": f"[ {question} ]", "back": answer})
            save_deck()
            cards.destroy()
    save = tk.Button(cards, text="SAVE CARD", command=save_flashcard, bg=COLOR_TEXT, fg=COLOR_BG, font=FONT_RETRO_SMALL, activebackground=COLOR_WHITE, bd=0, cursor="hand2")
    save.pack(pady=30)


add_card = tk.Button(frame_menu_page, text="[ ADD NEW CARD ]", command= add_cards, bg=COLOR_ACCENT, fg=COLOR_WHITE, font=FONT_RETRO_SMALL, activebackground=COLOR_TEXT, activeforeground=COLOR_BG, bd=0, padx=20, pady=10,cursor="hand2")
add_card.pack(pady=40)

dashboard = tk.Frame(frame_study_page, bg=COLOR_BG, bd=0)
dashboard.pack(pady=20, padx=40, fill="both", expand=True)

try:
    img_card_bg = tk.PhotoImage(file="flashcard.png")
    lbl_card_display = tk.Label(dashboard, image=img_card_bg, compound="center", bg=COLOR_BG, bd=0)
    lbl_card_display.pack(expand=True)

    lbl_card_text = tk.Label(lbl_card_display, text="", font=FONT_RETRO_LARGE, fg=COLOR_WHITE, bg="#2d2d3a", wraplength=450, justify="center")
    lbl_card_text.place(relx=0.5, rely=0.5, anchor="center")
except Exception:
    lbl_card_text = tk.Label(dashboard, text="", font=FONT_RETRO_LARGE, fg=COLOR_WHITE, bg=COLOR_PANEL, wraplength=550, justify="center")
    lbl_card_text.pack(expand=True, fill="both", pady=20)

btn_flip = tk.Button(frame_study_page, text="[ FLIP CARD ]", command=flip_card, bg=COLOR_TEXT, fg=COLOR_BG, font=FONT_RETRO_SMALL, bd=0, padx=20, pady=12, cursor="hand2")
btn_flip.pack(pady=10)

btn_menu = tk.Button(frame_study_page, text="[ RETURN TO MENU ]", command=lambda: show_page(frame_menu_page), bg=COLOR_PANEL, fg=COLOR_WHITE, font=FONT_RETRO_SMALL, bd=0, padx=15, pady=8, cursor="hand2")
btn_menu.pack(pady=15)

load_deck()
show_page(frame_menu_page)

root.mainloop()


