from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("Home.html")

@app.route('/about')
def about():
    return render_template("About.html")

@app.route('/admin')
def admin():
    return render_template("Admin.html")

@app.route('/blogocean')
def blogocean():
    return render_template("Blog-ocean.html")

@app.route('/blogs')
def blogs():
    return render_template("Blogs.html")

@app.route('/newpost')
def newpost():
    return render_template("Newpost.html")

@app.route('/promotions')
def promotions():
    return render_template("Promotions.html")

@app.route('/themes')
def themes():
    return render_template("Themes.html")

@app.route('/themes_item')
def themes_item():
    return render_template("Subpage-themes.html")

if __name__=='__main__':
    app.run()