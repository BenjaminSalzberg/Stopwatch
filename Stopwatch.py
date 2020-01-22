import time
import tkinter
from datetime import datetime

root = tkinter.Tk()  # creates a tkinter base
root.geometry("300x200")  # gives the size of the tkinter window
root.title('Stopwatch')  # gives the title of the tkinter window
var = tkinter.StringVar()  # creates an updating string for the tkinter window
label = tkinter.Message(root, textvariable=var, relief=tkinter.RAISED, width=150)
# creates the label in tkinter with the variable var in the tkinter window
var.set(value="Not Counting")  # defines current text of variable var

CurrTime = tkinter.StringVar()  # creates another updating string var
CountedTime = tkinter.Message(root, textvariable=CurrTime, relief=tkinter.RAISED, width=150)
CurrTime.set(value="Not Started")

start_times = []  # creates an array to store list of starting times
end_times = []  # creates an array to store list of ending times
start_date_times = []  # stores starting times as strings
end_date_times = []  # stores ending times as strings
elapsed_time = []  # calculates added times between start and stops
total_time = 0.0  # keeps track of total times elapsed
state = "start"  # state tracker variable
now = datetime.now()  # sets the time that the program was opened
# dd/mm/YY H:M:S
# dt_string_start = now.strftime("%d/%m/%Y %H:%M:%S")
dt_string_start = now.strftime("%d%m%Y%H%M%S")  # formats the starting date


def time_convert(sec, val=1):  # converts seconds value to proper time format
	minutes = sec // 60
	sec = sec % 60
	hours = minutes // 60
	minutes = minutes % 60
	if val == 1:
		print("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(minutes), sec))
		return "Time Lapsed = {0}:{1}:{2}".format(int(hours), int(minutes), sec)
	else:
		return "{0}:{1}:{2}".format(int(hours), int(minutes), sec)


# entry = Entry(root, width=10)
# entry.pack(side=TOP, padx=10, pady=10)


def on_start():  # runner of the stopwatch
	global state  # keep track of the state variable from gobal scope
	if state == "start":  # if the state is in start
		start_time = time.time()  # set the start time to now
		time_now = datetime.now()  # start the current time using datetime
		dt_string = time_now.strftime("%d/%m/%Y %H:%M:%S")  # format datetime
		start_date_times.append(dt_string)  # add start time to start time list
		var.set(value="Counting")  # change var text
		start_times.append(start_time)  # store start time
		state = "running"  # set state to running
	else:  # if state is not in start
		end_time = time.time()  # get end time
		var.set(value="Not Counting")  # set var display to not counting
		time_now = datetime.now()  # get current time
		dt_string = time_now.strftime("%d/%m/%Y %H:%M:%S")  # format current time
		end_date_times.append(dt_string)  # store end date time
		end_times.append(end_time)
		elapsed_time.append(end_time - start_times[len(start_times) - 1])  # get elapsed time since last activation
		counted_time = 0.0  # create a counter for start time
		for element in elapsed_time:  # for each loop of elapseed_time
			counted_time += element  # add all elements in elapsed time together in counted_time
		CurrTime.set(value=time_convert(counted_time, 0))  # get the current count of time
		state = "start"  # set state to start


def close_window():  # on window close
	global state  # using state variable
	if state == "running":  # if state is running, close out the counter
		end_time = time.time()
		time_now = datetime.now()
		dt_string = time_now.strftime("%d/%m/%Y %H:%M:%S")
		start_date_times.append(dt_string)
		end_times.append(end_time)
		elapsed_time.append(end_time - start_times[len(start_times) - 1])
		state = "start"
	root.destroy()  # destroy the main window


label.pack(side=tkinter.TOP, padx=50, pady=50)  # put label in the tkinter window in the proper location
CountedTime.pack(side=tkinter.TOP, padx=25)  # add CountedTime to the tkinter window
tkinter.Button(root, text='Run', command=on_start).pack(side=tkinter.LEFT)  # create tkinter button
tkinter.Button(root, text='Close', command=close_window).pack(side=tkinter.RIGHT)  # create tkinter button
root.mainloop()  # start the tkinter window
# after the end of the program
for ele in elapsed_time:  # count the elapsed time
	total_time += ele
time_convert(total_time)  # print out the elapsed time

now = datetime.now()  # get current time for ending
# dd/mm/YY H:M:S
# dt_string_end = now.strftime("%d/%m/%Y %H:%M:%S")
dt_string_end = now.strftime("%d%m%Y%H%M%S")
filename = "Stopwatch_Records_Start" + dt_string_start + "_End" + dt_string_end + ".txt"
# create the file for output based on the current time
with open(filename, "a") as output_file:  # open the file as output_file and write to it
	for i in range(len(start_date_times)):  # loop through loop
		output_file.write("Start: " + start_date_times[i] +
		                ", End: " + end_date_times[i] +
		                ", Elapsed Time: " + str(elapsed_time[i])+"\n")
		# write to file each activation and deactivation
	output_file.write("Total lapsed time: " + time_convert(total_time, 0))
	# write to file the total elapsed time
