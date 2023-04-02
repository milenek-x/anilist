from flask import Flask, render_template
import requests

app = Flask(__name__)

access_token = "YOUR_ACCESS_TOKEN"

@app.route("/")
def index():
    url = "https://graphql.anilist.co"
    query = '''
    query ($userName: String) {
      MediaListCollection(userName: $userName, type: ANIME) {
        lists {
          name
          entries {
            media {
              title {
                romaji
              }
              description
              coverImage {
                medium
              }
            }
            status
            progress
          }
        }
      }
    }
    '''

    variables = {
        "userName": "YOUR_ANILIST_USERNAME"
    }

    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    response = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)

    anime_lists = []
    if response.status_code == 200:
        data = response.json()
        for anime_list in data['data']['MediaListCollection']['lists']:
            entries = []
            for entry in anime_list['entries']:
                anime_data = {
                    'title': entry['media']['title']['romaji'],
                    'description': entry['media']['description'],
                    'image': entry['media']['coverImage']['medium'],
                    'status': entry['status'],
                    'progress': entry['progress']
                }
                entries.append(anime_data)

            anime_lists.append({'name': anime_list['name'], 'entries': entries})

    return render_template('index.html', anime_lists=anime_lists)


if __name__ == "__main__":
    app.run(debug=True)
