import { Component, OnInit } from "@angular/core";
import { IrisService } from "./iris.service";
import { LoanService } from "./loan.service";
import {
    Iris,
    Loan,
    ProbabilityPrediction,
    SVCParameters,
    SVCResult,
} from "./types";

@Component({
    selector: "home",
    templateUrl: "./home.component.html",
    styleUrls: ["./home.component.scss"],
})
export class HomeComponent implements OnInit {
    public svcParameters: SVCParameters = new SVCParameters();
    public svcResult: SVCResult;
    public iris: Iris = new Iris();
    public loan: Loan = new Loan();
    public probabilityPredictions: ProbabilityPrediction[];

    // graph styling
    public colorScheme = {
        domain: ["#1a242c", "#e81746", "#e67303", "#f0f0f0"],
    };

    constructor(
        private irisService: IrisService,
        private loanService: LoanService,
    ) {}

    ngOnInit() {}

    public trainModel() {
        this.irisService.trainModel(this.svcParameters).subscribe(svcResult => {
            this.svcResult = svcResult;
        });
    }

    public predictIris() {
        this.irisService
            .predictIris(this.iris)
            .subscribe(probabilityPredictions => {
                this.probabilityPredictions = probabilityPredictions;
            });
    }

    public predictLoan() {
        this.loanService
            .predictLoan(this.loan)
            .subscribe(probabilityPredictions => {
                this.probabilityPredictions = probabilityPredictions;
            });
    }
}
