# flowGPT API (Unofficial)

---


This is a simple public documented wrapper that is for flowGPT API. Nothing special though it could be useful to imlpement in your personal projects.
You can custom search for a specific promt or explore the wide range of prompts available. This could be useful for a variety of things such as 
AI generated anything really. 

[FlowGPT API docs](https://github.com/im-kuro/flowGPT-API/blob/main/flowGPT.md)
[Public API Wrapper](https://github.com/im-kuro/flowGPT-API/blob/main/flowGPT.py)


### install
```bash
git clone https://github.com/im-kuro/flowGPT-API
```


```bash
python -m pip install requirements.txt
```


#### Example Code

The following code snippet shows how to use the API wrapper & requests to retrieve a list of prompts and loop through them to find the 
prompt ID and title. The code snippet uses the `searchPrompt` endpoint to retrieve a list of prompts. The `searchPrompt` endpoint is used to search for prompts based on a specific tag, sorting criteria, and search term. The code snippet uses the following parameters:


flowGPT.py wrapper
```python

from flowGPT import flowGPT

# init the class
flowgptHandle = flowGPT()

# search for a prompt, saving the results to the variable 'x'
x = flowgptHandle.searchPromt(tag="python", sort="popularity", seachQ="python")

#loop through all the results to find ids/promts/ect.
for i in x[0]['result']['data']['json']:
	print("promt ID -> " + i['id'])
	print("title -> " + i['title'])
	print("")
```

useing requests
```python
import requests, urllib.parse, json

#define vars
tag = "null"
sort = "null"
searchQ = "marketing"
# define data to send
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
# send the request and save the results to the variable 'z'
z =  requests.get(f"https://flowgpt.com/api/trpc/prompt.getPrompts?batch=1&input={urllib.parse.quote(json.dumps(data))}").json()


#loop through all the results to find ids/promts/ect.
for i in z[0]['result']['data']['json']:
	print("promt ID -> " + i['id'])
	print("title -> " + i['title'])
	print("")

```

