import os
import sys
import time
import random
import threading
from datetime import datetime

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class FacebookBruteForce:
    def __init__(self):
        self.target = ""
        self.wordlist = ""
        self.proxy_status = False
        self.attempts = 0
        self.found_password = None
        self.running = False
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_banner(self):
        banner = f"""
{Colors.CYAN}{Colors.BOLD}
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║  ███████╗ █████╗  ██████╗███████╗██████╗  ██████╗  ██████╗██╗  ║
║  ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔═══██╗██╔════╝██║  ║
║  █████╗  ███████║██║     █████╗  ██████╔╝██║   ██║██║     ██║  ║
║  ██╔══╝  ██╔══██║██║     ██╔══╝  ██╔══██╗██║   ██║██║     ██║  ║
║  ██║     ██║  ██║╚██████╗███████╗██████╔╝╚██████╔╝╚██████╗██║  ║
║  ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═════╝  ╚═════╝  ╚═════╝╚═╝  ║
║                                                                ║
║                   {Colors.RED}BRUTE FORCE TOOL{Colors.CYAN}                     ║
║                    {Colors.YELLOW}by ChowdhuryVai{Colors.CYAN}                     ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
{Colors.END}
"""
        print(banner)
    
    def print_info(self):
        info = f"""
{Colors.YELLOW}{Colors.BOLD}[!] DEVELOPER INFORMATION:{Colors.END}
{Colors.CYAN}├── Telegram ID: {Colors.WHITE}https://t.me/darkvaiadmin{Colors.END}
{Colors.CYAN}├── Telegram Channel: {Colors.WHITE}https://t.me/windowspremiumkey{Colors.END}
{Colors.CYAN}└── Hacking/Cracking Website: {Colors.WHITE}https://crackyworld.com/{Colors.END}
"""
        print(info)
    
    def print_config(self):
        config = f"""
{Colors.GREEN}{Colors.BOLD}[>] CONFIGURATION:{Colors.END}
{Colors.CYAN}├── Target: {Colors.WHITE}{self.target}{Colors.END}
{Colors.CYAN}├── Wordlist: {Colors.WHITE}{self.wordlist}{Colors.END}
{Colors.CYAN}└── Proxy Status: {Colors.WHITE}{'[ON]' if self.proxy_status else '[OFF]'}{Colors.END}
"""
        print(config)
    
    def loading_animation(self, message, duration=3):
        animation = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
        start_time = time.time()
        i = 0
        
        while time.time() - start_time < duration:
            print(f"\r{Colors.YELLOW}[{animation[i % len(animation)]}] {message}{Colors.END}", end="")
            time.sleep(0.1)
            i += 1
        
        print("\r" + " " * (len(message) + 10) + "\r", end="")
    
    def check_wordlist(self, wordlist_path):
        if not os.path.exists(wordlist_path):
            print(f"{Colors.RED}[!] Wordlist file not found: {wordlist_path}{Colors.END}")
            return False
        
        try:
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                line_count = sum(1 for _ in f)
            
            if line_count == 0:
                print(f"{Colors.RED}[!] Wordlist is empty{Colors.END}")
                return False
            
            print(f"{Colors.GREEN}[+] Wordlist loaded: {line_count} passwords{Colors.END}")
            return True
        except Exception as e:
            print(f"{Colors.RED}[!] Error reading wordlist: {str(e)}{Colors.END}")
            return False
    
    def simulate_login(self, password):
        # Simulate network delay
        time.sleep(random.uniform(0.1, 0.5))
        
        # In a real tool, this would make an actual HTTP request to Facebook
        # For demonstration, we'll simulate finding a password after many attempts
        self.attempts += 1
        
        # Simulate finding password after many attempts (for demo purposes)
        if self.attempts > 50 and random.random() < 0.02:  # 2% chance after 50 attempts
            return True
        
        # Common passwords that might "work" in simulation
        common_passwords = ["password123", "facebook123", "admin123", "chowdhury", "darkvai"]
        if password.strip() in common_passwords:
            return True
            
        return False
    
    def brute_force_attack(self):
        if not self.check_wordlist(self.wordlist):
            return
        
        print(f"\n{Colors.RED}{Colors.BOLD}[~] BRUTE FORCE ATTACK: ENABLED [~]{Colors.END}\n")
        
        self.running = True
        self.attempts = 0
        start_time = time.time()
        
        try:
            with open(self.wordlist, 'r', encoding='utf-8', errors='ignore') as f:
                for line_num, password in enumerate(f, 1):
                    if not self.running:
                        break
                    
                    password = password.strip()
                    if not password:
                        continue
                    
                    # Display attempt with colorful formatting
                    color = random.choice([Colors.RED, Colors.YELLOW, Colors.BLUE, Colors.PURPLE, Colors.CYAN])
                    print(f"{color}[{line_num}] Trying Password[ {{{password}}} ] {Colors.RED}→ Login Failed{Colors.END}")
                    
                    # Simulate login attempt
                    if self.simulate_login(password):
                        self.found_password = password
                        print(f"\n{Colors.GREEN}{Colors.BOLD}[!] PASSWORD FOUND: {password}{Colors.END}")
                        print(f"{Colors.GREEN}[+] Account successfully compromised!{Colors.END}")
                        break
                    
                    # Add small delay for realism
                    time.sleep(0.05)
                    
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}[!] Attack interrupted by user{Colors.END}")
        except Exception as e:
            print(f"\n{Colors.RED}[!] Error during attack: {str(e)}{Colors.END}")
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        self.show_summary(elapsed_time)
    
    def show_summary(self, elapsed_time):
        print(f"\n{Colors.CYAN}{Colors.BOLD}[*] ATTACK SUMMARY:{Colors.END}")
        print(f"{Colors.CYAN}├── Target: {Colors.WHITE}{self.target}{Colors.END}")
        print(f"{Colors.CYAN}├── Total Attempts: {Colors.WHITE}{self.attempts}{Colors.END}")
        print(f"{Colors.CYAN}├── Time Elapsed: {Colors.WHITE}{elapsed_time:.2f} seconds{Colors.END}")
        
        if self.found_password:
            print(f"{Colors.CYAN}├── Status: {Colors.GREEN}SUCCESS{Colors.END}")
            print(f"{Colors.CYAN}└── Password: {Colors.GREEN}{self.found_password}{Colors.END}")
        else:
            print(f"{Colors.CYAN}├── Status: {Colors.RED}FAILED{Colors.END}")
            print(f"{Colors.CYAN}└── Result: {Colors.RED}Password not found in wordlist{Colors.END}")
    
    def main_menu(self):
        while True:
            self.clear_screen()
            self.print_banner()
            self.print_info()
            
            if self.target:
                self.print_config()
            
            print(f"\n{Colors.GREEN}{Colors.BOLD}[*] MAIN MENU:{Colors.END}")
            print(f"{Colors.CYAN}[1] Set Target{Colors.END}")
            print(f"{Colors.CYAN}[2] Set Wordlist{Colors.END}")
            print(f"{Colors.CYAN}[3] Toggle Proxy{Colors.END}")
            print(f"{Colors.CYAN}[4] Start Attack{Colors.END}")
            print(f"{Colors.CYAN}[5] Exit{Colors.END}")
            
            choice = input(f"\n{Colors.YELLOW}[?] Select option: {Colors.END}").strip()
            
            if choice == "1":
                self.set_target()
            elif choice == "2":
                self.set_wordlist()
            elif choice == "3":
                self.toggle_proxy()
            elif choice == "4":
                if self.target and self.wordlist:
                    self.start_attack()
                else:
                    print(f"{Colors.RED}[!] Please set target and wordlist first{Colors.END}")
                    input(f"{Colors.YELLOW}[?] Press Enter to continue...{Colors.END}")
            elif choice == "5":
                print(f"\n{Colors.GREEN}[+] Thank you for using ChowdhuryVai's Facebook Brute Force Tool!{Colors.END}")
                sys.exit(0)
            else:
                print(f"{Colors.RED}[!] Invalid option{Colors.END}")
                input(f"{Colors.YELLOW}[?] Press Enter to continue...{Colors.END}")
    
    def set_target(self):
        self.target = input(f"\n{Colors.YELLOW}[?] Enter target email/username: {Colors.END}").strip()
        if self.target:
            print(f"{Colors.GREEN}[+] Target set to: {self.target}{Colors.END}")
        else:
            print(f"{Colors.RED}[!] Invalid target{Colors.END}")
    
    def set_wordlist(self):
        self.wordlist = input(f"\n{Colors.YELLOW}[?] Enter wordlist path: {Colors.END}").strip()
        if self.wordlist and os.path.exists(self.wordlist):
            print(f"{Colors.GREEN}[+] Wordlist set to: {self.wordlist}{Colors.END}")
        else:
            print(f"{Colors.RED}[!] Wordlist file not found{Colors.END}")
            self.wordlist = ""
    
    def toggle_proxy(self):
        self.proxy_status = not self.proxy_status
        status = "ON" if self.proxy_status else "OFF"
        print(f"\n{Colors.GREEN}[+] Proxy status set to: [{status}]{Colors.END}")
    
    def start_attack(self):
        self.clear_screen()
        self.print_banner()
        self.print_config()
        
        print(f"\n{Colors.YELLOW}[!] Starting attack in 3 seconds...{Colors.END}")
        for i in range(3, 0, -1):
            print(f"{Colors.RED}[{i}]{Colors.END}", end=" ", flush=True)
            time.sleep(1)
        print("\n")
        
        # Start attack in a separate thread to allow interruption
        attack_thread = threading.Thread(target=self.brute_force_attack)
        attack_thread.start()
        
        try:
            while attack_thread.is_alive():
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.running = False
            print(f"\n{Colors.YELLOW}[!] Stopping attack...{Colors.END}")
            attack_thread.join()
        
        input(f"\n{Colors.YELLOW}[?] Press Enter to continue...{Colors.END}")

if __name__ == "__main__":
    try:
        tool = FacebookBruteForce()
        tool.main_menu()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Tool interrupted by user{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}[!] Unexpected error: {str(e)}{Colors.END}")
