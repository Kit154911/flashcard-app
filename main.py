import tkinter as tk
from tkinter import messagebox

# --- PALETTE CONFIGURATION (Retro Game Boy / 16-Bit Colors) ---
COLOR_BG = "#1a1a24"        # Deep retro arcade dark background
COLOR_PANEL = "#2d2d3a"     # Lighter block frame
COLOR_TEXT = "#00ff66"      # Neon matrix/arcade green
COLOR_ACCENT = "#ff0055"    # Cyberpunk magenta
COLOR_WHITE = "#ffffff"

FONT_RETRO_LARGE = ("Courier", 20, "bold")
FONT_RETRO_SMALL = ("Courier", 12, "bold")

root = tk.Tk()
root.title("Flash!")
root.geometry("800x600")
root.configure(bg=COLOR_BG)

lbl = tk.Label(root, text="FLASH!", font=(FONT_RETRO_LARGE), fg=COLOR_TEXT, bg=COLOR_BG)
lbl.pack(pady=30)

dashboard = tk.Frame(root, bg=COLOR_PANEL, bd=4, relief="flat")
dashboard.pack(pady=20, padx=40, fill="both", expand=True)

try:
    img_logo =tk.PhotoImage(file="FLASH!_neon.png")
    lbl_title_image = tk.Label(root, image=img_logo, font=FONT_RETRO_LARGE, fg=COLOR_TEXT, bg=COLOR_BG, bd=0)
    lbl_title_image.pack(pady=15)
except Exception as e:
    lbl_title = tk.Label(root, text="=== FLASH! ===", font=FONT_RETRO_LARGE, fg=COLOR_TEXT, bg=COLOR_BG)
    lbl_title.pack(pady=15)


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
            cards.destroy()
    save = tk.Button(cards, text="SAVED CARD", command=save_flashcard, bg=COLOR_TEXT, fg=COLOR_BG, font=FONT_RETRO_SMALL, activebackground=COLOR_WHITE, bd=0, cursor="hand2")
    save.pack(pady=30)


add_card = tk.Button(root, text="[ ADD NEW CARD ]", command= add_cards, bg=COLOR_ACCENT, fg=COLOR_WHITE, font=FONT_RETRO_SMALL, activebackground=COLOR_TEXT, activeforeground=COLOR_BG, bd=0, padx=20, pady=10,cursor="hand2")
add_card.pack(pady=40)

root.mainloop()


