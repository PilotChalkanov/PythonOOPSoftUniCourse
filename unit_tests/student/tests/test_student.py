from unittest import main, TestCase
from project.student import Student

class StudentTest(TestCase):

    def setUp(self):
        self.student = Student('name')

    def test_student_init(self):

        self.assertEqual(self.student.name,'name')
        self.assertEqual(self.student.courses, {})

    def test_when_init_student_with_course(self):
        self.student = Student('name', {'test_course':[]})
        self.assertEqual(self.student.courses,{'test_course':[]})

    def test_student_when_enrolls_course_and_add_notes_return_note_added(self):
        self.assertEqual(self.student.enroll('course1', 'alabalanica', ""),"Course and course notes have been added.")

    def test_student_when_enrolls_course_and_add_notes_Y_return_note_added(self):
        self.assertEqual(self.student.enroll('course1', 'alabalanica', "Y"), "Course and course notes have been added.")

    def test_student_enrolls_course_which_is_in_the_list(self):
        self.assertEqual(self.student.enroll('course1', ['alabalanica_turska', 'panica'], ""), "Course and course notes have been added.")
        self.assertEqual(self.student.courses['course1'],['alabalanica_turska', 'panica' ])

    def test_student_enroll_course_without_notes(self):
        self.assertEqual(self.student.enroll('course02', [], 'N'), "Course has been added.")
        self.assertEqual(self.student.courses["course02"], [])

    def test_if_student_add_note_to_a_given_course(self):
        self.student.enroll('course', 'alabala',"")
        self.assertEqual(self.student.courses['course'],'alabala')

    def test_add_note_when_course_is_in_the_list(self):
        self.student.enroll('course', [], "")
        self.assertEqual(self.student.add_notes("course","alabalanica"), "Notes have been updated" )
        self.assertEqual(self.student.courses["course"], ["alabalanica"])

    def test_add_note_when_there_is_no_such_course(self):
        self.student.enroll('course', [], "")

        with self.assertRaises(Exception) as context:
            self.assertEqual(self.student.add_notes("course7", "alabalanica"))
        self.assertEqual("Cannot add notes. Course not found.", str(context.exception))

    def test_leave_course_when_course_in_list(self):
        self.student.enroll('course', [], "")
        self.assertEqual(self.student.leave_course('course'),"Course has been removed")
        self.assertEqual(self.student.courses, {})

        with self.assertRaises(Exception) as context:
            self.assertEqual(self.student.leave_course("course"))
        self.assertEqual("Cannot remove course. Course not found.", str(context.exception))

if __name__ == '__main__':
    main()