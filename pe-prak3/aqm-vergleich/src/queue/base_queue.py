class BaseQueue:
    def __init__(self):
        self.queue = []
        self.total_latency = 0
        self.total_throughput = 0
        self.total_packets = 0

    def add_packet(self, packet):
        self.queue.append(packet)

    def remove_packet(self):
        if self.queue:
            packet = self.queue.pop(0)
            return packet
        return None

    def calculate_latency(self, packet):
        # Implement latency calculation logic
        pass

    def calculate_throughput(self):
        if self.total_packets > 0:
            return self.total_throughput / self.total_packets
        return 0

    def get_metrics(self):
        return {
            'latency': self.total_latency,
            'throughput': self.calculate_throughput(),
            'packet_loss': self.calculate_packet_loss()
        }

    def calculate_packet_loss(self):
        # Implement packet loss calculation logic
        pass