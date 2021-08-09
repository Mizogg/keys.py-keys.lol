# VIP_KEYS.py Random Bitcoin Legacy compressed/uncompresses addresses. Check 128 Addresses for Balance/transaction . Based on keys.lol 09/08/2021
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
import random
import csv
from itertools import zip_longest

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


x=1
y=115792089237316195423570985008687907852837564279074904382605163141518161494336
print(Fore.RED + "Starting search... Please Wait ")
print("=====================================================")

query = []
query1 = []
count=0
total=0
while True:
    ran = random.randint(x,y)
    seed = str(ran)
    key = Key.from_int(ran)
    key1 = Key.from_int(ran+1)
    key2 = Key.from_int(ran+2)
    key3 = Key.from_int(ran+3)
    key4 = Key.from_int(ran+4)
    key5 = Key.from_int(ran+5)
    key6 = Key.from_int(ran+6)
    key7 = Key.from_int(ran+7)
    key8 = Key.from_int(ran+8)
    key9 = Key.from_int(ran+9)
    key10 = Key.from_int(ran+10)
    key11 = Key.from_int(ran+11)
    key12 = Key.from_int(ran+12)
    key13 = Key.from_int(ran+13)
    key14 = Key.from_int(ran+14)
    key15 = Key.from_int(ran+15)
    key16 = Key.from_int(ran+16)
    key17 = Key.from_int(ran+17)
    key18 = Key.from_int(ran+18)
    key19 = Key.from_int(ran+19)
    key20 = Key.from_int(ran+20)
    key21 = Key.from_int(ran+21)
    key22 = Key.from_int(ran+22)
    key23 = Key.from_int(ran+23)
    key24 = Key.from_int(ran+24)
    key25 = Key.from_int(ran+25)
    key26 = Key.from_int(ran+26)
    key27 = Key.from_int(ran+27)
    key28 = Key.from_int(ran+28)
    key29 = Key.from_int(ran+29)
    key30 = Key.from_int(ran+30)
    key31 = Key.from_int(ran+31)
    key32 = Key.from_int(ran+32)
    key33 = Key.from_int(ran+33)
    key34 = Key.from_int(ran+34)
    key35 = Key.from_int(ran+35)
    key36 = Key.from_int(ran+36)
    key37 = Key.from_int(ran+37)
    key38 = Key.from_int(ran+38)
    key39 = Key.from_int(ran+39)
    key40 = Key.from_int(ran+40)
    key41 = Key.from_int(ran+41)
    key42 = Key.from_int(ran+42)
    key43 = Key.from_int(ran+43)
    key44 = Key.from_int(ran+44)
    key45 = Key.from_int(ran+45)
    key46 = Key.from_int(ran+46)
    key47 = Key.from_int(ran+47)
    key48 = Key.from_int(ran+48)
    key49 = Key.from_int(ran+49)
    key50 = Key.from_int(ran+50)
    key51 = Key.from_int(ran+51)
    key52 = Key.from_int(ran+52)
    key53 = Key.from_int(ran+53)
    key54 = Key.from_int(ran+54)
    key55 = Key.from_int(ran+55)
    key56 = Key.from_int(ran+56)
    key57 = Key.from_int(ran+57)
    key58 = Key.from_int(ran+58)
    key59 = Key.from_int(ran+59)
    key60 = Key.from_int(ran+60)
    key61 = Key.from_int(ran+61)
    key62 = Key.from_int(ran+62)
    key63 = Key.from_int(ran+63)
    key64 = Key.from_int(ran+64)
    key65 = Key.from_int(ran+65)
    key66 = Key.from_int(ran+66)
    key67 = Key.from_int(ran+67)
    key68 = Key.from_int(ran+68)
    key69 = Key.from_int(ran+69)
    key70 = Key.from_int(ran+70)
    key71 = Key.from_int(ran+71)
    key72 = Key.from_int(ran+72)
    key73 = Key.from_int(ran+73)
    key74 = Key.from_int(ran+74)
    key75 = Key.from_int(ran+75)
    key76 = Key.from_int(ran+76)
    key77 = Key.from_int(ran+77)
    key78 = Key.from_int(ran+78)
    key79 = Key.from_int(ran+79)
    key80 = Key.from_int(ran+80)
    key81 = Key.from_int(ran+81)
    key82 = Key.from_int(ran+82)
    key83 = Key.from_int(ran+83)
    key84 = Key.from_int(ran+84)
    key85 = Key.from_int(ran+85)
    key86 = Key.from_int(ran+86)
    key87 = Key.from_int(ran+87)
    key88 = Key.from_int(ran+88)
    key89 = Key.from_int(ran+89)
    key90 = Key.from_int(ran+90)
    key91 = Key.from_int(ran+91)
    key92 = Key.from_int(ran+92)
    key93 = Key.from_int(ran+93)
    key94 = Key.from_int(ran+94)
    key95 = Key.from_int(ran+95)
    key96 = Key.from_int(ran+96)
    key97 = Key.from_int(ran+97)
    key98 = Key.from_int(ran+98)
    key99 = Key.from_int(ran+99)
    key100 = Key.from_int(ran+100)
    key101 = Key.from_int(ran+101)
    key102 = Key.from_int(ran+102)
    key103 = Key.from_int(ran+103)
    key104 = Key.from_int(ran+104)
    key105 = Key.from_int(ran+105)
    key106 = Key.from_int(ran+106)
    key107 = Key.from_int(ran+107)
    key108 = Key.from_int(ran+108)
    key109 = Key.from_int(ran+109)
    key110 = Key.from_int(ran+110)
    key111 = Key.from_int(ran+111)
    key112 = Key.from_int(ran+112)
    key113 = Key.from_int(ran+113)
    key114 = Key.from_int(ran+114)
    key115 = Key.from_int(ran+115)
    key116 = Key.from_int(ran+116)
    key117 = Key.from_int(ran+117)
    key118 = Key.from_int(ran+118)
    key119 = Key.from_int(ran+119)
    key120 = Key.from_int(ran+120)
    key121 = Key.from_int(ran+121)
    key122 = Key.from_int(ran+122)
    key123 = Key.from_int(ran+123)
    key124 = Key.from_int(ran+124)
    key125 = Key.from_int(ran+125)
    key126 = Key.from_int(ran+126)
    key127 = Key.from_int(ran+127)

    caddr = key.address
    caddr1 = key1.address
    caddr2 = key2.address
    caddr3 = key3.address
    caddr4 = key4.address
    caddr5 = key5.address
    caddr6 = key6.address
    caddr7 = key7.address
    caddr8 = key8.address
    caddr9 = key9.address
    caddr10 = key10.address
    caddr11 = key11.address
    caddr12 = key12.address
    caddr13 = key13.address
    caddr14 = key14.address
    caddr15 = key15.address
    caddr16 = key16.address
    caddr17 = key17.address
    caddr18 = key18.address
    caddr19 = key19.address
    caddr20 = key20.address
    caddr21 = key21.address
    caddr22 = key22.address
    caddr23 = key23.address
    caddr24 = key24.address
    caddr25 = key25.address
    caddr26 = key26.address
    caddr27 = key27.address
    caddr28 = key28.address
    caddr29 = key29.address
    caddr30 = key30.address
    caddr31 = key31.address
    caddr32 = key32.address
    caddr33 = key33.address
    caddr34 = key34.address
    caddr35 = key35.address
    caddr36 = key36.address
    caddr37 = key37.address
    caddr38 = key38.address
    caddr39 = key39.address
    caddr40 = key40.address
    caddr41 = key41.address
    caddr42 = key42.address
    caddr43 = key43.address
    caddr44 = key44.address
    caddr45 = key45.address
    caddr46 = key46.address
    caddr47 = key47.address
    caddr48 = key48.address
    caddr49 = key49.address
    caddr50 = key50.address
    caddr51 = key51.address
    caddr52 = key52.address
    caddr53 = key53.address
    caddr54 = key54.address
    caddr55 = key55.address
    caddr56 = key56.address
    caddr57 = key57.address
    caddr58 = key58.address
    caddr59 = key59.address
    caddr60 = key60.address
    caddr61 = key61.address
    caddr62 = key62.address
    caddr63 = key63.address
    caddr64 = key64.address
    caddr65 = key65.address
    caddr66 = key66.address
    caddr67 = key67.address
    caddr68 = key68.address
    caddr69 = key69.address
    caddr70 = key70.address
    caddr71 = key71.address
    caddr72 = key72.address
    caddr73 = key73.address
    caddr74 = key74.address
    caddr75 = key75.address
    caddr76 = key76.address
    caddr77 = key77.address
    caddr78 = key78.address
    caddr79 = key79.address
    caddr80 = key80.address
    caddr81 = key81.address
    caddr82 = key82.address
    caddr83 = key83.address
    caddr84 = key84.address
    caddr85 = key85.address
    caddr86 = key86.address
    caddr87 = key87.address
    caddr88 = key88.address
    caddr89 = key89.address
    caddr90 = key90.address
    caddr91 = key91.address
    caddr92 = key92.address
    caddr93 = key93.address
    caddr94 = key94.address
    caddr95 = key95.address
    caddr96 = key96.address
    caddr97 = key97.address
    caddr98 = key98.address
    caddr99 = key99.address
    caddr100 = key100.address
    caddr101 = key101.address
    caddr102 = key102.address
    caddr103 = key103.address
    caddr104 = key104.address
    caddr105 = key105.address
    caddr106 = key106.address
    caddr107 = key107.address
    caddr108 = key108.address
    caddr109 = key109.address
    caddr110 = key110.address
    caddr111 = key111.address
    caddr112 = key112.address
    caddr113 = key113.address
    caddr114 = key114.address
    caddr115 = key115.address
    caddr116 = key116.address
    caddr117 = key117.address
    caddr118 = key118.address
    caddr119 = key119.address
    caddr120 = key120.address
    caddr121 = key121.address
    caddr122 = key122.address
    caddr123 = key123.address
    caddr124 = key124.address
    caddr125 = key125.address
    caddr126 = key126.address
    caddr127 = key127.address
    
    
    query=(caddr,caddr1,caddr2,caddr3,caddr4,caddr5,caddr6,caddr7,caddr8,caddr9,caddr10,caddr11,caddr12,caddr13,caddr14,caddr15,caddr16,caddr17,caddr18,caddr19,caddr20,caddr21,caddr22,caddr23,caddr24,caddr25,caddr26,caddr27,caddr28,caddr29,caddr30,caddr31,caddr32,caddr33,caddr34,caddr35,caddr36,caddr37,caddr38,caddr39,caddr40,caddr41,caddr42,caddr43,caddr44,caddr45,caddr46,caddr47,caddr48,caddr49,caddr50,caddr51,caddr52,caddr53,caddr54,caddr55,caddr56,caddr57,caddr58,caddr59,caddr60,caddr61,caddr62,caddr63,caddr64,caddr65,caddr66,caddr67,caddr68,caddr69,caddr70,caddr71,caddr72,caddr73,caddr74,caddr75,caddr76,caddr77,caddr78,caddr79,caddr80,caddr81,caddr82,caddr83,caddr84,caddr85,caddr86,caddr87,caddr88,caddr89,caddr90,caddr91,caddr92,caddr93,caddr94,caddr95,caddr96,caddr97,caddr98,caddr99,caddr100,caddr101,caddr102,caddr103,caddr104,caddr105,caddr106,caddr107,caddr108,caddr109,caddr110,caddr111,caddr112,caddr113,caddr114,caddr115,caddr116,caddr117,caddr118,caddr119,caddr120,caddr121,caddr122,caddr123,caddr124,caddr125,caddr126,caddr127)
    query1=(key.to_hex(),key1.to_hex(),key2.to_hex(),key3.to_hex(),key4.to_hex(),key5.to_hex(),key6.to_hex(),key7.to_hex(),key8.to_hex(),key9.to_hex(),key10.to_hex(),key11.to_hex(),key12.to_hex(),key13.to_hex(),key14.to_hex(),key15.to_hex(),key16.to_hex(),key17.to_hex(),key18.to_hex(),key19.to_hex(),key20.to_hex(),key21.to_hex(),key22.to_hex(),key23.to_hex(),key24.to_hex(),key25.to_hex(),key26.to_hex(),key27.to_hex(),key28.to_hex(),key29.to_hex(),key30.to_hex(),key31.to_hex(),key32.to_hex(),key33.to_hex(),key34.to_hex(),key35.to_hex(),key36.to_hex(),key37.to_hex(),key38.to_hex(),key39.to_hex(),key40.to_hex(),key41.to_hex(),key42.to_hex(),key43.to_hex(),key44.to_hex(),key45.to_hex(),key46.to_hex(),key47.to_hex(),key48.to_hex(),key49.to_hex(),key50.to_hex(),key51.to_hex(),key52.to_hex(),key53.to_hex(),key54.to_hex(),key55.to_hex(),key56.to_hex(),key57.to_hex(),key58.to_hex(),key59.to_hex(),key60.to_hex(),key61.to_hex(),key62.to_hex(),key63.to_hex(),key64.to_hex(),key65.to_hex(),key66.to_hex(),key67.to_hex(),key68.to_hex(),key69.to_hex(),key70.to_hex(),key71.to_hex(),key72.to_hex(),key73.to_hex(),key74.to_hex(),key75.to_hex(),key76.to_hex(),key77.to_hex(),key78.to_hex(),key79.to_hex(),key80.to_hex(),key81.to_hex(),key82.to_hex(),key83.to_hex(),key84.to_hex(),key85.to_hex(),key86.to_hex(),key87.to_hex(),key88.to_hex(),key89.to_hex(),key90.to_hex(),key91.to_hex(),key92.to_hex(),key93.to_hex(),key94.to_hex(),key95.to_hex(),key96.to_hex(),key97.to_hex(),key98.to_hex(),key99.to_hex(),key100.to_hex(),key101.to_hex(),key102.to_hex(),key103.to_hex(),key104.to_hex(),key105.to_hex(),key106.to_hex(),key107.to_hex(),key108.to_hex(),key109.to_hex(),key110.to_hex(),key111.to_hex(),key112.to_hex(),key113.to_hex(),key114.to_hex(),key115.to_hex(),key116.to_hex(),key117.to_hex(),key118.to_hex(),key119.to_hex(),key120.to_hex(),key121.to_hex(),key122.to_hex(),key123.to_hex(),key124.to_hex(),key125.to_hex(),key126.to_hex(),key127.to_hex())
    count+=1
    total+=128 
    pagenumber= int(seed)//128
    if len(query) == 128 or len(query1) == 128:
        try:
            request = requests.get("https://blockchain.info/multiaddr?active=%s" % ','.join(query),timeout=10)
            request = request.json()
            print(Fore.BLUE + "\nVIP_KEYS.py---" + Fore.RED + "Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD" + Fore.BLUE + "---VIP_KEYS.py"   + seconds_to_str())
            print(Fore.RED + '\nPrivateKey (hex) Last One in Scan : ' + Fore.YELLOW + key.to_hex() + Fore.RED + ' : PrivateKey (hex) Last One in Scan' + Style.RESET_ALL)
            print(Fore.RED + '\nPrivateKey (dec) Last One in Scan : ' + Fore.YELLOW + seed + Fore.RED + ' : PrivateKey (dec) Last One in Scan' + Style.RESET_ALL)
            print(Fore.RED + '\n  Any Winners found will be Within 128 Private Key range of this Scan '+ Style.RESET_ALL)
            print ('\n-- keys.py -- ' + Fore.GREEN +  'Running Scan : ' + str (count) + '  :  ' + Fore.BLUE + 'Total Bitcoin Addresses : ' + str (total) + ' : ' + Fore.YELLOW + seconds_to_str() + '] ----> '   + Style.RESET_ALL)
            for row in request["addresses"]:
                print(row)
                print(Fore.GREEN +  '<--------------------------------Page Number ' , Fore.YELLOW , pagenumber , Fore.GREEN , ' on Keys--------------------------------> '+ Style.RESET_ALL)
                if row["total_received"] > 0 or row["final_balance"] > 0: # final_balance or n_tx or total_received or total_sent
                    #print(str('\n'.join(query)))
                    #print(str('\n'.join(query1)))
                    print(Fore.GREEN +  '<--------------------------------Page Number ' , Fore.YELLOW , pagenumber , Fore.GREEN , ' on Keys--------------------------------> '+ Style.RESET_ALL)
                    print(Fore.GREEN + 'WINNER WINNER Ammount Found--------------------->  ' + Fore.YELLOW + str(row["total_sent"]) + Fore.GREEN + ' <---------------------WINNER WINNER' + Style.RESET_ALL)
                    print(Fore.BLUE + "\nVIP_KEYS.py---" + Fore.RED + "Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD" + Fore.BLUE + "---VIP_KEYS.py"   + seconds_to_str())
                    donate= 'WINNER WINNER Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD  THANK YOU \n Make sure to check all addresses in winner.txt 128 scanned WINNER WINNER     '
                    Addresses = [str('\n'.join(query))]
                    Privatehex = [str('\n'.join(query1))]
                    d = [Addresses, Privatehex]
                    export_data = zip_longest(*d, fillvalue = '')
                    with open('winner.txt', 'a') as myfile:
                          wr = csv.writer(myfile)
                          wr.writerow((donate + "Addresses", "Privatehex"))
                          wr.writerows(export_data)
                    myfile.close()
        except:
            pass

        # Reset counter
        query = []
        sleep(10) # Reduce Sleep to go faster
