import requests

client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
redirect_uri = "YOUR_WEBSITE_URL/"

# Prompt the user to authorize your app and obtain an authorization code
auth_url = "https://anilist.co/api/v2/oauth/authorize?client_id={}&redirect_uri={}&response_type=code".format(client_id, redirect_uri)
print("Please go to the following URL and authorize your app: " + auth_url)
auth_code = input("Enter the authorization code: ")

# Exchange the authorization code for an access token
token_url = "https://anilist.co/api/v2/oauth/token"
data = {
    "grant_type": "authorization_code",
    "client_id": client_id,
    "client_secret": client_secret,
    "redirect_uri": redirect_uri,
    "code": auth_code
}
response = requests.post(token_url, data=data)

# Extract the access token from the response
if response.status_code == 200:
    access_token = response.json()["access_token"]
    print("Access token: " + access_token)
else:
    print("Failed to obtain access token.")

