import sched
import time

# Initialize a scheduler instance
scheduler = sched.scheduler(time.time, time.sleep)

# Define a function to be executed as a task
def task(name):
    print(f"Task '{name}' executed at {time.time()}")

# Schedule tasks
scheduler.enter(5, 1, task, ("Task 1",))  # Task 1 scheduled after 5 seconds
scheduler.enter(10, 1, task, ("Task 2",))  # Task 2 scheduled after 10 seconds

print("Starting the scheduler...")
scheduler.run()  # Start the scheduler and execute tasks
print("Scheduler stopped.")
