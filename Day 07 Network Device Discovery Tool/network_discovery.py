import subprocess
import socket

network = input("Enter Network Prefix (e.g. 192.168.1): ")

print("\nScanning Network...\n")

for i in range(1, 255):
    ip = f"{network}.{i}"

    try:
        result = subprocess.run(
            ["ping", "-c", "1", "-W", "1", ip],
            stdout=subprocess.DEVNULL
        )

        if result.returncode == 0:

            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except:
                hostname = "Unknown"

            print("[+] Device Found")
            print(f"IP Address: {ip}")
            print(f"Hostname: {hostname}\n")

    except:
        pass
