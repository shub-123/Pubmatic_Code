from configparser import ConfigParser


def parse_data():
    config = ConfigParser()
    config.read("C:/Users/Admin/PycharmProjects/Python_Practice_demo/Properties.ini")
    return config

def url_connections():
    d = {"url1" : "http://"+ parse_data()["Domain"]["url1"] +"/ads.txt",
         "url2": "http://"+ parse_data()["Domain"]["url2"] +"/ads.txt",
         "url3": "http://"+ parse_data()["Domain"]["url3"] +"/ads.txt",
         "url4":"http://"+ parse_data()["Domain"]["url4"] +"/ads.txt"}

    return d




