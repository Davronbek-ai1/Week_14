names = ["Alice", "Bob", "Charlie", "David", "Eve"]
gpas = [3.9, 3.2, 3.6, 3.7, 3.5]
hours = [10, 100, 60, 20, 40]

single_list = []
#for name, gpa, hour in zip(names, gpas, hours):
single_list.append([name, gpa, hour] for name, gpa, hour in zip(names, gpas, hours))
for student in single_list:
    