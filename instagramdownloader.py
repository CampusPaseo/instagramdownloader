#!/usr/bin/python3

# import modul untuk mendownload profile instagram seseorang
import os, sys
os.system("clear")

# buat fungsi untuk menulis about author
def tentang_penulis():
	print("""\033[1m
		+=================================================================+
		....................... BEN LEO IT SECURITY .......................
		+=================================================================+
		     [!] Author          : BenLeo Cyber Security
		     [!] Hobby           : Coding and Learn Cryptography
		     [!] Created         : Oktober 17, 2021 at 15:23 PM
		     [!] Inspired By     : https://youtu.be/YNGumKrXrlQ
		+=================================================================+
		""")
tentang_penulis()

# Buat program untuk mendownload photo profil instagram seseorang
def download_photo_profil_instagram_seseorang():
	print("")
	# Import modul instaloader dan os, sys

	import instaloader
	ig=instaloader.Instaloader()
	profile=input("\033[1m[!] Input Username: ")
	print("")
	ig.download_profile(profile,profile_pic_only=True)
	print("")
	print("")
download_photo_profil_instagram_seseorang()