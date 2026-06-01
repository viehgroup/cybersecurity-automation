import requests

url = input("Enter URL: ")

headers_to_check = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Permissions-Policy"
]

try:
    response = requests.get(url, timeout=10)

    print("\nChecking Security Headers...\n")

    for header in headers_to_check:
        if header in response.headers:
            print(f"[+] {header} Found")
        else:
            print(f"[-] {header} Missing")

except Exception as e:
    print(f"Error: {e}")
