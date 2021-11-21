import sys

def get_msg(command):
  parent = sys.path[0]
  f = open(f"{parent}/texts/{command}.txt", "r")
  text = f.readlines()
  f.close()
  msg = ""
  for line in text:
    msg = msg + line
  return msg