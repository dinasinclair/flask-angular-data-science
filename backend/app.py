from flask import Flask, request, jsonify
from sklearn import svm
from sklearn import datasets
from sklearn.externals import joblib

# declare constants
HOST = '0.0.0.0'
PORT = 8081

# initialize flask application
app = Flask(__name__)

# @app.route('/api/train', methods=['POST'])
# def train():
#     # get parameters from request
#     parameters = request.get_json()

#     # read iris data set
#     iris = datasets.load_iris()
#     X, y = iris.data, iris.target

#     # fit model
#     clf = svm.SVC(C=float(parameters['C']),
#                  probability=True,
#                  random_state=1)
#     clf.fit(X, y)

#     # persist model
#     joblib.dump(clf, 'model.pkl')

#     return jsonify({'accuracy': round(clf.score(X, y) * 100, 2)})


@app.route('/api/predict', methods=['POST'])
def predict():
    # get iris object from request
    X = request.get_json()
    print(X, flush=True)
    # iris_X = [[
    #     float(X['sepalLength']), 
    #     float(X['sepalWidth']), 
    #     float(X['petalLength']), 
    #     float(X['petalWidth'])
    #     ]]
    # clf = joblib.load('model.pkl')
    # probabilities = clf.predict_proba(iris_X)

    loan_X = [[
        float(X['loan_amnt']),
        float(X['funded_amnt']),
        float(X['funded_amnt_inv']),
        float(X['installment']),
        float(X['annual_inc']),
        float(X['dti']),
        float(X['delinq_2yrs']),
        float(X['inq_last_6mths']),
        float(X['open_acc']),
        float(X['pub_rec']),
        float(X['revol_bal']),
        float(X['total_acc']),
        float(X['out_prncp']),
        float(X['out_prncp_inv']),
        float(X['total_pymnt']),
        float(X['total_pymnt_inv']),
        float(X['total_rec_prncp']),
        float(X['total_rec_late_fee']),
        float(X['last_pymnt_amnt']),
        float(X['collections_12_mths_ex_med']),
        float(X['total_rec_prncp']),
        float(X['acc_now_delinq']),
        float(X['chargeoff_within_12_mths']),
        float(X['total_pymnt']),
        float(X['delinq_amnt']),
        float(X['pub_rec_bankruptcies']),
        float(X['tax_liens']),
    ]]

    # read model
    clf = joblib.load('numeric_loan_forest.pkl')
    prediction = clf.predict(loan_X)
    print(prediction, flush=True)
    

    # return jasonify([{'name': 'Paid-off', 'value': 17}])
    # return jsonify([{'name': 'prediction', 'value': prediction[0]}
    #                ])
    return str(prediction)

if __name__ == '__main__':
    # run web server
    app.run(host=HOST,
            debug=True,  # automatic reloading enabled
            port=PORT)
