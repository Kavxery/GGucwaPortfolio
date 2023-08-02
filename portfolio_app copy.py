


from flask import Flask, render_template

app = Flask(__name__)

# Sample portfolio data
portfolio_data = {
    "name": "Gabriela Gucwa",
    "title": "GGucwaPortfolio",
    "about": "Welcome to my digital portfolio. I am a young girl with a special interest in the mathematical world and it's artistic impact on our human minds.",
    "projects": [
        {
            "title": "Project 1",
            "description": "A brief description of Project 1.",
            "image": "project1.jpg"
        },
        {
            "title": "Project 2",
            "description": "A brief description of Project 2.",
            "image": "project2.jpg"
        },
        # Add more projects here
    ],
    "contact": {
        "email": "GGucwa.art@yahoo.com",
        "phone": "919 10 219",
        "github": "https://github.com/yourusername/"
    }
}

@app.route('/')
def home():
    return render_template('index.html', data=portfolio_data)

@app.route('/about')
def about():
    return render_template('about.html', data=portfolio_data)

@app.route('/contact')
def contact():
    return render_template('contact.html', data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True)
