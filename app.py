from flask import render_template, Flask, request
import pandas as pd

import users as u

# Create the application.
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html',users=u.users_list)

@app.route('/searchbyusername', methods=['POST'])
def searchByUsername():
    username = request.form['username']
    print("username ********",username)
    unpickled_df = pd.read_pickle("model/recommendation_model.pkl")
    model_result_df= unpickled_df[unpickled_df['userID']==username]
    product_name= list(model_result_df['prod_name'])
    products=product_name[0:5]

    return render_template('product-response.html', username=username, pro=products)

if __name__ == '__main__':
    app.run(debug=True)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080)