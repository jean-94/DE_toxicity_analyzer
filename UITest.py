import unittest
import requests
import time
from statistics import mean
from detoxify import Detoxify

class UITest(unittest.TestCase):

    def testmodel(self):
        model = Detoxify(checkpoint = "./Backend/toxic_original-c1212f89.ckpt",device="cpu")
        texts = ["You are ugly","Hello my name is Jean","You are the worst","The rain is made of water.","That chicken is clever, like you.","I hate you with all my heart, go die in a ditch.","That camel think, so he is.","What glorious weather we have today.","The baker is a stupid ugly man, I hope the gestapo will get him.","I hope you get yourself a great family, who you love with all your heart, so that one day you lose everything but live a long life after that. "]
        prediction = model.predict(texts)
        if (len(prediction) == 10):
            re= True
        else:
            re = False
        self.assertEqual(re,True)

    def testsubmitbutton(self):
        self.assertEqual(re, True)

    def teststress(self):
        nb_test = 100
        tab = []
        for i in range(nb_test):
            t_rstart = time.process_time()
            requests.get("http://localhost:5001/")
            t_rend = time.process_time()
            tab.append(t_rend - t_rstart)
        if mean(tab) <= 60:
            re = True
        else :
            re = False
        self.assertEqual(re,True)