import {cloneDeep} from "lodash";
import { DEFAULT_POSITION, IPosition } from "./domain";

/*
todo
- validate position
- calculate moves
- calculate captures
- 
*/

export default class Chess {
    private position: IPosition;

    constructor(position?: IPosition) {
        const initial = position == null ? {...DEFAULT_POSITION} : {...position};
        this.position = cloneDeep(initial);
    }
}
