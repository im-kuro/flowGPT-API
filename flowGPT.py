from requests import sessions
import urllib.parse, json




class flowGPT():
	def __init__(self):
		self.session = sessions.Session()
		self.session.headers.update({
			"Host": "flowgpt.com",
			"Cookie": "__Host-next-auth.csrf-token=5746e527849f9acade58c2c11ac4ef9d95ec1e62c7c1f223bb6439e5c6cb805d%7C2909431aab5aac82941cc4a2861d732aed00bfe2c165a958e2a88194d4fb4523; __Secure-next-auth.callback-url=https%3A%2F%2Fflowgpt.com; mp_a44b0bc977d2c56bbe900386ad3af00a_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A188d9fbbad17fb-075fc72686488c-603f5054-1fa400-188d9fbbad17fb%22%2C%22%24device_id%22%3A%20%22188d9fbbad17fb-075fc72686488c-603f5054-1fa400-188d9fbbad17fb%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D",
			"Sec-Ch-Ua": "",
			"Sec-Ch-Ua-Platform": "",
			"Sec-Ch-Ua-Mobile": "?0",
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36",
			"Content-Type": "application/json",
			"Accept": "*/*",
			"Sec-Fetch-Site": "same-origin",
			"Sec-Fetch-Mode": "cors",
			"Sec-Fetch-Dest": "empty",
			"Referer": "https://flowgpt.com/",
			"Accept-Encoding": "gzip, deflate",
			"Accept-Language": "en-US,en;q=0.9"
		})


	def searchPromt(self, seachQ: str) -> json:
		"""searches the database for a promt

		Args:
			seachQ (str): the type of promt you want to search for

		Returns:
			json: json response from the server
		"""
		data = {
			"0": {
				"json": {
					"tag": "null",
					"sort": "null",
					"q": seachQ,
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
		return self.session.get(f"https://flowgpt.com/api/trpc/prompt.getPrompts?batch=1&input={urllib.parse.quote(json.dumps(data))}").json()

	def getFeaturedPromts (self) -> json:
		"""gets the current featured promts

		Args:
			None
		Returns:
			json: json response from the server
		"""
		data = """
			{
				"0":{
					"json":10
				}
			}
		
		"""
		return self.session.get(f"https://flowgpt.com/api/trpc/collection.getFeaturedCollections?batch=1&input={data}").json()

	def getCollections(self) -> json:
		data = """
		{
			"0":{
				"json":null, 
				"meta":{
					"values":[
						"undefined"
					]
				}
			}
		}
		"""
		return self.session.get(f"https://flowgpt.com/api/trpc/collection.getCollections?batch=1&input={data}").json()
	
  
  
  
  