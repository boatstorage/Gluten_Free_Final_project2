
from yelp.client import Client 
from yelp.oauth1_authenticator import Oauth1Authenticator 



from GFW_tokens import *

auth = Oauth1Authenticator(
	consumer_key=YOUR_CONSUMER_KEY,
	consumer_secret =YOUR_CONSUMER_SECRET,
	token=YOUR_TOKEN,
	token_secret=YOUR_TOKEN_SECRET
)
 # make dictionary of parameters based on user input
params = {
	"location": "San Francisco",
	# "radius_filter": 10, 
	"term": "gluten free, GF, Free from Gluten" 
	# "snippet_text": "Gluten-Free"


}
def user_prompt():
	location_param = raw_input("What city are you searching in?")
	params["location"] = location_param
	
	return params

client = Client(auth)
# def gf_restaurants(client):
params = user_prompt()
response = client.search(**params)
business_objs_list = response.businesses
# print client.__dict__
print business_objs_list
for restaurant in business_objs_list:
	print restaurant.name
