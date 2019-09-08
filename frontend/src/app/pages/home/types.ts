export class Iris {
    sepalLength: number = 5.0;
    sepalWidth: number = 3.5;
    petalLength: number = 2.5;
    petalWidth: number = 1.2;
}

export class Loan {
    loanAmount: number = 12;
    fundedAmount: number = 1235;
    fundedAmountInvestors: number = 34;
    installment: number = 123;
}

// 'loan_amnt', u'funded_amnt', u'funded_amnt_inv',
//        u'installment', u'annual_inc', u'dti', u'delinq_2yrs',
//        u'inq_last_6mths', u'open_acc', u'pub_rec', u'revol_bal', u'total_acc',
//        u'out_prncp', u'out_prncp_inv', u'total_pymnt', u'total_pymnt_inv',
//        u'total_rec_prncp', u'total_rec_int', u'total_rec_late_fee',
//        u'last_pymnt_amnt', u'collections_12_mths_ex_med', u'policy_code',
//        u'acc_now_delinq', u'chargeoff_within_12_mths', u'delinq_amnt',
//        u'pub_rec_bankruptcies', u'tax_liens'

export class ProbabilityPrediction {
    name: string;
    value: number;
}

export class SVCParameters {
    C: number = 2.0;
}

export class SVCResult {
    accuracy: number;
}
