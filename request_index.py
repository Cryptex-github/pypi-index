import requests

r = requests.get("https://www.piwheels.org/packages.json").json()
excluded = [
  "mapnik",
]
def check_is_valid(package):
  try:
    return requests.get(f"https://pypi.org/pypi/{package}/json").json()["info"]["downloads"]["last_month"] >= 1
  except:
    return False
packages = "\n".join([package[0] for package in r if ":" not in package[0] and not any(i in package[0] for i in excluded) and check_is_valid(package[0])][:1000])

with open("requirements.txt", "w") as f:
  f.write(packages)
