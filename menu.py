import random
import pyttsx3


class menu:

    def __init__(self):
        self.breakfast = ['aloo/paneer/palak/methi/Gobi paratha', 'sprouts', 'sevai', 'upma/dalia/poha', 'frankie', 'cheese sandwich', 'besan/moong chilla', 'lal channa']
        self.lunch = ['bhindi',	'aloo Gobi', 'fried rice', 'Shimla mirch alooo', 'carrot beans', 'aloo pyaaz', 'lauki', 'Brinjal']
        self.dinner = ['cuddi besan gatte',	'dosa',	'dal fry/tadka', 'paneer kofta/butter/bhurji', 'kichidi', 'besan ke gatte',	'Puri aloo mattar sabji', 'rajma']


    def computeBreakfast(self):
        l = len(self.breakfast)
        meal = self.breakfast[random.randint(0, l-1)]
        self.callPyttsx3("Hi! Ena, We have " + meal + " for breakfast,")


    def computeLunch(self):
        l = len(self.lunch)
        meal = self.lunch[random.randint(0, l-1)]
        self.callPyttsx3(meal + " for lunch, ")


    def computeDinner(self):
        l = len(self.dinner)
        meal = "and " + self.dinner[random.randint(0, l-1)]
        self.callPyttsx3(meal + " for dinner.")        

    
    def callPyttsx3(self, result):
        print(result)
        engine = pyttsx3.init()
        engine.say(result)
        engine.runAndWait()


menuObj = menu()
menuObj.computeBreakfast()
menuObj.computeLunch()
menuObj.computeDinner()