import json
import os
from queue.base_queue import BaseQueue
from queue.red_queue import REDQueue
from experiments.run_experiments import run_experiments
from analysis.evaluate_results import evaluate_results

RESULTS_DIR = './results/summary'
os.makedirs(RESULTS_DIR, exist_ok=True)

def main():
    # Initialize queues
    standard_queue = BaseQueue()
    red_queue = REDQueue()

    # Run experiments
    standard_results = run_experiments(standard_queue)
    red_results = run_experiments(red_queue)

    # Save results
    with open(os.path.join(RESULTS_DIR, 'standard_results.json'), 'w') as f:
        json.dump(standard_results, f, indent=2)

    with open(os.path.join(RESULTS_DIR, 'red_results.json'), 'w') as f:
        json.dump(red_results, f, indent=2)

    # Evaluate results
    evaluate_results(standard_results, 'Standard Queue')
    evaluate_results(red_results, 'RED Queue')

if __name__ == "__main__":
    main()