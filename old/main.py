import tkinter as ttk
from tkinter import messagebox
import login  # This assumes your login.py is properly set up
import time

def show_login_window():
    login_window = ttk.Toplevel()
    login_window.title("Login")

    ttk.Label(login_window, text="Username:").pack()
    username_entry = ttk.Entry(login_window)
    username_entry.pack()

    ttk.Label(login_window, text="Password:").pack()
    password_entry = ttk.Entry(login_window, show="*")
    password_entry.pack()

    ttk.Button(login_window, text="Login",
              command=lambda: attempt_login(username_entry.get(), password_entry.get(), login_window)).pack()

    ttk.Button(login_window, text="Register",
              command=lambda: attempt_registration(username_entry.get(), password_entry.get(), login_window)).pack()

def attempt_login(username, password, window):
    if login.login(username, password):
        messagebox.showinfo("Login Success", "You are now logged in!")
        window.destroy()  # Close the login window
        show_main_application_window()  # Function to create your main app window
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password.")

def attempt_registration(username, password, window):
    if login.register(username, password):
        messagebox.showinfo("Registration Success", "You are now registered and can log in.")
        #window.destroy()  # Optionally close the login window, or prompt to log in now
    else:
        messagebox.showerror("Registration Failed", "This username is already taken.")

def show_main_application_window():
    def update_time():
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        time_label.config(text=current_time)
        root.after(1000, update_time)

    root = ttk.Toplevel()  # Create a new top-level window
    root.title("My Python App")

    main_frame = ttk.Frame(root, padding="30 30 30 30")
    main_frame.grid(column=0, row=0, sticky=(ttk.W, ttk.E, ttk.N, ttk.S))

    time_label = ttk.Label(main_frame, text="", font=("Helvetica", 16))
    time_label.grid(column=0, row=0, sticky=ttk.W)

    username_label = ttk.Label(main_frame, text="Username", font=("Helvetica", 20))
    username_label.grid(column=1, row=1)

    logout_button = ttk.Button(main_frame, text="Logout")
    logout_button.grid(column=2, row=0, sticky=ttk.E)

    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=3)
    main_frame.columnconfigure(2, weight=1)
    main_frame.rowconfigure(1, weight=1)

    update_time()

    root.mainloop()



# Initialize the main application (this could also be your initial login or registration window)
if __name__ == "__main__":
    root = ttk.Tk()
    root.withdraw()  # Hide the main window (use show_login_window to show the login interface instead)
    show_login_window()
    root.mainloop()

