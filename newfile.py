print("The tiny gentle diary")

risposte_felici = ["good", "fine", "alright"]
risposte_tristi = ["bad", "horrible", "terrible", "tired"]

while True:
	come_stai = input("How are you today? ")
	
	if come_stai == "the end":
	    break 
	
	if come_stai in risposte_felici:
	   print("Happy to know, Viktor sends you a big hug.")
	   
	if come_stai in risposte_tristi:
	   vuole_parlare = input("Can I help you? (yes/no)")
	   
	   if vuole_parlare == "yes":
	   	print("Feel free to write everything you want, I'm here for you. 💖")
	   else:
	   	print("It's okay, I respect your silence. 🌺")

print("See you soon. 💞")