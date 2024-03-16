import tkinter as tk  # Import the Tkinter module for creating GUI
from time import strftime  # Import strftime function from time module to get current time

# Function to update time every second
def update_time():
    current_time = strftime('%H:%M:%S %p')  # Get current time in HH:MM:SS format with AM/PM
    label.config(text=current_time)  # Update the text of the label to display current time
    label.after(1000, update_time)  # Call update_time function again after 1000ms (1 second)

# Create the main window
root = tk.Tk()
root.title('Digital Clock')  # Set the title of the window

# Create a label to display the time
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='cyan')
label.pack(anchor='center')  # Pack the label in the center of the window

# Call the update_time function to start updating the time
update_time()

# Start the Tkinter event loop
root.mainloop()
