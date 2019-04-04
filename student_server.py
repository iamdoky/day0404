from flask import Flask,render_template,request
from day0404 import func0404

app = Flask(__name__)

@app.route('/students',methods=['GET','POST'])
def students():
    names = ''
    fname = ''
    msg = ''
    if request.method == 'POST':
        names = request.form['names']
        fname = func0404.students(names)
        if fname == 'no':
            msg = "사용자 이름이 없음"
    return render_template('students.html',names=names,fname= fname,msg=msg)

if __name__ == '__main__':
    app.run(debug=True, host='203.236.209.95')
