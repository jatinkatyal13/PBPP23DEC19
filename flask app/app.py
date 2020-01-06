from flask import Flask, render_template, request, redirect

app = Flask(__name__)

USERS = [
  {
    "name": "Jatin Katyal",
    "language": "Python",
    "college": "IPU"
  },
  {
    "name": "Himank",
    "language": "Node",
    "college": "IPU"
  },
  {
    "name": "Bipin Kalra",
    "language": "C++",
    "college": "DTU"
  },
  {
    "name": "Prateek Narang",
    "language": "C",
    "college": "IIT"
  },
]

@app.route('/')
def index():
  return "Hello World"

@app.route('/students')
def students():
  return render_template('students.html', students = USERS, enumerate = enumerate)

@app.route('/students/<int:id>')
def student(id):
  student = USERS[id - 1]
  return render_template('student.html', student=student)

@app.route('/students/new', methods = ['GET', 'POST'])
def student_new():
  if request.method == "POST":
    data = {
      "name": request.form.get("name"),
      "language": request.form.get("language"),
      "college": request.form.get("college")
    }
    USERS.append(data)
    return redirect('/students')

  return render_template('student_new.html')

@app.route('/profile')
def profile():
  # return render_template('profile.html',  first_name = 'Jatin', last_name = 'Katyal')
  return render_template('profile.html', user = USERS[0])

app.run(port = 8000, debug = True)
