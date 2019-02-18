import * as Fuse from "fuse.js";
import { IOpening } from "../root";
export interface IPreset {
    title: string;
    getSelectedOpenings: (openings: IOpening[]) => string[];
}

export const PRESETS: IPreset[] = [
    {
        title: "Ruy Lopez",
        getSelectedOpenings: (openings: IOpening[]) => {
            const fuse = new Fuse(openings, {
                keys: ["variantName"],
                id: "id",
                threshold: 0.2,
            });
            return fuse.search("ruy lopez");
        },
    },
    {
        title: "Queen's Gambit",
        getSelectedOpenings: (openings: IOpening[]) => {
            const fuse = new Fuse(openings, {
                keys: ["variantName"],
                id: "id",
                threshold: 0.2,
            });
            return fuse.search("queens gambit");
        },
    },
    {
        title: "Sicilian Defense",
        getSelectedOpenings: (openings: IOpening[]) => {
            const fuse = new Fuse(openings, {
                keys: ["variantName"],
                id: "id",
                threshold: 0.2,
            });
            return fuse.search("sicilian defense");
        },
    },
    {
        title: "King's Gambit",
        getSelectedOpenings: (openings: IOpening[]) => {
            const fuse = new Fuse(openings, {
                keys: ["variantName"],
                id: "id",
                threshold: 0.2,
            });
            return fuse.search("kings gambit");
        },
    },
    {
        title: "Basics",
        getSelectedOpenings: (openings: IOpening[]) => {
            return openings.filter(o => BASICS.indexOf(o.id) > -1).map(o => o.id);
        },
    },
];

const BASICS = [
    "47065a1d-211b-4a92-8eab-2edad7521c3d",
    "00520bab-5262-4a81-a06a-5dedaa8ef74b",
    "76f1dd4b-6639-4d34-8dab-0509f2e5fdb9",
    "50e2efba-2b64-4bc1-b13b-d4b55054511c",
    "c6193cab-141d-4ce6-aafb-4449394377b3",
    "158f92b0-50c6-4f43-874f-c1fbc01d4739",
    "7c777857-7ac9-4b63-89b4-735ee6ff9ebd",
    "3c716464-2eb3-4d17-89b4-fc45c7ce02de",
    "168dec55-340b-48f7-8bf7-620df1d2da84",
    "1cf63de1-4f85-4d06-b980-79cee013bb25",
    "66fed789-6e5d-47d0-86b5-2c55f0e4d60a",
    "8ae130aa-ec2f-480d-97fd-e658f72fe11f",
    "455e98ba-3888-4032-9350-adc470aa063d",
    "d2515a89-1772-4978-b255-760806b3abe5",
    "3ed84f1e-1f8a-4fd3-bde3-200602f7b870",
    "69234ccf-f44a-45c7-b375-cc6e2417fbf9",
    "d108dd0b-3c6f-4e68-b7ef-72c5b20a120e",
    "0fc04bd2-0d27-4652-b332-9e2ffbd3be4c",
    "d7a2f8ec-3283-411c-847d-8cd56f72ed86",
    "691c8125-625a-4e88-b8ea-e6b063cd30fb",
    "c5dcbb78-1fa2-4d4b-9548-6da9eb857c62",
    "faefe064-d1f6-44e5-82e9-3ea8f0ba4f55",
    "e1b66341-5762-4473-a9bf-4dc70b9cda99",
    "e85504ec-fc8d-406b-a56c-3e6594ea6978",
    "105aefad-c0b5-4bda-b394-0d9a7b6ef3ea",
    "3c84e9b4-3d76-4d4b-9224-9ec1e0bb5911",
    "c6c81eb5-e62a-43df-b5cf-05f1b848d083",
    "3a6fd289-47b6-46dd-ad88-949a178406b3",
    "d69c4888-7516-4490-8b08-0d1cf6116baf",
    "4943d8d7-6d41-4783-8e2d-2ed95269fe93",
    "56d66cf8-80cc-45be-98d7-a641e736e7ab",
    "987287a9-d1e2-448d-b2cf-933022f7a7a3",
    "89a49ac2-8858-44dd-86da-87832c10851b",
    "f74fa565-7d48-4767-8cc0-6b37f45c724a",
    "cf7a962c-ef3b-4d5a-9b20-77da3c96d3f3",
    "fdc84dc5-e743-4361-ba2c-2a67174eb235",
    "b67e9266-d17a-4b46-8a37-5d9cfaa3a596",
];
