export interface IOptions {
    recursive?: boolean;
    arrayRecursive?: boolean;
    throwOnDuplicate?: boolean;
}

export function camelKeys<T>(target: T, options?: IOptions): T;
export function camelArray<T>(target: Array<T>, options?: IOptions): Array<T>;