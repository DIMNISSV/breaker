import tkinter as tk
import json
import time


class TimerApp:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Timer App")
        self.root.geometry("400x300")
        self.root.withdraw()

        # Read break and frequency data from JSON file
        with open('params.json') as f:
            params = json.load(f)
        self.break_duration = params['break_duration']
        self.break_frequency = params['break_frequency']

        # Schedule first break
        self.schedule_next_break()

        self.root.mainloop()

    def schedule_next_break(self):
        # Schedule the next break after `self.break_frequency` seconds
        self.root.after(int(self.break_frequency * 1000 + self.break_duration * 1000), self.start_break)

    def start_break(self):
        # Create full-screen window with break message and timer
        self.break_window = tk.Toplevel()
        self.break_window.attributes('-fullscreen', True)
        self.break_window.config(bg='black')
        self.break_window.bind('<Escape>', self.end_break)

        self.break_label = tk.Label(self.break_window, text="Break time!", font=("Arial", 30), fg='white', bg='black')
        self.break_label.pack(expand=True)

        self.timer_label = tk.Label(self.break_window, text="", font=("Arial", 20), fg='white', bg='black')
        self.timer_label.pack(expand=True)

        self.break_end_time = time.time() + self.break_duration
        self.update_timer()

    def update_timer(self):
        # Update timer label with remaining time
        time_left = self.break_end_time - time.time()
        if time_left <= 0:
            self.break_window.destroy()
            self.schedule_next_break()
        else:
            minutes, seconds = divmod(int(time_left), 60)
            time_str = f"{minutes:02d}:{seconds:02d}"
            self.timer_label.config(text=time_str)
            self.break_window.after(1000, self.update_timer)

    def end_break(self, event):
        # End break when user presses the Escape key
        self.break_window.destroy()
        self.schedule_next_break()


if __name__ == '__main__':
    app = TimerApp()
