import requests

cve_id = input("Enter CVE ID: ").upper()

url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={cve_id}"

try:
    response = requests.get(url, timeout=10)
    data = response.json()

    vulnerabilities = data.get("vulnerabilities", [])

    if not vulnerabilities:
        print("CVE not found.")
        exit()

    cve = vulnerabilities[0]["cve"]

    description = cve["descriptions"][0]["value"]

    metrics = cve.get("metrics", {})

    cvss_score = "N/A"

    if "cvssMetricV31" in metrics:
        cvss_score = metrics["cvssMetricV31"][0]["cvssData"]["baseScore"]

    print("\nCVE ID:")
    print(cve_id)

    print("\nCVSS Score:")
    print(cvss_score)

    print("\nDescription:")
    print(description)

except Exception as e:
    print(f"Error: {e}")
