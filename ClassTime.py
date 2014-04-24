from Tkinter import *
import MySQLdb as sql

# courses and there corresponding slot
course_slot = {'C1':'A', 'C2': 'B', 'C3': 'C', 'C4':'D', 'C5':'A', 'C6' : 'B', 'C7': 'C', 'C8':'D'}
enable = {}
current_user = ""
course = []


# Time-table with their course slot
time_table = {('M','1'): 'A', ('M', '2'): 'B', ('M', '3'): 'C', ('M', '4'): 'D', ('M', '5'): 'E',
              ('T','1'): 'E', ('T', '2'): 'A', ('T', '3'): 'B', ('T', '4'): 'C', ('T', '5'): 'D',
              ('W','1'): 'D', ('W', '2'): 'E', ('W', '3'): 'A', ('W', '4'): 'B', ('W', '5'): 'C',
              ('Th','1'): 'C', ('Th', '2'): 'D', ('Th', '3'): 'E', ('Th', '4'): 'A', ('Th', '5'): 'B',
              ('F','1'): 'B', ('F', '2'): 'C', ('F', '3'): 'D', ('F', '4'): 'E', ('F', '5'): 'A' }

def SelectCourses():
    current_user = text1.get()

    i = 0
    for c in enable:
        if enable[c].get() == 1:
            course.append(c)
            i = i + 1
        #print enable[c]
    #print i
    if i != 4:
        L4 = Label(frame_to_list_courses, text="Error: choose 4 courses")
        L4.pack()
    else:
        db = sql.connect("localhost", "root", "12345", "classtime")
        cursor = db.cursor()
        cmd = """ INSERT INTO usrcourses(username, course1, course2, course3, course4)
              VALUES ('%s', '%s', '%s', '%s', '%s')""" % (current_user, course[0], course[1], course[2], course[3])
        cursor.execute(cmd)
        db.commit()
        #courses = []
        enable.clear()
        frame_to_list_courses.destroy()

        frame = Tk()
        frame.geometry("350x300")
        #frame.pack(expand = yes, fill = BOTH)

        arr = ['M', 'T', 'W', 'Th', 'F']

        m = "Day\t1\t2\t3\t4\t5"
        l1 = Label(frame, text=m)
        l1.pack()

        flag = 0
        for a in arr:
            item = []
            for i in range(1,6):
                flag = 0
                for c in course:
                    if course_slot[c] == time_table[(a, str(i))]:
                        var = c + "\t"
                        flag = 1
                if flag == 0:
                    var = "NIL\t"
                item.append(var)
            temp = Variable()
            la = a + "\t" + "".join(item)
            temp = Label(frame, text=la)
            temp.pack()
        

        db.close()

def ListCourses():
    for c in course_slot:
        enable[c] = Variable()
        l = Checkbutton(frame_to_list_courses, text=c + " " + course_slot[c], offvalue=0, onvalue=1, variable=enable[c])
        l.pack()
        

# GUI to list the courses
frame_to_list_courses = Tk()
frame_to_list_courses.title("Course Select")
frame_to_list_courses.geometry("300x350")

L1 = Label(frame_to_list_courses, text="Enter userId")
L2 = Label(frame_to_list_courses, text="")
L3 = Label(frame_to_list_courses, text="")
text1 = Entry(frame_to_list_courses)

button = Button(frame_to_list_courses, text="Select Courses", command=SelectCourses)

L1.pack()
text1.pack()
L2.pack()
ListCourses()
L3.pack()
button.pack()

frame_to_list_courses.mainloop()
