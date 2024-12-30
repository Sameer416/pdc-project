import time
import random
from multiprocessing import Pool

class ParallelProcessor:
    """
    Class to handle parallel processing of network packet data.
    """
    def __init__(self, data):
        """
        Initializes the processor with data.

        Args:
            data (list): A list of network packet data.
        """
        self.data = data

    @staticmethod
    def process_packet(packet):
        """
        Processes a single network packet.

        Args:
            packet: A single network packet to process.

        Returns:
            dict: Processed packet details, including packet ID, IP address, packet size, and status.
        """
        time.sleep(0.1)  # Simulate processing time
        ip_address = f"192.168.{random.randint(0, 255)}.{random.randint(1, 254)}"
        packet_size = random.randint(64, 1500)  # Packet size in bytes
        return {
            "packet_id": packet,
            "ip_address": ip_address,
            "packet_size": packet_size,
            "status": "processed"
        }

    def process_all(self):
        """
        Processes all packets in parallel.

        Returns:
            list: A list of processed packet details.
        """
        with Pool() as pool:
            return pool.map(ParallelProcessor.process_packet, self.data)