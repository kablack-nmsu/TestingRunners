import random
RAN = ("$", "#", "*", "~", "^", "@")

def randgrid(charlist):
  out = ""
  for index in range(0, 30):
    for index2  in range(0, 70):
      out += charlist[random.randint(0, len(charlist) - 1)]
    out += "\n"
  return out


print(randgrid(RAN))
