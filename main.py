import tkinter as tk #ui package




# functions
cordinates = ""
def get_location():
    print("get location")

def load_data():
	# do something
    print("load data")


# here we setup the UI

window = tk.Tk()
window.title("ELA Sentiment Analysis")
window.geometry("700x400")

# Application title label
title_label = tk.Label(text="ELA AS - Twitter data analysis")
title_label.place(x=350, y=20, anchor="center")

# Other UI elements

# 			get location
input_address_label = tk.Label(text="Input the address to get the location")
input_address_label.place(x=350, y=80, anchor="center")

address_label = tk.Label(text="Address: ")
address_label.place(x=350, y=135, anchor="center")

address_entry = tk.Entry(justify='center')
address_entry.place(x=350, y=105, anchor="center")

# range_entry = tk.Entry(justify='center')
# range_entry.place(x=480, y=105, width=50, anchor="center")

address_button = tk.Button(text="Locate", command=get_location)
address_button.place(x=350, y=165, anchor="center")


# 			search for tweets

input_text_label = tk.Label(text="Input the text and the # of tweets you want to search: ")
input_text_label.place(x=350, y=220, anchor="center")

text_entry = tk.Entry(justify='center')
text_entry.place(x=350, y=250, anchor="center")

number_entry = tk.Entry(justify='center')
number_entry.place(x=480, y=250, width=50, anchor="center")

input_range_label = tk.Label(text="Range of the address (miles): ")
input_range_label.place(x=350, y=280, anchor="center")

range_entry = tk.Entry(justify='center')
range_entry.place(x=480, y=280, width=50, anchor="center")

load_data_button = tk.Button(text="Analyze data",state=tk.DISABLED, command=load_data)
load_data_button.place(x=350, y=310, anchor="center")


window.mainloop()
