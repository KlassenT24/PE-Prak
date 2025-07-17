class BaseQueue:
    def __init__(self):
        self.queue = []
        self.total_packets = 0
        self.dropped_packets = 0
        self.latency_sum = 0

    def add_packet(self, packet):
        self.queue.append(packet)
        self.total_packets += 1

    def remove_packet(self):
        if self.queue:
            packet = self.queue.pop(0)
            self.latency_sum += packet['latency']
            return packet
        return None

    def calculate_throughput(self):
        return self.total_packets / (self.latency_sum + 1e-6)  # Avoid division by zero

    def calculate_loss(self):
        return (self.dropped_packets / self.total_packets) * 100 if self.total_packets > 0 else 0


class REDQueue(BaseQueue):
    def __init__(self, max_size=100, min_threshold=20, max_threshold=80, drop_probability=0.1):
        super().__init__()
        self.max_size = max_size
        self.min_threshold = min_threshold
        self.max_threshold = max_threshold
        self.drop_probability = drop_probability

    def add_packet(self, packet):
        if len(self.queue) < self.max_size:
            super().add_packet(packet)
        else:
            self.dropped_packets += 1
            if len(self.queue) >= self.min_threshold:
                if random.random() < self.drop_probability:
                    self.dropped_packets += 1
                else:
                    super().add_packet(packet)

    def remove_packet(self):
        return super().remove_packet()