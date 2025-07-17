def calculate_average(data):
    if not data:
        return None
    return sum(data) / len(data)

def calculate_packet_loss(sent, received):
    if sent == 0:
        return None
    return (sent - received) / sent * 100

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)