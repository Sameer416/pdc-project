import time
from parallel_processing import ParallelProcessor

def main_parallel():
    """
    Main function to execute parallel processing.
    """
    data = list(range(1, 101))  # Simulate 100 packets
    processor = ParallelProcessor(data)

    start_time = time.time()
    results = processor.process_all()
    end_time = time.time()

    # Display results
    print(f"Processed {len(results)} packets in parallel in {end_time - start_time:.2f} seconds.")

    # Save results to a text file
    with open("parallel_results.txt", "w") as file:
        for result in results:
            file.write(f"Packet ID: {result['packet_id']}, IP Address: {result['ip_address']}, "
                       f"Packet Size: {result['packet_size']} bytes, Status: {result['status']}\n")
        file.write(f"\nTotal Time Taken: {end_time - start_time:.2f} seconds\n")
    print("Results saved to 'parallel_results.txt'.")

if __name__ == "__main__":
    main_parallel()