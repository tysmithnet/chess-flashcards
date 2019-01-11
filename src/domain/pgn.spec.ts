import { parsePgn } from "./pgn";

const sample0 = `[Event "F/S Return Match"]
[Site "Belgrade, Serbia JUG"]
[Date "1992.11.04"]
[Round "29"]
[White "Fischer, Robert J."]
[Black "Spassky, Boris V."]
[Result "1/2-1/2"]

1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 {This opening is called the Ruy Lopez.}
4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. c3 O-O 9. h3 Nb8 10. d4 Nbd7
11. c4 c6 12. cxb5 axb5 13. Nc3 Bb7 14. Bg5 b4 15. Nb1 h6 16. Bh4 c5 17. dxe5
Nxe4 18. Bxe7 Qxe7 19. exd6 Qf6 20. Nbd2 Nxd6 21. Nc4 Nxc4 22. Bxc4 Nb6
23. Ne5 Rae8 24. Bxf7+ Rxf7 25. Nxf7 Rxe1+ 26. Qxe1 Kxf7 27. Qe3 Qg5 28. Qxg5
hxg5 29. b3 Ke6 30. a3 Kd6 31. axb4 cxb4 32. Ra5 Nd5 33. f3 Bc8 34. Kf2 Bf5
35. Ra7 g6 36. Ra6+ Kc5 37. Ke1 Nf4 38. g3 Nxh3 39. Kd2 Kb5 40. Rd6 Kc5 41. Ra6
Nf2 42. g4 Bd3 43. Re6 1/2-1/2`;

const sample1 = `[Event "Rated Bullet game"]
[Site "https://lichess.org/qmH9mjWf"]
[Date "2019.01.11"]
[Round "-"]
[White "KingHarii"]
[Black "MaitreCourse"]
[Result "1-0"]
[UTCDate "2019.01.11"]
[UTCTime "00:30:17"]
[WhiteElo "2652"]
[BlackElo "2364"]
[WhiteRatingDiff "+4"]
[BlackRatingDiff "-3"]
[WhiteTitle "IM"]
[Variant "Standard"]
[TimeControl "60+0"]
[ECO "A46"]
[Opening "Indian Game: Wade-Tartakower Defense"]
[Termination "Normal"]
[Annotator "lichess.org"]

1. d4 d6 2. Nf3 Nf6 { A46 Indian Game: Wade-Tartakower Defense } 3. b3 Bg4 4. Bb2 Bxf3 5. gxf3 Nbd7 6. Rg1 c5 7. e3 cxd4 8. Bxd4 Rc8 9. c3 a6 10. c4 e6 11. Be2 g6 12. Nd2 Bg7 13. Ne4 O-O 14. Nxd6 Rc7 15. Ne4 Nxe4 16. fxe4 Qe7 17. Bxg7 Kxg7 18. Qd2 b5 19. Rd1 bxc4 20. Bxc4 Ne5 21. Qb2 Qf6 22. Kf1 Nxc4 23. Qxf6+ Kxf6 24. bxc4 Rxc4 25. Rd2 Rxe4 26. Ke2 Rc8 27. Rb1 Rec4 28. Rb7 R8c6 29. Rdd7 Rc2+ 30. Kf3 Kg5 31. Rxf7 h5 32. Kg3 h4+ 33. Kh3 { Black resigns. } 1-0`;

test("Correctly parses basic header section", () => {
    const result = parsePgn(sample0);
    expect(result.event).toEqual("F/S Return Match");
    expect(result.site).toEqual("Belgrade, Serbia JUG");
    expect(result.date).toEqual(new Date("1992.11.04"));
    expect(result.round).toEqual("29");
    expect(result.white).toEqual("Fischer, Robert J.");
    expect(result.black).toEqual("Spassky, Boris V.");
    expect(result.result).toEqual("1/2-1/2");
});

test("Correctly parses header section with non-standard tags", () => {
    const result = parsePgn(sample1);
    expect(result.event).toEqual("Rated Bullet game");
    expect(result.site).toEqual("https://lichess.org/qmH9mjWf");
    expect(result.date).toEqual(new Date("2019.01.11"));
    expect(result.round).toEqual("-");
    expect(result.white).toEqual("KingHarii");
    expect(result.black).toEqual("MaitreCourse");
    expect(result.result).toEqual("1-0");
    expect(result.otherTags.get("UTCDate")).toEqual("2019.01.11");
    expect(result.otherTags.get("UTCTime")).toEqual("00:30:17");
    expect(result.otherTags.get("WhiteElo")).toEqual("2652");
    expect(result.otherTags.get("BlackElo")).toEqual("2364");
    expect(result.otherTags.get("WhiteRatingDiff")).toEqual("+4");
    expect(result.otherTags.get("BlackRatingDiff")).toEqual("-3");
    expect(result.otherTags.get("WhiteTitle")).toEqual("IM");
    expect(result.otherTags.get("Variant")).toEqual("Standard");
    expect(result.otherTags.get("TimeControl")).toEqual("60+0");
    expect(result.otherTags.get("ECO")).toEqual("A46");
    expect(result.otherTags.get("Opening")).toEqual("Indian Game: Wade-Tartakower Defense");
    expect(result.otherTags.get("Termination")).toEqual("Normal");
    expect(result.otherTags.get("Annotator")).toEqual("lichess.org");
});
