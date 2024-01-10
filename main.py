# Import the required modules
import time
import tkinter as tk
from tkinter import messagebox, simpledialog


# Function to update the time
def update_time():
    # Get the current time
    current_time = time.strftime("%H:%M:%S")
    # Update the time label
    time_label.config(text=current_time)
    # Check if the alarm is set
    check_alarm(current_time)
    # Call update_time() again after 1 second
    root.after(1000, update_time)


# Function to set the alarm
def set_alarm():
    # Use simple dialog to ask for the alarm time
    alarm_time = simpledialog.askstring("Set Alarm", "Enter alarm time in HH:MM format")
    # Check if the user entered a time
    if alarm_time:
        try:
            # This will raise ValueError if the time format is incorrect
            time.strptime(alarm_time, "%H:%M")
            # Check if the alarm time is in the future
            if alarm_time < time.strftime("%H:%M"):
                # If not, show an error message
                messagebox.showerror("Error", "Alarm time must be in the future.")
                return
            # Set the alarm
            global alarm_set
            alarm_set = alarm_time
            # Update the alarm label
            alarm_label.config(text=f"ALARM: {alarm_time}")
        except ValueError as value:
            messagebox.showerror("Error", "Please enter time in HH:MM format.")


# Function to clear the alarm
def clear_alarm():
    # Clear the alarm
    global alarm_set
    alarm_set = None
    # Clear the alarm label
    alarm_label.config(text="")


# Function to check the alarm
def check_alarm(current_time):
    # Check if the alarm is set and the current time is greater than the alarm time
    if alarm_set and current_time > alarm_set:
        # Show a warning message
        messagebox.showwarning("Alarm", "Wake up! It's time!")
        # Clear the alarm
        clear_alarm()


# Function to create the main window
def create_main_window():
    # Set the window size (width x height)
    window_width = 600
    window_height = 300
    root.geometry(f'{window_width}x{window_height}')
    # Get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # Find the center position
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    # Set the position of the window to the center of the screen
    root.geometry(f'+{center_x}+{center_y}')


# Function to create the labels
def create_labels():
    # Create and place the time label
    _time_label = tk.Label(root, font=('Helvetica', 100), bg='black', fg='white')
    _time_label.pack(expand=True, fill='both')
    # Create and configure the alarm label to show the alarm time in smaller letters
    _alarm_label = tk.Label(root, font=('Helvetica', 25), bg='black', fg='red')
    _alarm_label.pack(expand=True, fill='both')
    # Return the labels
    return _time_label, _alarm_label


# Function to create the buttons
def create_buttons():
    # Button frame
    button_frame = tk.Frame(root)
    button_frame.pack(fill='x', expand=True)
    # Create a button to open the modal dialog and set the alarm
    set_alarm_button = tk.Button(button_frame, text="Set Alarm", command=set_alarm, font=('Helvetica', 18))
    set_alarm_button.pack(side='left', padx=5, pady=20)
    # Create a button to clear the set alarm
    clear_alarm_button = tk.Button(button_frame, text="Clear Alarm", command=clear_alarm, font=('Helvetica', 18))
    clear_alarm_button.pack(side='right', padx=5, pady=20)


# Main program
if __name__ == '__main__':
    # Create the main window
    root = tk.Tk()
    root.title("Tkinter Alarm Clock")
    create_main_window()
    # Initialize alarm_set variable
    alarm_set = None
    # Create the labels
    time_label, alarm_label = create_labels()
    # Create the buttons
    create_buttons()
    # Initial call to display the time
    update_time()
    # Run the application
    root.mainloop()
