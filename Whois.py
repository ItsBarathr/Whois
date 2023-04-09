#!/bin/Python3
#Created by : ItsBarathr
#Name : Whois

# usage : Python3 Whois.py -i example.com
import requests
import argparse
import json

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--info", help="Get information about domain name")
    args = parser.parse_args()
    ip = args.info
    
    #Check its get input or not
    if ip:
        
        #API URL
        url = "http://ip-api.com/json/"+ip
        respon = requests.get(url)
        data = json.loads(respon.content)
        
        #print all value in JSON format
        print("Ip address : ", data["query"])
        print("Country : ", data["country"])
        print("Region Name : ", data["regionName"])
        print("City : ", data["city"])
        print("Lat : ", data["lat"])
        print("Lon : ", data["lon"])
        print("Isp : ", data["isp"])
        print("Org : ", data["org"])
    
    else:
        print("usage : Whois.py -i example.com")
        print("Error : Domain name or option are not found")