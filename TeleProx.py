import requests
import random

GREEN = "\033[0;32m"
END = "\033[0m"
BLUE = "\033[0;34m"
RED = "\033[0;31m"
BOLD = "\033[1m"



def banner():

  print(rf"""{GREEN}
      ██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗     ██████╗ ██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗ 
      ██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝    ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
      ██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝     ██║  ███╗██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝
      ██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝      ██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗
      ██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║       ╚██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝███████╗██║  ██║
      ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝        ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                    Telegram Proxy Grabber Bot
                                        Auther : Arbab Gul
                                          Version : 1.0{END}""")



class ProxyGrabber:
    def __init__(self):
        self.user_agents = [
            # Chrome
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
            
            # Firefox
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0',
            
            # Safari
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
            
            # Edge
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59',
            
            # More user agents
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (Linux; Android 10; SM-G980F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36'
            'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'
            'Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; rv:11.0) like Gecko'
            'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; TNJB; rv:11.0) like Gecko'
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'
            'Mozilla/5.0 (Windows NT 6.3; ARM; Trident/7.0; Touch; rv:11.0) like Gecko'
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0'
            'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MDDCJS; rv:11.0) like Gecko'
            'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
            'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'
            'Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4'
            'Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFASWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36'
            'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12H321 Safari/600.1.4'
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36'
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'
            'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko'
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:40.0) Gecko/20100101 Firefox/40.0'
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0'
            'Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4'
            'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MATBJS; rv:11.0) like Gecko'
            'Mozilla/5.0 (Linux; U; Android 4.0.4; en-us; KFJWI Build/IMM76D) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68'
        ]

    def get_random_user_agent(self):
        return random.choice(self.user_agents)

    @staticmethod
    def mtproto(num):
        if num <= 0:
            print(f"{RED}Please enter a valid number greater than 0.{END}")
            exit()
        try:
            url = "https://mtpro.xyz/api/?type=mtproto"
            proxy_grabber = ProxyGrabber()
            pg = proxy_grabber.get_random_user_agent()
            response = requests.get(url,headers={'User-Agent': pg})
            response.raise_for_status()
            json_data = response.json()
            
            total_items = len(json_data)

            if num > total_items:
                print(f"{RED}Requested number exceeds available items. Fetching all available items.{END}")
                print(f"{GREEN}Total items available: {total_items}{END}")
                exit()
            for json in json_data[0:num]:
                print(f"{BOLD}Country: {json['country']}\nHost: {json['host']}\nPort: {json['port']}\nPing: {json['ping']}\nSecret: {json['secret']}{END}")
                print("-" * 55)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")


    @staticmethod
    def socks5(num):
        if num <= 0:
            print(f"{RED}Please enter a valid number greater than 0.{END}")
            exit()
            
        url = "https://mtpro.xyz/api/?type=socks"
        response = requests.get(url)
        response.raise_for_status()
        json_data = response.json()
        total_items = len(json_data)
        
        if num > total_items:
            print(f"{RED}Requested number exceeds available items. Fetching all available items.{END}")
            print(f"{GREEN}Total items available: {total_items}{END}")
            exit()

        for json in json_data[0:num]:
            print(f"{BOLD}Country: {json['country']}\nIP: {json['ip']}\nPort: {json['port']}\nPing: {json['ping']}{END}")
            print("-" * 55)


def main():
    banner()
    choose = input(f'{BLUE}Select Proxy Type (1 for MTProto, 2 for Socks5){END}: ')
    match choose:
        case '1':
            try:
                number_of_proxies = int(input(f"{BLUE}Enter the number of proxies to fetch: {END}"))
                ProxyGrabber.mtproto(number_of_proxies)
            except ValueError:
                print(f"{RED}Invalid input. Please enter a valid number.{END}")
                exit()
        case '2':
            try:
                number_of_proxies = int(input(f"{BLUE}Enter the number of proxies to fetch: {END}"))
                ProxyGrabber.socks5(number_of_proxies)
            except ValueError:
                print(f"{RED}Invalid input. Please enter a valid number.{END}")
                exit()
        case _:
            print(f"{RED}Invalid choice. Please select 1 or 2.{END}")

if __name__ == "__main__":
    main()
