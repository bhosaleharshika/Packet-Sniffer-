## 🖥️ How to Run the Project

Follow these steps:<img width="623" height="297" alt="image" src="https://github.com/user-attachments/assets/5a57b746-bced-4a28-8803-15a58092f4f6" />


1️⃣ Download the Project
Click the green **Code** button at the top-right of this repository, then select **Download ZIP**.  
Extract the ZIP file on your computer and save in a folder


2️⃣ Install Python
Make sure you have **Python 3** installed.  
Check using:
```bash
python --version

If not installed, download from:
https://www.python.org/downloads/

3️⃣ Install Required Libraries
Run the following command:

pip install scapy

4️⃣ Run the Script
Navigate to the folder and run:

python packet_sniffer.py
💡 Note: On some systems, you may need to run with administrator/root privileges:

sudo python packet_sniffer.py

5️⃣ View the Output
The program will display captured packets in the terminal.
Example:

Source: 192.168.1.5 -> Destination: 142.250.183.238 | Protocol: TCP | Length: 60
Source: 142.250.183.238 -> Destination: 192.168.1.5 | Protocol: TCP | Length: 52

