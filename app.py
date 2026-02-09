from rule_engine import recommend_domain, company_fit
from ml_engine import predict_domain_ml
from flask import Flask, render_template, request
from rule_engine import recommend_domain

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    profile = {
        "dsa": int(request.form['dsa']),
        "python": int(request.form['python']),
        "web": int(request.form['web']),
        "ml": int(request.form['ml']),
        "os": int(request.form['os']),
        "dbms": int(request.form['dbms']),
        "cgpa": float(request.form['cgpa'])
    }

    rule_result = recommend_domain(profile)
    companies = company_fit(rule_result["recommended_domain"])
    ml_result = predict_domain_ml(profile)

    # Calculate overall profile strength
    overall_score = (
        profile["dsa"] +
        profile["python"] +
        profile["web"] +
        profile["ml"] +
        profile["os"] +
        profile["dbms"]
    ) / 6

    overall_percentage = round((overall_score / 5) * 100, 1)

    return render_template(
    "result.html",
    rule_result=rule_result,
    ml_result=ml_result,
    overall_percentage=overall_percentage,
    companies=companies
)


if __name__ == '__main__':
    app.run(debug=True)
