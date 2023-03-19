import requests
from flask import Flask, render_template, request
from mplsoccer import VerticalPitch
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from config import API_KEY

app = Flask(__name__)

headers = {
    'x-rapidapi-host': "api-football-beta.p.rapidapi.com",
    'x-rapidapi-key': API_KEY
}
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the player name from the form
        player_name = request.form['player']

        # Call the API to get the player ID and statistics
        url = f'https://api-football-beta.p.rapidapi.com/players?search={player_name}&league=39&season=2022'
        response = requests.get(url, headers=headers)
        data = response.json()

        # Extract statistics from the API response
        if data['results'] > 0:
            player_position = data['response'][0]['statistics'][0]['games']['position']
            stats = data['response'][0]['statistics'][0]
            if player_position == 'Attacker':
                stat_per_match = stats['goals']['total'] / stats['games']['appearences']
                stat_label = 'Buts par match'
            elif player_position == 'Midfielder':
                stat_per_match = stats['goals']['assists'] / stats['games']['appearences']
                stat_label = 'Passes décisives par match'
            elif player_position == 'Defender':
                stat_per_match = stats['tackles']['total'] / stats['games']['appearences']
                stat_label = 'Tacles par match'

            # Extract the player information from the API response
            player_info = {
                'Goals': data['response'][0]['statistics'][0]['goals']['total'],
                'Assists': data['response'][0]['statistics'][0]['goals']['assists'],
                'Name': data['response'][0]['player']['name'],
                'Nationality': data['response'][0]['player']['nationality'],
                'Age': data['response'][0]['player']['age'],
                'Height': data['response'][0]['player']['height'],
                'Weight': data['response'][0]['player']['weight'],
                'Team': data['response'][0]['statistics'][0]['team']['name']
            }

            # Get the player photo from the API
            photo_url = data['response'][0]['player']['photo']
            photo_response = requests.get(photo_url)
            photo_data = photo_response.content

            # Save the player photo as a PNG file
            with open('static/photo.png', 'wb') as f:
                f.write(photo_data)


            # Create a mplsoccer plot of the player statistics
            pitch = VerticalPitch(pitch_type='opta', pitch_color='#22312b', line_color='white')
            fig, ax = pitch.draw()

            # Add player position to the plot
            if player_position == 'Attacker':
                pitch.annotate("AT", xy=(80, 50), fontsize=20, ha='center', va='center', color='red',ax=ax)
            elif player_position == 'Midfielder':
                pitch.annotate("MID", xy=(50, 50), fontsize=20, ha='center', va='center', color='red',ax=ax)
            elif player_position == 'Defender':
                pitch.annotate("DEF", xy=(20, 50), fontsize=20, ha='center', va='center', color='red',ax=ax)

            plt.title(f"Statistiques pour {player_name}")
            plt.savefig('static/stats.png')

            # Render the result page with the player information, photo, and plot image
            return render_template('result.html', player_info=player_info, photo=photo_data, stat_label=stat_label,stat_per_match=stat_per_match)

        # Render the error page if the player was not found in the API
        if data['results'] == 0:
            return render_template('error.html', player_name=player_name)

     #Render the home page if the request method is GET
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,port =5002)