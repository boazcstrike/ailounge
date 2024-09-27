import datetime

everything = []
i = 1
timestamp = datetime.datetime.now().strftime("%m%d%y%H%M%S")
for i in range(4):
  i += 1
  with open(f"dump/response_business_opp_{i}.txt", "r") as file:
    content = file.read()
    everything.append(content)

with open(f"dump/response_{timestamp}.txt", "w") as file:
  file.write("\n".join(x for x in everything))
