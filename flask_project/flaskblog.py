from flask import Flask,render_template

app = Flask(__name__)

lst =[
    {
        'author': 'Geeta',
        'title': 'Blog1',
        'content' : 'First Blog',
        'date_posted' : '12thAug'
    },
    {
        'author': 'Saurav',
        'title': 'Blog2 ',
        'content': '2nd Blog',
        'date_posted': '12thAug'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts =lst)

@app.route('/about')
def about():
    return render_template('about.html',title='About')

if __name__ == "__main__":
    app.run(debug =True)