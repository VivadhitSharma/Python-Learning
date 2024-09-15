import tkinter as tk
class TypeSpeedGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("Typing Speed Application")
        self.frame = tk.Frame(self.root)
        self.root.mainloop()
if __name__ == "__main__":
    TypeSpeedGUI()