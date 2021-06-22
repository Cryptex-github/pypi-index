import requests

r = requests.get("https://www.piwheels.org/packages.json").json()
packages = "\n".join([package[0] for package in r if ":" not in package[0]][:10000])

with open("requirements.txt", "w") as f:
  f.write(packages)
