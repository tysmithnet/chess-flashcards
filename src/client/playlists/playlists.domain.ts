import { IRootState as IMasterListState } from "./master-list";
import { IRootState as IViewerState } from "./viewer";

export interface IRootState {
    masterList: IMasterListState;
    viewer: IViewerState;
}
