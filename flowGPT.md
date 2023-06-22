## flowGPT API Docs (unoffical) 


### flowGPT


---

#### Data response breakdown

Most data is returned in the form of arrays in json format. The following is a breakdown of the data returned by the API.
This response is specificly from /api/trpc/collection.getCollections returning the collections.
```json

[
	{
		"result": {
			"data": {
				"json": [
				{
					"id": "he-hgVnnN6xDSSEzW_R-h",
					"createdAt": "2023-06-21T01:36:07.238Z",
					"title": "SWE Engineering Prompts",
					"description": "Introducing a captivating collection of Swe Prompts! This meticulously curated assortment is a treasure trove for all writers seeking inspiration. Spanning various genres and themes, these prompts are designed to spark your creative genius and set your imagination ablaze. With 100 thought-provoking and evocative prompts, each crafted with utmost care, this collection offers a diverse range of storytelling possibilities. From thrilling adventures to heartfelt dramas, from mysterious puzzles to romantic escapades, Swe Prompts has it all. Unleash your inner storyteller and embark on a journey of endless possibilities with this exceptional compilation, a must-have companion for every aspiring wordsmith.",
					"userId": "28d3beb2-f6b8-4d22-8de2-270b9c922ad7",
					"featured": false,
					"thumbnailUrl": "https://www.springboard.com/blog/wp-content/uploads/2020/02/Screen-Shot-2020-09-25-at-9.50.34-AM.png",
					"Prompt": [
						{
							"id": "fp7U3k9Z3BnbzvqLt1tBC",
							"createdAt": "2023-04-02T19:17:38.943Z",
							"updatedAt": "2023-06-21T14:52:13.881Z",
							"title": "GUI GPT API prompt generator",
							"description": "A GUI GPT-3/4 API prompt generator written in Python. Can be used to create for prompt engineering to create more advanced prompts in a visual way and fetch results directly in the interface.",
							"saves": 18,
							"userId": "l7JPPh4o0A2cA-5FsqpLp",
							"thumbnailURL": "https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/realistic/real_9.png",
							"upvotes": 9,
							"initPrompt": "You are an experienced python developer. Your task is to develop a visual (GUI) desktop prompt editor with the following features:\n\nSelection of a role for ChatGPT to use from a list of most popular roles (e.g. Lawyer, Software Developer, Marketing Specialist, etc.).\n\nA slider to regulate Top P of the model\n\nA slider to regulate Temperature of the model\n\nA checkbox to include markdown (results in prompt addendum that requests to include headings, formatting, etc.)\n\nA checkbox to include questions from the model (results in prompt addendum that requests to include the text \"If you have any clarifying questions about the task, ask now before answering\")\n\nA text field to input the base prompt\n\nA button to generate the resulting prompt\n\nA text field that is editable and displays the resulting prompt (separate from the chat)\n\nA widget to select a GPT model from a list of all available models\n\nA button to call the selected GPT API to fetch the answer to the prompt from field 8.\n\nA chat log to display the result of queries, with new queries getting added to the bottom like in ChatGPT.\n\n\nThe Right panel containing the chat should take 80% width and the left panel with the prompts and buttons should be 20% width.\n\nThe chat should support text with markup.\n\nDevelop python code for the requested program.",
							"live": true,
							"popularity": 2462.5,
							"views": 371,
							"conversationId": "4d919cf0-5fca-41d0-adef-7c959b09e71b",
							"editedAt": null,
							"language": "en",
							"uses": 28,
							"ranking": 0.03916303342539415,
							"model": "chatgpt",
							"adminWeight": 1,
							"createdMethod": null,
							"systemMessage": null,
							"type": "CHATBOT",
							"Tag": [
								{
									"id": "295c7cec-4617-436d-bccb-41b642b88845",
									"createdAt": "2023-03-10T00:57:03.800Z",
									"name": "software_development"
								},
								{
									"id": "RTfNWml-WNHrkAY9ojB5s",
									"createdAt": "2023-04-02T12:15:51.283Z",
									"name": "prompt"
								},
								{
									"id": "HEATM1DgQOwAhL37YkMUv",
									"createdAt": "2023-04-02T19:17:38.563Z",
									"name": "python"
								},
								{
									"id": "KunrwXm42yQDhHiovAnsK",
									"createdAt": "2023-04-02T19:17:38.563Z",
									"name": "prompt engineering"
								}
							]
						}
						]
					}
				]
			}
		}
	}
]

```

A quick look at the response will tell you that we have a list of objects, each with a `result` key. The `result` key contains a `data` key, which in turn contains a `json` key. The `json` key holds an array of objects, which is the data we are interested in.

Each object in the array has the following properties:

- `id`: The ID of the prompt/data object.
- `createdAt`: The timestamp of when the object was created.
- `title`: The title of the prompt or data.
- `description`: A detailed description of the prompt or data.
- `userId`: The ID of the user who created the prompt or data.
- `featured`: A boolean value indicating if the prompt or data is featured.
- `thumbnailUrl`: The URL of the thumbnail image associated with the prompt or data.
- `Prompt`: An array of prompt objects associated with the data.

Each prompt object within the `Prompt` array has the following properties:

- `id`: The ID of the prompt.
- `createdAt`: The timestamp of when the prompt was created.
- `updatedAt`: The timestamp of when the prompt was last updated.
- `title`: The title of the prompt.
- `description`: A description of the prompt.
- `saves`: The number of times the prompt has been saved.
- `userId`: The ID of the user who created the prompt.
- `thumbnailURL`: The URL of the thumbnail image associated with the prompt.
- `upvotes`: The number of upvotes received by the prompt.
- `initPrompt`: The initial prompt text.
- `live`: A boolean value indicating if the prompt is live.
- `popularity`: The popularity score of the prompt.
- `views`: The number of views the prompt has received.
- `conversationId`: The ID of the conversation associated with the prompt.
- `editedAt`: The timestamp of when the prompt was last edited.
- `language`: The language of the prompt.
- `uses`: The number of times the prompt has been used.
- `ranking`: The ranking score of the prompt.
- `model`: The GPT model associated with the prompt.
- `adminWeight`: The administrative weight of the prompt.
- `createdMethod`: The method used to create the prompt.
- `systemMessage`: A system message associated with the prompt.
- `type`: The type of the prompt.
- `Tag`: An array of tag objects associated with the prompt.

Each tag object within the `Tag` array has the following properties:

- `id`: The ID of the tag.
- `createdAt`: The timestamp of when the tag was created.
- `name`: The name of the tag.

---

#### Data Sent Breakdown

The input data sent to all endpoints is in URL encoded JSON format. The JSON structure is consistent, although some specific details may vary depending on the endpoint.

```json
{
   "0":{
      "json":10
   },
   "1":{
      "json":{
         "q":"cybersec"
      },
      "meta":{
         "values":[
            "undefined"
         ]
      }
   }
}
```

The JSON object consists of multiple entries, each identified by a numeric key. The key starts from 0 and increments for each entry. Each entry represents different data sent to the endpoint.

- The first object (key: 0) is not fixed and varies for different endpoints. It does not follow a specific structure.
- The second object (key: 1) contains the data intended for use by the endpoint. It provides relevant information for the request.
- The third object (key: 2) holds metadata associated with the data sent. It likely includes additional details such as tags that are not included in the data object itself. The meta object is mainly used for supplementary information that may be required for other requests.

The following snippet represents the structure of the second object (key: 1) in the JSON:

```json
    "json":{
         "tag":null,
         "sort":null,
         "q":null,
         "language":"en"
      }
```

This snippet shows the available fields within the second object. The values for these fields may vary based on the specific endpoint. The fields include:

- "tag": Represents a tag associated with the data (null in this example).
- "sort": Specifies the sorting criteria for the data (null in this example).
- "q": Indicates a query parameter or search term (null in this example).
- "language": Specifies the language of the data, with "en" representing English in this case.


---


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

