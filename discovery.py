import requests
import os

def brute_force(url, wordlist_path):
    if not os.path.exists(wordlist_path):
        print(f"[!] Error: Wordlist file '{wordlist_path}' not found.")
        return

    print(f"[*] Starting scan on: {url}\n")
    
    with open(wordlist_path, 'r') as file:
        for line in file:
            directory = line.strip()
            full_url = f"{url}/{directory}"
            
            try:
                response = requests.get(full_url, timeout=5)
                
                if response.status_code == 200:
                    print(f"[+] Found: {full_url} (Status: 200)")
                elif response.status_code == 403:
                    print(f"[!] Forbidden: {full_url} (Status: 403)")
                
            except requests.exceptions.RequestException:
                pass

def main():
    print("--- CTF Web Directory Brute-Forcer ---")
    target_url = input("Enter target URL (e.g., http://example.com): ").strip("/")
    wordlist = input("Enter path to wordlist (e.g., wordlist.txt): ")
    
    brute_force(target_url, wordlist)

if __name__ == "__main__":
    main()