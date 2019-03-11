interface IOptions {
    emptyArrays?: boolean;
    emptyObjects?: boolean;
    emptyStrings?: boolean;
    nullValues?: boolean;
    undefinedValues?: boolean;
}
declare function cleanDeep(thing: any, options: IOptions): any;
export = cleanDeep;
