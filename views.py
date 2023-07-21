
from flask import render_template, request, redirect, url_for
from app import app
from models import Bug

# Initialize the database connection
from models import db
db.init_app(app)

# Home page
@app.route('/')
def home():
    bugs = Bug.objects.order_by('-priority', 'status', '-id')
    return render_template('index.html', bugs=bugs)

# Bug details page
@app.route('/bug/<string:id>')
def bug_details(id):
    bug = Bug.objects.get_or_404(id=id)
    return render_template('bug_details.html', bug=bug)

# Create new bug report
@app.route('/create_bug', methods=['GET', 'POST'])
def create_bug():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        status = request.form['status']
        priority = int(request.form['priority'])
        
        bug = Bug(title=title, description=description, status=status, priority=priority)
        bug.save()
        return redirect(url_for('home'))
    
    return render_template('create_bug.html')

if __name__ == '__main__':
    app.run(debug=True)