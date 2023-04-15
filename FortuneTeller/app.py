"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, request, render_template

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def index():
    """Renders a sample page."""
    return render_template('form.html')

@app.route("/fortune", methods=["POST"])
def fortune():
    user = request.form["user"]
    color = request.form["color"]
    number = request.form["number"]
    
    fortunes = {
        ("red", "1"): "You will have a great day!",
        ("red", "2"): "Good news is coming your way!",
        ("red", "3"): "You will meet someone special soon!",
        ("red", "4"): "Your hard work will pay off!",
        ("red", "5"): "Expect a pleasant surprise!",
        
        ("blue", "1"): "Your creative energy will be high today!",
        ("blue", "2"): "You will make a new friend soon!",
        ("blue", "3"): "A long-lost friend will contact you soon!",
        ("blue", "4"): "Your leadership skills will be in high demand!",
        ("blue", "5"): "You will achieve a major goal soon!",
        
        ("green", "1"): "You will have a peaceful day today!",
        ("green", "2"): "A major change is coming your way!",
        ("green", "3"): "You will learn something new today!",
        ("green", "4"): "You will receive a gift soon!",
        ("green", "5"): "You will find success in your career!",
        
        ("yellow", "1"): "Your financial situation will improve soon!",
        ("yellow", "2"): "You will have a lucky day today!",
        ("yellow", "3"): "You will have a great day to be outdoors!",
        ("yellow", "4"): "You will receive a phone call from someone important!",
        ("yellow", "5"): "Your dreams will come true soon!"
    }
    
    fortune = fortunes.get((color, number), "Sorry, I can't predict your fortune at this time.")
    
    return render_template("fortune.html", user=user, color=color, number=number, fortune=fortune)



if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
