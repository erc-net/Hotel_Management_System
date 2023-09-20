import tkinter as tk
from tkinter import messagebox
import mysql.connector
import subprocess

# Create a class for the login window
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("400x200")

        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(root, show="*")  # Hide the password
        self.password_entry.pack()

        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Connect to the MySQL database
        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="eric27",
                database="management"
            )
            cursor = conn.cursor()

            # Check if the username and password are correct
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()

            if user:
                messagebox.showinfo("Login Successful", "Welcome, " + username)
                conn.close()
                self.open_main()
                self.root.destroy()  # Close the login window
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")

            conn.close()
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", str(e))

    def open_main(self):
        # Launch the main.py script
        subprocess.Popen(["python", "hotel.py"])


if __name__ == "__main__":
    root = tk.Tk()
    login_window = LoginWindow(root)
    root.mainloop()
