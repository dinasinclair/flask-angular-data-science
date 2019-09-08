from flask import Flask, request, jsonify
from sklearn import svm
from sklearn import datasets
from sklearn.externals import joblib

# declare constants
HOST = '0.0.0.0'
PORT = 8081

# initialize flask application
app = Flask(__name__)

@app.route('/api/train', methods=['POST'])
def train():
    # get parameters from request
    parameters = request.get_json()

    # read iris data set
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    # fit model
    clf = svm.SVC(C=float(parameters['C']),
                 probability=True,
                 random_state=1)
    clf.fit(X, y)

    # persist model
    joblib.dump(clf, 'model.pkl')

    return jsonify({'accuracy': round(clf.score(X, y) * 100, 2)})


@app.route('/api/predict', methods=['POST'])
def predict():
    # get iris object from request
    X = request.get_json()
    print (X)
    iris_X = [[
        float(X['sepalLength']), 
        float(X['sepalWidth']), 
        float(X['petalLength']), 
        float(X['petalWidth'])
        ]]

    # loan_X = [[
    #     float(X['loan_amnt']),
    #     float(X['funded_amnt']),
    #     float(X['funded_amnt_inv']),
    #     float(X['installment']),
    #     float(X['annual_inc']),
    # ]]
# u'dti', u'delinq_2yrs',
#        u'inq_last_6mths', u'open_acc', u'pub_rec', u'revol_bal', u'total_acc',
#        u'out_prncp', u'out_prncp_inv', u'total_pymnt', u'total_pymnt_inv',
#        u'total_rec_prncp', u'total_rec_int', u'total_rec_late_fee',
#        u'last_pymnt_amnt', u'collections_12_mths_ex_med', u'policy_code',
#        u'acc_now_delinq', u'chargeoff_within_12_mths', u'delinq_amnt',
#        u'pub_rec_bankruptcies', u'tax_liens'],
#       dtype='object'
    # y_index = int(X['loanIndex'])
    # y = df.loc[df['index'] == X_index].values

    # read model
    clf = joblib.load('model.pkl')
    probabilities = clf.predict_proba(iris_X)

    # return jasonify([{'name': 'Paid-off', 'value': 17}])
    return jsonify([{'name': 'Iris-asdfasdfa', 'value': round(probabilities[0, 0] * 100, 2)},
                   {'name': 'Iris-Virginica', 'value': round(probabilities[0, 2] * 100, 2)}])


if __name__ == '__main__':
    # run web server
    app.run(host=HOST,
            debug=True,  # automatic reloading enabled
            port=PORT)
