# app.py
from flask import Flask, render_template, request, redirect, url_for, jsonify
from subdomain_enumerator import subdomain_enumerator
from xss_scanner import advanced_xss_scan
import time

app = Flask(__name__)

# In-memory cache for subdomain results.
SUBDOMAIN_CACHE = {}

@app.route("/")
def splash():
    # Display the splash screen with "Hello Hacker"
    return render_template("splash.html")     

@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        action = request.form.get("action")
        if action == "subdomains":
            domain = request.form.get("domain")
            if domain:
                time.sleep(1)  # simulate delay for animation
                subdomains = subdomain_enumerator(domain)
                SUBDOMAIN_CACHE[domain] = subdomains
                return redirect(url_for("subdomains", domain=domain))
        elif action == "direct":
            target = request.form.get("target")
            if target:
                return redirect(url_for("direct_scan", target=target))
    return render_template("home.html")

@app.route("/subdomains/<domain>")
def subdomains(domain):
    subs = SUBDOMAIN_CACHE.get(domain, [])
    return render_template("subdomains.html", domain=domain, subdomains=subs)

@app.route("/direct_scan", methods=["GET", "POST"])
def direct_scan():
    if request.method == "POST":
        target = request.form.get("target")
        if target:
            return redirect(url_for("xss_scan", target=target))
    target = request.args.get("target", "")
    return render_template("xss_scan.html", target=target)

@app.route("/xss_scan")
def xss_scan():
    target = request.args.get("target")
    if not target:
        return "No target specified."
    if not target.startswith("http"):
        target = "http://" + target
    # For demonstration, append a test query parameter.
    test_url = f"{target}?test=123"
    # advanced_xss_scan returns vulnerabilities and detailed payload-application logs.
    scan_result = advanced_xss_scan(test_url)
    return render_template("scan_results.html", target=test_url, results=scan_result["vulnerabilities"], details=scan_result["details"])

if __name__ == "__main__":
    app.run(debug=True, port=5000)

    
 
 