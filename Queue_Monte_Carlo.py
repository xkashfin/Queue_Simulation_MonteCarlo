import numpy as np

# Define arrival and service rate distributions
arrival_rate = 10  # customers/minute
service_rate = 12  # customers/minute

# Define simulation parameters
num_runs = 1000  # number of simulation runs
simulation_time = 60  # minutes
time_step = 0.1  # minutes

# Define queue variables
queue_length = 0
num_customers_served = 0
num_customers_arrived = 0
total_waiting_time = 0

# Run simulation
for run in range(num_runs):
    time = 0
    queue_length = 0
    num_customers_served = 0
    num_customers_arrived = 0
    total_waiting_time = 0
    while time < simulation_time:
        # Calculate time until next arrival or departure event
        next_arrival_time = np.random.exponential(scale=1/arrival_rate)
        next_departure_time = np.random.exponential(scale=1/service_rate)
        time_until_event = min(next_arrival_time, next_departure_time)

        # Update queue length and waiting time
        total_waiting_time += queue_length * time_until_event
        queue_length += int(next_arrival_time <= next_departure_time) - 1
        
        # Increment counters
        num_customers_arrived += int(next_arrival_time <= simulation_time)
        num_customers_served += int(next_departure_time <= simulation_time)

        # Update simulation time
        time += time_until_event

    # Calculate average waiting time and queue length
    avg_waiting_time = total_waiting_time / num_customers_served
    avg_queue_length = total_waiting_time / simulation_time
    
    # Print results
    print(f'Simulation run {run+1}:')
    print(f'Average waiting time: {avg_waiting_time:.2f} minutes')
    print(f'Average queue length: {avg_queue_length:.2f} customers')
