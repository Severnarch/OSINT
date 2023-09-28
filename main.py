import json
from requests import get

sites = {}

with open("sites.json") as f:
	sites = json.loads(f.read())

def main():
	print("[out] Enter an input type by number: [1] Name")
	types = ["name"]
	valRange = [1, len(types)]
	section = int(input("[int] > "))
	if section >= valRange[0] and section <= valRange[1]:
		finds = []
		maxFinds = len(sites[types[int(section)-1]])
		query = input("[str] > ")
		inputKey = sites["inputKey"]
		for site in sites[types[int(section)-1]]:
			req = get(site[1].replace(inputKey, query))
			if req.status_code == 200:
				if query in req.url and query in req.text.split("<body")[1]:
					markFound = True
					if markFound: finds.append([site[0], site[1].replace(inputKey, query)])
		for find in finds:
			print("[out] FOUND '"+find[0].lower()+"': "+find[1])

		print("[out] "+str(len(finds))+" out of "+str(maxFinds)+" sites found '"+query+"' user")
	else:
		print("[out] Invalid input. Please try again.")
		main()

if __name__ == "__main__":
	rep = True
	while rep:
		try:
			main()
			print("[out] Enter another name? (Y/N)")
			x = input("[bol] > ")
			if x.lower() == "n" or x.lower() == "f" or x.lower() == "x" or x.lower() == "false":
				rep = False
		except Exception as e:
			print("[err] "+str(e))
