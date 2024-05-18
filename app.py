import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("Hello World App")

# Set the size of the window
root.geometry("300x100")

# Create a label widget with "Hello World" text
hello_label = tk.Label(root, text="Hello, World!")

# Pack the label widget into the window
hello_label.pack(pady=20)

# Run the application
root.mainloop()
