# pip install dnspython

import dns.resolver

def dns_lookup(domain):
    records = ["A", "AAAA", "MX", "NS", "TXT"]
    results = {}

    for record in records:
        try:
            answers = dns.resolver.resolve(domain, record)
            results[record] = [str(ans) for ans in answers]
        except dns.resolver.NoAnswer:
            results[record] = ["No record found"]
        except dns.resolver.NXDOMAIN:
            print(f"❌ Domain {domain} does not exist.")
            return None
        except dns.exception.Timeout:
            print(f"⚠️ DNS query timed out for {record} records.")
            results[record] = ["Query timed out"]

    return results

def save_results(domain, results):
    filename = f"dns_results_{domain}.txt"
    with open(filename, "w") as file:
        file.write(f"DNS Lookup Results for {domain}\n\n")
        for record, values in results.items():
            file.write(f"{record} Records:\n")
            for value in values:
                file.write(f"  - {value}\n")
            file.write("\n")
    
    print(f"\n✅ Results saved to {filename}")

if __name__ == "__main__":
    domain = input("🔗 Enter a domain (e.g., example.com): ").strip()
    results = dns_lookup(domain)
    
    if results:
        print("\n📜 DNS Records Found:")
        for record, values in results.items():
            print(f"{record}: {values}")
        
        save_results(domain, results)
