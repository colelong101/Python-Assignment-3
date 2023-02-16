import unittest
from Student import Student, Assignment, Event
from testData import ASSIGNMENTS, EVENTS

class TestAssignment(unittest.TestCase):
    def test_getPercentage(self):
        for i, assignment_data in enumerate(ASSIGNMENTS):
            assignment = Assignment(
                assignment_data['name'],
                assignment_data['points'],
                assignment_data['maxPoints']
            )
            percentage = (assignment.points / assignment.maxPoints) * 100
            expected_percentage = assignment_data['points'] / assignment_data['maxPoints'] * 100
            self.assertEqual(expected_percentage, percentage)


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student('Matthew Pogue', 'h735f787', 'alex', [], ASSIGNMENTS)
        self.events = [Event(event_data['title'], event_data['eventType'], event_data['entryFee']) for event_data in EVENTS]
        self.student.addEvent(self.events)

    def test_addEvent(self):
        expected_event = self.events[2]
        self.student.addEvent([expected_event])
        self.assertIn(expected_event, self.student.events)

    def test_countMeetings(self):
        expected_count = sum(event.eventType == 'meeting' for event in self.student.events)
        actual_count = self.student.countMeetings()
        self.assertEqual(actual_count, expected_count)

    def test_getGrade(self):
        self.student.assignments = [Assignment(**assignment_data) for assignment_data in ASSIGNMENTS]
        total_points = sum(assignment.points for assignment in self.student.assignments)
        max_points = sum(assignment.maxPoints for assignment in self.student.assignments)
        expected_grade = round(total_points / max_points, 1)
        actual_grade = round(self.student.getGrade(), 1)
        self.assertEqual(actual_grade, expected_grade)

    def test_getLetterGrade(self):
        self.student.assignments = [Assignment(**assignment_data) for assignment_data in ASSIGNMENTS]
        total_points = sum(assignment.points for assignment in self.student.assignments)
        max_points = sum(assignment.maxPoints for assignment in self.student.assignments)
        expected_grade = round(total_points / max_points, 1)
        expected_letter_grade = 'F'
        if expected_grade >= .6 and expected_grade < .7:
            expected_letter_grade = 'D'
        elif expected_grade >= .7 and expected_grade < .8:
            expected_letter_grade = 'C'
        elif expected_grade >= .8 and expected_grade < .9:
            expected_letter_grade = 'B'
        elif expected_grade >= .9 and expected_grade < 1:
            expected_letter_grade = 'A'
        elif expected_grade == 1:
            expected_letter_grade = 'A+'
        actual_letter_grade = self.student.getLetterGrade(expected_grade)
        self.assertEqual(actual_letter_grade, expected_letter_grade)

if __name__ == '__main__':
    unittest.main()

