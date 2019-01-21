import { Color } from "csstype";
import * as React from "react";

export interface IProps {
    fillColor: Color;
    strokeColor: Color;
}

export const Bishop = (props: IProps) => {
    return (
        <svg viewBox="0 0 64 64" width="64" height="64">
            <g>
                <path
                    d="M14.7,49.8c4.2-1.2,12.6,0.5,16.8-2.5c4.2,3.1,12.6,1.3,16.8,2.5c0,0,2,0.7,3.7,2.5
                    c-0.8,1.2-2,1.3-3.7,0.6c-4.2-1.2-12.6,0.6-16.8-1.3c-4.2,1.9-12.6,0-16.8,1.3c-1.7,0.6-2.9,0.6-3.7-0.6
                    C12.7,49.8,14.7,49.8,14.7,49.8z"
                    fill={props.fillColor}
                    stroke={props.strokeColor}
                />
                <path
                    d="M22.2,44.6c3.1,3.2,15.5,3.2,18.6,0c0.6-1.9,0-2.5,0-2.5c0-3.2-3.1-5.2-3.1-5.2
                    c6.8-1.9,7.5-14.8-6.2-20c-13.7,5.2-13,18-6.2,20c0,0-3.1,1.9-3.1,5.2C22.2,42,21.6,42.7,22.2,44.6z"
                    fill={props.fillColor}
                    stroke={props.strokeColor}
                />
                <path
                    d="M34.6,13.7c0,1.8-1.4,3.2-3.1,3.2s-3.1-1.4-3.1-3.2s1.4-3.2,3.1-3.2
                    C33.2,10.4,34.6,12,34.6,13.7z"
                    fill={props.fillColor}
                    stroke={props.strokeColor}
                />
            </g>
            <path
                d="M25.3,36.9h12.4 M22.2,42h18.6 M31.5,23.3v6.4 M28.4,26.6h6.2"
                fill={props.fillColor}
                stroke={props.strokeColor}
            />
        </svg>
    );
};

export const Knight = (props: IProps) => {
    return (
        <svg viewBox="0 0 64 64" width="64" height="64">
            <g>
                <path
                    d="M32,14.4c0,0,0-4-1.4-4c-2.3,1.4-3.4,4-3.4,4h-2.7c0,0-2.7-4.7-4.1-3.3c0,1.3-0.3,2.7,0.7,4
                    c-0.1,2.1-2.7,4.7-2.7,4.7s-8.1,13.4-8.1,16.1c0,6.7,4.1,5.4,5.4,5.4c1.6-1,0-2.7,1.4-2.7c1.9-0.1-1.4,2.8,0,4
                    c3,0.5,2.7-2.7,6.8-5.4c2.5-1.6,7.6-5.4,9.8-8.8c0.8,15.8-11.1,13.5-11.1,24.8h31.1C54.3,25.1,46.2,15.7,32,14.4z M14.4,35.8
                    c-0.4,0-0.7-0.3-0.7-0.7c0-0.4,0.3-0.7,0.7-0.7s0.7,0.3,0.7,0.7C15.1,35.5,14.8,35.8,14.4,35.8z M22.4,22.1
                    c-0.6,1-1.3,1.6-1.6,1.4c-0.3-0.2-0.1-1.1,0.4-2.1c0.6-1,1.3-1.6,1.6-1.4C23.2,20.2,23,21.1,22.4,22.1z"
                    fill={props.fillColor}
                    stroke={props.strokeColor}
                />
                <path
                    d="M15.1,35.1c0,0.4-0.3,0.7-0.7,0.7s-0.7-0.3-0.7-0.7c0-0.4,0.3-0.7,0.7-0.7 S15.1,34.7,15.1,35.1z"
                    fill={props.fillColor}
                    stroke={props.strokeColor}
                />
                <path
                    d="M22.4,22.1c-0.6,1-1.3,1.6-1.6,1.4c-0.3-0.2-0.1-1.1,0.4-2.1c0.6-1,1.3-1.6,1.6-1.4 C23.2,20.2,23,21.1,22.4,22.1z"
                    fill={props.fillColor}
                    stroke={props.strokeColor}
                />
                <path
                    d="M15.1,35.1c0,0.4-0.3,0.7-0.7,0.7s-0.7-0.3-0.7-0.7c0-0.4,0.3-0.7,0.7-0.7 S15.1,34.7,15.1,35.1z"
                    fill={props.fillColor}
                    stroke={props.strokeColor}
                />
                <path
                    d="M22.4,22.1c-0.6,1-1.3,1.6-1.6,1.4c-0.3-0.2-0.1-1.1,0.4-2.1c0.6-1,1.3-1.6,1.6-1.4 C23.2,20.2,23,21.1,22.4,22.1z"
                    fill={props.fillColor}
                    stroke={props.strokeColor}
                />
            </g>
        </svg>
    );
};

export const Pawn = (props: IProps) => {
    return (
        <svg viewBox="0 0 64 64" width="64" height="64">
            <path
                d="M15.8,53.9c-0.4,0-0.8-0.3-0.8-0.8c0-8.9,5.2-14.3,9.4-16.2c-1.6-1.6-2.6-3.6-2.6-5.7
                c0-2.8,1.6-5.3,4.1-6.9c-0.5-0.8-0.7-1.7-0.7-2.6c0-3,2.8-5.5,6.2-5.5s6.2,2.5,6.2,5.5c0,0.9-0.2,1.8-0.7,2.6
                c2.6,1.6,4.1,4.2,4.1,6.9c0,2.2-0.9,4.2-2.6,5.7c4.2,1.9,9.4,7.3,9.4,16.2c0,0.4-0.3,0.8-0.8,0.8H15.8z"
                fill={props.fillColor}
                stroke={props.strokeColor}
            />
        </svg>
    );
};
