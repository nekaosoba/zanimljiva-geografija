app = Flask(__name__, template_folder='templates')
from flask import Flask, render_template, request
from threading import Timer

app = Flask(__name__)

players = {
    'player1': {
        'answers': {},
        'score': 0
    },
    'player2': {
        'answers': {},
        'score': 0
    }
}

categories = ['Država', 'Grad', 'Reka', 'Planina', 'Biljka', 'Životinja']

time_limit = 180  # Vrijeme u sekundama

def calculate_scores():
    for player in players.values():
        score = 0
        for answer in player['answers'].values():
            if answer:
                score += 1
        player['score'] = score

def display_results():
    calculate_scores()
    print("Rezultati:")
    for player, data in players.items():
        print(f"Igrač {player}:")
        for category, answer in data['answers'].items():
            print(f"{category}: {answer}")
        print(f"Broj poena: {data['score']}")
        print("")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        category = request.form['category']
        player1_answer = request.form['player1-answer']
        player2_answer = request.form['player2-answer']
        players['player1']['answers'][category] = player1_answer
        players['player2']['answers'][category] = player2_answer
        return render_template('index.html', categories=categories)
    return render_template('index.html', categories=categories)

@app.route('/results', methods=['GET', 'POST'])
def results():
    calculate_scores()
    if request.method == 'POST':
        players['player1']['score'] = int(request.form['player1-score'])
        players['player2']['score'] = int(request.form['player2-score'])
    return render_template('results.html', players=players)

if __name__ == '__main__':
    timer = Timer(time_limit, display_results)
    timer.start()
    app.run(host='0.0.0.0', port=5000)
