# Importing necessary libraries
import matplotlib.pyplot as plt

# Students' data
students_names = ["Sanjay", "Rahul", "Karan", "Wasim", "Ramesh", "Ajay", "Sartaj", "Priya"]
students_marks = [35, 50, 20, 45, 25, 40, 25, 40]

# Calculating percentages
marks_perc = []
for x in students_marks:
    res = (x / 50) * 100   # assuming the maximum mark is 50
    marks_perc.append(res)

print("Marks Percentage:", marks_perc)

# -------- LINE CHART --------
def marks_line_chart():
    plt.plot(students_names, students_marks, color='blue', marker='o', linestyle='--', linewidth=2, markersize=8)
    plt.title("Students Marks Graph")
    plt.xlabel("Students Names")
    plt.ylabel("Students Marks")
    plt.grid(True)
    plt.show()

# -------- BAR CHART --------
def percentage_bar_chart():
    plt.bar(students_names, marks_perc, color='orange')
    plt.title("Students' Percentage Graph")
    plt.xlabel("Students Names")
    plt.ylabel("Percentage (%)")
    plt.show()

# Calling the functions
marks_line_chart()
percentage_bar_chart()
