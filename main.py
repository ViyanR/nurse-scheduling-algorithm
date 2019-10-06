#Front-end table interface

from tkintertable import TableCanvas, TableModel
from tkinter import *

data = {'Nurses': {'Week 1': 'MTWTFSS', 'Week 2': 'MTWTFSS', 'Week 3': 'MTWTFSS', 'Week 4': 'MTWTFSS', 'Week 5': 'MTWTFSS'},'1': {'Week 1': 'RRRRRRR', 'Week 2': 'RRRRRRR', 'Week 3': 'RRRRRRR', 'Week 4': 'RRRRRRR', 'Week 5': 'RRRRRRR'},'2': {'Week 1': 'RRRRRRR', 'Week 2': 'RRRRRRR', 'Week 3': 'RRRRRRR', 'Week 4': 'RRRRRRR', 'Week 5': 'RRRRRRR'},'3': {'Week 1': 'RRRRRRR', 'Week 2': 'RRRRRRR', 'Week 3': 'RRRRRRR', 'Week 4': 'RRRRRRR', 'Week 5': 'RRRRRRR'},'4': {'Week 1': 'RRRRRRR', 'Week 2': 'RRRRRRR', 'Week 3': 'RRRRRRR', 'Week 4': 'RRRRRRR', 'Week 5': 'RRRRRRR'},'5': {'Week 1': 'RRRRRRR', 'Week 2': 'RRRRRRR', 'Week 3': 'RRRRRRR', 'Week 4': 'RRRRRRR', 'Week 5': 'RRRRRRR'},'6': {'Week 1': 'RRRRRRR', 'Week 2': 'RRRRRRR', 'Week 3': 'RRRRRRR', 'Week 4': 'RRRRRRR', 'Week 5': 'RRRRRRR'},'7': {'Week 1': 'RRRRRRR', 'Week 2': 'RRRRRRR', 'Week 3': 'RRRRRRR', 'Week 4': 'RRRRRRR', 'Week 5': 'RRRRRRR'},'8': {'Week 1': 'RRRRRRR', 'Week 2': 'RRRRRRR', 'Week 3': 'RRRRRRR', 'Week 4': 'RRRRRRR', 'Week 5': 'RRRRRRR'},'9': {'Week 1': 'RRRRRRR', 'Week 2': 'RRRRRRR', 'Week 3': 'RRRRRRR', 'Week 4': 'RRRRRRR', 'Week 5': 'RRRRRRR'},'10': {'Week 1': 'RRRRRRR', 'Week 2': 'RRRRRRR', 'Week 3': 'RRRRRRR', 'Week 4': 'RRRRRRR', 'Week 5': 'RRRRRRR'},'11': {'Week 1': 'RRRRRRR', 'Week 2': 'RRRRRRR', 'Week 3': 'RRRRRRR', 'Week 4': 'RRRRRRR', 'Week 5': 'RRRRRRR'},'12': {'Week 1': 'RRRRRRR', 'Week 2': 'RRRRRRR', 'Week 3': 'RRRRRRR', 'Week 4': 'RRRRRRR', 'Week 5': 'RRRRRRR'},'13': {'Week 1': 'RRRRRRR', 'Week 2': 'RRRRRRR', 'Week 3': 'RRRRRRR', 'Week 4': 'RRRRRRR', 'Week 5': 'RRRRRRR'},'14': {'Week 1': 'RRRRRRR', 'Week 2': 'RRRRRRR', 'Week 3': 'RRRRRRR', 'Week 4': 'RRRRRRR', 'Week 5': 'RRRRRRR'},'15': {'Week 1': 'RRRRRRR', 'Week 2': 'RRRRRRR', 'Week 3': 'RRRRRRR', 'Week 4': 'RRRRRRR', 'Week 5': 'RRRRRRR'},'16': {'Week 1': 'RRRRRRR', 'Week 2': 'RRRRRRR', 'Week 3': 'RRRRRRR', 'Week 4': 'RRRRRRR', 'Week 5': 'RRRRRRR'}}

root = Tk()
class Timetable(Frame):

    def __init__(self, parent=None):
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        self.main.geometry('800x500+0+0')
        self.main.title('Sequences of Shifts')
        f = Frame(self.main)
        f.pack(fill=BOTH,expand=1)
        self.table = TableCanvas(f, data=data, cellwidth=150, cellbackgr='#E3F6CE',read_only=True,rowselectedcolor='yellow',rowheaderwidth=100,showkeynamesinheader=True)
        self.table.show()
        return
    def redraw(self):
      self.table.redrawTable()


schedule=Timetable()

def AddToData(Nurse,Week,day,ShiftIndex):
	Week = 'Week ' + str(Week)
	DayIndex = {'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5,'Sunday':6}[day]
	Shift = ['E','D','L','N'][int(ShiftIndex)]
	global data
	CurrentWeek = list(data[str(Nurse)][Week])
	CurrentWeek[DayIndex] = Shift
	data[str(Nurse)][Week] = ''.join(CurrentWeek)
	schedule.redraw()



def RemoveFromData(Nurse,Week,day):
	Week = 'Week ' + str(Week)
	DayIndex = {'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5,'Sunday':6}[day]
	Shift = 'R'
	global data
	CurrentWeek = list(data[str(Nurse)][Week])
	CurrentWeek[DayIndex] = Shift
	data[str(Nurse)][Week] = ''.join(CurrentWeek)
	schedule.redraw()



#Scheduling backend algorithm
from copy import deepcopy
Hours = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
MaxHours = [36,36,36,36,36,36,36,36,36,36,36,36,32,20,0,20]
ExtraHours = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
NightShiftNum = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ConsecShiftCount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def DayInput(ListName,WeekNumber):

	global data
	if ListName.lower() == 'monday' or ListName.lower() == 'tuesday' or ListName.lower() == 'wednesday' or ListName.lower() == 'thursday' or ListName.lower() == 'friday':
		ShiftNum = 3
	
	elif ListName.lower() == 'saturday' or ListName.lower() == 'sunday':
		ShiftNum = 2
	else:
		print('Error - type of day not specified')
		exit()
	
	day = ListName
	print('Week {} {}'.format(str(WeekNumber),day.upper()))
	ListName = [[],[],[],[]]

	def DayTimeInput(index):
		global data
		for x in ListName[index]:
			RemoveFromData(x,WeekNumber,day)
		if index==0:
				'''Early shift'''
				prompt = "Enter the {} nurses for this day's early shift 07:00-16:00 (separated by spaces)".format(str(ShiftNum))
		elif index==1:
				'''Day shift'''
				prompt = "Enter the {} nurses for this day's day shift 08:00-17:00 (separated by spaces)".format(str(ShiftNum))
		elif index==2:
				'''Late shift'''
				prompt = "Enter the {} nurses for this day's late shift 14:00-23:00 (separated by spaces)".format(str(ShiftNum))
		elif index==3:
				'''Night shift'''
				print("Enter the 1 nurse for this day's night shift 23:00-07:00	(separated by spaces)")
				'''One nurse requests no night shifts (nurse 1)'''
				while True:
					ListName[3] = input().split(' ')
					if len(ListName[3]) == 1 and all(1<= int(i) <= 16 for i in ListName[3]) and '1' not in ListName[3]:
						AddToData(ListName[3][0],WeekNumber,day,index)
						break
					else:
						print('Error! Please try again')
				return None
		else:
			print('Invalid argument')
			return None
		print(prompt)
		'''Cover needs to be fulfilled'''
		while True:
			ListName[index] = input().split(' ')
			if len(ListName[index]) == ShiftNum and all(1<= int(i) <= 16 for i in ListName[index]) and len(set(ListName[index])) == len(ListName[index]):
				for x in range(ShiftNum):
					AddToData(ListName[index][x],WeekNumber,day,index)
				break
			else:
				print('Error! Please try again')



	DayTimeInput(0)
	DayTimeInput(1)
	DayTimeInput(2)
	DayTimeInput(3)



	ListName = [[int(i) for i in a] for a in ListName]

	print(ListName)


	'''For each day a nurse may only start one shift'''

	while True:
		duplicate = False
		seen = set()
		for item in ListName:
			for element in item:
				if element not in seen:
					seen.add(element)
				else:
					duplicate = True
					message = 'Nurse {} starts more than one shift on {}.'.format(str(element),day)
					OtherShift = []
					if element in ListName[0]:
						message += ' One shift is the Early shift (0),'
						OtherShift.append(0)
					if element in ListName[1]:
						message += ' One shift is the Day shift (1),'
						OtherShift.append(1)
					if element in ListName[2]:
						message += ' One shift is the Late shift (2),'
						OtherShift.append(2)
					if element in ListName[3]:
						message += ' One shift is the Night shift (3),'
						OtherShift.append(3)
					message += ' which shift would you like to change the schedule for? (Early=0, Day=1, Late=2, Night=3)\n NB: Only their latest shift is shown on the table'
					print(message)
					while True:
						while True:
							try:
								inp = int(input())
								break
							except ValueError:
								print('This is not a number inputted - try again')
						if not(0<=int(inp)<=3) or element not in ListName[inp]:
							print('Sorry - this is not one of the shifts that the nurse is on. Please enter a different shift (Early=0, Day=1, Late=2, Night=3) NB: Only their latest shift is shown on the table')
						else:
							break
					print("Ensure you don't re-enter nurse {} again, as they already start multiple shifts on this day".format(str(element)))
					DayTimeInput(inp)
					ListName[inp] = [int(i) for i in ListName[inp]]
					OtherShift.remove(inp)
					AddToData(element,WeekNumber,day,OtherShift[-1])
		if duplicate==False:
			break


	'''Within a scheduling period of 35 days nurses are allowed to exceed the number of hours per week specified in their individual employment contracts by at most 4 hours'''
	while True:
		for x in range (4):
			TooManyHours = False
			for num in ListName[x]:
				Hours[num-1] += 8
				if Hours[num-1] > MaxHours[num-1]+4:
					print('Error - Nurse {} has exceeded the number of hours specified in her employment contract ({}) by more than 4 hours. Please replace this nurse with another one - re-input all nurses for this shift'.format(str(num),str(MaxHours[num-1]),))
					TooManyHours = True
			while TooManyHours == True:
					for number in ListName[x]:
						Hours[number-1] -=8
					DayTimeInput(x)
					for number in ListName[x]:
						Hours[number-1] +=8
					if Hours[num-1] not in ListName[x]:
						break
					else:
						print("Error - you have re-inputted the same nurse who has exceeded her contract hours by more than 4 hours")
		if TooManyHours == False:
			break


	
		'''The maximum number of night shifts for any nurse is 3 per period of 5 weeks'''

		while True:
			element = ListName[3]
			NightShiftNum[element-1] += 1
			if NightShiftNum[element-1]>3:
				NightShiftNum[element-1] -= 1
				print('Nurse {} has had more than 3 night shifts in this period of 5 weeks. Please rectify this by re-entering the nurse for their final night shift.'.format(str(element)))
				DayTimeInput(3)
			else:
				break


	'''A nurse may only work 6 consecutive workdays'''

	while True:
		global ConsecShiftCount
		ConsecShiftCountTemp = deepcopy(ConsecShiftCount)
		ShiftError = False
		for x in range(1,len(ConsecShiftCountTemp)+1):
			if x in ListName[0] or x in ListName[1] or x in ListName[2] or x in ListName[3]:
				ConsecShiftCountTemp[x-1] += 1
			else:
				ConsecShiftCountTemp[x-1] = 0
		for List in ListName:
			for element in List:
				if ConsecShiftCountTemp[element-1] > 6:
					ShiftError = True
					print("Nurse {} has had more than 6 consecutive shifts. Please rectify this by re-entering all nurses for nurse {}'s 6th shift.".format(str(element),str(element)))
					DayTimeInput(ListName.index(List))
		if ShiftError == False:
			break
	ConsecShiftCount = deepcopy(ConsecShiftCountTemp)


	return(ListName)



def WeekInput(WeekNum):
	WeekName = WeekNum
	WeekNum = []
	WeekNum.append(DayInput('Monday',WeekName))
	WeekNum.append(DayInput('Tuesday',WeekName))
	WeekNum.append(DayInput('Wednesday',WeekName))
	WeekNum.append(DayInput('Thursday',WeekName))
	WeekNum.append(DayInput('Friday',WeekName))
	WeekNum.append(DayInput('Saturday',WeekName))
	WeekNum.append(DayInput('Sunday',WeekName))
	for x in range(len(Hours)):
		Hours[x] = 0
	return WeekNum

def FullInput():
	FullShift = []
	FullShift.append(WeekInput('1'))
	FullShift.append(WeekInput('2'))
	FullShift.append(WeekInput('3'))
	FullShift.append(WeekInput('4'))
	FullShift.append(WeekInput('5'))
	return FullShift


shift = FullInput()

#shift = [[[[1,2,3],[4,5,6],[7,8,9],[10]],[[11,12,13],[14,15,16],[7,5,3],[2]],[[1,4,5],[6,7,8],[9,10,11],[12]],[[14,15,16],[3,4,5],[7,8,10],[15]],[[1,2,6],[10,7,8],[11,12,13],[14]],[[11,4],[5,9],[2,3],[13]],[[15,16],[9,7],[5,6],[13]]],[[[1,2,3],[4,5,6],[7,8,9],[10]],[[11,12,13],[14,15,16],[7,5,3],[2]],[[1,4,5],[6,7,8],[9,10,11],[12]],[[14,15,16],[3,4,5],[7,8,10],[15]],[[1,2,6],[10,7,8],[11,12,13],[14]],[[11,4],[5,9],[2,3],[13]],[[15,16],[9,7],[13,6],[8]]]] #To test the rest of the code quickly

def SwapShift(week,day,nurse1,nurse2):
	print(nurse1,nurse2,week,day)
	shift1 = 0
	shift2 = 0
	for x in range(3):
		if nurse1 in shift[week][day][x]:
			shift1 = x
		elif nurse2 in shift[week][day][x]:
			shift2 = x
	shift[week][day][shift1].remove(nurse1)
	shift[week][day][shift1].append(nurse2)
	shift[week][day][shift2].remove(nurse2)
	shift[week][day][shift2].append(nurse1)
	AddToData(nurse2,week,day,shift1)
	AddToData(nurse1,week,day,shift2)

def ConstraintCheck(List):
	'''A night shift has to be followed by at least 14 hours rest (meaning it can only be followed by another night-shift)'''
	for week in range(len(List)):
		for day in range(len(List[week])):
			NightShiftNurse = List[week][day][3][0]
			try:
				if NightShiftNurse in List[week][day+1][0] or NightShiftNurse in List[week][day+1][1] or NightShiftNurse in List[week][day+1][2]:
					print('Error - Nurse {} has not had 14 hours rest after their night shift, during week {} day {}.\n Would you like to change their night shift on day {} or change their next shift on day {}? (Enter the day number)'.format(str(NightShiftNurse),str(week+1),str(day+1),str(day+1),str(day+2)))
					while True:
						try:
							ChangeDay = int(input())
							if ChangeDay == day+1 or ChangeDay == day+2:
								break
							print('Try again')
						except ValueError:
							print("Error - you didn't input a number. Try again.")
					if NightShiftNurse in shift[week][ChangeDay-1][0]:
						AlreadyShift = 0
						AlreadyShiftName = 'Early'
					if NightShiftNurse in shift[week][ChangeDay-1][1]:
						AlreadyShift = 1
						AlreadyShiftName = 'Day'
					if NightShiftNurse in shift[week][ChangeDay-1][2]:
						AlreadyShift = 2
						AlreadyShiftName = 'Late'
					if NightShiftNurse in shift[week][ChangeDay-1][3]:
						AlreadyShift = 3
						AlreadyShiftName = 'Night'
					print("On day {} which shift would you like to swap nurse {}'s shift with? \n This nurse is  working on the {} shift - don't enter this shift. \n (Early = 0, Day = 1, Late = 2, Night = 3)".format(ChangeDay,NightShiftNurse,AlreadyShiftName))
					while True:
						try:
							ChangeShift = int(input())
							if ChangeShift == AlreadyShift or ChangeShift<0 or ChangeShift>3:
								print('Error - please enter a valid number')
							else:
								break
						except ValueError:
							print("Error - you didn't input a number. Try again.")
					SwapShift(week,ChangeDay-1,NightShiftNurse,shift[week][ChangeDay-1][ChangeShift][0])
			except IndexError:#i.e. it's at the end of the week checking with the first day of the next week
				try:
					if NightShiftNurse in List[week+1][0][0] or NightShiftNurse in List[week+1][0][1] or NightShiftNurse in List[week+1][0][2]:
						print('Error - Nurse {}	has not had 14 hours rest after their night shift, during week {} day {}.\n Would you like to change their night shift on week {} day {} or change their next shift on week {} day 1? (Enter the day number)'.format(str(NightShiftNurse),str(week+1),str(day+1),str(week+1),str(day+1),str(week+2)))
						while True:
							try:
								ChangeDay = int(input())
								if ChangeDay == day+1 or ChangeDay == 1:
									break
								print('Try again')
							except ValueError:
								print("Error - you didn't input a number. Try again.")
						if ChangeDay == day+1:
							week2 = week
						else:
							week2 = week+1
						if NightShiftNurse in shift[week2][0][0]:
							AlreadyShift = 0
							AlreadyShiftName = 'EARLY'
						if NightShiftNurse in shift[week2][0][1]:
							AlreadyShift = 1
							AlreadyShiftName = 'DAY'
						if NightShiftNurse in shift[week2][0][2]:
							AlreadyShift = 2
							AlreadyShiftName = 'LATE'
						if NightShiftNurse in shift[week2][0][3]:
							AlreadyShift = 3
							AlreadyShiftName = 'NIGHT'
						print("On day {} which shift would you like to swap nurse {}'s shift with? \n This nurse is  working on the {} shift - don't enter this shift. \n (Early = 0, Day = 1, Late = 2, Night = 3".format(ChangeDay,NightShiftNurse,AlreadyShiftName))
						while True:
							try:
								ChangeShift = int(input())
								if ChangeShift == AlreadyShift or ChangeShift<0 or ChangeShift>3:
									print('Error - please enter a valid number')
								else:
									break
							except ValueError:
								print("Error - you didn't input a number. Try again.")
						SwapShift(week2,ChangeDay-1,NightShiftNurse,shift[week2][ChangeDay-1][ChangeShift][0])
				except IndexError:#end of 5 weeks - no check needed
					pass
ConstraintCheck(shift)