import tkinter as tk
from tkinter import messagebox
import pandas as pd
import subprocess
import sys
from PIL import Image, ImageTk

# Read the exam CSV file
csv_file_path = 'exam.csv'
questions_df = pd.read_csv(csv_file_path)

# Get the username from the command line arguments
username = sys.argv[1] if len(sys.argv) > 1 else "User"

class ExamApp:
    def __init__(self, root, username):
        self.root = root
        self.root.title("Online MCQ Exam")
        self.current_question = 0
        self.score = 0
        self.questions = questions_df.to_dict('records')
        self.var = tk.IntVar(value=-1)  # Using a single IntVar for Radiobuttons

        # Initial window size
        self.window_width = int(self.root.winfo_screenwidth() * 0.8 * 1.2)
        self.window_height = int(self.root.winfo_screenheight() * 0.8 * 1.2)
        self.root.geometry(f"{self.window_width}x{self.window_height}")
        self.root.config(bg="#f4f4f9")

        # Load the background image
        self.bg_image = Image.open("1.jpg")
        self.bg_image_tk = None

        def set_bg_image(self):
            """Resize and set the background image."""
            self.bg_image_resized = self.bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.Resampling.LANCZOS)
            self.bg_image_tk = ImageTk.PhotoImage(self.bg_image_resized)
            self.canvas.create_image(0, 0, image=self.bg_image_tk, anchor='nw')

        # Create a canvas for the background image
        self.canvas = tk.Canvas(self.root, width=self.window_width, height=self.window_height)
        self.canvas.pack(fill='both', expand=True)

        # Set the background image on the canvas
        set_bg_image(self)

        # Create a frame to hold all content
        frame_width = 700 * 1.2
        frame_height = 600 * 1.2
        frame = tk.Frame(self.canvas, bg='#ffffff', bd=12, relief='ridge', width=frame_width, height=frame_height)
        frame.place(relx=0.5, rely=0.5, anchor='center')

        # Welcome message with username
        self.welcome_label = tk.Label(frame, text=f"Welcome, {username}!", font=("Arial", 20, "bold"), bg='white', fg='#007bff')
        self.welcome_label.pack(pady=20)

        # Title
        self.title_label = tk.Label(frame, text="MCQ Exam", font=("Arial", 32, "bold"), bg='white', fg='#28a745')
        self.title_label.pack(pady=20)

        # Question label
        self.question_label = tk.Label(frame, text="", wraplength=500, justify="left", bg='white', fg='#28a745', font=("Arial", 18))
        self.question_label.pack(pady=20)

        # Option buttons (radio buttons for single selection)
        self.option_buttons = []
        for i in range(4):
            button = tk.Radiobutton(frame, text="", variable=self.var, value=i, bg='white', fg='#28a745', font=("Arial", 14), indicatoron=0, padx=20, pady=10, width=30, command=self.animate_selection)
            button.pack(fill="x", padx=20, pady=10)
            self.option_buttons.append(button)

        # Navigation buttons
        self.submit_button = tk.Button(frame, text="Next", command=self.submit_answer, bg="#007bff", fg="white", font=("Arial", 16), width=20)
        self.submit_button.pack(pady=30)

        # Show the first question
        self.show_question()

        # Bind the resizing of the window to adjust the background image
        self.root.bind("<Configure>", self.on_resize)

    def set_bg_image(self):
        """Resize and set the background image."""
        self.bg_image_resized = self.bg_image.resize((self.window_width, self.window_height), Image.Resampling.LANCZOS)
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image_resized)
        self.canvas.create_image(0, 0, image=self.bg_image_tk, anchor='nw')

    def on_resize(self, event):
        """Handle window resizing and adjust background image accordingly."""
        # Get the new window size
        self.window_width = event.width
        self.window_height = event.height

        # Resize the background image to fit the new window size
        self.set_bg_image()

    def show_question(self):
        question = self.questions[self.current_question]
        self.question_label.config(text=f"Q{self.current_question + 1}: {question['question']}")
        options = [question['option1'], question['option2'], question['option3'], question['option4']]
        self.var.set(-1)  # Reset radio button selection
        for i, option in enumerate(options):
            self.option_buttons[i].config(text=option)

    def animate_selection(self):
        """Animate the selection of an option with a color change."""
        selected_index = self.var.get()

        if selected_index != -1:
            selected_button = self.option_buttons[selected_index]

            # Temporarily change button color to give feedback
            selected_button.config(bg="#d4edda")  # Light green background
            self.root.after(300, lambda: selected_button.config(bg="white"))  # Revert after 300ms

    def submit_answer(self):
        selected_answer = self.var.get()
        correct_answer = self.questions[self.current_question]['answer']

        if selected_answer == -1:
            messagebox.showwarning("Warning", "You must select an answer!")
            return

        selected_text = self.option_buttons[selected_answer].cget("text")
        if correct_answer == selected_text:
            self.score += 1

        self.current_question += 1

        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.end_exam()

    def end_exam(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"Exam completed! Your score: {self.score}/{len(self.questions)}", font=("Arial", 20, "bold"), bg='white', fg='#007bff').pack(pady=30)
        tk.Button(self.root, text="Logout", command=self.logout, bg="#007bff", fg="white", font=("Arial", 16), width=20).pack(pady=30)

    def logout(self):
        self.root.destroy()
        subprocess.run(['python3', 'registration.py'])  # Redirect to registration.py

def start_exam():
    try:
        root = tk.Tk()
        username = sys.argv[1] if len(sys.argv) > 1 else "User"
        app = ExamApp(root, username)
        root.mainloop()
    except KeyboardInterrupt:
        print("Exam interrupted by the user. Exiting gracefully...")
        sys.exit(0)

if __name__ == "__main__":
    start_exam()
