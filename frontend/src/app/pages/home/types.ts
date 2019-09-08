export class Iris {
    sepalLength: number = 5.0;
    sepalWidth: number = 3.5;
    petalLength: number = 2.5;
    petalWidth: number = 1.2;
}

export class Loan {
    loan_amnt: number = 12;
    funded_amnt: number = 1235;
    funded_amnt_inv: number = 34;
    installment: number = 123;
    annual_inc: number = 1;
    dti: number = 12;
    delinq_2yrs: number = 0;
    inq_last_6mths: number = 0;
    open_acc: number = 0;
    pub_rec: number = 0;
    revol_bal: number = 0;
    total_acc: number = 0;
    out_prncp: number = 0;
    out_prncp_inv: number = 0;
    total_pymnt: number = 0;
    total_pymnt_inv: number = 0;
    total_rec_prncp: number = 0;
    total_rec_int: number = 0;
    total_rec_late_fee: number = 0;
    last_pymnt_amnt: number = 0;
    collections_12_mths_ex_med: number = 0;
    policy_code: number = 0;
    acc_now_delinq: number = 0;
    chargeoff_within_12_mths: number = 0;
    delinq_amnt: number = 0;
    pub_rec_bankruptcies: number = 0;
    tax_liens: number = 0;
}

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
