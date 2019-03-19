export interface IRootState {
    openingStats: IOpeningReportLine[];
}

export interface IOpeningReportLine {
    eco: number;
    name: string;
    date: Date;
    attempts: number;
    successes: number;
}
