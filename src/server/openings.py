import io
import re
import chess
import chess.pgn
from domain import Opening

TEXT = """******A00: Polish (Sokolsky) opening
Polish (Sokolsky) opening
b310c94b-a27b-46cc-b91f-e1691a6bfa3b
1. b4
Polish, Tuebingen variation
d8375340-0c02-4370-8ef9-0b5409487a28
1. b4 Nh6 
Polish, Outflank variation
08dd6049-656a-476a-8a27-2c6a213df7c6
1. b4 c6 
Benko's opening
cd8777ae-4afe-460f-b2bd-8beb6b653210
1. g3
Lasker simul special
1cad5c20-f236-4f83-afe1-db05b9a915cf
1. g3 h5 
Benko's opening, reversed Alekhine
6b3b67ba-22cc-462a-84b6-efc3463eefef
1. g3 e5 2. Nf3
Grob's attack
47065a1d-211b-4a92-8eab-2edad7521c3d
1. g4
Grob, spike attack
0b3f52ce-ef4f-4730-a9b2-2027d20f55c3
1. g4 d5 2. Bg2 c6 3. g5
Grob, Fritz gambit
68152012-bf50-4956-b93c-834812b7b420
1. g4 d5 2. Bg2 Bxg4 3. c4
Grob, Romford counter-gambit
ac7a4aba-18db-43ce-8480-40e5af1d11dd
1. g4 d5 2. Bg2 Bxg4 3. c4 d4 
Clemenz (Mead's, Basman's or de Klerk's) opening
ed6455c6-fb11-49a6-a759-a49a43e167b8
1. h3
Global opening
52d7d241-080a-49cd-a52d-821c7724b41e
1. h3 e5 2. a3
Amar (Paris) opening
0fd3f960-cbb2-4ce0-9c97-3183d381c3bf
1. Nh3
Amar gambit
213e94af-3a54-47ee-80b6-bb3bde80cc9c
1. Nh3 d5 2. g3 e5 3. f4 Bxh3 4. Bxh3 exf4 
Dunst (Sleipner,Heinrichsen) opening
819ec1a9-e42b-4f82-9f7f-709a79c133b6
1. Nc3 e5 
Battambang opening
c2965921-43ba-4ab7-977d-68e0eff69f1f
1. Nc3 e5 2. a3
Novosibirsk opening
6d5c1a42-df23-46a9-9d32-eab9d70f19c9
1. Nc3 c5 2. d4 cxd4 3. Qxd4 Nc6 4. Qh4
Anderssen's opening
9e44f3b3-0e8d-4b18-8938-6a375674caab
1. a3
Ware (Meadow Hay) opening
4f4a7576-cccf-454d-8bfc-2c8a7d8a3f99
1. a4
Crab opening
ef53292b-a3fe-405d-9b5e-694a9833bf19
1. a4 e5 2. h4
Saragossa opening
6be4ff1e-7c3f-4b2a-9df3-4cbc9300013a
1. c3
Mieses opening
74b7e357-2efe-4b42-9fbf-46418d2b66d9
1. d3 e5 
Valencia opening
74f8635b-95b2-4e51-83da-0b59c25f459c
1. d3 e5 2. Nd2
Venezolana opening
616a1c0b-d48a-442a-9682-8e1ae31b0c76
1. d3 c5 2. Nc3 Nc6 3. g3
Van't Kruijs opening
d1dceaf0-24c2-4c0c-a088-cee07e1f3bf7
1. e3
Amsterdam attack
c32feb9e-a5f5-4fc7-84bd-8f3b6d054d04
1. e3 e5 2. c4 d6 3. Nc3 Nc6 4. b3 Nf6 
Gedult's opening
c22cacda-db16-48f8-883a-8bf2976229e8
1. f3
Hammerschlag (Fried fox/Pork chop opening)
8c267087-3f2b-4f55-a658-c1f92c040d98
1. f3 e5 2. Kf2
Anti-Borg (Desprez) opening
988820b8-3b91-4fe3-9386-535d07452fb6
1. h4
Durkin's attack
c570c699-c85b-4fb9-a623-f3909f9a2f11
1. Na3
******A01: Nimzovich-Larsen attack
Nimzovich-Larsen attack
00520bab-5262-4a81-a06a-5dedaa8ef74b
1. b3
Nimzovich-Larsen attack, modern variation
a9785b4a-1edd-4d1e-bcd2-b9c49f116ca5
1. b3 e5 
Nimzovich-Larsen attack, Indian variation
53cb116b-bb2c-4a10-a66e-60e172fb7981
1. b3 Nf6 
Nimzovich-Larsen attack, classical variation
113e74d3-fa3d-44ab-86c1-ee66be7f5348
1. b3 d5 
Nimzovich-Larsen attack, English variation
4c1e704e-6d1a-41a8-844f-96a8ccf80067
1. b3 c5 
Nimzovich-Larsen attack, Dutch variation
7c7cb01f-1f54-474b-a1ba-012633dab88d
1. b3 f5 
Nimzovich-Larsen attack, Polish variation
8bc5b9b8-c14e-45ee-8af3-0eee7d9f7901
1. b3 b5 
Nimzovich-Larsen attack, symmetrical variation
a06e87e7-0fa7-4743-aeda-4bdb10d3af2f
1. b3 b6 
******A02: Bird's opening
Bird's opening
76f1dd4b-6639-4d34-8dab-0509f2e5fdb9
1. f4
Bird, From gambit
e0a8c33b-bb1d-4316-af4a-0034643a7e9e
1. f4 e5 
Bird, From gambit, Lasker variation
506942c2-2268-45d3-8ca0-6b4bb9c9919c
1. f4 e5 2. fxe5 d6 3. exd6 Bxd6 4. Nf3 g5 
Bird, From gambit, Lipke variation
67ee0104-8cc0-4ea5-9acb-4e5efb1e4683
1. f4 e5 2. fxe5 d6 3. exd6 Bxd6 4. Nf3 Nh6 5. d4
Bird's opening, Swiss gambit
240cc557-e9a4-4d2a-ab9a-dde7f3e944e5
1. f4 f5 2. e4 fxe4 3. Nc3 Nf6 4. g4
Bird, Hobbs gambit
501ed374-0929-42d4-81f0-5d70341de57d
1. f4 g5 
******A03: Bird's opening
Bird's opening
ecaa65bb-eac0-465f-b3be-32e0ac84d707
1. f4 d5 
Mujannah opening
16a50482-6118-493d-ba08-a4d1b31af363
1. f4 d5 2. c4
Bird's opening, Williams gambit
2c8f7dc4-0e36-4b7e-8596-2dccf4249505
1. f4 d5 2. e4
Bird's opening, Lasker variation
2def66b0-aa74-480a-8a98-fe5cd6ffd5ab
1. f4 d5 2. Nf3 Nf6 3. e3 c5 
******A04: Reti opening
Reti opening
50e2efba-2b64-4bc1-b13b-d4b55054511c
1. Nf3
Reti v Dutch
75ac5c1f-b470-4a7d-8364-8d0099242ac3
1. Nf3 f5 
Reti, Pirc-Lisitsin gambit
d0654edc-ef31-4508-9a96-ccee853cc9cc
1. Nf3 f5 2. e4
Reti, Lisitsin gambit deferred
bd1428bf-abd3-4a2b-a537-94447fd10aed
1. Nf3 f5 2. d3 Nf6 3. e4
Reti opening
847b794e-fb4f-42b1-a528-fa9dd598764b
1. Nf3 d6 
Reti, Wade defence
d4a7ce27-c522-428a-94ac-1b5634782ff6
1. Nf3 d6 2. e4 Bg4 
Reti, Herrstroem gambit
1185108f-39ec-4c88-937a-ca5e998ee0fd
1. Nf3 g5 
******A05: Reti opening
Reti opening
22c3ad3f-ce58-45ad-9d0a-b9d3bfc1989e
1. Nf3 Nf6 
Reti, King's Indian attack, Spassky's variation
792c7fa0-f007-4b46-9afb-4bf16565e9dc
1. Nf3 Nf6 2. g3 b5 
Reti, King's Indian attack
cd5d9400-0cef-4c87-9fc3-281881b5d66c
1. Nf3 Nf6 2. g3 g6 
Reti, King's Indian attack, Reti-Smyslov variation
f6f801bb-fd4d-4fe9-a879-491585c3bbe1
1. Nf3 Nf6 2. g3 g6 3. b4
******A06: Reti opening
Reti opening
7819f053-cbf8-47d3-8299-30d5a6e45001
1. Nf3 d5 
Reti, old Indian attack
c216f5d8-6709-4954-94c9-52c7e35745ff
1. Nf3 d5 2. d3
Santasiere's folly
ce177273-c4c5-4deb-8500-a29aa367d3f6
1. Nf3 d5 2. b4
Tennison (Lemberg, Zukertort) gambit
cbbdc46f-af59-4708-9cdc-10ea5a605b41
1. Nf3 d5 2. e4
Reti, Nimzovich-Larsen attack
b938b5a0-7b4a-44ab-8a61-1710e835eed5
1. Nf3 d5 2. b3
******A07: Reti, King's Indian attack (Barcza system)
Reti, King's Indian attack (Barcza system)
323e6252-98fe-417f-8ea9-7ff6d28588a7
1. Nf3 d5 2. g3
Reti, King's Indian attack, Yugoslav variation
70538641-01af-4e6b-bb58-e588d9d42f62
1. Nf3 d5 2. g3 Nf6 3. Bg2 c6 4. O-O Bg4 
Reti, King's Indian attack, Keres variation
5b731e69-7ec4-4ed3-8d9c-4d218eb85da9
1. Nf3 d5 2. g3 Bg4 3. Bg2 Nd7 
Reti, King's Indian attack
ad1623a6-2fd0-4c78-b165-946d177f1a19
1. Nf3 d5 2. g3 g6 
Reti, King's Indian attack, Pachman system
121f7989-922c-4e6b-b964-07a05c269de9
1. Nf3 d5 2. g3 g6 3. Bg2 Bg7 4. O-O e5 5. d3 Ne7 
Reti, King's Indian attack (with ...c5)
c31b2154-2ee8-4951-9315-5e0e80ed09e8
1. Nf3 d5 2. g3 c5 
******A08: Reti, King's Indian attack
Reti, King's Indian attack
29ef64a2-a733-4367-aab2-3d18b321da99
1. Nf3 d5 2. g3 c5 3. Bg2
Reti, King's Indian attack, French variation
e8d6135a-34b1-47ce-9194-11bc98b8b9fb
1. Nf3 d5 2. g3 c5 3. Bg2 Nc6 4. O-O e6 5. d3 Nf6 6. Nbd2 Be7 7. e4 O-O 8. Re1
******A09: Reti opening
Reti opening
86ad59ac-1b1e-4f87-a99a-cbf28d1c6e01
1. Nf3 d5 2. c4
Reti, advance variation
3be5fca7-e82b-47c9-bc5c-35b319fa9384
1. Nf3 d5 2. c4 d4 
Reti accepted
38dad1eb-6f5e-4dec-bde8-298a73daa9c0
1. Nf3 d5 2. c4 dxc4 
Reti accepted, Keres variation
36fbe692-1bb1-43db-afa6-b2458e7e655e
1. Nf3 d5 2. c4 dxc4 3. e3 Be6 
******A10: English opening
English opening
c6193cab-141d-4ce6-aafb-4449394377b3
1. c4
English opening
eb93cec5-724e-4377-994e-bd5ada64e839
1. c4 g6 
English, Adorjan defence
8fb68367-1a78-4e40-a813-f0c77e92c3c5
1. c4 g6 2. e4 e5 
English, Jaenisch gambit
df597d6d-e024-4f28-9ff6-55637e5f9d89
1. c4 b5 
English, Anglo-Dutch defense
34f9751d-daaa-4ce0-8661-6fda5116e5c9
1. c4 f5 
******A11: English, Caro-Kann defensive system
English, Caro-Kann defensive system
a7fa3349-2b70-448c-85a3-6ef6e61d5988
1. c4 c6 
******A12: English, Caro-Kann defensive system
English, Caro-Kann defensive system
bf9dda76-94ef-4104-9c1d-c308d6fae286
1. c4 c6 2. Nf3 d5 3. b3
English, Torre defensive system
0c672138-b6ee-400b-abd0-b3653f4640f9
1. c4 c6 2. Nf3 d5 3. b3 Nf6 4. g3 Bg4 
English, London defensive system
f01571d3-afe1-4a80-8131-950dfc24ba80
1. c4 c6 2. Nf3 d5 3. b3 Nf6 4. g3 Bf5 
English, Caro-Kann defensive system
0b073c6b-8134-4861-81e0-efbc01747980
1. c4 c6 2. Nf3 d5 3. b3 Nf6 4. Bb2
English, Bled variation
a294c26c-0ffb-4aaf-830d-1d155e02dc14
1. c4 c6 2. Nf3 d5 3. b3 Nf6 4. Bb2 g6 
English, New York (London) defensive system
45425ddf-db39-49f2-b43b-336462127038
1. c4 c6 2. Nf3 d5 3. b3 Nf6 4. Bb2 Bf5 
English, Capablanca's variation
553476a2-a3ed-4b6c-9089-5cc252af73ed
1. c4 c6 2. Nf3 d5 3. b3 Nf6 4. Bb2 Bg4 
English, Caro-Kann defensive system, Bogolyubov variation
94bf21e0-1447-459f-9c2d-0da4f00aa000
1. c4 c6 2. Nf3 d5 3. b3 Bg4 
******A13: English opening
English opening
1e9e8506-b31c-4fa8-a9b5-ab8aaf95d3b5
1. c4 e6 
English, Romanishin gambit
906e23ed-a3da-4b0d-80f5-09ef52a231bb
1. c4 e6 2. Nf3 Nf6 3. g3 a6 4. Bg2 b5 
English opening, Agincourt variation
81f6d0a7-edb1-41b6-8ff0-7be35cf16742
1. c4 e6 2. Nf3 d5 
English, Wimpey system
4c21b77a-037c-488c-a169-05760b494965
1. c4 e6 2. Nf3 d5 3. b3 Nf6 4. Bb2 c5 5. e3
English opening, Agincourt variation
0fa1af78-6e29-4f97-b439-c119e64b1228
1. c4 e6 2. Nf3 d5 3. g3
English, Kurajica defence
e2fd4bb0-9489-4551-bf31-a995bf236add
1. c4 e6 2. Nf3 d5 3. g3 c6 
English, Neo-Catalan
b836942e-cfcc-46a0-98d4-8c087021def3
1. c4 e6 2. Nf3 d5 3. g3 Nf6 
English, Neo-Catalan accepted
b70c36f2-fe54-403a-a274-159f5fad2070
1. c4 e6 2. Nf3 d5 3. g3 Nf6 4. Bg2 dxc4 
******A14: English, Neo-Catalan declined
English, Neo-Catalan declined
bad9ea1a-1c06-423a-a5a2-c14bf9f5fea2
1. c4 e6 2. Nf3 d5 3. g3 Nf6 4. Bg2 Be7 5. O-O
English, Symmetrical, Keres defence
f374d8db-3833-496b-9a60-42bc91817e73
1. c4 e6 2. Nf3 d5 3. g3 Nf6 4. Bg2 Be7 5. O-O c5 6. cxd5 Nxd5 7. Nc3 Nc6 
******A15: English, 1...Nf6 (Anglo-Indian defense)
English, 1...Nf6 (Anglo-Indian defense)
c514a91e-095e-4da6-b039-c05b6708f063
1. c4 Nf6 
English orang-utan
cd16ea69-bdc9-4ffd-b323-41728cbd5c54
1. c4 Nf6 2. b4
English opening
3351832a-52b5-42c5-8ba4-f5384c4d69be
1. c4 Nf6 2. Nf3
******A16: English opening
English opening
928a5ffe-00e7-4826-8ce3-ab490f2e88de
1. c4 Nf6 2. Nc3
English, Anglo-Gruenfeld defense
973d8f7a-ab0a-4f87-967f-b280010966d1
1. c4 Nf6 2. Nc3 d5 
English, Anglo-Gruenfeld, Smyslov defense
0b4eab27-6a45-4638-bde4-aa27fb76a120
1. c4 Nf6 2. Nc3 d5 3. cxd5 Nxd5 4. g3 g6 5. Bg2 Nxc3 
English, Anglo-Gruenfeld, Czech defense
2abdb620-0123-4486-948a-cac95a767f64
1. c4 Nf6 2. Nc3 d5 3. cxd5 Nxd5 4. g3 g6 5. Bg2 Nb6 
English, Anglo-Gruenfeld defense
cc049f71-9683-40ac-ba80-16984be4a97f
1. c4 Nf6 2. Nc3 d5 3. cxd5 Nxd5 4. Nf3
English, Anglo-Gruenfeld defense, Korchnoi variation
1718568f-2fe5-47de-8a72-9e2a7a6d3861
1. c4 Nf6 2. Nc3 d5 3. cxd5 Nxd5 4. Nf3 g6 5. g3 Bg7 6. Bg2 e5 
******A17: English opening
English opening
577ceafd-9dfd-4a90-a792-aee532a398f2
1. c4 Nf6 2. Nc3 e6 
English, Queens Indian formation
7a3e01e3-dcc2-412d-a5cd-45c2545e6f9a
1. c4 Nf6 2. Nc3 e6 3. Nf3 b6 
English, Queens Indian, Romanishin variation
d5998a86-c68e-4bd0-95c9-e101d4e44b83
1. c4 Nf6 2. Nc3 e6 3. Nf3 b6 4. e4 Bb7 5. Bd3
English, Nimzo-English opening
d5f714f9-6aee-4db0-80f6-a099667b6e74
1. c4 Nf6 2. Nc3 e6 3. Nf3 Bb4 
******A18: English, Mikenas-Carls variation
English, Mikenas-Carls variation
644ccdf2-0b46-4713-98e4-2ab42bb74bca
1. c4 Nf6 2. Nc3 e6 3. e4
English, Mikenas-Carls, Flohr variation
0a5df388-7fb2-40aa-8194-5154e0f0b2f7
1. c4 Nf6 2. Nc3 e6 3. e4 d5 4. e5
English, Mikenas-Carls, Kevitz variation
effddf4b-a613-4b8c-aef1-7df95f5d318d
1. c4 Nf6 2. Nc3 e6 3. e4 Nc6 
******A19: English, Mikenas-Carls, Sicilian variation
English, Mikenas-Carls, Sicilian variation
cbc3aaed-f3a1-411f-b1f9-17c925384a1d
1. c4 Nf6 2. Nc3 e6 3. e4 c5 
******A20: English opening
English opening
75662bd2-2910-4d8c-b4b7-81e5cbd0d24c
1. c4 e5 
English, Nimzovich variation
da09656d-f7ec-4665-a83d-72be28b4a002
1. c4 e5 2. Nf3
English, Nimzovich, Flohr variation
adde7bc5-4825-4a2b-929e-65ed0a54b812
1. c4 e5 2. Nf3 e4 
******A21: English opening
English opening
f66fef21-db06-4112-aa65-73f15683b789
1. c4 e5 2. Nc3
English, Troeger defence
b393875a-4ea7-48d8-b369-5e55ae9a4aae
1. c4 e5 2. Nc3 d6 3. g3 Be6 4. Bg2 Nc6 
English, Keres variation
33d165f0-dfd6-4bdd-814a-b979baa2c12d
1. c4 e5 2. Nc3 d6 3. g3 c6 
English opening
35cad3e2-3307-4004-bb02-272e42f0b35a
1. c4 e5 2. Nc3 d6 3. Nf3
English, Smyslov defence
4019e650-82e3-4ad7-bd98-05e69e6f0348
1. c4 e5 2. Nc3 d6 3. Nf3 Bg4 
English, Kramnik-Shirov counterattack
e99a3a0e-853c-45b1-a474-c64d038867c7
1. c4 e5 2. Nc3 Bb4 
******A22: English opening
English opening
7c450579-bf45-44c2-85af-be003e24ba25
1. c4 e5 2. Nc3 Nf6 
English, Bellon gambit
40585513-cb29-4893-98ad-93ccc450b49e
1. c4 e5 2. Nc3 Nf6 3. Nf3 e4 4. Ng5 b5 
English, Carls' Bremen system
62116c9f-d999-4325-85cc-84e4a48ef1b8
1. c4 e5 2. Nc3 Nf6 3. g3
English, Bremen, reverse dragon
e6277458-6641-4e93-a90a-a332de4aa6cb
1. c4 e5 2. Nc3 Nf6 3. g3 d5 
English, Bremen, Smyslov system
e8d20cbc-c466-47d8-9dd7-c5dcc66d7802
1. c4 e5 2. Nc3 Nf6 3. g3 Bb4 
******A23: English, Bremen system, Keres variation
English, Bremen system, Keres variation
e4fb15d6-bc34-475c-875b-840bcc1ed147
1. c4 e5 2. Nc3 Nf6 3. g3 c6 
******A24: English, Bremen system with ...g6
English, Bremen system with ...g6
c2f60e12-2101-41ea-b0e7-fa36e0bd7a22
1. c4 e5 2. Nc3 Nf6 3. g3 g6 
******A25: English, Sicilian reversed
English, Sicilian reversed
34bbc4df-e2e3-4ac2-a763-63acfe3259df
1. c4 e5 2. Nc3 Nc6 
English, closed system
839601aa-5b10-44fe-8c52-893c2a9fbf85
1. c4 e5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 
English, closed, Taimanov variation
9945d404-d3dc-43d1-94a7-d3c239588c9e
1. c4 e5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. e3 d6 6. Nge2 Nh6 
English, closed, Hort variation
930e04f1-cc88-40a4-96c9-fe3d46239fa2
1. c4 e5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. e3 d6 6. Nge2 Be6 
English, closed, 5.Rb1
34b40d8a-c287-482c-b2f4-da0660e3ccb0
1. c4 e5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. Rb1
English, closed, 5.Rb1 Taimanov variation
a6e1a248-afc3-4ac1-bae3-710745efffba
1. c4 e5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. Rb1 Nh6 
English, closed system (without ...d6)
d4b566c0-6d71-4c28-9442-8313a194cd47
1. c4 e5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. d3
******A26: English, closed system
English, closed system
0550dca1-88ba-4e80-8638-fb13904b9649
1. c4 e5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. d3 d6 
English, Botvinnik system
610ffbe3-39ae-415a-a523-3399f692ca8a
1. c4 e5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. d3 d6 6. e4
******A27: English, three knights system
English, three knights system
f5391dce-94de-4c42-b803-8ce8c99a4bc6
1. c4 e5 2. Nc3 Nc6 3. Nf3
******A28: English, four knights system
English, four knights system
9896c914-7cd9-443f-8e2c-f0b495d27d05
1. c4 e5 2. Nc3 Nc6 3. Nf3 Nf6 
English, Nenarokov variation
ed7ae747-d433-4888-bd69-8f8aef24708a
1. c4 e5 2. Nc3 Nc6 3. Nf3 Nf6 4. d4 exd4 5. Nxd4 Bb4 6. Bg5 h6 7. Bh4 Bxc3+ 8. bxc3 Ne5 
English, Bradley Beach variation
7309eca1-c7bc-475e-a86d-594c8ef8cd6c
1. c4 e5 2. Nc3 Nc6 3. Nf3 Nf6 4. d4 e4 
English, four knights, Nimzovich variation
cc3d1984-3d4f-4694-a162-e39a95da8027
1. c4 e5 2. Nc3 Nc6 3. Nf3 Nf6 4. e4
English, four knights, Marini variation
3f79641b-623c-42d2-9d71-883e17c4fa10
1. c4 e5 2. Nc3 Nc6 3. Nf3 Nf6 4. a3
English, four knights, Capablanca variation
34b1f591-ea60-41f1-aafd-ed10868f76cd
1. c4 e5 2. Nc3 Nc6 3. Nf3 Nf6 4. d3
English, four knights, 4.e3
a459266b-d3f6-491f-ba5b-f76a7bdc546e
1. c4 e5 2. Nc3 Nc6 3. Nf3 Nf6 4. e3
English, four knights, Stean variation
99cd9204-1280-4d6c-851d-dfd3efb44f1b
1. c4 e5 2. Nc3 Nc6 3. Nf3 Nf6 4. e3 Bb4 5. Qc2 O-O 6. Nd5 Re8 7. Qf5
English, four knights, Romanishin variation
3f8838f1-26ec-4fa4-8df9-93fcd197c91a
1. c4 e5 2. Nc3 Nc6 3. Nf3 Nf6 4. e3 Bb4 5. Qc2 Bxc3 
******A29: English, four knights, kingside fianchetto
English, four knights, kingside fianchetto
65586dcc-c57e-4f44-8e65-644524686965
1. c4 e5 2. Nc3 Nc6 3. Nf3 Nf6 4. g3
******A30: English, symmetrical variation
English, symmetrical variation
d5f3f3d0-c81c-428e-ab03-097e156c848c
1. c4 c5 
English, symmetrical, hedgehog system
7a450435-ba84-44a7-b3d2-f466dd48e65c
1. c4 c5 2. Nf3 Nf6 3. g3 b6 4. Bg2 Bb7 5. O-O e6 6. Nc3 Be7 
English, symmetrical, hedgehog, flexible formation
ed323407-bfbe-46c6-99fa-e5a99bfd7be9
1. c4 c5 2. Nf3 Nf6 3. g3 b6 4. Bg2 Bb7 5. O-O e6 6. Nc3 Be7 7. d4 cxd4 8. Qxd4 d6 9. Rd1 a6 10. b3 Nbd7 
******A31: English, symmetrical, Benoni formation
English, symmetrical, Benoni formation
40261622-2689-41b5-9c92-7fc066dc6d56
1. c4 c5 2. Nf3 Nf6 3. d4
******A32: English, symmetrical variation
English, symmetrical variation
3292a668-466e-4480-8d36-ab804986ce14
1. c4 c5 2. Nf3 Nf6 3. d4 cxd4 4. Nxd4 e6 
******A33: English, symmetrical variation
English, symmetrical variation
42e97ada-46f3-47f3-b5d0-647f20fe8056
1. c4 c5 2. Nf3 Nf6 3. d4 cxd4 4. Nxd4 e6 5. Nc3 Nc6 
English, symmetrical, Geller variation
a56f4443-5bad-49ea-8305-c5b4a37f141e
1. c4 c5 2. Nf3 Nf6 3. d4 cxd4 4. Nxd4 e6 5. Nc3 Nc6 6. g3 Qb6 
******A34: English, symmetrical variation
English, symmetrical variation
8f062f7e-c072-405d-9a1f-488498a31c06
1. c4 c5 2. Nc3
English, symmetrical, three knights system
f8222d5a-3f0a-421b-946b-98d4532ff0a8
1. c4 c5 2. Nc3 Nf6 3. Nf3 d5 4. cxd5 Nxd5 
English, symmetrical variation
fd362c62-985b-4f11-b8f8-5fc629164f9f
1. c4 c5 2. Nc3 Nf6 3. g3
English, symmetrical, Rubinstein system
719128d9-28dd-4c25-b02c-560aac5f00ab
1. c4 c5 2. Nc3 Nf6 3. g3 d5 4. cxd5 Nxd5 5. Bg2 Nc7 
******A35: English, symmetrical variation
English, symmetrical variation
bd49c646-8a03-4172-a05f-10adf4cdb186
1. c4 c5 2. Nc3 Nc6 
English, symmetrical, four knights system
26cdab26-c5dd-4566-9294-d6c2433ebebe
1. c4 c5 2. Nc3 Nc6 3. Nf3 Nf6 
******A36: English, symmetrical variation
English, symmetrical variation
e6932da9-f9e1-4081-a843-7b10b3284b05
1. c4 c5 2. Nc3 Nc6 3. g3
English, ultra-symmetrical variation
de9363ee-91ea-460e-b393-d0ce9a5cc231
1. c4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 
English, symmetrical, Botvinnik system reversed
16badb68-2c91-4635-9b1c-9f9be18e296f
1. c4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. e3 e5 
English, symmetrical, Botvinnik system
de0b41fa-7f0c-40dc-a63e-acaa99323e44
1. c4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. e4
******A37: English, symmetrical variation
English, symmetrical variation
2400f1e5-b18a-4673-adf8-8ff35fe28304
1. c4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. Nf3
English, symmetrical, Botvinnik system reversed
f93b47dd-6ee3-431f-9d6f-2555a4c1da98
1. c4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. Nf3 e5 
******A38: English, symmetrical variation
English, symmetrical variation
eb9c7f3c-d729-4a8d-8c57-eecb12444ea3
1. c4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. Nf3 Nf6 
English, symmetrical, main line with d3
f7229bc6-f3f1-4406-ac77-7691aeb70eef
1. c4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. Nf3 Nf6 6. O-O O-O 7. d3
English, symmetrical, main line with b3
0e34e740-1edd-4135-ad6f-723e53ecfa41
1. c4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. Nf3 Nf6 6. O-O O-O 7. b3
******A39: English, symmetrical, main line with d4
English, symmetrical, main line with d4
31e5217d-a233-4da9-a0a9-7997e8c71095
1. c4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. Nf3 Nf6 6. O-O O-O 7. d4
******A40: Queen's pawn
Queen's pawn
fd1be2ad-af9f-4f11-83ad-92993520ddd5
1. d4
Queen's pawn, Lundin (Kevitz-Mikenas) defence
dfa6397c-28b3-4480-a712-f8c3011be9c3
1. d4 Nc6 
Queen's pawn, Charlick (Englund) gambit
ac337509-69d8-42fd-b9f3-1afc138bf4f0
1. d4 e5 
Queen's pawn, Englund gambit
274b8615-0ed3-45fa-8648-c281749efc82
1. d4 e5 2. dxe5 Nc6 3. Nf3 Qe7 4. Qd5 f6 5. exf6 Nxf6 
Queen's pawn, English defence
5847523a-e771-43ce-ae81-f7630dec22f0
1. d4 b6 
Polish defence
69a63815-12c2-4230-985d-90005154cc04
1. d4 b5 
Queen's pawn
5f343872-37e4-4fb7-a41a-f32bb0e84b67
1. d4 e6 
Queen's pawn, Keres defence
c89cb53a-3bd8-410e-bf82-77137cedebd9
1. d4 e6 2. c4 b6 
Queen's pawn, Franco-Indian (Keres) defence
dfd5989b-95ea-485b-ad60-d6e5c37b4f73
1. d4 e6 2. c4 Bb4+ 
Modern defence
8ab67165-0bfb-401a-b511-c2103eef47cf
1. d4 g6 
Beefeater defence
acefcb09-1b9c-45e3-bece-f63e1b9bd0d0
1. d4 g6 2. c4 Bg7 3. Nc3 c5 4. d5 Bxc3+ 5. bxc3 f5 
******A41: Queen's Pawn
Queen's Pawn
0eea5212-53af-44a7-ad6f-0c9ff9110625
1. d4 d6 
Old Indian, Tartakower (Wade) variation
96c43013-e962-4e5f-a205-7eb09157052a
1. d4 d6 2. Nf3 Bg4 
Old Indian defence
abc32d05-8546-4801-a6f9-c93fca640505
1. d4 d6 2. c4
Modern defence
a0e9b645-2b85-4d73-8dfe-503ebbe32a87
1. d4 d6 2. c4 g6 3. Nc3 Bg7 
Robatsch defence, Rossolimo variation
8c0a2f2e-76e6-4fe9-870a-37a497360ca4
1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. c4 Bg4 
******A42: Modern defence, Averbakh system
Modern defence, Averbakh system
b13eb492-f2ff-4bd1-a4d3-472d418ff54b
1. d4 d6 2. c4 g6 3. Nc3 Bg7 4. e4
Pterodactyl defence
b34aeda4-b08a-4b00-b536-7b13c62a1707
1. d4 d6 2. c4 g6 3. Nc3 Bg7 4. e4 c5 5. Nf3 Qa5 
Modern defence, Averbakh system, Randspringer variation
997703f2-bc0b-43ab-90a7-8759c1825a07
1. d4 d6 2. c4 g6 3. Nc3 Bg7 4. e4 f5 
Modern defence, Averbakh system, Kotov variation
7575f5c9-4aa2-4a42-aaf9-9c5a2e0b68b8
1. d4 d6 2. c4 g6 3. Nc3 Bg7 4. e4 Nc6 
******A43: Old Benoni defence
Old Benoni defence
158f92b0-50c6-4f43-874f-c1fbc01d4739
1. d4 c5 
Old Benoni, Franco-Benoni defence
6c440638-1b89-49ad-b753-3fb5ad66a348
1. d4 c5 2. d5 e6 3. e4
Old Benoni, Mujannah formation
8751e271-0b11-4c0d-84c4-c41eaa2e3a13
1. d4 c5 2. d5 f5 
Old Benoni defence
1714a505-0834-46cc-8782-1a23d41792b7
1. d4 c5 2. d5 Nf6 
Woozle defence
54bb5564-3943-4c25-ae4d-bff0d1cf6bcd
1. d4 c5 2. d5 Nf6 3. Nc3 Qa5 
Old Benoni defence
f663323e-14f3-4c6e-b62f-010d18e5b448
1. d4 c5 2. d5 Nf6 3. Nf3
Hawk (Habichd) defence
c89b5ddc-27ea-4816-824a-b04d2070ed10
1. d4 c5 2. d5 Nf6 3. Nf3 c4 
Old Benoni defence
c6473f24-9b33-4bb6-ae56-d63f76662845
1. d4 c5 2. d5 d6 
Old Benoni, Schmid's system
77d01cad-a36a-4592-a136-18433f72bedb
1. d4 c5 2. d5 d6 3. Nc3 g6 
******A44: Old Benoni defence
Old Benoni defence
f381c16d-ef79-4965-88d8-90490d7e07ef
1. d4 c5 2. d5 e5 
Semi-Benoni (`blockade variation')
80a203c9-53bd-4984-abc0-5227cd62be92
1. d4 c5 2. d5 e5 3. e4 d6 
******A45: Queen's pawn game
Queen's pawn game
dbcdf561-b714-4544-bc0a-060689afe676
1. d4 Nf6 
Queen's pawn, Bronstein gambit
d881c066-6859-4bba-ac6f-e982702d2a8c
1. d4 Nf6 2. g4
Canard opening
6e95e372-178a-4099-be8b-da9569b86c87
1. d4 Nf6 2. f4
Paleface attack
662146db-6553-495a-9254-734f929c12d9
1. d4 Nf6 2. f3
Blackmar-Diemer gambit
df7c87a2-17ca-4cdb-a8c1-ae9495ff7670
1. d4 Nf6 2. f3 d5 3. e4
Gedult attack
e37293a4-32dc-458d-b158-8cee673eb541
1. d4 Nf6 2. f3 d5 3. g4
Trompovsky attack (Ruth, Opovcensky opening)
d3ff2242-92ad-43c7-b8ce-b37e4d9a684b
1. d4 Nf6 2. Bg5
******A46: Queen's pawn game
Queen's pawn game
f3fc784d-15f6-40b5-a4d6-e7f112fba2a9
1. d4 Nf6 2. Nf3
Queen's pawn, Torre attack
7839b99b-4cce-483f-bb05-1f978798df71
1. d4 Nf6 2. Nf3 e6 3. Bg5
Queen's pawn, Torre attack, Wagner gambit
bd4b9e26-9e63-4b54-a0cd-fdd3efc98179
1. d4 Nf6 2. Nf3 e6 3. Bg5 c5 4. e4
Queen's pawn, Yusupov-Rubinstein system
48ef5acb-fb32-4403-8a37-c946df88d3fc
1. d4 Nf6 2. Nf3 e6 3. e3
Doery defence
9d705c58-b32a-433d-ab2d-9cac4fdffc1c
1. d4 Nf6 2. Nf3 Ne4 
******A47: Queen's Indian defence
Queen's Indian defence
7c777857-7ac9-4b63-89b4-735ee6ff9ebd
1. d4 Nf6 2. Nf3 b6 
Queen's Indian, Marienbad system
a986a74a-33a9-47e9-97bb-15c8ab37bccf
1. d4 Nf6 2. Nf3 b6 3. g3 Bb7 4. Bg2 c5 
Queen's Indian, Marienbad system, Berg variation
ab062c64-d040-491b-b80b-bd954a132ada
1. d4 Nf6 2. Nf3 b6 3. g3 Bb7 4. Bg2 c5 5. c4 cxd4 6. Qxd4
******A48: King's Indian, East Indian defence
King's Indian, East Indian defence
1ad4693d-1fa2-4f88-ad46-a3753f39f29d
1. d4 Nf6 2. Nf3 g6 
King's Indian, Torre attack
7ca3eea6-a7af-4081-a4d1-6c0eecfb09cc
1. d4 Nf6 2. Nf3 g6 3. Bg5
King's Indian, London system
20dc541e-c571-41ae-8e25-41ae469418c0
1. d4 Nf6 2. Nf3 g6 3. Bf4
******A49: King's Indian, fianchetto without c4
King's Indian, fianchetto without c4
8b669a06-e111-47cc-a233-e19c4c607225
1. d4 Nf6 2. Nf3 g6 3. g3
******A50: Queen's pawn game
Queen's pawn game
6f14e8a6-12c1-4558-8e32-c04b13f09fbf
1. d4 Nf6 2. c4
Kevitz-Trajkovich defence
b93e6220-0aa9-44d0-b0e1-a2ceb69c88fb
1. d4 Nf6 2. c4 Nc6 
Queen's Indian accelerated
0eb69a2b-de1e-48e0-9553-75a1686b2873
1. d4 Nf6 2. c4 b6 
******A51: Budapest defence declined
Budapest defence declined
3c716464-2eb3-4d17-89b4-fc45c7ce02de
1. d4 Nf6 2. c4 e5 
Budapest, Fajarowicz variation
647839f7-a9cd-493e-bc69-7445551e8e35
1. d4 Nf6 2. c4 e5 3. dxe5 Ne4 
Budapest, Fajarowicz, Steiner variation
cdecaa27-d454-4362-9dcd-3919cc84d480
1. d4 Nf6 2. c4 e5 3. dxe5 Ne4 4. Qc2
******A52: Budapest defence
Budapest defence
168dec55-340b-48f7-8bf7-620df1d2da84
1. d4 Nf6 2. c4 e5 3. dxe5 Ng4 
Budapest, Adler variation
710d2230-4f2f-441a-b7a0-b168c257150d
1. d4 Nf6 2. c4 e5 3. dxe5 Ng4 4. Nf3
Budapest, Rubinstein variation
3c6d2ad3-de23-4324-834a-83525c91da59
1. d4 Nf6 2. c4 e5 3. dxe5 Ng4 4. Bf4
Budapest, Alekhine variation
ed73d52c-e508-4f32-86ed-70639ffbc4d4
1. d4 Nf6 2. c4 e5 3. dxe5 Ng4 4. e4
Budapest, Alekhine, Abonyi variation
de2c10d0-66eb-4e52-924f-e481486d6614
1. d4 Nf6 2. c4 e5 3. dxe5 Ng4 4. e4 Nxe5 5. f4 Nec6 
Budapest, Alekhine variation, Balogh gambit
a507221d-013a-4858-a8fb-0c16eff021e0
1. d4 Nf6 2. c4 e5 3. dxe5 Ng4 4. e4 d6 
******A53: Old Indian defence
Old Indian defence
1cf63de1-4f85-4d06-b980-79cee013bb25
1. d4 Nf6 2. c4 d6 
Old Indian, Janowski variation
5ae03405-e9f4-4930-a0fa-1e7f7a4afd9b
1. d4 Nf6 2. c4 d6 3. Nc3 Bf5 
******A54: Old Indian, Ukrainian variation
Old Indian, Ukrainian variation
9eadeac1-38f8-4d58-9f00-cfd408411671
1. d4 Nf6 2. c4 d6 3. Nc3 e5 
Old Indian, Dus-Khotimirsky variation
8a258071-dfaf-4e95-b8bd-20bcfee13c41
1. d4 Nf6 2. c4 d6 3. Nc3 e5 4. e3 Nbd7 5. Bd3
Old Indian, Ukrainian variation, 4.Nf3
9fd28711-33d3-4021-b292-f28aa558b4c7
1. d4 Nf6 2. c4 d6 3. Nc3 e5 4. Nf3
******A55: Old Indian, main line
Old Indian, main line
5c907953-9a90-41ae-b49a-1f6dd27ec95e
1. d4 Nf6 2. c4 d6 3. Nc3 e5 4. Nf3 Nbd7 5. e4
******A56: Benoni defence
Benoni defence
66fed789-6e5d-47d0-86b5-2c55f0e4d60a
1. d4 Nf6 2. c4 c5 
Benoni defence, Hromodka system
7c4ecaf5-80dc-41c8-b52a-5b88d0e535a4
1. d4 Nf6 2. c4 c5 3. d5 d6 
Vulture defence
79739894-959d-4add-8e7e-e5d4c281accd
1. d4 Nf6 2. c4 c5 3. d5 Ne4 
Czech Benoni defence
a564e647-fdbb-4c5d-9494-1b8bdb349969
1. d4 Nf6 2. c4 c5 3. d5 e5 
Czech Benoni, King's Indian system
df4a3771-15f2-4166-9715-33b48a837a39
1. d4 Nf6 2. c4 c5 3. d5 e5 4. Nc3 d6 5. e4 g6 
******A57: Benko gambit
Benko gambit
8ae130aa-ec2f-480d-97fd-e658f72fe11f
1. d4 Nf6 2. c4 c5 3. d5 b5 
Benko gambit half accepted
290cd4e7-3ac8-4172-a66e-3ffbc3cef28c
1. d4 Nf6 2. c4 c5 3. d5 b5 4. cxb5 a6 
Benko gambit, Zaitsev system
da73912f-07f2-461c-ac32-8fee1f593c38
1. d4 Nf6 2. c4 c5 3. d5 b5 4. cxb5 a6 5. Nc3
Benko gambit, Nescafe Frappe attack
7f597749-c06c-4904-b0f6-fa2207cdc3ff
1. d4 Nf6 2. c4 c5 3. d5 b5 4. cxb5 a6 5. Nc3 axb5 6. e4 b4 7. Nb5 d6 8. Bc4
******A58: Benko gambit accepted
Benko gambit accepted
aa7e9e1d-18f9-4498-888a-68f2f79ec8b8
1. d4 Nf6 2. c4 c5 3. d5 b5 4. cxb5 a6 5. bxa6
Benko gambit, Nd2 variation
2a08bdd3-b36e-4c5d-90a8-c4a14fa57788
1. d4 Nf6 2. c4 c5 3. d5 b5 4. cxb5 a6 5. bxa6 Bxa6 6. Nc3 d6 7. Nf3 g6 8. Nd2
Benko gambit, fianchetto variation
a8947d0a-f86f-48f9-8a10-45e3fa3bfe30
1. d4 Nf6 2. c4 c5 3. d5 b5 4. cxb5 a6 5. bxa6 Bxa6 6. Nc3 d6 7. Nf3 g6 8. g3
******A59: Benko gambit, 7.e4
Benko gambit, 7.e4
479ea7ea-6775-4d4d-bf22-753a617396d7
1. d4 Nf6 2. c4 c5 3. d5 b5 4. cxb5 a6 5. bxa6 Bxa6 6. Nc3 d6 7. e4
Benko gambit, Ne2 variation
0f4f1ed3-e8f8-4293-b274-ace8afad24a0
1. d4 Nf6 2. c4 c5 3. d5 b5 4. cxb5 a6 5. bxa6 Bxa6 6. Nc3 d6 7. e4 Bxf1 8. Kxf1 g6 9. Nge2
Benko gambit
88f76441-ffb7-4c26-a960-8058dd1c2fb9
1. d4 Nf6 2. c4 c5 3. d5 b5 4. cxb5 a6 5. bxa6 Bxa6 6. Nc3 d6 7. e4 Bxf1 8. Kxf1 g6 9. g3
Benko gambit, main line
7efa971c-2fcd-4504-aecc-beb492831067
1. d4 Nf6 2. c4 c5 3. d5 b5 4. cxb5 a6 5. bxa6 Bxa6 6. Nc3 d6 7. e4 Bxf1 8. Kxf1 g6 9. g3 Bg7 10. Kg2 O-O 11. Nf3
******A60: Benoni defence
Benoni defence
36d7455e-98a2-487d-a3a3-c338945fdd44
1. d4 Nf6 2. c4 c5 3. d5 e6 
******A61: Benoni defence
Benoni defence
455e98ba-3888-4032-9350-adc470aa063d
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. Nf3 g6 
Benoni, Uhlmann variation
50def532-c8d5-44e3-a92f-9561b2f6c0e8
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. Nf3 g6 7. Bg5
Benoni, Nimzovich (knight's tour) variation
12da43b2-8a23-45b6-ad54-c292c61d7deb
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. Nf3 g6 7. Nd2
Benoni, fianchetto variation
c8a755bd-0b73-4455-a03f-51ae45885fb8
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. Nf3 g6 7. g3
******A62: Benoni, fianchetto variation
Benoni, fianchetto variation
40621b78-1d40-4129-a591-5ce3a5eac47b
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. Nf3 g6 7. g3 Bg7 8. Bg2 O-O 
******A63: Benoni, fianchetto, 9...Nbd7
Benoni, fianchetto, 9...Nbd7
c8a31313-9932-4a4b-bbed-d7570fe96bf1
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. Nf3 g6 7. g3 Bg7 8. Bg2 O-O 9. O-O Nbd7 
******A64: Benoni, fianchetto, 11...Re8
Benoni, fianchetto, 11...Re8
f5bd2794-a6e0-402c-a4a6-b88865db403f
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. Nf3 g6 7. g3 Bg7 8. Bg2 O-O 9. O-O Nbd7 10. Nd2 a6 11. a4 Re8 
******A65: Benoni, 6.e4
Benoni, 6.e4
4bd1dbea-850c-49b2-8faa-63f5ce1c6e7d
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4
******A66: Benoni, pawn storm variation
Benoni, pawn storm variation
fe9dcffb-170a-4109-bd5d-82240c841bfa
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. f4
Benoni, Mikenas variation
094bfdec-1069-4d9e-9265-3db58d779c31
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. f4 Bg7 8. e5
******A67: Benoni, Taimanov variation
Benoni, Taimanov variation
989e1687-bc0d-4878-8b93-b32a1ee585cb
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. f4 Bg7 8. Bb5+
******A68: Benoni, four pawns attack
Benoni, four pawns attack
366a1f8d-2ec4-4bde-91c3-2e863cad2c5d
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. f4 Bg7 8. Nf3 O-O 
******A69: Benoni, four pawns attack, main line
Benoni, four pawns attack, main line
1381a1a0-9997-47bf-8ff2-c0c263ed4999
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. f4 Bg7 8. Nf3 O-O 9. Be2 Re8 
******A70: Benoni, classical with e4 and Nf3
Benoni, classical with e4 and Nf3
b84b5dce-a9dc-42b8-a84c-48949fd20b19
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. Nf3
Benoni, classical without 9.O-O
c03597fa-aa00-4d57-9cc4-338b5962d596
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. Nf3 Bg7 8. Be2
******A71: Benoni, classical, 8.Bg5
Benoni, classical, 8.Bg5
65524c9e-39ee-4e41-aeef-ed273a0dcade
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. Nf3 Bg7 8. Bg5
******A72: Benoni, classical without 9.O-O
Benoni, classical without 9.O-O
1c23521a-d6ff-41c2-bcbe-34cc2330d191
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. Nf3 Bg7 8. Be2 O-O 
******A73: Benoni, classical, 9.O-O
Benoni, classical, 9.O-O
2d16df70-43ec-453e-aa35-467281d15e9e
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. Nf3 Bg7 8. Be2 O-O 9. O-O
******A74: Benoni, classical, 9...a6, 10.a4
Benoni, classical, 9...a6, 10.a4
84f5851d-9be2-410a-84ab-8410a31f0e12
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. Nf3 Bg7 8. Be2 O-O 9. O-O a6 10. a4
******A75: Benoni, classical with ...a6 and 10...Bg4
Benoni, classical with ...a6 and 10...Bg4
0bfce9bd-bd1e-4a66-ae9c-218c68e9fa04
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. Nf3 Bg7 8. Be2 O-O 9. O-O a6 10. a4 Bg4 
******A76: Benoni, classical, 9...Re8
Benoni, classical, 9...Re8
20ee93f1-2210-4168-b926-503b04f49f13
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. Nf3 Bg7 8. Be2 O-O 9. O-O Re8 
******A77: Benoni, classical, 9...Re8, 10.Nd2
Benoni, classical, 9...Re8, 10.Nd2
4dbf8ba4-1eff-4cc9-b884-6f998a0727ed
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. Nf3 Bg7 8. Be2 O-O 9. O-O Re8 10. Nd2
******A78: Benoni, classical with ...Re8 and ...Na6
Benoni, classical with ...Re8 and ...Na6
92d2e0a9-79ea-458f-9ead-eb02c8d9e4c3
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. Nf3 Bg7 8. Be2 O-O 9. O-O Re8 10. Nd2 Na6 
******A79: Benoni, classical, 11.f3
Benoni, classical, 11.f3
71e496e8-4a5e-4d66-9aab-10219746dd01
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. Nf3 Bg7 8. Be2 O-O 9. O-O Re8 10. Nd2 Na6 11. f3
******A80: Dutch
Dutch
d2515a89-1772-4978-b255-760806b3abe5
1. d4 f5 
Dutch, Spielmann gambit
4beb0739-4839-4e5d-aa21-0f042544710a
1. d4 f5 2. Nc3 Nf6 3. g4
Dutch, Manhattan (Alapin, Ulvestad) variation
c85e81f5-0adf-439c-8d4e-46c80a84d1c0
1. d4 f5 2. Qd3
Dutch, Von Pretzel gambit
1bf9ef8d-bf7e-4b0d-9570-1d90e92e0dd1
1. d4 f5 2. Qd3 e6 3. g4
Dutch, Korchnoi attack
bc6a631a-ede4-4980-b7ab-61b750b050c2
1. d4 f5 2. h3
Dutch, Krejcik gambit
c3899657-1848-495f-b0ba-7aa67c79e7cd
1. d4 f5 2. g4
Dutch, 2.Bg5 variation
beea606d-0c39-4168-a383-a9553c7fc320
1. d4 f5 2. Bg5
******A81: Dutch defence
Dutch defence
b232c975-8f39-4201-ae76-5ad350a04eb0
1. d4 f5 2. g3
Dutch defence, Blackburne variation
e4cf5d0e-d91f-4182-a0c8-f03af676d053
1. d4 f5 2. g3 Nf6 3. Bg2 e6 4. Nh3
Dutch defence
01206678-13f6-44e8-8178-0ea75dd52734
1. d4 f5 2. g3 Nf6 3. Bg2 g6 
Dutch, Leningrad, Basman system
508ae91a-a260-462d-bf96-db692c363fe7
1. d4 f5 2. g3 g6 3. Bg2 Bg7 4. Nf3 c6 5. O-O Nh6 
Dutch, Leningrad, Karlsbad variation
c018d658-0452-4063-84e2-22d457f755c5
1. d4 f5 2. g3 g6 3. Bg2 Bg7 4. Nh3
******A82: Dutch, Staunton gambit
Dutch, Staunton gambit
93cd95c8-a67a-4c65-b1b7-8124b96f2470
1. d4 f5 2. e4
Dutch, Balogh defence
31ff8455-c052-4113-8670-312f977d5b51
1. d4 f5 2. e4 d6 
Dutch, Staunton gambit
550c3aeb-a313-4388-a19f-17408e81060a
1. d4 f5 2. e4 fxe4 
Dutch, Staunton gambit, Tartakower variation
a59298f1-2b06-4f89-b3db-459e73ad6273
1. d4 f5 2. e4 fxe4 3. Nc3 Nf6 4. g4
******A83: Dutch, Staunton gambit, Staunton's line
Dutch, Staunton gambit, Staunton's line
d2074c35-1da6-4283-b967-57b228543a12
1. d4 f5 2. e4 fxe4 3. Nc3 Nf6 4. Bg5
Dutch, Staunton gambit, Alekhine variation
459f3b16-9458-4ed5-b36a-b39d4c2c93f9
1. d4 f5 2. e4 fxe4 3. Nc3 Nf6 4. Bg5 g6 5. h4
Dutch, Staunton gambit, Lasker variation
d32ae406-f682-415b-afbc-1b6bd64c9ff8
1. d4 f5 2. e4 fxe4 3. Nc3 Nf6 4. Bg5 g6 5. f3
Dutch, Staunton gambit, Chigorin variation
5cf4f6ec-41ac-4f6b-bf48-94745de1f2f3
1. d4 f5 2. e4 fxe4 3. Nc3 Nf6 4. Bg5 c6 
Dutch, Staunton gambit, Nimzovich variation
48a80771-c8f5-4fc6-a94a-ac747786c091
1. d4 f5 2. e4 fxe4 3. Nc3 Nf6 4. Bg5 b6 
******A84: Dutch defence
Dutch defence
cc93fb07-23cd-4558-9b5b-9218b60aaac1
1. d4 f5 2. c4
Dutch defence, Bladel variation
f63f2237-5952-422e-9b76-66ded95e55e6
1. d4 f5 2. c4 g6 3. Nc3 Nh6 
Dutch defence
ef943ecd-0d84-4980-9120-329d14faf844
1. d4 f5 2. c4 e6 
Dutch defence, Rubinstein variation
85f09cd8-334a-48df-8767-5e0607812734
1. d4 f5 2. c4 e6 3. Nc3
Dutch, Staunton gambit deferred
af8d148f-8e66-4479-8e38-ee41a16cc7a8
1. d4 f5 2. c4 e6 3. e4
Dutch defence
431bfc00-09fc-482e-818e-172f5171c658
1. d4 f5 2. c4 Nf6 
******A85: Dutch with c4 & Nc3
Dutch with c4 & Nc3
d6640a0f-bbfd-4728-b8a2-a1a86a0b21a3
1. d4 f5 2. c4 Nf6 3. Nc3
******A86: Dutch with c4 & g3
Dutch with c4 & g3
5e60e7fc-0ebb-4929-9f2d-5b416bc8a359
1. d4 f5 2. c4 Nf6 3. g3
Dutch, Hort-Antoshin system
af672fc4-2906-464a-9fbe-99a6053dd6fb
1. d4 f5 2. c4 Nf6 3. g3 d6 4. Bg2 c6 5. Nc3 Qc7 
Dutch, Leningrad variation
3faded0c-cf87-4b85-bfae-6e19da0a5bdd
1. d4 f5 2. c4 Nf6 3. g3 g6 
******A87: Dutch, Leningrad, main variation
Dutch, Leningrad, main variation
44c150e9-914a-44eb-88fa-fc87d2865546
1. d4 f5 2. c4 Nf6 3. g3 g6 4. Bg2 Bg7 5. Nf3
******A88: Dutch, Leningrad, main variation with c6
Dutch, Leningrad, main variation with c6
242ee77a-8ae9-49d1-89a4-cad720a1f28e
1. d4 f5 2. c4 Nf6 3. g3 g6 4. Bg2 Bg7 5. Nf3 O-O 6. O-O d6 7. Nc3 c6 
******A89: Dutch, Leningrad, main variation with Nc6
Dutch, Leningrad, main variation with Nc6
85d82cf7-61e5-490c-ac95-53052962d8df
1. d4 f5 2. c4 Nf6 3. g3 g6 4. Bg2 Bg7 5. Nf3 O-O 6. O-O d6 7. Nc3 Nc6 
******A90: Dutch defence
Dutch defence
28e09a0a-f06e-4ea2-8023-9ac24d8c8246
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2
Dutch defence, Dutch-Indian (Nimzo-Dutch) variation
3518022d-2b34-4c4e-b2ea-e314a43f5740
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Bb4+ 
Dutch-Indian, Alekhine variation
f2067b98-ea32-4f1d-92df-59e2a37726da
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Bb4+ 5. Bd2 Be7 
******A91: Dutch defence
Dutch defence
6cd11758-2ee1-4c42-b497-7b2d98f34d1c
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 
******A92: Dutch defence
Dutch defence
8fa96278-6304-47b4-add7-a2699e74c8cb
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 5. Nf3 O-O 
Dutch defence, Alekhine variation
82ae24bb-4094-4f7a-a163-6ffe8b12e411
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 5. Nf3 O-O 6. O-O Ne4 
Dutch, stonewall variation
7f72ec51-9c36-44aa-a7d9-2af82a57f4e5
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 5. Nf3 O-O 6. O-O d5 
Dutch, stonewall with Nc3
5b50a0c3-2425-4c65-9949-e00765c124ec
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 5. Nf3 O-O 6. O-O d5 7. Nc3
******A93: Dutch, stonewall, Botwinnik variation
Dutch, stonewall, Botwinnik variation
07176b6c-db1e-4c96-bbd3-afb39f85f808
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 5. Nf3 O-O 6. O-O d5 7. b3
******A94: Dutch, stonewall with Ba3
Dutch, stonewall with Ba3
198703cb-eeb0-4bde-bcf7-cf1ab81be1b6
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 5. Nf3 O-O 6. O-O d5 7. b3 c6 8. Ba3
******A95: Dutch, stonewall with Nc3
Dutch, stonewall with Nc3
6fd98fb6-d9d6-4fbc-a432-306ffe465dfe
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 5. Nf3 O-O 6. O-O d5 7. Nc3 c6 
Dutch, stonewall: Chekhover variation
50155ff6-5999-499d-b8fe-d6a5e361b07f
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 5. Nf3 O-O 6. O-O d5 7. Nc3 c6 8. Qc2 Qe8 9. Bg5
******A96: Dutch, classical variation
Dutch, classical variation
2490ed2d-5d3f-48b7-9e20-1c30f105611c
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 5. Nf3 O-O 6. O-O d6 
******A97: Dutch, Ilyin-Genevsky variation
Dutch, Ilyin-Genevsky variation
cd625eb6-adfd-4772-a850-c51399a59e08
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 5. Nf3 O-O 6. O-O d6 7. Nc3 Qe8 
Dutch, Ilyin-Genevsky, Winter variation
e1b8497c-9898-4f31-8017-eba744ec4725
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 5. Nf3 O-O 6. O-O d6 7. Nc3 Qe8 8. Re1
******A98: Dutch, Ilyin-Genevsky variation with Qc2
Dutch, Ilyin-Genevsky variation with Qc2
cf407db2-4f78-45ca-8055-ef82675ff909
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 5. Nf3 O-O 6. O-O d6 7. Nc3 Qe8 8. Qc2
******A99: Dutch, Ilyin-Genevsky variation with b3
Dutch, Ilyin-Genevsky variation with b3
a64efcb5-2521-4997-bf09-9787b3c86371
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 5. Nf3 O-O 6. O-O d6 7. Nc3 Qe8 8. b3
******B00: King's pawn opening
King's pawn opening
f1531abf-39e8-422b-8905-700bb22d4d31
1. e4
Hippopotamus defence
98640a40-c6b8-414a-881a-edafcdcf354c
1. e4 Nh6 2. d4 g6 3. c4 f6 
Corn stalk defence
24c881ab-a3df-4c9d-8b3a-b23fa20c1858
1. e4 a5 
Lemming defence
946b29b1-25cb-4bce-8d67-1304d78c829e
1. e4 Na6 
Fred
e9893b04-dcbc-4fd7-829e-67140e6284ad
1. e4 f5 
Barnes defence
9ea7e241-3bcd-4cb3-bb41-ecfb689d32fd
1. e4 f6 
Fried fox defence
fde3f5b8-06dd-4507-824e-e7c9f30da8ab
1. e4 f6 2. d4 Kf7 
Carr's defence
419229f9-7fdc-4121-982f-1b0051abaf01
1. e4 h6 
Reversed Grob (Borg/Basman defence/macho Grob)
c96d59a1-6d80-4327-9532-93672585e6db
1. e4 g5 
St. George (Baker) defence
dd722d07-c637-49df-aae1-135a80fce536
1. e4 a6 
Owen defence
cc377386-8649-4de8-b988-e38131547eb6
1. e4 b6 
Guatemala defence
a6e7c8a9-aa72-42e5-8bef-6046f622dd66
1. e4 b6 2. d4 Ba6 
KP, Nimzovich defence
47078be5-6199-4410-80cb-10bd4516cd47
1. e4 Nc6 
KP, Nimzovich defence, Wheeler gambit
4f62362e-3b74-4731-bee4-8992e6f4bcb6
1. e4 Nc6 2. b4 Nxb4 3. c3 Nc6 4. d4
KP, Nimzovich defence
cdabd1a5-d2d8-42a1-8055-8ddf968c0770
1. e4 Nc6 2. Nf3
KP, Colorado counter
0b881ba5-66e1-4de0-b084-9384be462cae
1. e4 Nc6 2. Nf3 f5 
KP, Nimzovich defence
a5534063-a5a8-4daa-b0a0-33ca950482fd
1. e4 Nc6 2. d4
KP, Nimzovich defence, Marshall gambit
0be0be76-dbfe-4d63-bcf6-c9c8719be6c3
1. e4 Nc6 2. d4 d5 3. exd5 Qxd5 4. Nc3
KP, Nimzovich defence, Bogolyubov variation
f8351c2d-4f95-4c44-a48a-f7a436c0bf76
1. e4 Nc6 2. d4 d5 3. Nc3
KP, Neo-Mongoloid defence
a351a4df-0fcc-4adf-8df7-e4c9d83c9809
1. e4 Nc6 2. d4 f6 
******B01: Scandinavian (centre counter) defence
Scandinavian (centre counter) defence
3ed84f1e-1f8a-4fd3-bde3-200602f7b870
1. e4 d5 
Scandinavian defence, Lasker variation
30289852-31f6-4931-b2f5-0dd9a18674f7
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qa5 4. d4 Nf6 5. Nf3 Bg4 6. h3
Scandinavian defence
e7d92cea-09e9-4ab1-9856-41d2d48d3d96
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qa5 4. d4 Nf6 5. Nf3 Bf5 
Scandinavian defence, Gruenfeld variation
4c6e0827-8be9-4f5a-8969-de670c8e233f
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qa5 4. d4 Nf6 5. Nf3 Bf5 6. Ne5 c6 7. g4
Scandinavian, Anderssen counter-attack
bd695c9a-2219-4e31-86c8-5b4be41ca48a
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qa5 4. d4 e5 
Scandinavian, Anderssen counter-attack orthodox attack
786934b5-5fba-4a65-8238-91a5a389c206
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qa5 4. d4 e5 5. dxe5 Bb4 6. Bd2 Nc6 7. Nf3
Scandinavian, Anderssen counter-attack, Goteborg system
59e0dfcb-3a5d-49d8-a9db-f57afa38479e
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qa5 4. d4 e5 5. Nf3
Scandinavian, Anderssen counter-attack, Collijn variation
06985fd5-662d-4a4f-aeb9-3c8b13f48090
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qa5 4. d4 e5 5. Nf3 Bg4 
Scandinavian, Mieses-Kotrvc gambit
19a4890d-81c0-450f-83d7-c9dab7c07888
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qa5 4. b4
Scandinavian, Pytel-Wade variation
562b41b3-b13f-4541-a9d0-54a6f371692e
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qd6 
Scandinavian defence
f6567627-95a2-40c3-a21d-d791a488c14f
1. e4 d5 2. exd5 Nf6 
Scandinavian, Icelandic gambit
e0040aea-ed15-4ce0-b5e0-18eec06457bc
1. e4 d5 2. exd5 Nf6 3. c4 e6 
Scandinavian gambit
1d96cc20-5a0d-4211-acce-92dd0661a5b1
1. e4 d5 2. exd5 Nf6 3. c4 c6 
Scandinavian defence
b451abc7-7885-465f-b454-3ab72d4bdb55
1. e4 d5 2. exd5 Nf6 3. d4
Scandinavian, Marshall variation
1801d917-aff7-4ac0-9752-15ae3c445403
1. e4 d5 2. exd5 Nf6 3. d4 Nxd5 
Scandinavian, Kiel variation
4bdbdefb-aaca-4d2b-b425-e08ed111b292
1. e4 d5 2. exd5 Nf6 3. d4 Nxd5 4. c4 Nb4 
Scandinavian, Richter variation
477fb766-a17c-4d86-8129-993ff9983d7f
1. e4 d5 2. exd5 Nf6 3. d4 g6 
******B02: Alekhine's defence
Alekhine's defence
69234ccf-f44a-45c7-b375-cc6e2417fbf9
1. e4 Nf6 
Alekhine's defence, Scandinavian variation
3a9305a1-729a-4a21-88a4-d44031fd9d08
1. e4 Nf6 2. Nc3 d5 
Alekhine's defence, Spielmann variation
5100b327-6bad-45db-9d1b-b0a50ab6fa28
1. e4 Nf6 2. Nc3 d5 3. e5 Nfd7 4. e6
Alekhine's defence, Maroczy variation
a1474685-982b-4493-ad13-f64b1d81f705
1. e4 Nf6 2. d3
Alekhine's defence, Krejcik variation
20a54de9-956c-4f15-957e-50e7db842aaa
1. e4 Nf6 2. Bc4
Alekhine's defence, Mokele Mbembe (Buecker) variation
d421fd4f-b216-4d6e-99c0-eca226a03663
1. e4 Nf6 2. e5 Ne4 
Alekhine's defence, Brooklyn defence
92a957ac-38e1-481b-a7cc-4fb3f737f421
1. e4 Nf6 2. e5 Ng8 
Alekhine's defence
83ef6e52-550f-4213-b377-3938f1106918
1. e4 Nf6 2. e5 Nd5 
Alekhine's defence, Kmoch variation
7d162284-ff63-48dc-936e-2f0065a13bdc
1. e4 Nf6 2. e5 Nd5 3. Bc4 Nb6 4. Bb3 c5 5. d3
Alekhine's defence, Saemisch attack
7a63d92c-8f9d-476c-a390-9915e3699a48
1. e4 Nf6 2. e5 Nd5 3. Nc3
Alekhine's defence, Welling variation
3573be8e-c9f9-40b3-b283-e4716074e490
1. e4 Nf6 2. e5 Nd5 3. b3
Alekhine's defence
fdb6657f-4d10-4b03-bd3d-baf80613c570
1. e4 Nf6 2. e5 Nd5 3. c4
Alekhine's defence, Steiner variation
879b1a75-733f-40b0-99ca-84c6ffc14bf0
1. e4 Nf6 2. e5 Nd5 3. c4 Nb6 4. b3
Alekhine's defence, two pawns' (Lasker's) attack
61c539da-07c4-4858-8bc2-3ca944e8539e
1. e4 Nf6 2. e5 Nd5 3. c4 Nb6 4. c5
Alekhine's defence, two pawns' attack, Mikenas variation
b89fcfe9-c14f-4b94-98c1-c69033887e70
1. e4 Nf6 2. e5 Nd5 3. c4 Nb6 4. c5 Nd5 5. Bc4 e6 6. Nc3 d6 
******B03: Alekhine's defence
Alekhine's defence
8eb4f72d-7acc-4cf5-b283-28eb14ca6af5
1. e4 Nf6 2. e5 Nd5 3. d4
Alekhine's defence, O'Sullivan gambit
ec006fb6-d3de-4779-99f9-9355c141eef9
1. e4 Nf6 2. e5 Nd5 3. d4 b5 
Alekhine's defence
96dadc96-e3f7-4492-88cf-f041d0424156
1. e4 Nf6 2. e5 Nd5 3. d4 d6 
Alekhine's defence, Balogh variation
f8fc73d7-044c-40aa-997c-ac16ec56a414
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. Bc4
Alekhine's defence
cf3224f3-530e-45cf-8055-649c32adcbb2
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. c4
Alekhine's defence, exchange variation
f4c6db27-71a8-4cb4-a953-28b1aaba521b
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. c4 Nb6 5. exd6
Alekhine's defence, exchange, Karpov variation
43040f91-b10a-49c2-8575-dc58dd551337
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. c4 Nb6 5. exd6 cxd6 6. Nf3 g6 7. Be2 Bg7 8. O-O O-O 9. h3 Nc6 10. Nc3 Bf5 11. Bf4
Alekhine's defence, four pawns attack
da80254c-d4d6-499d-8f61-42b157b83509
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. c4 Nb6 5. f4
Alekhine's defence, four pawns attack, Korchnoi variation
ecf4387e-41e0-430b-96ff-db05f231129c
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. c4 Nb6 5. f4 dxe5 6. fxe5 Bf5 7. Nc3 e6 8. Nf3 Be7 9. Be2 O-O 10. O-O f6 
Alekhine's defence, four pawns attack, 6...Nc6
f84bbd40-ce03-4e6c-8247-a1a574ab1042
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. c4 Nb6 5. f4 dxe5 6. fxe5 Nc6 
Alekhine's defence, four pawns attack, Ilyin-Genevsky var.
e00ce660-1b24-4e90-9e34-a8f1b94134ec
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. c4 Nb6 5. f4 dxe5 6. fxe5 Nc6 7. Nf3 Bg4 8. e6 fxe6 9. c5
Alekhine's defence, four pawns attack, 7.Be3
ca6f2354-1d21-4ca8-b58c-4c530690abdc
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. c4 Nb6 5. f4 dxe5 6. fxe5 Nc6 7. Be3
Alekhine's defence, four pawns attack, Tartakower variation
6501c11a-a406-41d5-87e9-b8e3f80ced70
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. c4 Nb6 5. f4 dxe5 6. fxe5 Nc6 7. Be3 Bf5 8. Nc3 e6 9. Nf3 Qd7 10. Be2 O-O-O 11. O-O Be7 
Alekhine's defence, four pawns attack, Planinc variation
07e5d387-d5ac-4d48-b3ee-b2fadf261cf0
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. c4 Nb6 5. f4 g5 
Alekhine's defence, four pawns attack, fianchetto variation
82298f48-11f3-48e7-9576-ab7a9b603505
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. c4 Nb6 5. f4 g6 
Alekhine's defence, four pawns attack, Trifunovic variation
de6011f6-5480-4c8f-88a5-96f50fe1dae8
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. c4 Nb6 5. f4 Bf5 
******B04: Alekhine's defence, modern variation
Alekhine's defence, modern variation
bac8f8b0-04ee-4916-9a47-eff60f8ab5e8
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. Nf3
Alekhine's defence, modern, Larsen variation
aff66e5f-c6f9-4774-ba88-50519252fe76
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. Nf3 dxe5 
Alekhine's defence, modern, Schmid variation
89cafd54-4808-4ebe-b779-321cbbcaacbd
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. Nf3 Nb6 
Alekhine's defence, modern, fianchetto variation
ce0f340a-08a6-4536-a789-a6a1a11edb1e
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. Nf3 g6 
Alekhine's defence, modern, Keres variation
cb3821fa-3374-4463-8a70-3c9a99ed4f51
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. Nf3 g6 5. Bc4 Nb6 6. Bb3 Bg7 7. a4
******B05: Alekhine's defence, modern variation, 4...Bg4
Alekhine's defence, modern variation, 4...Bg4
0ab9d550-2699-4fcd-af1f-f31a46efcd6e
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. Nf3 Bg4 
Alekhine's defence, modern, Flohr variation
71a1d5a9-8fea-4f2b-9de5-86e3140dee95
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. Nf3 Bg4 5. Be2 c6 
Alekhine's defence, modern, Panov variation
5620d592-44c5-4c36-87e5-998ab51b5779
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. Nf3 Bg4 5. h3
Alekhine's defence, modern, Alekhine variation
1230d220-9fae-4ab0-aeb7-f8d7d7626781
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. Nf3 Bg4 5. c4
Alekhine's defence, modern, Vitolins attack
492e4251-741e-4a8b-b6fe-fc5d1fdf9be4
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. Nf3 Bg4 5. c4 Nb6 6. d5
******B06: Robatsch (modern) defence
Robatsch (modern) defence
d21d7ec3-4c7e-40ca-952b-c1dae881957d
1. e4 g6 
Norwegian defence
553fa0b5-8464-45d5-9f26-98ca4dac98b2
1. e4 g6 2. d4 Nf6 3. e5 Nh5 4. g4 Ng7 
Robatsch (modern) defence
53d13891-72c4-47f8-8d92-5abfff891153
1. e4 g6 2. d4 Bg7 
Robatsch defence, three pawns attack
87158235-62ed-4e01-8afb-c000f492627f
1. e4 g6 2. d4 Bg7 3. f4
Robatsch defence
21258c03-bbbd-4ced-ac39-684f4ad67e30
1. e4 g6 2. d4 Bg7 3. Nc3
Robatsch defence, Gurgenidze variation
2dd20bbc-9a5c-4439-acd3-bab91fb1fb68
1. e4 g6 2. d4 Bg7 3. Nc3 c6 4. f4 d5 5. e5 h5 
Robatsch (modern) defence
86fb0204-e010-4479-827a-0a249e762f1d
1. e4 g6 2. d4 Bg7 3. Nc3 d6 
Robatsch defence, two knights variation
cb1522d9-5b3d-4297-aced-c1fe37342798
1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Nf3
Robatsch defence, two knights, Suttles variation
ca82f54b-c478-45a5-8c9e-235086ec174f
1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Nf3 c6 
Robatsch defence, Pseudo-Austrian attack
3185424f-4611-45bb-8e1d-2aeee1d5b0a6
1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. f4
******B07: Pirc defence
Pirc defence
d108dd0b-3c6f-4e68-b7ef-72c5b20a120e
1. e4 d6 2. d4 Nf6 3. Nc3
Pirc, Ufimtsev-Pytel variation
6204a33b-312c-4059-917f-568662adba61
1. e4 d6 2. d4 Nf6 3. Nc3 c6 
Pirc defence
c86fad09-0e13-4ea2-89d9-a8bf3a23072d
1. e4 d6 2. d4 Nf6 3. Nc3 g6 
Pirc, 150 attack
31cd41d5-8165-4b21-a11a-4e426c1441c0
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. Be3 c6 5. Qd2
Pirc, Sveshnikov system
d9dd3985-0f8a-4d0f-9950-eab7b162d80e
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. g3
Pirc, Holmov system
b4a410c4-40e2-4c16-9359-6db4ba351ade
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. Bc4
Pirc, Byrne variation
1bd69e24-8cf1-4eb9-a960-86bc461972cc
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. Bg5
Pirc defence
0140eaea-54d5-494f-92cd-9ebf9389fe4c
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. Be2
Pirc, Chinese variation
fa5e4011-a6d8-4063-867f-c605630aa6b8
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. Be2 Bg7 5. g4
Pirc, bayonet (Mariotti) attack
045ca20d-281a-405b-bb54-f5854951ddcc
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. Be2 Bg7 5. h4
Robatsch defence, Geller's system
0b5c7bff-ac34-44bf-8c21-412db1ea3668
1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. c3
******B08: Pirc, classical (two knights) system
Pirc, classical (two knights) system
c4cb4a8a-7068-4412-840a-082af65b7b44
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. Nf3
Pirc, classical (two knights) system
a09a813d-4596-4d85-9e92-3b7ed5d410d2
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. Nf3 Bg7 
Pirc, classical, h3 system
65f3be21-1ab3-4d80-93cd-6e44902719aa
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. Nf3 Bg7 5. h3
Pirc, classical system, 5.Be2
7f6200aa-e9cf-47cd-9a82-76f62740638b
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. Nf3 Bg7 5. Be2
******B09: Pirc, Austrian attack
Pirc, Austrian attack
ab056767-ac2d-48b7-8f58-d3aae2a8ce51
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. f4
Pirc, Austrian attack
b36070e7-2eb5-43ef-94fb-45dd8463da35
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. f4 Bg7 5. Nf3 O-O 
Pirc, Austrian attack, 6.e5
d728db0e-c5dd-4cc7-87c5-0e7b38db4aaa
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. f4 Bg7 5. Nf3 O-O 6. e5
Pirc, Austrian attack, 6.Be3
e8f3831b-3bc7-49ef-8df0-08833b8e3e7d
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. f4 Bg7 5. Nf3 O-O 6. Be3
Pirc, Austrian attack, 6.Bd3
ef5d0bf3-5eed-4d76-ade2-50a8c3b6f2ac
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. f4 Bg7 5. Nf3 O-O 6. Bd3
Pirc, Austrian attack, dragon formation
454fc1ea-5223-4f9f-8478-0e762b625b15
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. f4 Bg7 5. Nf3 c5 
Pirc, Austrian attack, Ljubojevic variation
d2fdfccb-a9c8-4ccd-ab1c-2c5cef31813b
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. f4 Bg7 5. Bc4
******B10: Caro-Kann defence
Caro-Kann defence
0fc04bd2-0d27-4652-b332-9e2ffbd3be4c
1. e4 c6 
Caro-Kann, Hillbilly attack
5d2c3628-2057-4a32-9bc7-7633869ac0d8
1. e4 c6 2. Bc4
Caro-Kann, anti-Caro-Kann defence
1e151666-0559-49b7-ae07-0ae8e35e47c2
1. e4 c6 2. c4
Caro-Kann, anti-anti-Caro-Kann defence
6f9eece5-6b51-41c4-b15d-96e35b949a8f
1. e4 c6 2. c4 d5 
Caro-Kann, closed (Breyer) variation
7341d843-bb62-4168-9ad4-4329ed3b700b
1. e4 c6 2. d3
Caro-Kann defence
4839c8b7-9663-4fae-9683-8e9410f6e93c
1. e4 c6 2. Nc3
Caro-Kann, Goldman (Spielmann) variation
d76ad4a2-4208-4f26-b745-1aaa03d0ae8a
1. e4 c6 2. Nc3 d5 3. Qf3
Caro-Kann, two knights variation
56a31f07-d4b4-4bc4-9393-926323c55dd6
1. e4 c6 2. Nc3 d5 3. Nf3
******B11: Caro-Kann, two knights, 3...Bg4
Caro-Kann, two knights, 3...Bg4
ed86bc4a-193f-43b6-80a2-8b852bd2e630
1. e4 c6 2. Nc3 d5 3. Nf3 Bg4 
******B12: Caro-Kann defence
Caro-Kann defence
87b26d05-c71f-42c7-8cc7-1e8b6cbd0224
1. e4 c6 2. d4
de Bruycker defence
e35abe94-3867-4625-bc4d-d91e2e0a4556
1. e4 c6 2. d4 Na6 3. Nc3 Nc7 
Caro-Masi defence
2b58c6bf-2205-4b45-b609-2757ed066d02
1. e4 c6 2. d4 Nf6 
Caro-Kann defence
8c8f8ef6-b2d6-4945-b6e4-035273b3b2e3
1. e4 c6 2. d4 d5 
Caro-Kann, Tartakower (fantasy) variation
3460ee07-7900-4645-8d2d-67bff571c3d8
1. e4 c6 2. d4 d5 3. f3
Caro-Kann, 3.Nd2
ffea7204-a272-496e-b8b4-e688f853e057
1. e4 c6 2. d4 d5 3. Nd2
Caro-Kann, Edinburgh variation
e82f912c-c0d5-48a8-a91b-aed44a4458ac
1. e4 c6 2. d4 d5 3. Nd2 Qb6 
Caro-Kann, advance variation
45b1319b-11fd-43f9-8ff1-ac75d7e24bcb
1. e4 c6 2. d4 d5 3. e5
Caro-Kann, advance, Short variation
5d5c4352-220f-4fa9-8b27-57ae4cb3dc0d
1. e4 c6 2. d4 d5 3. e5 Bf5 4. c3 e6 5. Be2
******B13: Caro-Kann, exchange variation
Caro-Kann, exchange variation
d38d085d-964d-4163-ba18-54c034000b33
1. e4 c6 2. d4 d5 3. exd5
Caro-Kann, exchange, Rubinstein variation
5d754f01-9d54-4149-a419-0a8de4fa8bad
1. e4 c6 2. d4 d5 3. exd5 cxd5 4. Bd3 Nc6 5. c3 Nf6 6. Bf4
Caro-Kann, Panov-Botvinnik attack
a44c3cab-488a-4724-9c24-ea6a8de8a028
1. e4 c6 2. d4 d5 3. exd5 cxd5 4. c4
Caro-Kann, Panov-Botvinnik, Gunderam attack
02ea270e-ddf6-4169-b58b-e38845a97930
1. e4 c6 2. d4 d5 3. exd5 cxd5 4. c4 Nf6 5. c5
Caro-Kann, Panov-Botvinnik attack
404815fb-0e3e-4969-919a-14f7ca5295a0
1. e4 c6 2. d4 d5 3. exd5 cxd5 4. c4 Nf6 5. Nc3
Caro-Kann, Panov-Botvinnik, Herzog defence
0ca3750e-a96e-43ec-899d-8def198ffaa6
1. e4 c6 2. d4 d5 3. exd5 cxd5 4. c4 Nf6 5. Nc3 Nc6 6. Bg5 dxc4 7. d5 Na5 
Caro-Kann, Panov-Botvinnik, normal variation
702f5bf4-c2b1-4820-80dc-82950f7d3163
1. e4 c6 2. d4 d5 3. exd5 cxd5 4. c4 Nf6 5. Nc3 Nc6 6. Bg5 e6 
Caro-Kann, Panov-Botvinnik, Czerniak variation
a57e2295-ef2c-464b-a192-9f3959c9a10e
1. e4 c6 2. d4 d5 3. exd5 cxd5 4. c4 Nf6 5. Nc3 Nc6 6. Bg5 Qa5 
Caro-Kann, Panov-Botvinnik, Reifir (Spielmann) variation
2c0bbf02-fb2d-4a9e-87e5-3f8a820337d4
1. e4 c6 2. d4 d5 3. exd5 cxd5 4. c4 Nf6 5. Nc3 Nc6 6. Bg5 Qb6 
******B14: Caro-Kann, Panov-Botvinnik attack, 5...e6
Caro-Kann, Panov-Botvinnik attack, 5...e6
1a683371-5ac1-4e07-ad16-f121e77bea49
1. e4 c6 2. d4 d5 3. exd5 cxd5 4. c4 Nf6 5. Nc3 e6 
Caro-Kann, Panov-Botvinnik attack, 5...g6
ab389b96-8d43-45e1-bb7f-bae216b2f91b
1. e4 c6 2. d4 d5 3. exd5 cxd5 4. c4 Nf6 5. Nc3 g6 
******B15: Caro-Kann defence
Caro-Kann defence
a83b1720-a40e-4c57-b43f-3ae7d47f2d74
1. e4 c6 2. d4 d5 3. Nc3
Caro-Kann, Gurgenidze counter-attack
813bd92e-91a8-404d-9a56-25ab767a4b69
1. e4 c6 2. d4 d5 3. Nc3 b5 
Caro-Kann, Gurgenidze system
769bd335-7e2f-4124-8d24-7d555e321c70
1. e4 c6 2. d4 d5 3. Nc3 g6 
Caro-Kann, Rasa-Studier gambit
ab86b708-e9d6-4892-a7f8-a2588089e5d2
1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. f3
Caro-Kann defence
05fc662f-98bd-41b7-a291-67666403cd3f
1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4
Caro-Kann, Alekhine gambit
310a674a-661b-4f83-896b-d00003197504
1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Nf6 5. Bd3
Caro-Kann, Tartakower (Nimzovich) variation
88f85115-2609-471a-9dd8-51621b1cf529
1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Nf6 5. Nxf6+ exf6 
Caro-Kann, Forgacs variation
f9ffa3ff-3627-4d2b-bbba-c312a9a8dc3b
1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Nf6 5. Nxf6+ exf6 6. Bc4
******B16: Caro-Kann, Bronstein-Larsen variation
Caro-Kann, Bronstein-Larsen variation
e63a0ca3-5ce0-42e7-91d0-30841c8604cc
1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Nf6 5. Nxf6+ gxf6 
******B17: Caro-Kann, Steinitz variation
Caro-Kann, Steinitz variation
cb11d08e-d677-4863-b79f-c43bb5bd94a7
1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Nd7 
******B18: Caro-Kann, classical variation
Caro-Kann, classical variation
08f9b058-e490-4d1c-88d2-c70a733d82a9
1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Bf5 
Caro-Kann, classical, Flohr variation
5e926820-9807-4648-9c63-ecf2e9efe731
1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Bf5 5. Ng3 Bg6 6. Nh3
Caro-Kann, classical, Maroczy attack
3d79813c-2dc7-490f-af14-10159857cce2
1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Bf5 5. Ng3 Bg6 6. f4
Caro-Kann, classical, 6.h4
7de6ca07-9e09-4d06-8533-5f7b31db4475
1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Bf5 5. Ng3 Bg6 6. h4
******B19: Caro-Kann, classical, 7...Nd7
Caro-Kann, classical, 7...Nd7
9ae77fff-0786-4d10-9b2d-89e150aafda1
1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Bf5 5. Ng3 Bg6 6. h4 h6 7. Nf3 Nd7 
Caro-Kann, classical, Spassky variation
62903734-ba05-4d20-bf2a-b98deeba7351
1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Bf5 5. Ng3 Bg6 6. h4 h6 7. Nf3 Nd7 8. h5
******B20: Sicilian defence
Sicilian defence
d7a2f8ec-3283-411c-847d-8cd56f72ed86
1. e4 c5 
Sicilian, Gloria variation
34c812fa-cb74-426c-8564-c79bd7ee8138
1. e4 c5 2. c4 d6 3. Nc3 Nc6 4. g3 h5 
Sicilian, Steinitz variation
6ed32707-9bc4-43ce-a020-01d15a35a200
1. e4 c5 2. g3
Sicilian, wing gambit
f28b5333-6637-4a4f-9aea-f87d4ad4349b
1. e4 c5 2. b4
Sicilian, wing gambit, Santasiere variation
d4b901ed-3559-481c-aeff-32bc0efcaa33
1. e4 c5 2. b4 cxb4 3. c4
Sicilian, wing gambit, Marshall variation
bb691ee2-5420-4827-8558-4257348c7eec
1. e4 c5 2. b4 cxb4 3. a3
Sicilian, wing gambit, Marienbad variation
71dbc028-d16a-4b5a-97e7-3cb49fc5f3cb
1. e4 c5 2. b4 cxb4 3. a3 d5 4. exd5 Qxd5 5. Bb2
Sicilian, wing gambit, Carlsbad variation
490982d5-1b15-4268-ba30-ca416b1f476c
1. e4 c5 2. b4 cxb4 3. a3 bxa3 
Sicilian, Keres variation (2.Ne2)
a3ac3b75-1aca-4f79-af9b-589aa93cdabf
1. e4 c5 2. Ne2
******B21: Sicilian, Grand Prix attack
Sicilian, Grand Prix attack
33dd39dc-4d76-49f3-b4c2-3156340aba7f
1. e4 c5 2. f4
Sicilian, Smith-Morra gambit
8b5779b2-0d32-45a6-9d3e-c8ddbc5cf8e9
1. e4 c5 2. d4
Sicilian, Andreaschek gambit
cd3d3585-8140-4d46-9aa4-2325737362cd
1. e4 c5 2. d4 cxd4 3. Nf3 e5 4. c3
Sicilian, Smith-Morra gambit, 2...cxd4 3.c3
be4e100c-bf21-456b-bfc4-0a9a8134fbb8
1. e4 c5 2. d4 cxd4 3. c3
Sicilian, Smith-Morra gambit, Chicago defence
6a4f487d-32cd-469c-8d92-f121431dc13e
1. e4 c5 2. d4 cxd4 3. c3 dxc3 4. Nxc3 Nc6 5. Nf3 d6 6. Bc4 e6 7. O-O a6 8. Qe2 b5 9. Bb3 Ra7 
******B22: Sicilian, Alapin's variation (2.c3)
Sicilian, Alapin's variation (2.c3)
cc734181-818b-4724-bc48-5836ebd989c2
1. e4 c5 2. c3
Sicilian, 2.c3, Heidenfeld variation
148c635c-07bb-4306-a688-3cfac30ffe4e
1. e4 c5 2. c3 Nf6 3. e5 Nd5 4. Nf3 Nc6 5. Na3
******B23: Sicilian, closed
Sicilian, closed
d12c345e-6101-4e71-96b7-58adca323e25
1. e4 c5 2. Nc3
Sicilian, closed, Korchnoi variation
0cb89dd3-2e41-4b4f-bdf4-86701f93d9f5
1. e4 c5 2. Nc3 e6 3. g3 d5 
Sicilian, closed, 2...Nc6
e082c0a9-210c-4e85-9c64-e05c5f2b61d0
1. e4 c5 2. Nc3 Nc6 
Sicilian, chameleon variation
5778dab5-a9d7-4972-b7f1-552a2952f5eb
1. e4 c5 2. Nc3 Nc6 3. Nge2
Sicilian, Grand Prix attack
99fd0baf-172c-4cf8-8bbd-f5d4733dcec5
1. e4 c5 2. Nc3 Nc6 3. f4
Sicilian, Grand Prix attack, Schofman variation
4660ca84-7897-4633-8a27-3be08e2785d4
1. e4 c5 2. Nc3 Nc6 3. f4 g6 4. Nf3 Bg7 5. Bc4 e6 6. f5
******B24: Sicilian, closed
Sicilian, closed
1a6fcd50-5376-4932-a48e-b74789d5f93c
1. e4 c5 2. Nc3 Nc6 3. g3
Sicilian, closed, Smyslov variation
91961e44-b889-456f-b707-77ceb866ccb1
1. e4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. d3 e6 6. Be3 Nd4 7. Nce2
******B25: Sicilian, closed
Sicilian, closed
dd086521-b653-42ba-99ca-e468ad824f6e
1. e4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. d3 d6 
Sicilian, closed, 6.Ne2 e5 (Botvinnik)
d9661abe-1e62-470e-b60e-63e8d852effc
1. e4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. d3 d6 6. Nge2 e5 
Sicilian, closed, 6.f4
c2ef012a-7c49-4d6a-be7e-f8ec653b61c4
1. e4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. d3 d6 6. f4
Sicilian, closed, 6.f4 e5 (Botvinnik)
cdcd4c5d-39ad-486f-bdbb-cc23294995e9
1. e4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. d3 d6 6. f4 e5 
******B26: Sicilian, closed, 6.Be3
Sicilian, closed, 6.Be3
a981dd80-17a0-4fd5-b022-51daedf0076d
1. e4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. d3 d6 6. Be3
******B27: Sicilian defence
Sicilian defence
037ddc31-a89e-46f0-b67e-3233ac593392
1. e4 c5 2. Nf3
Sicilian, Stiletto (Althouse) variation
30b0b855-6985-4a7e-80cb-e0efa4af7ac7
1. e4 c5 2. Nf3 Qa5 
Sicilian, Quinteros variation
6782f68b-136f-4d22-8cc5-5e09f5d8d899
1. e4 c5 2. Nf3 Qc7 
Sicilian, Katalimov variation
b6990b9d-bc48-46a7-b965-9298ebb18535
1. e4 c5 2. Nf3 b6 
Sicilian, Hungarian variation
5da7fb4f-e93b-4cf8-a897-d0fb3b452335
1. e4 c5 2. Nf3 g6 
Sicilian, Acton extension
28eee378-5acc-4ec1-8bab-2dd42d556e30
1. e4 c5 2. Nf3 g6 3. c4 Bh6 
******B28: Sicilian, O'Kelly variation
Sicilian, O'Kelly variation
d9a0aab1-a34c-4cbf-b85f-4fbbd2d1d023
1. e4 c5 2. Nf3 a6 
******B29: Sicilian, Nimzovich-Rubinstein variation
Sicilian, Nimzovich-Rubinstein variation
b78017c5-d315-4958-a9d4-c406c3652bbd
1. e4 c5 2. Nf3 Nf6 
Sicilian, Nimzovich-Rubinstein; Rubinstein counter-gambit
6f20fc76-ae43-4496-9acb-568802bda8f0
1. e4 c5 2. Nf3 Nf6 3. e5 Nd5 4. Nc3 e6 5. Nxd5 exd5 6. d4 Nc6 
******B30: Sicilian defence
Sicilian defence
d1040f49-8ed6-4f38-be42-1eb95cded986
1. e4 c5 2. Nf3 Nc6 
Sicilian, Nimzovich-Rossolimo attack (without ...d6)
89663792-041d-4727-9a59-e13d07cb6766
1. e4 c5 2. Nf3 Nc6 3. Bb5
******B31: Sicilian, Nimzovich-Rossolimo attack (with ...g6, without ...d6)
Sicilian, Nimzovich-Rossolimo attack (with ...g6, without ...d6)
0d69b3c1-7d84-4edd-aec2-00b406a8b02c
1. e4 c5 2. Nf3 Nc6 3. Bb5 g6 
Sicilian, Nimzovich-Rossolimo attack, Gurgenidze variation
77db3d02-1738-4ecb-bb36-fa1909260da1
1. e4 c5 2. Nf3 Nc6 3. Bb5 g6 4. O-O Bg7 5. Re1 e5 6. b4
******B32: Sicilian defence
Sicilian defence
e390a907-04fb-47a0-9b9f-9c8347497e56
1. e4 c5 2. Nf3 Nc6 3. d4
Sicilian, Flohr variation
085fdd48-2687-4ed1-ac33-da93576e0674
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 Qc7 
Sicilian, Nimzovich variation
0117a0fe-fa8a-4201-93f3-b943f4b366fc
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 d5 
Sicilian, Labourdonnais-Loewenthal variation
4e564f6e-29e0-4ff5-af54-c941207003f2
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 e5 
Sicilian, Labourdonnais-Loewenthal (Kalashnikov) variation
8af441dd-916d-4d82-8142-4662014b1dba
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 e5 5. Nb5 d6 
******B33: Sicilian defence
Sicilian defence
80ea405e-4613-4df5-8363-0403fed337fe
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 Nf6 
Sicilian, Pelikan (Lasker/Sveshnikov) variation
e3ce46e2-fc7d-48ab-970f-ab09d6efdf5e
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e5 
Sicilian, Pelikan, Bird variation
df68e8d7-1252-449d-a57a-f00940ea9ffb
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e5 6. Ndb5 d6 7. Bg5 a6 8. Na3 Be6 
Sicilian, Pelikan, Chelyabinsk variation
92fb2a14-d213-41a8-a836-61ac31ee8d49
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e5 6. Ndb5 d6 7. Bg5 a6 8. Na3 b5 
Sicilian, Sveshnikov variation
d1cfabe6-b1e2-476f-9ca3-cd9f9d19655e
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e5 6. Ndb5 d6 7. Bg5 a6 8. Na3 b5 9. Bxf6 gxf6 10. Nd5 f5 
******B34: Sicilian, accelerated fianchetto, exchange variation
Sicilian, accelerated fianchetto, exchange variation
19405db1-9efc-48b4-b223-e6a3a0b7095c
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 g6 5. Nxc6
Sicilian, accelerated fianchetto, modern variation
a6486177-1499-4709-907f-10724d6e8566
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 g6 5. Nc3
******B35: Sicilian, accelerated fianchetto, modern variation with Bc4
Sicilian, accelerated fianchetto, modern variation with Bc4
64256c70-3020-4392-ac6f-576e6c36c593
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 g6 5. Nc3 Bg7 6. Be3 Nf6 7. Bc4
******B36: Sicilian, accelerated fianchetto, Maroczy bind
Sicilian, accelerated fianchetto, Maroczy bind
2e6ae2c1-be88-4e12-877d-4afdd535d028
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 g6 5. c4
Sicilian, accelerated fianchetto, Gurgenidze variation
5daa5438-b16b-4d48-8023-384d8c186599
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 g6 5. c4 Nf6 6. Nc3 Nxd4 7. Qxd4 d6 
******B37: Sicilian, accelerated fianchetto, Maroczy bind, 5...Bg7
Sicilian, accelerated fianchetto, Maroczy bind, 5...Bg7
75bbfa43-67ff-4009-b02e-fa6b2dd9f0f8
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 g6 5. c4 Bg7 
Sicilian, accelerated fianchetto, Simagin variation
f36b19ed-3920-419e-bb51-83e0c0755271
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 g6 5. c4 Bg7 6. Nc2 d6 7. Be2 Nh6 
******B38: Sicilian, accelerated fianchetto, Maroczy bind, 6.Be3
Sicilian, accelerated fianchetto, Maroczy bind, 6.Be3
051ecca2-90d8-484c-8141-11ee382d5d1c
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 g6 5. c4 Bg7 6. Be3
******B39: Sicilian, accelerated fianchetto, Breyer variation
Sicilian, accelerated fianchetto, Breyer variation
dc95fac2-2976-4ae8-994a-b8adecc988f3
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 g6 5. c4 Bg7 6. Be3 Nf6 7. Nc3 Ng4 
******B40: Sicilian defence
Sicilian defence
30a194d3-e082-4a4e-9a86-241a96995cd4
1. e4 c5 2. Nf3 e6 
Sicilian, Marshall variation
9b0d4092-ad79-4274-b0b8-6e9d651439e5
1. e4 c5 2. Nf3 e6 3. d4 d5 
Sicilian defence
3d0349fa-ba22-4bf2-987e-318639226939
1. e4 c5 2. Nf3 e6 3. d4 cxd4 
Sicilian, Anderssen variation
8faeda65-26ca-43ec-bcb5-caa46e1b0f7f
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nf6 
Sicilian, Pin variation (Sicilian counter-attack)
f6fd0440-6608-4c8f-99db-564fc595cd38
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Bb4 
Sicilian, Pin, Jaffe variation
43fb658a-7762-4659-bb0f-da424cc9650f
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Bb4 6. Bd3 e5 
Sicilian, Pin, Koch variation
7e98ed25-aa49-467f-b980-5fa9a6013f0f
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Bb4 6. e5
******B41: Sicilian, Kan variation
Sicilian, Kan variation
b7a99bc3-981f-4158-8307-32a2697e27b8
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 a6 
Sicilian, Kan, Maroczy bind (Reti variation)
321b9af6-a1a8-4f5f-aa89-f5a77a470c16
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 a6 5. c4
Sicilian, Kan, Maroczy bind - Bronstein variation
13ff0f24-f0fb-425f-af47-680da39c83ce
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 a6 5. c4 Nf6 6. Nc3 Bb4 7. Bd3 Nc6 8. Bc2
******B42: Sicilian, Kan, 5.Bd3
Sicilian, Kan, 5.Bd3
f6644207-98bf-4fc2-9548-fbd0d1749382
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 a6 5. Bd3
Sicilian, Kan, Gipslis variation
7544e3ef-4042-4e03-b7f3-53f273946784
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 a6 5. Bd3 Nf6 6. O-O d6 7. c4 g6 
Sicilian, Kan, Polugaievsky variation
f598826f-cc81-4896-8fc1-02143797b774
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 a6 5. Bd3 Bc5 
Sicilian, Kan, Swiss cheese variation
c9fb0062-9e05-408b-9731-d2590d8980be
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 a6 5. Bd3 g6 
******B43: Sicilian, Kan, 5.Nc3
Sicilian, Kan, 5.Nc3
7b7b01d3-e1cf-4b71-887f-d52321ec9c37
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 a6 5. Nc3
******B44: Sicilian defence
Sicilian defence
bb773fbf-ce9a-431c-adad-97f64366dbde
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nc6 
Sicilian, Szen (`anti-Taimanov') variation
25621900-3aca-4e6e-9df6-4c606b2dd80d
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nc6 5. Nb5
Sicilian, Szen, hedgehog variation
d2ff7f03-1035-4a8a-91e3-0486d0749c1a
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nc6 5. Nb5 d6 6. c4 Nf6 7. Nb1-c3 a6 8. Na3 Be7 9. Be2 O-O 10. O-O b6 
Sicilian, Szen variation, Dely-Kasparov gambit
89eeef77-12f3-40e6-be62-611f9c7c9248
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nc6 5. Nb5 d6 6. c4 Nf6 7. Nb1-c3 a6 8. Na3 d5 
******B45: Sicilian, Taimanov variation
Sicilian, Taimanov variation
b8a9812f-9fbf-4f1e-92a1-2ea0a2152489
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nc6 5. Nc3
Sicilian, Taimanov, American attack
b7d9fe17-0301-4a50-85d9-057df780a645
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nc6 5. Nc3 Nf6 6. Ndb5 Bb4 7. Nd6+
******B46: Sicilian, Taimanov variation
Sicilian, Taimanov variation
d0bef7fc-79dd-465a-9903-35f1b3d8a5c3
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nc6 5. Nc3 a6 
******B47: Sicilian, Taimanov (Bastrikov) variation
Sicilian, Taimanov (Bastrikov) variation
7c6eab81-f78f-4b97-89fb-5751601f7d43
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nc6 5. Nc3 Qc7 
******B48: Sicilian, Taimanov variation
Sicilian, Taimanov variation
e403218d-8265-4b59-8bf0-0dd390497778
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nc6 5. Nc3 Qc7 6. Be3
******B49: Sicilian, Taimanov variation
Sicilian, Taimanov variation
68812dfc-468a-4c02-9768-daa9d7415f72
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nc6 5. Nc3 Qc7 6. Be3 a6 7. Be2
******B50: Sicilian
Sicilian
ae3fa64c-2a63-4a7d-a691-d924e2ddc5ff
1. e4 c5 2. Nf3 d6 
Sicilian, wing gambit deferred
f1ce6aac-cf6e-472f-a307-2bc8c917becf
1. e4 c5 2. Nf3 d6 3. b4
******B51: Sicilian, Canal-Sokolsky (Nimzovich-Rossolimo, Moscow) attack
Sicilian, Canal-Sokolsky (Nimzovich-Rossolimo, Moscow) attack
c72f835f-ef60-42c7-b7bf-13ee088b7e5a
1. e4 c5 2. Nf3 d6 3. Bb5+
******B52: Sicilian, Canal-Sokolsky attack, 3...Bd7
Sicilian, Canal-Sokolsky attack, 3...Bd7
5c06db85-2fd1-470b-8c0e-71938033e63f
1. e4 c5 2. Nf3 d6 3. Bb5+ Bd7 
Sicilian, Canal-Sokolsky attack, Bronstein gambit
06fd24d5-0f69-4c79-a2af-cef885515cc5
1. e4 c5 2. Nf3 d6 3. Bb5+ Bd7 4. Bxd7+ Qxd7 5. O-O Nc6 6. c3 Nf6 7. d4
Sicilian, Canal-Sokolsky attack, Sokolsky variation
7813f0a2-5473-458f-92fc-78734de6d831
1. e4 c5 2. Nf3 d6 3. Bb5+ Bd7 4. Bxd7+ Qxd7 5. c4
******B53: Sicilian, Chekhover variation
Sicilian, Chekhover variation
731c3099-1eb1-4dc0-b51b-99940d341be9
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Qxd4
Sicilian, Chekhover, Zaitsev variation
ed7e42f4-15cf-4d23-9f24-86d532662c73
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Qxd4 Nc6 5. Bb5 Qd7 
******B54: Sicilian
Sicilian
0004c6b1-91bf-4200-9105-f89d99af4599
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4
Sicilian, Prins (Moscow) variation
f838109a-9210-4b28-8f99-6f5c0e5ca032
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. f3
******B55: Sicilian, Prins variation, Venice attack
Sicilian, Prins variation, Venice attack
561cea7c-44db-47ba-973e-03a111427028
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. f3 e5 6. Bb5+
******B56: Sicilian
Sicilian
edab8cb1-f57a-4ffa-aced-43432802f522
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3
Sicilian, Venice attack
f30cdddd-f382-4fd3-a4c5-e03d4b483d36
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e5 6. Bb5+
Sicilian
8083dcbe-3178-418e-8c96-bf251b05dddb
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 
******B57: Sicilian, Sozin, not Scheveningen
Sicilian, Sozin, not Scheveningen
ee041ee9-90b8-4f97-94ef-8a2b3f185022
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bc4
Sicilian, Magnus Smith trap
a2b467a6-4c87-472f-83ec-6fd148fd5d2e
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bc4 g6 7. Nxc6 bxc6 8. e5
Sicilian, Sozin, Benko variation
333871f8-46f0-415a-aeb6-1082f0b2b85b
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bc4 Qb6 
******B58: Sicilian, classical
Sicilian, classical
47a06e6b-c77c-4297-b2a4-8af7c8730953
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 d6 6. Be2
Sicilian, Boleslavsky variation
8dad2144-0ac1-4772-9d7a-77bbd303cd46
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 d6 6. Be2 e5 
Sicilian, Boleslavsky, Louma variation
7a7de177-fa7b-416c-9c41-81665f7f3860
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 d6 6. Be2 e5 7. Nxc6
******B59: Sicilian, Boleslavsky variation, 7.Nb3
Sicilian, Boleslavsky variation, 7.Nb3
92b0a2b3-a8fe-4a8c-b087-6fc560195b23
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 d6 6. Be2 e5 7. Nb3
******B60: Sicilian, Richter-Rauzer
Sicilian, Richter-Rauzer
159d3b35-7d4f-4856-97aa-f20dc9290b79
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5
Sicilian, Richter-Rauzer, Bondarevsky variation
594da262-d381-4e4d-b403-05ed954b0eed
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 g6 
Sicilian, Richter-Rauzer, Larsen variation
5a63bb2a-149d-4dff-940c-5850e9c7c50d
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 Bd7 
******B61: Sicilian, Richter-Rauzer, Larsen variation, 7.Qd2
Sicilian, Richter-Rauzer, Larsen variation, 7.Qd2
7d5227df-47cc-4860-9e89-1eca3d1946e9
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 Bd7 7. Qd2
******B62: Sicilian, Richter-Rauzer, 6...e6
Sicilian, Richter-Rauzer, 6...e6
dde0a8ac-37d2-46c0-869e-98a154c03283
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 
Sicilian, Richter-Rauzer, Podvebrady variation
1edeb79d-58af-4532-859b-04671f020a4f
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Nb3
Sicilian, Richter-Rauzer, Margate (Alekhine) variation
ca4a56b8-38ec-4984-83e3-24e8f6d8a78c
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Bb5
Sicilian, Richter-Rauzer, Richter attack
d2fd11c8-3c53-4636-82a6-9264812138ec
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Nxc6
Sicilian, Richter-Rauzer, Keres variation
7add6780-bc02-4a79-a428-90ad8f8e62e7
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Qd3
******B63: Sicilian, Richter-Rauzer, Rauzer attack
Sicilian, Richter-Rauzer, Rauzer attack
dff6cbf3-14a7-4fda-8605-9b46472f72c1
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Qd2
Sicilian, Richter-Rauzer, Rauzer attack, 7...Be7
56c66550-706c-46c6-aaf3-3c0c95b92188
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Qd2 Be7 
******B64: Sicilian, Richter-Rauzer, Rauzer attack, 7...Be7 defence, 9.f4
Sicilian, Richter-Rauzer, Rauzer attack, 7...Be7 defence, 9.f4
a894a265-cf11-4798-9451-8a4063042d8d
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Qd2 Be7 8. O-O-O O-O 9. f4
Sicilian, Richter-Rauzer, Rauzer attack, Geller variation
debd07b8-2ce1-47ec-802c-3c4e4bd00f1d
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Qd2 Be7 8. O-O-O O-O 9. f4 e5 
******B65: Sicilian, Richter-Rauzer, Rauzer attack, 7...Be7 defence, 9...Nxd4
Sicilian, Richter-Rauzer, Rauzer attack, 7...Be7 defence, 9...Nxd4
70bba61b-9eb4-4b3f-86a0-8e0ad6a65273
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Qd2 Be7 8. O-O-O O-O 9. f4 Nxd4 
Sicilian, Richter-Rauzer, Rauzer attack, 7...Be7 defence, 9...Nxd4
492b9651-dd86-4424-8e3e-e89e6fa16790
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Qd2 Be7 8. O-O-O O-O 9. f4 Nxd4 10. Qxd4
******B66: Sicilian, Richter-Rauzer, Rauzer attack, 7...a6
Sicilian, Richter-Rauzer, Rauzer attack, 7...a6
7c48ee12-a824-41f1-a7c1-a7e930e6b8d5
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Qd2 a6 
******B67: Sicilian, Richter-Rauzer, Rauzer attack, 7...a6 defence, 8...Bd7
Sicilian, Richter-Rauzer, Rauzer attack, 7...a6 defence, 8...Bd7
5cea6ebb-223c-4352-ad62-9e9cdd2259cb
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Qd2 a6 8. O-O-O Bd7 
******B68: Sicilian, Richter-Rauzer, Rauzer attack, 7...a6 defence, 9...Be7
Sicilian, Richter-Rauzer, Rauzer attack, 7...a6 defence, 9...Be7
6f58463c-5d3e-4dd6-94c7-eb2ae76c2a3d
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Qd2 a6 8. O-O-O Bd7 9. f4 Be7 
******B69: Sicilian, Richter-Rauzer, Rauzer attack, 7...a6 defence, 11.Bxf6
Sicilian, Richter-Rauzer, Rauzer attack, 7...a6 defence, 11.Bxf6
9d778c1f-91e0-453f-85f8-6ea368a508fd
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Qd2 a6 8. O-O-O Bd7 9. f4 Be7 10. Nf3 b5 11. Bxf6
******B70: Sicilian, dragon variation
Sicilian, dragon variation
43fec2be-a8df-4511-a64b-9cb5148b6379
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 
******B71: Sicilian, dragon, Levenfish variation
Sicilian, dragon, Levenfish variation
7f3fe9e2-3dab-495c-9117-4132c84ad229
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. f4
Sicilian, dragon, Levenfish; Flohr variation
17586f6f-224b-41e5-93e6-4b537235ed9d
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. f4 Nbd7 
******B72: Sicilian, dragon, 6.Be3
Sicilian, dragon, 6.Be3
b302bab0-0842-40b9-bbf8-66e27abb4b15
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3
Sicilian, dragon, classical attack
99387a9d-1c11-4ad9-b7cb-b250a9cfec30
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Be2
Sicilian, dragon, classical, Amsterdam variation
aebe0abf-ab2d-4c8d-9245-a645186aed4c
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Be2 Nc6 8. Qd2
Sicilian, dragon, classical, Grigoriev variation
34147b0e-4283-491f-ae2b-3d790e7e5866
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Be2 Nc6 8. Qd2 O-O 9. O-O-O
Sicilian, dragon, classical, Nottingham variation
753daeae-26ab-4557-ac92-36e9bb767409
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Be2 Nc6 8. Nb3
******B73: Sicilian, dragon, classical, 8.O-O
Sicilian, dragon, classical, 8.O-O
d1c3e0a6-60a9-4d1c-9831-2aab9796a0ec
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Be2 Nc6 8. O-O
Sicilian, dragon, classical, Zollner gambit
41537cc5-5fb3-4a64-864c-6bd71bc65ffb
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Be2 Nc6 8. O-O O-O 9. f4 Qb6 10. e5
Sicilian, dragon, classical, Richter variation
f8b2697f-2e64-4ba1-8ca5-53cedb9ff124
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Be2 Nc6 8. O-O O-O 9. Qd2
******B74: Sicilian, dragon, classical, 9.Nb3
Sicilian, dragon, classical, 9.Nb3
9f689e92-e5c6-4aa0-8d4a-7e75ff93bfa9
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Be2 Nc6 8. O-O O-O 9. Nb3
Sicilian, dragon, classical, Stockholm attack
c571f6c4-9ece-4761-a6a1-3eac5fa2727c
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Be2 Nc6 8. O-O O-O 9. Nb3 Be6 10. f4 Na5 11. f5 Bc4 12. Nxa5 Bxe2 13. Qxe2 Qxa5 14. g4
Sicilian, dragon, classical, Spielmann variation
8dd0ba5c-9323-4927-b41e-cad58722fb18
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Be2 Nc6 8. O-O O-O 9. Nb3 Be6 10. f4 Na5 11. f5 Bc4 12. Bd3
Sicilian, dragon, classical, Bernard defence
4c2bf725-8b9c-4417-ad66-0657d010d822
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Be2 Nc6 8. O-O O-O 9. Nb3 Be6 10. f4 Na5 11. f5 Bc4 12. Bd3 Bxd3 13. cxd3 d5 
Sicilian, dragon, classical, Reti-Tartakower variation
da5e9971-fbc0-45ad-a167-87150216eef0
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Be2 Nc6 8. O-O O-O 9. Nb3 Be6 10. f4 Qc8 
Sicilian, dragon, classical, Alekhine variation
1df46777-2cf8-4ca9-bbdb-d7f28e759e10
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Be2 Nc6 8. O-O O-O 9. Nb3 a5 
******B75: Sicilian, dragon, Yugoslav attack
Sicilian, dragon, Yugoslav attack
960f8027-d8fb-4c79-a23c-88f4fb08a374
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. f3
******B76: Sicilian, dragon, Yugoslav attack, 7...O-O
Sicilian, dragon, Yugoslav attack, 7...O-O
b42adef1-3eb4-4a48-859d-40203e3419c1
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. f3 O-O 
Sicilian, dragon, Yugoslav attack, Rauser variation
0350b97d-18ae-408a-84e1-ffb378a8455a
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. f3 O-O 8. Qd2 Nc6 9. O-O-O
******B77: Sicilian, dragon, Yugoslav attack, 9.Bc4
Sicilian, dragon, Yugoslav attack, 9.Bc4
44e9f578-e8b0-4804-bbd3-d7d0a0bc301e
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. f3 O-O 8. Qd2 Nc6 9. Bc4
Sicilian, dragon, Yugoslav attack, Byrne variation
ebc0fd8f-1f8b-4673-813b-92d096a433ff
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. f3 O-O 8. Qd2 Nc6 9. Bc4 a5 
Sicilian, dragon, Yugoslav attack, 9...Bd7
5b5d06e7-9f83-4fa1-9872-b4297620cf2a
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. f3 O-O 8. Qd2 Nc6 9. Bc4 Bd7 
******B78: Sicilian, dragon, Yugoslav attack, 10.O-O-O
Sicilian, dragon, Yugoslav attack, 10.O-O-O
32eb7242-956b-4cb5-bc26-a2c26e519451
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. f3 O-O 8. Qd2 Nc6 9. Bc4 Bd7 10. O-O-O
******B79: Sicilian, dragon, Yugoslav attack, 12.h4
Sicilian, dragon, Yugoslav attack, 12.h4
1f7af48a-dc6e-4c06-adf1-29b0158afb68
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. f3 O-O 8. Qd2 Nc6 9. Bc4 Bd7 10. O-O-O Qa5 11. Bb3 Rfc8 12. h4
******B80: Sicilian, Scheveningen variation
Sicilian, Scheveningen variation
a55984bf-0df1-4695-be89-9de83a0f15bb
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 
Sicilian, Scheveningen, English variation
ec588f9f-350a-4c4f-bfcc-352ac5f750ac
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Be3 a6 7. Qd2
Sicilian, Scheveningen, Vitolins variation
8dec5c50-5b06-4ad6-b3a4-6b08ac196d44
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Bb5+
Sicilian, Scheveningen, fianchetto variation
b026463e-030d-425a-9ded-757d91b1f34f
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. g3
******B81: Sicilian, Scheveningen, Keres attack
Sicilian, Scheveningen, Keres attack
dd41139f-56e2-4bec-982e-db14e47af0c3
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. g4
******B82: Sicilian, Scheveningen, 6.f4
Sicilian, Scheveningen, 6.f4
1306f67c-d5a7-4171-9195-82951ac225e3
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. f4
Sicilian, Scheveningen, Tal variation
0b545738-85c6-4bc2-99ea-cd1440b9f59a
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. f4 Nc6 7. Be3 Be7 8. Qf3
******B83: Sicilian, Scheveningen, 6.Be2
Sicilian, Scheveningen, 6.Be2
d19fecad-e9c6-4d4e-93a2-61d96077ae26
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Be2
Sicilian, modern Scheveningen
48ac4fc5-592d-4e96-a330-e53c3bcc4b76
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Be2 Nc6 
Sicilian, modern Scheveningen, main line
8b3e1fac-27ea-45c9-9f3b-948b5e90bbd6
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Be2 Nc6 7. O-O Be7 8. Be3 O-O 9. f4
Sicilian, modern Scheveningen, main line with Nb3
ec5b640c-6c5e-4267-8616-4acd32ea12d4
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Be2 Nc6 7. O-O Be7 8. Be3 O-O 9. f4 Bd7 10. Nb3
******B84: Sicilian, Scheveningen (Paulsen), classical variation
Sicilian, Scheveningen (Paulsen), classical variation
63954b3e-d126-42d0-812b-035bd0765b56
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Be2 a6 
Sicilian, Scheveningen, classical, Nd7 system
253c9c85-ae0d-4976-b2fb-40d39a8102ed
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Be2 a6 7. O-O Nbd7 
Sicilian, Scheveningen (Paulsen), classical variation
ddf57154-ad59-4f7f-8034-14781299f39e
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Be2 a6 7. O-O Qc7 
******B85: Sicilian, Scheveningen, classical variation with ...Qc7 and ...Nc6
Sicilian, Scheveningen, classical variation with ...Qc7 and ...Nc6
a7191b52-27be-47eb-8974-0424e0a40b91
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Be2 a6 7. O-O Qc7 8. f4 Nc6 
Sicilian, Scheveningen, classical, Maroczy system
59311da1-e23e-423c-ae5d-dfbb8594d18c
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Be2 a6 7. O-O Qc7 8. f4 Nc6 9. Kh1 Be7 10. a4
Sicilian, Scheveningen, classical
01754267-4f23-4ea3-b96e-1ce2a4d7af53
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Be2 a6 7. O-O Qc7 8. f4 Nc6 9. Be3
Sicilian, Scheveningen, classical main line
0bcfddd1-6f4f-4f6f-a036-205ba16a0756
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Be2 a6 7. O-O Qc7 8. f4 Nc6 9. Be3 Be7 10. Qe1 O-O 
******B86: Sicilian, Sozin attack
Sicilian, Sozin attack
a0a5b4c7-5c61-472f-84d9-cb1959cbfc18
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Bc4
******B87: Sicilian, Sozin with ...a6 and ...b5
Sicilian, Sozin with ...a6 and ...b5
25548ea5-4a16-4b51-aedf-34c45b42f5d2
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Bc4 a6 7. Bb3 b5 
******B88: Sicilian, Sozin, Leonhardt variation
Sicilian, Sozin, Leonhardt variation
5ba3c248-9c4f-4a67-abd4-521920089701
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Bc4 Nc6 
Sicilian, Sozin, Fischer variation
cd795230-bdb8-4808-841f-a0483f854277
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Bc4 Nc6 7. Bb3 Be7 8. Be3 O-O 9. f4
******B89: Sicilian, Sozin, 7.Be3
Sicilian, Sozin, 7.Be3
4b14b3d0-d0b1-4f3a-a458-78d065b486fc
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Bc4 Nc6 7. Be3
Sicilian, Velimirovic attack
f856fbe2-5d31-4f2b-9823-29074ab62c3a
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Bc4 Nc6 7. Be3 Be7 8. Qe2
******B90: Sicilian, Najdorf
Sicilian, Najdorf
05e003d0-5bfb-43b6-a031-9abd0d8887fd
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 
Sicilian, Najdorf, Adams attack
6013062a-aef9-42dc-9fc9-25d5643bda2c
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. h3
Sicilian, Najdorf, Lipnitzky attack
c5d5c6c0-e90b-4067-a4b5-f039d240d24b
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bc4
Sicilian, Najdorf, Byrne (English) attack
b00b6891-6404-45cc-a31f-5257c9d26f79
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Be3
******B91: Sicilian, Najdorf, Zagreb (fianchetto) variation
Sicilian, Najdorf, Zagreb (fianchetto) variation
001f1659-078b-482b-a690-922651d0ac9e
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. g3
******B92: Sicilian, Najdorf, Opovcensky variation
Sicilian, Najdorf, Opovcensky variation
1918c38e-64e7-4786-8aa2-5f8d257418a7
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Be2
******B93: Sicilian, Najdorf, 6.f4
Sicilian, Najdorf, 6.f4
d3cfe3ad-8083-4e60-9190-f2a8af1613a5
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. f4
******B94: Sicilian, Najdorf, 6.Bg5
Sicilian, Najdorf, 6.Bg5
5e66f411-0827-4f64-805c-fa0882d7b448
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bg5
Sicilian, Najdorf, Ivkov variation
639325a4-5e48-4204-a2e5-a079c74fb286
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bg5 Nbd7 7. Bc4 Qa5 8. Qd2 e6 9. O-O-O b5 10. Bb3 Bb7 11. Rhe1 Nc5 12. e5
******B95: Sicilian, Najdorf, 6...e6
Sicilian, Najdorf, 6...e6
c1063552-830e-4113-a164-1e1458b4ee64
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bg5 e6 
******B96: Sicilian, Najdorf, 7.f4
Sicilian, Najdorf, 7.f4
70c4bdb1-2a90-48c6-b9f3-1512bf626672
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bg5 e6 7. f4
Sicilian, Najdorf, Polugayevsky variation
4ea080eb-63d7-4581-b2c8-b5896ca93e4a
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bg5 e6 7. f4 b5 
Sicilian, Najdorf, Polugayevsky, Simagin variation
c3ab9c5e-3def-4251-bef4-dee885f54993
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bg5 e6 7. f4 b5 8. e5 dxe5 9. fxe5 Qc7 10. Qe2
******B97: Sicilian, Najdorf, 7...Qb6
Sicilian, Najdorf, 7...Qb6
652d6dcf-8a94-4644-88b1-a23cf5f1eb6f
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bg5 e6 7. f4 Qb6 
Sicilian, Najdorf, Poisoned pawn variation
75edba32-9b53-4f06-ae10-f76956f0b07d
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bg5 e6 7. f4 Qb6 8. Qd2 Qxb2 9. Rb1 Qa3 
******B98: Sicilian, Najdorf, 7...Be7
Sicilian, Najdorf, 7...Be7
513bd7d4-0729-44c9-b035-2bc4aedc21a4
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bg5 e6 7. f4 Be7 
Sicilian, Najdorf, Browne variation
19321d4b-2463-4648-99c3-bfac49e9415f
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bg5 e6 7. f4 Be7 8. Qf3 h6 9. Bh4 Qc7 
Sicilian, Najdorf, Goteborg (Argentine) variation
854360ec-daca-4fce-bba8-e9f17bdb3152
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bg5 e6 7. f4 Be7 8. Qf3 h6 9. Bh4 g5 
Sicilian, Najdorf variation
536142aa-f089-45e1-8269-342da96e517a
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bg5 e6 7. f4 Be7 8. Qf3 Qc7 
******B99: Sicilian, Najdorf, 7...Be7 main line
Sicilian, Najdorf, 7...Be7 main line
3e74b104-5ed0-4dd4-a239-ed9b9ee49263
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bg5 e6 7. f4 Be7 8. Qf3 Qc7 9. O-O-O Nbd7 
******C00: French defence
French defence
691c8125-625a-4e88-b8ea-e6b063cd30fb
1. e4 e6 
French defence, Steiner variation
5c138d03-a916-4f33-8bf6-7d1574ae9e82
1. e4 e6 2. c4
French, Reti (Spielmann) variation
dca970eb-c4c0-45d6-8848-9deb63489f6d
1. e4 e6 2. b3
French, Steinitz attack
032d427d-8a7e-44bd-94f3-228f7830158e
1. e4 e6 2. e5
French, Labourdonnais variation
3d8acb52-c24f-4f76-8099-64bec218fead
1. e4 e6 2. f4
French defence
dd74c44c-5420-4dde-b332-527efd6202e5
1. e4 e6 2. Nf3
French, Wing gambit
575cc8df-3ff8-41c2-a1c7-9270f490f626
1. e4 e6 2. Nf3 d5 3. e5 c5 4. b4
French defence
e1f20c43-dd56-4637-adc9-dd9d2220c0a2
1. e4 e6 2. Nc3
French, Pelikan variation
1160cd23-24a8-4aa4-a6f2-ed8a612d4d25
1. e4 e6 2. Nc3 d5 3. f4
French, Two knights variation
b795ba7a-e5de-492b-b479-a303072ba6d5
1. e4 e6 2. Nc3 d5 3. Nf3
French, Chigorin variation
9fd9cdad-ddaa-4063-a40a-e73ecb819e0c
1. e4 e6 2. Qe2
French, King's Indian attack
b39753ed-3b0b-4f21-9438-5f2b440d557b
1. e4 e6 2. d3
French, Reversed Philidor formation
dfc1c309-2af5-492b-a986-3cd80433e00b
1. e4 e6 2. d3 d5 3. Nd2 Nf6 4. Ngf3 Nc6 5. Be2
French defence
5bf7b649-344e-4d1e-bd57-8c793e553dd9
1. e4 e6 2. d4
Lengfellner system
59b70c25-a16e-420e-9071-924801a894a5
1. e4 e6 2. d4 d6 
St. George defence
1705470a-da8d-43b2-bf00-3a5fc250f46c
1. e4 e6 2. d4 a6 
French defence
4dba46bb-26d7-496b-aa49-4633de24ce25
1. e4 e6 2. d4 d5 
French, Schlechter variation
a993fa54-d81c-4b76-84eb-58631ba14ec3
1. e4 e6 2. d4 d5 3. Bd3
French, Alapin variation
3af59311-2102-43e0-ac57-5f3f6ad08f49
1. e4 e6 2. d4 d5 3. Be3
******C01: French, exchange variation
French, exchange variation
d07a3352-5ae5-4c95-98ab-06a9cec9168b
1. e4 e6 2. d4 d5 3. exd5
French, exchange, Svenonius variation
db2c1a1b-62fb-46ec-aad5-4cc299bf452c
1. e4 e6 2. d4 d5 3. exd5 exd5 4. Nc3 Nf6 5. Bg5
French, exchange, Bogolyubov variation
8f9ee085-05c3-475f-89a7-c2d41355fb29
1. e4 e6 2. d4 d5 3. exd5 exd5 4. Nc3 Nf6 5. Bg5 Nc6 
******C02: French, advance variation
French, advance variation
b7d535e5-b4ad-479c-82c7-5de672c7b41a
1. e4 e6 2. d4 d5 3. e5
French, advance, Steinitz variation
6130622f-a4bc-4624-ae46-58ec425d6bb4
1. e4 e6 2. d4 d5 3. e5 c5 4. dxc5
French, advance, Nimzovich variation
fa6b3174-f82b-46c2-bffd-d2b3f9e4d32e
1. e4 e6 2. d4 d5 3. e5 c5 4. Qg4
French, advance, Nimzovich system
3f7f8cec-5034-4238-afaa-fc45073fa589
1. e4 e6 2. d4 d5 3. e5 c5 4. Nf3
French, advance variation
396e61ea-d7d1-460e-a58f-95f27495827b
1. e4 e6 2. d4 d5 3. e5 c5 4. c3
French, advance, Wade variation
07056479-48bd-4870-85df-429f9b1d129c
1. e4 e6 2. d4 d5 3. e5 c5 4. c3 Qb6 5. Nf3 Bd7 
French, advance variation
f657419f-49af-42fb-bb57-320007827e44
1. e4 e6 2. d4 d5 3. e5 c5 4. c3 Nc6 
French, advance, Paulsen attack
d7553182-aea4-4567-ba07-fab74f476e2c
1. e4 e6 2. d4 d5 3. e5 c5 4. c3 Nc6 5. Nf3
French, advance, Milner-Barry gambit
614c9276-8a0c-4aeb-abfa-a7c0fd7e8d09
1. e4 e6 2. d4 d5 3. e5 c5 4. c3 Nc6 5. Nf3 Qb6 6. Bd3
French, advance, Euwe variation
fe630900-be35-46c7-a5db-92738aa3b7c9
1. e4 e6 2. d4 d5 3. e5 c5 4. c3 Nc6 5. Nf3 Bd7 
******C03: French, Tarrasch
French, Tarrasch
72feaf56-5ebc-4e32-a345-dc75c1c6e9f3
1. e4 e6 2. d4 d5 3. Nd2
French, Tarrasch, Haberditz variation
d5850cab-5d75-48b9-bc1c-c9238e939ab1
1. e4 e6 2. d4 d5 3. Nd2 f5 
French, Tarrasch, Guimard variation
0b369815-b0aa-48b2-9878-f10ba9658d35
1. e4 e6 2. d4 d5 3. Nd2 Nc6 
******C04: French, Tarrasch, Guimard main line
French, Tarrasch, Guimard main line
01212753-3982-4c03-bcaf-47423784a286
1. e4 e6 2. d4 d5 3. Nd2 Nc6 4. Ngf3 Nf6 
******C05: French, Tarrasch, closed variation
French, Tarrasch, closed variation
275570fb-afd5-49dc-85a6-42d353d89aa3
1. e4 e6 2. d4 d5 3. Nd2 Nf6 
French, Tarrasch, Botvinnik variation
c88bfca4-44e7-4fc8-be04-ca071f94834f
1. e4 e6 2. d4 d5 3. Nd2 Nf6 4. e5 Nfd7 5. Bd3 c5 6. c3 b6 
French, Tarrasch, closed variation
5dd5272a-616e-4837-a70e-e140efc26255
1. e4 e6 2. d4 d5 3. Nd2 Nf6 4. e5 Nfd7 5. Bd3 c5 6. c3 Nc6 
******C06: French, Tarrasch, closed variation, main line
French, Tarrasch, closed variation, main line
ae980e87-23d6-459a-9963-d5c6d6c9eb44
1. e4 e6 2. d4 d5 3. Nd2 Nf6 4. e5 Nfd7 5. Bd3 c5 6. c3 Nc6 7. Ne2 cxd4 8. cxd4
French, Tarrasch, Leningrad variation
c9a453a9-6a3e-49b4-a53f-06a6a42282eb
1. e4 e6 2. d4 d5 3. Nd2 Nf6 4. e5 Nfd7 5. Bd3 c5 6. c3 Nc6 7. Ne2 cxd4 8. cxd4 Nb6 
******C07: French, Tarrasch, open variation
French, Tarrasch, open variation
3aae9ae8-2ce7-48f8-ac31-3a8a078f866d
1. e4 e6 2. d4 d5 3. Nd2 c5 
French, Tarrasch, Eliskases variation
9b852abc-3c03-403e-b143-6fc46b95fb25
1. e4 e6 2. d4 d5 3. Nd2 c5 4. exd5 Qxd5 5. Ngf3 cxd4 6. Bc4 Qd8 
******C08: French, Tarrasch, open, 4.ed ed
French, Tarrasch, open, 4.ed ed
3bc64f93-e037-443e-8205-6f7ce161e20e
1. e4 e6 2. d4 d5 3. Nd2 c5 4. exd5 exd5 
******C09: French, Tarrasch, open variation, main line
French, Tarrasch, open variation, main line
82c695c9-1f03-4eb1-8fe1-fd937dd90730
1. e4 e6 2. d4 d5 3. Nd2 c5 4. exd5 exd5 5. Ngf3 Nc6 
******C10: French, Paulsen variation
French, Paulsen variation
662100f6-cbbe-4790-b006-b98209baec91
1. e4 e6 2. d4 d5 3. Nc3
French, Marshall variation
be9eb019-c048-427d-99ad-a70583acc4a1
1. e4 e6 2. d4 d5 3. Nc3 c5 
French, Rubinstein variation
622c9a2f-a17f-4b8a-9262-3532f9a933a7
1. e4 e6 2. d4 d5 3. Nc3 dxe4 
French, Fort Knox variation
9dbf5a53-3459-46b7-bf40-778de1644f9c
1. e4 e6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Bd7 5. Nf3 Bc6 
French, Rubinstein variation
7d7b669d-eee3-412d-a014-0a0c212c0a00
1. e4 e6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Nd7 
French, Rubinstein, Capablanca line
57315aeb-934f-40f5-9c58-4fafa3042c94
1. e4 e6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Nd7 5. Nf3 Ngf6 6. Nxf6+ Nxf6 7. Ne5
French, Frere (Becker) variation
4abb9156-3d31-44b6-99fa-ba8df1ed3b0e
1. e4 e6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Qd5 
******C11: French defence
French defence
b28386b6-3a75-4c86-8bd7-a0019c94b043
1. e4 e6 2. d4 d5 3. Nc3 Nf6 
French, Swiss variation
4fd7dd83-6219-46ed-863f-90a66568eb3f
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bd3
French, Henneberger variation
78c97af7-dab7-432e-bb1d-8b6c362ee477
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Be3
French, Steinitz variation
a6f1d214-9a0f-4919-b13b-7133436a3190
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. e5
French, Steinitz, Bradford attack
f51c3c74-4b12-42a1-9b67-b81d73ec0880
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. e5 Nfd7 5. f4 c5 6. dxc5 Bxc5 7. Qg4
French, Steinitz variation
7e8057bc-b63a-4a23-83a7-39e23e5d3d5f
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. e5 Nfd7 5. f4 c5 6. dxc5 Nc6 
French, Steinitz, Brodsky-Jones variation
a280fc7d-7d23-4d98-ad33-11cacfc73db4
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. e5 Nfd7 5. f4 c5 6. dxc5 Nc6 7. a3 Bxc5 8. Qg4 O-O 9. Nf3 f6 
French, Steinitz variation
c90d7370-8bfb-4678-9b8a-c14e1a013032
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. e5 Nfd7 5. f4 c5 6. Nf3
French, Steinitz, Boleslavsky variation
10187112-efe7-4a59-9f2f-256a146439d9
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. e5 Nfd7 5. f4 c5 6. Nf3 Nc6 7. Be3
French, Steinitz, Gledhill attack
817f843d-bc07-4340-a3f6-2cf3a0a49e2e
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. e5 Nfd7 5. Qg4
French, Burn variation
574742b0-0c4f-4de0-bf3a-87a06634ec81
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 dxe4 
******C12: French, MacCutcheon variation
French, MacCutcheon variation
52ceaa46-5d46-4ea3-b4d8-88f2ccaa3159
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Bb4 
French, MacCutcheon, Bogolyubov variation
bba3d20e-1fb2-42a8-95f4-2feec99aea1c
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Bb4 5. exd5 Qxd5 6. Bxf6 gxf6 7. Qd2 Qa5 
French, MacCutcheon, advance variation
eb5e9175-76fa-4206-b4c4-cdc55a8f653e
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Bb4 5. e5
French, MacCutcheon, Chigorin variation
8c0fd046-d5f5-4124-8ec5-5821134101d2
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Bb4 5. e5 h6 6. exf6
French, MacCutcheon, Grigoriev variation
c5bbf9d8-429d-4892-8dcc-e0d59c421bbe
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Bb4 5. e5 h6 6. exf6 hxg5 7. fxg7 Rg8 8. h4 gxh4 9. Qg4
French, MacCutcheon, Bernstein variation
9851245e-84d7-4995-898e-8d6a056ee64c
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Bb4 5. e5 h6 6. Bh4
French, MacCutcheon, Janowski variation
71066728-d63b-4912-8d4a-5773b7b76fde
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Bb4 5. e5 h6 6. Be3
French, MacCutcheon, Dr. Olland (Dutch) variation
25afb83f-7f01-48e6-9e95-2817cbb14b36
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Bb4 5. e5 h6 6. Bc1
French, MacCutcheon, Tartakower variation
65790624-19c4-4d67-bb1c-42a075514617
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Bb4 5. e5 h6 6. Bd2 Nfd7 
French, MacCutcheon, Lasker variation
88562ff8-4972-4262-bae8-1f5fc8668530
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Bb4 5. e5 h6 6. Bd2 Bxc3 
French, MacCutcheon, Duras variation
5b143e48-7a4b-4b45-bec8-167706e1412f
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Bb4 5. e5 h6 6. Bd2 Bxc3 7. bxc3 Ne4 8. Qg4 Kf8 9. Bc1
French, MacCutcheon, Lasker variation, 8...g6
e59c99ef-c5f6-4afe-9c06-422da091014a
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Bb4 5. e5 h6 6. Bd2 Bxc3 7. bxc3 Ne4 8. Qg4 g6 
******C13: French, classical
French, classical
55b2f3b6-491e-4d98-9390-21263a2dfb24
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 
French, classical, Anderssen variation
41a57760-e1cb-4f61-a8c8-2875e73a2b76
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. Bxf6
French, classical, Anderssen-Richter variation
58e5822e-45e8-441b-a60b-765a26b48745
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. Bxf6 Bxf6 6. e5 Be7 7. Qg4
French, classical, Vistaneckis (Nimzovich) variation
6d09e63a-556a-4a36-aadb-e08693966b61
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Ng8 
French, classical, Frankfurt variation
944da43d-1ad3-46ad-a059-7c76e225c841
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Ng8 6. Be3 b6 
French, classical, Tartakower variation
ef1100d2-6892-4249-bda6-52ba3b8bea29
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Ne4 
French, Albin-Alekhine-Chatard attack
1a3317d5-48c1-41a2-a77d-afe8b7d7b0e7
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 6. h4
French, Albin-Alekhine-Chatard attack, Maroczy variation
f4aa3ba4-15ba-42d1-b601-fdf2f76f108e
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 6. h4 a6 
French, Albin-Alekhine-Chatard attack, Breyer variation
3845d9d7-313c-4664-a90d-f318354aa4d4
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 6. h4 c5 
French, Albin-Alekhine-Chatard attack, Teichmann variation
aca72e70-8b3b-4bc8-8112-bbab55fd3bd3
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 6. h4 f6 
French, Albin-Alekhine-Chatard attack, Spielmann variation
73d3c0db-cf80-427c-a56e-8a4799443154
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 6. h4 O-O 
******C14: French, classical variation
French, classical variation
d03acdfb-3104-45a4-9001-bf7d91bdc34f
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 6. Bxe7 Qxe7 
French, classical, Tarrasch variation
77c29431-bf51-4335-af3c-ca3556e5238e
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 6. Bxe7 Qxe7 7. Bd3
French, classical, Rubinstein variation
19610c24-5551-49c8-93b5-5bf834ed943f
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 6. Bxe7 Qxe7 7. Qd2
French, classical, Alapin variation
8ff559d4-8f9a-467e-a308-cf4e0f5427a3
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 6. Bxe7 Qxe7 7. Nb5
French, classical, Pollock variation
cd876f53-9e28-4bca-babe-062ba10d8f3a
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 6. Bxe7 Qxe7 7. Qg4
French, classical, Steinitz variation
ea4e96bc-4264-4bb3-9f69-690a6c89c236
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 6. Bxe7 Qxe7 7. f4
French, classical, Stahlberg variation
2cfe8b38-115b-4d57-85ae-a09e45d44d94
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 6. Bxe7 Qxe7 7. f4 O-O 8. Nf3 c5 9. Qd2 Nc6 10. O-O-O c4 
******C15: French, Winawer (Nimzovich) variation
French, Winawer (Nimzovich) variation
e9bb7f48-9452-40ad-9650-1e5d6a7b7e95
1. e4 e6 2. d4 d5 3. Nc3 Bb4 
French, Winawer, Kondratiyev variation
2c35b1f4-e7c0-4604-987d-00a4332bd129
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. Bd3 c5 5. exd5 Qxd5 6. Bd2
French, Winawer, fingerslip variation
6a8bd527-f886-4c16-8316-46380ad470d8
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. Bd2
French, Winawer, Alekhine (Maroczy) gambit
794644c3-1509-4293-a1bf-821a2d58938d
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. Nge2
French, Winawer, Alekhine gambit, Alatortsev variation
abc4934f-f2a4-4586-91e6-099a4dab7102
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. Nge2 dxe4 5. a3 Be7 6. Nxe4 Nf6 7. Ne2-g3 O-O 8. Be2 Nc6 
French, Winawer, Alekhine gambit
fdaf95fb-0eff-494e-b3bc-e325f28e462f
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. Nge2 dxe4 5. a3 Bxc3+ 
French, Winawer, Alekhine gambit, Kan variation
1253f4eb-d62b-4831-817f-18fcba91b443
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. Nge2 dxe4 5. a3 Bxc3+ 6. Nxc3 Nc6 
******C16: French, Winawer, advance variation
French, Winawer, advance variation
6def50ea-6262-4b81-9c2d-0ad75b435945
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5
French, Winawer, Petrosian variation
fed7a994-1543-49df-a617-2c425e7a3fd3
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 Qd7 
******C17: French, Winawer, advance variation
French, Winawer, advance variation
be312de4-1d3c-457f-9437-41e50c7cf062
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 c5 
French, Winawer, advance, Bogolyubov variation
74e31438-e554-4140-a643-30d7567f8014
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 c5 5. Bd2
French, Winawer, advance, Russian variation
2002d355-53d6-4cdf-9939-2bf70eb371c8
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 c5 5. Qg4
French, Winawer, advance, 5.a3
fa9067d4-e12c-49b7-b107-c1980a322f2d
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 c5 5. a3
French, Winawer, advance, Rauzer variation
34c8dd06-3b36-4862-87b1-830daad96e97
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 c5 5. a3 cxd4 6. axb4 dxc3 7. Nf3
******C18: French, Winawer, advance variation
French, Winawer, advance variation
7ecebc82-19b5-4b22-a784-dba82e255cbe
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 c5 5. a3 Bxc3+ 6. bxc3
French, Winawer, classical variation
310e86c7-e9ba-433c-ad77-12d5af3892a2
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 c5 5. a3 Bxc3+ 6. bxc3 Qc7 
******C19: French, Winawer, advance, 6...Ne7
French, Winawer, advance, 6...Ne7
c2366a6b-ab88-4744-8007-92a260560fee
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 c5 5. a3 Bxc3+ 6. bxc3 Ne7 
French, Winawer, advance, Smyslov variation
861c4043-8525-4b12-8d88-0c4f63378dd0
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 c5 5. a3 Bxc3+ 6. bxc3 Ne7 7. a4
French, Winawer, advance, positional main line
ef38203c-9102-46b5-8634-db3f8e661754
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 c5 5. a3 Bxc3+ 6. bxc3 Ne7 7. Nf3
French, Winawer, advance, poisoned pawn variation
3e2a5235-c8d3-4965-980c-907c59857a6f
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 c5 5. a3 Bxc3+ 6. bxc3 Ne7 7. Qg4
French, Winawer, advance, poisoned pawn, Euwe-Gligoric variation
01113624-17da-4d05-bc97-8c1b90d7ebfd
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 c5 5. a3 Bxc3+ 6. bxc3 Ne7 7. Qg4 Qc7 8. Qxg7 Rg8 9. Qxh7 cxd4 10. Kd1
French, Winawer, advance, poisoned pawn, Konstantinopolsky variation
c52426fd-a526-48f5-80f8-94b201699221
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 c5 5. a3 Bxc3+ 6. bxc3 Ne7 7. Qg4 Qc7 8. Qxg7 Rg8 9. Qxh7 cxd4 10. Ne2
******C20: King's pawn game
King's pawn game
68a961dc-ac6b-467f-8134-98626a4dbbb8
1. e4 e5 
KP, Indian opening
dd86ec8b-df33-45a8-b174-535c0da476f1
1. e4 e5 2. d3
KP, Mengarini's opening
d59163c9-6e87-426a-8959-bfc94c9305f6
1. e4 e5 2. a3
KP, King's head opening
d000cf39-0991-4d9f-bdcb-6212f71c2862
1. e4 e5 2. f3
KP, Patzer opening
286ec48b-626e-4c75-a95d-d5ddf6a80d33
1. e4 e5 2. Qh5
KP, Napoleon's opening
55da55ba-0266-4f10-832e-d65bf910b1b4
1. e4 e5 2. Qf3
KP, Lopez opening
6b7c97a6-6bc8-4704-9688-783127e96b63
1. e4 e5 2. c3
Alapin's opening
27a1b6f8-06b6-49dc-95ce-a258b3ad2ca7
1. e4 e5 2. Ne2
******C21: Centre game
Centre game
c5dcbb78-1fa2-4d4b-9548-6da9eb857c62
1. e4 e5 2. d4 exd4 
Centre game, Kieseritsky variation
e9f4e0ef-52be-464e-99d8-1529d942ae8d
1. e4 e5 2. d4 exd4 3. Nf3 c5 4. Bc4 b5 
Halasz gambit
a6c866bc-da5f-4c36-82db-20eb04fb965f
1. e4 e5 2. d4 exd4 3. f4
Danish gambit
536b3a70-f4d1-4d96-b89d-2d1dc1955e5e
1. e4 e5 2. d4 exd4 3. c3
Danish gambit, Collijn defence
ee144128-9b78-42ec-bf96-1c555d8bf3aa
1. e4 e5 2. d4 exd4 3. c3 dxc3 4. Bc4 cxb2 5. Bxb2 Qe7 
Danish gambit, Schlechter defence
390d124d-8073-4f9b-a9e7-bba2d33411db
1. e4 e5 2. d4 exd4 3. c3 dxc3 4. Bc4 cxb2 5. Bxb2 d5 
Danish gambit, Soerensen defence
0c106f07-4f05-43e2-bf8e-5fb4fc4237d6
1. e4 e5 2. d4 exd4 3. c3 d5 
Centre game
0ee63508-f68c-4a4d-a4ec-e43182877063
1. e4 e5 2. d4 exd4 3. Qxd4
******C22: Centre game
Centre game
802b05d4-f9db-46fd-98e8-16183b8c68bb
1. e4 e5 2. d4 exd4 3. Qxd4 Nc6 
Centre game, Paulsen attack
9bbae722-41f2-4697-be0b-7881bc20e739
1. e4 e5 2. d4 exd4 3. Qxd4 Nc6 4. Qe3
Centre game, Charousek variation
48de2baa-74d9-47eb-9b20-672b7296cf1e
1. e4 e5 2. d4 exd4 3. Qxd4 Nc6 4. Qe3 Bb4+ 5. c3 Be7 
Centre game, l'Hermet variation
e9c4147d-fb9f-4c09-9c62-3ae594aa9d3d
1. e4 e5 2. d4 exd4 3. Qxd4 Nc6 4. Qe3 f5 
Centre game, Berger variation
6b8ad3d1-4c29-495c-91dd-fa7680cd6e1b
1. e4 e5 2. d4 exd4 3. Qxd4 Nc6 4. Qe3 Nf6 
Centre game, Kupreichik variation
a26d993f-b04e-4207-867a-48f7e3ee7dbe
1. e4 e5 2. d4 exd4 3. Qxd4 Nc6 4. Qe3 Nf6 5. Nc3 Bb4 6. Bd2 O-O 7. O-O-O Re8 8. Bc4 d6 9. Nh3
Centre game, Hall variation
3245c6aa-a09a-416e-8e36-9c7eba02f10f
1. e4 e5 2. d4 exd4 3. Qxd4 Nc6 4. Qc4
******C23: Bishop's opening
Bishop's opening
faefe064-d1f6-44e5-82e9-3ea8f0ba4f55
1. e4 e5 2. Bc4
Bishop's opening, Philidor counter-attack
7bda41c1-f30b-4082-b997-f49d2a9841d0
1. e4 e5 2. Bc4 c6 
Bishop's opening, Lisitsyn variation
8863e34a-736b-447b-aa95-5a3bf8a1a302
1. e4 e5 2. Bc4 c6 3. d4 d5 4. exd5 cxd5 5. Bb5+ Bd7 6. Bxd7+ Nxd7 7. dxe5 Nxe5 8. Ne2
Bishop's opening, Calabrese counter-gambit
5013a5d8-5645-4cd2-bb87-6076b259580b
1. e4 e5 2. Bc4 f5 
Bishop's opening, Calabrese counter-gambit, Jaenisch variation
2bcb106d-ae80-475a-8804-d2a7b6fd2729
1. e4 e5 2. Bc4 f5 3. d3
Bishop's opening, Classical variation
ea748b90-1b19-4862-8fe9-ee157ee337f3
1. e4 e5 2. Bc4 Bc5 
Bishop's opening, Lopez gambit
b15b1010-6993-406e-aa53-8ef08b493b77
1. e4 e5 2. Bc4 Bc5 3. Qe2 Nc6 4. c3 Nf6 5. f4
Bishop's opening, Philidor variation
be9f0194-8da5-474b-84ac-84930dad5acb
1. e4 e5 2. Bc4 Bc5 3. c3
Bishop's opening, Pratt variation
967ead3d-9044-434b-966b-230f0467c291
1. e4 e5 2. Bc4 Bc5 3. c3 Nf6 4. d4 exd4 5. e5 d5 6. exf6 dxc4 7. Qh5 O-O 
Bishop's opening, Lewis counter-gambit
976fa3c0-58a0-4035-83f2-2f8f1259ff72
1. e4 e5 2. Bc4 Bc5 3. c3 d5 
Bishop's opening, del Rio variation
5b342f96-d5b5-4bf6-8213-511656c698a3
1. e4 e5 2. Bc4 Bc5 3. c3 Qg5 
Bishop's opening, Lewis gambit
37e21cb7-a41d-42e3-8bc5-a0ea3de8c742
1. e4 e5 2. Bc4 Bc5 3. d4
Bishop's opening, Wing gambit
361beb5f-992b-4a0a-b736-a8574332eb18
1. e4 e5 2. Bc4 Bc5 3. b4
Bishop's opening, MacDonnell double gambit
5835448c-a02e-48d6-bb54-e164007f3b57
1. e4 e5 2. Bc4 Bc5 3. b4 Bxb4 4. f4
Bishop's opening, Four pawns' gambit
92f644a7-e686-4ddc-87a0-ee74996bdf16
1. e4 e5 2. Bc4 Bc5 3. b4 Bxb4 4. f4 exf4 5. Nf3 Be7 6. d4 Bh4+ 7. g3 fxg3 8. O-O gxh2+ 9. Kh1
******C24: Bishop's opening, Berlin defence
Bishop's opening, Berlin defence
45b19f82-fde8-4afc-9e5f-4cea9692d943
1. e4 e5 2. Bc4 Nf6 
Bishop's opening, Greco gambit
93300386-6a3b-432d-ab36-db71d70ebb28
1. e4 e5 2. Bc4 Nf6 3. f4
Bishop's opening, Ponziani gambit
1504587f-8375-46aa-a909-9f93a5e5ce2c
1. e4 e5 2. Bc4 Nf6 3. d4
Bishop's opening, Urusov gambit
53a94150-6f2a-492b-82ac-97f28f28fb9c
1. e4 e5 2. Bc4 Nf6 3. d4 exd4 4. Nf3
Bishop's opening, Urusov gambit, Panov variation
dcb803db-4028-4f89-a24d-df044e6ccf2e
1. e4 e5 2. Bc4 Nf6 3. d4 exd4 4. Nf3 d5 5. exd5 Bb4+ 6. c3 Qe7+ 
******C25: Vienna game
Vienna game
e1b66341-5762-4473-a9bf-4dc70b9cda99
1. e4 e5 2. Nc3
Vienna, Zhuravlev countergambit
4d74a448-d3fc-4d52-8f08-538e954265c2
1. e4 e5 2. Nc3 Bb4 3. Qg4 Nf6 
Vienna game, Max Lange defence
5b0a0421-7dcf-4bb1-a309-08957bd833d2
1. e4 e5 2. Nc3 Nc6 
Vienna, Paulsen variation
38313fab-90f4-4143-bc37-247ae350ccef
1. e4 e5 2. Nc3 Nc6 3. g3
Vienna, Fyfe gambit
add8ab2e-bf3a-4bec-86b8-650b6023c403
1. e4 e5 2. Nc3 Nc6 3. d4
Vienna gambit
68fdc26f-c70d-4aca-a323-3cdcaa595c30
1. e4 e5 2. Nc3 Nc6 3. f4
Vienna, Steinitz gambit
8f163e85-5f26-4c04-8281-81d41f234315
1. e4 e5 2. Nc3 Nc6 3. f4 exf4 4. d4
Vienna, Steinitz gambit, Zukertort defence
5265c1f6-1218-4a16-826a-7991800c7da9
1. e4 e5 2. Nc3 Nc6 3. f4 exf4 4. d4 Qh4+ 5. Ke2 d5 
Vienna, Steinitz gambit, Fraser-Minckwitz variation
7a8bf09b-c91d-46a1-96be-8014c01d6473
1. e4 e5 2. Nc3 Nc6 3. f4 exf4 4. d4 Qh4+ 5. Ke2 b6 
Vienna gambit
1fc2f94a-a48a-48e6-b18e-b7027c3aa513
1. e4 e5 2. Nc3 Nc6 3. f4 exf4 4. Nf3
Vienna, Hamppe-Allgaier gambit
273ff96b-0a31-4ba3-86e9-31ded3cd0cac
1. e4 e5 2. Nc3 Nc6 3. f4 exf4 4. Nf3 g5 5. h4 g4 6. Ng5
Vienna, Hamppe-Allgaier gambit, Alapin variation
7a270d85-d005-45ef-bf9d-c5ae54fd29d9
1. e4 e5 2. Nc3 Nc6 3. f4 exf4 4. Nf3 g5 5. h4 g4 6. Ng5 d6 
Vienna, Hamppe-Muzio gambit
72c939d6-5b4c-46fc-b860-563de298a39e
1. e4 e5 2. Nc3 Nc6 3. f4 exf4 4. Nf3 g5 5. Bc4 g4 6. O-O
Vienna, Hamppe-Muzio, Dubois variation
f9207466-a88f-406e-ad5d-46d0e7976fa1
1. e4 e5 2. Nc3 Nc6 3. f4 exf4 4. Nf3 g5 5. Bc4 g4 6. O-O gxf3 7. Qxf3 Ne5 8. Qxf4 Qf6 
Vienna, Pierce gambit
162b6f0d-ba4c-40ef-99ee-d0fe5e1860d9
1. e4 e5 2. Nc3 Nc6 3. f4 exf4 4. Nf3 g5 5. d4
Vienna, Pierce gambit, Rushmere attack
4e8358f7-82ae-4719-aa10-5c7e0aff50a9
1. e4 e5 2. Nc3 Nc6 3. f4 exf4 4. Nf3 g5 5. d4 g4 6. Bc4 gxf3 7. O-O d5 8. exd5 Bg4 9. dxc6
******C26: Vienna, Falkbeer variation
Vienna, Falkbeer variation
3f764941-5552-49e1-8414-0e6f17f403dd
1. e4 e5 2. Nc3 Nf6 
Vienna, Mengarini variation
6bceeda8-6a6b-4074-9c66-80321836a46a
1. e4 e5 2. Nc3 Nf6 3. a3
Vienna, Paulsen-Mieses variation
7818fb87-86e8-4f5f-a0a1-2e96a66c24a4
1. e4 e5 2. Nc3 Nf6 3. g3
Vienna game
b120663a-afae-410d-9e54-46382f2f9ffd
1. e4 e5 2. Nc3 Nf6 3. Bc4
******C27: Vienna game
Vienna game
60f7ae78-1802-4762-b539-f52035c93d3b
1. e4 e5 2. Nc3 Nf6 3. Bc4 Nxe4 
Vienna, `Frankenstein-Dracula' variation
86a6af21-7d4a-495f-9e5b-098919589512
1. e4 e5 2. Nc3 Nf6 3. Bc4 Nxe4 4. Qh5 Nd6 5. Bb3 Nc6 6. Nb5 g6 7. Qf3 f5 8. Qd5 Qe7 9. Nxc7+ Kd8 10. Nxa8 b6 
Vienna, Adams' gambit
d1b7e150-92a6-4fec-99a8-2dd84c71c2fd
1. e4 e5 2. Nc3 Nf6 3. Bc4 Nxe4 4. Qh5 Nd6 5. Bb3 Nc6 6. d4
Vienna game
1814e688-26bb-4d79-8733-0d4c32011b90
1. e4 e5 2. Nc3 Nf6 3. Bc4 Nxe4 4. Qh5 Nd6 5. Bb3 Be7 
Vienna, Alekhine variation
674f560d-0b52-4877-ad5f-638fd1d0460e
1. e4 e5 2. Nc3 Nf6 3. Bc4 Nxe4 4. Qh5 Nd6 5. Bb3 Be7 6. Nf3 Nc6 7. Nxe5
Boden-Kieseritsky gambit
cb35ee93-7fb0-4303-8ed6-39bb002b79ae
1. e4 e5 2. Nc3 Nf6 3. Bc4 Nxe4 4. Nf3
Boden-Kieseritsky gambit, Lichtenhein defence
cc698114-d62c-4918-adac-ddca0f95d1f0
1. e4 e5 2. Nc3 Nf6 3. Bc4 Nxe4 4. Nf3 d5 
******C28: Vienna game
Vienna game
79205c86-b0df-4354-a3ad-8ed365666b39
1. e4 e5 2. Nc3 Nf6 3. Bc4 Nc6 
******C29: Vienna gambit
Vienna gambit
48d4b9e1-d0e9-4458-82c9-4e2ebbfcf01d
1. e4 e5 2. Nc3 Nf6 3. f4 d5 
Vienna gambit, Kaufmann variation
b21e3462-c8f4-4b58-88e5-bc51ba65c9a6
1. e4 e5 2. Nc3 Nf6 3. f4 d5 4. fxe5 Nxe4 5. Nf3 Bg4 6. Qe2
Vienna gambit, Breyer variation
adc2d973-943f-40f2-9301-bc39b29b6b56
1. e4 e5 2. Nc3 Nf6 3. f4 d5 4. fxe5 Nxe4 5. Nf3 Be7 
Vienna gambit, Paulsen attack
09ecda3a-d8a3-485d-ad8e-21e9f131eff3
1. e4 e5 2. Nc3 Nf6 3. f4 d5 4. fxe5 Nxe4 5. Qf3
Vienna gambit, Bardeleben variation
d72a2661-e3e9-4233-804d-b76959cb5100
1. e4 e5 2. Nc3 Nf6 3. f4 d5 4. fxe5 Nxe4 5. Qf3 f5 
Vienna gambit, Heyde variation
127efa05-d765-4129-9544-17bf10a57419
1. e4 e5 2. Nc3 Nf6 3. f4 d5 4. fxe5 Nxe4 5. Qf3 f5 6. d4
Vienna gambit
9da9bf03-778d-4886-8728-4a945396d626
1. e4 e5 2. Nc3 Nf6 3. f4 d5 4. fxe5 Nxe4 5. d3
Vienna gambit, Wurzburger trap
0b36c8b7-ec5b-47a3-9d7b-cbb98d9e14a7
1. e4 e5 2. Nc3 Nf6 3. f4 d5 4. fxe5 Nxe4 5. d3 Qh4+ 6. g3 Nxg3 7. Nf3 Qh5 8. Nxd5
Vienna gambit, Steinitz variation
e0386571-bafb-439b-9dc1-a99ae32bd289
1. e4 e5 2. Nc3 Nf6 3. f4 d5 4. d3
******C30: King's gambit
King's gambit
e85504ec-fc8d-406b-a56c-3e6594ea6978
1. e4 e5 2. f4
King's Gambit Declined, Keene's defence
94aab111-b709-460e-9a67-2110c8cf6ae4
1. e4 e5 2. f4 Qh4+ 3. g3 Qe7 
King's Gambit Declined, Mafia defence
8375fb85-3c9b-408f-ac6b-d6e01704347c
1. e4 e5 2. f4 c5 
King's Gambit Declined, Norwalde variation
a9dd3f02-623f-4b18-b6c9-739d3885acd6
1. e4 e5 2. f4 Qf6 
King's Gambit Declined, Norwalde variation, Buecker gambit
7fa93ee4-2699-457c-8bc7-dd5f5d694081
1. e4 e5 2. f4 Qf6 3. Nf3 Qxf4 4. Nc3 Bb4 5. Bc4
King's Gambit Declined, classical variation
f47e2fd2-bc9b-4b24-96d2-8125c8a4d6dd
1. e4 e5 2. f4 Bc5 
King's Gambit Declined, classical, Svenonius variation
70dd526f-ea48-4559-8d9c-b92c5fb47073
1. e4 e5 2. f4 Bc5 3. Nf3 d6 4. Nc3 Nf6 5. Bc4 Nc6 6. d3 Bg4 7. h3 Bxf3 8. Qxf3 exf4 
King's Gambit Declined, classical, Hanham variation
a2dd6e64-c9e2-445c-9186-c70b4706f600
1. e4 e5 2. f4 Bc5 3. Nf3 d6 4. Nc3 Nd7 
King's Gambit Declined, classical, 4.c3
57f0c619-adf6-4bd6-a8ed-7283413cade6
1. e4 e5 2. f4 Bc5 3. Nf3 d6 4. c3
King's Gambit Declined, classical, Marshall attack
35e73faf-6423-4ac4-988d-1673750e9b65
1. e4 e5 2. f4 Bc5 3. Nf3 d6 4. c3 Bg4 5. fxe5 dxe5 6. Qa4+
King's Gambit Declined, classical counter-gambit
45e49ad3-cb82-4a58-a946-d042507fa55f
1. e4 e5 2. f4 Bc5 3. Nf3 d6 4. c3 f5 
King's Gambit Declined, classical, Reti variation
15959f30-d05a-4cc7-8a0e-91c031bad89b
1. e4 e5 2. f4 Bc5 3. Nf3 d6 4. c3 f5 5. fxe5 dxe5 6. d4 exd4 7. Bc4
King's Gambit Declined, classical, Soldatenkov variation
ebea7d02-cafc-4ffe-ac01-72f0b1015757
1. e4 e5 2. f4 Bc5 3. Nf3 d6 4. fxe5
King's Gambit Declined, classical, Heath variation
d64029d3-6521-481f-a641-4c2bfbf9c658
1. e4 e5 2. f4 Bc5 3. Nf3 d6 4. b4
King's Gambit Declined, 2...Nf6
df4b623e-fe9a-4051-b337-1bb51071bd7d
1. e4 e5 2. f4 Nf6 
******C31: King's Gambit Declined, Falkbeer counter-gambit
King's Gambit Declined, Falkbeer counter-gambit
6f3a34e0-7b37-4dcf-b226-17a5645e140a
1. e4 e5 2. f4 d5 
King's Gambit Declined, Falkbeer, Tartakower variation
60a08013-1ce2-4c2e-b82e-336bb71f0e77
1. e4 e5 2. f4 d5 3. Nf3
King's Gambit Declined, Falkbeer, Milner-Barry variation
85d1d743-a506-4718-b2b0-38e344f06d56
1. e4 e5 2. f4 d5 3. Nc3
King's Gambit Declined, Falkbeer counter-gambit
4d8f899d-24d8-4970-a799-b80fa3ce9426
1. e4 e5 2. f4 d5 3. exd5
King's Gambit Declined, Nimzovich counter-gambit
d524bf5d-2fa6-4af1-ae73-83f956ffacb5
1. e4 e5 2. f4 d5 3. exd5 c6 
King's Gambit Declined, Falkbeer, 3...e4
025dda31-810a-4174-a8c6-7b3eff2e1170
1. e4 e5 2. f4 d5 3. exd5 e4 
King's Gambit Declined, Falkbeer, Rubinstein variation
e79c3ac1-7e82-4fec-b5c9-597da17b4dc0
1. e4 e5 2. f4 d5 3. exd5 e4 4. Nc3 Nf6 5. Qe2
King's Gambit Declined, Falkbeer, Nimzovich variation
72d96baa-941d-4075-97da-470da6c2b1a1
1. e4 e5 2. f4 d5 3. exd5 e4 4. Bb5+
King's Gambit Declined, Falkbeer, 4.d3
3eeedff5-562e-45e9-8a96-4d903ff2deb5
1. e4 e5 2. f4 d5 3. exd5 e4 4. d3
King's Gambit Declined, Falkbeer, Morphy gambit
271cdba0-2451-4b90-b77e-2935517b43a3
1. e4 e5 2. f4 d5 3. exd5 e4 4. d3 Nf6 5. Nc3 Bb4 6. Bd2 e3 
******C32: King's Gambit Declined, Falkbeer, 5.de
King's Gambit Declined, Falkbeer, 5.de
a5e2d1d3-d35e-42da-89e8-d39108879820
1. e4 e5 2. f4 d5 3. exd5 e4 4. d3 Nf6 5. dxe4
King's Gambit Declined, Falkbeer, Alapin variation
63702366-4bea-43d8-b36f-2500ac01124e
1. e4 e5 2. f4 d5 3. exd5 e4 4. d3 Nf6 5. dxe4 Nxe4 6. Nf3 Bc5 7. Qe2 Bf2+ 8. Kd1 Qxd5+ 9. Nfd2
King's Gambit Declined, Falkbeer, main line, 7...Bf5
634c010a-e7df-4f38-ada5-c60d556270a1
1. e4 e5 2. f4 d5 3. exd5 e4 4. d3 Nf6 5. dxe4 Nxe4 6. Nf3 Bc5 7. Qe2 Bf5 
King's Gambit Declined, Falkbeer, Tarrasch variation
684ede0b-8815-4e2a-9956-8cf4bf351a70
1. e4 e5 2. f4 d5 3. exd5 e4 4. d3 Nf6 5. dxe4 Nxe4 6. Nf3 Bc5 7. Qe2 Bf5 8. g4 O-O 
King's Gambit Declined, Falkbeer, Charousek gambit
f3ca6de6-d042-43fb-b2f2-4e40a974395c
1. e4 e5 2. f4 d5 3. exd5 e4 4. d3 Nf6 5. dxe4 Nxe4 6. Qe2
King's Gambit Declined, Falkbeer, Charousek variation
e69f5645-d37e-4479-ac33-2b7ab81007d6
1. e4 e5 2. f4 d5 3. exd5 e4 4. d3 Nf6 5. dxe4 Nxe4 6. Qe2 Qxd5 7. Nd2 f5 8. g4
King's Gambit Declined, Falkbeer, Keres variation
428e07f8-8321-45d2-8327-858ff7669568
1. e4 e5 2. f4 d5 3. exd5 e4 4. d3 Nf6 5. Nd2
King's Gambit Declined, Falkbeer, Reti variation
8c15d27a-169e-4b61-918d-1aa6ea5394ef
1. e4 e5 2. f4 d5 3. exd5 e4 4. d3 Nf6 5. Qe2
******C33: King's gambit accepted
King's gambit accepted
33ef5c65-65de-4c35-82a2-47f763ad8ae1
1. e4 e5 2. f4 exf4 
King's Gambit Accepted, Tumbleweed gambit
2f59be80-88dd-4f11-901e-f1647717bcfc
1. e4 e5 2. f4 exf4 3. Kf2
King's Gambit Accepted, Orsini gambit
9a88ef48-1dfa-4cca-8da6-e3e024c521d7
1. e4 e5 2. f4 exf4 3. b3
King's Gambit Accepted, Pawn's gambit (Stamma gambit)
5c9fb876-5fcf-4b16-893d-88dc3648741a
1. e4 e5 2. f4 exf4 3. h4
King's Gambit Accepted, Schurig gambit
09678251-7132-445f-847f-62b8568c8fd0
1. e4 e5 2. f4 exf4 3. Bd3
King's Gambit Accepted, Carrera (Basman) gambit
d9adbd24-85a9-4fbd-bd36-36836d301e21
1. e4 e5 2. f4 exf4 3. Qe2
King's Gambit Accepted, Villemson (Steinitz) gambit
e4abfbeb-65c5-4a36-bc2d-724b15160582
1. e4 e5 2. f4 exf4 3. d4
King's Gambit Accepted, Keres (Mason-Steinitz) gambit
ff5391d6-e296-4ae5-91f1-e2b64c6bd0da
1. e4 e5 2. f4 exf4 3. Nc3
King's Gambit Accepted, Breyer gambit
2f7dc459-8a08-4ea2-a5ee-0a4d67a594c2
1. e4 e5 2. f4 exf4 3. Qf3
King's Gambit Accepted, Lesser bishop's (Petroff-Jaenisch-Tartakower) gambit
02c57ae0-1b92-40b6-98b2-eef79b74053a
1. e4 e5 2. f4 exf4 3. Be2
King's Gambit Accepted, bishop's gambit
4a661125-0d27-4cf2-be95-4b672f05b9d4
1. e4 e5 2. f4 exf4 3. Bc4
King's Gambit Accepted, bishop's gambit, Chigorin's attack
9a368738-b7a1-4dba-96f6-c2ad59b6e577
1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 d5 5. Bxd5 g5 6. g3
King's Gambit Accepted, bishop's gambit, Greco variation
4aa548d3-08d2-4652-96ec-b4cdd3a0b21e
1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 Bc5 
King's Gambit Accepted, bishop's gambit, classical defence
bc240f1f-2747-48e5-bda3-a2b67c1355e7
1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 g5 
King's Gambit Accepted, bishop's gambit, Grimm attack
77a7e8d9-be15-46fc-a93d-e2bb9b62fff1
1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 g5 5. Nc3 Bg7 6. d4 d6 7. e5
King's Gambit Accepted, bishop's gambit, classical defence
f4962e15-4280-4a22-984b-66aa31e900bd
1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 g5 5. Nc3 Bg7 6. d4 Ne7 
King's Gambit Accepted, bishop's gambit, McDonnell attack
9ab9d560-4d0c-4f43-a1d3-bad258e85ea3
1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 g5 5. Nc3 Bg7 6. d4 Ne7 7. g3
King's Gambit Accepted, bishop's gambit, McDonnell attack
59dbbca7-f75f-4ede-8ce6-3d45f1cb0427
1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 g5 5. Nc3 Bg7 6. g3
King's Gambit Accepted, bishop's gambit, Fraser variation
fa7e9329-0bd5-4576-8ea9-53550a298246
1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 g5 5. Nc3 Bg7 6. g3 fxg3 7. Qf3
King's Gambit Accepted, bishop's gambit, classical defence, Cozio attack
b66955e6-3fb7-4e4f-b929-331316d9b13a
1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 g5 5. Qf3
King's Gambit Accepted, bishop's gambit, Boden defence
9c457121-5682-4f41-8436-1fc1fb010cab
1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 Nc6 
King's Gambit Accepted, bishop's gambit, Bryan counter-gambit
ca4e185a-d490-4498-a63e-5c06ab0ff6d2
1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 b5 
King's Gambit Accepted, bishop's gambit, Bryan counter-gambit
4b8fc90a-4324-453e-89a5-11187177c032
1. e4 e5 2. f4 exf4 3. Bc4 b5 
King's Gambit Accepted, bishop's gambit, Steinitz defence
c70f9ffa-410a-46c1-8eae-91b22458de1a
1. e4 e5 2. f4 exf4 3. Bc4 Ne7 
King's Gambit Accepted, bishop's gambit, Maurian defence
ace0c12e-b7e7-4809-ad4c-cf8ad8b2a529
1. e4 e5 2. f4 exf4 3. Bc4 Nc6 
King's Gambit Accepted, bishop's gambit, Ruy Lopez defence
3253ac1e-6aff-47b4-b3d3-0b553d80a050
1. e4 e5 2. f4 exf4 3. Bc4 c6 
King's Gambit Accepted, bishop's gambit, Lopez-Gianutio counter-gambit
1d65459e-2838-4b85-9bdf-cb184acb0c10
1. e4 e5 2. f4 exf4 3. Bc4 f5 
King's Gambit Accepted, Lopez-Gianutio counter-gambit, Hein variation
f0f35725-f9ee-42c1-a719-2653d92e2eed
1. e4 e5 2. f4 exf4 3. Bc4 f5 4. Qe2 Qh4+ 5. Kd1 fxe4 6. Nc3 Kd8 
King's Gambit Accepted, bishop's gambit, Bledow variation
3c32f225-8ef4-4519-aed5-d37168cfc0dd
1. e4 e5 2. f4 exf4 3. Bc4 d5 
King's Gambit Accepted, bishop's gambit, Gifford variation
c24e3327-1e1d-4004-a966-d2fc211eeb96
1. e4 e5 2. f4 exf4 3. Bc4 d5 4. Bxd5 Qh4+ 5. Kf1 g5 6. g3
King's Gambit Accepted, bishop's gambit, Boren-Svenonius variation
140ed18f-2f73-44d9-9eca-20fc785db219
1. e4 e5 2. f4 exf4 3. Bc4 d5 4. Bxd5 Qh4+ 5. Kf1 Bd6 
King's Gambit Accepted, bishop's gambit, Anderssen variation
824ebd42-965a-4a89-b8b4-1a68668b3f3e
1. e4 e5 2. f4 exf4 3. Bc4 d5 4. Bxd5 c6 
King's Gambit Accepted, bishop's gambit, Morphy variation
19a6826c-3bce-4c8c-9803-bfe0ea7b2636
1. e4 e5 2. f4 exf4 3. Bc4 d5 4. Bxd5 Nf6 
King's Gambit Accepted, bishop's gambit, Cozio (Morphy) defence
45f05ec8-4a6a-4d3d-a054-0aba16cde618
1. e4 e5 2. f4 exf4 3. Bc4 Nf6 
King's Gambit Accepted, bishop's gambit, Bogolyubov variation
1fe8b324-d84c-4f1f-be4f-c70771a246dc
1. e4 e5 2. f4 exf4 3. Bc4 Nf6 4. Nc3
King's Gambit Accepted, bishop's gambit, Paulsen attack
4ead9dea-8e11-43d2-8e40-b17cdd2bde66
1. e4 e5 2. f4 exf4 3. Bc4 Nf6 4. Nc3 Bb4 5. e5
King's Gambit Accepted, bishop's gambit, Jaenisch variation
c5aa97df-831a-440f-8929-8e5694cebde8
1. e4 e5 2. f4 exf4 3. Bc4 Nf6 4. Nc3 c6 
******C34: King's Gambit Accepted
King's Gambit Accepted
cc128cd0-8ad2-4ac2-8168-145dfcd91188
1. e4 e5 2. f4 exf4 3. Nf3
King's Gambit Accepted, Bonsch-Osmolovsky variation
c6cb59e6-e801-4793-80e7-c485f26c0167
1. e4 e5 2. f4 exf4 3. Nf3 Ne7 
King's Gambit Accepted, Gianutio counter-gambit
5e5af26b-5b03-4e78-a19d-ea842f5c19f1
1. e4 e5 2. f4 exf4 3. Nf3 f5 
King's Gambit Accepted, Fischer defence
782c6a69-8e36-4b62-891a-2a4b2097ddea
1. e4 e5 2. f4 exf4 3. Nf3 d6 
King's Gambit Accepted, Becker defence
be7eae1f-3605-40f5-af8c-a8567e58d406
1. e4 e5 2. f4 exf4 3. Nf3 h6 
King's Gambit Accepted, Schallop defence
a07af602-5166-43c3-8c86-53d28b04ad16
1. e4 e5 2. f4 exf4 3. Nf3 Nf6 
******C35: King's Gambit Accepted, Cunningham defence
King's Gambit Accepted, Cunningham defence
00bc0b57-a32c-42ea-bff7-792d4c4ae5d6
1. e4 e5 2. f4 exf4 3. Nf3 Be7 
King's Gambit Accepted, Cunningham, Bertin gambit
05163197-49ef-4fa9-b82b-8399bf5664c0
1. e4 e5 2. f4 exf4 3. Nf3 Be7 4. Bc4 Bh4+ 5. g3
King's Gambit Accepted, Cunningham, three pawns gambit
5aa27381-9b80-4223-8750-d82f8e2f7f53
1. e4 e5 2. f4 exf4 3. Nf3 Be7 4. Bc4 Bh4+ 5. g3 fxg3 6. O-O gxh2+ 7. Kh1
King's Gambit Accepted, Cunningham, Euwe defence
b66a6d56-f8f0-4a78-a6a2-af0de11d1859
1. e4 e5 2. f4 exf4 3. Nf3 Be7 4. Bc4 Nf6 
******C36: King's Gambit Accepted, Abbazia defence (classical defence, modern defence[!])
King's Gambit Accepted, Abbazia defence (classical defence, modern defence[!])
067dc520-b2c3-4391-b431-1299b5a78a7d
1. e4 e5 2. f4 exf4 3. Nf3 d5 
King's Gambit Accepted, Abbazia defence, modern variation
c95a7803-d340-46a3-a9ba-fa4fa3369561
1. e4 e5 2. f4 exf4 3. Nf3 d5 4. exd5 Nf6 
King's Gambit Accepted, Abbazia defence, Botvinnik variation
7dede761-daa5-4cd3-82df-b9b9c9ba64aa
1. e4 e5 2. f4 exf4 3. Nf3 d5 4. exd5 Nf6 5. Bb5+ c6 6. dxc6 bxc6 7. Bc4 Nd5 
******C37: King's Gambit Accepted, Quaade gambit
King's Gambit Accepted, Quaade gambit
12852eb5-d795-44c0-b679-944ab1bd955c
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Nc3
King's Gambit Accepted, Rosentreter gambit
ecec08e0-830d-48d4-afd2-c35e5e4c97d4
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. d4
King's Gambit Accepted, Soerensen gambit
a213c9c0-8263-42c9-b30a-82339ba4a71e
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. d4 g4 5. Ne5
King's Gambit Accepted, King's knight's gambit
59994256-d683-4f56-a464-81dc89eb629b
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4
King's Gambit Accepted, Blachly gambit
e746bed0-ef73-4ffc-aef4-763fb409bc92
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 Nc6 
King's Gambit Accepted, Lolli gambit (wild Muzio gambit)
5ca2bd2d-50a0-43ff-b867-4cee3c2c9217
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. Bxf7+
King's Gambit Accepted, Lolli gambit, Young variation
8f2a2008-74be-4561-b172-7efde6cbbd33
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. Bxf7+ Kxf7 6. O-O gxf3 7. Qxf3 Qf6 8. d4 Qxd4+ 9. Be3 Qf6 10. Nc3
King's Gambit Accepted, Ghulam Kassim gambit
ba3e1f51-9235-4237-bd8b-bbaaac35f0e3
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. d4
King's Gambit Accepted, MacDonnell gambit
ec10548a-b612-49dc-ba86-9bed6e93fe35
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. Nc3
King's Gambit Accepted, Salvio gambit
9d49bef7-610c-4eaa-8ac9-04fb383ed854
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. Ne5
King's Gambit Accepted, Silberschmidt gambit
fb556466-72e0-4b67-bae4-87e5db449eb9
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. Ne5 Qh4+ 6. Kf1 Nh6 7. d4 f3 
King's Gambit Accepted, Salvio gambit, Anderssen counter-attack
2de75a9d-aa69-4f22-9dae-ca8601fe7d21
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. Ne5 Qh4+ 6. Kf1 Nh6 7. d4 d6 
King's Gambit Accepted, Cochrane gambit
75714d7d-7627-42cb-8170-d49194be23d3
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. Ne5 Qh4+ 6. Kf1 f3 
King's Gambit Accepted, Herzfeld gambit
68ecebd6-6882-4844-90ab-04adb5eba9b1
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. Ne5 Qh4+ 6. Kf1 Nc6 
King's Gambit Accepted, Muzio gambit
e78164ae-13cf-42e9-a03d-3600890c7bf0
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. O-O
King's Gambit Accepted, Muzio gambit, Paulsen variation
e6c397de-1a29-456a-adcb-c83767505989
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. O-O gxf3 6. Qxf3 Qf6 7. e5 Qxe5 8. d3 Bh6 9. Nc3 Ne7 10. Bd2 Nbc6 11. Rae1
King's Gambit Accepted, double Muzio gambit
eb608f34-9e17-4b75-aa03-f362585fa78f
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. O-O gxf3 6. Qxf3 Qf6 7. e5 Qxe5 8. Bxf7+
King's Gambit Accepted, Muzio gambit, From defence
cb9b532b-f27d-410d-ae80-d2e2751549f8
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. O-O gxf3 6. Qxf3 Qe7 
King's Gambit Accepted, Muzio gambit, Holloway defence
239ab639-8455-495d-8850-962ec8b3c7b7
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. O-O gxf3 6. Qxf3 Nc6 
King's Gambit Accepted, Muzio gambit, Kling and Horwitz counter-attack
1cb11d35-d791-4c5e-b36d-4de49a0f9fd6
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. O-O Qe7 
King's Gambit Accepted, Muzio gambit, Brentano defence
9bd0a5a8-aac1-4b8a-ac61-62cb9e4b3b73
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. O-O d5 
******C38: King's Gambit Accepted
King's Gambit Accepted
ca6039aa-359b-46e2-884e-b4b09f31e8d3
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 Bg7 
King's Gambit Accepted, Hanstein gambit
d2be9b96-9370-4781-a5d9-988dacc536ab
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 Bg7 5. O-O
King's Gambit Accepted, Philidor gambit
9fb30ef7-6fb5-4816-8e17-39e3a96c370c
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 Bg7 5. h4
King's Gambit Accepted, Greco gambit
6e9a4d2e-9b02-43a7-80a4-5e0e93c64fb8
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 Bg7 5. h4 h6 6. d4 d6 7. Nc3 c6 8. hxg5 hxg5 9. Rxh8 Bxh8 10. Ne5
King's Gambit Accepted, Philidor gambit, Schultz variation
d4d7d493-460c-4570-976e-a3b676bb3fd1
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 Bg7 5. h4 h6 6. d4 d6 7. Qd3
******C39: King's Gambit Accepted
King's Gambit Accepted
3df86716-fc78-428c-a712-61ebb85412aa
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4
King's Gambit Accepted, Allgaier gambit
c7bc740b-9351-415c-a3af-1dd7e3d917e6
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ng5
King's Gambit Accepted, Allgaier, Horny defence
2acdcbd4-17fe-4e2c-8a39-b2f1ee00bc67
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ng5 h6 6. Nxf7 Kxf7 7. Qxg4 Nf6 8. Qxf4 Bd6 
King's Gambit Accepted, Allgaier, Thorold variation
bbf0d4f3-7031-4c92-a5d5-b6cb2a2cd899
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ng5 h6 6. Nxf7 Kxf7 7. d4
King's Gambit Accepted, Allgaier, Cook variation
c6b41c69-c430-4c78-bde5-2ef127c5c8b5
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ng5 h6 6. Nxf7 Kxf7 7. d4 d5 8. Bxf4 dxe4 9. Bc4+ Kg7 10. Be5+
King's Gambit Accepted, Allgaier, Blackburne gambit
20cebc38-4012-476b-8a2c-e8b51efdc384
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ng5 h6 6. Nxf7 Kxf7 7. Nc3
King's Gambit Accepted, Allgaier, Walker attack
fa7b8639-7c1e-4aec-8561-f0d0c50e93d6
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ng5 h6 6. Nxf7 Kxf7 7. Bc4+
King's Gambit Accepted, Allgaier, Urusov attack
8f63a417-07ee-486b-ba17-304ea941bba0
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ng5 h6 6. Nxf7 Kxf7 7. Bc4+ d5 8. Bxd5+ Kg7 9. d4
King's Gambit Accepted, Allgaier, Schlechter defence
984adc57-0804-45f1-a666-7c63874a76ea
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ng5 Nf6 
King's Gambit Accepted, Kieseritsky, Paulsen defence
7a6234af-dbd9-4a3f-ba4d-703002e05bc3
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 Bg7 
King's Gambit Accepted, Kieseritsky, long whip (Stockwhip, classical) defence
d56c0bae-fc06-4c5b-9c53-1e7a19bd94fa
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 h5 
King's Gambit Accepted, Kieseritsky, long whip defence, Jaenisch variation
98b7d4e6-d708-4935-9931-3d1bd03d9fb8
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 h5 6. Bc4 Rh7 7. d4 Bh6 8. Nc3
King's Gambit Accepted, Kieseritsky, Brentano (Campbell) defence
78b68808-1a4f-4a60-b924-3cc84774ea56
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 d5 
King's Gambit Accepted, Kieseritsky, Brentano defence, Kaplanek variation
d913c2ce-1ff8-418d-ad71-52c58ee33906
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 d5 6. d4 Nf6 7. exd5 Qxd5 8. Nc3 Bb4 9. Kf2
King's Gambit Accepted, Kieseritsky, Brentano defence
cbd57d3b-cbb9-42d9-aa87-7cd2f5bf386d
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 d5 6. d4 Nf6 7. Bxf4
King's Gambit Accepted, Kieseritsky, Brentano defence, Caro variation
0ae8c621-6b90-446f-b621-0189dfa4c148
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 d5 6. d4 Nf6 7. Bxf4 Nxe4 8. Nd2
King's Gambit Accepted, Kieseritsky, Salvio (Rosenthal) defence
d2ab9c22-66f5-4a81-8742-e5a2d701ed95
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 Qe7 
King's Gambit Accepted, Kieseritsky, Salvio defence, Cozio variation
88e5bcdb-4223-45b0-836b-050a57e684ab
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 Qe7 6. d4 f5 7. Bc4
King's Gambit Accepted, Kieseritsky, Polerio defence
3ec8ad6b-df2b-437b-9681-8b91e91f8d8d
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 Be7 
King's Gambit Accepted, Kieseritsky, Neumann defence
1164f9e5-502a-485e-afd9-5a1426c115d6
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 Nc6 
King's Gambit Accepted, Kieseritsky, Kolisch defence
9774efee-b8c6-45db-83c5-1ae6130132dc
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 d6 
King's Gambit Accepted, Kieseritsky, Berlin defence
af7c98fc-eb0c-4699-bda7-6723a26c6af7
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 Nf6 
King's Gambit Accepted, Kieseritsky, Berlin defence, Riviere variation
409b67ae-b7e1-422f-bb16-f1a302c1e3ca
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 Nf6 6. Nxg4 d5 
King's Gambit Accepted, Kieseritsky, Berlin defence, 6.Bc4
3d1e895f-b53e-42c0-955d-563b66818e31
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 Nf6 6. Bc4
King's Gambit Accepted, Kieseritsky, Rice gambit
1b80033f-f431-4f7e-8152-4b794686d55e
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 Nf6 6. Bc4 d5 7. exd5 Bd6 8. O-O
******C40: King's knight opening
King's knight opening
105aefad-c0b5-4bda-b394-0d9a7b6ef3ea
1. e4 e5 2. Nf3
Gunderam defence
f4a59a50-ffb6-40de-a064-8e507d1b22e0
1. e4 e5 2. Nf3 Qe7 
Greco defence
13385344-3b68-4630-aaef-9070f1de288e
1. e4 e5 2. Nf3 Qf6 
Damiano's defence
9136ff5d-51fe-4802-8750-194521ed44a3
1. e4 e5 2. Nf3 f6 
QP counter-gambit (elephant gambit)
42c7104d-d510-4752-ac2e-7912d4a56c69
1. e4 e5 2. Nf3 d5 
QP counter-gambit, Maroczy gambit
e6bf935a-961c-4666-843c-368400519f44
1. e4 e5 2. Nf3 d5 3. exd5 Bd6 
Latvian counter-gambit
e8d48927-9d54-4a67-9338-bb4a879056d2
1. e4 e5 2. Nf3 f5 
Latvian, Nimzovich variation
b02ff80f-99e4-47f3-8482-a0ca8c0fed0c
1. e4 e5 2. Nf3 f5 3. Nxe5 Qf6 4. d4 d6 5. Nc4 fxe4 6. Ne3
Latvian, Fraser defence
25928fa9-15b5-4c39-a69a-9e230e26673c
1. e4 e5 2. Nf3 f5 3. Nxe5 Nc6 
Latvian gambit, 3.Bc4
19bb6d8a-6cb8-4c04-8a39-d9875bce5fa0
1. e4 e5 2. Nf3 f5 3. Bc4
Latvian, Behting variation
e01b4557-ef31-49c9-a447-caec1f3082cf
1. e4 e5 2. Nf3 f5 3. Bc4 fxe4 4. Nxe5 Qg5 5. Nf7 Qxg2 6. Rf1 d5 7. Nxh8 Nf6 
Latvian, Polerio variation
cf2c6d76-b8bc-4637-86c4-7ffc18032bf5
1. e4 e5 2. Nf3 f5 3. Bc4 fxe4 4. Nxe5 d5 
Latvian, corkscrew counter-gambit
fb100ada-fbf3-4186-91c1-358a56e6e8b0
1. e4 e5 2. Nf3 f5 3. Bc4 fxe4 4. Nxe5 Nf6 
******C41: Philidor's defence
Philidor's defence
3c84e9b4-3d76-4d4b-9224-9ec1e0bb5911
1. e4 e5 2. Nf3 d6 
Philidor, Steinitz variation
036adc03-750b-4a91-b52f-c1ea85b0091c
1. e4 e5 2. Nf3 d6 3. Bc4 Be7 4. c3
Philidor, Lopez counter-gambit
a4df0d24-7b36-485d-9ff7-f65c31e2e3c7
1. e4 e5 2. Nf3 d6 3. Bc4 f5 
Philidor, Lopez counter-gambit, Jaenisch variation
a74750d8-d012-449e-aa9d-d122adb7862a
1. e4 e5 2. Nf3 d6 3. Bc4 f5 4. d4 exd4 5. Ng5 Nh6 6. Nxh7
Philidor's defence
dc0d3ece-1854-4012-bea1-eb7dbeb13697
1. e4 e5 2. Nf3 d6 3. d4
Philidor, Philidor counter-gambit
701f4d74-1aff-4266-9178-3bdbf1d1a357
1. e4 e5 2. Nf3 d6 3. d4 f5 
Philidor, Philidor counter-gambit, del Rio attack
63f3a8b6-8331-481c-a63c-5a4157b5de87
1. e4 e5 2. Nf3 d6 3. d4 f5 4. dxe5 fxe4 5. Ng5 d5 6. e6
Philidor, Philidor counter-gambit, Berger variation
a725469c-601d-4260-b507-221e175d6867
1. e4 e5 2. Nf3 d6 3. d4 f5 4. dxe5 fxe4 5. Ng5 d5 6. e6 Bc5 7. Nc3
Philidor, Philidor counter-gambit, Zukertort variation
9c483589-1db7-4c82-93c8-ea9847f8f73b
1. e4 e5 2. Nf3 d6 3. d4 f5 4. Nc3
Philidor, exchange variation
65b97e64-2502-48e0-9d14-3a1c03dbccd3
1. e4 e5 2. Nf3 d6 3. d4 exd4 
Philidor, Boden variation
3a1d2e33-a86f-463d-9a89-d82ec8fec9b3
1. e4 e5 2. Nf3 d6 3. d4 exd4 4. Qxd4 Bd7 
Philidor, exchange variation
903d6434-3773-468d-a61c-f7aebe5de5a3
1. e4 e5 2. Nf3 d6 3. d4 exd4 4. Nxd4
Philidor, Paulsen attack
99ece7a0-f1c0-49f6-9772-7c89c50a21ac
1. e4 e5 2. Nf3 d6 3. d4 exd4 4. Nxd4 d5 5. exd5
Philidor, exchange variation
73c55ce4-3add-480c-b8f2-5d5d8943fa29
1. e4 e5 2. Nf3 d6 3. d4 exd4 4. Nxd4 Nf6 
Philidor, Berger variation
a3bc33d6-3d1b-4a36-be5b-27d5cf5b7d86
1. e4 e5 2. Nf3 d6 3. d4 exd4 4. Nxd4 Nf6 5. Nc3 Be7 6. Be2 O-O 7. O-O c5 8. Nf3 Nc6 9. Bg5 Be6 10. Re1
Philidor, Larsen variation
2aaeeca0-d74e-428d-9071-b920a2e31599
1. e4 e5 2. Nf3 d6 3. d4 exd4 4. Nxd4 g6 
Philidor, Nimzovich (Jaenisch) variation
c2d779c0-8f48-4672-9ea0-cd7dd00aff76
1. e4 e5 2. Nf3 d6 3. d4 Nf6 
Philidor, Improved Hanham variation
ed48b2af-9632-481d-a9b6-32e308f36c71
1. e4 e5 2. Nf3 d6 3. d4 Nf6 4. Nc3 Nbd7 
Philidor, Nimzovich, Sozin variation
28aca7de-fc50-421a-bd6e-2f5272e0b35d
1. e4 e5 2. Nf3 d6 3. d4 Nf6 4. Nc3 Nbd7 5. Bc4 Be7 6. O-O O-O 7. Qe2 c6 8. a4 exd4 
Philidor, Nimzovich, Larobok variation
a04da419-d6b3-46d7-b305-2f6b1ba0f27f
1. e4 e5 2. Nf3 d6 3. d4 Nf6 4. Nc3 Nbd7 5. Bc4 Be7 6. Ng5 O-O 7. Bxf7+
Philidor, Nimzovich variation
1765b44d-450a-43c3-8a18-99e415f63f89
1. e4 e5 2. Nf3 d6 3. d4 Nf6 4. dxe5
Philidor, Nimzovich, Sokolsky variation
de390583-c77b-4de8-9413-0f7cbdca78df
1. e4 e5 2. Nf3 d6 3. d4 Nf6 4. dxe5 Nxe4 5. Nbd2
Philidor, Nimzovich, Rellstab variation
845325be-49bb-4935-8fb4-d4402ac1ce5e
1. e4 e5 2. Nf3 d6 3. d4 Nf6 4. dxe5 Nxe4 5. Qd5
Philidor, Nimzovich, Locock variation
af6afa36-a26f-48bc-84c2-2d2f0e793a30
1. e4 e5 2. Nf3 d6 3. d4 Nf6 4. Ng5
Philidor, Nimzovich, Klein variation
c88dd190-c40c-42b2-ae35-092038fad8c6
1. e4 e5 2. Nf3 d6 3. d4 Nf6 4. Bc4
Philidor, Hanham variation
967ce54e-7ee0-4b33-b8e2-5a11b8f763cc
1. e4 e5 2. Nf3 d6 3. d4 Nd7 
Philidor, Hanham, Krause variation
149c953b-5fa6-47ab-97fe-3e38d077705d
1. e4 e5 2. Nf3 d6 3. d4 Nd7 4. Bc4 c6 5. O-O

Philidor, Hanham, Steiner variation
91f35c1a-85e0-4a02-8131-a0aaf0fa94bc
1. e4 e5 2. Nf3 d6 3. d4 Nd7 4. Bc4 c6 5. O-O Be7 6. dxe5
Philidor, Hanham, Kmoch variation
aa61d857-6fe2-487a-bd32-4637065be8dd
1. e4 e5 2. Nf3 d6 3. d4 Nd7 4. Bc4 c6 5. Ng5
Philidor, Hanham, Berger variation
07482e3e-f009-4540-8e75-98112a890afe
1. e4 e5 2. Nf3 d6 3. d4 Nd7 4. Bc4 c6 5. Ng5 Nh6 6. f4 Be7 7. O-O O-O 8. c3 d5 
Philidor, Hanham, Schlechter variation
de274533-66e1-4095-838b-a0e2d767c46b
1. e4 e5 2. Nf3 d6 3. d4 Nd7 4. Bc4 c6 5. Nc3
Philidor, Hanham, Delmar variation
145dde31-7cce-4742-9cea-1c8338a5c0ff
1. e4 e5 2. Nf3 d6 3. d4 Nd7 4. Bc4 c6 5. c3
******C42: Petrov's defence
Petrov's defence
c6c81eb5-e62a-43df-b5cf-05f1b848d083
1. e4 e5 2. Nf3 Nf6 
Petrov, French attack
8d382c65-b272-48ad-95fd-417063779d65
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. d3
Petrov, Kaufmann attack
e2a6e294-72e4-485a-a197-d21b774b9d01
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. c4
Petrov, Nimzovich attack
e0c116bb-d1e8-4739-80cb-ed7f65af9517
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. Nc3
Petrov, Cozio (Lasker) attack
4402bba9-9981-49e7-b103-8c5097fcb4f4
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. Qe2
Petrov, classical attack
5f30eb4b-2dff-4928-82a1-212924372745
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. d4
Petrov, classical attack, Chigorin variation
1d20a001-1d25-44b2-b47b-69b0dff780cc
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. d4 d5 6. Bd3 Be7 7. O-O Nc6 8. Re1
Petrov, classical attack, Berger variation
589de5d7-0acd-4e59-832d-9ad7ef098751
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. d4 d5 6. Bd3 Be7 7. O-O Nc6 8. Re1 Bg4 9. c3 f5 10. Nbd2
Petrov, classical attack, Krause variation
be24ae0c-b4bf-49a6-b861-dda546ef87c6
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. d4 d5 6. Bd3 Be7 7. O-O Nc6 8. Re1 Bg4 9. c3 f5 10. c4
Petrov, classical attack, Maroczy variation
0c84dff5-84bb-44f9-94dd-dddd81196b91
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. d4 d5 6. Bd3 Be7 7. O-O Nc6 8. Re1 Bg4 9. c3 f5 10. c4 Bh4 
Petrov, classical attack, Jaenisch variation
982ca276-c307-47d1-9732-09c3ebe5c4f2
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. d4 d5 6. Bd3 Be7 7. O-O Nc6 8. c4
Petrov, classical attack, Mason variation
6d68567b-247b-43fa-8368-1cd93a69c47d
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. d4 d5 6. Bd3 Be7 7. O-O O-O 
Petrov, classical attack, Marshall variation
90034c48-26cd-4c3f-a870-9cd14880306e
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. d4 d5 6. Bd3 Bd6 
Petrov, classical attack, Tarrasch variation
a78182a8-910e-4515-8a83-aaf9fce8890a
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. d4 d5 6. Bd3 Bd6 7. O-O O-O 8. c4 Bg4 
Petrov, classical attack, Marshall trap
739fcab7-e9d4-480e-b7cf-53e5635db5a9
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. d4 d5 6. Bd3 Bd6 7. O-O O-O 8. c4 Bg4 9. cxd5 f5 10. Re1 Bxh2+ 
Petrov, classical attack, close variation
af5758bc-b868-4b3e-84d0-dcd438980191
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. d4 Nf6 
Petrov, Cochrane gambit
873f7d4f-6a85-43bf-ac6d-b62ebdbb9b68
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nxf7
Petrov, Paulsen attack
407dbb59-41b1-41af-b085-8f3f3ae4ada2
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nc4
Petrov, Damiano variation
3dc57628-54fa-4a3b-ae0b-c2a3fac3187a
1. e4 e5 2. Nf3 Nf6 3. Nxe5 Nxe4 
Petrov three knights game
e4d2df10-4f2f-4f56-93b5-bc6e50a27b7a
1. e4 e5 2. Nf3 Nf6 3. Nc3
Petrov, Italian variation
1afed0e8-df29-42ed-ad01-1493f15d0b47
1. e4 e5 2. Nf3 Nf6 3. Bc4
******C43: Petrov, modern (Steinitz) attack
Petrov, modern (Steinitz) attack
c7d792df-4a76-4839-8bc4-535697d6ab18
1. e4 e5 2. Nf3 Nf6 3. d4
Petrov, modern attack, main line
a1755b05-db9f-4b7b-8e9c-77105761ce17
1. e4 e5 2. Nf3 Nf6 3. d4 exd4 4. e5 Ne4 5. Qxd4
Petrov, modern attack, Steinitz variation
51e21954-cbd6-418a-80a3-d19b346cd991
1. e4 e5 2. Nf3 Nf6 3. d4 exd4 4. e5 Ne4 5. Qe2
Petrov, modern attack, Bardeleben variation
d5427a76-a3cf-42a7-8b81-47dd53976754
1. e4 e5 2. Nf3 Nf6 3. d4 exd4 4. e5 Ne4 5. Qe2 Nc5 6. Nxd4 Nc6 
Petrov, Urusov gambit
a4c21a11-55db-44bb-96a8-45739e99f135
1. e4 e5 2. Nf3 Nf6 3. d4 exd4 4. Bc4
Petrov, modern attack, Symmetrical variation
97c3362c-b06f-426c-bc09-db4e362e5477
1. e4 e5 2. Nf3 Nf6 3. d4 Nxe4 
Petrov, modern attack, Trifunovic variation
0f122165-8cc1-4ed2-b428-62d44de404e0
1. e4 e5 2. Nf3 Nf6 3. d4 Nxe4 4. Bd3 d5 5. Nxe5 Bd6 6. O-O O-O 7. c4 Bxe5 
******C44: King's pawn game
King's pawn game
90846b2a-6a3e-4519-87d6-13fe386af351
1. e4 e5 2. Nf3 Nc6 
Irish (Chicago) gambit
700e785c-c155-45e7-a462-63e471fb2ad6
1. e4 e5 2. Nf3 Nc6 3. Nxe5 Nxe5 4. d4
Konstantinopolsky opening
7be8d32c-1d20-4447-b557-c22a39b357d1
1. e4 e5 2. Nf3 Nc6 3. g3
Dresden opening
e3784d0a-bc0b-402c-8e15-22470ae3e2a0
1. e4 e5 2. Nf3 Nc6 3. c4
Inverted Hungarian
51181068-57f0-4113-ad20-4ca6f15bba7c
1. e4 e5 2. Nf3 Nc6 3. Be2
Inverted Hanham
9e039d73-2980-4804-af9d-918fd7825d87
1. e4 e5 2. Nf3 Nc6 3. Be2 Nf6 4. d3 d5 5. Nbd2
Tayler opening
8df66aa8-d8ad-4264-9d02-b70328562749
1. e4 e5 2. Nf3 Nc6 3. Be2 Nf6 4. d4
Ponziani opening
a030804b-d95b-4109-b93b-3d6a7b43b596
1. e4 e5 2. Nf3 Nc6 3. c3
Ponziani, Caro variation
628e3749-5edd-47e4-abeb-7469bbf94cc0
1. e4 e5 2. Nf3 Nc6 3. c3 d5 4. Qa4 Bd7 
Ponziani, Leonhardt variation
7a438d0c-6408-4e11-83a3-e73c899a450e
1. e4 e5 2. Nf3 Nc6 3. c3 d5 4. Qa4 Nf6 
Ponziani, Steinitz variation
63febac1-8d35-4be2-ac3a-265d921fb452
1. e4 e5 2. Nf3 Nc6 3. c3 d5 4. Qa4 f6 
Ponziani, Jaenisch counter-attack
ce7ec60a-0a52-4461-85cc-42af3459f57e
1. e4 e5 2. Nf3 Nc6 3. c3 Nf6 
Ponziani, Fraser defence
50e247e4-5c32-464b-8205-7fdcd5a96d54
1. e4 e5 2. Nf3 Nc6 3. c3 Nf6 4. d4 Nxe4 5. d5 Bc5 
Ponziani, Reti variation
0ce6bc90-dc8d-4b80-b2cb-2c3b7bc153b2
1. e4 e5 2. Nf3 Nc6 3. c3 Nge7 
Ponziani, Romanishin variation
3a09c2d0-0b3c-45da-8bc9-e7834729d68d
1. e4 e5 2. Nf3 Nc6 3. c3 Be7 
Ponziani counter-gambit
a951041c-a469-40b2-9055-812c8e30f00f
1. e4 e5 2. Nf3 Nc6 3. c3 f5 
Ponziani counter-gambit, Schmidt attack
4622e84f-65c3-404f-a774-5907fa33d30e
1. e4 e5 2. Nf3 Nc6 3. c3 f5 4. d4 d6 5. d5
Ponziani counter-gambit, Cordel variation
3248e4cd-8bae-4a69-a5c3-5a919422817c
1. e4 e5 2. Nf3 Nc6 3. c3 f5 4. d4 d6 5. d5 fxe4 6. Ng5 Nb8 7. Nxe4 Nf6 8. Bd3 Be7 
Scotch opening
0b1deacd-52c9-4072-b905-13bfd4d3b1c8
1. e4 e5 2. Nf3 Nc6 3. d4
Scotch, Lolli variation
4fc45b7b-936b-4c11-b3d7-079478f4cdd1
1. e4 e5 2. Nf3 Nc6 3. d4 Nxd4 
Scotch, Cochrane variation
8b7c75e5-09f3-498c-afaa-9579571c7b58
1. e4 e5 2. Nf3 Nc6 3. d4 Nxd4 4. Nxe5 Ne6 5. Bc4 c6 6. O-O Nf6 7. Nxf7
Scotch, Relfsson gambit ('MacLopez')
b6860010-d22f-4be3-b717-57dae282992b
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Bb5
Scotch, Goering gambit
f3d6d6a7-a941-470a-862c-e82c2ee92348
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. c3
Scotch, Sea-cadet mate
4965a606-c402-4c0d-ba3e-8a9c1966253a
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. c3 dxc3 5. Nxc3 d6 6. Bc4 Bg4 7. O-O Ne5 8. Nxe5 Bxd1 9. Bxf7+ Ke7 10. Nd5+
Scotch, Goering gambit
df532a65-aa83-42a4-8951-cea990e6b1ac
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. c3 dxc3 5. Nxc3 Bb4 
Scotch, Goering gambit, Bardeleben variation
dbdc80e9-fe3c-4698-968b-3f4a0f0b6885
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. c3 dxc3 5. Nxc3 Bb4 6. Bc4 Nf6 
Scotch gambit
7d9f1373-cec4-49dc-be02-8e1fb8781537
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Bc4
Scotch gambit, Anderssen (Paulsen, Suhle) counter-attack
e6ec068a-376f-467d-bad2-7142aad0a05b
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Bc4 Bc5 5. O-O d6 6. c3 Bg4 
Scotch gambit
d77ec25f-74b8-453a-902f-a404a30404f6
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Bc4 Bc5 5. Ng5
Scotch gambit, Cochrane-Shumov defence
cf4f2e90-1e1c-4eb3-a601-6def04bd355a
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Bc4 Bc5 5. Ng5 Nh6 6. Nxf7 Nxf7 7. Bxf7+ Kxf7 8. Qh5+ g6 9. Qxc5 d5 
Scotch gambit, Vitzhum attack
7e8a63e5-8403-48b7-b891-91916b63b59c
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Bc4 Bc5 5. Ng5 Nh6 6. Qh5
Scotch gambit
eca982f9-c8c5-441e-ab3a-0635e75691bd
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Bc4 Bb4+ 
Scotch gambit, Hanneken variation
80f561d4-316c-4969-a865-596cf8baa8ee
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Bc4 Bb4+ 5. c3 dxc3 6. O-O cxb2 7. Bxb2 Nf6 8. Ng5 O-O 9. e5 Nxe5 
Scotch gambit
c0151c4b-0a4d-4d87-81e3-4a6a292dcbcd
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Bc4 Bb4+ 5. c3 dxc3 6. bxc3
Scotch gambit, Cochrane variation
1c3d36f7-81ba-4528-8868-b642545484d5
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Bc4 Bb4+ 5. c3 dxc3 6. bxc3 Ba5 7. e5
Scotch gambit, Benima defence
8103ef0e-a4a4-4928-913c-df0ec0f2a07b
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Bc4 Be7 
Scotch gambit, Dubois-Reti defence
a10e87c8-1c23-407d-a844-436782897a29
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Bc4 Nf6 
******C45: Scotch game
Scotch game
3a6fd289-47b6-46dd-ad88-949a178406b3
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4
Scotch, Ghulam Kassim variation
56254a7c-f6f4-46f4-a517-9c1116a1f6f6
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Nxd4 5. Qxd4 d6 6. Bd3
Scotch, Pulling counter-attack
a8d5b1ff-0f28-4fb3-88cf-3a1947d5dd9b
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Qh4 
Scotch, Horwitz attack
ff5489d6-5a77-4a92-9294-717149a0fdf1
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Qh4 5. Nb5
Scotch, Berger variation
346d795c-4a05-4d2e-97ed-5dc2606c6433
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Qh4 5. Nb5 Bb4+ 6. Nd2 Qxe4+ 7. Be2 Qxg2 8. Bf3 Qh3 9. Nxc7+ Kd8 10. Nxa8 Nf6 11. a3
Scotch game
367835f8-5e10-4ba6-8dca-7bd388994731
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Qh4 5. Nb5 Bb4+ 6. Bd2
Scotch, Rosenthal variation
01b7d6b2-54b9-489c-b7ed-44c02648bc4f
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Qh4 5. Nb5 Bb4+ 6. Bd2 Qxe4+ 7. Be2 Kd8 8. O-O Bxd2 9. Nxd2 Qg6 
Scotch, Fraser attack
6df7eb0a-36a7-4384-875f-ce6d93e35f5f
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Qh4 5. Nf3
Scotch, Steinitz variation
d2d665cc-3ec6-44d4-b9cf-60f7753c31a8
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Qh4 5. Nc3
Scotch, Schmidt variation
4f620b64-855a-492a-87c9-edf07509cd01
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Nf6 
Scotch, Mieses variation
3d3a3a3c-9b97-4ff4-9647-e641ce9b5c51
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Nf6 5. Nxc6 bxc6 6. e5
Scotch, Tartakower variation
4b2f8b12-80a6-410e-a4d8-570baf24244a
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Nf6 5. Nxc6 bxc6 6. Nd2
Scotch game
ae18ae29-07d7-45bd-8979-fc0e164502ab
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Bc5 
Scotch, Blackburne attack
9b9c1e78-3aff-4f47-9d14-74670fbcb184
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Bc5 5. Be3 Qf6 6. c3 Nge7 7. Qd2
Scotch, Gottschall variation
e3037495-c201-48b1-9e1f-6de70ed84238
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Bc5 5. Be3 Qf6 6. c3 Nge7 7. Qd2 d5 8. Nb5 Bxe3 9. Qxe3 O-O 10. Nxc7 Rb8 11. Nxd5 Nxd5 12. exd5 Nb4 
Scotch, Paulsen attack
73ac4373-f811-4263-9b0c-746d0aaa69bc
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Bc5 5. Be3 Qf6 6. c3 Nge7 7. Bb5
Scotch, Paulsen, Gunsberg defence
13f9e322-4176-4724-978e-f1fbc184a73a
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Bc5 5. Be3 Qf6 6. c3 Nge7 7. Bb5 Nd8 
Scotch, Meitner variation
2a904908-b823-43ce-9283-d34259bbad1f
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Bc5 5. Be3 Qf6 6. c3 Nge7 7. Nc2
Scotch, Blumenfeld attack
525e75ca-1a6f-4768-8427-173dd131dcb9
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Bc5 5. Be3 Qf6 6. Nb5
Scotch, Potter variation
a8b01c26-d1fd-4c0a-9577-3f778e0a6bfa
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Bc5 5. Nb3
Scotch, Romanishin variation
be965246-16d0-4f48-ab25-f3a35011ac8b
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Bc5 5. Nb3 Bb4+ 
******C46: Three knights game
Three knights game
d2491bf6-a0a0-4d9f-a600-692d1bbcaca6
1. e4 e5 2. Nf3 Nc6 3. Nc3
Three knights, Schlechter variation
f689bf82-f3f2-403e-ab0b-eb3ffb01b556
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bb4 4. Nd5 Nf6 
Three knights, Winawer defence (Gothic defence)
9f425983-9e2e-4784-ad7d-10eb3e9f7d50
1. e4 e5 2. Nf3 Nc6 3. Nc3 f5 
Three knights, Steinitz variation
c72844c1-67a6-4c26-acd6-4945b4b10ca6
1. e4 e5 2. Nf3 Nc6 3. Nc3 g6 
Three knights, Steinitz, Rosenthal variation
7496a6f2-a8ae-422f-ad34-7ea2338bceef
1. e4 e5 2. Nf3 Nc6 3. Nc3 g6 4. d4 exd4 5. Nd5
Four knights game
738b357f-4c02-4b87-95d8-e0539abb70bf
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 
Four knights, Schultze-Mueller gambit
2b804a26-ce18-4b6d-9b28-9c08a0c0e618
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Nxe5
Four knights, Italian variation
cd00ba49-b337-42d1-b6dd-00fa315def4a
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bc4
Four knights, Gunsberg variation
c85ad14a-38ac-4244-8bda-70c8763ae912
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. a3
******C47: Four knights, Scotch variation
Four knights, Scotch variation
d0689406-f118-48eb-9f9a-bf66bf7c5210
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. d4
Four knights, Scotch, Krause variation
d36450ac-e0f4-420f-9f6a-4128f5ab4e76
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. d4 Bb4 5. Nxe5
Four knights, Scotch, 4...exd4
5a8c39ca-3357-481e-a910-ff53db1dd754
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. d4 exd4 
Four knights, Belgrade gambit
e084ea2a-ec5e-433c-9e50-68a071821478
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. d4 exd4 5. Nd5
******C48: Four knights, Spanish variation
Four knights, Spanish variation
d144d0e0-1109-4d20-9f70-083e33615d6e
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5
Four knights, Ranken variation
8a2908f9-afe2-4422-b3e1-7b02c863920c
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 a6 5. Bxc6
Four knights, Spielmann variation
a52fd8bb-5479-4e2f-9242-1f24b7ab9444
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 a6 5. Bxc6 dxc6 6. Nxe5 Nxe4 7. Nxe4 Qd4 8. O-O Qxe5 9. Re1 Be6 10. d4 Qd5 
Four knights, Spanish, classical defence
09b7f6b4-e399-444f-867f-fe5423c898e3
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bc5 
Four knights, Bardeleben variation
109fef90-d1c0-454b-9798-fa5dacda1b76
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bc5 5. O-O O-O 6. Nxe5 Nxe5 7. d4 Bd6 8. f4 Nc6 9. e5 Bb4 
Four knights, Marshall variation
a3c2ee68-1ee0-4bfe-8abb-092e928b4c93
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bc5 5. O-O O-O 6. Nxe5 Nd4 
Four knights, Rubinstein counter-gambit
b20ed582-2753-4275-ba7b-a19a46549d0a
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Nd4 
Four knights, Rubinstein counter-gambit, Bogolyubov variation
b27e0dd9-a334-4051-a2f3-f13a7f7a66d2
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Nd4 5. Nxe5 Qe7 6. f4
Four knights, Rubinstein counter-gambit, 5.Be2
919dc42f-94c8-4de2-842c-0e079d71802a
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Nd4 5. Be2
Four knights, Rubinstein counter-gambit Maroczy variation
80bad24d-6694-4874-a0ab-7575950e1bfc
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Nd4 5. Be2 Nxf3+ 6. Bxf3 Bc5 7. O-O O-O 8. d3 d6 9. Na4 Bb6 
Four knights, Rubinstein counter-gambit, exchange variation
38bd3b14-4707-4b27-a390-8f90293ee31a
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Nd4 5. Nxd4
Four knights, Rubinstein counter-gambit, Henneberger variation
a4698a75-a410-4545-91a5-60df201444dc
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Nd4 5. O-O
******C49: Four knights, double Ruy Lopez
Four knights, double Ruy Lopez
87170120-3c5e-4682-a28a-237ca3efb235
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 
Four knights, Gunsberg counter-attack
2675e35f-a2fa-4a59-8f2b-3d584fce1110
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. Nd5 Nxd5 7. exd5 e4 
Four knights, double Ruy Lopez
b8e76218-ce3e-4968-911d-a3a1ef4092de
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. d3
Four knights, Alatortsev variation
25369ee7-4624-4ba0-810a-c5c943b59183
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. d3 Qe7 7. Ne2 d5 
Four knights
fb29f17a-c3dc-4137-ab8b-30be983ac79d
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. d3 Bxc3 
Four knights, Janowski variation
28daac28-823c-469f-8160-1f1a7eb8b788
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. d3 Bxc3 7. bxc3 d6 8. Re1
Four knights, Svenonius variation
40051496-e362-4402-ba38-64db00dd5502
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. d3 Bxc3 7. bxc3 d5 
Four knights, symmetrical variation
f0a4b740-d161-4e1b-9d9e-13835c3c9cca
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. d3 d6 
Four knights, symmetrical, Metger unpin
5281ffd4-f5ad-44ed-aff0-36910ac8c26b
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. d3 d6 7. Bg5 Bxc3 8. bxc3 Qe7 
Four knights, symmetrical, Capablanca variation
011e6e36-4d07-40a2-b8dc-db2594323d5e
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. d3 d6 7. Bg5 Bxc3 8. bxc3 Qe7 9. Re1 Nd8 10. d4 Bg4 
Four knights, symmetrical, Pillsbury variation
88843515-78e6-48b8-a14a-c9f1d68d2e71
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. d3 d6 7. Bg5 Ne7 
Four knights, symmetrical, Blake variation
82de1437-ded1-4953-ba5f-0676720cba28
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. d3 d6 7. Bg5 Ne7 8. Nh4 c6 9. Bc4 d5 10. Bb3 Qd6 
Four knights, symmetrical, Tarrasch variation
a32bbee1-c1ab-4089-b53e-2fb2e9714655
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. d3 d6 7. Bg5 Be6 
Four knights, symmetrical, Maroczy system
66b3040a-8917-4636-be23-07f12fcd8ee3
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. d3 d6 7. Ne2
Four knights, Nimzovich (Paulsen) variation
bc9cd9d5-4ed9-4ce2-9167-3dd357e573e6
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. Bxc6
******C50: King's pawn game
King's pawn game
11e2cf62-d45d-41c2-a7c1-e5a6e3306d2a
1. e4 e5 2. Nf3 Nc6 3. Bc4
Blackburne shilling gambit
78c9c9d1-9cce-4437-bfec-052d4834296a
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nd4 4. Nxe5 Qg5 5. Nxf7 Qxg2 6. Rf1 Qxe4+ 7. Be2 Nf3+ 
Rousseau gambit
202e2323-a712-48ae-adb1-4a1a18f2128b
1. e4 e5 2. Nf3 Nc6 3. Bc4 f5 
Hungarian defence
e65b0808-0a95-4b28-822c-f78789e71f11
1. e4 e5 2. Nf3 Nc6 3. Bc4 Be7 
Hungarian defence, Tartakower variation
1f6930f6-0d45-4f3d-aff0-7bb0a69ea43d
1. e4 e5 2. Nf3 Nc6 3. Bc4 Be7 4. d4 exd4 5. c3 Nf6 6. e5 Ne4 
Giuoco Piano
0fe2c0d8-d674-4702-946e-7dda85f9560c
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 
Giuoco Piano, four knights variation
20bc047a-a770-480a-98d2-13158284dbed
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. Nc3 Nf6 
Giuoco Piano, Jerome gambit
aa07da9c-b338-4886-968b-41f6bff14713
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. Bxf7+
Giuoco Pianissimo
5a86a5ee-0365-41a2-88e6-c1e3530f6540
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. d3
Giuoco Pianissimo, Dubois variation
bce2c2b0-6c80-4b06-8370-8eb848095099
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. d3 f5 5. Ng5 f4 
Giuoco Pianissimo
0b64b95e-1b52-4aa6-a0a7-37bdba2a1445
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. d3 Nf6 
Giuoco Pianissimo, Italian four knights variation
fc2d8ee0-4a26-47b5-bbf0-0aee8f70e913
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. d3 Nf6 5. Nc3
Giuoco Pianissimo, Canal variation
a911ca70-b205-4778-8340-70c497446194
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. d3 Nf6 5. Nc3 d6 6. Bg5
******C51: Evans gambit declined
Evans gambit declined
44f8372e-a614-468d-beb4-eb8736b5d28e
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4
Evans gambit declined, Lange variation
d1862ff9-44ec-4042-8f02-3602666b0ca9
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bb6 5. b5 Na5 6. Nxe5 Nh6 
Evans gambit declined, Pavlov variation
03239656-161f-4bdd-9e34-ff4ec9e9f28e
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bb6 5. b5 Na5 6. Nxe5 Nh6 7. d4 d6 8. Bxh6 dxe5 9. Bxg7 Rg8 10. Bxf7+ Kxf7 11. Bxe5 Qg5 12. Nd2
Evans gambit declined, Hirschbach variation
a05275ae-a986-4011-9ef4-ed9b76432f3c
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bb6 5. b5 Na5 6. Nxe5 Qg5 
Evans gambit declined, Vasquez variation
f7c2f3f1-cb23-4189-a9e1-89c6feaa2e99
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bb6 5. b5 Na5 6. Nxe5 Qg5 7. Bxf7+ Ke7 8. Qh5
Evans gambit declined, Hicken variation
213667e6-2571-4958-aff3-0dca9151ab2f
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bb6 5. b5 Na5 6. Nxe5 Qg5 7. Qf3 Qxe5 8. Qxf7+ Kd8 9. Bb2
Evans gambit declined, 5.a4
dd8f51f0-be5d-443e-9fb3-17a7643e0520
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bb6 5. a4
Evans gambit declined, Showalter variation
0a7a8536-dd2b-481b-a0e1-0e0433691084
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bb6 5. a4 a6 6. Nc3
Evans gambit declined, Cordel variation
5edd16d6-8abb-4abf-b899-635a50ca4346
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bb6 5. Bb2
Evans counter-gambit
4591323e-f320-4745-8e7d-ff61673fda1e
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 d5 
Evans gambit
bdfe070d-4cdb-42aa-90db-92af7d856157
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 
Evans gambit, normal variation
511ff5f5-f389-4c90-8c0a-0566c73144d2
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Bc5 6. d4 exd4 7. O-O d6 8. cxd4 Bb6 
Evans gambit, Ulvestad variation
4213b795-597e-4ccb-a373-fdb3743770be
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Bc5 6. d4 exd4 7. O-O d6 8. cxd4 Bb6 9. d5 Na5 10. Bb2
Evans gambit, Paulsen variation
70b68809-e5ea-45ce-ad14-a4366ad01d04
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Bc5 6. d4 exd4 7. O-O d6 8. cxd4 Bb6 9. d5 Na5 10. Bb2 Ne7 
Evans gambit, Morphy attack
168b5e65-2f86-426e-bd2b-c257b9959f2f
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Bc5 6. d4 exd4 7. O-O d6 8. cxd4 Bb6 9. Nc3
Evans gambit, Goering attack
b63bdc05-ca72-4546-9469-470942c99b23
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Bc5 6. d4 exd4 7. O-O d6 8. cxd4 Bb6 9. Nc3 Na5 10. Bg5
Evans gambit, Steinitz variation
b84d46a0-2208-44b6-b88b-21609c8b5a59
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Bc5 6. d4 exd4 7. O-O d6 8. cxd4 Bb6 9. Nc3 Na5 10. Bg5 f6 11. Be3
Evans gambit
9a9f0c37-08ae-4eb0-a340-8be4e835d86d
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Bc5 6. d4 exd4 7. O-O d6 8. cxd4 Bb6 9. Nc3 Bg4 
Evans gambit, Fraser attack
ba1fbde8-4e7b-4283-83f2-20d40a1b2b81
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Bc5 6. d4 exd4 7. O-O d6 8. cxd4 Bb6 9. Nc3 Bg4 10. Qa4
Evans gambit, Fraser-Mortimer attack
39cee321-af1b-4d17-ab9b-f2d441b57b86
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Bc5 6. d4 exd4 7. O-O d6 8. cxd4 Bb6 9. Nc3 Bg4 10. Qa4 Bd7 11. Qb3 Na5 12. Bxf7+ Kf8 13. Qc2
Evans gambit, Stone-Ware variation
f389ff20-27fa-4808-823b-73f20837737e
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Bd6 
Evans gambit, Mayet defence
8377d828-d052-4acb-915e-4c8822a217be
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Bf8 
Evans gambit, 5...Be7
0fea0d6b-9d9e-4059-8376-9dd9cd1d8242
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Be7 
Evans gambit, Cordel variation
f8bb7ede-efd3-4457-87ce-d923827449e7
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Be7 6. d4 Na5 
******C52: Evans gambit
Evans gambit
d69c4888-7516-4490-8b08-0d1cf6116baf
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 
Evans gambit, compromised defence
8f109d21-731a-4668-806e-11875bfa05e4
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. d4 exd4 7. O-O dxc3 
Evans gambit, compromised defence, Paulsen variation
2553af01-a1d6-4627-af5b-1e6ccba8ec2c
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. d4 exd4 7. O-O dxc3 8. Qb3 Qf6 9. e5 Qg6 10. Nxc3 Nge7 11. Ba3
Evans gambit, compromised defence, Potter variation
9737c24e-6e4d-4124-81a1-137cb9b347f3
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. d4 exd4 7. O-O dxc3 8. Qb3 Qf6 9. e5 Qg6 10. Nxc3 Nge7 11. Rd1
Evans gambit, Leonhardt variation
b810d419-ce56-40c0-a877-58164fca8882
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. d4 b5 
Evans gambit
6776fddf-b597-4829-8c77-3041948916c0
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. d4 d6 
Evans gambit, Tartakower attack
bf5759fd-6dbe-4eb7-8672-457c25aa5247
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. d4 d6 7. Qb3
Evans gambit, Levenfish variation
17cb51fe-1438-4584-8910-e8eb5bd75af7
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. d4 d6 7. Qb3 Qd7 8. dxe5 dxe5 9. O-O Bb6 10. Ba3 Na5 11. Nxe5
Evans gambit, Sokolsky variation
03954c0d-95d4-4d41-b106-be3ea8fe5d18
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. d4 d6 7. Bg5
Evans gambit
660ca55d-11fb-442e-a2f9-8a9f4a7676ae
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. O-O
Evans gambit, Richardson attack
a18092a5-1916-4572-b7d5-adc6662d8e0c
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. O-O Nf6 7. d4 O-O 8. Nxe5
Evans gambit
7f7d5c10-d714-436d-9901-286ddf59340f
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. O-O d6 
Evans gambit, Waller attack
3e7d373f-604b-48a2-9f2d-432f951a20eb
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. O-O d6 7. d4 exd4 8. Qb3
Evans gambit, Lasker defence
ae4ccce4-ff87-4e35-b532-cebf0fa92861
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. O-O d6 7. d4 Bb6 
Evans gambit, Sanders-Alapin variation
849dfb06-8e01-4657-ad1d-2a59445eb096
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. O-O d6 7. d4 Bd7 
Evans gambit, Alapin-Steinitz variation
1d0ec380-8584-466a-b246-1df9fc6be326
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. O-O d6 7. d4 Bg4 
******C53: Giuoco Piano
Giuoco Piano
9a2f3b02-eb0b-4583-aa38-71f3445d3fcb
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3
Giuoco Piano, LaBourdonnais variation
31d4a6cc-149f-4aa9-8cd8-47a9c98f24e5
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 d6 5. d4 exd4 6. cxd4 Bb6 
Giuoco Piano, close variation
a449fc24-c0b8-4d1a-9300-a98a96528190
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Qe7 
Giuoco Piano, centre-holding variation
f4ed5f1f-0a0b-4922-94b5-907d795f556f
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Qe7 5. d4 Bb6 
Giuoco Piano, Tarrasch variation
6abf844b-c394-46e8-b4e9-d5a91591e187
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Qe7 5. d4 Bb6 6. O-O Nf6 7. a4 a6 8. Re1 d6 9. h3
Giuoco Piano, Mestel variation
76f7afcc-5942-43b1-bef8-02cd34fdc561
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Qe7 5. d4 Bb6 6. Bg5
Giuoco Piano, Eisinger variation
58e24bb3-ad43-4d91-88c3-1cab2a79b477
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Qe7 5. d4 Bb6 6. d5 Nb8 7. d6
Giuoco Piano
1625cf4c-0d3e-43e3-93ce-840ca41a22b1
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 
Giuoco Piano, Bird's attack
fc4e1c86-414a-4d85-aad6-ab0793f287f6
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. b4
Giuoco Piano
678a3d46-ee6a-4e0b-a00b-590e9b31ff98
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4
Giuoco Piano, Ghulam Kassim variation
e021f2d4-fef0-41fa-81ac-3b5b64bbaf2c
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. e5 Ne4 7. Bd5 Nxf2 8. Kxf2 dxc3+ 9. Kg3
Giuoco Piano
4703419b-90c8-4295-8680-c9c2fe160450
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. e5 d5 
Giuoco Piano, Anderssen variation
d93f5ecd-bb30-406a-9d6b-339255097bd6
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. e5 d5 7. Bb5 Ne4 8. cxd4 Bb4+ 
******C54: Giuoco Piano
Giuoco Piano
5df4279f-3024-4035-837c-75f11aba36cc
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. cxd4
Giuoco Piano, Krause variation
db8b9c37-b581-4d3a-a801-8466fc32839f
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. cxd4 Bb4+ 7. Bd2 Nxe4 8. Bxb4 Nxb4 9. Bxf7+ Kxf7 10. Qb3+ d5 11. Ne5+ Kf6 12. f3
Giuoco Piano, Cracow variation
9d17c08d-e904-457b-9007-fc11fb41f1b0
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. cxd4 Bb4+ 7. Kf1
Giuoco Piano, Greco's attack
e3a4eb62-3e0b-4ed5-8050-02d126f66929
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. cxd4 Bb4+ 7. Nc3
Giuoco Piano, Greco variation
cd866245-2ba2-433b-91f9-5dc49736c5a4
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. cxd4 Bb4+ 7. Nc3 Nxe4 8. O-O Nxc3 
Giuoco Piano, Bernstein variation
f870358b-3c38-465d-9514-f06abf8bb3b2
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. cxd4 Bb4+ 7. Nc3 Nxe4 8. O-O Nxc3 9. bxc3 Bxc3 10. Qb3 d5 
Giuoco Piano, Aitken variation
61ef837f-9612-4bd2-84d0-6c2a3b931229
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. cxd4 Bb4+ 7. Nc3 Nxe4 8. O-O Nxc3 9. bxc3 Bxc3 10. Ba3
Giuoco Piano
59caa680-9a66-44a0-ba3b-ca4c4c132e2b
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. cxd4 Bb4+ 7. Nc3 Nxe4 8. O-O Bxc3 
Giuoco Piano, Steinitz variation
ee267d7b-e657-418c-9b67-b0cb205e63fc
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. cxd4 Bb4+ 7. Nc3 Nxe4 8. O-O Bxc3 9. bxc3 d5 10. Ba3
Giuoco Piano, Moeller (Therkatz) attack
12ab31c5-0863-4f4a-ba06-d0d928fccd87
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. cxd4 Bb4+ 7. Nc3 Nxe4 8. O-O Bxc3 9. d5
Giuoco Piano, Therkatz-Herzog variation
85ab71fc-8dab-411f-89c7-6e92a5acdc77
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. cxd4 Bb4+ 7. Nc3 Nxe4 8. O-O Bxc3 9. d5 Bf6 10. Re1 Ne7 11. Rxe4 d6 12. Bg5 Bxg5 13. Nxg5 O-O 14. Nxh7
Giuoco Piano, Moeller, bayonet attack
22283fcd-c055-4d5c-8e13-fb68d64fe8eb
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. cxd4 Bb4+ 7. Nc3 Nxe4 8. O-O Bxc3 9. d5 Bf6 10. Re1 Ne7 11. Rxe4 d6 12. g4
******C55: Two knights defence
Two knights defence
4943d8d7-6d41-4783-8e2d-2ed95269fe93
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 
Giuoco piano, Rosentreter variation
c277f41a-f74f-41e1-b0af-553cc691ff78
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. O-O Bc5 5. d4 Bxd4 6. Nxd4 Nxd4 7. Bg5 h6 8. Bh4 g5 9. f4
Giuoco piano
fa455c5c-f16f-4c1b-b4d8-ac4014236988
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. O-O Bc5 5. d4 Bxd4 6. Nxd4 Nxd4 7. Bg5 d6 
Giuoco piano, Holzhausen attack
35b578f8-8b74-4b2d-bc19-ca578df19130
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. O-O Bc5 5. d4 Bxd4 6. Nxd4 Nxd4 7. Bg5 d6 8. f4 Qe7 9. fxe5 dxe5 10. Nc3
Two knights defence (Modern bishop's opening)
b7ebb7e7-5c3a-47bc-8f26-6e3f1166a443
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d3
Two knights defence
353ab8f0-8604-4cda-aede-d4e2bc611434
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4
Two knights defence, Keidanz variation
0d6f8aff-3cfc-4ba7-99e9-d0a1006cf9cf
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. e5 d5 6. Bb5 Ne4 7. Nxd4 Bc5 8. Nxc6 Bxf2+ 9. Kf1 Qh4 
Two knights defence, Perreux variation
a5b34724-43a8-4286-b591-46376b89d606
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. Ng5
Two knights defence
cc1c81c9-50c2-493e-963d-bdbb2ca8a689
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. O-O
two knights, Max Lange attack
15307b69-151b-40a5-ad64-99244e440f84
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. O-O Bc5 6. e5
two knights, Max Lange attack, Berger variation
10314ddb-c633-4ca1-aa70-5103531df349
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. O-O Bc5 6. e5 d5 7. exf6 dxc4 8. Re1+ Be6 9. Ng5 Qd5 10. Nc3 Qf5 11. g4 Qg6 12. Nce4 Bb6 13. f4 O-O-O 
two knights, Max Lange attack, Marshall variation
3eda01b5-947e-4a60-baf0-47df2c49d6c9
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. O-O Bc5 6. e5 d5 7. exf6 dxc4 8. Re1+ Be6 9. Ng5 Qd5 10. Nc3 Qf5 11. Nce4
two knights, Max Lange attack, Rubinstein variation
61c1c52b-c220-4dbc-9806-dce36ed9d236
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. O-O Bc5 6. e5 d5 7. exf6 dxc4 8. Re1+ Be6 9. Ng5 Qd5 10. Nc3 Qf5 11. Nce4 Bf8 
two knights, Max Lange attack, Loman defence
7943d9cb-0cdb-4ff0-9891-ad9c449bd6bc
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. O-O Bc5 6. e5 d5 7. exf6 dxc4 8. Re1+ Be6 9. Ng5 g6 
two knights, Max Lange attack, Schlechter variation
1f23bc8e-56aa-4d13-8775-4e9ffdc6f394
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. O-O Bc5 6. e5 d5 7. exf6 dxc4 8. Re1+ Be6 9. fxg7
two knights, Max Lange attack, Steinitz variation
703b991e-a722-4ae6-9e16-6ef57a9d631b
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. O-O Bc5 6. e5 Ng4 
two knights, Max Lange attack, Krause variation
704c0d93-ddaa-4b75-a673-0b3dbefc3bda
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. O-O Bc5 6. e5 Ng4 7. c3
******C56: Two knights defence
Two knights defence
2590a2ba-ceeb-439d-b6bf-2fcc693bc30e
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. O-O Nxe4 
two knights defence, Yurdansky attack
56847640-4f5d-45c7-b84a-464227d0ba7c
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. O-O Nxe4 6. Re1 d5 7. Bxd5 Qxd5 8. Nc3 Qa5 9. Nxe4 Be6 10. Bg5 h6 11. Bh4 g5 12. Nf6+ Ke7 13. b4
two knights defence, Canal variation
b5796173-b176-461e-bf0e-b746243879f9
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. O-O Nxe4 6. Re1 d5 7. Nc3
******C57: Two knights defence
Two knights defence
7d1745aa-8154-4321-aee4-285eb3a15430
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5
two knights defence, Wilkes Barre (Traxler) variation
5402eb92-9ddd-438b-94c9-a9c5336c44d4
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 Bc5 
two knights defence, Ulvestad variation
e94c0182-263b-4f24-a66d-13c824b49a70
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 b5 
two knights defence, Fritz variation
df1cd755-03fb-4a41-b9bf-62809cc6c95b
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Nd4 
two knights defence, Fritz, Gruber variation
220fe3ed-2311-4fd9-b408-158edbc2b422
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Nd4 6. c3 b5 7. Bf1 Nxd5 8. Ne4
two knights defence, Lolli attack
8e592c50-82f0-414d-b714-b4fe897620cb
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Nxd5 6. d4
two knights defence, Pincus variation
d9940ce6-bf0a-4a88-aa8a-03876588e160
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Nxd5 6. d4 Bb4+ 
two knights defence, Fegatello attack
2353db86-b6a8-4154-8acb-d64e63a87678
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Nxd5 6. Nxf7
two knights defence, Fegatello attack, Leonhardt variation
390e4ad3-07a7-464a-8101-d730bb4b860b
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Nxd5 6. Nxf7 Kxf7 7. Qf3+ Ke6 8. Nc3 Ncb4 9. Qe4 c6 10. a3 Na6 11. d4 Nac7 
two knights defence, Fegatello attack, Polerio defence
8f6afc55-04b3-4d3c-a3db-c830ef510dda
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Nxd5 6. Nxf7 Kxf7 7. Qf3+ Ke6 8. Nc3 Nce7 
******C58: two knights defence
two knights defence
f3dc46fa-b03a-480f-9382-0987e499b12d
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 
two knights defence, Kieseritsky variation
5e2d09dc-6367-4ade-b7dd-baf1588e6b4d
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 6. d3
two knights defence, Yankovich variation
78d316b0-1f8c-4071-a7e4-84c961df4763
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 6. d3 h6 7. Nf3 e4 8. Qe2 Nxc4 9. dxc4 Bc5 10. Nfd2
two knights defence, Maroczy variation
3bd10712-6d93-49dc-9129-c862f2eca453
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 6. d3 h6 7. Nf3 e4 8. Qe2 Nxc4 9. dxc4 Be7 
Two knights defence
22b29549-c122-4607-a7c2-071cc674e132
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 6. Bb5+
two knights defence, Bogolyubov variation
acd65e44-70f4-49d9-a403-eeb12c2691a2
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 6. Bb5+ c6 7. dxc6 bxc6 8. Qf3
two knights defence, Paoli variation
2d297d56-37a5-4ec5-8fad-2b5f79340e9c
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 6. Bb5+ c6 7. dxc6 bxc6 8. Qf3 Qc7 9. Bd3
two knights defence, Colman variation
88136004-2ca5-4489-9d1c-c468dd955a41
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 6. Bb5+ c6 7. dxc6 bxc6 8. Qf3 Rb8 
two knights defence, Blackburne variation
790d000e-6597-4b3a-b8b5-f1a66b567036
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 6. Bb5+ c6 7. dxc6 bxc6 8. Qf3 cxb5 
Two knights defence
65f2c09e-6c43-4004-998c-484ce807c459
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 6. Bb5+ c6 7. dxc6 bxc6 8. Be2
******C59: Two knights defence
Two knights defence
ddfc4e85-55bb-4cb0-a94b-c29f1e19e089
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 6. Bb5+ c6 7. dxc6 bxc6 8. Be2 h6 
two knights defence, Knorre variation
3ee1a14f-5d89-488e-9d0b-2ee6da361261
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 6. Bb5+ c6 7. dxc6 bxc6 8. Be2 h6 9. Nf3 e4 10. Ne5 Bd6 11. d4 Qc7 12. Bd2
two knights defence, Goering variation
6f4de025-a01c-43c7-81d1-cd688192e1fe
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 6. Bb5+ c6 7. dxc6 bxc6 8. Be2 h6 9. Nf3 e4 10. Ne5 Qc7 
two knights defence, Steinitz variation
3a99de09-71ef-41d1-ba1d-1d7aab2cf790
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 6. Bb5+ c6 7. dxc6 bxc6 8. Be2 h6 9. Nh3
******C60: Ruy Lopez (Spanish opening)
Ruy Lopez (Spanish opening)
56d66cf8-80cc-45be-98d7-a641e736e7ab
1. e4 e5 2. Nf3 Nc6 3. Bb5
Ruy Lopez, Nuernberg variation
07cd8447-6d71-4491-8493-c09077d5dcb6
1. e4 e5 2. Nf3 Nc6 3. Bb5 f6 
Ruy Lopez, Pollock defence
49d84591-2b59-4b09-a4e9-c2023bd3d3b7
1. e4 e5 2. Nf3 Nc6 3. Bb5 Na5 
Ruy Lopez, Lucena defence
3d705a50-37f7-4cc5-a43f-63c6118a573b
1. e4 e5 2. Nf3 Nc6 3. Bb5 Be7 
Ruy Lopez, Vinogradov variation
502b6fbb-8703-484e-9a9e-b75003becc43
1. e4 e5 2. Nf3 Nc6 3. Bb5 Qe7 
Ruy Lopez, Brentano defence
19889dcb-8561-41c7-a632-692a35bbc864
1. e4 e5 2. Nf3 Nc6 3. Bb5 g5 
Ruy Lopez, fianchetto (Smyslov/Barnes) defence
c1c9f249-00bd-421d-8e9b-ab9c030d9f0e
1. e4 e5 2. Nf3 Nc6 3. Bb5 g6 
Ruy Lopez, Cozio defence
aa50ace0-16ba-4994-9c79-8b73189919fd
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nge7 
Ruy Lopez, Cozio defence, Paulsen variation
d92d6e4d-d9fa-4db5-a617-9138d0287315
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nge7 4. Nc3 g6 
******C61: Ruy Lopez, Bird's defence
Ruy Lopez, Bird's defence
d91c21d1-5379-434a-b0e4-331d163c9888
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nd4 
Ruy Lopez, Bird's defence, Paulsen variation
c2079c3f-5e70-4229-a5b0-d8b0b1857096
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nd4 4. Nxd4 exd4 5. O-O Ne7 
******C62: Ruy Lopez, old Steinitz defence
Ruy Lopez, old Steinitz defence
c1bbb169-4524-4e86-af55-0b5f9b9b71db
1. e4 e5 2. Nf3 Nc6 3. Bb5 d6 
Ruy Lopez, old Steinitz defence, Nimzovich attack
4ce8009e-0843-4d93-9813-3aae45ae2050
1. e4 e5 2. Nf3 Nc6 3. Bb5 d6 4. d4 Bd7 5. Nc3 Nf6 6. Bxc6
Ruy Lopez, old Steinitz defence, semi-Duras variation
74b57ea4-c6ac-4a20-b9db-f51aae5dc3ab
1. e4 e5 2. Nf3 Nc6 3. Bb5 d6 4. d4 Bd7 5. c4
******C63: Ruy Lopez, Schliemann defence
Ruy Lopez, Schliemann defence
9a629e42-4241-4d75-b029-739d5a796d4c
1. e4 e5 2. Nf3 Nc6 3. Bb5 f5 
Ruy Lopez, Schliemann defence, Berger variation
08997b03-5e0d-42eb-9c48-067563b4c3ad
1. e4 e5 2. Nf3 Nc6 3. Bb5 f5 4. Nc3
******C64: Ruy Lopez, classical (Cordel) defence
Ruy Lopez, classical (Cordel) defence
a261e4d6-1d2c-4af9-8fff-b22a0a7e1231
1. e4 e5 2. Nf3 Nc6 3. Bb5 Bc5 
Ruy Lopez, classical defence, Zaitsev variation
6cf1571d-bf5d-4fd4-bb88-0fd5f91588d7
1. e4 e5 2. Nf3 Nc6 3. Bb5 Bc5 4. O-O Nd4 5. b4
Ruy Lopez, classical defence, 4.c3
e62bc7cd-9ce5-4d59-9cf2-5d4ba9e71ccf
1. e4 e5 2. Nf3 Nc6 3. Bb5 Bc5 4. c3
Ruy Lopez, classical defence, Benelux variation
17117c85-5301-4f85-a067-78a1b4056de4
1. e4 e5 2. Nf3 Nc6 3. Bb5 Bc5 4. c3 Nf6 5. O-O O-O 6. d4 Bb6 
Ruy Lopez, classical defence, Charousek variation
1f082f2e-21e0-4dae-b511-16794da90b01
1. e4 e5 2. Nf3 Nc6 3. Bb5 Bc5 4. c3 Bb6 
Ruy Lopez, classical defence, Boden variation
dbd08d76-e33c-4a44-a846-c4a534d5b5f8
1. e4 e5 2. Nf3 Nc6 3. Bb5 Bc5 4. c3 Qe7 
Ruy Lopez, Cordel gambit
7ce57c78-ab9f-4500-a78d-0ec72dd0c7c0
1. e4 e5 2. Nf3 Nc6 3. Bb5 Bc5 4. c3 f5 
******C65: Ruy Lopez, Berlin defence
Ruy Lopez, Berlin defence
c2174e60-d4aa-46a7-9351-ce1bc0db749d
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 
Ruy Lopez, Berlin defence, Nyholm attack
0f373933-4b6b-4b93-86d7-7ec4bc8ba68c
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. d4 exd4 5. O-O
Ruy Lopez, Berlin defence, Mortimer variation
e54eb94a-2eb5-46b5-8125-8c08ef65ac87
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. d3 Ne7 
Ruy Lopez, Berlin defence, Mortimer trap
123937af-a78b-45fe-818e-187ddc9f4c65
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. d3 Ne7 5. Nxe5 c6 
Ruy Lopez, Berlin defence, Anderssen variation
6b6b5bfe-fb1f-4890-86aa-748ba7fb764b
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. d3 d6 5. Bxc6+
Ruy Lopez, Berlin defence, Duras variation
696f5423-3a49-4557-965d-78a26bbc99d9
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. d3 d6 5. c4
Ruy Lopez, Berlin defence, Kaufmann variation
cca4eff8-23c1-4ea9-af2d-dabe4f944d66
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. d3 Bc5 5. Be3
Ruy Lopez, Berlin defence, 4.O-O
9615df5a-2923-46f8-abf5-af19ae87d3b2
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O
Ruy Lopez, Berlin defence, Beverwijk variation
44535809-c663-428d-b4f3-52024dc65ba0
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Bc5 
******C66: Ruy Lopez, Berlin defence, 4.O-O, d6
Ruy Lopez, Berlin defence, 4.O-O, d6
f7d7545c-41f3-433f-9fb7-53f64a8441ed
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O d6 
Ruy Lopez, Berlin defence, hedgehog variation
42a0370c-b395-4f64-8da2-5672e8191989
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O d6 5. d4 Bd7 6. Nc3 Be7 
Ruy Lopez, Berlin defence, Tarrasch trap
72dd026a-8c6b-497a-9b61-77b5d0c82f03
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O d6 5. d4 Bd7 6. Nc3 Be7 7. Re1 O-O 
Ruy Lopez, closed Berlin defence, Bernstein variation
cc72fbce-0d8e-4bdd-89d2-d894d835d0e8
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O d6 5. d4 Bd7 6. Nc3 Be7 7. Bg5
Ruy Lopez, closed Berlin defence, Showalter variation
0a2e385e-aecb-41fd-b283-0927478364e1
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O d6 5. d4 Bd7 6. Nc3 Be7 7. Bxc6
Ruy Lopez, closed Berlin defence, Wolf variation
5bad1091-930e-4908-a361-0eec0a8f0a77
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O d6 5. d4 Bd7 6. Nc3 exd4 
Ruy Lopez, closed Berlin defence, Chigorin variation
432e5c45-5496-498f-bb87-c0a5b01bb6d2
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O d6 5. d4 Nd7 
******C67: Ruy Lopez, Berlin defence, open variation
Ruy Lopez, Berlin defence, open variation
2755f759-630d-4a0b-9ca2-84ca38b48dad
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Nxe4 
Ruy Lopez, open Berlin defence, l'Hermet variation
fe72ce9a-643c-404d-b402-e8f4d1825bd4
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Nxe4 5. d4 Nd6 6. dxe5
Ruy Lopez, open Berlin defence, Showalter variation
d7d4734e-8291-4657-8996-1f45c15ed899
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Nxe4 5. d4 Nd6 6. Ba4
Ruy Lopez, open Berlin defence, 5...Be7
876708fa-d863-40c9-996c-a1c4785e66f0
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Nxe4 5. d4 Be7 
Ruy Lopez, Berlin defence, Rio de Janeiro variation
db9a6ab4-9f8d-44e9-81e6-d6c8d149a88e
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Nxe4 5. d4 Be7 6. Qe2 Nd6 7. Bxc6 bxc6 8. dxe5 Nb7 9. Nc3 O-O 10. Re1 Nc5 11. Nd4 Ne6 12. Be3 Nxd4 13. Bxd4 c5 
Ruy Lopez, Berlin defence, Zukertort variation
3b95192f-f1be-4150-ba51-837496adf785
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Nxe4 5. d4 Be7 6. Qe2 Nd6 7. Bxc6 bxc6 8. dxe5 Nb7 9. c4
Ruy Lopez, Berlin defence, Pillsbury variation
81f54b5b-cf4e-46ea-9a81-a6cfbd51132a
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Nxe4 5. d4 Be7 6. Qe2 Nd6 7. Bxc6 bxc6 8. dxe5 Nb7 9. b3
Ruy Lopez, Berlin defence, Winawer attack
7371a0fc-84a9-4059-9fd4-cdd09e798588
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Nxe4 5. d4 Be7 6. Qe2 Nd6 7. Bxc6 bxc6 8. dxe5 Nb7 9. Nd4
Ruy Lopez, Berlin defence, Cordel variation
7b23fa6a-fa1f-47c6-9118-f329ce281ea2
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Nxe4 5. d4 Be7 6. Qe2 Nd6 7. Bxc6 bxc6 8. dxe5 Nf5 
Ruy Lopez, Berlin defence, Trifunovic variation
7029f1d4-0a88-483b-902d-6764933fc174
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Nxe4 5. d4 Be7 6. Qe2 d5 
Ruy Lopez, Berlin defence, Minckwitz variation
db936d75-1cc0-4dcf-adfc-9c0fb3f06470
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Nxe4 5. d4 Be7 6. dxe5
Ruy Lopez, Berlin defence, Rosenthal variation
84c92e2c-219f-41ed-8ec9-9b823a4068c8
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Nxe4 5. d4 a6 
******C68: Ruy Lopez, exchange variation
Ruy Lopez, exchange variation
9ab9242e-52cd-4040-bb0a-42ebbdaa9086
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Bxc6
Ruy Lopez, exchange, Alekhine variation
0abea1da-9e7a-4d51-9926-82660290c400
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Bxc6 dxc6 5. d4 exd4 6. Qxd4 Qxd4 7. Nxd4 Bd7 
Ruy Lopez, exchange, Keres variation
e50dc8a0-1d9e-45f9-9942-bae83d4814a4
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Bxc6 dxc6 5. Nc3
Ruy Lopez, exchange, Romanovsky variation
f2b38ba3-1b6d-4699-92a6-1e974cf3b316
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Bxc6 dxc6 5. Nc3 f6 6. d3
******C69: Ruy Lopez, exchange variation, 5.O-O
Ruy Lopez, exchange variation, 5.O-O
12da610d-1792-4384-bfc1-904eb589d747
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Bxc6 dxc6 5. O-O
Ruy Lopez, exchange variation, Alapin gambit
de5a7ae8-747c-4520-b21c-23eab1c43a7e
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Bxc6 dxc6 5. O-O Bg4 6. h3 h5 
Ruy Lopez, exchange, Gligoric variation
96a3f6d5-ccc6-46ca-aba6-a29332a168d5
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Bxc6 dxc6 5. O-O f6 
Ruy Lopez, exchange, Bronstein variation
0456159e-db65-4064-9eca-277152c16d45
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Bxc6 dxc6 5. O-O Qd6 
******C70: Ruy Lopez
Ruy Lopez
e5e5bad9-7d92-4d15-b0da-9c8627656455
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4
Ruy Lopez, fianchetto defence deferred
0bd45fc8-a5da-4268-a293-9d86edf32520
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 g6 
Ruy Lopez, Cozio defence deferred
3cc83870-f8aa-4436-a603-c222415b0c3e
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nge7 
Ruy Lopez, Bird's defence deferred
639419cd-4e6f-4a3f-87eb-85c93b577781
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nd4 
Ruy Lopez, Alapin's defence deferred
aff7eec8-0f65-4312-bc88-fa9d45972879
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Bb4 
Ruy Lopez, Classical defence deferred
b5899591-df42-4e08-b9b1-8ce631f4b611
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Bc5 
Ruy Lopez, Caro variation
d5d5bc76-e222-4544-9601-ba45fa13d8b4
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 b5 
Ruy Lopez, Graz variation
81f63d0f-50ed-4874-9621-c8cd953ea2ff
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 b5 5. Bb3 Bc5 
Ruy Lopez, Taimanov (chase/wing/accelerated counterthrust) variation
beb2a022-5925-4ed6-b805-c4c8378f2db6
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 b5 5. Bb3 Na5 
Ruy Lopez, Schliemann defence deferred
3426d9cc-24be-4d28-a8a1-5dc02c41dfca
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 f5 
******C71: Ruy Lopez, modern Steinitz defence
Ruy Lopez, modern Steinitz defence
0f80c3e5-aafb-460f-90f5-4c62fa2285af
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 d6 
Ruy Lopez, Noah's ark trap
b111b629-11e9-4a25-b225-0faa1b69512a
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 d6 5. d4 b5 6. Bb3 Nxd4 7. Nxd4 exd4 8. Qxd4 c5 
Ruy Lopez, modern Steinitz defence, Three knights variation
9c328650-aaea-4d40-afd4-17a733cdfe58
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 d6 5. Nc3
Ruy Lopez, modern Steinitz defence, Duras (Keres) variation
e9c99d26-6086-49c7-b809-9e25b45daf7b
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 d6 5. c4
******C72: Ruy Lopez, modern Steinitz defence, 5.O-O
Ruy Lopez, modern Steinitz defence, 5.O-O
c23c6b08-98da-4ac5-a4d3-2bf2472f6c68
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 d6 5. O-O
******C73: Ruy Lopez, modern Steinitz defence, Richter variation
Ruy Lopez, modern Steinitz defence, Richter variation
3179ae5c-dd8f-49e3-8082-55c4154a035f
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 d6 5. Bxc6+ bxc6 6. d4
Ruy Lopez, modern Steinitz defence, Alapin variation
f1611c0a-c928-4d64-b24c-29f5b67d9d65
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 d6 5. Bxc6+ bxc6 6. d4 f6 
******C74: Ruy Lopez, modern Steinitz defence
Ruy Lopez, modern Steinitz defence
4fc95001-c1d8-4dfb-b208-a2a9fa8f4d5d
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 d6 5. c3
Ruy Lopez, modern Steinitz defence, siesta variation
699672aa-cbc5-498e-ba32-5924efd93e8f
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 d6 5. c3 f5 
Ruy Lopez, Siesta, Kopayev variation
bc0b79e5-e5d9-4ab2-90a5-f154f7fb0521
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 d6 5. c3 f5 6. exf5 Bxf5 7. O-O
******C75: Ruy Lopez, modern Steinitz defence
Ruy Lopez, modern Steinitz defence
3076d92a-1135-4332-b2ba-0507d595b4da
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 d6 5. c3 Bd7 
Ruy Lopez, modern Steinitz defence, Rubinstein variation
52f907d1-1f1d-487e-98f3-6671d1026a5b
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 d6 5. c3 Bd7 6. d4 Nge7 
******C76: Ruy Lopez, modern Steinitz defence, fianchetto (Bronstein) variation
Ruy Lopez, modern Steinitz defence, fianchetto (Bronstein) variation
78fecf74-4852-4a59-9f51-cadbfef30035
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 d6 5. c3 Bd7 6. d4 g6 
******C77: Ruy Lopez, Morphy defence
Ruy Lopez, Morphy defence
c7682ed7-2271-4a6c-9d49-55481c15197c
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 
Ruy Lopez, four knights (Tarrasch) variation
8127645e-eb73-461e-93e5-2e0b1e4d31a9
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. Nc3
Ruy Lopez, Treybal (Bayreuth) variation (exchange var. deferred)
5495aa1b-a797-4550-a7da-a99d39511f47
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. Bxc6
Ruy Lopez, Wormald (Alapin) attack
290408e1-b984-405c-a738-f9fc60739b5d
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. Qe2
Ruy Lopez, Wormald attack, Gruenfeld variation
3a32dad6-a2b3-441c-84fb-1e6082f2b570
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. Qe2 b5 6. Bb3 Be7 7. d4 d6 8. c3 Bg4 
Ruy Lopez, Anderssen variation
78046f69-6b03-48ed-8d3f-ea08f26b6958
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. d3
Ruy Lopez, Morphy defence, Duras variation
5698e823-3c50-4584-abb0-734e66c7ae93
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. d3 d6 6. c4
******C78: Ruy Lopez, 5.O-O
Ruy Lopez, 5.O-O
22530789-155b-48cb-8483-066ea1343db7
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O
Ruy Lopez, Wing attack
cdc96ec7-fae3-4339-81a7-e3c61478936d
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O b5 6. Bb3 Be7 7. a4
Ruy Lopez, ...b5 & ...d6
604c3d37-3324-46a1-995d-415343a0d10e
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O b5 6. Bb3 d6 
Ruy Lopez, Rabinovich variation
1540095c-1aa4-4e54-9300-d70e24ac3378
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O b5 6. Bb3 d6 7. Ng5 d5 8. exd5 Nd4 9. Re1 Bc5 10. Rxe5+ Kf8 
Ruy Lopez, Archangelsk (counterthrust) variation
f497ffd6-d411-4edf-8cd5-33bea358088f
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O b5 6. Bb3 Bb7 
Ruy Lopez, Moeller defence
3c0cb40e-e3da-48bd-8bbc-f87568a948ea
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Bc5 
******C79: Ruy Lopez, Steinitz defence deferred (Russian defence)
Ruy Lopez, Steinitz defence deferred (Russian defence)
33514e04-728b-450c-9883-10de9e6d14cb
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O d6 
Ruy Lopez, Steinitz defence deferred, Lipnitsky variation
a3524021-a3eb-4607-9898-1f86c5160fce
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O d6 6. Bxc6+ bxc6 7. d4 Bg4 
Ruy Lopez, Steinitz defence deferred, Rubinstein variation
38343aeb-d57b-48e7-a719-b9d687a89d4c
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O d6 6. Bxc6+ bxc6 7. d4 Nxe4 
Ruy Lopez, Steinitz defence deferred, Boleslavsky variation
45fa2545-1846-4d1d-82e2-c5fd0e27bec0
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O d6 6. Bxc6+ bxc6 7. d4 Nxe4 8. Re1 f5 9. dxe5 d5 10. Nc3
******C80: Ruy Lopez, open (Tarrasch) defence
Ruy Lopez, open (Tarrasch) defence
293c9282-0cec-48fe-8c73-f2ac480cc2d8
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 
Ruy Lopez, open, Tartakower variation
0fad158b-bf3b-4734-a7e0-39f1fcca532c
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. Qe2
Ruy Lopez, open, Knorre variation
47af9276-1e86-43ba-81bc-7739a9405acb
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. Nc3
Ruy Lopez, open, 6.d4
9f4557aa-9bb2-4776-a86b-0055fcff95b0
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4
Ruy Lopez, open, Riga variation
74dcd13f-ecb4-4033-ac93-97f5ed62a2e9
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 exd4 
Ruy Lopez, open, 6.d4 b5
d7fa07c0-906e-4e65-9055-a267fed8ef68
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 
Ruy Lopez, open, Friess attack
03248310-5d27-4a29-b1b7-c48ce4bed3a0
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Nxe5
Ruy Lopez, open, Richter variation
301690e1-6a6f-440f-95de-a1ee33db787b
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. d5
Ruy Lopez, open, 7.Bb3
95d0be42-5a35-47ba-b03f-158afd090d93
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3
Ruy Lopez, open, Schlechter defence
8fbd6039-5422-4be8-bafd-b3dfc7de7cb3
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. a4 Nxd4 
Ruy Lopez, open, Berger variation
8a74bc26-3ad8-4bf4-a638-1e0ed79232e4
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. a4 Nxd4 9. Nxd4 exd4 10. Nc3
Ruy Lopez, open, Harksen gambit
e2cca1f0-d3d3-4959-bf7c-62c8ed2e2b25
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. c4
Ruy Lopez, open, 8.de
850ffa0f-7a03-4ebf-9410-efb2c500391c
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5
Ruy Lopez, open, Zukertort variation
d621ee38-9db7-4edd-9174-e85f3daf5c96
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Ne7 
Ruy Lopez, open, 8...Be6
70b56e95-c48f-4d2f-80dc-7816b03c3035
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 
Ruy Lopez, open, Bernstein variation
b542cd12-e024-4642-8d8d-4e6d4cc02f0f
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. Nbd2
Ruy Lopez, open, Bernstein variation, Karpov gambit
d97ca037-acf1-4e86-a84a-d529354e4abd
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. Nbd2 Nc5 10. c3 d4 11. Ng5
******C81: Ruy Lopez, open, Howell attack
Ruy Lopez, open, Howell attack
65e529bc-e5e3-423f-b8a1-bbdd94473a31
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. Qe2
Ruy Lopez, open, Howell attack, Ekstroem variation
bf06849c-3bf8-48ca-a262-1fbe3553241d
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. Qe2 Be7 10. Rd1 O-O 11. c4 bxc4 12. Bxc4 Qd7 
Ruy Lopez, open, Howell attack, Adam variation
d7326af5-6a3d-4b10-88ac-3e2ceeb8f3df
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. Qe2 Be7 10. c4
******C82: Ruy Lopez, open, 9.c3
Ruy Lopez, open, 9.c3
f2f794b2-4f1e-4496-8563-05fa98b08d5d
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. c3
Ruy Lopez, open, Berlin variation
5a794d21-31f1-4f8f-b1aa-d99229277b5d
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. c3 Nc5 
Ruy Lopez, open, Italian variation
27718afb-1c61-4303-bef2-40255646d721
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. c3 Bc5 
Ruy Lopez, open, St. Petersburg variation
fc1d80ce-47a3-4c30-b6ad-d17f7c70ddbc
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. c3 Bc5 10. Nbd2
Ruy Lopez, open, Dilworth variation
8c6e7921-56a9-41d6-ba80-bf7bfdae084c
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. c3 Bc5 10. Nbd2 O-O 11. Bc2 Nxf2 
Ruy Lopez, open, Motzko attack
89092148-282a-4e6c-bec7-e0e1c77ac504
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. c3 Bc5 10. Qd3
Ruy Lopez, open, Motzko attack, Nenarokov variation
38e8da34-fc3a-4265-bde5-43b55468ba30
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. c3 Bc5 10. Qd3 Ne7 
******C83: Ruy Lopez, open, classical defence
Ruy Lopez, open, classical defence
4f8c7a06-efa1-442e-a22f-4970ceeb6ffa
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. c3 Be7 
Ruy Lopez, open, Malkin variation
cda8e487-faaa-48ba-9e28-28ba38f32142
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. c3 Be7 10. Nbd2 O-O 11. Qe2
Ruy Lopez, open, 9...Be7, 10.Re1
f2597990-fcdf-4cf3-aee9-db668f12cb5b
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. c3 Be7 10. Re1
Ruy Lopez, open, Tarrasch trap
8169d244-87f1-4b2b-8c40-555ffb12a3f7
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. c3 Be7 10. Re1 O-O 11. Nd4 Qd7 12. Nxe6 fxe6 13. Rxe4
Ruy Lopez, open, Breslau variation
fe396f91-c397-4dac-8b0b-9fc3d78f28bb
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. c3 Be7 10. Re1 O-O 11. Nd4 Nxe5 
******C84: Ruy Lopez, closed defence
Ruy Lopez, closed defence
e1969d5d-a86e-4995-a662-b0ebc17237b1
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 
Ruy Lopez, closed, centre attack
050c4036-435c-42cb-b8ee-1245a9b8dedb
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. d4
Ruy Lopez, closed, Basque gambit (North Spanish variation)
a06db8c2-3fe5-4084-8db5-ecc9a8974a74
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. d4 exd4 7. e5 Ne4 8. c3
******C85: Ruy Lopez, Exchange variation doubly deferred (DERLD)
Ruy Lopez, Exchange variation doubly deferred (DERLD)
5533459d-4e43-436d-b8f4-79ea89fa8f4e
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Bxc6
******C86: Ruy Lopez, Worrall attack
Ruy Lopez, Worrall attack
953d5ebf-b803-49f2-a43b-2760d45a434a
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Qe2
Ruy Lopez, Worrall attack, sharp line
1f758335-231f-4831-a648-6d208df03913
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Qe2 b5 7. Bb3 O-O 
Ruy Lopez, Worrall attack, solid line
e18cef76-16ee-4c1b-9496-c04793fd6ec6
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Qe2 b5 7. Bb3 d6 
******C87: Ruy Lopez, closed, Averbach variation
Ruy Lopez, closed, Averbach variation
7251f17e-2bd3-4dc4-9888-d7bf6c7faf67
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 d6 
******C88: Ruy Lopez, closed
Ruy Lopez, closed
b5ce6e87-ce53-4051-bdab-416b461ad542
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3
Ruy Lopez, closed, Leonhardt variation
8d5c0fcb-f2be-422f-a870-b2c0a039f6bc
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. c3 Na5 9. Bc2 c5 10. d4 Qc7 11. h3 Nc6 12. d5 Nb8 13. Nbd2 g5 
Ruy Lopez, closed, Balla variation
6fd18267-6836-4802-9602-8cd5750adad9
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. c3 Na5 9. Bc2 c5 10. d4 Qc7 11. a4
Ruy Lopez, closed, 7...d6, 8.d4
7908ba8c-0bda-4324-adf2-4fbff3ad02a0
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. d4
Ruy Lopez, Noah's ark trap
474cabf3-c74f-493f-a6ed-4a288f6fdedd
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. d4 Nxd4 9. Nxd4 exd4 10. Qxd4 c5 
Ruy Lopez, Trajkovic counter-attack
c2669fb9-04d9-4502-a466-b4e4f7842343
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 Bb7 
Ruy Lopez, closed, 7...O-O
2940c95b-900c-4525-8ef1-d4daddd76ecc
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 
Ruy Lopez, closed, anti-Marshall 8.a4
c5fa0f1d-b6e2-45f1-9058-5c10a6dd83f7
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. a4
Ruy Lopez, closed, 8.c3
5ad0d66c-66c8-420e-bfe5-2383b4dddb9b
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3
******C89: Ruy Lopez, Marshall counter-attack
Ruy Lopez, Marshall counter-attack
3673b4fe-baf5-49cc-a71e-454455a0ee8c
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d5 
Ruy Lopez, Marshall counter-attack, 11...c6
6ce80780-9fed-49b9-8d8c-9a749ba86ac7
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d5 9. exd5 Nxd5 10. Nxe5 Nxe5 11. Rxe5 c6 
Ruy Lopez, Marshall, Kevitz variation
5480fb65-6549-41e8-85ae-d35a011a3e63
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d5 9. exd5 Nxd5 10. Nxe5 Nxe5 11. Rxe5 c6 12. Bxd5 cxd5 13. d4 Bd6 14. Re3
Ruy Lopez, Marshall, main line, 12.d2d4
469db241-7fd6-4912-9e2a-d1a67310eeaf
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d5 9. exd5 Nxd5 10. Nxe5 Nxe5 11. Rxe5 c6 12. d4
Ruy Lopez, Marshall, main line, 14...Qh3
8885c27c-aa7b-4f26-845a-247641aed02b
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d5 9. exd5 Nxd5 10. Nxe5 Nxe5 11. Rxe5 c6 12. d4 Bd6 13. Re1 Qh4 14. g3 Qh3 
Ruy Lopez, Marshall, main line, Spassky variation
f036ab87-d43e-4aea-8452-b711ae1bf5f0
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d5 9. exd5 Nxd5 10. Nxe5 Nxe5 11. Rxe5 c6 12. d4 Bd6 13. Re1 Qh4 14. g3 Qh3 15. Be3 Bg4 16. Qd3 Rae8 17. Nd2 Re6 18. a4 Qh5 
Ruy Lopez, Marshall, Herman Steiner variation
f6639296-7778-4e07-91af-ddb0e2ab26bb
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d5 9. exd5 e4 
******C90: Ruy Lopez, closed (with ...d6)
Ruy Lopez, closed (with ...d6)
0a159d04-e323-4062-a8d6-1bd76c58075a
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 
Ruy Lopez, closed, Pilnik variation
27865a27-c08e-48da-adeb-274060d2eaef
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. d3
Ruy Lopez, closed, Lutikov variation
9d323c0b-f021-4c69-a81b-282790c81bd9
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. Bc2
Ruy Lopez, closed, Suetin variation
b0697ac7-1119-41d0-9aa3-7c03033000d3
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. a3
******C91: Ruy Lopez, closed, 9.d4
Ruy Lopez, closed, 9.d4
6c467c21-50aa-4aa5-9a4e-477c52b1366a
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. d4
Ruy Lopez, closed, Bogolyubov variation
5e27c1c8-9a90-4a7f-9e94-2e55afb4aab2
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. d4 Bg4 
******C92: Ruy Lopez, closed, 9.h3
Ruy Lopez, closed, 9.h3
37492bb3-e608-442b-8159-24e525e0acf2
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3
Ruy Lopez, closed, Keres (9...a5) variation
6ae43fcd-4513-47e8-8a64-a17ca767ebb5
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 a5 
Ruy Lopez, closed, Kholmov variation
91cc9859-4ad9-471f-935e-e97db268511a
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Be6 
Ruy Lopez, closed, Ragozin-Petrosian (`Keres') variation
8d703dc2-c03d-474b-bd03-529796f7ae77
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Nd7 
Ruy Lopez, closed, Flohr-Zaitsev system (Lenzerheide variation)
b768ec73-d766-4ba3-9206-5490c30088f8
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Bb7 
******C93: Ruy Lopez, closed, Smyslov defence
Ruy Lopez, closed, Smyslov defence
56f267f9-b90c-4973-ab69-9ce29e5cb1be
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 h6 
******C94: Ruy Lopez, closed, Breyer defence
Ruy Lopez, closed, Breyer defence
78b74d56-1cf8-4cc6-983b-85464b3af965
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Nb8 
******C95: Ruy Lopez, closed, Breyer, 10.d4
Ruy Lopez, closed, Breyer, 10.d4
bde5e977-d04a-4e14-9e50-d65b734bd34d
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Nb8 10. d4
Ruy Lopez, closed, Breyer, Borisenko variation
d6ea13ad-11b0-4aef-9ee5-78313d1e8267
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Nb8 10. d4 Nbd7 
Ruy Lopez, closed, Breyer, Gligoric variation
9002a85f-7f83-4d9f-9367-a7e0c621eb27
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Nb8 10. d4 Nbd7 11. Nbd2 Bb7 12. Bc2 c5 
Ruy Lopez, closed, Breyer, Simagin variation
dde674e7-aaa0-4db5-829e-4d4f4b295b6f
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Nb8 10. d4 Nbd7 11. Nh4
******C96: Ruy Lopez, closed (8...Na5)
Ruy Lopez, closed (8...Na5)
15fd425c-7880-4490-b514-e0c822053b44
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Na5 10. Bc2
Ruy Lopez, closed, Rossolimo defence
f85a9e63-e626-469f-90f5-f10062bfbf00
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Na5 10. Bc2 c6 11. d4 Qc7 
Ruy Lopez, closed (10...c5)
2428edca-e64f-493c-a4cb-21e336a09b84
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Na5 10. Bc2 c5 
Ruy Lopez, closed, Borisenko defence
8b7a7083-82fb-4c21-8302-faccca667c42
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Na5 10. Bc2 c5 11. d4 Nc6 
Ruy Lopez, closed, Keres (...Nd7) defence
00eeebdc-a562-40c4-a250-356e233d9397
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Na5 10. Bc2 c5 11. d4 Nd7 
******C97: Ruy Lopez, closed, Chigorin defence
Ruy Lopez, closed, Chigorin defence
e52c60a8-a616-4f21-bb34-fe5b96012db4
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Na5 10. Bc2 c5 11. d4 Qc7 
Ruy Lopez, closed, Chigorin, Yugoslav system
0e55aa9e-b334-461f-b5fa-4aad0bd38ffa
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Na5 10. Bc2 c5 11. d4 Qc7 12. Nbd2 Bd7 13. Nf1 Rfe8 14. Ne3 g6 
******C98: Ruy Lopez, closed, Chigorin, 12...Nc6
Ruy Lopez, closed, Chigorin, 12...Nc6
98ebf117-0c01-42cd-8156-d8062c58529d
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Na5 10. Bc2 c5 11. d4 Qc7 12. Nbd2 Nc6 
Ruy Lopez, closed, Chigorin, Rauzer attack
e8bc848b-fd64-4978-af2b-d7eb6314b044
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Na5 10. Bc2 c5 11. d4 Qc7 12. Nbd2 Nc6 13. dxc5
******C99: Ruy Lopez, closed, Chigorin, 12...c5d4
Ruy Lopez, closed, Chigorin, 12...c5d4
b10f2cc0-18d7-4d98-95e6-caf3c51fc5e5
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Na5 10. Bc2 c5 11. d4 Qc7 12. Nbd2 cxd4 13. cxd4
******D00: Queen's pawn game
Queen's pawn game
a7f32019-00ad-41f0-a7b6-0912550dc709
1. d4 d5 
Queen's pawn, Mason variation
bb919f81-17d6-425d-a271-64707e1c2e91
1. d4 d5 2. Bf4
Queen's pawn, Mason variation, Steinitz counter-gambit
42376fd1-4470-4780-93b5-bd8ecd503604
1. d4 d5 2. Bf4 c5 
Levitsky attack (Queen's bishop attack)
1c231110-a1bc-43dc-93b5-53930f544534
1. d4 d5 2. Bg5
Blackmar gambit
b13b6285-0dde-42ca-9bfc-3f6c4f5b340b
1. d4 d5 2. e4
Queen's pawn, stonewall attack
7a90b3b2-42d3-42cd-ba24-0f6731dac08a
1. d4 d5 2. e3 Nf6 3. Bd3
Queen's pawn, Chigorin variation
8f16e1e8-2d1c-4cac-8b1a-494ddebc1a4d
1. d4 d5 2. Nc3
Queen's pawn, Anti-Veresov
6ea1f969-6a15-49d8-9aec-c29f5a31e5e4
1. d4 d5 2. Nc3 Bg4 
Blackmar-Diemer gambit
d67602f2-a6e9-4bd1-b533-8ca4dd03c0f9
1. d4 d5 2. Nc3 Nf6 3. e4
Blackmar-Diemer, Euwe defence
bd59926c-0b57-4a5d-8af4-eb85ca7164e9
1. d4 d5 2. Nc3 Nf6 3. e4 dxe4 4. f3 exf3 5. Nxf3 e6 
Blackmar-Diemer, Lemberg counter-gambit
9b9ccb8c-fd31-4ec0-b8af-c99de14effea
1. d4 d5 2. Nc3 Nf6 3. e4 e5 
******D01: Richter-Veresov attack
Richter-Veresov attack
80161963-40cc-420d-b1ab-f9a81200ec15
1. d4 d5 2. Nc3 Nf6 3. Bg5
Richter-Veresov attack, Veresov variation
f5ecaa38-7f83-4224-bc0b-2a974f962c03
1. d4 d5 2. Nc3 Nf6 3. Bg5 Bf5 4. Bxf6
Richter-Veresov attack, Richter variation
acbf67e6-e232-44be-9423-927279243e99
1. d4 d5 2. Nc3 Nf6 3. Bg5 Bf5 4. f3
******D02: Queen's pawn game
Queen's pawn game
ca9a3356-2ee5-4f1a-8b0a-2db608af1883
1. d4 d5 2. Nf3
Queen's pawn game, Chigorin variation
8c5c82b0-a786-4ca6-94f3-976f3c0b2c0f
1. d4 d5 2. Nf3 Nc6 
Queen's pawn game, Krause variation
c20cc6ef-b640-4216-95d9-5682aca3c0f8
1. d4 d5 2. Nf3 c5 
Queen's pawn game
7cd2c2c1-5e09-453a-925a-c608ba4f0d23
1. d4 d5 2. Nf3 Nf6 
Queen's bishop game
e6ebbc63-e7e8-45b0-88d6-ebeada4d1142
1. d4 d5 2. Nf3 Nf6 3. Bf4
******D03: Torre attack (Tartakower variation)
Torre attack (Tartakower variation)
24e750ba-1090-47e0-88c7-3491d3025137
1. d4 d5 2. Nf3 Nf6 3. Bg5
******D04: Queen's pawn game
Queen's pawn game
05e6915f-5dbc-4edb-8d95-bf6ba4fd48a9
1. d4 d5 2. Nf3 Nf6 3. e3
******D05: Queen's pawn game
Queen's pawn game
ba7f37ac-c91e-4b90-85cf-22b9b917500a
1. d4 d5 2. Nf3 Nf6 3. e3 e6 
Queen's pawn game, Zukertort variation
c15cae82-d458-4386-899d-93f17fc97d28
1. d4 d5 2. Nf3 Nf6 3. e3 e6 4. Nbd2 c5 5. b3
Queen's pawn game
cfeaa63d-7d07-46dc-8fb5-b7fac7c550d3
1. d4 d5 2. Nf3 Nf6 3. e3 e6 4. Bd3
Queen's pawn game, Rubinstein (Colle-Zukertort) variation
a6a007c7-35a9-417c-a7e7-f0d5f6dfcb86
1. d4 d5 2. Nf3 Nf6 3. e3 e6 4. Bd3 c5 5. b3
Colle system
8301a619-86ee-438f-a43c-d957a787c77b
1. d4 d5 2. Nf3 Nf6 3. e3 e6 4. Bd3 c5 5. c3
******D06: Queen's Gambit
Queen's Gambit
987287a9-d1e2-448d-b2cf-933022f7a7a3
1. d4 d5 2. c4
Queen's Gambit Declined, Grau (Sahovic) defence
c76404aa-ba73-48dc-8ed9-954306595613
1. d4 d5 2. c4 Bf5 
Queen's Gambit Declined, Marshall defence
13fc1ed9-3ee7-401e-86b5-9ff19ce0ba04
1. d4 d5 2. c4 Nf6 
Queen's Gambit Declined, symmetrical (Austrian) defence
e5a6e28f-2137-4fb1-8e9f-dcca446fa2c5
1. d4 d5 2. c4 c5 
******D07: Queen's Gambit Declined, Chigorin defence
Queen's Gambit Declined, Chigorin defence
fe19b274-7f06-49b3-80b9-14221966198d
1. d4 d5 2. c4 Nc6 
Queen's Gambit Declined, Chigorin defence, Janowski variation
b8ddf100-0761-4a4e-8ace-866a6cb65f1f
1. d4 d5 2. c4 Nc6 3. Nc3 dxc4 4. Nf3
******D08: Queen's Gambit Declined, Albin counter-gambit
Queen's Gambit Declined, Albin counter-gambit
03a2b7cc-0136-4382-8c58-e445955bfdee
1. d4 d5 2. c4 e5 
Queen's Gambit Declined, Albin counter-gambit, Lasker trap
c093b76a-cd3f-4a75-b03c-8eeaca19247c
1. d4 d5 2. c4 e5 3. dxe5 d4 4. e3 Bb4+ 5. Bd2 dxe3 
Queen's Gambit Declined, Albin counter-gambit
adddfeff-ee0a-45e0-b925-19953fe9c00e
1. d4 d5 2. c4 e5 3. dxe5 d4 4. Nf3
Queen's Gambit Declined, Albin counter-gambit, Alapin variation
8eac4de1-b656-468a-9e5a-b7db0e45cb03
1. d4 d5 2. c4 e5 3. dxe5 d4 4. Nf3 Nc6 5. Nbd2
Queen's Gambit Declined, Albin counter-gambit, Krenosz variation
d58fb33d-91f1-4992-bf42-f5b76be2905b
1. d4 d5 2. c4 e5 3. dxe5 d4 4. Nf3 Nc6 5. Nbd2 Bg4 6. h3 Bxf3 7. Nxf3 Bb4+ 8. Bd2 Qe7 
Queen's Gambit Declined, Albin counter-gambit, Janowski variation
262eec00-5b59-4581-982f-6f073c775fc9
1. d4 d5 2. c4 e5 3. dxe5 d4 4. Nf3 Nc6 5. Nbd2 f6 
Queen's Gambit Declined, Albin counter-gambit, Balogh variation
e1c28f24-5d9d-409a-b982-3e8f238798ce
1. d4 d5 2. c4 e5 3. dxe5 d4 4. Nf3 Nc6 5. Nbd2 Qe7 
******D09: Queen's Gambit Declined, Albin counter-gambit, 5.g3
Queen's Gambit Declined, Albin counter-gambit, 5.g3
60f8a05b-3cbe-4af7-8aac-495d2a1f4d3a
1. d4 d5 2. c4 e5 3. dxe5 d4 4. Nf3 Nc6 5. g3
******D10: Queen's Gambit Declined Slav defence
Queen's Gambit Declined Slav defence
ac25ff16-182e-4df5-a52f-af1a66e0a2ad
1. d4 d5 2. c4 c6 
Queen's Gambit Declined Slav defence, Alekhine variation
71ba9ebe-13ea-4e22-b4cd-d1e658545beb
1. d4 d5 2. c4 c6 3. Nc3 dxc4 4. e4
Queen's Gambit Declined Slav, Winawer counter-gambit
58dcd45c-65ac-4669-9029-35b2b3d45dbd
1. d4 d5 2. c4 c6 3. Nc3 e5 
Queen's Gambit Declined Slav defence, exchange variation
7c694ff1-93a8-447b-bacf-d85c49eb3936
1. d4 d5 2. c4 c6 3. cxd5
******D11: Queen's Gambit Declined Slav, 3.Nf3
Queen's Gambit Declined Slav, 3.Nf3
bef74a4f-4986-4f31-80bf-920d979f7d75
1. d4 d5 2. c4 c6 3. Nf3
Queen's Gambit Declined Slav, Breyer variation
8dea6c11-c2ad-4bc4-a5dd-16213ea6def5
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nbd2
Queen's Gambit Declined Slav, 4.e3
a497ba30-c11f-47a9-b338-bc051735b3d3
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. e3
******D12: Queen's Gambit Declined Slav, 4.e3 Bf5
Queen's Gambit Declined Slav, 4.e3 Bf5
d99673f6-6def-45a0-8cdd-e01d16c3b501
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. e3 Bf5 
Queen's Gambit Declined Slav, Landau variation
6cd83fe7-fb94-496d-a812-5558902ed728
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. e3 Bf5 5. cxd5 cxd5 6. Qb3 Qc8 7. Bd2 e6 8. Na3
Queen's Gambit Declined Slav, exchange variation
936e383a-5f73-48bb-b727-223660176797
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. e3 Bf5 5. cxd5 cxd5 6. Nc3
Queen's Gambit Declined Slav, Amsterdam variation
a305f916-04b1-4dac-913d-20d488a4894a
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. e3 Bf5 5. cxd5 cxd5 6. Nc3 e6 7. Ne5 Nfd7 
******D13: Queen's Gambit Declined Slav, exchange variation
Queen's Gambit Declined Slav, exchange variation
e284d795-2ae9-4550-a8d1-77f5af05bd77
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. cxd5 cxd5 
******D14: Queen's Gambit Declined Slav, exchange variation, 6.Bf4 Bf5
Queen's Gambit Declined Slav, exchange variation, 6.Bf4 Bf5
4d32fabd-7e81-4115-9205-6abea95a4992
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. cxd5 cxd5 5. Nc3 Nc6 6. Bf4 Bf5 
Queen's Gambit Declined Slav, exchange, Trifunovic variation
d32e6407-644c-41a4-a7d1-1543a39fd044
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. cxd5 cxd5 5. Nc3 Nc6 6. Bf4 Bf5 7. e3 e6 8. Qb3 Bb4 
******D15: Queen's Gambit Declined Slav, 4.Nc3
Queen's Gambit Declined Slav, 4.Nc3
433e4fcc-3aa2-46df-b4ea-d9f8d7178592
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3
Queen's Gambit Declined Slav, Suechting variation
78f233a4-68d7-4993-a57f-2f2a80ebcdb9
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 Qb6 
Queen's Gambit Declined Slav, Schlechter variation
77f45055-ef31-42f2-9133-3ccc5ad819ff
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 g6 
Queen's Gambit Declined Slav accepted
122efc1b-6a82-4adf-bd08-95888310cf00
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 
Queen's Gambit Declined Slav, 5.e3 (Alekhine variation)
3d2f53cc-6537-40dd-a037-5936b66bd0d9
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. e3
Queen's Gambit Declined Slav, Slav gambit
6fad0d0f-cffb-41ab-9116-9e5f416324ac
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. e4
Queen's Gambit Declined Slav, Tolush-Geller gambit
6f21df18-3e6a-484b-8159-fb5f06778c6b
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. e4 b5 6. e5
******D16: Queen's Gambit Declined Slav accepted, Alapin variation
Queen's Gambit Declined Slav accepted, Alapin variation
05597f6f-4310-484a-82f4-f0e62681ff9b
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. a4
Queen's Gambit Declined Slav, Smyslov variation
6d3bb354-06e0-4544-b777-f3864da59306
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. a4 Na6 6. e4 Bg4 
Queen's Gambit Declined Slav, Soultanbeieff variation
2df4b367-3ef6-4ba5-9f4d-abb06cd52521
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. a4 e6 
Queen's Gambit Declined Slav, Steiner variation
16d0a288-6c07-4e54-995d-1076c3b7eab8
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. a4 Bg4 
******D17: Queen's Gambit Declined Slav, Czech defence
Queen's Gambit Declined Slav, Czech defence
7864ca5c-087c-4bf5-abad-2da424aa5cc3
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. a4 Bf5 
Queen's Gambit Declined Slav, Krause attack
a776adc8-8def-455f-8c6f-9fab07096340
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. a4 Bf5 6. Ne5
Queen's Gambit Declined Slav, Carlsbad variation
3b1cad8c-48b2-4928-88eb-09688a330943
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. a4 Bf5 6. Ne5 Nbd7 7. Nxc4 Qc7 8. g3 e5 
Queen's Gambit Declined Slav, Wiesbaden variation
bf48a98a-04ea-4c5c-95b1-a577d5c99d68
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. a4 Bf5 6. Ne5 e6 
******D18: Queen's Gambit Declined Slav, Dutch variation
Queen's Gambit Declined Slav, Dutch variation
61f2f303-f596-4636-932d-f0af033352c5
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. a4 Bf5 6. e3
Queen's Gambit Declined Slav, Dutch, Lasker variation
b7eb578f-4e84-40ab-98f3-7803b122ccef
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. a4 Bf5 6. e3 Na6 
******D19: Queen's Gambit Declined Slav, Dutch variation
Queen's Gambit Declined Slav, Dutch variation
8061d8ce-6866-46d2-a0ea-2b84a6b4270b
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. a4 Bf5 6. e3 e6 7. Bxc4 Bb4 8. O-O
Queen's Gambit Declined Slav, Dutch variation, main line
b3cc4b72-cc97-450b-bc5a-dee4fc7b6fc4
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. a4 Bf5 6. e3 e6 7. Bxc4 Bb4 8. O-O O-O 9. Qe2
Queen's Gambit Declined Slav, Dutch, Saemisch variation
900f9a08-8bc1-43be-ad11-9d9542a0a8b8
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. a4 Bf5 6. e3 e6 7. Bxc4 Bb4 8. O-O O-O 9. Qe2 Ne4 10. g4
******D20: Queen's gambit accepted
Queen's gambit accepted
480c2f49-34b2-4609-820f-0a81f12c768a
1. d4 d5 2. c4 dxc4 
Queen's Gambit Accepted, 3.e4
dfd708d1-e60b-4c2c-8ce0-efca4b2221b3
1. d4 d5 2. c4 dxc4 3. e4
Queen's Gambit Accepted, Linares variation
c5d9d5a0-e76b-4ef0-85e5-83f50551ed93
1. d4 d5 2. c4 dxc4 3. e4 c5 4. d5 Nf6 5. Nc3 b5 
Queen's Gambit Accepted, Schwartz defence
337816d4-d3a9-4abc-81cc-4957fa163cd7
1. d4 d5 2. c4 dxc4 3. e4 f5 
******D21: Queen's Gambit Accepted, 3.Nf3
Queen's Gambit Accepted, 3.Nf3
791e7bab-a84e-4fa5-998c-7ba9a3ead657
1. d4 d5 2. c4 dxc4 3. Nf3
Queen's Gambit Accepted, Ericson variation
127e76e3-d3c9-4b3e-a783-7c33feedef29
1. d4 d5 2. c4 dxc4 3. Nf3 b5 
Queen's Gambit Accepted, Alekhine defense, Borisenko-Furman variation
edac74f6-c428-4096-bdda-e3e6f8b04f12
1. d4 d5 2. c4 dxc4 3. Nf3 a6 4. e4
******D22: Queen's Gambit Accepted, Alekhine defence
Queen's Gambit Accepted, Alekhine defence
cf0c5a0d-67a3-4899-b50f-f2705419af11
1. d4 d5 2. c4 dxc4 3. Nf3 a6 
Queen's Gambit Accepted, Alekhine defence, Alatortsev variation
dfa22b94-720b-4159-877a-3af071ca7062
1. d4 d5 2. c4 dxc4 3. Nf3 a6 4. e3 Bg4 5. Bxc4 e6 6. d5
Queen's Gambit Accepted, Haberditz variation
712bf668-9c8c-41af-af1a-d9a9524fc931
1. d4 d5 2. c4 dxc4 3. Nf3 a6 4. e3 b5 
******D23: Queen's gambit accepted
Queen's gambit accepted
a515bf01-9885-4b3b-8093-0f14426518a3
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 
Queen's Gambit Accepted, Mannheim variation
42e9a2d4-b452-4b5f-add7-80994dfbaae6
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. Qa4+
******D24: Queen's Gambit Accepted, 4.Nc3
Queen's Gambit Accepted, 4.Nc3
637c15f9-d6f2-41e7-bb0f-e49475068898
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. Nc3
Queen's Gambit Accepted, Bogolyubov variation
59fd5572-1f09-4a39-a7c0-16809ed6460d
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. Nc3 a6 5. e4
******D25: Queen's Gambit Accepted, 4.e3
Queen's Gambit Accepted, 4.e3
c429b201-7354-4eb4-b435-01de6c57d7b8
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3
Queen's Gambit Accepted, Smyslov variation
9f71de97-8303-4103-8fb4-114033d44888
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 g6 
Queen's Gambit Accepted, Janowsky-Larsen variation
a98b4eb9-4de7-47c3-a6d7-553760d8ac8a
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 Bg4 
Queen's Gambit Accepted, Flohr variation
8379a88b-7723-469f-80f3-72e470ec932e
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 Be6 
******D26: Queen's Gambit Accepted, 4...e6
Queen's Gambit Accepted, 4...e6
dcc56451-29f0-4bb8-a429-14f7a9344b22
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 e6 
Queen's Gambit Accepted, classical variation
c7128405-7489-4575-b59c-8d4efb762d2c
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 e6 5. Bxc4 c5 
Queen's Gambit Accepted, classical, Furman variation
f1aa7369-6873-4004-8dc2-31069edc4746
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 e6 5. Bxc4 c5 6. Qe2 a6 7. dxc5 Bxc5 8. O-O Nc6 9. e4 b5 10. e5
Queen's Gambit Accepted, classical variation, 6.O-O
fdf33745-1ddf-453c-8158-46b6120c3239
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 e6 5. Bxc4 c5 6. O-O
Queen's Gambit Accepted, classical, Steinitz variation
1d342088-316d-40ce-a831-b37511d708fd
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 e6 5. Bxc4 c5 6. O-O cxd4 
******D27: Queen's Gambit Accepted, classical, 6...a6
Queen's Gambit Accepted, classical, 6...a6
bf14eff9-662b-4119-a617-2d63e767856c
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 e6 5. Bxc4 c5 6. O-O a6 
Queen's Gambit Accepted, classical, Rubinstein variation
a9b39207-d9d7-41b7-8263-246e04056f30
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 e6 5. Bxc4 c5 6. O-O a6 7. a4
Queen's Gambit Accepted, classical, Geller variation
66af11a8-17a6-4aae-9e03-c082caf2c4b9
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 e6 5. Bxc4 c5 6. O-O a6 7. e4
******D28: Queen's Gambit Accepted, classical, 7.Qe2
Queen's Gambit Accepted, classical, 7.Qe2
49252f31-d6c3-4076-874a-fa82cfd35dc3
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 e6 5. Bxc4 c5 6. O-O a6 7. Qe2
Queen's Gambit Accepted, classical, 7...b5
cb3ace89-ea3f-444b-8577-39a056ab0da8
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 e6 5. Bxc4 c5 6. O-O a6 7. Qe2 b5 
Queen's Gambit Accepted, classical, Flohr variation
241da695-21d8-45f0-9a1c-ed4982051c69
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 e6 5. Bxc4 c5 6. O-O a6 7. Qe2 b5 8. Bb3 Nc6 9. Rd1 c4 10. Bc2 Nb4 11. Nc3 Nxc2 12. Qxc2 Bb7 13. d5 Qc7 
******D29: Queen's Gambit Accepted, classical, 8...Bb7
Queen's Gambit Accepted, classical, 8...Bb7
353dc715-4fbc-4f1f-a897-30d7f8efc691
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 e6 5. Bxc4 c5 6. O-O a6 7. Qe2 b5 8. Bb3 Bb7 
Queen's Gambit Accepted, classical, Smyslov variation
2a0be13d-35c5-43e5-a3fe-e1d66b7e7709
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 e6 5. Bxc4 c5 6. O-O a6 7. Qe2 b5 8. Bb3 Bb7 9. Rd1 Nbd7 10. Nc3 Bd6 
******D30: Queen's gambit declined
Queen's gambit declined
0cdfa47a-25ea-4f56-b47a-8368c20de93d
1. d4 d5 2. c4 e6 
Queen's Gambit Declined Slav
48efa32c-ab9e-4b8f-b75f-9d4d513fb2e8
1. d4 d5 2. c4 e6 3. Nf3 Nf6 4. e3 c6 5. Nbd2
Queen's Gambit Declined, Stonewall variation
99b096ef-4f02-4005-a5f2-9ad3744d14fe
1. d4 d5 2. c4 e6 3. Nf3 Nf6 4. e3 c6 5. Nbd2 Ne4 6. Bd3 f5 
Queen's Gambit Declined Slav
2bfe273c-3218-4b3b-9095-ddf1ddc87235
1. d4 d5 2. c4 e6 3. Nf3 Nf6 4. e3 c6 5. Nbd2 Nbd7 
Queen's Gambit Declined Slav, Semmering variation
04ac8c6d-d6a3-48c2-9b0f-7d95e5fc4968
1. d4 d5 2. c4 e6 3. Nf3 Nf6 4. e3 c6 5. Nbd2 Nbd7 6. Bd3 c5 
Queen's Gambit Declined, Spielmann variation
4f5cb400-6676-43b7-b54a-b45aa459018d
1. d4 d5 2. c4 e6 3. Nf3 Nf6 4. e3 c6 5. Nbd2 g6 
Queen's Gambit Declined
4feb61b8-6e09-4cb2-aa24-96f0873d37b6
1. d4 d5 2. c4 e6 3. Nf3 Nf6 4. Bg5
Queen's Gambit Declined, Capablanca variation
075c40da-1f0b-4cc2-a188-0f21003adb38
1. d4 d5 2. c4 e6 3. Nf3 Nf6 4. Bg5 Nbd7 5. e3 c6 6. Nbd2
Queen's Gambit Declined, Vienna variation
5efef144-b842-4287-992b-4e6ae1014fa7
1. d4 d5 2. c4 e6 3. Nf3 Nf6 4. Bg5 Bb4+ 
Queen's Gambit Declined, Capablanca-Duras variation
178344cb-6ff0-45a4-b5fd-37fd9997eea9
1. d4 d5 2. c4 e6 3. Nf3 Nf6 4. Bg5 h6 
Queen's Gambit Declined, Hastings variation
0058cb1c-b260-4d5f-bb77-31e671337a89
1. d4 d5 2. c4 e6 3. Nf3 Nf6 4. Bg5 h6 5. Bxf6 Qxf6 6. Nc3 c6 7. Qb3
******D31: Queen's Gambit Declined, 3.Nc3
Queen's Gambit Declined, 3.Nc3
825cdd4e-36ef-4ecf-a7a6-ff2f5aee0bb3
1. d4 d5 2. c4 e6 3. Nc3
Queen's Gambit Declined, Janowski variation
e3400b17-17b0-429b-a962-2dd8ae3a97e1
1. d4 d5 2. c4 e6 3. Nc3 a6 
Queen's Gambit Declined, Alapin variation
1ec16568-44c9-4419-b5f2-6f7ba3a2a7c7
1. d4 d5 2. c4 e6 3. Nc3 b6 
Queen's Gambit Declined, Charousek (Petrosian) variation
abb10ef2-940f-4330-a983-d54dc4aeebd1
1. d4 d5 2. c4 e6 3. Nc3 Be7 
Queen's Gambit Declined, semi-Slav
07aa9930-156c-4b3c-9f38-03fbbf61b4e4
1. d4 d5 2. c4 e6 3. Nc3 c6 
Queen's Gambit Declined, semi-Slav, Noteboom variation
063eb51c-dc93-42cf-9a53-9677e703b635
1. d4 d5 2. c4 e6 3. Nc3 c6 4. Nf3 dxc4 
Queen's Gambit Declined, semi-Slav, Koomen variation
b33612b9-4d04-40a0-8abd-666027961686
1. d4 d5 2. c4 e6 3. Nc3 c6 4. Nf3 dxc4 5. a4 Bb4 6. e3 b5 7. Bd2 Qe7 
Queen's Gambit Declined, semi-Slav, Junge variation
9e48e952-8baa-4466-bffb-cf4f6d0e6289
1. d4 d5 2. c4 e6 3. Nc3 c6 4. Nf3 dxc4 5. a4 Bb4 6. e3 b5 7. Bd2 Qb6 
Queen's Gambit Declined, semi-Slav, Abrahams variation
3387cd93-4857-4098-87a9-69336c1274be
1. d4 d5 2. c4 e6 3. Nc3 c6 4. Nf3 dxc4 5. a4 Bb4 6. e3 b5 7. Bd2 a5 
Queen's Gambit Declined, semi-Slav, Marshall gambit
e7e5ae32-6751-496f-9eaf-4242d387ac1e
1. d4 d5 2. c4 e6 3. Nc3 c6 4. e4
******D32: Queen's Gambit Declined, Tarrasch defence
Queen's Gambit Declined, Tarrasch defence
63d89465-45cc-44bb-8ce5-cf31dc41200b
1. d4 d5 2. c4 e6 3. Nc3 c5 
Queen's Gambit Declined, Tarrasch, von Hennig-Schara gambit
3302b36e-8a25-4c3c-af1f-4254cbb61535
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 cxd4 
Queen's Gambit Declined, Tarrasch defence, 4.cd ed
4fb417bc-8536-4218-85a9-c1047de6ef0f
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 
Queen's Gambit Declined, Tarrasch defence, Tarrasch gambit
68c19c5c-7115-4e26-a4c2-176fbc5bfbf5
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. dxc5 d4 6. Na4 b5 
Queen's Gambit Declined, Tarrasch defence, Marshall gambit
9d1c2bf9-d8f1-4386-b9df-c988ff11f837
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. e4
Queen's Gambit Declined, Tarrasch defence
f4b6e689-0512-47e1-b796-02d4947a4486
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. Nf3
******D33: Queen's Gambit Declined, Tarrasch, Schlechter-Rubinstein system
Queen's Gambit Declined, Tarrasch, Schlechter-Rubinstein system
e69579df-9395-4492-8bf6-4cc4e6eb9246
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. Nf3 Nc6 6. g3
Queen's Gambit Declined, Tarrasch, Folkestone (Swedish) variation
fbffbeff-2c66-42d5-9a1b-55b749cd51d1
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. Nf3 Nc6 6. g3 c4 
Queen's Gambit Declined, Tarrasch, Schlechter-Rubinstein system, Rey Ardid variation
66e2ec83-baa8-4b18-90aa-ea83734304d5
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. Nf3 Nc6 6. g3 c4 7. e4
Queen's Gambit Declined, Tarrasch, Prague variation
54b81988-883b-4f47-8380-e686c33ed243
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. Nf3 Nc6 6. g3 Nf6 
Queen's Gambit Declined, Tarrasch, Wagner variation
d7b56d24-586f-45c5-a19e-2341f55d79c2
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. Nf3 Nc6 6. g3 Nf6 7. Bg2 Bg4 
******D34: Queen's Gambit Declined, Tarrasch, Prague variation, 7...Be7
Queen's Gambit Declined, Tarrasch, Prague variation, 7...Be7
20cff93f-217f-4582-8cd5-7be8977dc8e5
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. Nf3 Nc6 6. g3 Nf6 7. Bg2 Be7 
Queen's Gambit Declined, Tarrasch, Prague variation, Normal position
b5058036-3326-4fbe-a090-93e61d33c259
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. Nf3 Nc6 6. g3 Nf6 7. Bg2 Be7 8. O-O O-O 
Queen's Gambit Declined, Tarrasch, Reti variation
0f5e2aab-cf5e-4965-82fa-110562b3e790
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. Nf3 Nc6 6. g3 Nf6 7. Bg2 Be7 8. O-O O-O 9. dxc5 Bxc5 10. Na4
Queen's Gambit Declined, Tarrasch, Prague variation, 9.Bg5
dadb8155-6c5c-4765-986c-2aabb1f70fb2
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. Nf3 Nc6 6. g3 Nf6 7. Bg2 Be7 8. O-O O-O 9. Bg5
Queen's Gambit Declined, Tarrasch, Bogolyubov variation
f41f42fb-325c-4912-a454-7326abba7ed5
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. Nf3 Nc6 6. g3 Nf6 7. Bg2 Be7 8. O-O O-O 9. Bg5 Be6 10. Rc1 c4 
Queen's Gambit Declined, Tarrasch, Stoltz variation
a2c7f52a-e501-4577-83fa-0166d5dcb413
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. Nf3 Nc6 6. g3 Nf6 7. Bg2 Be7 8. O-O O-O 9. Bg5 Be6 10. Rc1 b6 
******D35: Queen's Gambit Declined, 3...Nf6
Queen's Gambit Declined, 3...Nf6
28701ed9-11ed-4d95-bfec-3a2927e58eeb
1. d4 d5 2. c4 e6 3. Nc3 Nf6 
Queen's Gambit Declined, Harrwitz attack
dfeec2d3-d055-46df-bc0f-7948d81ce9f0
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bf4
Queen's Gambit Declined, exchange variation
cabcd3d8-4169-43bb-bbfd-c11d4861f0be
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. cxd5
Queen's Gambit Declined, exchange, Saemisch variation
98e60904-42c7-4466-b251-e746b694d4c4
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. cxd5 exd5 5. Nf3 Nbd7 6. Bf4
Queen's Gambit Declined, exchange, positional line
07efd7bb-2257-41c2-a3c4-93ba29786d65
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. cxd5 exd5 5. Bg5
Queen's Gambit Declined, exchange, chameleon variation
8e51be44-66b3-4748-8f45-adb7b06a1173
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. cxd5 exd5 5. Bg5 Be7 6. e3 O-O 7. Bd3 Nbd7 8. Qc2 Re8 9. Nge2 Nf8 10. O-O-O
Queen's Gambit Declined, exchange, positional line, 5...c6
dd71b73f-5139-4880-897f-74e11cd91a76
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. cxd5 exd5 5. Bg5 c6 
******D36: Queen's Gambit Declined, exchange, positional line, 6.Qc2
Queen's Gambit Declined, exchange, positional line, 6.Qc2
a2d8d614-97ca-4fde-9456-1662b1896a89
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. cxd5 exd5 5. Bg5 c6 6. Qc2
******D37: Queen's Gambit Declined, 4.Nf3
Queen's Gambit Declined, 4.Nf3
75abe465-a5cb-4f4b-90d1-4bdc28ed6404
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3
Queen's Gambit Declined, classical variation (5.Bf4)
1b582ea8-4eb1-4e60-92d9-3907d666cd6c
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 Be7 5. Bf4
******D38: Queen's Gambit Declined, Ragozin variation
Queen's Gambit Declined, Ragozin variation
3f83cade-d3e2-439a-a1a6-ac9373386b2c
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 Bb4 
******D39: Queen's Gambit Declined, Ragozin, Vienna variation
Queen's Gambit Declined, Ragozin, Vienna variation
98674170-316e-423f-b56e-1995de14b4ae
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 Bb4 5. Bg5 dxc4 
******D40: Queen's Gambit Declined, Semi-Tarrasch defence
Queen's Gambit Declined, Semi-Tarrasch defence
661fb89e-4c28-4896-847b-3dca805a95b5
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c5 
Queen's Gambit Declined, Semi-Tarrasch, symmetrical variation
e3954dc5-0825-4f84-b0bc-21bffa6efdea
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c5 5. e3 Nc6 6. Bd3 Bd6 7. O-O O-O 
Queen's Gambit Declined, Semi-Tarrasch, Levenfish variation
40abcf6c-7f37-4a75-a2f7-40b28ba99b54
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c5 5. e3 Nc6 6. Bd3 Bd6 7. O-O O-O 8. Qe2 Qe7 9. dxc5 Bxc5 10. e4
Queen's Gambit Declined, Semi-Tarrasch defence, Pillsbury variation
1043f6d5-dc78-4e41-a664-207cd41ce517
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c5 5. Bg5
******D41: Queen's Gambit Declined, Semi-Tarrasch, 5.cd
Queen's Gambit Declined, Semi-Tarrasch, 5.cd
d29af010-f88d-41c0-8418-93d614e5b54c
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c5 5. cxd5
Queen's Gambit Declined, Semi-Tarrasch, Kmoch variation
e2f7f767-a217-4435-a89d-e544c4630516
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c5 5. cxd5 Nxd5 6. e4 Nxc3 7. bxc3 cxd4 8. cxd4 Bb4+ 9. Bd2 Bxd2+ 10. Qxd2 O-O 11. Bb5
Queen's Gambit Declined, Semi-Tarrasch, San Sebastian variation
56759e96-f44d-46c0-a5de-7132b776b20d
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c5 5. cxd5 Nxd5 6. e4 Nxc3 7. bxc3 cxd4 8. cxd4 Bb4+ 9. Bd2 Qa5 
Queen's Gambit Declined, Semi-Tarrasch with e3
a7d9b38e-50e6-4eca-8653-8ea70ba460fe
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c5 5. cxd5 Nxd5 6. e3
******D42: Queen's Gambit Declined, Semi-Tarrasch, 7.Bd3
Queen's Gambit Declined, Semi-Tarrasch, 7.Bd3
8f1a4311-8b36-4925-8a2c-0f2bf1ed4750
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c5 5. cxd5 Nxd5 6. e3 Nc6 7. Bd3
******D43: Queen's Gambit Declined semi-Slav
Queen's Gambit Declined semi-Slav
73064fa6-221a-46fa-9083-6c0dda0494da
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 
Queen's Gambit Declined semi-Slav, Hastings variation
67935ad1-7e15-4784-8668-93b2622bb61e
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. Bg5 h6 6. Bxf6 Qxf6 7. Qb3
******D44: Queen's Gambit Declined semi-Slav, 5.Bg5 dc
Queen's Gambit Declined semi-Slav, 5.Bg5 dc
2535349d-eba2-4d7a-a2b0-78cb46e83c52
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. Bg5 dxc4 
Queen's Gambit Declined semi-Slav, Botvinnik system (anti-Meran)
9ac2641a-cfd5-45f9-8ef3-0f656e70b358
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. Bg5 dxc4 6. e4
Queen's Gambit Declined semi-Slav, Ekstrom variation
b6afa357-1d2c-47c8-a096-7246aa4b3ea4
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. Bg5 dxc4 6. e4 b5 7. e5 h6 8. Bh4 g5 9. exf6 gxh4 10. Ne5
Queen's Gambit Declined semi-Slav, anti-Meran gambit
f5a42fd3-c51c-4eb1-ad31-589dc52c0053
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. Bg5 dxc4 6. e4 b5 7. e5 h6 8. Bh4 g5 9. Nxg5
Queen's Gambit Declined semi-Slav, anti-Meran, Lilienthal variation
fda9495d-487f-4e96-8604-832af623fcef
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. Bg5 dxc4 6. e4 b5 7. e5 h6 8. Bh4 g5 9. Nxg5 hxg5 10. Bxg5 Nbd7 11. g3
Queen's Gambit Declined semi-Slav, anti-Meran, Szabo variation
1d3bd680-e5ec-4d5b-a7f8-28076c638f43
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. Bg5 dxc4 6. e4 b5 7. e5 h6 8. Bh4 g5 9. Nxg5 hxg5 10. Bxg5 Nbd7 11. Qf3
Queen's Gambit Declined semi-Slav, anti-Meran, Alatortsev system
261542bc-ea6e-441b-81c8-0a4a88ef6c36
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. Bg5 dxc4 6. e4 b5 7. e5 h6 8. Bh4 g5 9. Nxg5 Nd5 
******D45: Queen's Gambit Declined semi-Slav, 5.e3
Queen's Gambit Declined semi-Slav, 5.e3
af936948-43b4-4904-8ebc-39387decca5c
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3
Queen's Gambit Declined semi-Slav, stonewall defence
f3638ad5-1006-4d2c-b777-4556e3a1e327
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Ne4 6. Bd3 f5 
Queen's Gambit Declined semi-Slav, accelerated Meran (Alekhine variation)
2be1a7be-1408-4717-b578-00bd20671516
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 a6 
Queen's Gambit Declined semi-Slav, 5...Nd7
082a5d62-a62e-4333-8e09-8c07ffc4e7fb
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 
Queen's Gambit Declined semi-Slav, Stoltz variation
ef9397a1-aa57-43c3-8332-e8a8a43cf701
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Qc2
Queen's Gambit Declined semi-Slav, Rubinstein (anti-Meran) system
e434edb1-ab29-477e-988b-f62216900b4f
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Ne5
******D46: Queen's Gambit Declined semi-Slav, 6.Bd3
Queen's Gambit Declined semi-Slav, 6.Bd3
8140ce73-ab40-43a5-b995-127238e98705

1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3
Queen's Gambit Declined semi-Slav, Bogolyubov variation
1f35f2cf-5361-42f5-ad04-726ac6103a9d
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 Be7 
Queen's Gambit Declined semi-Slav, Romih variation
a7427aa4-cb5a-4359-975b-fc6dcca68837
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 Bb4 
Queen's Gambit Declined semi-Slav, Chigorin defence
855b61d3-eae6-43db-acb9-e713ad6faa6f
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 Bd6 
******D47: Queen's Gambit Declined semi-Slav, 7.Bc4
Queen's Gambit Declined semi-Slav, 7.Bc4
f4c2eb6e-8c3a-4a6b-8eda-70fd6ce03808
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4
Queen's Gambit Declined semi-Slav, Meran variation
5c8d1360-17a0-4872-87bf-cbfbc93be29f
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 
Queen's Gambit Declined semi-Slav, neo-Meran (Lundin variation)
5ca0fe7d-27f6-448d-9d23-101cb6a888e7
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 8. Bd3 b4 
Queen's Gambit Declined semi-Slav, Meran, Wade variation
1de2666c-37a5-4c9c-82c5-65cd9644df38
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 8. Bd3 Bb7 
******D48: Queen's Gambit Declined semi-Slav, Meran, 8...a6
Queen's Gambit Declined semi-Slav, Meran, 8...a6
6e697349-818e-4f66-84ca-48ca5a6437db
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 8. Bd3 a6 
Queen's Gambit Declined semi-Slav, Meran, Pirc variation
5fad76a2-9401-4910-94d5-3628328271c8
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 8. Bd3 a6 9. e4 b4 
Queen's Gambit Declined semi-Slav, Meran
fb611a84-400f-4c8c-9a9a-ca27d9efb20d
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 8. Bd3 a6 9. e4 c5 
Queen's Gambit Declined semi-Slav, Meran, Reynolds' variation
4aa4946a-02ae-4923-b42f-c0403761a1e0
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 8. Bd3 a6 9. e4 c5 10. d5
Queen's Gambit Declined semi-Slav, Meran, old main line
a6071588-81d1-4d2f-a465-100d71d67d65
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 8. Bd3 a6 9. e4 c5 10. e5
******D49: Queen's Gambit Declined semi-Slav, Meran, Blumenfeld variation
Queen's Gambit Declined semi-Slav, Meran, Blumenfeld variation
1ea1ed12-a644-4183-8b1e-50194507106d
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 8. Bd3 a6 9. e4 c5 10. e5 cxd4 11. Nxb5
Queen's Gambit Declined semi-Slav, Meran, Rabinovich variation
28815100-cd89-4027-a26e-f957aee3b1ea
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 8. Bd3 a6 9. e4 c5 10. e5 cxd4 11. Nxb5 Ng4 
Queen's Gambit Declined semi-Slav, Meran, Sozin variation
0b025c92-dbf9-449a-9b7e-0797e1f26abc
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 8. Bd3 a6 9. e4 c5 10. e5 cxd4 11. Nxb5 Nxe5 
Queen's Gambit Declined semi-Slav, Meran, Stahlberg variation
da5abe67-eff3-4805-a6ca-615ddecac810
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 8. Bd3 a6 9. e4 c5 10. e5 cxd4 11. Nxb5 Nxe5 12. Nxe5 axb5 13. Qf3
Queen's Gambit Declined semi-Slav, Meran, Sozin variation
68401cb6-7a06-442d-9b1b-23b58bff43cc
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 8. Bd3 a6 9. e4 c5 10. e5 cxd4 11. Nxb5 Nxe5 12. Nxe5 axb5 13. O-O
Queen's Gambit Declined semi-Slav, Meran, Rellstab attack
ed4d9c47-e190-49e6-92ab-801e6e5e16e3
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 8. Bd3 a6 9. e4 c5 10. e5 cxd4 11. Nxb5 Nxe5 12. Nxe5 axb5 13. O-O Qd5 14. Qe2 Ba6 15. Bg5
******D50: Queen's Gambit Declined, 4.Bg5
Queen's Gambit Declined, 4.Bg5
a8d032e1-6866-4b40-bf28-b30342ebecc1
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5
Queen's Gambit Declined, Been-Koomen variation
aea4c62a-a1e4-4820-9966-31cdb10ac5f1
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 c5 
Queen's Gambit Declined, Semi-Tarrasch, Krause variation
ab783533-2869-487e-b476-412e9f450b14
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 c5 5. Nf3 cxd4 6. Nxd4 e5 7. Ndb5 a6 8. Qa4
Queen's Gambit Declined, Semi-Tarrasch, Primitive Pillsbury variation
2fa01cb1-2ae4-497e-9ea9-503e799fa525
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 c5 5. Nf3 cxd4 6. Qxd4
Queen's Gambit Declined, Semi-Tarrasch
1f6f94d7-99d8-4820-85ba-92a268164b16
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 c5 5. cxd5
Queen's Gambit Declined, Canal (Venice) variation
c8fd7f94-154f-4735-be62-88b425e283f9
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 c5 5. cxd5 Qb6 
******D51: Queen's Gambit Declined, 4.Bg5 Nbd7
Queen's Gambit Declined, 4.Bg5 Nbd7
62d3c98e-a0aa-4d74-bd1f-a2212796ea53
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 
Queen's Gambit Declined, Rochlin variation
001f5607-1bd1-4783-a71c-d953d8cb3253
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. Nf3 c6 6. Rc1 Qa5 7. Bd2
Queen's Gambit Declined, Alekhine variation
445e0333-7823-4b00-a8d7-14ef6774b310
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. Nf3 c6 6. e4
Queen's Gambit Declined
ead607ec-88ad-4fe3-83ba-25efafaaf510
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. e3
Queen's Gambit Declined, Manhattan variation
48ae92a2-480d-4407-b3e3-1ba797a1fcb1
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. e3 Bb4 
Queen's Gambit Declined, 5...c6
f5f45893-f9ab-4dc4-9536-a59e96815db9
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. e3 c6 
Queen's Gambit Declined, Capablanca anti-Cambridge Springs variation
ff0421d5-a1ba-4b57-a2bf-dbc20ada082a
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. e3 c6 6. a3
******D52: Queen's Gambit Declined
Queen's Gambit Declined
f4e6718f-bd95-4ee8-a18e-9fd791f85a42
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. e3 c6 6. Nf3
Queen's Gambit Declined, Cambridge Springs defence
8b4afa89-f3fb-4822-afad-cd9217e083c7
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. e3 c6 6. Nf3 Qa5 
Queen's Gambit Declined, Cambridge Springs defence, Bogoljubow variation
680fefef-21e0-4ef7-933b-d36ef0772779
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. e3 c6 6. Nf3 Qa5 7. Nd2 Bb4 8. Qc2
Queen's Gambit Declined, Cambridge Springs defence, Argentine variation
3d2a588f-72bf-4785-a6d6-454e4367127b
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. e3 c6 6. Nf3 Qa5 7. Nd2 Bb4 8. Qc2 O-O 9. Bh4
Queen's Gambit Declined, Cambridge Springs defence, Rubinstein variation
dda5bd94-4977-491f-953c-473ed8984fee
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. e3 c6 6. Nf3 Qa5 7. Nd2 dxc4 
Queen's Gambit Declined, Cambridge Springs defence, Capablanca variation
f42d8e77-e1ba-40b1-bd9e-08944c4f22c3
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. e3 c6 6. Nf3 Qa5 7. Bxf6
Queen's Gambit Declined, Cambridge Springs defence, 7.cd
96725384-2f93-437f-956e-5de6a3b6d0e5
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. e3 c6 6. Nf3 Qa5 7. cxd5
Queen's Gambit Declined, Cambridge Springs defence, Yugoslav variation
cf9a3794-5129-4b0d-bfee-88b00698510f
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. e3 c6 6. Nf3 Qa5 7. cxd5 Nxd5 
******D53: Queen's Gambit Declined, 4.Bg5 Be7
Queen's Gambit Declined, 4.Bg5 Be7
fd7cb325-c832-4d08-8946-efd18d4b89a8
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 
Queen's Gambit Declined, Lasker variation
b7076242-0922-40b7-8d35-5d95b46b9d9d
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 Ne4 
Queen's Gambit Declined, 4.Bg5 Be7, 5.e3 O-O
7cd3ad5c-e07c-45e0-907b-02ec6d908d3c
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 
******D54: Queen's Gambit Declined, Anti-neo-orthodox variation
Queen's Gambit Declined, Anti-neo-orthodox variation
585fc01f-fd17-46e8-8bb7-32465c20c340
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Rc1
******D55: Queen's Gambit Declined, 6.Nf3
Queen's Gambit Declined, 6.Nf3
414945a0-0122-40b4-8357-437d3776c107
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3
Queen's Gambit Declined, Pillsbury attack
575c827e-9ec2-464a-be22-70d58c6c83e0
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 b6 7. Bd3 Bb7 8. cxd5 exd5 9. Ne5
Queen's Gambit Declined, Neo-orthodox variation
2a78051a-2f86-4658-b433-fcd212af378d
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 h6 
Queen's Gambit Declined, Neo-orthodox variation, 7.Bxf6
3dc3e719-9cfc-439c-8188-b0e182f6e1a5
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 h6 7. Bxf6
Queen's Gambit Declined, Petrosian variation
81eb50f9-d750-47fd-afb4-f6a1b5b2dce0
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 h6 7. Bxf6 Bxf6 8. Rc1 c6 9. Bd3 Nd7 10. O-O dxc4 11. Bxc4
Queen's Gambit Declined, Neo-orthodox variation, 7.Bh4
fa40e0af-a575-414e-bcf6-a28dcde94c63
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 h6 7. Bh4
******D56: Queen's Gambit Declined, Lasker defence
Queen's Gambit Declined, Lasker defence
2540b909-8fff-4f1f-a140-0716c3e2c487
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 h6 7. Bh4 Ne4 
Queen's Gambit Declined, Lasker defence, Teichmann variation
a1f90866-88f3-4e38-8ac5-7e2078cac858
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 h6 7. Bh4 Ne4 8. Bxe7 Qxe7 9. Qc2
Queen's Gambit Declined, Lasker defence, Russian variation
e16bcd2f-6dc4-4835-9785-eb1235e7a393
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 h6 7. Bh4 Ne4 8. Bxe7 Qxe7 9. Qc2 Nf6 10. Bd3 dxc4 11. Bxc4 c5 12. O-O Nc6 13. Rfd1 Bd7 
******D57: Queen's Gambit Declined, Lasker defence, main line
Queen's Gambit Declined, Lasker defence, main line
bf4c98e4-c250-4c9d-ac62-8dce8077e97e
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 h6 7. Bh4 Ne4 8. Bxe7 Qxe7 9. cxd5 Nxc3 10. bxc3
Queen's Gambit Declined, Lasker defence, Bernstein variation
226348a5-8309-4dba-9b6c-9df2e76901e2
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 h6 7. Bh4 Ne4 8. Bxe7 Qxe7 9. cxd5 Nxc3 10. bxc3 exd5 11. Qb3 Qd6 
******D58: Queen's Gambit Declined, Tartakower (Makagonov-Bondarevsky) system
Queen's Gambit Declined, Tartakower (Makagonov-Bondarevsky) system
8556f601-4c48-4660-ae16-9f752d904fab
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 h6 7. Bh4 b6 
******D59: Queen's Gambit Declined, Tartakower (Makagonov-Bondarevsky) system, 8.cd Nxd5
Queen's Gambit Declined, Tartakower (Makagonov-Bondarevsky) system, 8.cd Nxd5
4cd069c8-1c13-420b-9af9-d52984c8cc0a
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 h6 7. Bh4 b6 8. cxd5 Nxd5 
Queen's Gambit Declined, Tartakower variation
94acf5ee-9091-4102-a28b-1c19d02f7a9c
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 h6 7. Bh4 b6 8. cxd5 Nxd5 9. Bxe7 Qxe7 10. Nxd5 exd5 11. Rc1 Be6 
******D60: Queen's Gambit Declined, Orthodox defence
Queen's Gambit Declined, Orthodox defence
3c0c6919-37bb-4e48-9bbf-9cfebca7789c
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 
Queen's Gambit Declined, Orthodox defence, Botvinnik variation
d625ca69-1f82-45b9-b158-b6bdc6fa8f9e
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Bd3
Queen's Gambit Declined, Orthodox defence, Rauzer variation
42a8a860-c25c-4727-8d4d-3e1f824cf482
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Qb3
******D61: Queen's Gambit Declined, Orthodox defence, Rubinstein variation
Queen's Gambit Declined, Orthodox defence, Rubinstein variation
c808a88f-4bb5-423d-bbd0-eb5a3fb4b6c8
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Qc2
******D62: Queen's Gambit Declined, Orthodox defence, 7.Qc2 c5, 8.cd (Rubinstein)
Queen's Gambit Declined, Orthodox defence, 7.Qc2 c5, 8.cd (Rubinstein)
b0428991-5b6a-407f-a60f-543568d3b378
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Qc2 c5 8. cxd5
******D63: Queen's Gambit Declined, Orthodox defence, 7.Rc1
Queen's Gambit Declined, Orthodox defence, 7.Rc1
d95bdb70-3252-4e4b-b7a4-491d6ec11db4
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1
Queen's Gambit Declined, Orthodox defence, Pillsbury attack
0af5fb7a-2d5e-4b9b-af9e-75eb63cda89e
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 b6 8. cxd5 exd5 9. Bd3
Queen's Gambit Declined, Orthodox defence, Capablanca variation
892f04ab-277b-4c82-919e-02c92fa2eaeb
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 b6 8. cxd5 exd5 9. Bb5
Queen's Gambit Declined, Orthodox defence, Swiss (Henneberger) variation
2f604edd-861f-49ff-b123-fbcb4191b475
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 a6 
Queen's Gambit Declined, Orthodox defence, Swiss, Karlsbad variation
47a1232e-316c-4d44-8bc2-9902a991070e
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 a6 8. cxd5
Queen's Gambit Declined, Orthodox defence
6a75617b-14ae-4071-8a3e-5db966dccecf
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 
******D64: Queen's Gambit Declined, Orthodox defence, Rubinstein attack (with Rc1)
Queen's Gambit Declined, Orthodox defence, Rubinstein attack (with Rc1)
6b275e63-b334-437c-bebc-b6f88e4b47ab
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Qc2
Queen's Gambit Declined, Orthodox defence, Rubinstein attack, Wolf variation
085f6835-33f3-469b-a351-2c81a1969953
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Qc2 Ne4 
Queen's Gambit Declined, Orthodox defence, Rubinstein attack, Karlsbad variation
5abda6dc-3d8a-4122-b894-205af57743c6
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Qc2 a6 
Queen's Gambit Declined, Orthodox defence, Rubinstein attack, Gruenfeld variation
4099ca87-8976-44cd-8b8b-c983cd52a7a5
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Qc2 a6 9. a3
******D65: Queen's Gambit Declined, Orthodox defence, Rubinstein attack, main line
Queen's Gambit Declined, Orthodox defence, Rubinstein attack, main line
e0de0331-522f-456b-9170-6880c590e3d0
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Qc2 a6 9. cxd5
******D66: Queen's Gambit Declined, Orthodox defence, Bd3 line
Queen's Gambit Declined, Orthodox defence, Bd3 line
d5a98cb9-503b-4a9a-a264-ac408f9b3f70
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Bd3
Queen's Gambit Declined, Orthodox defence, Bd3 line, fianchetto variation
a6b48e24-06a5-4c3a-990e-4dab8e7891c0
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Bd3 dxc4 9. Bxc4 b5 
******D67: Queen's Gambit Declined, Orthodox defence, Bd3 line, Capablanca freeing manoevre
Queen's Gambit Declined, Orthodox defence, Bd3 line, Capablanca freeing manoevre
c27f2610-547e-404b-b98c-c324e9f7b391
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Bd3 dxc4 9. Bxc4 Nd5 
Queen's Gambit Declined, Orthodox defence, Bd3 line, Janowski variation
c052f906-743a-47be-8006-1566ae4c9aa6
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Bd3 dxc4 9. Bxc4 Nd5 10. h4
Queen's Gambit Declined, Orthodox defence, Bd3 line
3f4743db-6cef-43eb-8db9-d5724006ffb9
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Bd3 dxc4 9. Bxc4 Nd5 10. Bxe7 Qxe7 
Queen's Gambit Declined, Orthodox defence, Bd3 line, Alekhine variation
c456cac4-85e2-4155-8c9a-17917d35d17b
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Bd3 dxc4 9. Bxc4 Nd5 10. Bxe7 Qxe7 11. Ne4
Queen's Gambit Declined, Orthodox defence, Bd3 line, 11.O-O
20f6794e-2455-46fd-a32d-0dc7a5ab3ec6
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Bd3 dxc4 9. Bxc4 Nd5 10. Bxe7 Qxe7 11. O-O
******D68: Queen's Gambit Declined, Orthodox defence, classical variation
Queen's Gambit Declined, Orthodox defence, classical variation
f5e28bd8-7cbf-4097-bc2b-7de5cb972d4f
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Bd3 dxc4 9. Bxc4 Nd5 10. Bxe7 Qxe7 11. O-O Nxc3 12. Rxc3 e5 
Queen's Gambit Declined, Orthodox defence, classical, 13.d1b1 (Maroczy)
3e3bf400-7a71-4576-a6fa-1c1b8af90a9c
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Bd3 dxc4 9. Bxc4 Nd5 10. Bxe7 Qxe7 11. O-O Nxc3 12. Rxc3 e5 13. Qb1
Queen's Gambit Declined, Orthodox defence, classical, 13.d1c2 (Vidmar)
3005314c-4376-47e5-b3a2-9afd7b3ffff4
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Bd3 dxc4 9. Bxc4 Nd5 10. Bxe7 Qxe7 11. O-O Nxc3 12. Rxc3 e5 13. Qc2
******D69: Queen's Gambit Declined, Orthodox defence, classical, 13.de
Queen's Gambit Declined, Orthodox defence, classical, 13.de
89baa73b-8c25-4b37-8339-153de3cbd8ce
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Bd3 dxc4 9. Bxc4 Nd5 10. Bxe7 Qxe7 11. O-O Nxc3 12. Rxc3 e5 13. dxe5 Nxe5 14. Nxe5 Qxe5 
******D70: Neo-Gruenfeld defence
Neo-Gruenfeld defence
89a49ac2-8858-44dd-86da-87832c10851b
1. d4 Nf6 2. c4 g6 3. f3 d5 
Neo-Gruenfeld (Kemeri) defence
afb2be83-228b-4778-b1f4-3b13e6e48a66
1. d4 Nf6 2. c4 g6 3. g3 d5 
******D71: Neo-Gruenfeld, 5.cd
Neo-Gruenfeld, 5.cd
fb520a51-8683-4756-8251-59a75eafc106
1. d4 Nf6 2. c4 g6 3. g3 d5 4. Bg2 Bg7 5. cxd5 Nxd5 
******D72: Neo-Gruenfeld, 5.cd, main line
Neo-Gruenfeld, 5.cd, main line
15dd70e3-9517-4631-b85c-d13d961ffde2
1. d4 Nf6 2. c4 g6 3. g3 d5 4. Bg2 Bg7 5. cxd5 Nxd5 6. e4 Nb6 7. Ne2
******D73: Neo-Gruenfeld, 5.Nf3
Neo-Gruenfeld, 5.Nf3
3c58055a-5deb-4acf-8b3d-c950edf33d68
1. d4 Nf6 2. c4 g6 3. g3 d5 4. Bg2 Bg7 5. Nf3
******D74: Neo-Gruenfeld, 6.cd Nxd5, 7.O-O
Neo-Gruenfeld, 6.cd Nxd5, 7.O-O
41fb63b4-31cb-435c-a1ff-16ea1e31286e
1. d4 Nf6 2. c4 g6 3. g3 d5 4. Bg2 Bg7 5. Nf3 O-O 6. cxd5 Nxd5 7. O-O
******D75: Neo-Gruenfeld, 6.cd Nxd5, 7.O-O c5, 8.Nc3
Neo-Gruenfeld, 6.cd Nxd5, 7.O-O c5, 8.Nc3
a9e88d9e-eecf-4947-a70f-116318ea821b
1. d4 Nf6 2. c4 g6 3. g3 d5 4. Bg2 Bg7 5. Nf3 O-O 6. cxd5 Nxd5 7. O-O c5 8. Nc3
Neo-Gruenfeld, 6.cd Nxd5, 7.O-O c5, 8.dc
527420bf-6e61-4872-b7ad-855a0d4ebfae
1. d4 Nf6 2. c4 g6 3. g3 d5 4. Bg2 Bg7 5. Nf3 O-O 6. cxd5 Nxd5 7. O-O c5 8. dxc5
******D76: Neo-Gruenfeld, 6.cd Nxd5, 7.O-O Nb6
Neo-Gruenfeld, 6.cd Nxd5, 7.O-O Nb6
8fdd8b05-bf8e-4dfc-84ac-679bfde1125b
1. d4 Nf6 2. c4 g6 3. g3 d5 4. Bg2 Bg7 5. Nf3 O-O 6. cxd5 Nxd5 7. O-O Nb6 
******D77: Neo-Gruenfeld, 6.O-O
Neo-Gruenfeld, 6.O-O
9448728f-d3eb-467c-a837-a225191fc102
1. d4 Nf6 2. c4 g6 3. g3 d5 4. Bg2 Bg7 5. Nf3 O-O 6. O-O
******D78: Neo-Gruenfeld, 6.O-O c6
Neo-Gruenfeld, 6.O-O c6
89585f17-09b0-4f99-b461-2003c5e6522e
1. d4 Nf6 2. c4 g6 3. g3 d5 4. Bg2 Bg7 5. Nf3 O-O 6. O-O c6 
******D79: Neo-Gruenfeld, 6.O-O, main line
Neo-Gruenfeld, 6.O-O, main line
63a42260-4ebf-438e-8232-48a33e696162
1. d4 Nf6 2. c4 g6 3. g3 d5 4. Bg2 Bg7 5. Nf3 O-O 6. O-O c6 7. cxd5 cxd5 
******D80: Gruenfeld defence
Gruenfeld defence
f74fa565-7d48-4767-8cc0-6b37f45c724a
1. d4 Nf6 2. c4 g6 3. Nc3 d5 
Gruenfeld, Spike gambit
1f9afbcb-2e3b-4293-b02a-518dc1957e37
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. g4
Gruenfeld, Stockholm variation
de982c84-192e-4915-9cc9-edd73148c72f
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Bg5
Gruenfeld, Lundin variation
a1a048ac-9fb2-4713-9d5b-8db03626a350
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Bg5 Ne4 5. Nxe4 dxe4 6. Qd2 c5 
******D81: Gruenfeld, Russian variation
Gruenfeld, Russian variation
35a9f091-9d69-48c7-8e02-304b91ec88b1
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Qb3
******D82: Gruenfeld, 4.Bf4
Gruenfeld, 4.Bf4
18c28593-80fc-4a07-9aa3-0b78628c1c5d
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Bf4
******D83: Gruenfeld, Gruenfeld gambit
Gruenfeld, Gruenfeld gambit
c9305b0b-afb7-4ef2-a9b3-53230a37d0c5
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Bf4 Bg7 5. e3 O-O 
Gruenfeld, Gruenfeld gambit, Capablanca variation
519b1036-ef85-4fc5-b14c-0d4c329491cb
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Bf4 Bg7 5. e3 O-O 6. Rc1
Gruenfeld, Gruenfeld gambit, Botvinnik variation
03fd394f-8e90-47ac-a4b4-3664133c05a4
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Bf4 Bg7 5. e3 O-O 6. Rc1 c5 7. dxc5 Be6 
******D84: Gruenfeld, Gruenfeld gambit accepted
Gruenfeld, Gruenfeld gambit accepted
75e01c5d-1d6f-40cc-8a49-fc62907a60d8
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Bf4 Bg7 5. e3 O-O 6. cxd5 Nxd5 7. Nxd5 Qxd5 8. Bxc7
******D85: Gruenfeld, exchange variation
Gruenfeld, exchange variation
a69edd57-a23a-477c-aec2-8c33e37ae374
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. cxd5 Nxd5 
Gruenfeld, modern exchange variation
4a566e11-91e7-4765-8efc-bbd9e27c5dd5
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. cxd5 Nxd5 5. e4 Nxc3 6. bxc3 Bg7 7. Nf3
******D86: Gruenfeld, exchange, classical variation
Gruenfeld, exchange, classical variation
42c0fb14-bcb3-4f5a-bb0f-8d7145504a02
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. cxd5 Nxd5 5. e4 Nxc3 6. bxc3 Bg7 7. Bc4
Gruenfeld, exchange, Larsen variation
2fe8315d-983f-404a-9144-429be35ed32c
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. cxd5 Nxd5 5. e4 Nxc3 6. bxc3 Bg7 7. Bc4 O-O 8. Ne2 Qd7 9. O-O b6 
Gruenfeld, exchange, Simagin's lesser variation
f81912a7-867f-41a2-9709-36ecab11e2f6
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. cxd5 Nxd5 5. e4 Nxc3 6. bxc3 Bg7 7. Bc4 O-O 8. Ne2 b6 
Gruenfeld, exchange, Simagin's improved variation
517d4ee9-047e-41df-a145-a07c1858e903
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. cxd5 Nxd5 5. e4 Nxc3 6. bxc3 Bg7 7. Bc4 O-O 8. Ne2 Nc6 
******D87: Gruenfeld, exchange, Spassky variation
Gruenfeld, exchange, Spassky variation
2ababaa3-ae5a-4f20-b41c-b03d08d23536
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. cxd5 Nxd5 5. e4 Nxc3 6. bxc3 Bg7 7. Bc4 O-O 8. Ne2 c5 
Gruenfeld, exchange, Seville variation
94e410af-faf2-4d7d-a93d-41eac78c3c91
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. cxd5 Nxd5 5. e4 Nxc3 6. bxc3 Bg7 7. Bc4 O-O 8. Ne2 c5 9. O-O Nc6 10. Be3 Bg4 11. f3 Na5 12. Bxf7+
******D88: Gruenfeld, Spassky variation, main line, 10...cd, 11.cd
Gruenfeld, Spassky variation, main line, 10...cd, 11.cd
bd7160a8-e406-4edf-937c-f7276195090c
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. cxd5 Nxd5 5. e4 Nxc3 6. bxc3 Bg7 7. Bc4 O-O 8. Ne2 c5 9. O-O Nc6 10. Be3 cxd4 11. cxd4
******D89: Gruenfeld, Spassky variation, main line, 13.Bd3
Gruenfeld, Spassky variation, main line, 13.Bd3
0e063ceb-35ad-49e8-8026-4e6de212cc86
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. cxd5 Nxd5 5. e4 Nxc3 6. bxc3 Bg7 7. Bc4 O-O 8. Ne2 c5 9. O-O Nc6 10. Be3 cxd4 11. cxd4 Bg4 12. f3 Na5 13. Bd3 Be6 
Gruenfeld, exchange, Sokolsky variation
cf74ffc3-c2df-41b3-8e28-43cd416606f9
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. cxd5 Nxd5 5. e4 Nxc3 6. bxc3 Bg7 7. Bc4 O-O 8. Ne2 c5 9. O-O Nc6 10. Be3 cxd4 11. cxd4 Bg4 12. f3 Na5 13. Bd3 Be6 14. d5
******D90: Gruenfeld, Three knights variation
Gruenfeld, Three knights variation
c8bd7fe8-344f-46eb-a371-c7b2c4b15c23
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3
Gruenfeld, Schlechter variation
ccf135fd-177b-4c7d-b78c-458ab8e33fca
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 c6 
Gruenfeld, Three knights variation
51183b6c-252e-486d-a66d-981dbf4fc77f
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 
Gruenfeld, Flohr variation
38724ffa-85bb-4aec-980a-b9d5b374b28c
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Qa4+
******D91: Gruenfeld, 5.Bg5
Gruenfeld, 5.Bg5
81eb765f-9668-4870-bd56-44d6b6475f8c
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Bg5
******D92: Gruenfeld, 5.Bf4
Gruenfeld, 5.Bf4
a2e70e26-6ec4-490a-9e40-3aa69b9eeece
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Bf4
******D93: Gruenfeld with Bf4    e3
Gruenfeld with Bf4    e3
9aecd0a1-bc49-45d6-9842-a26523121874
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Bf4 O-O 6. e3
******D94: Gruenfeld, 5.e3
Gruenfeld, 5.e3
5f2233c4-d7a6-4eeb-902a-5f03de54c909
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. e3
Gruenfeld, Makogonov variation
ec14aabd-577a-443c-bf03-b95f99f457c6
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. e3 O-O 6. b4
Gruenfeld, Opovcensky variation
0050839e-7065-47ce-84b8-cb44bb06e091
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. e3 O-O 6. Bd2
Gruenfeld with e3    Bd3
f7110c33-c4c5-470b-8533-22d3dd8c11b0
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. e3 O-O 6. Bd3
Gruenfeld, Smyslov defence
5099b340-4f39-4c48-a09b-0b2a204945ce
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. e3 O-O 6. Bd3 c6 7. O-O Bg4 
Gruenfeld, Flohr defence
60e3cba8-6061-44c9-a0d6-f37a6ab5aeed
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. e3 O-O 6. Bd3 c6 7. O-O Bf5 
******D95: Gruenfeld with e3 & Qb3
Gruenfeld with e3 & Qb3
ec3a582f-e458-4095-9d2d-ab3af2c50ba6
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. e3 O-O 6. Qb3
Gruenfeld, Botvinnik variation
a68efbbf-2ec2-4f18-bc40-0973f39d741a
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. e3 O-O 6. Qb3 e6 
Gruenfeld, Pachman variation
28f1ffad-aa93-411f-b645-8524ff4a8c23
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. e3 O-O 6. Qb3 dxc4 7. Bxc4 Nbd7 8. Ng5
******D96: Gruenfeld, Russian variation
Gruenfeld, Russian variation
93695989-f7da-4d13-896c-8170ab553aa6
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Qb3
******D97: Gruenfeld, Russian variation with e4
Gruenfeld, Russian variation with e4
03ad15c6-dccc-4697-bab9-6cb243a117a1
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Qb3 dxc4 6. Qxc4 O-O 7. e4
Gruenfeld, Russian, Alekhine (Hungarian) variation
7657dc71-5b10-4c16-88cc-2e065697dbed
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Qb3 dxc4 6. Qxc4 O-O 7. e4 a6 
Gruenfeld, Russian, Szabo (Boleslavsky) variation
ce677b9d-2e03-4953-b820-a1ce58cbd2cd
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Qb3 dxc4 6. Qxc4 O-O 7. e4 c6 
Gruenfeld, Russian, Levenfish variation
313a17b1-d38b-4ae7-8d55-60f84dc4f0f0
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Qb3 dxc4 6. Qxc4 O-O 7. e4 b6 
Gruenfeld, Russian, Byrne (Simagin) variation
e973271c-28c9-4297-87db-80cb65220aac
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Qb3 dxc4 6. Qxc4 O-O 7. e4 Nc6 
Gruenfeld, Russian, Prins variation
63356d34-4151-4651-ad5f-4b910057f7dc
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Qb3 dxc4 6. Qxc4 O-O 7. e4 Na6 
******D98: Gruenfeld, Russian, Smyslov variation
Gruenfeld, Russian, Smyslov variation
b454c44e-0525-47ce-a272-144347f9e2be
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Qb3 dxc4 6. Qxc4 O-O 7. e4 Bg4 
Gruenfeld, Russian, Keres variation
c0a4c337-6aa5-4b6c-b39d-7fb653f21edd
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Qb3 dxc4 6. Qxc4 O-O 7. e4 Bg4 8. Be3 Nfd7 9. Be2 Nb6 10. Qd3 Nc6 11. O-O-O
******D99: Gruenfeld defence, Smyslov, main line
Gruenfeld defence, Smyslov, main line
f3caa860-01ac-424b-9c70-719f873a8e39
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Qb3 dxc4 6. Qxc4 O-O 7. e4 Bg4 8. Be3 Nfd7 9. Qb3
Gruenfeld defence, Smyslov, Yugoslav variation
aa480566-d055-4e6f-87f5-d0f9f67283d7
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Qb3 dxc4 6. Qxc4 O-O 7. e4 Bg4 8. Be3 Nfd7 9. Qb3 c5 
******E00: Queen's pawn game
Queen's pawn game
6665dfe1-2411-4bb1-8612-58f836f99a82
1. d4 Nf6 2. c4 e6 
Neo-Indian (Seirawan) attack
2347c020-ea87-4ce4-b45d-0ab52fd4f2ec
1. d4 Nf6 2. c4 e6 3. Bg5
Catalan opening
c204ad80-3719-4464-a633-e9b3f6dc2081
1. d4 Nf6 2. c4 e6 3. g3
******E01: Catalan, closed
Catalan, closed
cf7a962c-ef3b-4d5a-9b20-77da3c96d3f3
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2
******E02: Catalan, open, 5.Qa4
Catalan, open, 5.Qa4
39ff183e-840f-4a61-b4e2-82fa8a030e92
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 dxc4 5. Qa4+
******E03: Catalan, open, Alekhine variation
Catalan, open, Alekhine variation
f779df9b-692e-4352-8520-d7fb5a00318e
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 dxc4 5. Qa4+ Nbd7 6. Qxc4 a6 7. Qc2
Catalan, open, 5.Qa4 Nbd7, 6.Qxc4
9258376b-5d4f-4676-89ba-3fc11add5281
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 dxc4 5. Qa4+ Nbd7 6. Qxc4
******E04: Catalan, open, 5.Nf3
Catalan, open, 5.Nf3
11ebc6ea-4a01-4e4a-a004-975b5f339fee
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 dxc4 5. Nf3
******E05: Catalan, open, classical line
Catalan, open, classical line
57969219-1c7c-4f6c-80ae-5e714efc1e06
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 dxc4 5. Nf3 Be7 
******E06: Catalan, closed, 5.Nf3
Catalan, closed, 5.Nf3
4d8cf486-4c8f-428a-ae20-86be840f299a
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 Be7 5. Nf3
******E07: Catalan, closed, 6...Nbd7
Catalan, closed, 6...Nbd7
7d5a3a8e-f409-441f-9a98-ee508d77774e
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 Be7 5. Nf3 O-O 6. O-O Nbd7 
Catalan, closed, Botvinnik variation
e5c27147-e6c0-45f9-8e49-d02c9d22345c
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 Be7 5. Nf3 O-O 6. O-O Nbd7 7. Nc3 c6 8. Qd3
******E08: Catalan, closed, 7.Qc2
Catalan, closed, 7.Qc2
7e3ac9d7-d9ec-49b1-abf9-4388bfb71272
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 Be7 5. Nf3 O-O 6. O-O Nbd7 7. Qc2
Catalan, closed, Zagoryansky variation
f8ae493e-633c-4280-8acc-21a4e58840ac
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 Be7 5. Nf3 O-O 6. O-O Nbd7 7. Qc2 c6 8. Rd1 b6 9. a4
Catalan, closed, Qc2 & b3
c1037226-68a1-40ed-bb05-d9992ef761f5
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 Be7 5. Nf3 O-O 6. O-O Nbd7 7. Qc2 c6 8. b3
Catalan, closed, Spassky gambit
6c17f364-0958-4b62-9290-887dfb74bff2
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 Be7 5. Nf3 O-O 6. O-O Nbd7 7. Qc2 c6 8. b3 b6 9. Rd1 Bb7 10. Nc3 b5 
******E09: Catalan, closed, main line
Catalan, closed, main line
cbfb1765-ffa9-48ed-acaf-f243011c97f4
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 Be7 5. Nf3 O-O 6. O-O Nbd7 7. Qc2 c6 8. Nbd2
Catalan, closed, Sokolsky variation
0fc215c3-930a-4dff-b95a-d67a6811361d
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 Be7 5. Nf3 O-O 6. O-O Nbd7 7. Qc2 c6 8. Nbd2 b6 9. b3 a5 10. Bb2 Ba6 
******E10: Queen's pawn game
Queen's pawn game
1b646f91-fa28-4de6-b7af-ab2151bac191
1. d4 Nf6 2. c4 e6 3. Nf3
Blumenfeld counter-gambit
29954688-7bab-4899-b04e-4fea782423b2
1. d4 Nf6 2. c4 e6 3. Nf3 c5 4. d5 b5 
Blumenfeld counter-gambit accepted
4b42dac7-a0c5-4605-a2e3-5880571120f9
1. d4 Nf6 2. c4 e6 3. Nf3 c5 4. d5 b5 5. dxe6 fxe6 6. cxb5 d5 
Blumenfeld counter-gambit, Dus-Chotimursky variation
50ae71b9-be58-44e1-9e76-611d7da1b5d0
1. d4 Nf6 2. c4 e6 3. Nf3 c5 4. d5 b5 5. Bg5
Blumenfeld counter-gambit, Spielmann variation
9162618b-050f-4b1a-8958-1b62c383a8d8
1. d4 Nf6 2. c4 e6 3. Nf3 c5 4. d5 b5 5. Bg5 exd5 6. cxd5 h6 
Dzindzikhashvili defence
dba9ee05-ed6f-4e78-ab24-2ac4023919ea
1. d4 Nf6 2. c4 e6 3. Nf3 a6 
Doery defence
354068e5-f8fe-45b9-a355-c0070abb220b
1. d4 Nf6 2. c4 e6 3. Nf3 Ne4 
******E11: Bogo-Indian defence
Bogo-Indian defence
65141d30-f53a-46af-aee2-d4caacabb890
1. d4 Nf6 2. c4 e6 3. Nf3 Bb4+ 
Bogo-Indian defence, Gruenfeld variation
772ba452-bec5-40c2-8c40-45fa82a7e9bf
1. d4 Nf6 2. c4 e6 3. Nf3 Bb4+ 4. Nbd2
Bogo-Indian defence, Nimzovich variation
b1fd5563-3512-41fa-871f-2707b47cd8ca
1. d4 Nf6 2. c4 e6 3. Nf3 Bb4+ 4. Bd2 Qe7 
Bogo-Indian defence, Monticelli trap
f6537c81-ad83-4ff3-86c4-5d9b344ff27e
1. d4 Nf6 2. c4 e6 3. Nf3 Bb4+ 4. Bd2 Bxd2+ 5. Qxd2 b6 6. g3 Bb7 7. Bg2 O-O 8. Nc3 Ne4 9. Qc2 Nxc3 10. Ng5
******E12: Queen's Indian defence
Queen's Indian defence
cce839c5-ce3c-43ca-8c36-ec43ef234edf
1. d4 Nf6 2. c4 e6 3. Nf3 b6 
Queen's Indian, Miles variation
a81282b5-86cd-4e81-8e49-9b4504bfa59e
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. Bf4
Queen's Indian, Petrosian system
3f849284-a21e-4a50-8f1f-5bddef5658ba
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. a3
Queen's Indian, 4.Nc3
96abdbdf-6ccd-4beb-89af-73e4bdf0ccc9
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. Nc3
Queen's Indian, 4.Nc3, Botvinnik variation
8d3daa74-e59e-40e9-9707-ce1d9d763c99
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. Nc3 Bb7 5. Bg5 h6 6. Bh4 g5 7. Bg3 Nh5 
******E13: Queen's Indian, 4.Nc3, main line
Queen's Indian, 4.Nc3, main line
1dd84d24-4d05-4a42-b5a5-3c887b465c40
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. Nc3 Bb7 5. Bg5 h6 6. Bh4 Bb4 
******E14: Queen's Indian, 4.e3
Queen's Indian, 4.e3
b91f9bb4-0a18-4271-a27f-e71577c24001
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. e3
Queen's Indian, Averbakh variation
563902eb-4d8e-44f3-b1d1-a23a4c6622c4
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. e3 Bb7 5. Bd3 c5 6. O-O Be7 7. b3 O-O 8. Bb2 cxd4 9. Nxd4
******E15: Queen's Indian, 4.g3
Queen's Indian, 4.g3
6fec4e61-063d-4961-b8e9-b27be68e98eb
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3
Queen's Indian, Nimzovich variation (exaggerated fianchetto)
dad517cb-82e4-41b5-91b2-3af3e5983613
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Ba6 
Queen's Indian, 4.g3 Bb7
970e4c26-3663-4f00-8fb2-8019c8e451f1
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Bb7 
Queen's Indian, Rubinstein variation
3d2634c5-e6ad-4978-bf4b-0cc035f536a9
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Bb7 5. Bg2 c5 6. d5 exd5 7. Nh4
Queen's Indian, Buerger variation
5030a2df-d112-43df-8776-7ca5fc040fa5
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Bb7 5. Bg2 c5 6. d5 exd5 7. Ng5
******E16: Queen's Indian, Capablanca variation
Queen's Indian, Capablanca variation
c103183b-bc55-4fe7-8c0c-b38c8f2fc0a2
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Bb7 5. Bg2 Bb4+ 
Queen's Indian, Yates variation
6f15e9d2-132d-4491-9a02-76e08c900aa3
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Bb7 5. Bg2 Bb4+ 6. Bd2 a5 
Queen's Indian, Riumin variation
3739deb8-1be3-4d9c-aafe-23a4020067ee
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Bb7 5. Bg2 Bb4+ 6. Bd2 Be7 
******E17: Queen's Indian, 5.Bg2 Be7
Queen's Indian, 5.Bg2 Be7
1fbbc6b7-ba23-49c1-a448-cf552a6e4867
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Bb7 5. Bg2 Be7 
Queen's Indian, anti-Queen's Indian system
28582e09-95c0-4883-8e88-7dfee405e65a
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Bb7 5. Bg2 Be7 6. Nc3
Queen's Indian, Opovcensky variation
f35005d4-b795-4a76-9d16-c8277089f9b8
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Bb7 5. Bg2 Be7 6. Nc3 Ne4 7. Bd2
Queen's Indian, old main line, 6.O-O
920e3673-80d2-4c20-8474-01fd013e7a97
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Bb7 5. Bg2 Be7 6. O-O
Queen's Indian, Euwe variation
32aab761-c9af-4172-a343-173239dd18a5
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Bb7 5. Bg2 Be7 6. O-O O-O 7. b3
******E18: Queen's Indian, old main line, 7.Nc3
Queen's Indian, old main line, 7.Nc3
1cf96658-4749-4703-a82d-2dee6c70d9e7
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Bb7 5. Bg2 Be7 6. O-O O-O 7. Nc3
******E19: Queen's Indian, old main line, 9.Qxc3
Queen's Indian, old main line, 9.Qxc3
20c5ca0a-6ee5-4d36-a27e-508bcbd8fea1
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Bb7 5. Bg2 Be7 6. O-O O-O 7. Nc3 Ne4 8. Qc2 Nxc3 9. Qxc3
******E20: Nimzo-Indian defence
Nimzo-Indian defence
fdc84dc5-e743-4361-ba2c-2a67174eb235
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 
Nimzo-Indian, Kmoch variation
8beca8f7-4347-456e-9ef1-dcae7a59bc5e
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. f3
Nimzo-Indian, Mikenas attack
bc34d16c-7061-43b3-8d8e-da67f7a87f30
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qd3
Nimzo-Indian, Romanishin-Kasparov (Steiner) system
9881af96-bd54-4e65-b135-20587a6a39a3
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. g3
******E21: Nimzo-Indian, three knights variation
Nimzo-Indian, three knights variation
0bd44a9c-ef67-47c8-8179-ee1144c977da
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Nf3
Nimzo-Indian, three knights, Korchnoi variation
f1c18728-c51e-40fd-bfcb-39f896a086cd
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Nf3 c5 5. d5
Nimzo-Indian, three knights, Euwe variation
996f241e-415e-4675-8326-12f4e4aa3b71
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Nf3 c5 5. d5 Ne4 
******E22: Nimzo-Indian, Spielmann variation
Nimzo-Indian, Spielmann variation
1982e32a-dec2-4b25-9b3b-3d422077bdf1
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qb3
******E23: Nimzo-Indian, Spielmann, 4...c5, 5.dc Nc6
Nimzo-Indian, Spielmann, 4...c5, 5.dc Nc6
2250efe0-c38e-4866-8bc1-82b98b999eef
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qb3 c5 5. dxc5 Nc6 
Nimzo-Indian, Spielmann, Karlsbad variation
c0affa47-49a4-40b9-9684-437d42ace520
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qb3 c5 5. dxc5 Nc6 6. Nf3 Ne4 7. Bd2 Nxd2 
Nimzo-Indian, Spielmann, San Remo variation
6aae592f-47f5-4743-9f62-f5a74c2866e3
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qb3 c5 5. dxc5 Nc6 6. Nf3 Ne4 7. Bd2 Nxc5 
Nimzo-Indian, Spielmann, Staahlberg variation
3c70621e-998a-45eb-82ae-17515cd0b73a
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qb3 c5 5. dxc5 Nc6 6. Nf3 Ne4 7. Bd2 Nxc5 8. Qc2 f5 9. g3
******E24: Nimzo-Indian, Saemisch variation
Nimzo-Indian, Saemisch variation
ace5f5e4-f189-4512-853f-7b30b6cb44d9
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. a3 Bxc3+ 5. bxc3
Nimzo-Indian, Saemisch, Botvinnik variation
1fbadb31-a1ad-4378-ad3b-5aa3110d1f06
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. a3 Bxc3+ 5. bxc3 c5 6. f3 d5 7. e3 O-O 8. cxd5 Nxd5 
******E25: Nimzo-Indian, Saemisch variation
Nimzo-Indian, Saemisch variation
c3d2d55a-8d01-4ca5-bdcb-ebcb5285b781
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. a3 Bxc3+ 5. bxc3 c5 6. f3 d5 7. cxd5
Nimzo-Indian, Saemisch, Keres variation
6a8e979e-5052-443b-a674-d39a3b66c449
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. a3 Bxc3+ 5. bxc3 c5 6. f3 d5 7. cxd5 Nxd5 8. dxc5
Nimzo-Indian, Saemisch, Romanovsky variation
eabc12e5-9af7-4c21-b111-402fe2f4f5ec
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. a3 Bxc3+ 5. bxc3 c5 6. f3 d5 7. cxd5 Nxd5 8. dxc5 f5 
******E26: Nimzo-Indian, Saemisch variation
Nimzo-Indian, Saemisch variation
d5c784bc-a9f2-42b4-9667-27043555110c
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. a3 Bxc3+ 5. bxc3 c5 6. e3
Nimzo-Indian, Saemisch, O'Kelly variation
e05509cd-f263-4cf5-b844-6900f3b956c8
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. a3 Bxc3+ 5. bxc3 c5 6. e3 b6 
******E27: Nimzo-Indian, Saemisch variation
Nimzo-Indian, Saemisch variation
2b6a9f35-55e9-47a6-b4e0-3c2c2ac9b612
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. a3 Bxc3+ 5. bxc3 O-O 
******E28: Nimzo-Indian, Saemisch variation
Nimzo-Indian, Saemisch variation
718fc513-005b-4e1a-b434-a4e5d635cb32
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. a3 Bxc3+ 5. bxc3 O-O 6. e3
******E29: Nimzo-Indian, Saemisch, main line
Nimzo-Indian, Saemisch, main line
e2aa684d-4815-43f7-9a4b-d666d947989e
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. a3 Bxc3+ 5. bxc3 O-O 6. e3 c5 7. Bd3 Nc6 
Nimzo-Indian, Saemisch, Capablanca variation
56e98e01-ad3a-4a46-9bdc-5f1478bb4f88
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. a3 Bxc3+ 5. bxc3 O-O 6. e3 c5 7. Bd3 Nc6 8. Ne2 b6 9. e4 Ne8 
******E30: Nimzo-Indian, Leningrad variation
Nimzo-Indian, Leningrad variation
a9d30200-58a9-4561-bb44-5d5190505700
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Bg5
Nimzo-Indian, Leningrad, ...b5 gambit
1d7997b9-137c-4a2d-b27e-2dbdba8a1955
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Bg5 h6 5. Bh4 c5 6. d5 b5 
******E31: Nimzo-Indian, Leningrad, main line
Nimzo-Indian, Leningrad, main line
a1433d9a-b953-45b3-8a22-d42d0faa6c9c
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Bg5 h6 5. Bh4 c5 6. d5 d6 
******E32: Nimzo-Indian, classical variation
Nimzo-Indian, classical variation
3955ddcc-6387-4d87-bc3a-9d9776d0cf99
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2
Nimzo-Indian, classical, Adorjan gambit
b591e85b-a940-4a93-be36-040aaff266c1
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2 O-O 5. a3 Bxc3+ 6. Qxc3 b5 
******E33: Nimzo-Indian, classical, 4...Nc6
Nimzo-Indian, classical, 4...Nc6
19a3b8c2-f398-4496-b666-944e93962589
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2 Nc6 
Nimzo-Indian, classical, Milner-Barry (Zurich) variation
10e87b48-6693-4365-be7f-8a8122079d42
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2 Nc6 5. Nf3 d6 
******E34: Nimzo-Indian, classical, Noa variation
Nimzo-Indian, classical, Noa variation
ac6bfe4d-00ad-4745-83ac-ef06f151401f
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2 d5 
******E35: Nimzo-Indian, classical, Noa variation, 5.cd ed
Nimzo-Indian, classical, Noa variation, 5.cd ed
87bafbf5-c065-4c88-b86c-171123a2e017
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2 d5 5. cxd5 exd5 
******E36: Nimzo-Indian, classical, Noa variation, 5.a3
Nimzo-Indian, classical, Noa variation, 5.a3
10491dcc-d6ab-4e38-bf13-12884075dd39
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2 d5 5. a3
Nimzo-Indian, classical, Botvinnik variation
76fcea01-e4b9-4419-bf02-0ca58896bad9
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2 d5 5. a3 Bxc3+ 6. Qxc3 Nc6 
Nimzo-Indian, classical, Noa variation, main line
4b803275-1855-4f87-8fb1-652364154fc9
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2 d5 5. a3 Bxc3+ 6. Qxc3 Ne4 
******E37: Nimzo-Indian, classical, Noa variation, main line, 7.Qc2
Nimzo-Indian, classical, Noa variation, main line, 7.Qc2
e3856c35-de1d-428d-8ba3-9328aa9d0f79
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2 d5 5. a3 Bxc3+ 6. Qxc3 Ne4 7. Qc2
Nimzo-Indian, classical, San Remo variation
eadcc86b-a7f4-4a53-aafe-8d9940c42f36
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2 d5 5. a3 Bxc3+ 6. Qxc3 Ne4 7. Qc2 Nc6 8. e3 e5 
******E38: Nimzo-Indian, classical, 4...c5
Nimzo-Indian, classical, 4...c5
82436090-6ae4-410c-a1dd-1746659ac11a
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2 c5 
******E39: Nimzo-Indian, classical, Pirc variation
Nimzo-Indian, classical, Pirc variation
abbb6404-f2fc-43b0-9f7f-5e387f545e9c
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2 c5 5. dxc5 O-O 
******E40: Nimzo-Indian, 4.e3
Nimzo-Indian, 4.e3
cb4751a6-6adc-439d-90e9-c8cdfe36a2b8
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3
Nimzo-Indian, 4.e3, Taimanov variation
12dbe496-0364-4ed5-bc2e-db2fb5a91acb
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 Nc6 
******E41: Nimzo-Indian, 4.e3 c5
Nimzo-Indian, 4.e3 c5
38d438d5-b25e-4ef2-98e9-13c06066ee0f
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 c5 
Nimzo-Indian, e3, Huebner variation
3c55231b-62c6-474a-8295-81cf0ac5ecf8
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 c5 5. Bd3 Nc6 6. Nf3 Bxc3+ 7. bxc3 d6 
******E42: Nimzo-Indian, 4.e3 c5, 5.Ne2 (Rubinstein)
Nimzo-Indian, 4.e3 c5, 5.Ne2 (Rubinstein)
9457fb76-4fa9-47be-85c5-969a3362b5ec
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 c5 5. Nge2
******E43: Nimzo-Indian, Fischer variation
Nimzo-Indian, Fischer variation
d4ea1d64-12d2-4a54-88a7-2ebd3842379a
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 b6 
******E44: Nimzo-Indian, Fischer variation, 5.Ne2
Nimzo-Indian, Fischer variation, 5.Ne2
86c5c019-a707-4146-85c1-6c8b39caf1af
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 b6 5. Nge2
******E45: Nimzo-Indian, 4.e3, Bronstein (Byrne) variation
Nimzo-Indian, 4.e3, Bronstein (Byrne) variation
33241218-b9a0-492a-b6ae-dd644be47c4e
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 b6 5. Nge2 Ba6 
******E46: Nimzo-Indian, 4.e3 O-O
Nimzo-Indian, 4.e3 O-O
8ca470ff-f494-4f11-a502-3bf0f13ea360
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 
Nimzo-Indian, Reshevsky variation
ee11a4d1-5863-4013-8861-a6934fa82c9b
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nge2
Nimzo-Indian, Simagin variation
1320ecc4-c58f-47f1-855e-998418fed7d4
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nge2 d5 6. a3 Bd6 
******E47: Nimzo-Indian, 4.e3 O-O, 5.Bd3
Nimzo-Indian, 4.e3 O-O, 5.Bd3
ac449d09-bba5-4a19-984e-6bd0e074b60d
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Bd3
******E48: Nimzo-Indian, 4.e3 O-O, 5.Bd3 d5
Nimzo-Indian, 4.e3 O-O, 5.Bd3 d5
6381ac99-f3c2-4a54-bd0d-593e63939ab1
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Bd3 d5 
******E49: Nimzo-Indian, 4.e3, Botvinnik system
Nimzo-Indian, 4.e3, Botvinnik system
e049f910-daa7-436c-af75-82b4039eb7a9
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Bd3 d5 6. a3 Bxc3+ 7. bxc3
******E50: Nimzo-Indian, 4.e3 e8g8, 5.Nf3, without ...d5
Nimzo-Indian, 4.e3 e8g8, 5.Nf3, without ...d5
66a00275-cba2-4473-93de-cc68071bb6eb
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3
******E51: Nimzo-Indian, 4.e3 e8g8, 5.Nf3 d7d5
Nimzo-Indian, 4.e3 e8g8, 5.Nf3 d7d5
0ad96206-4c5a-44f1-bc9b-98864e255a32
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3 d5 
Nimzo-Indian, 4.e3, Ragozin variation
805c4c5d-336f-4dde-8e3c-f1ecc11a4f23
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3 d5 6. Bd3 Nc6 7. O-O dxc4 
******E52: Nimzo-Indian, 4.e3, main line with ...b6
Nimzo-Indian, 4.e3, main line with ...b6
15ac14be-10e2-4200-92e6-998e41aec4fc
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3 d5 6. Bd3 b6 
******E53: Nimzo-Indian, 4.e3, main line with ...c5
Nimzo-Indian, 4.e3, main line with ...c5
6f9beb1f-06ff-4132-a8d0-45c8c9286875
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3 d5 6. Bd3 c5 
Nimzo-Indian, 4.e3, Keres variation
e18384a6-a6f9-4426-9dd4-40c20cda0e2f
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3 d5 6. Bd3 c5 7. O-O b6 
Nimzo-Indian, 4.e3, Gligoric system with 7...Nbd7
14ac2f7a-a610-4744-9579-69ad63c254f5
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3 d5 6. Bd3 c5 7. O-O Nbd7 
******E54: Nimzo-Indian, 4.e3, Gligoric system with 7...dc
Nimzo-Indian, 4.e3, Gligoric system with 7...dc
665c6d12-46e6-4df6-981f-2f4cc56dae09
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3 d5 6. Bd3 c5 7. O-O dxc4 8. Bxc4
Nimzo-Indian, 4.e3, Gligoric system, Smyslov variation
6fc83e30-dd30-40cd-98a7-db078e0068a7
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3 d5 6. Bd3 c5 7. O-O dxc4 8. Bxc4 Qe7 
******E55: Nimzo-Indian, 4.e3, Gligoric system, Bronstein variation
Nimzo-Indian, 4.e3, Gligoric system, Bronstein variation
22b14b1f-08b2-40be-a1b1-3c86878bd028
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3 d5 6. Bd3 c5 7. O-O dxc4 8. Bxc4 Nbd7 
******E56: Nimzo-Indian, 4.e3, main line with 7...Nc6
Nimzo-Indian, 4.e3, main line with 7...Nc6
50e167b5-d702-4d99-88ff-5b7aec5778b9
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3 d5 6. Bd3 c5 7. O-O Nc6 
******E57: Nimzo-Indian, 4.e3, main line with 8...dc and 9...cd
Nimzo-Indian, 4.e3, main line with 8...dc and 9...cd
eaa14372-f3f2-47d0-a77d-306852690bf2
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3 d5 6. Bd3 c5 7. O-O Nc6 8. a3 dxc4 9. Bxc4 cxd4 
******E58: Nimzo-Indian, 4.e3, main line with 8...Bxc3
Nimzo-Indian, 4.e3, main line with 8...Bxc3
aafd5b27-bc4d-4104-a200-d8b8e15e44ad
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3 d5 6. Bd3 c5 7. O-O Nc6 8. a3 Bxc3 9. bxc3
******E59: Nimzo-Indian, 4.e3, main line
Nimzo-Indian, 4.e3, main line
3cf77a0e-3d07-4268-a5e9-bce72b8b66d1
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3 d5 6. Bd3 c5 7. O-O Nc6 8. a3 Bxc3 9. bxc3 dxc4 10. Bxc4
******E60: King's Indian defence
King's Indian defence
b67e9266-d17a-4b46-8a37-5d9cfaa3a596
1. d4 Nf6 2. c4 g6 
King's Indian, 3.Nf3
04579723-4355-483a-bc6e-5e7a3e3b4347
1. d4 Nf6 2. c4 g6 3. Nf3
Queen's pawn, Mengarini attack
a84cee0a-52ea-4204-8d21-9aafbdb720f3
1. d4 Nf6 2. c4 g6 3. Qc2
King's Indian, Anti-Gruenfeld
98d470d0-86ad-4359-9eaa-8a6a647ac293
1. d4 Nf6 2. c4 g6 3. d5
King's Indian, Danube gambit
10c0e378-7c00-4d3e-a318-6b76aad7ef67
1. d4 Nf6 2. c4 g6 3. d5 b5 
King's Indian, 3.g3
10e7961c-f6c2-4376-a405-b229e49cbfac
1. d4 Nf6 2. c4 g6 3. g3
King's Indian, 3.g3, counterthrust variation
01ff97e7-e226-4771-ab5c-eb250eaaff6f
1. d4 Nf6 2. c4 g6 3. g3 Bg7 4. Bg2 d5 
******E61: King's Indian defence, 3.Nc3
King's Indian defence, 3.Nc3
9a14f698-eca0-4c75-b597-25da463acf3f
1. d4 Nf6 2. c4 g6 3. Nc3
King's Indian, Smyslov system
0a880f13-fda2-48e5-91f5-1acd21bb1531
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. Bg5
******E62: King's Indian, fianchetto variation
King's Indian, fianchetto variation
1c4a0799-dc07-4e3e-af46-39ac1826fbfc
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3
King's Indian, fianchetto, Larsen system
544f453c-71eb-40e2-bf45-8ee0de877256
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 c6 7. O-O Bf5 
King's Indian, fianchetto, Kavalek (Bronstein) variation
c946b016-eef3-48f5-bff9-8fe831f998d1
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 c6 7. O-O Qa5 
King's Indian, fianchetto with ...Nc6
1dd8c5d9-2d6f-4ad9-b8a9-8fd72ec48552
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 Nc6 
King's Indian, fianchetto, Uhlmann (Szabo) variation
a04d093e-e95b-491b-9998-ccbf98c9b1e9
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 Nc6 7. O-O e5 
King's Indian, fianchetto, lesser Simagin (Spassky) variation
d173f4ce-b975-43f2-a24a-ae2cc53419ba
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 Nc6 7. O-O Bf5 
King's Indian, fianchetto, Simagin variation
184b1458-4ade-4b2c-bb1e-bba23c52eaca
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 Nc6 7. O-O Bg4 
******E63: King's Indian, fianchetto, Panno variation
King's Indian, fianchetto, Panno variation
1a8a4a1c-7b56-4a5b-ba1f-df65fcad88c3
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 Nc6 7. O-O a6 
******E64: King's Indian, fianchetto, Yugoslav system
King's Indian, fianchetto, Yugoslav system
1583822b-7891-4ba2-9ca7-8780be53af2a
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 c5 
******E65: King's Indian, fianchetto, Yugoslav, 7.O-O
King's Indian, fianchetto, Yugoslav, 7.O-O
1dcd1c03-60e1-4683-af91-c041159f8ce0
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 c5 7. O-O
******E66: King's Indian, fianchetto, Yugoslav Panno
King's Indian, fianchetto, Yugoslav Panno
a6c15cb4-4ba9-4f80-84a7-7c9f7bc1dcc6
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 c5 7. O-O Nc6 8. d5
******E67: King's Indian, fianchetto with ...Nd7
King's Indian, fianchetto with ...Nd7
31abc31e-f293-4907-864a-c6a0f2bb8e69
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 Nbd7 
King's Indian, fianchetto, classical variation
57b02cea-777e-4cce-b7b4-e1944422db1a
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 Nbd7 7. O-O e5 
******E68: King's Indian, fianchetto, classical variation, 8.e4
King's Indian, fianchetto, classical variation, 8.e4
25027e6c-7f4d-419a-a8d0-99eb56a24bd7
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 Nbd7 7. O-O e5 8. e4
******E69: King's Indian, fianchetto, classical main line
King's Indian, fianchetto, classical main line
d5c59da3-e1cd-4f34-880d-8b5a3f6a60b1
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 Nbd7 7. O-O e5 8. e4 c6 9. h3
******E70: King's Indian, 4.e4
King's Indian, 4.e4
0b4a42d8-6ed6-4108-ad2b-e0d768489a0a
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4
King's Indian, Kramer system
00678a8e-5136-4d05-bb38-744b7cadc0f8
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nge2
King's Indian, accelerated Averbakh system
8f2b24c7-9298-410d-b232-13e8f0bfbd83
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Bg5
******E71: King's Indian, Makagonov system (5.h3)
King's Indian, Makagonov system (5.h3)
98a76c03-5af8-4712-96a7-8144766c4514
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. h3
******E72: King's Indian with e4 & g3
King's Indian with e4 & g3
14c4d450-8268-47dd-87de-23c7785d9e5a
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. g3
King's Indian, Pomar system
8bd530aa-0467-4935-a2b2-5ad581669ce0
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. g3 O-O 6. Bg2 e5 7. Nge2
******E73: King's Indian, 5.Be2
King's Indian, 5.Be2
2b92241a-0902-4228-8de4-fbbc7f7bedb1
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Be2
King's Indian, Semi-Averbakh system
5efd93eb-2a81-4629-8749-5488789001fe
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Be2 O-O 6. Be3
King's Indian, Averbakh system
a1626613-fa63-4a24-9f91-91f2dc2b347c
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Be2 O-O 6. Bg5
******E74: King's Indian, Averbakh, 6...c5
King's Indian, Averbakh, 6...c5
24157cc9-081c-4134-8aea-76014995040d
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Be2 O-O 6. Bg5 c5 
******E75: King's Indian, Averbakh, main line
King's Indian, Averbakh, main line
8df51727-ac6a-494a-83ee-1c936bb6d93f
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Be2 O-O 6. Bg5 c5 7. d5 e6 
******E76: King's Indian, Four pawns attack
King's Indian, Four pawns attack
871465cd-9548-4559-8827-cf4f32e9d58d
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f4
King's Indian, Four pawns attack, dynamic line
00dba293-89c5-4a53-8fa0-14a01489443f
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f4 O-O 6. Nf3 c5 7. d5
******E77: King's Indian, Four pawns attack, 6.Be2
King's Indian, Four pawns attack, 6.Be2
fe9070d5-59fe-426f-8fed-7e32055e1e72
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f4 O-O 6. Be2
King's Indian, Six pawns attack
235f11c5-3aea-4d2f-977c-6ea9f14851ec
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f4 O-O 6. Be2 c5 7. d5 e6 8. dxe6 fxe6 9. g4 Nc6 10. h4
King's Indian, Four pawns attack
355ab510-0a69-4ac3-af94-b5288b70a32c
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f4 O-O 6. Be2 c5 7. d5 e6 8. Nf3
King's Indian, Four pawns attack, Florentine gambit
f96395af-c4f3-4f85-8b20-a1941ce784db
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f4 O-O 6. Be2 c5 7. d5 e6 8. Nf3 exd5 9. e5
******E78: King's Indian, Four pawns attack, with Be2 and Nf3
King's Indian, Four pawns attack, with Be2 and Nf3
f06d8125-aa49-437d-be28-dc8446330e1c
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f4 O-O 6. Be2 c5 7. Nf3
******E79: King's Indian, Four pawns attack, main line
King's Indian, Four pawns attack, main line
50ef0e52-ecfa-4f79-bfcc-a687abfab6bb
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f4 O-O 6. Be2 c5 7. Nf3 cxd4 8. Nxd4 Nc6 9. Be3
******E80: King's Indian, Saemisch variation
King's Indian, Saemisch variation
a224e11c-0a12-40f7-a385-7962265f0717
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3
******E81: King's Indian, Saemisch, 5...O-O
King's Indian, Saemisch, 5...O-O
b31ec15a-ab4b-4ee0-948b-c9b37e6d591e
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3 O-O 
King's Indian, Saemisch, Byrne variation
55c23255-44f9-41f5-afed-ecbbcc4dce92
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3 O-O 6. Be3 c6 7. Bd3 a6 
******E82: King's Indian, Saemisch, double fianchetto variation
King's Indian, Saemisch, double fianchetto variation
3e270bd7-b6e7-4c0b-bf53-993c8f5440bd
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3 O-O 6. Be3 b6 
******E83: King's Indian, Saemisch, 6...Nc6
King's Indian, Saemisch, 6...Nc6
8c49a146-a017-4a92-bb6c-46f9b0808562
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3 O-O 6. Be3 Nc6 
King's Indian, Saemisch, Ruban variation
b0125447-0293-4fe0-94f4-65f77f942a72
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3 O-O 6. Be3 Nc6 7. Nge2 Rb8 
King's Indian, Saemisch, Panno formation
c195c925-adec-4da8-916d-ec0a8bb82b1a
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3 O-O 6. Be3 Nc6 7. Nge2 a6 
******E84: King's Indian, Saemisch, Panno main line
King's Indian, Saemisch, Panno main line
61c412c9-b7b0-4643-a58e-39f01c58cf0c
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3 O-O 6. Be3 Nc6 7. Nge2 a6 8. Qd2 Rb8 
******E85: King's Indian, Saemisch, orthodox variation
King's Indian, Saemisch, orthodox variation
716701fa-1133-41cb-8605-11d614a6d560
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3 O-O 6. Be3 e5 
******E86: King's Indian, Saemisch, orthodox, 7.Nge2 c6
King's Indian, Saemisch, orthodox, 7.Nge2 c6
dbf6c275-2d0f-4e1f-820b-728d39640778
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3 O-O 6. Be3 e5 7. Nge2 c6 
******E87: King's Indian, Saemisch, orthodox, 7.d5
King's Indian, Saemisch, orthodox, 7.d5
2ecda61c-fdf9-4e88-90b2-795a987be0a2
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3 O-O 6. Be3 e5 7. d5
King's Indian, Saemisch, orthodox, Bronstein variation
6a92c8da-67d7-40c9-80db-4174052a5da5
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3 O-O 6. Be3 e5 7. d5 Nh5 8. Qd2 Qh4+ 9. g3 Nxg3 10. Qf2 Nxf1 11. Qxh4 Nxe3 12. Ke2 Nxc4 
******E88: King's Indian, Saemisch, orthodox, 7.d5 c6
King's Indian, Saemisch, orthodox, 7.d5 c6
e6012df4-211d-404a-96de-b0d5cf034cce
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3 O-O 6. Be3 e5 7. d5 c6 
******E89: King's Indian, Saemisch, orthodox main line
King's Indian, Saemisch, orthodox main line
d8756b82-ccbb-4a83-ad58-d52636d2246a
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3 O-O 6. Be3 e5 7. d5 c6 8. Nge2 cxd5 
******E90: King's Indian, 5.Nf3
King's Indian, 5.Nf3
ef127a95-e41a-4332-97c6-1056b0b7e8bb
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3
King's Indian, Larsen variation
0946db4f-637b-4d4d-8a72-fa583f89bf7b
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be3
King's Indian, Zinnowitz variation
8eb105db-1f7d-40f2-b331-d8f274ce7066
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Bg5
******E91: King's Indian, 6.Be2
King's Indian, 6.Be2
2ad94d32-a498-4b40-8660-918399152922
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2
King's Indian, Kazakh variation
d4c1738e-5271-4c88-bd55-dcd14162538a
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 Na6 
******E92: King's Indian, classical variation
King's Indian, classical variation
8a1caa98-585b-4dec-ac2a-2b6116c6fc81
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 
King's Indian, Andersson variation
e5484ad4-5939-4362-bd29-05577f1bfb8b
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. dxe5
King's Indian, Gligoric-Taimanov system
9806c9bc-a064-460b-b4c9-e1b08c8c6725
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. Be3
King's Indian, Petrosian system
30a7dd9c-4819-4c2d-8184-065d0426f0e1
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. d5
King's Indian, Petrosian system, Stein variation
a87efb96-d539-4135-a237-26ad7be2b391
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. d5 a5 
******E93: King's Indian, Petrosian system, main line
King's Indian, Petrosian system, main line
87be9869-54bb-4a58-ac08-dd9aeda73a2d
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. d5 Nbd7 
King's Indian, Petrosian system, Keres variation
2e8c8dd7-e98f-4c16-8c60-1ade92aad238
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. d5 Nbd7 8. Bg5 h6 9. Bh4 g5 10. Bg3 Nh5 11. h4
******E94: King's Indian, orthodox variation
King's Indian, orthodox variation
bb5def1e-12af-466e-a9a9-dc825c6ad836
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. O-O
King's Indian, orthodox, Donner variation
35cfa509-413a-4855-97c0-a0d738169a5a
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. O-O c6 
King's Indian, orthodox, 7...Nbd7
4dfe275c-4c4f-47b9-bd87-10742ac4092e
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. O-O Nbd7 
******E95: King's Indian, orthodox, 7...Nbd7, 8.Re1
King's Indian, orthodox, 7...Nbd7, 8.Re1
8b0b8c8d-66ab-4218-a876-b676a61141ed
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. O-O Nbd7 8. Re1
******E96: King's Indian, orthodox, 7...Nbd7, main line
King's Indian, orthodox, 7...Nbd7, main line
75a49312-c53a-47b2-95a2-db0567a87dfd
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. O-O Nbd7 8. Re1 c6 9. Bf1 a5 
******E97: King's Indian, orthodox, Aronin-Taimanov variation (Yugoslav attack / Mar del Plata variation)
King's Indian, orthodox, Aronin-Taimanov variation (Yugoslav attack / Mar del Plata variation)
b8863e20-7318-43eb-82f0-574db715f600
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. O-O Nc6 
King's Indian, orthodox, Aronin-Taimanov, bayonet attack
d2094ce2-bc1d-42fe-8946-6b0e11a7d14e
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. O-O Nc6 8. d5 Ne7 9. b4
******E98: King's Indian, orthodox, Aronin-Taimanov, 9.Ne1
King's Indian, orthodox, Aronin-Taimanov, 9.Ne1
37f45e88-6cc3-4908-b86a-51a5e97cbe86
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. O-O Nc6 8. d5 Ne7 9. Ne1
******E99: King's Indian, orthodox, Aronin-Taimanov, main line
King's Indian, orthodox, Aronin-Taimanov, main line
194ec3a1-5cc0-43ab-960e-e7304201e5c3
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. O-O Nc6 8. d5 Ne7 9. Ne1 Nd7 10. f3 f5 
King's Indian, orthodox, Aronin-Taimanov, Benko attack
33d7990c-a09c-4839-847f-c4596ac91eb5
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. O-O Nc6 8. d5 Ne7 9. Ne1 Nd7 10. f3 f5 11. g4"""

OPENINGS = []

class MoveVisitor(chess.pgn.BaseVisitor):
    def __init__(self):
        self.moves = []

    def visit_move(self, board, move):
        self.moves.append(move)

# fix me
sections = TEXT.split("******")
sections = [x for x in sections if not re.match(r"^[\s]*$", x)]
for section in sections:
    def create_move(uci):
        src = chess.SQUARE_NAMES[uci.from_square]
        dst = chess.SQUARE_NAMES[uci.to_square]
        return {
            "src": src,
            "dst": dst
        }
    section_lines = [x for x in section.split("\n") if not re.match(r"^[\s]*$", x)]
    opening_name = section_lines[0][5:]
    opening_id = section_lines[0][0:3]
    variant_lines = [x for x in section_lines[1:] if not re.match(r"^[\s]*$", x)]
    variant_groups = [variant_lines[i:i+3] for i in range(0, len(variant_lines), 3)]
    
    for group in variant_groups:
        name = group[0]
        id = group[1]
        line = group[2]
        opening = Opening()
        opening.eco_id = opening_id
        opening.eco_name = opening_name
        opening.id = id
        opening.move_text = line.strip()
        opening.variant_name = name
        pgn = io.StringIO(line)
        game = chess.pgn.read_game(pgn)
        visitor = MoveVisitor()
        game.accept(visitor)
        opening.moves = list(map(create_move, visitor.moves))
        OPENINGS.append(opening)