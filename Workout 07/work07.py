import re

txt1 = "red flag blue flag"
txt2 = "yellow flag red flag blue flag green flag"
txt3 = "pink flag red flag black flag blue flag green flag red flag"
pattern = "red flag|blue flag"

print(re.findall(pattern, txt1))
print(re.findall(pattern, txt2))
print(re.findall(pattern, txt3))
