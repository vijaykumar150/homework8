class Animal:
    def __init__(self,name):
        self.name = name
    def guess_who_am_i(self):
        d1={"elephant":["I have exceptional memory","I'm the largest land living mammal in the world","I have long trunk"],"tiger":["I am the biggest cat","I come in black and white or orange and black","My scientific name is Panthera tigris"],"bat":["I use echo-location","I come in black and white or orange and black","I see well in dark"]}

        print("\n\nI will give you 3 hints, guess what animal I am\n")
        cnt=0
        while cnt<3:
          print(d1[self.name][cnt])
          n1 = input("Who am i? : ")
          if n1 == self.name:
            print("You got it! I am "+ self.name + "\n\n")
            return 1
          else:
            print("Nope, try again!\n")
            cnt=cnt+1
        print("\nI'm out of hints! The answer is : " + self.name + "\n\n")



e = Animal('elephant')
t = Animal("tiger")
b = Animal("bat")

e.guess_who_am_i()
t.guess_who_am_i()
b.guess_who_am_i()