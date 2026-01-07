from flask import Flask ,redirect,url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/hello/<Welcome>')
def hello_Welcome(Welcome):
   return 'Hello %s!' % Welcome 

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID
@app.route('/success/<int:score>')
def success(score):
   return "The person pass with the marks is" +str(score)  

@app.route('/fail/<int:score>')
def fail(score):
   return "The person fail with the marks is" +str(score)
#Test
@app.route('/results/<int:marks>')
def results(marks):
   result=""
   if marks>35:
      result='success'
   else:
      result='fail'
   return redirect(url_for(result,score=marks))


@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

if __name__ == '__main__':
   app.run(debug=True)