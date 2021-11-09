import random 

# import tkinter as tk
import tkinter as tk
from tkinter.constants import CENTER, N, S


# import image library

from PIL import ImageTk,Image

photoArray = ["AligatorLoki.jpg","BaldNonce.jpg", "BorisJohnson.jpeg", "Dadosaur.png",  "DannyDorito.jpg", "Doll.jpg", "Drip_Goku.jpg", "freecuthbert.jpg", "Halo3Rat.jpg", "hilda.jpeg", "IceAgeBaby.jpg", "imthetrashman.png", "johnxina.jpg", "keanu.jpg", "KevinMug.jpg", "KrisJongUn.png", "ladydimitrescu.png", "lobsterwoman.jpg", "PsychicFriendFredbear.jpg" , "RapperMario.jpg" , "SlavCat.jpg" , "SquirtGunPriest.jpg" , "StudyGirl.jpg" , "the_wock.jpg" , "wurmple.png"]


root = tk.Tk()


# setting tkinter size 
root.geometry('600x400+50+50')


x = len(photoArray)
x -= 1
# getting image 
kev = random.randint(0,x)

print(kev)
if kev == 14:
    image1 = Image.open(photoArray[14])
    test = ImageTk.PhotoImage(image1)
    label2 = tk.Label(image=test)
    label2.pack()
    root.mainloop()
    import sys, time
    time.sleep(10)
    sys.exit()


else: pass

# Create a photoimage object of the image in the path
image1 = Image.open(photoArray[kev])
test = ImageTk.PhotoImage(image1)

label1 = tk.Label(image=test)
label1.image = test
windowSize = root.winfo_width
label1.place(relx=0.5, rely=0.7, anchor=S)




with open ("6K adverbs.txt", "r") as adverbs:
    adverbList = adverbs.readlines()
adverbs.close()

with open ("28K adjectives.txt", "r") as adjectives:
    adjectiveList = adjectives.readlines()
adjectives.close()

with open ("31K verbs.txt", "r") as verbs:
    verbsList = verbs.readlines()
verbs.close()

with open ("91K nouns.txt", "r") as nouns:
    nounsList = nouns.readlines()
nouns.close()

sentence = (" {} \n {} {} {} {}".format(photoArray[kev].split(".",1)[0], verbsList[random.randint(0,len(verbsList))], nounsList[random.randint(0,len(nounsList))],\
    adjectiveList[random.randint(0,len(adjectiveList))], adverbList[random.randint(0,len(adverbList))]))
sentence = sentence.strip()

print (sentence)
# adding sentence 
l = tk.Label(root, text = sentence)
l.place(relx= 0.5, rely= 0.7, anchor=CENTER)
l.pack()

root.mainloop()

# Final commit 