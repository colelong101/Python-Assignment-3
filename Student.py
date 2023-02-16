from datetime import datetime


class Event():
	def __init__(self, title, eventType, entryFee=0):
		self.title = title
		self.eventType = eventType
		self.cost = entryFee


class Assignment():
	def __init__(self, name, points, maxPoints, assignmentType='assignment'):
		self.name = name
		self.points = points
		self.maxPoints = maxPoints
		self.assignmentType = assignmentType

	def getPercentage(self):
		''' Returns a percentage representing the score given on the assignment.

		Returns a float between 0 and 1 for the score of the assignment.
		'''
		return self.points / self.maxPoints


class Student():
	def __init__(self, name:str, ID:str, nickname:str='', events:list[Event]=[], assignments:list[Assignment]=[]):
		self.name = name
		self.ID = ID
		self.nick = nickname
		self.events = events
		self.assignments = assignments

	def addEvent(self, eventAttended:Event):
		''' Adds an events or list of events to the student record.

		Arguments:
			eventAttended(Event): The Event object instance in which the student attended.

		Exceptions:
			TypeError if not all elements provided are an Event object.
		'''
		# Making sure our eventAttended is a list. If not, we make it a single list
		if type(eventAttended) is not list:
			eventAttended = [eventAttended]

		# Checking for items in our list that aren't events.
		for event in eventAttended:
			if type(event) != Event:
				raise TypeError('All elements provided must be an Event')

		# Extending our students events list with the new one.
		self.events += eventAttended

	def countEventOfType(self, eventType:str) -> int:
		''' Gets the number of events that match the type given.

		The event type check is NOT cause sensitive.

		Arguments:
			eventType(str): The event type to search for. i.e. 'meeting'.

		Returns an integer for how many events match your type.
		'''
		count = 0
		# Iterating and finding matching event types
		for event in self.events:
			if event.eventType.lower() == eventType.lower():
				count += 1

		# Returning our count
		return count

	def countMeetings(self) -> int:
		''' Convenience binding over `self.countEventOfType` for the number of meetings.

		See `self.countEventOfType` for documentation.

		Returns an integer for how many events were meetings.
		'''
		return self.countEventOfType('meeting')

	def countEvents(self):
		return len(self.events)

	def addAssignment(self, assignments):
		''' Adds an events or list of events to the student record.

		Arguments:
			assignments(Assignment): The Event object instance in which the student attended.

		Exceptions:
			TypeError if not all elements provided are an Event object.
		'''
		# Making sure our assignment is a list. If not, we make it a single list
		if type(assignments) is not list:
			assignments = [assignments]

		# Checking for items in our list that aren't assignments.
		for assignment in assignments:
			if type(assignment) != Assignment:
				raise TypeError('All elements provided must be an Assignment')

		# Extending our students assignments list with the new one.
		self.assignments += assignments

	def getGrade(self) -> float:
		''' Returns the total weighted grade as a percentage point from 0 to 1.

		Returns None if no assignments have been recorded.
		'''
		# Checking for no assignments
		if len(self.assignments) == 0:
			return None

		# First, we'll get our total possible points for our assignments
		totalPoints = sum([assignment.maxPoints for assignment in self.assignments])
		# Finding the current points from all assignments
		currentPoints = sum([assignment.points for assignment in self.assignments])

		return currentPoints / totalPoints

	def getLetterGrade(self, grade:float=None) -> str:
		''' Returns a string containing the character grade that the student will receive.

		Arguments:
			grade(float): Float between 0 and 1 that represents a grade

		Returns None if no assignments have been recorded.
		'''
		# Getting our grade and confirming it's not a null value
		grade = grade or self.getGrade()
		if grade is None:
			return None

		# Switch to see what we return
		if grade < .6:
			return 'F'
		elif grade < .7:
			return 'D'
		elif grade < .8:
			return 'C'
		elif grade < .9:
			return 'B'
		elif grade < 1:
			return 'A'
		else:
			return 'A+'


if __name__ == '__main__':

	from testData import *
	matthew = Student(**MATTHEW_POGUE)

	EVENTS = [Event(**data) for data in EVENTS]
	matthew.addEvent(EVENTS[:3])
	for event in EVENTS[3:]:
		matthew.addEvent(event)

	ASSIGNMENTS = [Assignment(**data) for data in ASSIGNMENTS]
	for assignment in ASSIGNMENTS[:4]:
		matthew.addAssignment(assignment)
	matthew.addAssignment(ASSIGNMENTS[4:])

	pass