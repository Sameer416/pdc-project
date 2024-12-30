import time  # Import time module
from linear_processing import LinearProcessor

def main_linear():
    """
    Main function to execute linear processing.
    """
    data = list(range(1, 101))  # Simulate 100 packets
    processor = LinearProcessor(data)

    start_time = time.time()
    results = processor.process_all()
    end_time = time.time()

    # Display results
    print(f"Processed {len(results)} packets sequentially in {end_time - start_time:.2f} seconds.")

    # Save results to a text file
    with open("linear_results.txt", "w") as file:
        for result in results:
            file.write(f"Packet ID: {result['packet_id']}, IP Address: {result['ip_address']}, "
                       f"Packet Size: {result['packet_size']} bytes, Status: {result['status']}\n")
        file.write(f"\nTotal Time Taken: {end_time - start_time:.2f} seconds\n")
    print("Results saved to 'linear_results.txt'.")

if __name__ == "__main__":
    main_linear()
