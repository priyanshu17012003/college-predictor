from flask import Flask, render_template, request
from CollegeAllotment import algorithms
from CollegeAllotment import college_links
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/exam')
def exam():
    return render_template('exam.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')


@app.route('/predictCollege')
def predictCollege():
    return render_template("predictCollege.html")

@app.route('/results', methods=['GET', 'POST'])
@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        marks = request.form['marks']
        algorithm = request.form['algo']
        caste = request.form['caste']
        c = algorithms()

        if algorithm == "KNN":
            college_info = c.predictKNN_with_links(marks, caste)
            return render_template("results.html", colleges=[college_info])
        elif algorithm == "SVM":
            college = c.predictSVM(marks, caste)
            college_info = {"name": college, "cutoff": "NA", "url": college_links.get(college, 'Website not found')}
            return render_template("results.html", colleges=[college_info])

    return render_template("results.html", colleges=None)




@app.route('/colleges')
def colleges():
    return render_template("colleges.html")

@app.route('/web')
def web():
    return render_template("web.html")

@app.route('/Devops')
def Devops():
    return render_template("Devops.html")

@app.route('/Python')
def Python():
    return render_template("Python.html")

@app.route('/Math')
def Math():
    return render_template("Math.html")

@app.route('/sortedResults')
def sortedResults():
    start = float(request.args.get('minpercentage'))
    end = float(request.args.get('maxpercentage'))
    results = int(request.args.get('results'))
    caste = str(request.args.get('caste'))
    branch = str(request.args.get('branch'))
    c = algorithms()
    my_list = c.get_by_range(start, end, results, caste,branch)
    # return render_template("sortedResults.html", my_list=my_list, size=len(my_list))
    return render_template("sortedResults.html", my_list=my_list, size=len(my_list), college_links=college_links)
if __name__ == '__main__':
    app.debug = True
    app.run()


