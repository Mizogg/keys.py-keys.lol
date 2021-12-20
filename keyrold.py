# My Version of Random KEYS.LOL made my Mizogg https://mizogg.co.uk
from bit import *
from bit.format import bytes_to_wif
import random, codecs, sys, atexit, time, requests
from rich.console import Console
console = Console()
console.clear()
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

my_colours = [W, R, G, O, B, P]
icons= ['⏳', 'ℹ️', '✅', '⛔️', '🔁', '🔑', '💸', '😔', '🌍', '✍️', '🚌', '👇', '📋', '📣', '🤩','😀', '😃', '😄', '😁', '😆', '😅', '😂', '🤣', '🥲', '☺️', '😊', '😇', '🙂', '🙃', '😉', '😌', '😍', '🥰', '😘', '😗', '😙', '😚', '😋', '😛', '😝', '😜', '🤪', '🤨', '🧐', '🤓', '😎', '🥸', '🤩', '🥳', '😏', '😒', '😞', '😔', '😟', '😕', '🙁', '☹️', '😣', '😖', '😫', '😩', '🥺', '😢', '😭', '😤', '😠', '😡', '🤬', '🤯', '😳', '🥵', '🥶', '😱', '😨', '😰', '😥', '😓', '🤗', '🤔', '🤭', '🤫', '🤥', '😶', '😐', '😑', '😬', '🙄', '😯', '😦', '😧', '😮', '😲', '🥱', '😴', '🤤', '😪', '😵', '🤐', '🥴', '🤢', '🤮', '🤧', '😷', '🤒', '🤕', '🤑', '🤠', '😈', '👿', '👹', '👺', '🤡', '💩', '👻', '💀', '☠️', '👽', '👾', '🤖', '🎃', '😺', '😸', '😹', '😻', '😼', '😽', '🙀', '😿', '😾', '👋', '🤚', '🖐', '✋', '🖖', '👌', '🤌', '🤏', '✌️', '🤞', '🤟', '🤘', '🤙', '👈', '👉', '👆', '🖕', '👇', '☝️', '👍', '👎', '✊', '👊', '🤛', '🤜', '👏', '🙌', '👐', '🤲', '🤝', '🙏', '✍️', '💅', '🤳', '💪', '🦾', '🦵', '🦿', '🦶', '👣', '👂', '🦻', '👃', '🫀', '🫁', '🧠', '🦷', '🦴', '👀', '👁', '👅', '👄', '💋', '🩸', '🐒', '🐔', '🐧', '🐦', '🐤', '🐣', '🐥', '🦆', '🦅', '🦉', '🦇', '🐺', '🐗', '🐴', '🦄', '🐝', '🪱', '🐛', '🦋', '🐌', '🐞', '🐜', '🪰', '🪲', '🪳', '🦟', '🦗', '🕷', '🕸', '🦂', '🐢', '🐍', '🦎', '🦖', '🦕', '🐙', '🦑', '🦐', '🦞', '🦀', '🐡', '🐠', '🐟', '🐬', '🐳', '🐋', '🦈', '🐊', '🐅', '🐆', '🦓', '🦍', '🦧', '🦣', '🐘', '🦛', '🦏', '🐪', '🐫', '🦒', '🦘', '🦬', '🐃', '🐂', '🐄', '🐎', '🐖', '🐏', '🐑', '🦙', '🐐', '🦌', '🐕', '🐩', '🦮', '🐕‍🦺', '🐈', '🐈‍⬛', '🪶', '🐓', '🦃', '🦤', '🦚', '🦜', '🦢', '🦩', '🕊', '🐇', '🦝', '🦨', '🦡', '🦫', '🦦', '🦥', '🐁', '🐀', '🐿', '🦔', '🐾', '🐉', '🐲', '🌵', '🎄', '🌲', '🌳', '🌴', '🪵', '🌱', '🌿', '☘️', '🍀', '🎍', '🪴', '🎋', '🍃', '🍂', '🍁', '🍄', '🐚', '🪨', '🌾', '💐', '🌷', '🌹', '🥀', '🌺', '🌸', '🌼', '🌻', '🌞', '🌝', '🌛', '🌜', '🌚', '🌕', '🌖', '🌗', '🌘', '🌑', '🌒', '🌓', '🌔', '🌙', '🌎', '🌍', '🌏', '🪐', '💫', '⭐️', '🌟', '✨', '⚡️', '☄️', '💥', '🔥', '🌪', '🌈', '☀️', '🌤', '⛅️', '🌥', '☁️', '🌦', '🌧', '⛈', '🌩', '🌨', '❄️', '☃️', '⛄️', '🌬', '💨', '💧', '💦', '☔️', '☂️', '🌊', '🌫', '⏰', '💰', '🎅🏻', '🎄', '🎁', '🎶']

animation = ["□□□□□□□□□□□□□□□□□□□□  0%","■□□□□□□□□□□□□□□□□□□□  5%","■■□□□□□□□□□□□□□□□□□□ 10%","■■■□□□□□□□□□□□□□□□□□ 15%","■■■■□□□□□□□□□□□□□□□□ 20%","■■■■■□□□□□□□□□□□□□□□ 25%","■■■■■■□□□□□□□□□□□□□□ 30%","■■■■■■■□□□□□□□□□□□□□ 35%","■■■■■■■■□□□□□□□□□□□□ 40%","■■■■■■■■■□□□□□□□□□□□ 45%","■■■■■■■■■■□□□□□□□□□□ 50%","■■■■■■■■■■■□□□□□□□□□ 55%","■■■■■■■■■■■■□□□□□□□□ 60%","■■■■■■■■■■■■■□□□□□□□ 65%","■■■■■■■■■■■■■■□□□□□□ 70%","■■■■■■■■■■■■■■■□□□□□ 75%","■■■■■■■■■■■■■■■■□□□□ 80%","■■■■■■■■■■■■■■■■■□□□ 85%","■■■■■■■■■■■■■■■■■■□□ 90%","■■■■■■■■■■■■■■■■■■■□ 95%","■■■■■■■■■■■■■■■■■■■■100%"]

#animation = ["□□□□□□□□□□□□□□□□□□□□  0%","🔑□□□□□□□□□□□□□□□□□□□  5%","🔑🔑□□□□□□□□□□□□□□□□□□ 10%","🔑🔑🔑□□□□□□□□□□□□□□□□□ 15%","🔑🔑🔑🔑□□□□□□□□□□□□□□□□ 20%","🔑🔑🔑🔑🔑□□□□□□□□□□□□□□□ 25%","🔑🔑🔑🔑🔑🔑□□□□□□□□□□□□□□ 30%","🔑🔑🔑🔑🔑🔑🔑□□□□□□□□□□□□□ 35%","🔑🔑🔑🔑🔑🔑🔑🔑□□□□□□□□□□□□ 40%","🔑🔑🔑🔑🔑🔑🔑🔑🔑□□□□□□□□□□□ 45%","🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑□□□□□□□□□□ 50%","🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑□□□□□□□□□ 55%","🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑□□□□□□□□ 60%","🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑□□□□□□□ 65%","🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑□□□□□□ 70%","🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑□□□□□ 75%","🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑□□□□ 80%","🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑□□□ 85%","🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑□□ 90%","🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑□ 95%","🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑100%"]
   
console.print(" [yellow]-----------------KEYS.LOL----------------------[/yellow]")
console.print("[yellow]                 Starting search...[/yellow]")
console.print("[yellow]                Using Block Chain API...[/yellow]")
console.print(" [yellow]-----------------KEYS.LOL----------------------[/yellow]")
console.print("[yellow] ℹ️ Start search... Pick Range to start (Min=0 Max=256) ℹ️ [/yellow] ")
x=int(input(" ✅ Start range in BITs (Puzzle StartNumber) ✍️ -> "))
a = 2**x
y=int(input(" ⛔️ Stop range Max in BITs (Puzzle StopNumber)✍️ -> "))
b = 2**y
console.print("[purple]⏳Starting search... Please Wait ⏳[/purple]")
console.print("==========================================================")

query = []

counter=0
total=0
pagenumber=0


while True:
    lol= random.choice(icons)
    colour = random.choice(my_colours)
    ran = random.randrange(a,b)
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
    
    wifu = bytes_to_wif(key.to_bytes(), compressed=False) # Uncompressed WIF
    wifc = bytes_to_wif(key.to_bytes(), compressed=True) # Compressed WIF
    keyu = Key(wifu)
    wifu1 = bytes_to_wif(key1.to_bytes(), compressed=False) # Uncompressed WIF
    wifc1 = bytes_to_wif(key1.to_bytes(), compressed=True) # Compressed WIF
    keyu1 = Key(wifu1)
    wifu2 = bytes_to_wif(key2.to_bytes(), compressed=False) # Uncompressed WIF
    wifc2 = bytes_to_wif(key2.to_bytes(), compressed=True) # Compressed WIF
    keyu2 = Key(wifu2)
    wifu3 = bytes_to_wif(key3.to_bytes(), compressed=False) # Uncompressed WIF
    wifc3 = bytes_to_wif(key3.to_bytes(), compressed=True) # Compressed WIF
    keyu3 = Key(wifu3)
    wifu4 = bytes_to_wif(key4.to_bytes(), compressed=False) # Uncompressed WIF
    wifc4 = bytes_to_wif(key4.to_bytes(), compressed=True) # Compressed WIF
    keyu4 = Key(wifu4)
    wifu5 = bytes_to_wif(key5.to_bytes(), compressed=False) # Uncompressed WIF
    wifc5 = bytes_to_wif(key5.to_bytes(), compressed=True) # Compressed WIF
    keyu5 = Key(wifu5)
    wifu6 = bytes_to_wif(key6.to_bytes(), compressed=False) # Uncompressed WIF
    wifc6 = bytes_to_wif(key6.to_bytes(), compressed=True) # Compressed WIF
    keyu6 = Key(wifu6)
    wifu7 = bytes_to_wif(key7.to_bytes(), compressed=False) # Uncompressed WIF
    wifc7 = bytes_to_wif(key7.to_bytes(), compressed=True) # Compressed WIF
    keyu7 = Key(wifu7)
    wifu8 = bytes_to_wif(key8.to_bytes(), compressed=False) # Uncompressed WIF
    wifc8 = bytes_to_wif(key8.to_bytes(), compressed=True) # Compressed WIF
    keyu8 = Key(wifu8)
    wifu9 = bytes_to_wif(key9.to_bytes(), compressed=False) # Uncompressed WIF
    wifc9 = bytes_to_wif(key9.to_bytes(), compressed=True) # Compressed WIF
    keyu9 = Key(wifu9)
    wifu10 = bytes_to_wif(key10.to_bytes(), compressed=False) # Uncompressed WIF
    wifc10 = bytes_to_wif(key10.to_bytes(), compressed=True) # Compressed WIF
    keyu10 = Key(wifu10)
    wifu11 = bytes_to_wif(key11.to_bytes(), compressed=False) # Uncompressed WIF
    wifc11 = bytes_to_wif(key11.to_bytes(), compressed=True) # Compressed WIF
    keyu11 = Key(wifu11)
    wifu12 = bytes_to_wif(key12.to_bytes(), compressed=False) # Uncompressed WIF
    wifc12 = bytes_to_wif(key12.to_bytes(), compressed=True) # Compressed WIF
    keyu12 = Key(wifu12)
    wifu13 = bytes_to_wif(key13.to_bytes(), compressed=False) # Uncompressed WIF
    wifc13 = bytes_to_wif(key13.to_bytes(), compressed=True) # Compressed WIF
    keyu13 = Key(wifu13)
    wifu14 = bytes_to_wif(key14.to_bytes(), compressed=False) # Uncompressed WIF
    wifc14 = bytes_to_wif(key14.to_bytes(), compressed=True) # Compressed WIF
    keyu14 = Key(wifu14)
    wifu15 = bytes_to_wif(key15.to_bytes(), compressed=False) # Uncompressed WIF
    wifc15 = bytes_to_wif(key15.to_bytes(), compressed=True) # Compressed WIF
    keyu15 = Key(wifu15)
    wifu16 = bytes_to_wif(key16.to_bytes(), compressed=False) # Uncompressed WIF
    wifc16 = bytes_to_wif(key16.to_bytes(), compressed=True) # Compressed WIF
    keyu16 = Key(wifu16)
    wifu17 = bytes_to_wif(key17.to_bytes(), compressed=False) # Uncompressed WIF
    wifc17 = bytes_to_wif(key17.to_bytes(), compressed=True) # Compressed WIF
    keyu17 = Key(wifu17)
    wifu18 = bytes_to_wif(key18.to_bytes(), compressed=False) # Uncompressed WIF
    wifc18 = bytes_to_wif(key18.to_bytes(), compressed=True) # Compressed WIF
    keyu18 = Key(wifu18)
    wifu19 = bytes_to_wif(key19.to_bytes(), compressed=False) # Uncompressed WIF
    wifc19 = bytes_to_wif(key19.to_bytes(), compressed=True) # Compressed WIF
    keyu19 = Key(wifu19)
    wifu20 = bytes_to_wif(key20.to_bytes(), compressed=False) # Uncompressed WIF
    wifc20 = bytes_to_wif(key20.to_bytes(), compressed=True) # Compressed WIF
    keyu20 = Key(wifu20)
    wifu21 = bytes_to_wif(key21.to_bytes(), compressed=False) # Uncompressed WIF
    wifc21 = bytes_to_wif(key21.to_bytes(), compressed=True) # Compressed WIF
    keyu21 = Key(wifu21)
    wifu22 = bytes_to_wif(key22.to_bytes(), compressed=False) # Uncompressed WIF
    wifc22 = bytes_to_wif(key22.to_bytes(), compressed=True) # Compressed WIF
    keyu22 = Key(wifu22)
    wifu23 = bytes_to_wif(key23.to_bytes(), compressed=False) # Uncompressed WIF
    wifc23 = bytes_to_wif(key23.to_bytes(), compressed=True) # Compressed WIF
    keyu23 = Key(wifu23)
    wifu24 = bytes_to_wif(key24.to_bytes(), compressed=False) # Uncompressed WIF
    wifc24 = bytes_to_wif(key24.to_bytes(), compressed=True) # Compressed WIF
    keyu24 = Key(wifu24)
    wifu25 = bytes_to_wif(key25.to_bytes(), compressed=False) # Uncompressed WIF
    wifc25 = bytes_to_wif(key25.to_bytes(), compressed=True) # Compressed WIF
    keyu25 = Key(wifu25)
    wifu26 = bytes_to_wif(key26.to_bytes(), compressed=False) # Uncompressed WIF
    wifc26 = bytes_to_wif(key26.to_bytes(), compressed=True) # Compressed WIF
    keyu26 = Key(wifu26)
    wifu27 = bytes_to_wif(key27.to_bytes(), compressed=False) # Uncompressed WIF
    wifc27 = bytes_to_wif(key27.to_bytes(), compressed=True) # Compressed WIF
    keyu27 = Key(wifu27)
    wifu28 = bytes_to_wif(key28.to_bytes(), compressed=False) # Uncompressed WIF
    wifc28 = bytes_to_wif(key28.to_bytes(), compressed=True) # Compressed WIF
    keyu28 = Key(wifu28)
    wifu29 = bytes_to_wif(key29.to_bytes(), compressed=False) # Uncompressed WIF
    wifc29 = bytes_to_wif(key29.to_bytes(), compressed=True) # Compressed WIF
    keyu29 = Key(wifu29)
    wifu30 = bytes_to_wif(key30.to_bytes(), compressed=False) # Uncompressed WIF
    wifc30 = bytes_to_wif(key30.to_bytes(), compressed=True) # Compressed WIF
    keyu30 = Key(wifu30)
    wifu31 = bytes_to_wif(key31.to_bytes(), compressed=False) # Uncompressed WIF
    wifc31 = bytes_to_wif(key31.to_bytes(), compressed=True) # Compressed WIF
    keyu31 = Key(wifu31)
    wifu32 = bytes_to_wif(key32.to_bytes(), compressed=False) # Uncompressed WIF
    wifc32 = bytes_to_wif(key32.to_bytes(), compressed=True) # Compressed WIF
    keyu32 = Key(wifu32)
    wifu33 = bytes_to_wif(key33.to_bytes(), compressed=False) # Uncompressed WIF
    wifc33 = bytes_to_wif(key33.to_bytes(), compressed=True) # Compressed WIF
    keyu33 = Key(wifu33)
    wifu34 = bytes_to_wif(key34.to_bytes(), compressed=False) # Uncompressed WIF
    wifc34 = bytes_to_wif(key34.to_bytes(), compressed=True) # Compressed WIF
    keyu34 = Key(wifu34)
    wifu35 = bytes_to_wif(key35.to_bytes(), compressed=False) # Uncompressed WIF
    wifc35 = bytes_to_wif(key35.to_bytes(), compressed=True) # Compressed WIF
    keyu35 = Key(wifu35)
    wifu36 = bytes_to_wif(key36.to_bytes(), compressed=False) # Uncompressed WIF
    wifc36 = bytes_to_wif(key36.to_bytes(), compressed=True) # Compressed WIF
    keyu36 = Key(wifu36)
    wifu37 = bytes_to_wif(key37.to_bytes(), compressed=False) # Uncompressed WIF
    wifc37 = bytes_to_wif(key37.to_bytes(), compressed=True) # Compressed WIF
    keyu37 = Key(wifu37)
    wifu38 = bytes_to_wif(key38.to_bytes(), compressed=False) # Uncompressed WIF
    wifc38 = bytes_to_wif(key38.to_bytes(), compressed=True) # Compressed WIF
    keyu38 = Key(wifu38)
    wifu39 = bytes_to_wif(key39.to_bytes(), compressed=False) # Uncompressed WIF
    wifc39 = bytes_to_wif(key39.to_bytes(), compressed=True) # Compressed WIF
    keyu39 = Key(wifu39)
    wifu40 = bytes_to_wif(key40.to_bytes(), compressed=False) # Uncompressed WIF
    wifc40 = bytes_to_wif(key40.to_bytes(), compressed=True) # Compressed WIF
    keyu40 = Key(wifu40)
    wifu41 = bytes_to_wif(key41.to_bytes(), compressed=False) # Uncompressed WIF
    wifc41 = bytes_to_wif(key41.to_bytes(), compressed=True) # Compressed WIF
    keyu41 = Key(wifu41)
    wifu42 = bytes_to_wif(key42.to_bytes(), compressed=False) # Uncompressed WIF
    wifc42 = bytes_to_wif(key42.to_bytes(), compressed=True) # Compressed WIF
    keyu42 = Key(wifu42)
    wifu43 = bytes_to_wif(key43.to_bytes(), compressed=False) # Uncompressed WIF
    wifc43 = bytes_to_wif(key43.to_bytes(), compressed=True) # Compressed WIF
    keyu43 = Key(wifu43)
    wifu44 = bytes_to_wif(key44.to_bytes(), compressed=False) # Uncompressed WIF
    wifc44 = bytes_to_wif(key44.to_bytes(), compressed=True) # Compressed WIF
    keyu44 = Key(wifu44)
    wifu45 = bytes_to_wif(key45.to_bytes(), compressed=False) # Uncompressed WIF
    wifc45 = bytes_to_wif(key45.to_bytes(), compressed=True) # Compressed WIF
    keyu45 = Key(wifu45)
    wifu46 = bytes_to_wif(key46.to_bytes(), compressed=False) # Uncompressed WIF
    wifc46 = bytes_to_wif(key46.to_bytes(), compressed=True) # Compressed WIF
    keyu46 = Key(wifu46)
    wifu47 = bytes_to_wif(key47.to_bytes(), compressed=False) # Uncompressed WIF
    wifc47 = bytes_to_wif(key47.to_bytes(), compressed=True) # Compressed WIF
    keyu47 = Key(wifu47)
    wifu48 = bytes_to_wif(key48.to_bytes(), compressed=False) # Uncompressed WIF
    wifc48 = bytes_to_wif(key48.to_bytes(), compressed=True) # Compressed WIF
    keyu48 = Key(wifu48)
    wifu49 = bytes_to_wif(key49.to_bytes(), compressed=False) # Uncompressed WIF
    wifc49 = bytes_to_wif(key49.to_bytes(), compressed=True) # Compressed WIF
    keyu49 = Key(wifu49)
    wifu50 = bytes_to_wif(key50.to_bytes(), compressed=False) # Uncompressed WIF
    wifc50 = bytes_to_wif(key50.to_bytes(), compressed=True) # Compressed WIF
    keyu50 = Key(wifu50)
    wifu51 = bytes_to_wif(key51.to_bytes(), compressed=False) # Uncompressed WIF
    wifc51 = bytes_to_wif(key51.to_bytes(), compressed=True) # Compressed WIF
    keyu51 = Key(wifu51)
    wifu52 = bytes_to_wif(key52.to_bytes(), compressed=False) # Uncompressed WIF
    wifc52 = bytes_to_wif(key52.to_bytes(), compressed=True) # Compressed WIF
    keyu52 = Key(wifu52)
    wifu53 = bytes_to_wif(key53.to_bytes(), compressed=False) # Uncompressed WIF
    wifc53 = bytes_to_wif(key53.to_bytes(), compressed=True) # Compressed WIF
    keyu53 = Key(wifu53)
    wifu54 = bytes_to_wif(key54.to_bytes(), compressed=False) # Uncompressed WIF
    wifc54 = bytes_to_wif(key54.to_bytes(), compressed=True) # Compressed WIF
    keyu54 = Key(wifu54)
    wifu55 = bytes_to_wif(key55.to_bytes(), compressed=False) # Uncompressed WIF
    wifc55 = bytes_to_wif(key55.to_bytes(), compressed=True) # Compressed WIF
    keyu55 = Key(wifu55)
    wifu56 = bytes_to_wif(key56.to_bytes(), compressed=False) # Uncompressed WIF
    wifc56 = bytes_to_wif(key56.to_bytes(), compressed=True) # Compressed WIF
    keyu56 = Key(wifu56)
    wifu57 = bytes_to_wif(key57.to_bytes(), compressed=False) # Uncompressed WIF
    wifc57 = bytes_to_wif(key57.to_bytes(), compressed=True) # Compressed WIF
    keyu57 = Key(wifu57)
    wifu58 = bytes_to_wif(key58.to_bytes(), compressed=False) # Uncompressed WIF
    wifc58 = bytes_to_wif(key58.to_bytes(), compressed=True) # Compressed WIF
    keyu58 = Key(wifu58)
    wifu59 = bytes_to_wif(key59.to_bytes(), compressed=False) # Uncompressed WIF
    wifc59 = bytes_to_wif(key59.to_bytes(), compressed=True) # Compressed WIF
    keyu59 = Key(wifu59)
    wifu60 = bytes_to_wif(key60.to_bytes(), compressed=False) # Uncompressed WIF
    wifc60 = bytes_to_wif(key60.to_bytes(), compressed=True) # Compressed WIF
    keyu60 = Key(wifu60)
    wifu61 = bytes_to_wif(key61.to_bytes(), compressed=False) # Uncompressed WIF
    wifc61 = bytes_to_wif(key61.to_bytes(), compressed=True) # Compressed WIF
    keyu61 = Key(wifu61)
    wifu62 = bytes_to_wif(key62.to_bytes(), compressed=False) # Uncompressed WIF
    wifc62 = bytes_to_wif(key62.to_bytes(), compressed=True) # Compressed WIF
    keyu62 = Key(wifu62)
    wifu63 = bytes_to_wif(key63.to_bytes(), compressed=False) # Uncompressed WIF
    wifc63 = bytes_to_wif(key63.to_bytes(), compressed=True) # Compressed WIF
    keyu63 = Key(wifu63)
    wifu64 = bytes_to_wif(key64.to_bytes(), compressed=False) # Uncompressed WIF
    wifc64 = bytes_to_wif(key64.to_bytes(), compressed=True) # Compressed WIF
    keyu64 = Key(wifu64)
    wifu65 = bytes_to_wif(key65.to_bytes(), compressed=False) # Uncompressed WIF
    wifc65 = bytes_to_wif(key65.to_bytes(), compressed=True) # Compressed WIF
    keyu65 = Key(wifu65)
    wifu66 = bytes_to_wif(key66.to_bytes(), compressed=False) # Uncompressed WIF
    wifc66 = bytes_to_wif(key66.to_bytes(), compressed=True) # Compressed WIF
    keyu66 = Key(wifu66)
    wifu67 = bytes_to_wif(key67.to_bytes(), compressed=False) # Uncompressed WIF
    wifc67 = bytes_to_wif(key67.to_bytes(), compressed=True) # Compressed WIF
    keyu67 = Key(wifu67)
    wifu68 = bytes_to_wif(key68.to_bytes(), compressed=False) # Uncompressed WIF
    wifc68 = bytes_to_wif(key68.to_bytes(), compressed=True) # Compressed WIF
    keyu68 = Key(wifu68)
    wifu69 = bytes_to_wif(key69.to_bytes(), compressed=False) # Uncompressed WIF
    wifc69 = bytes_to_wif(key69.to_bytes(), compressed=True) # Compressed WIF
    keyu69 = Key(wifu69)
    wifu70 = bytes_to_wif(key70.to_bytes(), compressed=False) # Uncompressed WIF
    wifc70 = bytes_to_wif(key70.to_bytes(), compressed=True) # Compressed WIF
    keyu70 = Key(wifu70)
    wifu71 = bytes_to_wif(key71.to_bytes(), compressed=False) # Uncompressed WIF
    wifc71 = bytes_to_wif(key71.to_bytes(), compressed=True) # Compressed WIF
    keyu71 = Key(wifu71)
    wifu72 = bytes_to_wif(key72.to_bytes(), compressed=False) # Uncompressed WIF
    wifc72 = bytes_to_wif(key72.to_bytes(), compressed=True) # Compressed WIF
    keyu72 = Key(wifu72)
    wifu73 = bytes_to_wif(key73.to_bytes(), compressed=False) # Uncompressed WIF
    wifc73 = bytes_to_wif(key73.to_bytes(), compressed=True) # Compressed WIF
    keyu73 = Key(wifu73)
    wifu74 = bytes_to_wif(key74.to_bytes(), compressed=False) # Uncompressed WIF
    wifc74 = bytes_to_wif(key74.to_bytes(), compressed=True) # Compressed WIF
    keyu74 = Key(wifu74)
    wifu75 = bytes_to_wif(key75.to_bytes(), compressed=False) # Uncompressed WIF
    wifc75 = bytes_to_wif(key75.to_bytes(), compressed=True) # Compressed WIF
    keyu75 = Key(wifu75)
    wifu76 = bytes_to_wif(key76.to_bytes(), compressed=False) # Uncompressed WIF
    wifc76 = bytes_to_wif(key76.to_bytes(), compressed=True) # Compressed WIF
    keyu76 = Key(wifu76)
    wifu77 = bytes_to_wif(key77.to_bytes(), compressed=False) # Uncompressed WIF
    wifc77 = bytes_to_wif(key77.to_bytes(), compressed=True) # Compressed WIF
    keyu77 = Key(wifu77)
    wifu78 = bytes_to_wif(key78.to_bytes(), compressed=False) # Uncompressed WIF
    wifc78 = bytes_to_wif(key78.to_bytes(), compressed=True) # Compressed WIF
    keyu78 = Key(wifu78)
    wifu79 = bytes_to_wif(key79.to_bytes(), compressed=False) # Uncompressed WIF
    wifc79 = bytes_to_wif(key79.to_bytes(), compressed=True) # Compressed WIF
    keyu79 = Key(wifu79)
    wifu80 = bytes_to_wif(key80.to_bytes(), compressed=False) # Uncompressed WIF
    wifc80 = bytes_to_wif(key80.to_bytes(), compressed=True) # Compressed WIF
    keyu80 = Key(wifu80)
    wifu81 = bytes_to_wif(key81.to_bytes(), compressed=False) # Uncompressed WIF
    wifc81 = bytes_to_wif(key81.to_bytes(), compressed=True) # Compressed WIF
    keyu81 = Key(wifu81)
    wifu82 = bytes_to_wif(key82.to_bytes(), compressed=False) # Uncompressed WIF
    wifc82 = bytes_to_wif(key82.to_bytes(), compressed=True) # Compressed WIF
    keyu82 = Key(wifu82)
    wifu83 = bytes_to_wif(key83.to_bytes(), compressed=False) # Uncompressed WIF
    wifc83 = bytes_to_wif(key83.to_bytes(), compressed=True) # Compressed WIF
    keyu83 = Key(wifu83)
    wifu84 = bytes_to_wif(key84.to_bytes(), compressed=False) # Uncompressed WIF
    wifc84 = bytes_to_wif(key84.to_bytes(), compressed=True) # Compressed WIF
    keyu84 = Key(wifu84)
    wifu85 = bytes_to_wif(key85.to_bytes(), compressed=False) # Uncompressed WIF
    wifc85 = bytes_to_wif(key85.to_bytes(), compressed=True) # Compressed WIF
    keyu85 = Key(wifu85)
    wifu86 = bytes_to_wif(key86.to_bytes(), compressed=False) # Uncompressed WIF
    wifc86 = bytes_to_wif(key86.to_bytes(), compressed=True) # Compressed WIF
    keyu86 = Key(wifu86)
    wifu87 = bytes_to_wif(key87.to_bytes(), compressed=False) # Uncompressed WIF
    wifc87 = bytes_to_wif(key87.to_bytes(), compressed=True) # Compressed WIF
    keyu87 = Key(wifu87)
    wifu88 = bytes_to_wif(key88.to_bytes(), compressed=False) # Uncompressed WIF
    wifc88 = bytes_to_wif(key88.to_bytes(), compressed=True) # Compressed WIF
    keyu88 = Key(wifu88)
    wifu89 = bytes_to_wif(key89.to_bytes(), compressed=False) # Uncompressed WIF
    wifc89 = bytes_to_wif(key89.to_bytes(), compressed=True) # Compressed WIF
    keyu89 = Key(wifu89)
    wifu90 = bytes_to_wif(key90.to_bytes(), compressed=False) # Uncompressed WIF
    wifc90 = bytes_to_wif(key90.to_bytes(), compressed=True) # Compressed WIF
    keyu90 = Key(wifu90)
    wifu91 = bytes_to_wif(key91.to_bytes(), compressed=False) # Uncompressed WIF
    wifc91 = bytes_to_wif(key91.to_bytes(), compressed=True) # Compressed WIF
    keyu91 = Key(wifu91)
    wifu92 = bytes_to_wif(key92.to_bytes(), compressed=False) # Uncompressed WIF
    wifc92 = bytes_to_wif(key92.to_bytes(), compressed=True) # Compressed WIF
    keyu92 = Key(wifu92)
    wifu93 = bytes_to_wif(key93.to_bytes(), compressed=False) # Uncompressed WIF
    wifc93 = bytes_to_wif(key93.to_bytes(), compressed=True) # Compressed WIF
    keyu93 = Key(wifu93)
    wifu94 = bytes_to_wif(key94.to_bytes(), compressed=False) # Uncompressed WIF
    wifc94 = bytes_to_wif(key94.to_bytes(), compressed=True) # Compressed WIF
    keyu94 = Key(wifu94)
    wifu95 = bytes_to_wif(key95.to_bytes(), compressed=False) # Uncompressed WIF
    wifc95 = bytes_to_wif(key95.to_bytes(), compressed=True) # Compressed WIF
    keyu95 = Key(wifu95)
    wifu96 = bytes_to_wif(key96.to_bytes(), compressed=False) # Uncompressed WIF
    wifc96 = bytes_to_wif(key96.to_bytes(), compressed=True) # Compressed WIF
    keyu96 = Key(wifu96)
    wifu97 = bytes_to_wif(key97.to_bytes(), compressed=False) # Uncompressed WIF
    wifc97 = bytes_to_wif(key97.to_bytes(), compressed=True) # Compressed WIF
    keyu97 = Key(wifu97)
    wifu98 = bytes_to_wif(key98.to_bytes(), compressed=False) # Uncompressed WIF
    wifc98 = bytes_to_wif(key98.to_bytes(), compressed=True) # Compressed WIF
    keyu98 = Key(wifu98)
    wifu99 = bytes_to_wif(key99.to_bytes(), compressed=False) # Uncompressed WIF
    wifc99 = bytes_to_wif(key99.to_bytes(), compressed=True) # Compressed WIF
    keyu99 = Key(wifu99)
    wifu100 = bytes_to_wif(key100.to_bytes(), compressed=False) # Uncompressed WIF
    wifc100 = bytes_to_wif(key100.to_bytes(), compressed=True) # Compressed WIF
    keyu100 = Key(wifu100)
    wifu101 = bytes_to_wif(key101.to_bytes(), compressed=False) # Uncompressed WIF
    wifc101 = bytes_to_wif(key101.to_bytes(), compressed=True) # Compressed WIF
    keyu101 = Key(wifu101)
    wifu102 = bytes_to_wif(key102.to_bytes(), compressed=False) # Uncompressed WIF
    wifc102 = bytes_to_wif(key102.to_bytes(), compressed=True) # Compressed WIF
    keyu102 = Key(wifu102)
    wifu103 = bytes_to_wif(key103.to_bytes(), compressed=False) # Uncompressed WIF
    wifc103 = bytes_to_wif(key103.to_bytes(), compressed=True) # Compressed WIF
    keyu103 = Key(wifu103)
    wifu104 = bytes_to_wif(key104.to_bytes(), compressed=False) # Uncompressed WIF
    wifc104 = bytes_to_wif(key104.to_bytes(), compressed=True) # Compressed WIF
    keyu104 = Key(wifu104)
    wifu105 = bytes_to_wif(key105.to_bytes(), compressed=False) # Uncompressed WIF
    wifc105 = bytes_to_wif(key105.to_bytes(), compressed=True) # Compressed WIF
    keyu105 = Key(wifu105)
    wifu106 = bytes_to_wif(key106.to_bytes(), compressed=False) # Uncompressed WIF
    wifc106 = bytes_to_wif(key106.to_bytes(), compressed=True) # Compressed WIF
    keyu106 = Key(wifu106)
    wifu107 = bytes_to_wif(key107.to_bytes(), compressed=False) # Uncompressed WIF
    wifc107 = bytes_to_wif(key107.to_bytes(), compressed=True) # Compressed WIF
    keyu107 = Key(wifu107)
    wifu108 = bytes_to_wif(key108.to_bytes(), compressed=False) # Uncompressed WIF
    wifc108 = bytes_to_wif(key108.to_bytes(), compressed=True) # Compressed WIF
    keyu108 = Key(wifu108)
    wifu109 = bytes_to_wif(key109.to_bytes(), compressed=False) # Uncompressed WIF
    wifc109 = bytes_to_wif(key109.to_bytes(), compressed=True) # Compressed WIF
    keyu109 = Key(wifu109)
    wifu110 = bytes_to_wif(key110.to_bytes(), compressed=False) # Uncompressed WIF
    wifc110 = bytes_to_wif(key110.to_bytes(), compressed=True) # Compressed WIF
    keyu110 = Key(wifu110)
    wifu111 = bytes_to_wif(key111.to_bytes(), compressed=False) # Uncompressed WIF
    wifc111 = bytes_to_wif(key111.to_bytes(), compressed=True) # Compressed WIF
    keyu111 = Key(wifu111)
    wifu112 = bytes_to_wif(key112.to_bytes(), compressed=False) # Uncompressed WIF
    wifc112 = bytes_to_wif(key112.to_bytes(), compressed=True) # Compressed WIF
    keyu112 = Key(wifu112)
    wifu113 = bytes_to_wif(key113.to_bytes(), compressed=False) # Uncompressed WIF
    wifc113 = bytes_to_wif(key113.to_bytes(), compressed=True) # Compressed WIF
    keyu113 = Key(wifu113)
    wifu114 = bytes_to_wif(key114.to_bytes(), compressed=False) # Uncompressed WIF
    wifc114 = bytes_to_wif(key114.to_bytes(), compressed=True) # Compressed WIF
    keyu114 = Key(wifu114)
    wifu115 = bytes_to_wif(key115.to_bytes(), compressed=False) # Uncompressed WIF
    wifc115 = bytes_to_wif(key115.to_bytes(), compressed=True) # Compressed WIF
    keyu115 = Key(wifu115)
    wifu116 = bytes_to_wif(key116.to_bytes(), compressed=False) # Uncompressed WIF
    wifc116 = bytes_to_wif(key116.to_bytes(), compressed=True) # Compressed WIF
    keyu116 = Key(wifu116)
    wifu117 = bytes_to_wif(key117.to_bytes(), compressed=False) # Uncompressed WIF
    wifc117 = bytes_to_wif(key117.to_bytes(), compressed=True) # Compressed WIF
    keyu117 = Key(wifu117)
    wifu118 = bytes_to_wif(key118.to_bytes(), compressed=False) # Uncompressed WIF
    wifc118 = bytes_to_wif(key118.to_bytes(), compressed=True) # Compressed WIF
    keyu118 = Key(wifu118)
    wifu119 = bytes_to_wif(key119.to_bytes(), compressed=False) # Uncompressed WIF
    wifc119 = bytes_to_wif(key119.to_bytes(), compressed=True) # Compressed WIF
    keyu119 = Key(wifu119)
    wifu120 = bytes_to_wif(key120.to_bytes(), compressed=False) # Uncompressed WIF
    wifc120 = bytes_to_wif(key120.to_bytes(), compressed=True) # Compressed WIF
    keyu120 = Key(wifu120)
    wifu121 = bytes_to_wif(key121.to_bytes(), compressed=False) # Uncompressed WIF
    wifc121 = bytes_to_wif(key121.to_bytes(), compressed=True) # Compressed WIF
    keyu121 = Key(wifu121)
    wifu122 = bytes_to_wif(key122.to_bytes(), compressed=False) # Uncompressed WIF
    wifc122 = bytes_to_wif(key122.to_bytes(), compressed=True) # Compressed WIF
    keyu122 = Key(wifu122)
    wifu123 = bytes_to_wif(key123.to_bytes(), compressed=False) # Uncompressed WIF
    wifc123 = bytes_to_wif(key123.to_bytes(), compressed=True) # Compressed WIF
    keyu123 = Key(wifu123)
    wifu124 = bytes_to_wif(key124.to_bytes(), compressed=False) # Uncompressed WIF
    wifc124 = bytes_to_wif(key124.to_bytes(), compressed=True) # Compressed WIF
    keyu124 = Key(wifu124)
    wifu125 = bytes_to_wif(key125.to_bytes(), compressed=False) # Uncompressed WIF
    wifc125 = bytes_to_wif(key125.to_bytes(), compressed=True) # Compressed WIF
    keyu125 = Key(wifu125)
    wifu126 = bytes_to_wif(key126.to_bytes(), compressed=False) # Uncompressed WIF
    wifc126 = bytes_to_wif(key126.to_bytes(), compressed=True) # Compressed WIF
    keyu126 = Key(wifu126)
    wifu127 = bytes_to_wif(key127.to_bytes(), compressed=False) # Uncompressed WIF
    wifc127 = bytes_to_wif(key127.to_bytes(), compressed=True) # Compressed WIF
    keyu127 = Key(wifu127)
    

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
    
    uaddr = keyu.address
    uaddr1 = keyu1.address
    uaddr2 = keyu2.address
    uaddr3 = keyu3.address
    uaddr4 = keyu4.address
    uaddr5 = keyu5.address
    uaddr6 = keyu6.address
    uaddr7 = keyu7.address
    uaddr8 = keyu8.address
    uaddr9 = keyu9.address
    uaddr10 = keyu10.address
    uaddr11 = keyu11.address
    uaddr12 = keyu12.address
    uaddr13 = keyu13.address
    uaddr14 = keyu14.address
    uaddr15 = keyu15.address
    uaddr16 = keyu16.address
    uaddr17 = keyu17.address
    uaddr18 = keyu18.address
    uaddr19 = keyu19.address
    uaddr20 = keyu20.address
    uaddr21 = keyu21.address
    uaddr22 = keyu22.address
    uaddr23 = keyu23.address
    uaddr24 = keyu24.address
    uaddr25 = keyu25.address
    uaddr26 = keyu26.address
    uaddr27 = keyu27.address
    uaddr28 = keyu28.address
    uaddr29 = keyu29.address
    uaddr30 = keyu30.address
    uaddr31 = keyu31.address
    uaddr32 = keyu32.address
    uaddr33 = keyu33.address
    uaddr34 = keyu34.address
    uaddr35 = keyu35.address
    uaddr36 = keyu36.address
    uaddr37 = keyu37.address
    uaddr38 = keyu38.address
    uaddr39 = keyu39.address
    uaddr40 = keyu40.address
    uaddr41 = keyu41.address
    uaddr42 = keyu42.address
    uaddr43 = keyu43.address
    uaddr44 = keyu44.address
    uaddr45 = keyu45.address
    uaddr46 = keyu46.address
    uaddr47 = keyu47.address
    uaddr48 = keyu48.address
    uaddr49 = keyu49.address
    uaddr50 = keyu50.address
    uaddr51 = keyu51.address
    uaddr52 = keyu52.address
    uaddr53 = keyu53.address
    uaddr54 = keyu54.address
    uaddr55 = keyu55.address
    uaddr56 = keyu56.address
    uaddr57 = keyu57.address
    uaddr58 = keyu58.address
    uaddr59 = keyu59.address
    uaddr60 = keyu60.address
    uaddr61 = keyu61.address
    uaddr62 = keyu62.address
    uaddr63 = keyu63.address
    uaddr64 = keyu64.address
    uaddr65 = keyu65.address
    uaddr66 = keyu66.address
    uaddr67 = keyu67.address
    uaddr68 = keyu68.address
    uaddr69 = keyu69.address
    uaddr70 = keyu70.address
    uaddr71 = keyu71.address
    uaddr72 = keyu72.address
    uaddr73 = keyu73.address
    uaddr74 = keyu74.address
    uaddr75 = keyu75.address
    uaddr76 = keyu76.address
    uaddr77 = keyu77.address
    uaddr78 = keyu78.address
    uaddr79 = keyu79.address
    uaddr80 = keyu80.address
    uaddr81 = keyu81.address
    uaddr82 = keyu82.address
    uaddr83 = keyu83.address
    uaddr84 = keyu84.address
    uaddr85 = keyu85.address
    uaddr86 = keyu86.address
    uaddr87 = keyu87.address
    uaddr88 = keyu88.address
    uaddr89 = keyu89.address
    uaddr90 = keyu90.address
    uaddr91 = keyu91.address
    uaddr92 = keyu92.address
    uaddr93 = keyu93.address
    uaddr94 = keyu94.address
    uaddr95 = keyu95.address
    uaddr96 = keyu96.address
    uaddr97 = keyu97.address
    uaddr98 = keyu98.address
    uaddr99 = keyu99.address
    uaddr100 = keyu100.address
    uaddr101 = keyu101.address
    uaddr102 = keyu102.address
    uaddr103 = keyu103.address
    uaddr104 = keyu104.address
    uaddr105 = keyu105.address
    uaddr106 = keyu106.address
    uaddr107 = keyu107.address
    uaddr108 = keyu108.address
    uaddr109 = keyu109.address
    uaddr110 = keyu110.address
    uaddr111 = keyu111.address
    uaddr112 = keyu112.address
    uaddr113 = keyu113.address
    uaddr114 = keyu114.address
    uaddr115 = keyu115.address
    uaddr116 = keyu116.address
    uaddr117 = keyu117.address
    uaddr118 = keyu118.address
    uaddr119 = keyu119.address
    uaddr120 = keyu120.address
    uaddr121 = keyu121.address
    uaddr122 = keyu122.address
    uaddr123 = keyu123.address
    uaddr124 = keyu124.address
    uaddr125 = keyu125.address
    uaddr126 = keyu126.address
    uaddr127 = keyu127.address
    counter+=1
    total+=256
    query=(caddr,caddr1,caddr2,caddr3,caddr4,caddr5,caddr6,caddr7,caddr8,caddr9,caddr10,caddr11,caddr12,caddr13,caddr14,caddr15,caddr16,caddr17,caddr18,caddr19,caddr20,caddr21,caddr22,caddr23,caddr24,caddr25,caddr26,caddr27,caddr28,caddr29,caddr30,caddr31,caddr32,caddr33,caddr34,caddr35,caddr36,caddr37,caddr38,caddr39,caddr40,caddr41,caddr42,caddr43,caddr44,caddr45,caddr46,caddr47,caddr48,caddr49,caddr50,caddr51,caddr52,caddr53,caddr54,caddr55,caddr56,caddr57,caddr58,caddr59,caddr60,caddr61,caddr62,caddr63,caddr64,caddr65,caddr66,caddr67,caddr68,caddr69,caddr70,caddr71,caddr72,caddr73,caddr74,caddr75,caddr76,caddr77,caddr78,caddr79,caddr80,caddr81,caddr82,caddr83,caddr84,caddr85,caddr86,caddr87,caddr88,caddr89,caddr90,caddr91,caddr92,caddr93,caddr94,caddr95,caddr96,caddr97,caddr98,caddr99,caddr100,caddr101,caddr102,caddr103,caddr104,caddr105,caddr106,caddr107,caddr108,caddr109,caddr110,caddr111,caddr112,caddr113,caddr114,caddr115,caddr116,caddr117,caddr118,caddr119,caddr120,caddr121,caddr122,caddr123,caddr124,caddr125,caddr126,caddr127)
    query1=(uaddr,uaddr1,uaddr2,uaddr3,uaddr4,uaddr5,uaddr6,uaddr7,uaddr8,uaddr9,uaddr10,uaddr11,uaddr12,uaddr13,uaddr14,uaddr15,uaddr16,uaddr17,uaddr18,uaddr19,uaddr20,uaddr21,uaddr22,uaddr23,uaddr24,uaddr25,uaddr26,uaddr27,uaddr28,uaddr29,uaddr30,uaddr31,uaddr32,uaddr33,uaddr34,uaddr35,uaddr36,uaddr37,uaddr38,uaddr39,uaddr40,uaddr41,uaddr42,uaddr43,uaddr44,uaddr45,uaddr46,uaddr47,uaddr48,uaddr49,uaddr50,uaddr51,uaddr52,uaddr53,uaddr54,uaddr55,uaddr56,uaddr57,uaddr58,uaddr59,uaddr60,uaddr61,uaddr62,uaddr63,uaddr64,uaddr65,uaddr66,uaddr67,uaddr68,uaddr69,uaddr70,uaddr71,uaddr72,uaddr73,uaddr74,uaddr75,uaddr76,uaddr77,uaddr78,uaddr79,uaddr80,uaddr81,uaddr82,uaddr83,uaddr84,uaddr85,uaddr86,uaddr87,uaddr88,uaddr89,uaddr90,uaddr91,uaddr92,uaddr93,uaddr94,uaddr95,uaddr96,uaddr97,uaddr98,uaddr99,uaddr100,uaddr101,uaddr102,uaddr103,uaddr104,uaddr105,uaddr106,uaddr107,uaddr108,uaddr109,uaddr110,uaddr111,uaddr112,uaddr113,uaddr114,uaddr115,uaddr116,uaddr117,uaddr118,uaddr119,uaddr120,uaddr121,uaddr122,uaddr123,uaddr124,uaddr125,uaddr126,uaddr127)
    pagenumber= (int(seed)//128)+1
    if len(query) == 128 or len(query1) == 128:
        
        try:
            request = requests.get("https://blockchain.info/multiaddr?active=%s" % ','.join(query), timeout=10)
            request = request.json()


            for row in request["addresses"]:
                print(row)
                if row["final_balance"] or row["total_received"]> 0:
                    print('💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰')
                    console.print('[bold green]📋 Page Number : [' + str(pagenumber) + '] [/bold green]')
                    print( 'Matching Key ==== Found!!!\n PrivateKey: ' + key.to_hex())
                    print('⛔️WARNING !!!!  Any Winners found will be Within 128 Private Key range of this Scan !!!! WARNING !!!!⛔️')
                    print('💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰')
                    f=open("winner.txt","a")
                    f.write('\n=============Bitcoin Address with Balance Found=====================')
                    f.write('\nPage Number: '+ str(pagenumber))
                    f.write('\nPrivateKey (hex): ' + key.to_hex())
                    f.write('\nBitcoin Address Compressed : ' + caddr)
                    f.write('\nBitcoin Address UnCompressed :' + uaddr)
                    f.write('\nPrivateKey (wif) Compressed : ' + wifc)
                    f.write('\nPrivateKey (wif) UnCompressed : ' + wifu)
                    f.write('\n Check All Addresses within 128 in this range to find wallet')
                    f.close()
                    break
            request1 = requests.get("https://blockchain.info/multiaddr?active=%s" % ','.join(query1), timeout=10)
            request1 = request1.json()


            for row in request1["addresses"]:
                print(row)
                if row["final_balance"] or row["total_received"]> 0:
                    print('💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰')
                    console.print('[bold green]📋 Page Number : [' + str(pagenumber) + '] [/bold green]')
                    print( 'Matching Key ==== Found!!!\n PrivateKey: ' + key.to_hex())
                    print('⛔️WARNING !!!!  Any Winners found will be Within 128 Private Key range of this Scan !!!! WARNING !!!!⛔️')
                    print('💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰')
                    f=open("winner.txt","a")
                    f.write('\n=============Bitcoin Address with Balance Found=====================')
                    f.write('\nPage Number: '+ str(pagenumber))
                    f.write('\nPrivateKey (hex): ' + key.to_hex())
                    f.write('\nBitcoin Address Compressed : ' + caddr)
                    f.write('\nBitcoin Address UnCompressed :' + uaddr)
                    f.write('\nPrivateKey (wif) Compressed : ' + wifc)
                    f.write('\nPrivateKey (wif) UnCompressed : ' + wifu)
                    f.write('\n Check All Addresses within 128 in this range to find wallet')
                    f.close()
                    break
        except:
            pass

        query = []
        console.print('[red] [' + str(counter) + '] ------------------------[/red]')
        console.print('[red]🔁 Total Checked 👇[' + str(total) + '] [/red]')
        print('😒😞😔😟😕 Bitcoin Address Compressed : ' + caddr)
        print('😒😞😔😟😕 Bitcoin Address UnCompressed : ' + uaddr)
        print('🔑 Private Key (HEX) : ' + key.to_hex())
        print('🔑 Private Key (DEC) : ' + seed)
        print('🔑 PrivateKey (wif) Compressed : ' + wifc)
        print('🔑 PrivateKey (wif) UnCompressed : ' + wifu)
        console.print('[red]📋 Page Number : [' + str(pagenumber) + '] [/red]')
        for i in range(len(animation)):
            time.sleep(0.5)
            sys.stdout.write("\r" + colour + lol + "Loading 10 Seconds :" + animation[i % len(animation)])
            sys.stdout.flush()
