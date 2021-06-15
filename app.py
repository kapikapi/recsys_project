from svd_model import SvdRecommender
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    recs = []
    user = ''
    no_such_user = False
    if request.method == 'POST':
        user = request.form.get('user_id')
        num_recs = request.form.get('num_recs')
        
    elif request.method == 'GET':
        user = request.args.get('user_id')
        num_recs = request.args.get('num_recs')
    if num_recs:
        svd_rec = SvdRecommender()
        try:
            recs = svd_rec.predict(user, n_recs=int(num_recs))
        except KeyError:
            no_such_user = True
    
    return render_template("index.html", recs=recs, user=user, no_such_user=no_such_user)