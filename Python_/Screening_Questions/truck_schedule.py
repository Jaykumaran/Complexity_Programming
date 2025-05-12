"""Question:

At a logistics center, trucks arrive and depart according to the following schedule:

Truck 1: 8:40 AM – 8:50 AM

Truck 2: 8:45 AM – 9:00 AM

Truck 3: 8:55 AM – 9:20 AM

Truck 4: 8:50 AM – 9:30 AM

Each truck must be assigned to a dock as soon as it arrives and will occupy that dock until it departs. No dock can serve more than one truck at the same time.

What is the minimum number of docks required so that no truck has to wait?"""

def time_to_minutes(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m # total minutes

def min_docks_required(truck_times):
    # Convert time range into (start, end) tuples in minutes
    trucks = [(time_to_minutes(start), time_to_minutes(end)) for start, end in truck_times]

    # Sort by arrival time , sorting reduces complexity 
    trucks.sort()
    docks = [] # holds the end time of last assigned truck

    for arrival, departure in trucks:
        assigned = False

        # Try to assign the truck to any dock that;s free
        for i in range(len(docks)):
            if docks[i] <= arrival: #ReUse the dock for the newly arrived truck
               docks[i] = departure # update the last left trucks depature time
               assigned = True
               break
        if not assigned:
           docks.append(departure) # A new dock is assigned
    return len(docks)

# Input time in strings
truck_times = [
    ("8:40", "8:50"),
    ("8:45", "9:00"),
    ("8:55", "9:20"),
    ("8:50", "9:30"),
]
print("Minimum number of docks needed:", min_docks_required(truck_times))

          
    
  
