import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import { Observable } from "rxjs/Observable";
import "rxjs/add/operator/map";
import {
    LoanIndex,
    ProbabilityPrediction,
    SVCParameters,
    SVCResult,
} from "./types";

const SERVER_URL: string = "api/";

@Injectable()
export class LoanIndexService {
    constructor(private http: Http) {}

    public trainModel(svcParameters: SVCParameters): Observable<SVCResult> {
        return this.http
            .post(`${SERVER_URL}train`, svcParameters)
            .map(res => res.json());
    }

    public predictLoanIndex(
        loanIndex: LoanIndex,
    ): Observable<ProbabilityPrediction[]> {
        return this.http
            .post(`${SERVER_URL}predict`, loanIndex)
            .map(res => res.json());
    }
}
