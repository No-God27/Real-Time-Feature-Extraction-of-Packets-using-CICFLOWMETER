# Real-Time Network Traffic Capture and Feature Extraction

This repository contains a Python script that automates the process of:
1. Capturing network traffic from a specified network interface for a defined time duration (default: 10 seconds).
2. Saving the captured traffic as a `.pcap` file in a designated input folder.
3. Running CICFlowMeter to extract network flow features from the captured traffic.
4. Storing the extracted features in a designated output folder.

The script is designed for integration with a real-time dashboard that updates periodically to display extracted features.

## Prerequisites

### Software Dependencies
- **Python 3.8+**
  - Required Python libraries: `pyshark`, `os`, `subprocess`, `datetime`, `time`
- **CICFlowMeter**
  - Download and extract the CICFlowMeter tool: [CICFlowMeter GitHub](https://github.com/ahlashkari/CICFlowMeter)
  - Ensure the `cfm.bat` file is present in the `bin` directory of the extracted folder.

### System Requirements
- **Windows OS** (with the Command Prompt)
- **WinPcap/Npcap** (installed to enable packet capture capabilities)
- Administrator privileges to allow packet capturing from the network interface.

## Folder Structure
```
project_directory/
|-- automate.py        # Main Python script for the automation process
|-- input/             # Folder to save captured .pcap files
|-- output/            # Folder to save extracted features as .csv files
```

## Usage

### Setup
1. Clone this repository to your local machine:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd project_directory
   ```
3. Install Python dependencies:
   ```bash
   pip install pyshark
   ```

4. Update the paths in the script:
   - **Path to `cfm.bat`**:
     Update the variable `cfm_path` with the location of the `cfm.bat` file (e.g., `"C:\\Users\\YourUsername\\CICFlowMeter-4.0\\bin\\cfm.bat"`).
   - **Input Folder**:
     Update the variable `input_folder` to the directory where `.pcap` files will be stored (e.g., `"C:\\Users\\YourUsername\\Documents\\pcap_store"`).
   - **Output Folder**:
     Update the variable `output_folder` to the directory where `.csv` files will be saved (e.g., `"C:\\Users\\YourUsername\\Documents\\output"`).

### Run the Script
To run the script, use:
```bash
python automate.py
```
The script will:
- Capture packets from the `Wi-Fi` network interface for 10 seconds.
- Save the captured packets in the `input_folder` as a `.pcap` file.
- Run CICFlowMeter to process the `.pcap` file and extract features into the `output_folder`.

### CICFlowMeter Command Execution
The script uses the following command to run CICFlowMeter:
```
cfm.bat "<input_file_path>" "<output_folder_path>"
```
This ensures compatibility with how CICFlowMeter operates in the Windows Command Prompt.

## Key Components

### Packet Capture
- Captures packets using `pyshark` and saves them as a `.pcap` file.

### Feature Extraction
- Automates the execution of the CICFlowMeter command to generate network flow features from the `.pcap` file.

### Real-Time Operation
- The script is modular and can be extended to run periodically or integrate into a dashboard for real-time updates.

## Extending to Real-Time Dashboard
For real-time dashboards:
- Store extracted features in a database (e.g., SQLite, PostgreSQL).
- Use frameworks like Flask or Django to create an API for fetching data.
- Build a frontend using visualization libraries like Plotly, Dash, or D3.js.

## Troubleshooting

### "Error running CICFlowMeter"
Ensure that:
- `cfm.bat` can be executed from its directory without issues.
- `WinPcap` or `Npcap` is installed correctly.
- The network interface name in the script matches the actual interface name (e.g., `Wi-Fi`).

### Packet Capture Errors
- Run the script as an administrator to enable packet capturing.
- Verify the interface name (`Wi-Fi` for wireless networks). List interfaces using `pyshark`.
  ```python
  import pyshark
  print(pyshark.LiveCapture().interfaces)
  ```

## Contact
For issues or contributions, please create an issue or pull request in this repository.

