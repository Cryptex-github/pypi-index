import requests

r = requests.get("https://www.piwheels.org/packages.json").json()
excluded = [
  "mapnik",
]
packages = "\n".join([package[0] for package in r if ":" not in package[0] and not any(i in package[0] for i in excluded) and requests.get(f"https://pypi.org/pypi/{package[0]}/json").json()["info"]["downloads"]["last_month"] >= 1][:10000])

with open("requirements.txt", "w") as f:
  f.write(packages)
