# **Obtaining the client ID and client secret for Anilist API**

1. Go to the Anilist website (https://anilist.co) and create an account if you don't already have one.
2. Once you have created an account, navigate to the settings page by clicking on the gear icon in the top right corner of the page.
3. On the settings page, scroll down to the "Developer" section and click on "Developer Settings".
4. On the Developer Settings page, click on "Create New Client".
5. Fill out the form with the required information, such as the client name and redirect URLs.
6. Once you have submitted the form, your client ID and client secret will be displayed[^1]. Make sure to copy and save these credentials in a secure location.

[^1]: The client secret should be kept confidential and never shared publicly.

# **Updating Anilist API credentials and access token in Python Flask app**

1. Run the get_access_code.py script to obtain the authorization code. This script will output a URL that you can use to authorize your app.
2. Click on the URL and authorize your app. You will be redirected to a page with a code parameter in the URL. Copy this code.
3. Open the get_access_token.py file in your preferred text editor or IDE.
4. Replace the value of the AUTHORIZATION_CODE variable with the code you copied in step 2.
5. Replace the values of the CLIENT_ID and CLIENT_SECRET variables with your own client ID and client secret obtained from the Anilist Developer Settings page.
6. Save the changes to the file.
7. Run the get_access_token.py script to obtain the access token. This script will output the access token.
8. Open the app.py file in your preferred text editor or IDE.
9. Replace the value of the ACCESS_TOKEN variable with the access token obtained from step 7.
10. Save the changes to the file.
