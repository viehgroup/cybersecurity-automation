import socket

domain = input("Enter Domain: ")

subdomains = [
    "www",
    "mail",
    "api",
    "blog",
    "dev",
    "test",
    "admin",
    "portal"
]

print("\nScanning...\n")

for sub in subdomains:
    target = f"{sub}.{domain}"

    try:
        ip = socket.gethostbyname(target)
        print(f"[+] Found: {target} -> {ip}")

    except socket.gaierror:
        pass
