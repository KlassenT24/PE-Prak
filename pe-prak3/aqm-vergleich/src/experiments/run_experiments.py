import subprocess
import json
import os
import statistics
from queue.base_queue import BaseQueue
from queue.red_queue import REDQueue

NUM_RUNS = 5
RESULTS_DIR = './results/summary'
os.makedirs(RESULTS_DIR, exist_ok=True)

def run_experiment(queue_type):
    print(f"Starting experiments for {queue_type}...")
    latencies = []
    throughputs = []
    udp_losses = []

    for i in range(1, NUM_RUNS + 1):
        if queue_type == 'standard':
            queue = BaseQueue()
        elif queue_type == 'red':
            queue = REDQueue()

        # Simulate packet processing and collect metrics
        result = queue.process_packets()
        latencies.append(result['latency'])
        throughputs.append(result['throughput'])
        udp_losses.append(result['udp_loss'])

    avg_latency = statistics.mean(latencies) if latencies else None
    avg_throughput = statistics.mean(throughputs) if throughputs else None
    avg_udp_loss = statistics.mean(udp_losses) if udp_losses else None

    summary = {
        'queue_type': queue_type,
        'avg_latency': avg_latency,
        'avg_throughput': avg_throughput,
        'avg_udp_loss_percent': avg_udp_loss,
        'num_iterations': NUM_RUNS
    }

    return summary

def main():
    results = []
    for queue_type in ['standard', 'red']:
        result = run_experiment(queue_type)
        results.append(result)
        print(f"Results for {queue_type} queue: {result}")

    # Save results to a JSON file
    with open(os.path.join(RESULTS_DIR, 'experiment_results.json'), 'w') as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()