from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Cameroon',
    'salary': '500000frs'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Nigeria',
    'salary': '600000frs'
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': '450000frs'
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'America',
    'salary': '$700,000'
}]


@app.route('/')
def hello_worls():
  return render_template('home.html', jobs=JOBS, company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
