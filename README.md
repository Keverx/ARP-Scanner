# Python ARP Network Scanner

A lightweight network discovery tool built with **Python** and **Scapy**. This tool sends ARP requests to a specified IP range to identify active devices (IP and MAC addresses) on the local network.

## Key Features
* **ARP Protocol:** Uses low-level packet manipulation to discover devices.
* **MAC Address Resolution:** Identifies the physical address of connected devices.
* **CLI Arguments:** Works professionally via command line with flags (`-t`).

## Requirements
* Python 3.x
* Scapy
* Npcap (for Windows users)

## How to Run
1. Install dependencies:
    pip install scapy
   
2. Run the tool specifying your network range:
   python ARP_Scanner.py -t 192.168.1.1/24
    (Note: Replace 192.168.1.1 with your actual gateway IP)
