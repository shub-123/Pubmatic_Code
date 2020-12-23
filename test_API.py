import requests
from parse_dict.parser import *
import csv





class Test_API:
    def test_API1(self):
        response = requests.get("http://"+ parse_data()["Domain"]["url1"] +"/ads.txt")
        response_data = response.text
        if response.status_code == 200:
            response_text(response_data, parse_data()["Domain"]["url1"]+ ".txt")
            print("The api run is sucess", response)

            print("---------------------------------------------")
        else:
            print("The api run is not sucess", response.status_code)

    def test_API2(self):
        response = requests.get("http://" + parse_data()["Domain"]["url2"] + "/ads.txt")
        response_data = response.text
        if response.status_code == 200:
            response_text(response_data, parse_data()["Domain"]["url2"]+ ".txt")
            print("The api run is sucess", response)
            print("---------------------------------------------")
        else:
            print("The api run is not sucess", response.status_code)


    def test_API3(self):
        response = requests.get("http://" + parse_data()["Domain"]["url3"] + "/ads.txt")
        response_data = response.text
        if response.status_code == 200:
            response_text(response_data, parse_data()["Domain"]["url3"]+".txt")
            print("The api run is sucess", response)
            print("---------------------------------------------")
        else:
            print("The api run is not sucess", response.status_code)

    def test_API4(self):
        response = requests.get("http://" + parse_data()["Domain"]["url4"] + "/ads.txt")
        response_data = response.text
        if response.status_code == 200:
            response_text(response_data, parse_data()["Domain"]["url4"]+".txt")
            print("The api run is sucess", response)
            print("---------------------------------------------")
        else:
            print("The api run is not sucess", response.status_code)



def read_file(filename):
    counter = 0
    with open(filename) as fp:
        for line in fp:
            for word in line.split(","):
                if "DIRECT" in word:
                    print(word)
                    counter +=1
        print(counter)


read_file("edition.cnn.com")

def response_text(response, url):
    with open(url, "w") as fp:
        fp.writelines(response)

Deepanshu.sagar@pubmatic.com
