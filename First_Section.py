# Create disk class
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
            response_times.append((request[0], total_time + request[1]))

        return response_times

    def fcfs_algorithm(self):
        total_time = 0
        response_times = []

        for request in self.requests:
            distance = abs(self.head_position - request[0])
            total_time += distance
            self.head_position = request[0]
            response_times.append((request[0], total_time + request[1]))

        return response_times

# Input
current_head = int(input("Enter the current head position: "))
num_requests = int(input("Enter the number of I/O requests: "))

requests = []
for _ in range(num_requests):
    request = tuple(map(int, input().split()))
    requests.append(request)

# Run the Elevator algorithm
elevator_scheduler = DiskScheduler(current_head, requests)
elevator_response_times = elevator_scheduler.elevator_algorithm()

# Display results for Elevator algorithm
print("\nElevator Algorithm:")
for response in elevator_response_times:
    print(f"{response[0]}  {"{:.1f}".format(response[1]/1000)}")

# Run the FCFS algorithm
fcfs_scheduler = DiskScheduler(current_head, requests)
fcfs_response_times = fcfs_scheduler.fcfs_algorithm()

# Display results for FCFS algorithm
print("\nFCFS Algorithm:")
for response in fcfs_response_times:
    print(f"{response[0]}  {"{:.1f}".format(response[1]/1000)}")
