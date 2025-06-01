# subdomain_enumerator.py
import dns.resolver

def subdomain_enumerator(domain, subdomains_list=None):
    """
    Enumerate subdomains by trying a short list of common prefixes.
    """
    if subdomains_list is None:
        subdomains_list = ["www", "mail", "test", "api", "dev", "blog", "shop", "admin", "m"]
    found = []
    for sub in subdomains_list:
        full_sub = f"{sub}.{domain}"
        try:
            answers = dns.resolver.resolve(full_sub, 'A')
            if answers:
                found.append(full_sub)
        except Exception:
            pass
    return found

if __name__ == "__main__":
    domain = input("Enter a domain (e.g., example.com): ")
    results = subdomain_enumerator(domain)
    print("Found subdomains:")
    for r in results:
        print(" -", r)

          inti and the trnsnbi of the new mania to the old fradg kan jij  dfvjijiuhd eikejn feoifen 