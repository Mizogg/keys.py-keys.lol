# keys.py Full Random Bitcoin Legacy compressed/uncompresses address and Segwit address Online Transactions\Balance\TotalReceaived. 09/07/2021
# Good Luck and Happy Hunting. Made by mizogg.co.uk
# Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD
from time import sleep
import bit
import requests
from bitcoin import *
import colorama
from colorama import Fore, Back, Style
colorama.init()
import atexit
from time import time
from datetime import timedelta, datetime
from bit import *
from bit.format import bytes_to_wif


def seconds_to_str(elapsed=None):
    if elapsed is None:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    else:
        return str(timedelta(seconds=elapsed))


def log(txt, elapsed=None):
    print('\n ' + Fore.BLUE + '  [TIMING]> [' + seconds_to_str() + '] ----> ' + txt + '\n' )
    if elapsed:
        print("\n " + Fore.RED + " [TIMING]> Elapsed time ==> " + elapsed + "\n" )


def end_log():
    end = time()
    elapsed = end-start
    log("End Program", seconds_to_str(elapsed))


start = time()
atexit.register(end_log)
log("Start Program")


print(Fore.GREEN + "Start search... Pick Range 128 Above you starting range or it will not work")
x=int(input(Fore.YELLOW +"'start range Min 1-115792089237316195423570985008687907852837564279074904382605163141518161494335 -> "))
y=int(input("stop range Max 115792089237316195423570985008687907852837564279074904382605163141518161494336 -> "))
print(Fore.RED + "Starting search... Please Wait ")
print("=====================================================")

query = []
F = []
P = x
count=0
total=0
pagenumber=0
while P<y:
    P+=1
    ran = P
    key = Key.from_int(ran)
    wif = bytes_to_wif(key.to_bytes(), compressed=False)
    wif2 = bytes_to_wif(key.to_bytes(), compressed=True)
    key1 = Key(wif)
    caddr = key.address #Legacy compressed address
    uaddr = key1.address #Legacy uncompressed address
    saddr = key.segwit_address  #Segwit address
    query.append(caddr)
    count+=1
    total+=128 
    seed=str(ran)
    pagenumber= int(seed)//128
    if len(query) == 128:
        
        try:
            request = requests.get("https://blockchain.info/multiaddr?active=%s" % ','.join(query), timeout=10)
            request = request.json()
            print(Fore.BLUE + "\nkeys.py---" + Fore.RED + "Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD" + Fore.BLUE + "---keys.py"   + seconds_to_str())
            print(Fore.RED + '\nPrivateKey (hex) Last One in Scan : ' + Fore.YELLOW + key.to_hex() + Fore.RED + ' : PrivateKey (hex) Last One in Scan' + Style.RESET_ALL)
            print(Fore.RED + '\nPrivateKey (dec) Last One in Scan : ' + Fore.YELLOW + seed + Fore.RED + ' : PrivateKey (dec) Last One in Scan' + Style.RESET_ALL)
            print(Fore.RED + '\n WARNING !!!!  Any Winners found will be Within 128 Private Key range of this Scan !!!! WARNING !!!!'+ Style.RESET_ALL)
            print ('\n-- keys.py -- ' + Fore.GREEN +  'Running Scan : ' + str (count) + '  :  ' + Fore.BLUE + 'Total Bitcoin Addresses : ' + str (total) + ' : ' + Fore.YELLOW + seconds_to_str() + '] ----> '   + Style.RESET_ALL)

            #Parse results
            for row in request["addresses"]:
                print(row)
                print(Fore.GREEN +  '<--------------------------------Page Number ' , Fore.YELLOW , pagenumber , Fore.GREEN , ' on Keys--------------------------------> '+ Style.RESET_ALL)
                if row["final_balance"] > 0:
                    print(Fore.GREEN + "\nMatching Key ==== Found!!!\n PrivateKey: " + Fore.YELLOW + key.to_hex() + Style.RESET_ALL)
                    print(Fore.GREEN + "\nMatching Key ==== Found!!!\n Page Number: " + Fore.YELLOW , pagenumber , Style.RESET_ALL)
                    f=open(u"winner.txt","a")
                    f.write('\n=============Bitcoin Address with Balance Found=====================')
                    f.write('\nPrivateKey (hex) Last One on Page: ' + key.to_hex())
                    f.write('\nBitcoin Address Compressed : ' + caddr)
                    f.write('\nBitcoin Address UnCompressed :' + uaddr)
                    f.write('\nBitcoin Segwit Address :' + saddr)
                    f.write('\nPrivateKey (wif) Compressed : ' + wif2)
                    f.write('\nPrivateKey (wif) UnCompressed : ' + wif)
                    f.write('\n Check All Addresses within 128 in this range to find wallet')
                    f.write('\n Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD ' )
                    f.close()
                    print('\a')
                    break
        except:
            pass

        # Reset counter
        query = []
        sleep(10) # Reduce Sleep to go faster
