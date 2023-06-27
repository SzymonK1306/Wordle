from flask import Flask, request, render_template
import random

app = Flask(__name__)

with open('words_eng.txt', 'r') as file:
    # Read the contents
    words = file.read()

# words = ['banana', 'cherry', 'orange']
words = words.split()
words = [word.lower() for word in words]
print(words)
selected_word = random.choice(words)
print(selected_word)
guessed_word = ['_'] * len(selected_word)

@app.route('/', methods=['GET', 'POST'])
def game():
    global guessed_word
    if request.method == 'POST':
        word = request.form['word']
        if word not in words:
            error = 'This word is not in the base.'
            return render_template('game.html', guessed_word=guessed_word, error=error)
        elif len(word) == len(selected_word):
            update_word(word)

        else:
            error = 'Please enter a word with the same length as the selected word.'
            return render_template('game.html', guessed_word=guessed_word, error=error)
    return render_template('game.html', guessed_word=guessed_word)

def update_word(word):
    global guessed_word
    colored_word = []
    for i in range(len(selected_word)):
        if selected_word[i] == word[i]:
            colored_word.append(f'<span style="color: green;">{word[i]}</span>')
        elif word[i] in selected_word:
            colored_word.append(f'<span style="color: orange;">{word[i]}</span>')
        else:
            colored_word.append(word[i])
    guessed_word[:] = colored_word

if __name__ == '__main__':
    app.run(debug=True)
