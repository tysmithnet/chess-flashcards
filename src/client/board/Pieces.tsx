import { Color } from "csstype";
import * as React from "react";

export interface IProps {
    dataSrc: string; // a1..h8
    fillColor: Color;
    strokeColor: Color;
    onMouseDown?: React.MouseEventHandler<SVGElement>;
    onMouseMove?: React.MouseEventHandler<SVGElement>;
    x: number;
    y: number;
}

export class King extends React.Component<IProps> {
    public render() {
        return (
        <svg viewBox="0 0 64 64" width="64" height="64" x={this.props.x} y={this.props.y} data-src={this.props.dataSrc}>
            <path
                d="M31.5,17.6v-7.2"
                opacity={1}
                fill={this.props.fillColor}
                fillOpacity={1}
                fillRule="nonzero"
                stroke={this.props.strokeColor}
                strokeWidth={1.5}
                strokeLinecap="round"
                strokeLinejoin="miter"
                strokeMiterlimit={4}
                strokeDasharray="none"
                strokeOpacity={1}
            />
            <path
                d="M28.3,13h6.4"
                opacity={1}
                fill={this.props.fillColor}
                fillOpacity={1}
                fillRule="nonzero"
                stroke={this.props.strokeColor}
                strokeWidth={1.5}
                strokeLinecap="round"
                strokeLinejoin="miter"
                strokeMiterlimit={4}
                strokeDasharray="none"
                strokeOpacity={1}
            />
            <path
                d="M31.5,34.6c0,0,5.7-9.5,3.8-13.3c0,0-1.3-3.2-3.8-3.2s-3.8,3.2-3.8,3.2
                C25.8,25.1,31.5,34.6,31.5,34.6"
                opacity={1}
                fill={this.props.fillColor}
                fillOpacity={1}
                fillRule="nonzero"
                stroke={this.props.strokeColor}
                strokeWidth={1.5}
                strokeLinecap="round"
                strokeLinejoin="miter"
                strokeMiterlimit={4}
                strokeDasharray="none"
                strokeOpacity={1}
            />
            <path
                d="M17.5,49.8c7,4.4,19.7,4.4,26.7,0v-8.9c0,0,11.4-5.7,7.6-13.3c-5.1-8.3-17.2-4.4-20.3,5.1v4.4
                v-4.4c-4.4-9.5-16.5-13.3-20.3-5.1c-3.8,7.6,6.4,12.7,6.4,12.7V49.8z"
                opacity={1}
                fill={this.props.fillColor}
                fillOpacity={1}
                fillRule="nonzero"
                stroke={this.props.strokeColor}
                strokeWidth={1.5}
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeMiterlimit={4}
                strokeDasharray="none"
                strokeOpacity={1}
            />
            <path
                d="M17.5,40.9c7-3.8,19.7-3.8,26.7,0"
                opacity={1}
                fill={this.props.fillColor}
                fillOpacity={1}
                fillRule="nonzero"
                stroke={this.props.strokeColor}
                strokeWidth={1.5}
                strokeLinecap="round"
                strokeLinejoin="miter"
                strokeMiterlimit={4}
                strokeDasharray="none"
                strokeOpacity={1}
            />
            <path
                d="M17.5,45.4c7-3.8,19.7-3.8,26.7,0"
                opacity={1}
                fill={this.props.fillColor}
                fillOpacity={1}
                fillRule="nonzero"
                stroke={this.props.strokeColor}
                strokeWidth={1.5}
                strokeLinecap="round"
                strokeLinejoin="miter"
                strokeMiterlimit={4}
                strokeDasharray="none"
                strokeOpacity={1}
            />
            <path
                d="M17.5,49.8c7-3.8,19.7-3.8,26.7,0"
                opacity={1}
                fill={this.props.fillColor}
                fillOpacity={1}
                fillRule="nonzero"
                stroke={this.props.strokeColor}
                strokeWidth={1.5}
                strokeLinecap="round"
                strokeLinejoin="miter"
                strokeMiterlimit={4}
                strokeDasharray="none"
                strokeOpacity={1}
            />
            </svg>
        );
    }
}
export class Queen extends React.Component<IProps> {
    public render() {
        return (
        <svg viewBox="0 0 64 64" width="64" height="64" x={this.props.x} y={this.props.y} data-src={this.props.dataSrc}>
            <path
                d="M13.3,19.3c0,1.4-1.1,2.5-2.5,2.5s-2.5-1.1-2.5-2.5c0-1.4,1.1-2.5,2.5-2.5
                S13.3,17.9,13.3,19.3z"
                opacity={1}
                fill={this.props.fillColor}
                fillOpacity={1}
                fillRule="nonzero"
                stroke={this.props.strokeColor}
                strokeWidth={1.5}
                strokeLinecap="round"
                strokeLinejoin="miter"
                strokeMiterlimit={4}
                strokeDasharray="none"
                strokeOpacity={1}
            />
            <path
                d="M34,13.7c0,1.4-1.1,2.5-2.5,2.5c-1.4,0-2.5-1.1-2.5-2.5s1.1-2.5,2.5-2.5
                C32.9,11.2,34,12.3,34,13.7z"
                opacity={1}
                fill={this.props.fillColor}
                fillOpacity={1}
                fillRule="nonzero"
                stroke={this.props.strokeColor}
                strokeWidth={1.5}
                strokeLinecap="round"
                strokeLinejoin="miter"
                strokeMiterlimit={4}
                strokeDasharray="none"
                strokeOpacity={1}
            />
            <path
                d="M54.7,19.3c0,1.4-1.1,2.5-2.5,2.5c-1.4,0-2.5-1.1-2.5-2.5c0-1.4,1.1-2.5,2.5-2.5
                C53.6,16.8,54.7,17.9,54.7,19.3z"
                opacity={1}
                fill={this.props.fillColor}
                fillOpacity={1}
                fillRule="nonzero"
                stroke={this.props.strokeColor}
                strokeWidth={1.5}
                strokeLinecap="round"
                strokeLinejoin="miter"
                strokeMiterlimit={4}
                strokeDasharray="none"
                strokeOpacity={1}
            />
            <path
                d="M23.4,15c0,1.4-1.1,2.5-2.5,2.5s-2.5-1.1-2.5-2.5c0-1.4,1.1-2.5,2.5-2.5S23.4,13.6,23.4,15z"
                opacity={1}
                fill={this.props.fillColor}
                fillOpacity={1}
                fillRule="nonzero"
                stroke={this.props.strokeColor}
                strokeWidth={1.5}
                strokeLinecap="round"
                strokeLinejoin="miter"
                strokeMiterlimit={4}
                strokeDasharray="none"
                strokeOpacity={1}
            />
            <path
                d="M44.7,15.6c0,1.4-1.1,2.5-2.5,2.5c-1.4,0-2.5-1.1-2.5-2.5s1.1-2.5,2.5-2.5
                C43.5,13.1,44.7,14.2,44.7,15.6z"
                opacity={1}
                fill={this.props.fillColor}
                fillOpacity={1}
                fillRule="nonzero"
                stroke={this.props.strokeColor}
                strokeWidth={1.5}
                strokeLinecap="round"
                strokeLinejoin="miter"
                strokeMiterlimit={4}
                strokeDasharray="none"
                strokeOpacity={1}
            />
            <path
                d="M14.6,36.7c10.6-1.9,26.3-1.9,33.8,0l2.5-14.9l-8.8,13.7V18.1l-6.9,16.8l-3.8-18.6l-3.8,18.6
                l-6.9-17.4v18l-8.8-13.7L14.6,36.7z"
                opacity={1}
                fill={this.props.fillColor}
                fillOpacity={1}
                fillRule="nonzero"
                stroke={this.props.strokeColor}
                strokeWidth={1.5}
                strokeLinecap="round"
                strokeLinejoin="miter"
                strokeMiterlimit={4}
                strokeDasharray="none"
                strokeOpacity={1}
            />
            <path
                d="M14.6,36.7c0,2.5,1.9,2.5,3.1,5c1.3,1.9,1.3,1.2,0.6,4.3c-1.9,1.2-1.9,3.1-1.9,3.1
                c-1.9,1.9,0.6,3.1,0.6,3.1c8.1,1.2,20.7,1.2,28.8,0c0,0,1.9-1.2,0-3.1c0,0,0.6-1.9-1.3-3.1c-0.6-3.1-0.6-2.5,0.6-4.3
                c1.3-2.5,3.1-2.5,3.1-5C37.8,34.8,25.2,34.8,14.6,36.7z"
                opacity={1}
                fill={this.props.fillColor}
                fillOpacity={1}
                fillRule="nonzero"
                stroke={this.props.strokeColor}
                strokeWidth={1.5}
                strokeLinecap="round"
                strokeLinejoin="miter"
                strokeMiterlimit={4}
                strokeDasharray="none"
                strokeOpacity={1}
            />
            <path
                d="M17.7,41.7c4.4-1.2,23.2-1.2,27.6,0"
                opacity={1}
                fill={this.props.fillColor}
                fillOpacity={1}
                fillRule="nonzero"
                stroke={this.props.strokeColor}
                strokeWidth={1.5}
                strokeLinecap="round"
                strokeLinejoin="miter"
                strokeMiterlimit={4}
                strokeDasharray="none"
                strokeOpacity={1}
            />
            <path
                d="M18.3,46c7.5-1.2,18.8-1.2,26.3,0"
                opacity={1}
                fill={this.props.fillColor}
                fillOpacity={1}
                fillRule="nonzero"
                stroke={this.props.strokeColor}
                strokeWidth={1.5}
                strokeLinecap="round"
                strokeLinejoin="miter"
                strokeMiterlimit={4}
                strokeDasharray="none"
                strokeOpacity={1}
            />
        </svg>
        );
    }
}
export class Rook extends React.Component<IProps> {
    public render() {
        return (
        <svg viewBox="0 0 64 64" width="64" height="64" x={this.props.x} y={this.props.y} data-src={this.props.dataSrc}>
            <path
                d="M12.8,53.2h37.5v-3.9H12.8V53.2z"
                opacity={1}
                fill={this.props.fillColor}
                fillOpacity={1}
                fillRule="nonzero"
                stroke={this.props.strokeColor}
                strokeWidth={1.5}
                strokeLinecap="round"
                strokeLinejoin="miter"
                strokeMiterlimit={4}
                strokeDasharray="none"
                strokeOpacity={1}
            />
            <path
                d="M16.9,49.2V44h29.1v5.2H16.9z"
                opacity={1}
                fill={this.props.fillColor}
                fillOpacity={1}
                fillRule="nonzero"
                stroke={this.props.strokeColor}
                strokeWidth={1.5}
                strokeLinecap="round"
                strokeLinejoin="miter"
                strokeMiterlimit={4}
                strokeDasharray="none"
                strokeOpacity={1}
            />
            <path
                d="M15.5,20.4v-6.6h5.6v2.6H28v-2.6H35v2.6h6.9v-2.6h5.6v6.6"
                opacity={1}
                fill={this.props.fillColor}
                fillOpacity={1}
                fillRule="nonzero"
                stroke={this.props.strokeColor}
                strokeWidth={1.5}
                strokeLinecap="round"
                strokeLinejoin="miter"
                strokeMiterlimit={4}
                strokeDasharray="none"
                strokeOpacity={1}
            />
            <path
                d="M47.5,20.4l-4.2,3.9H19.7l-4.2-3.9"
                opacity={1}
                fill={this.props.fillColor}
                fillOpacity={1}
                fillRule="nonzero"
                stroke={this.props.strokeColor}
                strokeWidth={1.5}
                strokeLinecap="round"
                strokeLinejoin="miter"
                strokeMiterlimit={4}
                strokeDasharray="none"
                strokeOpacity={1}
            />
            <path
                d="M43.3,24.3v16.4H19.7V24.3"
                opacity={1}
                fill={this.props.fillColor}
                fillOpacity={1}
                fillRule="nonzero"
                stroke={this.props.strokeColor}
                strokeWidth={1.5}
                strokeLinecap="round"
                strokeLinejoin="miter"
                strokeMiterlimit={4}
                strokeDasharray="none"
                strokeOpacity={1}
            />
            <path
                d="M43.3,40.7l2.1,3.3H17.6l2.1-3.3"
                opacity={1}
                fill={this.props.fillColor}
                fillOpacity={1}
                fillRule="nonzero"
                stroke={this.props.strokeColor}
                strokeWidth={1.5}
                strokeLinecap="round"
                strokeLinejoin="miter"
                strokeMiterlimit={4}
                strokeDasharray="none"
                strokeOpacity={1}
            />
            <path
                d="M15.5,20.4h31.9"
                opacity={1}
                fill={this.props.fillColor}
                fillOpacity={1}
                fillRule="nonzero"
                stroke={this.props.strokeColor}
                strokeWidth={1.5}
                strokeLinecap="round"
                strokeLinejoin="miter"
                strokeMiterlimit={4}
                strokeDasharray="none"
                strokeOpacity={1}
            />
        </svg>
    );
}}

export class Bishop extends React.Component<IProps> {
    public render() {
        return (
        <svg viewBox="0 0 64 64" width="64" height="64" x={this.props.x} y={this.props.y} data-src={this.props.dataSrc}>
            <g>
                <path
                    d="M14.7,49.8c4.2-1.2,12.6,0.5,16.8-2.5c4.2,3.1,12.6,1.3,16.8,2.5c0,0,2,0.7,3.7,2.5
                    c-0.8,1.2-2,1.3-3.7,0.6c-4.2-1.2-12.6,0.6-16.8-1.3c-4.2,1.9-12.6,0-16.8,1.3c-1.7,0.6-2.9,0.6-3.7-0.6
                    C12.7,49.8,14.7,49.8,14.7,49.8z"
                    opacity={1}
                    fill={this.props.fillColor}
                    fillOpacity={1}
                    fillRule="nonzero"
                    stroke={this.props.strokeColor}
                    strokeWidth={1.5}
                    strokeLinecap="round"
                    strokeLinejoin="miter"
                    strokeMiterlimit={4}
                    strokeDasharray="none"
                    strokeOpacity={1}
                />
                <path
                    d="M22.2,44.6c3.1,3.2,15.5,3.2,18.6,0c0.6-1.9,0-2.5,0-2.5c0-3.2-3.1-5.2-3.1-5.2
                    c6.8-1.9,7.5-14.8-6.2-20c-13.7,5.2-13,18-6.2,20c0,0-3.1,1.9-3.1,5.2C22.2,42,21.6,42.7,22.2,44.6z"
                    opacity={1}
                    fill={this.props.fillColor}
                    fillOpacity={1}
                    fillRule="nonzero"
                    stroke={this.props.strokeColor}
                    strokeWidth={1.5}
                    strokeLinecap="round"
                    strokeLinejoin="miter"
                    strokeMiterlimit={4}
                    strokeDasharray="none"
                    strokeOpacity={1}
                />
                <path
                    d="M34.6,13.7c0,1.8-1.4,3.2-3.1,3.2s-3.1-1.4-3.1-3.2s1.4-3.2,3.1-3.2
                    C33.2,10.4,34.6,12,34.6,13.7z"
                    opacity={1}
                    fill={this.props.fillColor}
                    fillOpacity={1}
                    fillRule="nonzero"
                    stroke={this.props.strokeColor}
                    strokeWidth={1.5}
                    strokeLinecap="round"
                    strokeLinejoin="miter"
                    strokeMiterlimit={4}
                    strokeDasharray="none"
                    strokeOpacity={1}
                />
            </g>
            <path
                d="M25.3,36.9h12.4 M22.2,42h18.6 M31.5,23.3v6.4 M28.4,26.6h6.2"
                opacity={1}
                fill={this.props.fillColor}
                fillOpacity={1}
                fillRule="nonzero"
                stroke={this.props.strokeColor}
                strokeWidth={1.5}
                strokeLinecap="round"
                strokeLinejoin="miter"
                strokeMiterlimit={4}
                strokeDasharray="none"
                strokeOpacity={1}
            />
        </svg>
    );
}}

export class Knight extends React.Component<IProps> {
    public render() {
        return (
        <svg viewBox="0 0 64 64" width="64" height="64" x={this.props.x} y={this.props.y} data-src={this.props.dataSrc}>
            <g>
                <path
                    d="M32,14.4c0,0,0-4-1.4-4c-2.3,1.4-3.4,4-3.4,4h-2.7c0,0-2.7-4.7-4.1-3.3c0,1.3-0.3,2.7,0.7,4
                    c-0.1,2.1-2.7,4.7-2.7,4.7s-8.1,13.4-8.1,16.1c0,6.7,4.1,5.4,5.4,5.4c1.6-1,0-2.7,1.4-2.7c1.9-0.1-1.4,2.8,0,4
                    c3,0.5,2.7-2.7,6.8-5.4c2.5-1.6,7.6-5.4,9.8-8.8c0.8,15.8-11.1,13.5-11.1,24.8h31.1C54.3,25.1,46.2,15.7,32,14.4z M14.4,35.8
                    c-0.4,0-0.7-0.3-0.7-0.7c0-0.4,0.3-0.7,0.7-0.7s0.7,0.3,0.7,0.7C15.1,35.5,14.8,35.8,14.4,35.8z M22.4,22.1
                    c-0.6,1-1.3,1.6-1.6,1.4c-0.3-0.2-0.1-1.1,0.4-2.1c0.6-1,1.3-1.6,1.6-1.4C23.2,20.2,23,21.1,22.4,22.1z"
                    opacity={1}
                    fill={this.props.fillColor}
                    fillOpacity={1}
                    fillRule="nonzero"
                    stroke={this.props.strokeColor}
                    strokeWidth={1.5}
                    strokeLinecap="round"
                    strokeLinejoin="miter"
                    strokeMiterlimit={4}
                    strokeDasharray="none"
                    strokeOpacity={1}
                />
                <path
                    d="M15.1,35.1c0,0.4-0.3,0.7-0.7,0.7s-0.7-0.3-0.7-0.7c0-0.4,0.3-0.7,0.7-0.7 S15.1,34.7,15.1,35.1z"
                    opacity={1}
                    fill={this.props.fillColor}
                    fillOpacity={1}
                    fillRule="nonzero"
                    stroke={this.props.strokeColor}
                    strokeWidth={1.5}
                    strokeLinecap="round"
                    strokeLinejoin="miter"
                    strokeMiterlimit={4}
                    strokeDasharray="none"
                    strokeOpacity={1}
                />
                <path
                    d="M22.4,22.1c-0.6,1-1.3,1.6-1.6,1.4c-0.3-0.2-0.1-1.1,0.4-2.1c0.6-1,1.3-1.6,1.6-1.4 C23.2,20.2,23,21.1,22.4,22.1z"
                    opacity={1}
                    fill={this.props.fillColor}
                    fillOpacity={1}
                    fillRule="nonzero"
                    stroke={this.props.strokeColor}
                    strokeWidth={1.5}
                    strokeLinecap="round"
                    strokeLinejoin="miter"
                    strokeMiterlimit={4}
                    strokeDasharray="none"
                    strokeOpacity={1}
                />
                <path
                    d="M15.1,35.1c0,0.4-0.3,0.7-0.7,0.7s-0.7-0.3-0.7-0.7c0-0.4,0.3-0.7,0.7-0.7 S15.1,34.7,15.1,35.1z"
                    opacity={1}
                    fill={this.props.fillColor}
                    fillOpacity={1}
                    fillRule="nonzero"
                    stroke={this.props.strokeColor}
                    strokeWidth={1.5}
                    strokeLinecap="round"
                    strokeLinejoin="miter"
                    strokeMiterlimit={4}
                    strokeDasharray="none"
                    strokeOpacity={1}
                />
                <path
                    d="M22.4,22.1c-0.6,1-1.3,1.6-1.6,1.4c-0.3-0.2-0.1-1.1,0.4-2.1c0.6-1,1.3-1.6,1.6-1.4 C23.2,20.2,23,21.1,22.4,22.1z"
                    opacity={1}
                    fill={this.props.fillColor}
                    fillOpacity={1}
                    fillRule="nonzero"
                    stroke={this.props.strokeColor}
                    strokeWidth={1.5}
                    strokeLinecap="round"
                    strokeLinejoin="miter"
                    strokeMiterlimit={4}
                    strokeDasharray="none"
                    strokeOpacity={1}
                />
            </g>
        </svg>
        );
    }
}

export class Pawn extends React.Component<IProps> {
    public render() {
        return (
            <svg viewBox="0 0 64 64" width="64" height="64" x={this.props.x} y={this.props.y} data-src={this.props.dataSrc} onMouseDown={this.props.onMouseDown} onMouseMove={this.props.onMouseMove}>
                <path
                    d="M15.8,53.9c-0.4,0-0.8-0.3-0.8-0.8c0-8.9,5.2-14.3,9.4-16.2c-1.6-1.6-2.6-3.6-2.6-5.7
                    c0-2.8,1.6-5.3,4.1-6.9c-0.5-0.8-0.7-1.7-0.7-2.6c0-3,2.8-5.5,6.2-5.5s6.2,2.5,6.2,5.5c0,0.9-0.2,1.8-0.7,2.6
                    c2.6,1.6,4.1,4.2,4.1,6.9c0,2.2-0.9,4.2-2.6,5.7c4.2,1.9,9.4,7.3,9.4,16.2c0,0.4-0.3,0.8-0.8,0.8H15.8z"
                    opacity={1}
                    fill={this.props.fillColor}
                    fillOpacity={1}
                    fillRule="nonzero"
                    stroke={this.props.strokeColor}
                    strokeWidth={1.5}
                    strokeLinecap="round"
                    strokeLinejoin="miter"
                    strokeMiterlimit={4}
                    strokeDasharray="none"
                    strokeOpacity={1}
                />
            </svg>
        );
    }
}
