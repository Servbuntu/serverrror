import playsound, os, json, sys, copy
path = os.path.dirname(os.path.realpath(__file__))

user = json.load(open('/serv/core/data/user.json'))
class colour:
   PURPLE = '\033[1;35;48m'
   CYAN = '\033[0;36;48m'
   class bold:
        RED = '\033[1;31;48m'
        GREEN = '\033[1;32;48m'
        YELLOW = '\033[1;33;48m'
        BLUE = '\033[1;34;48m'
        CYAN = '\033[1;36;48m'
   BLUE = '\033[0;34;48m'
   GREEN = '\033[0;32;48m'
   YELLOW = '\033[0;33;48m'
   RED = '\033[0;31;48m'
   BLACK = '\033[0;30;48m'
   UNDERLINE = '\033[4;37;48m'
   END = '\033[0;37;0m'
exitcode = 0
def setexitcode(code):
    global exitcode
    exitcode = copy.copy(code)
def exit(code=None):
    if(code == None):
        sys.exit(exitcode)
    else:
        sys.exit(code)
def error(text, severity=0, exiting=False):
    if(severity >= user["sounds"] and exiting == False):
        print(colour.bold.RED + "[-] " + colour.END + colour.RED + text + colour.END)
        playsound.playsound('/serv/core/core/hellnaw.mp3', True)
    if(exiting != False):
        if(severity >= user["sounds"]):
            playsound.playsound('/serv/core/core/hellnaw.mp3', True)
        print(colour.bold.RED + "[--] " + colour.END + colour.RED + text + colour.END)
        if(exiting == True):
            sys.exit()
        else:
            sys.exit(exiting)
    else:
        print(colour.bold.RED + "[-] " + colour.END + colour.RED + text + colour.END)
def success(text):
    print(colour.bold.GREEN + "[+] " + colour.END + colour.GREEN + text + colour.END)
def warning(text):
    print(colour.bold.YELLOW + "[!] " + colour.END + colour.YELLOW + text + colour.END)
def info(text):
    print(colour.bold.BLUE + "[i] " + colour.END + colour.BLUE + text + colour.END)
def header(text):
    print(colour.bold.CYAN + text + colour.END)
#error("This is an error!", 1)
#success("This is a success!")
#warning("This is a warning!")
#info("This is an info!")
#error("This is an EXTREMLEY SEVERE error which is terminating this!", 5, 2)
#print("hi")