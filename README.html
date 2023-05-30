# zanimljiva-geografija
from flask import Flask, render_template, request
from threading import Timer

app = Flask(__name__)

player1_answers = {}
player2_answers = {}
time_limit = 180  # Vrijeme u sekundama

def display_results():
    print("Rezultati:")
    print("Igrač 1:")
    for category, answer in player1_answers.items():
        print(f"{category}: {answer}")
    print("Igrač 2:")
    for category, answer in player2_answers.items():
        print(f"{category}: {answer}")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        category = request.form['category']
        player1_answer = request.form['player1-answer']
        player2_answer = request.form['player2-answer']
        player1_answers[category] = player1_answer
        player2_answers[category] = player2_answer
        return render_template('index.html', category=category)
    return render_template('index.html')

if __name__ == '__main__':
    timer = Timer(time_limit, display_results)
    timer.start()
    app.run()
