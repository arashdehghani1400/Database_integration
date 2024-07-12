import random
import time
import matplotlib.pyplot as plt

class DiskScheduler:
    def __init__(self, head_position, requests):
        self.head_position = head_position
        self.requests = requests

    def elevator_algorithm(self):
        sorted_requests = sorted(self.requests)
        total_time = 0
        response_times = []

        for request in sorted_requests:
            distance = abs(self.head_position - request[0])
            total_time += distance
            self.head_position = request[0]
            response_times.append(total_time * 0.001 + request[1])  # Convert milliseconds to seconds

        return response_times

    def fcfs_algorithm(self):
        total_time = 0
        response_times = []

        for request in self.requests:
            distance = abs(self.head_position - request[0])
            total_time += distance
            self.head_position = request[0]
            response_times.append(total_time * 0.001 + request[1])  # Convert milliseconds to seconds

        return response_times

def generate_random_requests(num_requests):
    return [(random.randint(0, 65535), random.uniform(0, 100)) for _ in range(num_requests)]

def run_simulation():
    num_requests = 1000
    current_head = 8000

    # Generate random requests
    requests = generate_random_requests(num_requests)

    # Run the Elevator algorithm
    elevator_scheduler = DiskScheduler(current_head, requests)
    start_time_elevator = time.time()
    elevator_response_times = elevator_scheduler.elevator_algorithm()
    end_time_elevator = time.time()

    # Run the FCFS algorithm
    fcfs_scheduler = DiskScheduler(current_head, requests)
    start_time_fcfs = time.time()
    fcfs_response_times = fcfs_scheduler.fcfs_algorithm()
    end_time_fcfs = time.time()

    
    print("\nResults for 1000 random requests:")
    print("Elevator Algorithm:")
    for response in elevator_response_times:
        print(f"Response Time: {response} seconds")

    print("\nFCFS Algorithm:")
    for response in fcfs_response_times:
        print(f"Response Time: {response} seconds")

    
    return elevator_response_times, fcfs_response_times

# Run the simulation for 1000 requests
elevator_times, fcfs_times = run_simulation()

# Plotting
plt.figure(figsize=(10, 6))
request_numbers = range(1, 1001)
plt.plot(request_numbers, elevator_times, label='Elevator Algorithm', linestyle='--')
plt.plot(request_numbers, fcfs_times, label='FCFS Algorithm', linestyle='--')
plt.xlabel('Request Number')
plt.ylabel('Response Time (seconds)')
plt.title('Response Time Comparison for Elevator and FCFS Algorithms (1000 requests)')
plt.legend()
plt.show()
