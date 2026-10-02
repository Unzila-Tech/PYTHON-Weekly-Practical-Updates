# Read employee data
employees = []

with open("employee.txt", "r") as file:
    next(file)  # skip header

    for line in file:
        data = line.strip().split(",")

        name = data[0]
        eid = data[1]
        salary = int(data[2])
        did = data[3]

        employees.append((name, salary, did))


# Calculate total salary and employee count department-wise
department_data = {}

for name, salary, did in employees:

    if did not in department_data:
        department_data[did] = [0, 0]

    department_data[did][0] += salary
    department_data[did][1] += 1


# Read department data
departments = {}

with open("department.txt", "r") as file:
    next(file)

    for line in file:
        data = line.strip().split(",")

        did = data[0]
        dname = data[1]
        location = data[2]

        departments[did] = (dname, location)


# Display average salary
print("Department-wise Average Salary")
print("--------------------------------")

for did in department_data:
    total_salary = department_data[did][0]
    count = department_data[did][1]

    average = total_salary / count

    dname = departments[did][0]

    print(dname, ":", average)