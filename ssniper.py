import requests
import sys
from threading import Thread
from colorama import Fore, init

# Developer/s: SirCryptic @ (NullSecurityTeam) - 0XJACK @ (deletehumanity)
# Info: ssniper (social sniper)
# Greetz To ecriminals for pulling a stupid issue request on a 3 year old script ¯\_(ツ)_/¯ ~ (https://github.com/ecriminals)

init()

class c:
    g = Fore.GREEN
    y = Fore.YELLOW
    r = Fore.RED
    w = Fore.WHITE

def getList():
    try:
        wlist = open('socials.txt', 'r')
        return wlist
    except:
        print('Unable to open social list')
        sys.exit()

def testMedia(name, social, f, s, outfile=None):
    global num
    try:
        r = requests.get(f.strip() + name.strip() + s.strip())
    except KeyboardInterrupt:
        print()
        sys.exit()
    if r.status_code == 200:
        print('"%s" exists on %s'%(c.g+name+c.w, c.g+social+c.w))
        num += 1
        if outfile is not None:
            with open(outfile, "a") as f_out:
                f_out.write(f"{social}: {f.strip()}{name.strip()}{s.strip()}\n")
    else:
        if '-v' in sys.argv:
            print('"%s" does not exist on %s'%(c.r+name+c.w, c.r+social+c.w))

def parseW(name, list, s):
    global num
    num = 0
    outfile = f"{name}.txt" if s else None
    for line in list:
        if line.strip() != '' and line.strip()[0] != '#':
            social, page = line.split(':', 1)
            f,s = page.split('<user>')
            if '-t' in sys.argv:
                #print(c.y + '---[-]' + c.w + ' Scanning %s...'%(page.strip()))
                t = Thread(target = testMedia, args=(name,social,f,s,outfile))
                t.start()
            else:
                testMedia(name, social, f,s,outfile)
    if '-t' not in sys.argv:
        print('%s accounts found with the username: %s'%(c.g+str(num)+c.w, c.g+name+c.w))
        if outfile is not None:
            print(f"Results saved to {outfile}")

def main():
    if len(sys.argv) < 2:
        print('Usage:\n\tpython3 %s <username> <-t(hread)> <-v(erbose)> <-s(ave)>\nExample:\n\tpython %s exampleuser -v -t -s\n'%(sys.argv[0], sys.argv[0]))
        sys.exit()

    uname = sys.argv[1]
    wlist = getList()
    save = '-s' in sys.argv
    parseW(uname, wlist, save)

if __name__ == '__main__':
    main()
