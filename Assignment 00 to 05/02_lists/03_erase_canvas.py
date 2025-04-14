import tkinter as tk  # Tkinter library import karna for creating GUI

# Grid aur Eraser ke size define karte hain
CELL_SIZE = 40  # Har square ka size
ERASER_SIZE = 20  # Eraser ka size

def erase(event):
    """Jis cell ke upar mouse jayega, uska color white ho jayega"""
    x, y = event.x, event.y  # Mouse ka position lena
    items = canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)  # Mouse ke area ko check karna
    for item in items:
        canvas.itemconfig(item, fill="white")  # White color set karte hain (erase effect)

# Tkinter ka window create karna
root = tk.Tk()
root.title("Eraser Tool")

# Canvas create karna jisme shapes draw karenge
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Blue squares ka grid draw karna
for row in range(0, 400, CELL_SIZE):
    for col in range(0, 400, CELL_SIZE):
        canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")

# Mouse ke click ya drag par erase function ko call karenge
canvas.bind("<B1-Motion>", erase)

# Tkinter main loop (GUI window ko open rakhta hai)
root.mainloop()
