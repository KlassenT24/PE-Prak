import json
import os

def load_results(result_dir):
    results = []
    for filename in os.listdir(result_dir):
        if filename.endswith('.json'):
            with open(os.path.join(result_dir, filename)) as f:
                results.append(json.load(f))
    return results

def analyze_results(results):
    summary = {
        'avg_latency': [],
        'avg_packet_loss': [],
        'avg_throughput': []
    }
    
    for result in results:
        summary['avg_latency'].append(result.get('avg_latency'))
        summary['avg_packet_loss'].append(result.get('avg_packet_loss_percent'))
        summary['avg_throughput'].append(result.get('avg_throughput'))

    avg_summary = {
        'avg_latency': sum(filter(None, summary['avg_latency'])) / len(summary['avg_latency']),
        'avg_packet_loss_percent': sum(filter(None, summary['avg_packet_loss'])) / len(summary['avg_packet_loss']),
        'avg_throughput': sum(filter(None, summary['avg_throughput'])) / len(summary['avg_throughput'])
    }
    
    return avg_summary

def save_summary(summary, output_file):
    with open(output_file, 'w') as f:
        json.dump(summary, f, indent=2)

def main():
    result_dir = './results/summary'
    output_file = os.path.join(result_dir, 'final_summary.json')
    
    results = load_results(result_dir)
    summary = analyze_results(results)
    save_summary(summary, output_file)
    print("Zusammenfassung der Ergebnisse gespeichert.")

if __name__ == "__main__":
    main()