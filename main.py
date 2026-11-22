import os
import sys
import time
import requests
import json
import random
import re
import base64

RESET="\033[0m"; BOLD="\033[1m"; GREEN="\033[92m"; RED="\033[91m"; YELLOW="\033[93m"; BLUE="\033[94m"; CYAN="\033[96m"; WHITE="\033[97m"; MAGENTA="\033[95m"

# ================== CONFIGURATION ==================
API_BASE = "https://ftgm-simdb.vercel.app/api?query="
# ===================================================

def clear(): os.system("clear")

def show_banner():
    print(f"""{CYAN}{BOLD}
    ██████╗  ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗████╗  ██║
    ██████╔╝██║   ██║██╔████╔██║███████║██╔██╗ ██║
    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
    ██║  ██║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
    {RED}⠀⠀⠀⠀⠀⠀⠀⣠⣶⣶⣦⡀⠀
    {RED}⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⠀⠀⣴⣶⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣧
    {RED}⠀⠀⠀⠀⣼⣿⣿⣿⡿⣿⣿⣆⠀⠀⠀⠀⠀⠀⣠⣴⣶⣤⡀⠀
    {RED}⠀⠀⠀⢰⣿⣿⣿⣿⠃⠈⢻⣿⣦⠀⠀⠀⠀⣸⣿⣿⣿⣿⣷⠀
    {RED}⠀⠀⠀⠘⣿⣿⣿⡏⣴⣿⣷⣝⢿⣷⢀⠀⢀⣿⣿⣿⣿⡿⠋⠀
    {RED}⠀⠀⠀⠀⢿⣿⣿⡇⢻⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⢸⣿⣿⣇⢸⣿⣿⡟⠙⠛⠻⣿⣿⣿⣿⡇⠀⠀⠀⠀
    {RED}⣴⣿⣿⣿⣿⣿⣿⣿⣠⣿⣿⡇⠀⠀⠀⠉⠛⣽⣿⣇⣀⣀⣀⠀
    {RED}⠙⠻⠿⠿⠿⠿⠿⠟⠿⠿⠿⠇⠀⠀⠀⠀⠀⠻⠿⠿⠛⠛⠛{RESET}
    {MAGENTA}{BOLD}   [ R O M A N   O V E R L O R D   S I M   D B ]{RESET}
    {YELLOW}══════════════════════════════════════════════════{RESET}
    {GREEN} DEV: {WHITE}ROMAN HACKER {GREEN}| TG: {WHITE}@romanempire078{RESET}
    {YELLOW}══════════════════════════════════════════════════{RESET}
    """)

def hacker_loading(msg, duration=1.0):
    frames = ["|", "/", "-", "\\"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r{YELLOW}{BOLD}  [{frames[i % 4]}] {msg}...{RESET}   ")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write(f"\r{GREEN}{BOLD}  [✓] {msg} DONE!{RESET}          \n")

def fake_sql_injection():
    queries = [
        "SELECT * FROM users WHERE mobile = '{}'",
        "UNION SELECT null, username, password FROM admins",
        "SELECT table_name FROM information_schema.tables",
        "UPDATE users SET access_level = 'ROOT' WHERE id = 1"
    ]
    print(f"\n{RED}{BOLD}  [!] INITIATING SQL INJECTION...{RESET}")
    for i in range(3):
        q = random.choice(queries)
        print(f"\033[91m  [SQL] {q}\033[0m")
        time.sleep(0.3)

def fake_proxy_routing():
    print(f"\n{CYAN}{BOLD}  [!] ROUTING VIA SECURE PROXIES...{RESET}")
    for _ in range(3):
        ip = f"{random.randint(11, 250)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"
        print(f"\033[93m  [PROXY] Connecting to Node {ip} -> OK\033[0m")
        time.sleep(0.2)

def save_to_clipboard(data):
    try:
        # Try termux-clipboard-set
        b64_data = base64.b64encode(data.encode('utf-8')).decode('utf-8')
        os.system(f"echo '{b64_data}' | base64 -d | termux-clipboard-set")
        print(f"{GREEN}  [✓] Result copied to clipboard!{RESET}")
    except Exception:
        print(f"{YELLOW}  [!] Clipboard not available (Termux API missing).{RESET}")

def display_results(results, query, search_type):
    clear()
    show_banner()
    print(f"\n{GREEN}{BOLD}  [✓] DATA BREACH SUCCESSFUL!{RESET}")
    print(f"{RED}  [!] TARGET: {WHITE}{query} ({search_type}){RESET}\n")
    
    all_text = ""
    for idx, rec in enumerate(results, 1):
        name = rec.get('Name', 'Unknown')
        mobile = rec.get('Mobile', 'N/A')
        cnic = rec.get('CNIC', 'N/A')
        address = rec.get('ADDRESS', 'N/A')
        
        rec_text = f"""
╔══════════════════════════════════════════════════╗
║               🔓 RECORD #{idx} DECRYPTED 🔓              ║
╠══════════════════════════════════════════════════╣
║  {YELLOW}NAME    : {WHITE}{name[:35]:<35} {CYAN}║
║  {YELLOW}MOBILE  : {WHITE}{mobile[:35]:<35} {CYAN}║
║  {YELLOW}CNIC    : {WHITE}{cnic[:35]:<35} {CYAN}║
║  {YELLOW}ADDRESS : {WHITE}{address[:35]:<35} {CYAN}║
╚══════════════════════════════════════════════════╝
"""
        print(rec_text)
        all_text += rec_text
        
    all_text += f"\n── HACKED BY ROMAN HACKER ──\n"
    save_to_clipboard(all_text)

def fetch_data(query, search_type):
    # Animation Sequence
    fake_proxy_routing()
    hacker_loading(f"Bypassing NADRA Firewall for {search_type}", 1.2)
    fake_sql_injection()
    hacker_loading("Extracting Encrypted Data", 1.5)
    
    print(f"\n{YELLOW}  [~] Fetching Raw Payload from Server...{RESET}")
    time.sleep(1)
    
    url = API_BASE + query
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code != 200:
            print(f"{RED}  [!] Server Rejected Connection: {response.status_code}{RESET}")
            input(f"\n{CYAN}  Press ENTER to return...{RESET}")
            return
            
        data = response.json()
        hacker_loading("Decrypting AES-256 Payload", 1.2)
        
        if data.get('status') == 'not_found' or not data.get('results'):
            print(f"\n{RED}  [X] NO RECORDS FOUND FOR {query}.{RESET}")
            input(f"\n{CYAN}  Press ENTER to return...{RESET}")
            return
            
        results = data.get('results', [])
        valid_results = [r for r in results if isinstance(r, dict)]
        
        if not valid_results:
            print(f"\n{RED}  [X] NO VALID RECORDS FOUND.{RESET}")
            input(f"\n{CYAN}  Press ENTER to return...{RESET}")
            return

        display_results(valid_results, query, search_type)
            
    except requests.exceptions.Timeout:
        print(f"\n{RED}  [!] Error: Connection Timed Out.{RESET}")
    except requests.exceptions.ConnectionError:
        print(f"\n{RED}  [!] Error: No Internet Connection.{RESET}")
    except json.JSONDecodeError:
        print(f"\n{RED}  [!] Error: Invalid API Response.{RESET}")
    except Exception as e:
        print(f"\n{RED}  [!] System Error: {e}{RESET}")
    finally:
        input(f"\n{CYAN}  Press ENTER to return to main menu...{RESET}")

def search_by_number():
    clear()
    show_banner()
    print(f"{GREEN}{BOLD}  ► SEARCH BY MOBILE NUMBER{RESET}\n")
    number = input(f"{WHITE}  [?] Enter Mobile Number (e.g., 03001234567): {RESET}").strip()
    
    clean_num = re.sub(r'\D', '', number) # Keep only digits
    if len(clean_num) < 10 or len(clean_num) > 12:
        print(f"{RED}  [!] Invalid Number! Please enter a valid mobile number.{RESET}")
        time.sleep(2)
        return
        
    fetch_data(clean_num, "Mobile")

def search_by_cnic():
    clear()
    show_banner()
    print(f"{GREEN}{BOLD}  ► SEARCH BY CNIC{RESET}\n")
    cnic = input(f"{WHITE}  [?] Enter CNIC without dashes (13 digits): {RESET}").strip()
    
    clean_cnic = re.sub(r'\D', '', cnic)
    if len(clean_cnic) != 13:
        print(f"{RED}  [!] Invalid CNIC! Must be exactly 13 digits.{RESET}")
        time.sleep(2)
        return
        
    fetch_data(clean_cnic, "CNIC")

def bulk_search():
    clear()
    show_banner()
    print(f"{GREEN}{BOLD}  ► BULK SEARCH (Comma Separated){RESET}\n")
    queries = input(f"{WHITE}  [?] Enter queries (e.g., 03001234567,3520112345671): {RESET}").strip()
    
    query_list = [q.strip() for q in queries.split(',') if q.strip()]
    if not query_list:
        print(f"{RED}  [!] No queries provided.{RESET}")
        time.sleep(2)
        return
        
    for query in query_list:
        # Determine if it's a number or CNIC
        clean = re.sub(r'\D', '', query)
        if len(clean) == 13:
            fetch_data(clean, "CNIC")
        elif 10 <= len(clean) <= 12:
            fetch_data(clean, "Mobile")
        else:
            print(f"{RED}  [!] Skipping invalid query: {query}{RESET}")
            time.sleep(1)

def main():
    while True:
        try:
            clear()
            show_banner()
            print(f"""{BLUE}{BOLD}
    ┌──────────────────────────────────────────────────┐
    │             ROMAN OVERLORD SIM DATABASES         │
    ├──────────────────────────────────────────────────┤
    │  {WHITE}[1]{GREEN} Search Ownership (By Number)              │
    │  {WHITE}[2]{GREEN} Search All Numbers (By CNIC)              │
    │  {WHITE}[3]{GREEN} Bulk Search (Multiple Queries)            │
    │  {WHITE}[4]{RED} Exit System                               │
    └──────────────────────────────────────────────────┘
{RESET}""")
            
            choice = input(f"{GREEN}{BOLD}  └──► Select Option [1-4]: {RESET}").strip()
            
            if choice == "1":
                search_by_number()
            elif choice == "2":
                search_by_cnic()
            elif choice == "3":
                bulk_search()
            elif choice == "4":
                print(f"\n{RED} Exiting System...{RESET}")
                time.sleep(1)
                break
            else:
                time.sleep(0.5)
        except KeyboardInterrupt:
            print(f"\n{RED}  System Terminated.{RESET}")
            break
        except Exception as e:
            print(f"\n{RED}  Unexpected Error: {e}{RESET}")
            time.sleep(2)

if __name__ == "__main__":
    main()
