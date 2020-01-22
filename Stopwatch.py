import time
import tkinter
from datetime import datetime

root = tkinter.Tk()
root.geometry("300x200")
root.title('Stopwatch')
var = tkinter.StringVar()
label = tkinter.Message(root, textvariable=var, relief=tkinter.RAISED, width=150)
var.set(value="Not Counting")

CurrTime = tkinter.StringVar()
CountedTime = tkinter.Message(root, textvariable=CurrTime, relief=tkinter.RAISED, width=150)
CurrTime.set(value="Not Started")

start_times = []
end_times = []
start_date_times = []
end_date_times = []
elapsed_time = []
total_time = 0.0
state = "start"
now = datetime.now()
# dd/mm/YY H:M:S
# dt_string_start = now.strftime("%d/%m/%Y %H:%M:%S")
dt_string_start = now.strftime("%d%m%Y%H%M%S")


def time_convert(sec, val=1):
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


def on_start():
	global state
	if state == "start":
		start_time = time.time()
		time_now = datetime.now()
		dt_string = time_now.strftime("%d/%m/%Y %H:%M:%S")
		start_date_times.append(dt_string)
		var.set(value="Counting")
		start_times.append(start_time)
		state = "running"
	else:
		end_time = time.time()
		var.set(value="Not Counting")
		time_now = datetime.now()
		dt_string = time_now.strftime("%d/%m/%Y %H:%M:%S")
		end_date_times.append(dt_string)
		end_times.append(end_time)
		elapsed_time.append(end_time - start_times[len(start_times) - 1])
		counted_time = 0.0
		for element in elapsed_time:
			counted_time += element
		CurrTime.set(value=time_convert(counted_time, 0))
		state = "start"


def close_window():
	global state
	if state == "running":
		end_time = time.time()
		time_now = datetime.now()
		dt_string = time_now.strftime("%d/%m/%Y %H:%M:%S")
		start_date_times.append(dt_string)
		end_times.append(end_time)
		elapsed_time.append(end_time - start_times[len(start_times) - 1])
		state = "start"
	root.destroy()  # destroying the main window


label.pack(side=tkinter.TOP, padx=50, pady=50)
CountedTime.pack(side=tkinter.TOP, padx=25)
tkinter.Button(root, text='Run', command=on_start).pack(side=tkinter.LEFT)
tkinter.Button(root, text='Close', command=close_window).pack(side=tkinter.RIGHT)
root.mainloop()
for ele in elapsed_time:
	total_time += ele
time_convert(total_time)

now = datetime.now()
# dd/mm/YY H:M:S
# dt_string_end = now.strftime("%d/%m/%Y %H:%M:%S")
dt_string_end = now.strftime("%d%m%Y%H%M%S")
filename = "Stopwatch_Records_Start" + dt_string_start + "_End" + dt_string_end + ".txt"
with open(filename, "a") as output_file:
	for i in range(len(start_date_times)):
		output_file.write("Start: " + start_date_times[i] +
		                ", End: " + end_date_times[i] +
		                ", Elapsed Time: " + str(elapsed_time[i])+"\n")
	output_file.write("Total lapsed time: " + time_convert(total_time, 0))
