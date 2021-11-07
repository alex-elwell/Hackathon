import random 

# import tkinter as tk
import tkinter as tk


# import image library

from PIL import ImageTk,Image

photoArray = ["AligatorLoki.jpg","BaldNonce.jpg", "BorisJohnson.jpeg", "Dadosaur.png",  "DannyDorito.jpg", "Doll.jpg", "Drip_Goku.jpg", "freecuthbert.jpg", "Halo3Rat.jpg", "hilda.jpeg", "IceAgeBaby.jpg", "imthetrashman.png", "johnxina.jpg", "keanu.jpg", "KevinMug.jpg", "KrisJongUn.png", "ladydimitrescu.png", "lobsterwoman.jpg", "PsychicFriendFredbear.jpg" , "RapperMario.jpg" , "SlavCat.jpg" , "SquirtGunPriest.jpg" , "StudyGirl.jpg" , "the_wock.jpg" , "wurmple.png"]

# create an instance of the tk.Tk class - this creates the window. 
root = tk.Tk()
# setting tkinter size 
root.geometry('600x400+50+50')

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

sentence = (" {} {} {} {} {}".format("", verbsList[random.randint(0,len(verbsList))], nounsList[random.randint(0,len(nounsList))],\
    adjectiveList[random.randint(0,len(adjectiveList))], adverbList[random.randint(0,len(adverbList))]))
sentence = sentence.strip()

print (sentence)

x = len(photoArray)



# getting image 
img = ImageTk.PhotoImage(Image.open(photoArray[random.randint(0,x)]))
# adding sentence 
l = tk.Label(root, text = sentence)
l.pack()

root = Tk()

# Create a photoimage object of the image in the path
image1 = Image.open("<path/image_name>")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

# Position image
label1.place(x=<x_coordinate>, y=<y_coordinate>)
root.mainloop()