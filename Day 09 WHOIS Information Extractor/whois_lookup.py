import whois

domain = input("Enter Domain: ")

try:
    data = whois.whois(domain)

    print("\nDomain Name:")
    print(data.domain_name)

    print("\nRegistrar:")
    print(data.registrar)

    print("\nCreation Date:")
    print(data.creation_date)

    print("\nExpiration Date:")
    print(data.expiration_date)

    print("\nName Servers:")

    if data.name_servers:
        for ns in data.name_servers:
            print(ns)

except Exception as e:
    print(f"Error: {e}")
