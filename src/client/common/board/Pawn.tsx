import { Color } from "csstype";
import * as React from "react";

export interface IProps {
    fillColor: Color;
    strokeColor: Color;
}

export const Pawn = (props: IProps) => {
    return (
        <svg viewBox="0 0 64 64" width="64" height="64">
        <g>
            <g>
                <path
                    d="M15.8,53.9c-0.4,0-0.8-0.3-0.8-0.8c0-8.9,5.2-14.3,9.4-16.2c-1.6-1.6-2.6-3.6-2.6-5.7
                    c0-2.8,1.6-5.3,4.1-6.9c-0.5-0.8-0.7-1.7-0.7-2.6c0-3,2.8-5.5,6.2-5.5s6.2,2.5,6.2,5.5c0,0.9-0.2,1.8-0.7,2.6
                    c2.6,1.6,4.1,4.2,4.1,6.9c0,2.2-0.9,4.2-2.6,5.7c4.2,1.9,9.4,7.3,9.4,16.2c0,0.4-0.3,0.8-0.8,0.8H15.8z"
                    fill={props.fillColor}
                    stroke={props.strokeColor}
                />
            </g>
        </g>
        </svg>
    );
};
