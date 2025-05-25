import matplotlib.pyplot as plt
std_names =["Damola", "Jessica","Joel", "Ali","Musa","Olive","Gift","Soubr"]
std_marks=[35,50,20,45,25,40,25,40]

marks_perc=[]
for x in std_marks:
    res = (x/50)*100
    marks_perc.append(res)
print(marks_perc)

# Line chart
def mark_line():
    plt.plot(std_names,std_marks)
    plt.title("Student marks graph")
    plt.xlabel("Student name")
    plt.ylabel("Student Marks")
    plt.show()
mark_line()

# Bar chart
def perce_bar():
    plt.plot(std_names,marks_perc)
    plt.title("Student percentage graph")
    plt.xlabel("Student name")
    plt.ylabel("Student Percentage")
    plt.show()
perce_bar()