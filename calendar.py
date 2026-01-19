import tkinter as tk
import calendar
from datetime import datetime

# Get current date
today = datetime.now()
year = today.year
month = today.month
current_day = today.day

# Create window
root = tk.Tk()
root.title("Baby Pink Calendar")
root.geometry("360x320")
root.configure(bg="#ffe4f2")  # baby pink background

# Header
header = tk.Label(
    root,
    text=f"{calendar.month_name[month]} {year}",
    font=("Helvetica", 16, "bold"),
    bg="#ffe4f2",
    fg="#a64d79"
)
header.pack(pady=10)

# Days of week
days_frame = tk.Frame(root, bg="#ffe4f2")
days_frame.pack()

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for day in days:
    tk.Label(
        days_frame,
        text=day,
        width=5,
        font=("Helvetica", 10, "bold"),
        bg="#ffb6d9",
        fg="#7a2c4f"
    ).pack(side="left", padx=1)

# Calendar grid
dates_frame = tk.Frame(root, bg="#ffe4f2")
dates_frame.pack(pady=10)

month_days = calendar.monthcalendar(year, month)

for r, week in enumerate(month_days):
    for c, day in enumerate(week):
        if day == 0:
            text = ""
            bg = "#ffe4f2"
        elif day == current_day:
            text = str(day)
            bg = "#ff8fc7"  # highlight today
        else:
            text = str(day)
            bg = "#fff0f7"

        tk.Label(
            dates_frame,
            text=text,
            width=5,
            height=2,
            font=("Helvetica", 10),
            bg=bg,
            fg="#7a2c4f",
            relief="ridge"
        ).grid(row=r, column=c, padx=2, pady=2)

root.mainloop()
