import urllib, json
import time
from Tkinter import *

root = Tk()
root.wm_title("SimpleCryptoBalances")
text = Text(root, width=100, height=50)

scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )
scrollbar.config( command = text.yview )

lines=open('addr.txt').readlines()
for line1,line2 in zip(lines[::2],lines[1::2]):
	if line1.strip() == 'BTC':
		btcaddr = line2.strip()
		url = "https://blockchain.info/q/addressbalance/" + btcaddr
		response = urllib.urlopen(url);
		data = json.loads(response.read())
		sdata = "{:,}".format(data / 100000000.0, '.8f')
		text.insert(INSERT, '\n' + btcaddr + '\n' + sdata + ' BTC\n')	 
		
	if line1.strip() == 'LTC':
		ltcaddr = line2.strip()
		url = "http://explorer.litecoin.net/chain/Litecoin/q/getreceivedbyaddress/" + ltcaddr
		url2 = "http://explorer.litecoin.net/chain/Litecoin/q/getsentbyaddress/" + ltcaddr
		response = urllib.urlopen(url);
		response2 = urllib.urlopen(url2);
		data = json.loads(response.read())
		data2 = json.loads(response2.read())
		data3 = data - data2
		ltcdata =  '\n' + ltcaddr + '\n' + "{:,}".format(data3) + ' LTC\n'
		text.insert(INSERT, ltcdata)	
		text.tag_add(ltcdata, "1.0", "1.4")
		text.tag_config(ltcdata, background="yellow")
		
	if line1.strip() == 'DOGE':
		dogeaddr = line2.strip()
		url = "https://dogechain.info/chain/Dogecoin/q/addressbalance/" + dogeaddr
		response = urllib.urlopen(url);
		data = json.loads(response.read())
		text.insert(INSERT, '\n' + dogeaddr + '\n' + "{:,}".format(data) + ' DOGE\n' )	
	
text.insert(END, '' )
text.pack()

root.mainloop()
	