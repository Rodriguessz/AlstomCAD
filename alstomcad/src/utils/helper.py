import datetime

def getRelayInfos(relay, cab = "1"):
  releyObject = {"R": None, "SIN": None, "cab": cab}
  for attibute in relay.GetAttributes():
    releyObject[attibute.TagString] = attibute.TextString
  return releyObject;

def getModDate(filepath):
  modfication_date = datetime.datetime.fromtimestamp(filepath.stat().st_mtime)

  return modfication_date;