import time
startTime = time.time()
runtime = 0

print("========== T&M Group of Companies ==========")
salary = input("Enter your salary: ")
years = int(input("Enter the number of years you have served for the company: "))

if (5 <= years < 10):
    runtime =+ 1
    bonus = float(salary) * 0.05
    finalSalary = float(salary) + bonus
elif (10 <= years < 15):
    runtime =+ 2
    bonus = float(salary) * 1
    finalSalary = float(salary) + bonus
elif (15 <= years < 20):
    runtime =+ 3
    bonus = float(salary) * 1.5
    finalSalary = float(salary) + bonus
elif (20 <= years):
    runtime =+ 4
    bonus = float(salary) * 2
    finalSalary = float(salary) + bonus
else:
    runtime =+ 5
    bonus = 0.0
    finalSalary = float(salary)

print("")
print("========== SALARY ==========")
print(f"Final Salary: {finalSalary}")
print(f"Bonus: {bonus}")

print("")
print("========== RUNNING TIME ==========")
print(f"Big O: O({runtime}n)")
time.sleep(1)
endTime = time.time()
elapsedTime = endTime - startTime
print(f"Runtime: {elapsedTime}")
