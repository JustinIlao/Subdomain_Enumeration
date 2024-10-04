import requests
import argparse
import time


def main():
    parser = argparse.ArgumentParser()
    #Add argument to parser
    parser.add_argument("-u", "--Url", type =str, help = "Input url and enumerate.")
    args = parser.parse_args()
    print(args.Url)
    if args.Url:
        with open('TOPsubdomains.txt') as h:
            for i in h: #open Textfile with subdomains
                r = requests.get("https://"+i.strip()+"."+args.Url) #grab and combine the prefix(subdomain) with url passed.
                print(r)
                if r.status_code == 200:
                    with open("Successfuldomains.txt", "a+") as z: #If status code is 200 write domain to a txt file(Created if not there)
                        z.write("https://"+i.strip()+"."+args.Url+"\n")
                time.sleep(1) #sleep to prevent a refused connection


if __name__ == "__main__":
    main()