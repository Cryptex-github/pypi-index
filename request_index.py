import requests

r = requests.get("https://www.piwheels.org/packages.json").json()
packages = "\n".join([package[0] for package in r])

with open("requirements.txt", "w") as f:
  f.write(packages)
