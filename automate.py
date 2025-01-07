import subprocess
import os
import time
from datetime import datetime
import pyshark

def capture_pcap(interface, capture_duration, output_pcap):
    """Capture network packets from a specific interface for a given duration."""
    try:
        print(f"Capturing network traffic for {capture_duration} seconds from interface {interface}...")
        capture = pyshark.LiveCapture(interface=interface, output_file=output_pcap)
        capture.sniff(timeout=capture_duration)
        print(f"Packet capture completed: {output_pcap}")
    except Exception as e:
        print(f"An error occurred while capturing traffic: {e}")

def run_cfm(cfm_path, input_file, output_folder):
    """Run CICFlowMeter on the given .pcap file to generate flow statistics."""
    try:
        print(f"Running CICFlowMeter on {input_file}...")

        # Save the original working directory
        original_working_dir = os.getcwd()

        # Change working directory to where cfm.bat is located
        bin_directory = os.path.dirname(cfm_path)
        os.chdir(bin_directory)

        # Construct the command for running CICFlowMeter
        command = f"cfm.bat {input_file} {output_folder}"
        print(f"Command being executed: {command}")

        # Execute the command from the `bin` directory
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True  # Run in a new shell to handle batch files
        )

        # Capture the output and error streams
        stdout, stderr = process.communicate()

        # Check if there was an error
        if process.returncode != 0:
            print(f"Error running CICFlowMeter:\n{stderr}")
        else:
            print("CICFlowMeter Output:\n", stdout)

        # Restore the original working directory after executing the command
        os.chdir(original_working_dir)

    except Exception as e:
        print(f"An error occurred while running CICFlowMeter: {e}")

def main():
    # Define paths
    cfm_path = r"C:\Users\linpa\OneDrive\Desktop\charm\CICFlowMeter-4.0\bin\cfm.bat"
    input_folder = r"C:\Users\linpa\OneDrive\Documents\pcap_store"
    output_folder = r"C:\Users\linpa\OneDrive\Documents\output"
    interface = "Wi-Fi"  # Modify with the correct interface name for your system
    capture_duration = 100  # seconds

    # Generate the file name with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_pcap = os.path.join(input_folder, f"traffic_{timestamp}.pcap")

    # Capture the packets
    capture_pcap(interface, capture_duration, output_pcap)

    # Run CICFlowMeter on the captured pcap file
    run_cfm(cfm_path, output_pcap, output_folder)

if __name__ == "__main__":
    main()
