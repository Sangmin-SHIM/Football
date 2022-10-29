import tkinter as tk
import tkinter.ttk as ttk
from param_url import all_leagues_list

global year, period, enter_league, data

def user_input_interface():
    window = tk.Tk()
    window.title("Year / Period / League")
    window.geometry('200x100')

    # Label Definition
    year = tk.Label(text="Year", font=("Arial Bold", 10))
    period = tk.Label(text="Period", font=("Arial Bold", 10))
    league = tk.Label(text="League", font=("Arial Bold", 10))

    # Input Area
    year_input = tk.Entry(window,width=10)
    period_input = tk.Entry(window,width=10)
    league_combobox_input = ttk.Combobox(window)
    league_combobox_input['values']= all_leagues_list()

    # Button
    # Function
    def button_clicked():
        year = year_input.get()
        period = period_input.get()
        enter_league =  league_combobox_input.get()
        print("hello, it's clicked : ", enter_league)
        data = [year, period, enter_league]
        return data

    button = tk.Button(window, text="Send", command=button_clicked)

    # Position
    year.grid(column=0, row=0)
    year_input.grid(column=1,row=0)
    period.grid(column=0, row=4)
    period_input.grid(column=1,row=4)
    league.grid(column=0, row=8)
    league_combobox_input.grid(column=1,row=8)
    button.grid(column=1,row=20)
    window.mainloop()
