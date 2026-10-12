class person:# this becomes a tamplet for every person
    name = "isagi"# this will be default person name
    occupation = "u20 striker"# this will be default person occupation
    networth = 190000000# this will be default person networth
    def worldcup(self):
        print(f"player name: {self.name} \noccupation : {self.occupation}")

#for every player objects there will be his own name occupation etc
#person class is a tamplet that decides for every player what details should be mentioned
player1 = person()
player1.name = "ichigo"# here iam specifying the properties of the person 
player1.occupation = "soul reaper"
player1.worldcup()

player2 = person()# here iam using the default properties of the class
player2.worldcup()