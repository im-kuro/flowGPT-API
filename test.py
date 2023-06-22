import requests, urllib.parse, json

tag = "null"
sort = "null"
searchQ = "marketing"

data = {
	"0": {
		"json": {
			"tag": tag,
			"sort": sort,
			"q": searchQ,
			"language": "en"
		},
		"meta": {
			"values": {
				"tag": [
					"undefined"
				],
				"sort": [
					"undefined"
				]
			}
		}
	}
}

z =  requests.get(f"https://flowgpt.com/api/trpc/prompt.getPrompts?batch=1&input={urllib.parse.quote(json.dumps(data))}").json()


#loop through all the results ti find ids/promts/ect.
for i in z[0]['result']['data']['json']:
	print("promt ID -> " + i['id'])
	print("title -> " + i['title'])
	print("")