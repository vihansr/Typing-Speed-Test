import tkinter as tk
import time

class TypingSpeed:
    def __init__(self, root):
        self.root = root
        self.root.title("Test Your Speed!")
        self.root.geometry("400x300")

        self.frame1 = tk.Frame(root, width=400, height=300)
        self.frame2 = tk.Frame(root, width=400, height=300)
        self.frame3 = tk.Frame(root, width=400, height=300)

        self.title_label = tk.Label(self.frame1, text="Typing Speed Calculator", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        self.start_btn = tk.Button(self.frame1, text="Start", font=("Arial", 12, "bold"), padx=10, pady=5, command=self.typing_face)
        self.start_btn.pack(pady=50)

        self.frame1.pack(fill="both", expand=True)

    def typing_face(self):
        """Starts typing test"""
        self.starting_time = time.time()

        self.frame1.pack_forget()
        self.frame2.pack(fill="both", expand=True)

        self.typing_label = tk.Label(self.frame2, text="Start Typing!!!", font=("Arial", 16, "bold"))
        self.typing_label.pack(pady=10)

        self.text_box = tk.Text(self.frame2, font=("Arial", 14), height=5, width=30)
        self.text_box.pack()

        self.submit_btn = tk.Button(self.frame2, text="Submit", font=("Arial", 12, "bold"), padx=10, pady=5, command=self.stop)
        self.submit_btn.pack(pady=50)

    def stop(self):
        self.frame2.pack_forget()
        self.frame3.pack(fill="both", expand=True)

        elapsed_time = (time.time() - self.starting_time) / 60
        answer = self.text_box.get("1.0", tk.END).strip()
        answer_length = len(answer)

        wpm = (answer_length / 5) / elapsed_time if elapsed_time > 0 else 0

        tk.Label(self.frame3, text=f"Your Typing Speed: {wpm:.2f} WPM", font=("Arial", 12, "bold"), fg="blue").pack(pady=10)

        self.reset_btn = tk.Button(self.frame3, text="Restart", font=("Arial", 12, "bold"), padx=10, pady=5, command=self.restart)
        self.reset_btn.pack()

    def restart(self):
        """Resets the test and goes back to the start screen"""
        self.frame3.pack_forget()
        self.frame1.pack(fill="both", expand=True)


root = tk.Tk()
app = TypingSpeed(root)
root.mainloop()
