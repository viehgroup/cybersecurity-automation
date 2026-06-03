import ssl
import socket
from datetime import datetime

domain = input("Enter Domain: ")

try:
    context = ssl.create_default_context()

    with socket.create_connection((domain, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:

            cert = ssock.getpeercert()

            issuer = dict(x[0] for x in cert['issuer'])
            valid_from = cert['notBefore']
            valid_until = cert['notAfter']

            expiry_date = datetime.strptime(
                valid_until,
                "%b %d %H:%M:%S %Y %Z"
            )

            days_remaining = (
                expiry_date - datetime.utcnow()
            ).days

            print("\nCertificate Information\n")

            print("Issuer:")
            print(issuer.get('organizationName', 'Unknown'))

            print("\nValid From:")
            print(valid_from)

            print("\nValid Until:")
            print(valid_until)

            print("\nDays Remaining:")
            print(days_remaining)

except Exception as e:
    print(f"Error: {e}")
