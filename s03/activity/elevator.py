import time

"""========== CODES INSIDE THE FUNCTION =========="""
def elevate(start_floor):
    while True:
        target_floor = int(input("What floor are you heading to: "))

        if target_floor in floors:
            break
        else:
            print("Invalid target floor.")

    while True:
        if start_floor == target_floor:
            print("=========================================")
            print(f"Floor {target_floor}. You are already in your destination.")

        elif start_floor > target_floor:
            # Going down.
            print("=========================================")
            print(f"You are going down from Floor {start_floor} to Floor {target_floor}.")
            print("=========================================")
            time.sleep(1)

            for floor in floorsB:
                if floor == target_floor:
                    time.sleep(1)
                    print(f"Floor {floor}. You are now in your destination.")
                    break
                elif floor >= start_floor:
                    continue
                else:
                    time.sleep(1)
                    print(f"Going down. Floor {floor}.")

        elif start_floor < target_floor:
            # Going up.
            print("=========================================")
            print(f"You are going up from Floor {start_floor} to Floor {target_floor}.")
            print("=========================================")

            for floor in floors:
                if floor == target_floor:
                    time.sleep(1)
                    print(f"Floor {floor}. You are now in your destination.")
                    break
                elif floor <= start_floor:
                    continue
                else:
                    time.sleep(1)
                    print(f"Going up. Floor {floor}.")

        return target_floor
        break

"""========== CODES OUTSIDE THE FUNCTION =========="""
floors = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
floorsB = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

print("""========== Welcome to the Mall ==========
	[0] Lower Ground Floor      [6] 6th Floor
	[1] Upper Ground Floor      [7] 7th Floor
	[2] 2nd Floor               [8] 8th Floor
	[3] 3rd Floor               [9] 9th Floor
	[4] 4th Floor               [10] 10th Floor
	[5] 5th Floor
=========================================""")

start_floor = int(input("What is your current floor: "))
if start_floor in floors:
    current_floor = elevate(start_floor)

    while True:
        leave = input("Proceed to another level (Yes or No): ")

        if leave.lower() == "yes":
            current_floor = elevate(current_floor)
            continue
        elif leave.lower() == "no":
            print("=========================================")
            print("You may now exit the elevator.")
            print("=========================================")
            break
        else:
            print("Invalid choice.")

else:
    print("Invalid starting point.")
