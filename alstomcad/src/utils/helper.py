import datetime
from colorama import Fore, Back, Style

def getRelayInfos(relay, cab = "1"):
  releyObject = {"R": None, "SIN": None, "CAB": cab}
  for attibute in relay.GetAttributes():
    releyObject[attibute.TagString] = attibute.TextString
  return releyObject;

def getModDate(filepath):
      modfication_date = datetime.datetime.fromtimestamp(filepath.stat().st_mtime)
      return modfication_date;

def getDiffs(prev, new):
  diffs = {}
  for key in prev.keys():
    for positon in range(len(prev[key])):
      if(prev[key][positon] != new[key][positon] ):
        # diff = {prev[key][positon]["R"]: new[key][positon]}
        diffs[prev[key][positon]["R"]] = new[key][positon]
  return diffs

      # print(Fore.GREEN, "<-------------------------------->")
      # print("Antigo item ==> " , prev[key][positon])
      # print("Novo item ==> " , new[key][positon])
      # print(Fore.GREEN, "<-------------------------------->")

      

    