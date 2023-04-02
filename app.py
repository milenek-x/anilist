from flask import Flask, render_template
import requests

app = Flask(__name__)

access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImUxYzYzNmZjMTE1NjU5MjJiZmVhODljYjQwYjQ3ZGU5MTA1YzhiNWM2OTE2YjM1NmZlMzNmZWIyYTBjYjU0ZGEyMDE4NGZmNjA5NGYyMDIwIn0.eyJhdWQiOiIxMTkzNyIsImp0aSI6ImUxYzYzNmZjMTE1NjU5MjJiZmVhODljYjQwYjQ3ZGU5MTA1YzhiNWM2OTE2YjM1NmZlMzNmZWIyYTBjYjU0ZGEyMDE4NGZmNjA5NGYyMDIwIiwiaWF0IjoxNjgwNDEwMTU5LCJuYmYiOjE2ODA0MTAxNTksImV4cCI6MTcxMjAzMjU1OSwic3ViIjoiNTM1ODA4Iiwic2NvcGVzIjpbXX0.HmQ5LPWIWj9kUz0d4-tv6rYHJyqPmVZhuYzcLG-nrBjVEV8bimdEn3hgUnEn4OvYyo0pHgbrdVWBX1Tmxe-LV8nwS6wrLHBavGMvyCeQO27J1p5DsgatkU_p6poe7TcUf49SJ67BBBKM1APWo6YqO9voKqJlGEJwEM4vMuEno3t-kzeHnOoGPgh0xR2X2C5mc0ZW-G6mgD-h0urafEMlsdo8TD5w7CkTHtTK_8e8vjPi4HMQomTGGPJ51JCUJC_jArZdYIeHpUqhcg0BcslN1-7qzqpF-jVpQlJR0bvXnGYAaucrSUCfIiTi0TMup-r2oN3wadLgk53ofxJOHan07nOSZJ4l6mMmmKcUvHfiu2TwF-1x9szDgWZOn4oJQzMtQEShyQZdHlwSFjqCHd_ZKlx-vco1typ2_COoQwLJ6oFaq2krJdoBXhYc-yw75YfFRZnDm9e9j8VtfVxYgSoQ1h9MO0xfJmZSdNY1EWPSUgqka0z2rXchWzf_P6USYI_EzBQWvlFAhfQrYriiJ5we8H0cEI5RSyuCSumB1ZeuL5iHz7NJfuHL4QeiVI07gxqlD4ffzWx0zK54XiPclie2EduJyc7jaGh5n4RyouFZeE5hAtXbMD7OHhQwy2dg20UJl7BRL6h6z21WBVg5tVpqrQC9Oebu0_kfT83QLm3X0Oo"

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
        "userName": "milenekx"
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
