from selfie_models import Selfie

def SeedData():
    Selfie(title='Working Hard', image='https://i.imgur.com/Rpj8BCx.jpg', user='Nate', price='29.99').put()
    Selfie(title='Buy Now! Very Rare', image='https://i.imgur.com/QwRfOJT.jpg', user='Selfie Markeplace LLC', price='99.99').put()
