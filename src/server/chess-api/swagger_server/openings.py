import io
import chess
import chess.pgn

from pprint import pprint as pp
from swagger_server.models.move_factory import create_move_models
from swagger_server.models import Opening, OpeningVariant

class MoveVisitor(chess.pgn.BaseVisitor):
    def __init__(self):
        self.moves = []

    def visit_move(self, board, move):
        self.moves.append(move)

TEXT = """******A00: Polish (Sokolsky) opening
Polish (Sokolsky) opening
1. b4
Polish, Tuebingen variation
1. b4 Nh6 
Polish, Outflank variation
1. b4 c6 
Benko's opening
1. g3
Lasker simul special
1. g3 h5 
Benko's opening, reversed Alekhine
1. g3 e5 2. Nf3
Grob's attack
1. g4
Grob, spike attack
1. g4 d5 2. Bg2 c6 3. g5
Grob, Fritz gambit
1. g4 d5 2. Bg2 Bxg4 3. c4
Grob, Romford counter-gambit
1. g4 d5 2. Bg2 Bxg4 3. c4 d4 
Clemenz (Mead's, Basman's or de Klerk's) opening
1. h3
Global opening
1. h3 e5 2. a3
Amar (Paris) opening
1. Nh3
Amar gambit
1. Nh3 d5 2. g3 e5 3. f4 Bxh3 4. Bxh3 exf4 
Dunst (Sleipner,Heinrichsen) opening
1. Nc3 e5 
Battambang opening
1. Nc3 e5 2. a3
Novosibirsk opening
1. Nc3 c5 2. d4 cxd4 3. Qxd4 Nc6 4. Qh4
Anderssen's opening
1. a3
Ware (Meadow Hay) opening
1. a4
Crab opening
1. a4 e5 2. h4
Saragossa opening
1. c3
Mieses opening
1. d3 e5 
Valencia opening
1. d3 e5 2. Nd2
Venezolana opening
1. d3 c5 2. Nc3 Nc6 3. g3
Van't Kruijs opening
1. e3
Amsterdam attack
1. e3 e5 2. c4 d6 3. Nc3 Nc6 4. b3 Nf6 
Gedult's opening
1. f3
Hammerschlag (Fried fox/Pork chop opening)
1. f3 e5 2. Kf2
Anti-Borg (Desprez) opening
1. h4
Durkin's attack
1. Na3
******A01: Nimzovich-Larsen attack
Nimzovich-Larsen attack
1. b3
Nimzovich-Larsen attack, modern variation
1. b3 e5 
Nimzovich-Larsen attack, Indian variation
1. b3 Nf6 
Nimzovich-Larsen attack, classical variation
1. b3 d5 
Nimzovich-Larsen attack, English variation
1. b3 c5 
Nimzovich-Larsen attack, Dutch variation
1. b3 f5 
Nimzovich-Larsen attack, Polish variation
1. b3 b5 
Nimzovich-Larsen attack, symmetrical variation
1. b3 b6 
******A02: Bird's opening
Bird's opening
1. f4
Bird, From gambit
1. f4 e5 
Bird, From gambit, Lasker variation
1. f4 e5 2. fxe5 d6 3. exd6 Bxd6 4. Nf3 g5 
Bird, From gambit, Lipke variation
1. f4 e5 2. fxe5 d6 3. exd6 Bxd6 4. Nf3 Nh6 5. d4
Bird's opening, Swiss gambit
1. f4 f5 2. e4 fxe4 3. Nc3 Nf6 4. g4
Bird, Hobbs gambit
1. f4 g5 
******A03: Bird's opening
Bird's opening
1. f4 d5 
Mujannah opening
1. f4 d5 2. c4
Bird's opening, Williams gambit
1. f4 d5 2. e4
Bird's opening, Lasker variation
1. f4 d5 2. Nf3 Nf6 3. e3 c5 
******A04: Reti opening
Reti opening
1. Nf3
Reti v Dutch
1. Nf3 f5 
Reti, Pirc-Lisitsin gambit
1. Nf3 f5 2. e4
Reti, Lisitsin gambit deferred
1. Nf3 f5 2. d3 Nf6 3. e4
Reti opening
1. Nf3 d6 
Reti, Wade defence
1. Nf3 d6 2. e4 Bg4 
Reti, Herrstroem gambit
1. Nf3 g5 
******A05: Reti opening
Reti opening
1. Nf3 Nf6 
Reti, King's Indian attack, Spassky's variation
1. Nf3 Nf6 2. g3 b5 
Reti, King's Indian attack
1. Nf3 Nf6 2. g3 g6 
Reti, King's Indian attack, Reti-Smyslov variation
1. Nf3 Nf6 2. g3 g6 3. b4
******A06: Reti opening
Reti opening
1. Nf3 d5 
Reti, old Indian attack
1. Nf3 d5 2. d3
Santasiere's folly
1. Nf3 d5 2. b4
Tennison (Lemberg, Zukertort) gambit
1. Nf3 d5 2. e4
Reti, Nimzovich-Larsen attack
1. Nf3 d5 2. b3
******A07: Reti, King's Indian attack (Barcza system)
Reti, King's Indian attack (Barcza system)
1. Nf3 d5 2. g3
Reti, King's Indian attack, Yugoslav variation
1. Nf3 d5 2. g3 Nf6 3. Bg2 c6 4. O-O Bg4 
Reti, King's Indian attack, Keres variation
1. Nf3 d5 2. g3 Bg4 3. Bg2 Nd7 
Reti, King's Indian attack
1. Nf3 d5 2. g3 g6 
Reti, King's Indian attack, Pachman system
1. Nf3 d5 2. g3 g6 3. Bg2 Bg7 4. O-O e5 5. d3 Ne7 
Reti, King's Indian attack (with ...c5)
1. Nf3 d5 2. g3 c5 
******A08: Reti, King's Indian attack
Reti, King's Indian attack
1. Nf3 d5 2. g3 c5 3. Bg2
Reti, King's Indian attack, French variation
1. Nf3 d5 2. g3 c5 3. Bg2 Nc6 4. O-O e6 5. d3 Nf6 6. Nbd2 Be7 7. e4 O-O 8. Re1
******A09: Reti opening
Reti opening
1. Nf3 d5 2. c4
Reti, advance variation
1. Nf3 d5 2. c4 d4 
Reti accepted
1. Nf3 d5 2. c4 dxc4 
Reti accepted, Keres variation
1. Nf3 d5 2. c4 dxc4 3. e3 Be6 
******A10: English opening
English opening
1. c4
English opening
1. c4 g6 
English, Adorjan defence
1. c4 g6 2. e4 e5 
English, Jaenisch gambit
1. c4 b5 
English, Anglo-Dutch defense
1. c4 f5 
******A11: English, Caro-Kann defensive system
English, Caro-Kann defensive system
1. c4 c6 
******A12: English, Caro-Kann defensive system
English, Caro-Kann defensive system
1. c4 c6 2. Nf3 d5 3. b3
English, Torre defensive system
1. c4 c6 2. Nf3 d5 3. b3 Nf6 4. g3 Bg4 
English, London defensive system
1. c4 c6 2. Nf3 d5 3. b3 Nf6 4. g3 Bf5 
English, Caro-Kann defensive system
1. c4 c6 2. Nf3 d5 3. b3 Nf6 4. Bb2
English, Bled variation
1. c4 c6 2. Nf3 d5 3. b3 Nf6 4. Bb2 g6 
English, New York (London) defensive system
1. c4 c6 2. Nf3 d5 3. b3 Nf6 4. Bb2 Bf5 
English, Capablanca's variation
1. c4 c6 2. Nf3 d5 3. b3 Nf6 4. Bb2 Bg4 
English, Caro-Kann defensive system, Bogolyubov variation
1. c4 c6 2. Nf3 d5 3. b3 Bg4 
******A13: English opening
English opening
1. c4 e6 
English, Romanishin gambit
1. c4 e6 2. Nf3 Nf6 3. g3 a6 4. Bg2 b5 
English opening, Agincourt variation
1. c4 e6 2. Nf3 d5 
English, Wimpey system
1. c4 e6 2. Nf3 d5 3. b3 Nf6 4. Bb2 c5 5. e3
English opening, Agincourt variation
1. c4 e6 2. Nf3 d5 3. g3
English, Kurajica defence
1. c4 e6 2. Nf3 d5 3. g3 c6 
English, Neo-Catalan
1. c4 e6 2. Nf3 d5 3. g3 Nf6 
English, Neo-Catalan accepted
1. c4 e6 2. Nf3 d5 3. g3 Nf6 4. Bg2 dxc4 
******A14: English, Neo-Catalan declined
English, Neo-Catalan declined
1. c4 e6 2. Nf3 d5 3. g3 Nf6 4. Bg2 Be7 5. O-O
English, Symmetrical, Keres defence
1. c4 e6 2. Nf3 d5 3. g3 Nf6 4. Bg2 Be7 5. O-O c5 6. cxd5 Nxd5 7. Nc3 Nc6 
******A15: English, 1...Nf6 (Anglo-Indian defense)
English, 1...Nf6 (Anglo-Indian defense)
1. c4 Nf6 
English orang-utan
1. c4 Nf6 2. b4
English opening
1. c4 Nf6 2. Nf3
******A16: English opening
English opening
1. c4 Nf6 2. Nc3
English, Anglo-Gruenfeld defense
1. c4 Nf6 2. Nc3 d5 
English, Anglo-Gruenfeld, Smyslov defense
1. c4 Nf6 2. Nc3 d5 3. cxd5 Nxd5 4. g3 g6 5. Bg2 Nxc3 
English, Anglo-Gruenfeld, Czech defense
1. c4 Nf6 2. Nc3 d5 3. cxd5 Nxd5 4. g3 g6 5. Bg2 Nb6 
English, Anglo-Gruenfeld defense
1. c4 Nf6 2. Nc3 d5 3. cxd5 Nxd5 4. Nf3
English, Anglo-Gruenfeld defense, Korchnoi variation
1. c4 Nf6 2. Nc3 d5 3. cxd5 Nxd5 4. Nf3 g6 5. g3 Bg7 6. Bg2 e5 
******A17: English opening
English opening
1. c4 Nf6 2. Nc3 e6 
English, Queens Indian formation
1. c4 Nf6 2. Nc3 e6 3. Nf3 b6 
English, Queens Indian, Romanishin variation
1. c4 Nf6 2. Nc3 e6 3. Nf3 b6 4. e4 Bb7 5. Bd3
English, Nimzo-English opening
1. c4 Nf6 2. Nc3 e6 3. Nf3 Bb4 
******A18: English, Mikenas-Carls variation
English, Mikenas-Carls variation
1. c4 Nf6 2. Nc3 e6 3. e4
English, Mikenas-Carls, Flohr variation
1. c4 Nf6 2. Nc3 e6 3. e4 d5 4. e5
English, Mikenas-Carls, Kevitz variation
1. c4 Nf6 2. Nc3 e6 3. e4 Nc6 
******A19: English, Mikenas-Carls, Sicilian variation
English, Mikenas-Carls, Sicilian variation
1. c4 Nf6 2. Nc3 e6 3. e4 c5 
******A20: English opening
English opening
1. c4 e5 
English, Nimzovich variation
1. c4 e5 2. Nf3
English, Nimzovich, Flohr variation
1. c4 e5 2. Nf3 e4 
******A21: English opening
English opening
1. c4 e5 2. Nc3
English, Troeger defence
1. c4 e5 2. Nc3 d6 3. g3 Be6 4. Bg2 Nc6 
English, Keres variation
1. c4 e5 2. Nc3 d6 3. g3 c6 
English opening
1. c4 e5 2. Nc3 d6 3. Nf3
English, Smyslov defence
1. c4 e5 2. Nc3 d6 3. Nf3 Bg4 
English, Kramnik-Shirov counterattack
1. c4 e5 2. Nc3 Bb4 
******A22: English opening
English opening
1. c4 e5 2. Nc3 Nf6 
English, Bellon gambit
1. c4 e5 2. Nc3 Nf6 3. Nf3 e4 4. Ng5 b5 
English, Carls' Bremen system
1. c4 e5 2. Nc3 Nf6 3. g3
English, Bremen, reverse dragon
1. c4 e5 2. Nc3 Nf6 3. g3 d5 
English, Bremen, Smyslov system
1. c4 e5 2. Nc3 Nf6 3. g3 Bb4 
******A23: English, Bremen system, Keres variation
English, Bremen system, Keres variation
1. c4 e5 2. Nc3 Nf6 3. g3 c6 
******A24: English, Bremen system with ...g6
English, Bremen system with ...g6
1. c4 e5 2. Nc3 Nf6 3. g3 g6 
******A25: English, Sicilian reversed
English, Sicilian reversed
1. c4 e5 2. Nc3 Nc6 
English, closed system
1. c4 e5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 
English, closed, Taimanov variation
1. c4 e5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. e3 d6 6. Nge2 Nh6 
English, closed, Hort variation
1. c4 e5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. e3 d6 6. Nge2 Be6 
English, closed, 5.Rb1
1. c4 e5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. Rb1
English, closed, 5.Rb1 Taimanov variation
1. c4 e5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. Rb1 Nh6 
English, closed system (without ...d6)
1. c4 e5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. d3
******A26: English, closed system
English, closed system
1. c4 e5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. d3 d6 
English, Botvinnik system
1. c4 e5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. d3 d6 6. e4
******A27: English, three knights system
English, three knights system
1. c4 e5 2. Nc3 Nc6 3. Nf3
******A28: English, four knights system
English, four knights system
1. c4 e5 2. Nc3 Nc6 3. Nf3 Nf6 
English, Nenarokov variation
1. c4 e5 2. Nc3 Nc6 3. Nf3 Nf6 4. d4 exd4 5. Nxd4 Bb4 6. Bg5 h6 7. Bh4 Bxc3+ 8. bxc3 Ne5 
English, Bradley Beach variation
1. c4 e5 2. Nc3 Nc6 3. Nf3 Nf6 4. d4 e4 
English, four knights, Nimzovich variation
1. c4 e5 2. Nc3 Nc6 3. Nf3 Nf6 4. e4
English, four knights, Marini variation
1. c4 e5 2. Nc3 Nc6 3. Nf3 Nf6 4. a3
English, four knights, Capablanca variation
1. c4 e5 2. Nc3 Nc6 3. Nf3 Nf6 4. d3
English, four knights, 4.e3
1. c4 e5 2. Nc3 Nc6 3. Nf3 Nf6 4. e3
English, four knights, Stean variation
1. c4 e5 2. Nc3 Nc6 3. Nf3 Nf6 4. e3 Bb4 5. Qc2 O-O 6. Nd5 Re8 7. Qf5
English, four knights, Romanishin variation
1. c4 e5 2. Nc3 Nc6 3. Nf3 Nf6 4. e3 Bb4 5. Qc2 Bxc3 
******A29: English, four knights, kingside fianchetto
English, four knights, kingside fianchetto
1. c4 e5 2. Nc3 Nc6 3. Nf3 Nf6 4. g3
******A30: English, symmetrical variation
English, symmetrical variation
1. c4 c5 
English, symmetrical, hedgehog system
1. c4 c5 2. Nf3 Nf6 3. g3 b6 4. Bg2 Bb7 5. O-O e6 6. Nc3 Be7 
English, symmetrical, hedgehog, flexible formation
1. c4 c5 2. Nf3 Nf6 3. g3 b6 4. Bg2 Bb7 5. O-O e6 6. Nc3 Be7 7. d4 cxd4 8. Qxd4 d6 9. Rd1 a6 10. b3 Nbd7 
******A31: English, symmetrical, Benoni formation
English, symmetrical, Benoni formation
1. c4 c5 2. Nf3 Nf6 3. d4
******A32: English, symmetrical variation
English, symmetrical variation
1. c4 c5 2. Nf3 Nf6 3. d4 cxd4 4. Nxd4 e6 
******A33: English, symmetrical variation
English, symmetrical variation
1. c4 c5 2. Nf3 Nf6 3. d4 cxd4 4. Nxd4 e6 5. Nc3 Nc6 
English, symmetrical, Geller variation
1. c4 c5 2. Nf3 Nf6 3. d4 cxd4 4. Nxd4 e6 5. Nc3 Nc6 6. g3 Qb6 
******A34: English, symmetrical variation
English, symmetrical variation
1. c4 c5 2. Nc3
English, symmetrical, three knights system
1. c4 c5 2. Nc3 Nf6 3. Nf3 d5 4. cxd5 Nxd5 
English, symmetrical variation
1. c4 c5 2. Nc3 Nf6 3. g3
English, symmetrical, Rubinstein system
1. c4 c5 2. Nc3 Nf6 3. g3 d5 4. cxd5 Nxd5 5. Bg2 Nc7 
******A35: English, symmetrical variation
English, symmetrical variation
1. c4 c5 2. Nc3 Nc6 
English, symmetrical, four knights system
1. c4 c5 2. Nc3 Nc6 3. Nf3 Nf6 
******A36: English, symmetrical variation
English, symmetrical variation
1. c4 c5 2. Nc3 Nc6 3. g3
English, ultra-symmetrical variation
1. c4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 
English, symmetrical, Botvinnik system reversed
1. c4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. e3 e5 
English, symmetrical, Botvinnik system
1. c4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. e4
******A37: English, symmetrical variation
English, symmetrical variation
1. c4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. Nf3
English, symmetrical, Botvinnik system reversed
1. c4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. Nf3 e5 
******A38: English, symmetrical variation
English, symmetrical variation
1. c4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. Nf3 Nf6 
English, symmetrical, main line with d3
1. c4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. Nf3 Nf6 6. O-O O-O 7. d3
English, symmetrical, main line with b3
1. c4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. Nf3 Nf6 6. O-O O-O 7. b3
******A39: English, symmetrical, main line with d4
English, symmetrical, main line with d4
1. c4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. Nf3 Nf6 6. O-O O-O 7. d4
******A40: Queen's pawn
Queen's pawn
1. d4
Queen's pawn, Lundin (Kevitz-Mikenas) defence
1. d4 Nc6 
Queen's pawn, Charlick (Englund) gambit
1. d4 e5 
Queen's pawn, Englund gambit
1. d4 e5 2. dxe5 Nc6 3. Nf3 Qe7 4. Qd5 f6 5. exf6 Nxf6 
Queen's pawn, English defence
1. d4 b6 
Polish defence
1. d4 b5 
Queen's pawn
1. d4 e6 
Queen's pawn, Keres defence
1. d4 e6 2. c4 b6 
Queen's pawn, Franco-Indian (Keres) defence
1. d4 e6 2. c4 Bb4+ 
Modern defence
1. d4 g6 
Beefeater defence
1. d4 g6 2. c4 Bg7 3. Nc3 c5 4. d5 Bxc3+ 5. bxc3 f5 
******A41: Queen's Pawn
Queen's Pawn
1. d4 d6 
Old Indian, Tartakower (Wade) variation
1. d4 d6 2. Nf3 Bg4 
Old Indian defence
1. d4 d6 2. c4
Modern defence
1. d4 d6 2. c4 g6 3. Nc3 Bg7 
Robatsch defence, Rossolimo variation
1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. c4 Bg4 
******A42: Modern defence, Averbakh system
Modern defence, Averbakh system
1. d4 d6 2. c4 g6 3. Nc3 Bg7 4. e4
Pterodactyl defence
1. d4 d6 2. c4 g6 3. Nc3 Bg7 4. e4 c5 5. Nf3 Qa5 
Modern defence, Averbakh system, Randspringer variation
1. d4 d6 2. c4 g6 3. Nc3 Bg7 4. e4 f5 
Modern defence, Averbakh system, Kotov variation
1. d4 d6 2. c4 g6 3. Nc3 Bg7 4. e4 Nc6 
******A43: Old Benoni defence
Old Benoni defence
1. d4 c5 
Old Benoni, Franco-Benoni defence
1. d4 c5 2. d5 e6 3. e4
Old Benoni, Mujannah formation
1. d4 c5 2. d5 f5 
Old Benoni defence
1. d4 c5 2. d5 Nf6 
Woozle defence
1. d4 c5 2. d5 Nf6 3. Nc3 Qa5 
Old Benoni defence
1. d4 c5 2. d5 Nf6 3. Nf3
Hawk (Habichd) defence
1. d4 c5 2. d5 Nf6 3. Nf3 c4 
Old Benoni defence
1. d4 c5 2. d5 d6 
Old Benoni, Schmid's system
1. d4 c5 2. d5 d6 3. Nc3 g6 
******A44: Old Benoni defence
Old Benoni defence
1. d4 c5 2. d5 e5 
Semi-Benoni (`blockade variation')
1. d4 c5 2. d5 e5 3. e4 d6 
******A45: Queen's pawn game
Queen's pawn game
1. d4 Nf6 
Queen's pawn, Bronstein gambit
1. d4 Nf6 2. g4
Canard opening
1. d4 Nf6 2. f4
Paleface attack
1. d4 Nf6 2. f3
Blackmar-Diemer gambit
1. d4 Nf6 2. f3 d5 3. e4
Gedult attack
1. d4 Nf6 2. f3 d5 3. g4
Trompovsky attack (Ruth, Opovcensky opening)
1. d4 Nf6 2. Bg5
******A46: Queen's pawn game
Queen's pawn game
1. d4 Nf6 2. Nf3
Queen's pawn, Torre attack
1. d4 Nf6 2. Nf3 e6 3. Bg5
Queen's pawn, Torre attack, Wagner gambit
1. d4 Nf6 2. Nf3 e6 3. Bg5 c5 4. e4
Queen's pawn, Yusupov-Rubinstein system
1. d4 Nf6 2. Nf3 e6 3. e3
Doery defence
1. d4 Nf6 2. Nf3 Ne4 
******A47: Queen's Indian defence
Queen's Indian defence
1. d4 Nf6 2. Nf3 b6 
Queen's Indian, Marienbad system
1. d4 Nf6 2. Nf3 b6 3. g3 Bb7 4. Bg2 c5 
Queen's Indian, Marienbad system, Berg variation
1. d4 Nf6 2. Nf3 b6 3. g3 Bb7 4. Bg2 c5 5. c4 cxd4 6. Qxd4
******A48: King's Indian, East Indian defence
King's Indian, East Indian defence
1. d4 Nf6 2. Nf3 g6 
King's Indian, Torre attack
1. d4 Nf6 2. Nf3 g6 3. Bg5
King's Indian, London system
1. d4 Nf6 2. Nf3 g6 3. Bf4
******A49: King's Indian, fianchetto without c4
King's Indian, fianchetto without c4
1. d4 Nf6 2. Nf3 g6 3. g3
******A50: Queen's pawn game
Queen's pawn game
1. d4 Nf6 2. c4
Kevitz-Trajkovich defence
1. d4 Nf6 2. c4 Nc6 
Queen's Indian accelerated
1. d4 Nf6 2. c4 b6 
******A51: Budapest defence declined
Budapest defence declined
1. d4 Nf6 2. c4 e5 
Budapest, Fajarowicz variation
1. d4 Nf6 2. c4 e5 3. dxe5 Ne4 
Budapest, Fajarowicz, Steiner variation
1. d4 Nf6 2. c4 e5 3. dxe5 Ne4 4. Qc2
******A52: Budapest defence
Budapest defence
1. d4 Nf6 2. c4 e5 3. dxe5 Ng4 
Budapest, Adler variation
1. d4 Nf6 2. c4 e5 3. dxe5 Ng4 4. Nf3
Budapest, Rubinstein variation
1. d4 Nf6 2. c4 e5 3. dxe5 Ng4 4. Bf4
Budapest, Alekhine variation
1. d4 Nf6 2. c4 e5 3. dxe5 Ng4 4. e4
Budapest, Alekhine, Abonyi variation
1. d4 Nf6 2. c4 e5 3. dxe5 Ng4 4. e4 Nxe5 5. f4 Nec6 
Budapest, Alekhine variation, Balogh gambit
1. d4 Nf6 2. c4 e5 3. dxe5 Ng4 4. e4 d6 
******A53: Old Indian defence
Old Indian defence
1. d4 Nf6 2. c4 d6 
Old Indian, Janowski variation
1. d4 Nf6 2. c4 d6 3. Nc3 Bf5 
******A54: Old Indian, Ukrainian variation
Old Indian, Ukrainian variation
1. d4 Nf6 2. c4 d6 3. Nc3 e5 
Old Indian, Dus-Khotimirsky variation
1. d4 Nf6 2. c4 d6 3. Nc3 e5 4. e3 Nbd7 5. Bd3
Old Indian, Ukrainian variation, 4.Nf3
1. d4 Nf6 2. c4 d6 3. Nc3 e5 4. Nf3
******A55: Old Indian, main line
Old Indian, main line
1. d4 Nf6 2. c4 d6 3. Nc3 e5 4. Nf3 Nbd7 5. e4
******A56: Benoni defence
Benoni defence
1. d4 Nf6 2. c4 c5 
Benoni defence, Hromodka system
1. d4 Nf6 2. c4 c5 3. d5 d6 
Vulture defence
1. d4 Nf6 2. c4 c5 3. d5 Ne4 
Czech Benoni defence
1. d4 Nf6 2. c4 c5 3. d5 e5 
Czech Benoni, King's Indian system
1. d4 Nf6 2. c4 c5 3. d5 e5 4. Nc3 d6 5. e4 g6 
******A57: Benko gambit
Benko gambit
1. d4 Nf6 2. c4 c5 3. d5 b5 
Benko gambit half accepted
1. d4 Nf6 2. c4 c5 3. d5 b5 4. cxb5 a6 
Benko gambit, Zaitsev system
1. d4 Nf6 2. c4 c5 3. d5 b5 4. cxb5 a6 5. Nc3
Benko gambit, Nescafe Frappe attack
1. d4 Nf6 2. c4 c5 3. d5 b5 4. cxb5 a6 5. Nc3 axb5 6. e4 b4 7. Nb5 d6 8. Bc4
******A58: Benko gambit accepted
Benko gambit accepted
1. d4 Nf6 2. c4 c5 3. d5 b5 4. cxb5 a6 5. bxa6
Benko gambit, Nd2 variation
1. d4 Nf6 2. c4 c5 3. d5 b5 4. cxb5 a6 5. bxa6 Bxa6 6. Nc3 d6 7. Nf3 g6 8. Nd2
Benko gambit, fianchetto variation
1. d4 Nf6 2. c4 c5 3. d5 b5 4. cxb5 a6 5. bxa6 Bxa6 6. Nc3 d6 7. Nf3 g6 8. g3
******A59: Benko gambit, 7.e4
Benko gambit, 7.e4
1. d4 Nf6 2. c4 c5 3. d5 b5 4. cxb5 a6 5. bxa6 Bxa6 6. Nc3 d6 7. e4
Benko gambit, Ne2 variation
1. d4 Nf6 2. c4 c5 3. d5 b5 4. cxb5 a6 5. bxa6 Bxa6 6. Nc3 d6 7. e4 Bxf1 8. Kxf1 g6 9. Nge2
Benko gambit
1. d4 Nf6 2. c4 c5 3. d5 b5 4. cxb5 a6 5. bxa6 Bxa6 6. Nc3 d6 7. e4 Bxf1 8. Kxf1 g6 9. g3
Benko gambit, main line
1. d4 Nf6 2. c4 c5 3. d5 b5 4. cxb5 a6 5. bxa6 Bxa6 6. Nc3 d6 7. e4 Bxf1 8. Kxf1 g6 9. g3 Bg7 10. Kg2 O-O 11. Nf3
******A60: Benoni defence
Benoni defence
1. d4 Nf6 2. c4 c5 3. d5 e6 
******A61: Benoni defence
Benoni defence
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. Nf3 g6 
Benoni, Uhlmann variation
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. Nf3 g6 7. Bg5
Benoni, Nimzovich (knight's tour) variation
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. Nf3 g6 7. Nd2
Benoni, fianchetto variation
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. Nf3 g6 7. g3
******A62: Benoni, fianchetto variation
Benoni, fianchetto variation
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. Nf3 g6 7. g3 Bg7 8. Bg2 O-O 
******A63: Benoni, fianchetto, 9...Nbd7
Benoni, fianchetto, 9...Nbd7
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. Nf3 g6 7. g3 Bg7 8. Bg2 O-O 9. O-O Nbd7 
******A64: Benoni, fianchetto, 11...Re8
Benoni, fianchetto, 11...Re8
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. Nf3 g6 7. g3 Bg7 8. Bg2 O-O 9. O-O Nbd7 10. Nd2 a6 11. a4 Re8 
******A65: Benoni, 6.e4
Benoni, 6.e4
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4
******A66: Benoni, pawn storm variation
Benoni, pawn storm variation
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. f4
Benoni, Mikenas variation
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. f4 Bg7 8. e5
******A67: Benoni, Taimanov variation
Benoni, Taimanov variation
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. f4 Bg7 8. Bb5+
******A68: Benoni, four pawns attack
Benoni, four pawns attack
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. f4 Bg7 8. Nf3 O-O 
******A69: Benoni, four pawns attack, main line
Benoni, four pawns attack, main line
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. f4 Bg7 8. Nf3 O-O 9. Be2 Re8 
******A70: Benoni, classical with e4 and Nf3
Benoni, classical with e4 and Nf3
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. Nf3
Benoni, classical without 9.O-O
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. Nf3 Bg7 8. Be2
******A71: Benoni, classical, 8.Bg5
Benoni, classical, 8.Bg5
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. Nf3 Bg7 8. Bg5
******A72: Benoni, classical without 9.O-O
Benoni, classical without 9.O-O
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. Nf3 Bg7 8. Be2 O-O 
******A73: Benoni, classical, 9.O-O
Benoni, classical, 9.O-O
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. Nf3 Bg7 8. Be2 O-O 9. O-O
******A74: Benoni, classical, 9...a6, 10.a4
Benoni, classical, 9...a6, 10.a4
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. Nf3 Bg7 8. Be2 O-O 9. O-O a6 10. a4
******A75: Benoni, classical with ...a6 and 10...Bg4
Benoni, classical with ...a6 and 10...Bg4
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. Nf3 Bg7 8. Be2 O-O 9. O-O a6 10. a4 Bg4 
******A76: Benoni, classical, 9...Re8
Benoni, classical, 9...Re8
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. Nf3 Bg7 8. Be2 O-O 9. O-O Re8 
******A77: Benoni, classical, 9...Re8, 10.Nd2
Benoni, classical, 9...Re8, 10.Nd2
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. Nf3 Bg7 8. Be2 O-O 9. O-O Re8 10. Nd2
******A78: Benoni, classical with ...Re8 and ...Na6
Benoni, classical with ...Re8 and ...Na6
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. Nf3 Bg7 8. Be2 O-O 9. O-O Re8 10. Nd2 Na6 
******A79: Benoni, classical, 11.f3
Benoni, classical, 11.f3
1. d4 Nf6 2. c4 c5 3. d5 e6 4. Nc3 exd5 5. cxd5 d6 6. e4 g6 7. Nf3 Bg7 8. Be2 O-O 9. O-O Re8 10. Nd2 Na6 11. f3
******A80: Dutch
Dutch
1. d4 f5 
Dutch, Spielmann gambit
1. d4 f5 2. Nc3 Nf6 3. g4
Dutch, Manhattan (Alapin, Ulvestad) variation
1. d4 f5 2. Qd3
Dutch, Von Pretzel gambit
1. d4 f5 2. Qd3 e6 3. g4
Dutch, Korchnoi attack
1. d4 f5 2. h3
Dutch, Krejcik gambit
1. d4 f5 2. g4
Dutch, 2.Bg5 variation
1. d4 f5 2. Bg5
******A81: Dutch defence
Dutch defence
1. d4 f5 2. g3
Dutch defence, Blackburne variation
1. d4 f5 2. g3 Nf6 3. Bg2 e6 4. Nh3
Dutch defence
1. d4 f5 2. g3 Nf6 3. Bg2 g6 
Dutch, Leningrad, Basman system
1. d4 f5 2. g3 g6 3. Bg2 Bg7 4. Nf3 c6 5. O-O Nh6 
Dutch, Leningrad, Karlsbad variation
1. d4 f5 2. g3 g6 3. Bg2 Bg7 4. Nh3
******A82: Dutch, Staunton gambit
Dutch, Staunton gambit
1. d4 f5 2. e4
Dutch, Balogh defence
1. d4 f5 2. e4 d6 
Dutch, Staunton gambit
1. d4 f5 2. e4 fxe4 
Dutch, Staunton gambit, Tartakower variation
1. d4 f5 2. e4 fxe4 3. Nc3 Nf6 4. g4
******A83: Dutch, Staunton gambit, Staunton's line
Dutch, Staunton gambit, Staunton's line
1. d4 f5 2. e4 fxe4 3. Nc3 Nf6 4. Bg5
Dutch, Staunton gambit, Alekhine variation
1. d4 f5 2. e4 fxe4 3. Nc3 Nf6 4. Bg5 g6 5. h4
Dutch, Staunton gambit, Lasker variation
1. d4 f5 2. e4 fxe4 3. Nc3 Nf6 4. Bg5 g6 5. f3
Dutch, Staunton gambit, Chigorin variation
1. d4 f5 2. e4 fxe4 3. Nc3 Nf6 4. Bg5 c6 
Dutch, Staunton gambit, Nimzovich variation
1. d4 f5 2. e4 fxe4 3. Nc3 Nf6 4. Bg5 b6 
******A84: Dutch defence
Dutch defence
1. d4 f5 2. c4
Dutch defence, Bladel variation
1. d4 f5 2. c4 g6 3. Nc3 Nh6 
Dutch defence
1. d4 f5 2. c4 e6 
Dutch defence, Rubinstein variation
1. d4 f5 2. c4 e6 3. Nc3
Dutch, Staunton gambit deferred
1. d4 f5 2. c4 e6 3. e4
Dutch defence
1. d4 f5 2. c4 Nf6 
******A85: Dutch with c4 & Nc3
Dutch with c4 & Nc3
1. d4 f5 2. c4 Nf6 3. Nc3
******A86: Dutch with c4 & g3
Dutch with c4 & g3
1. d4 f5 2. c4 Nf6 3. g3
Dutch, Hort-Antoshin system
1. d4 f5 2. c4 Nf6 3. g3 d6 4. Bg2 c6 5. Nc3 Qc7 
Dutch, Leningrad variation
1. d4 f5 2. c4 Nf6 3. g3 g6 
******A87: Dutch, Leningrad, main variation
Dutch, Leningrad, main variation
1. d4 f5 2. c4 Nf6 3. g3 g6 4. Bg2 Bg7 5. Nf3
******A88: Dutch, Leningrad, main variation with c6
Dutch, Leningrad, main variation with c6
1. d4 f5 2. c4 Nf6 3. g3 g6 4. Bg2 Bg7 5. Nf3 O-O 6. O-O d6 7. Nc3 c6 
******A89: Dutch, Leningrad, main variation with Nc6
Dutch, Leningrad, main variation with Nc6
1. d4 f5 2. c4 Nf6 3. g3 g6 4. Bg2 Bg7 5. Nf3 O-O 6. O-O d6 7. Nc3 Nc6 
******A90: Dutch defence
Dutch defence
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2
Dutch defence, Dutch-Indian (Nimzo-Dutch) variation
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Bb4+ 
Dutch-Indian, Alekhine variation
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Bb4+ 5. Bd2 Be7 
******A91: Dutch defence
Dutch defence
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 
******A92: Dutch defence
Dutch defence
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 5. Nf3 O-O 
Dutch defence, Alekhine variation
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 5. Nf3 O-O 6. O-O Ne4 
Dutch, stonewall variation
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 5. Nf3 O-O 6. O-O d5 
Dutch, stonewall with Nc3
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 5. Nf3 O-O 6. O-O d5 7. Nc3
******A93: Dutch, stonewall, Botwinnik variation
Dutch, stonewall, Botwinnik variation
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 5. Nf3 O-O 6. O-O d5 7. b3
******A94: Dutch, stonewall with Ba3
Dutch, stonewall with Ba3
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 5. Nf3 O-O 6. O-O d5 7. b3 c6 8. Ba3
******A95: Dutch, stonewall with Nc3
Dutch, stonewall with Nc3
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 5. Nf3 O-O 6. O-O d5 7. Nc3 c6 
Dutch, stonewall: Chekhover variation
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 5. Nf3 O-O 6. O-O d5 7. Nc3 c6 8. Qc2 Qe8 9. Bg5
******A96: Dutch, classical variation
Dutch, classical variation
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 5. Nf3 O-O 6. O-O d6 
******A97: Dutch, Ilyin-Genevsky variation
Dutch, Ilyin-Genevsky variation
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 5. Nf3 O-O 6. O-O d6 7. Nc3 Qe8 
Dutch, Ilyin-Genevsky, Winter variation
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 5. Nf3 O-O 6. O-O d6 7. Nc3 Qe8 8. Re1
******A98: Dutch, Ilyin-Genevsky variation with Qc2
Dutch, Ilyin-Genevsky variation with Qc2
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 5. Nf3 O-O 6. O-O d6 7. Nc3 Qe8 8. Qc2
******A99: Dutch, Ilyin-Genevsky variation with b3
Dutch, Ilyin-Genevsky variation with b3
1. d4 f5 2. c4 Nf6 3. g3 e6 4. Bg2 Be7 5. Nf3 O-O 6. O-O d6 7. Nc3 Qe8 8. b3
******B00: King's pawn opening
King's pawn opening
1. e4
Hippopotamus defence
1. e4 Nh6 2. d4 g6 3. c4 f6 
Corn stalk defence
1. e4 a5 
Lemming defence
1. e4 Na6 
Fred
1. e4 f5 
Barnes defence
1. e4 f6 
Fried fox defence
1. e4 f6 2. d4 Kf7 
Carr's defence
1. e4 h6 
Reversed Grob (Borg/Basman defence/macho Grob)
1. e4 g5 
St. George (Baker) defence
1. e4 a6 
Owen defence
1. e4 b6 
Guatemala defence
1. e4 b6 2. d4 Ba6 
KP, Nimzovich defence
1. e4 Nc6 
KP, Nimzovich defence, Wheeler gambit
1. e4 Nc6 2. b4 Nxb4 3. c3 Nc6 4. d4
KP, Nimzovich defence
1. e4 Nc6 2. Nf3
KP, Colorado counter
1. e4 Nc6 2. Nf3 f5 
KP, Nimzovich defence
1. e4 Nc6 2. d4
KP, Nimzovich defence, Marshall gambit
1. e4 Nc6 2. d4 d5 3. exd5 Qxd5 4. Nc3
KP, Nimzovich defence, Bogolyubov variation
1. e4 Nc6 2. d4 d5 3. Nc3
KP, Neo-Mongoloid defence
1. e4 Nc6 2. d4 f6 
******B01: Scandinavian (centre counter) defence
Scandinavian (centre counter) defence
1. e4 d5 
Scandinavian defence, Lasker variation
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qa5 4. d4 Nf6 5. Nf3 Bg4 6. h3
Scandinavian defence
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qa5 4. d4 Nf6 5. Nf3 Bf5 
Scandinavian defence, Gruenfeld variation
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qa5 4. d4 Nf6 5. Nf3 Bf5 6. Ne5 c6 7. g4
Scandinavian, Anderssen counter-attack
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qa5 4. d4 e5 
Scandinavian, Anderssen counter-attack orthodox attack
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qa5 4. d4 e5 5. dxe5 Bb4 6. Bd2 Nc6 7. Nf3
Scandinavian, Anderssen counter-attack, Goteborg system
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qa5 4. d4 e5 5. Nf3
Scandinavian, Anderssen counter-attack, Collijn variation
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qa5 4. d4 e5 5. Nf3 Bg4 
Scandinavian, Mieses-Kotrvc gambit
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qa5 4. b4
Scandinavian, Pytel-Wade variation
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qd6 
Scandinavian defence
1. e4 d5 2. exd5 Nf6 
Scandinavian, Icelandic gambit
1. e4 d5 2. exd5 Nf6 3. c4 e6 
Scandinavian gambit
1. e4 d5 2. exd5 Nf6 3. c4 c6 
Scandinavian defence
1. e4 d5 2. exd5 Nf6 3. d4
Scandinavian, Marshall variation
1. e4 d5 2. exd5 Nf6 3. d4 Nxd5 
Scandinavian, Kiel variation
1. e4 d5 2. exd5 Nf6 3. d4 Nxd5 4. c4 Nb4 
Scandinavian, Richter variation
1. e4 d5 2. exd5 Nf6 3. d4 g6 
******B02: Alekhine's defence
Alekhine's defence
1. e4 Nf6 
Alekhine's defence, Scandinavian variation
1. e4 Nf6 2. Nc3 d5 
Alekhine's defence, Spielmann variation
1. e4 Nf6 2. Nc3 d5 3. e5 Nfd7 4. e6
Alekhine's defence, Maroczy variation
1. e4 Nf6 2. d3
Alekhine's defence, Krejcik variation
1. e4 Nf6 2. Bc4
Alekhine's defence, Mokele Mbembe (Buecker) variation
1. e4 Nf6 2. e5 Ne4 
Alekhine's defence, Brooklyn defence
1. e4 Nf6 2. e5 Ng8 
Alekhine's defence
1. e4 Nf6 2. e5 Nd5 
Alekhine's defence, Kmoch variation
1. e4 Nf6 2. e5 Nd5 3. Bc4 Nb6 4. Bb3 c5 5. d3
Alekhine's defence, Saemisch attack
1. e4 Nf6 2. e5 Nd5 3. Nc3
Alekhine's defence, Welling variation
1. e4 Nf6 2. e5 Nd5 3. b3
Alekhine's defence
1. e4 Nf6 2. e5 Nd5 3. c4
Alekhine's defence, Steiner variation
1. e4 Nf6 2. e5 Nd5 3. c4 Nb6 4. b3
Alekhine's defence, two pawns' (Lasker's) attack
1. e4 Nf6 2. e5 Nd5 3. c4 Nb6 4. c5
Alekhine's defence, two pawns' attack, Mikenas variation
1. e4 Nf6 2. e5 Nd5 3. c4 Nb6 4. c5 Nd5 5. Bc4 e6 6. Nc3 d6 
******B03: Alekhine's defence
Alekhine's defence
1. e4 Nf6 2. e5 Nd5 3. d4
Alekhine's defence, O'Sullivan gambit
1. e4 Nf6 2. e5 Nd5 3. d4 b5 
Alekhine's defence
1. e4 Nf6 2. e5 Nd5 3. d4 d6 
Alekhine's defence, Balogh variation
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. Bc4
Alekhine's defence
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. c4
Alekhine's defence, exchange variation
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. c4 Nb6 5. exd6
Alekhine's defence, exchange, Karpov variation
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. c4 Nb6 5. exd6 cxd6 6. Nf3 g6 7. Be2 Bg7 8. O-O O-O 9. h3 Nc6 10. Nc3 Bf5 11. Bf4
Alekhine's defence, four pawns attack
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. c4 Nb6 5. f4
Alekhine's defence, four pawns attack, Korchnoi variation
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. c4 Nb6 5. f4 dxe5 6. fxe5 Bf5 7. Nc3 e6 8. Nf3 Be7 9. Be2 O-O 10. O-O f6 
Alekhine's defence, four pawns attack, 6...Nc6
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. c4 Nb6 5. f4 dxe5 6. fxe5 Nc6 
Alekhine's defence, four pawns attack, Ilyin-Genevsky var.
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. c4 Nb6 5. f4 dxe5 6. fxe5 Nc6 7. Nf3 Bg4 8. e6 fxe6 9. c5
Alekhine's defence, four pawns attack, 7.Be3
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. c4 Nb6 5. f4 dxe5 6. fxe5 Nc6 7. Be3
Alekhine's defence, four pawns attack, Tartakower variation
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. c4 Nb6 5. f4 dxe5 6. fxe5 Nc6 7. Be3 Bf5 8. Nc3 e6 9. Nf3 Qd7 10. Be2 O-O-O 11. O-O Be7 
Alekhine's defence, four pawns attack, Planinc variation
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. c4 Nb6 5. f4 g5 
Alekhine's defence, four pawns attack, fianchetto variation
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. c4 Nb6 5. f4 g6 
Alekhine's defence, four pawns attack, Trifunovic variation
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. c4 Nb6 5. f4 Bf5 
******B04: Alekhine's defence, modern variation
Alekhine's defence, modern variation
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. Nf3
Alekhine's defence, modern, Larsen variation
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. Nf3 dxe5 
Alekhine's defence, modern, Schmid variation
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. Nf3 Nb6 
Alekhine's defence, modern, fianchetto variation
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. Nf3 g6 
Alekhine's defence, modern, Keres variation
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. Nf3 g6 5. Bc4 Nb6 6. Bb3 Bg7 7. a4
******B05: Alekhine's defence, modern variation, 4...Bg4
Alekhine's defence, modern variation, 4...Bg4
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. Nf3 Bg4 
Alekhine's defence, modern, Flohr variation
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. Nf3 Bg4 5. Be2 c6 
Alekhine's defence, modern, Panov variation
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. Nf3 Bg4 5. h3
Alekhine's defence, modern, Alekhine variation
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. Nf3 Bg4 5. c4
Alekhine's defence, modern, Vitolins attack
1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. Nf3 Bg4 5. c4 Nb6 6. d5
******B06: Robatsch (modern) defence
Robatsch (modern) defence
1. e4 g6 
Norwegian defence
1. e4 g6 2. d4 Nf6 3. e5 Nh5 4. g4 Ng7 
Robatsch (modern) defence
1. e4 g6 2. d4 Bg7 
Robatsch defence, three pawns attack
1. e4 g6 2. d4 Bg7 3. f4
Robatsch defence
1. e4 g6 2. d4 Bg7 3. Nc3
Robatsch defence, Gurgenidze variation
1. e4 g6 2. d4 Bg7 3. Nc3 c6 4. f4 d5 5. e5 h5 
Robatsch (modern) defence
1. e4 g6 2. d4 Bg7 3. Nc3 d6 
Robatsch defence, two knights variation
1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Nf3
Robatsch defence, two knights, Suttles variation
1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Nf3 c6 
Robatsch defence, Pseudo-Austrian attack
1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. f4
******B07: Pirc defence
Pirc defence
1. e4 d6 2. d4 Nf6 3. Nc3
Pirc, Ufimtsev-Pytel variation
1. e4 d6 2. d4 Nf6 3. Nc3 c6 
Pirc defence
1. e4 d6 2. d4 Nf6 3. Nc3 g6 
Pirc, 150 attack
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. Be3 c6 5. Qd2
Pirc, Sveshnikov system
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. g3
Pirc, Holmov system
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. Bc4
Pirc, Byrne variation
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. Bg5
Pirc defence
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. Be2
Pirc, Chinese variation
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. Be2 Bg7 5. g4
Pirc, bayonet (Mariotti) attack
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. Be2 Bg7 5. h4
Robatsch defence, Geller's system
1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. c3
******B08: Pirc, classical (two knights) system
Pirc, classical (two knights) system
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. Nf3
Pirc, classical (two knights) system
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. Nf3 Bg7 
Pirc, classical, h3 system
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. Nf3 Bg7 5. h3
Pirc, classical system, 5.Be2
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. Nf3 Bg7 5. Be2
******B09: Pirc, Austrian attack
Pirc, Austrian attack
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. f4
Pirc, Austrian attack
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. f4 Bg7 5. Nf3 O-O 
Pirc, Austrian attack, 6.e5
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. f4 Bg7 5. Nf3 O-O 6. e5
Pirc, Austrian attack, 6.Be3
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. f4 Bg7 5. Nf3 O-O 6. Be3
Pirc, Austrian attack, 6.Bd3
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. f4 Bg7 5. Nf3 O-O 6. Bd3
Pirc, Austrian attack, dragon formation
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. f4 Bg7 5. Nf3 c5 
Pirc, Austrian attack, Ljubojevic variation
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. f4 Bg7 5. Bc4
******B10: Caro-Kann defence
Caro-Kann defence
1. e4 c6 
Caro-Kann, Hillbilly attack
1. e4 c6 2. Bc4
Caro-Kann, anti-Caro-Kann defence
1. e4 c6 2. c4
Caro-Kann, anti-anti-Caro-Kann defence
1. e4 c6 2. c4 d5 
Caro-Kann, closed (Breyer) variation
1. e4 c6 2. d3
Caro-Kann defence
1. e4 c6 2. Nc3
Caro-Kann, Goldman (Spielmann) variation
1. e4 c6 2. Nc3 d5 3. Qf3
Caro-Kann, two knights variation
1. e4 c6 2. Nc3 d5 3. Nf3
******B11: Caro-Kann, two knights, 3...Bg4
Caro-Kann, two knights, 3...Bg4
1. e4 c6 2. Nc3 d5 3. Nf3 Bg4 
******B12: Caro-Kann defence
Caro-Kann defence
1. e4 c6 2. d4
de Bruycker defence
1. e4 c6 2. d4 Na6 3. Nc3 Nc7 
Caro-Masi defence
1. e4 c6 2. d4 Nf6 
Caro-Kann defence
1. e4 c6 2. d4 d5 
Caro-Kann, Tartakower (fantasy) variation
1. e4 c6 2. d4 d5 3. f3
Caro-Kann, 3.Nd2
1. e4 c6 2. d4 d5 3. Nd2
Caro-Kann, Edinburgh variation
1. e4 c6 2. d4 d5 3. Nd2 Qb6 
Caro-Kann, advance variation
1. e4 c6 2. d4 d5 3. e5
Caro-Kann, advance, Short variation
1. e4 c6 2. d4 d5 3. e5 Bf5 4. c3 e6 5. Be2
******B13: Caro-Kann, exchange variation
Caro-Kann, exchange variation
1. e4 c6 2. d4 d5 3. exd5
Caro-Kann, exchange, Rubinstein variation
1. e4 c6 2. d4 d5 3. exd5 cxd5 4. Bd3 Nc6 5. c3 Nf6 6. Bf4
Caro-Kann, Panov-Botvinnik attack
1. e4 c6 2. d4 d5 3. exd5 cxd5 4. c4
Caro-Kann, Panov-Botvinnik, Gunderam attack
1. e4 c6 2. d4 d5 3. exd5 cxd5 4. c4 Nf6 5. c5
Caro-Kann, Panov-Botvinnik attack
1. e4 c6 2. d4 d5 3. exd5 cxd5 4. c4 Nf6 5. Nc3
Caro-Kann, Panov-Botvinnik, Herzog defence
1. e4 c6 2. d4 d5 3. exd5 cxd5 4. c4 Nf6 5. Nc3 Nc6 6. Bg5 dxc4 7. d5 Na5 
Caro-Kann, Panov-Botvinnik, normal variation
1. e4 c6 2. d4 d5 3. exd5 cxd5 4. c4 Nf6 5. Nc3 Nc6 6. Bg5 e6 
Caro-Kann, Panov-Botvinnik, Czerniak variation
1. e4 c6 2. d4 d5 3. exd5 cxd5 4. c4 Nf6 5. Nc3 Nc6 6. Bg5 Qa5 
Caro-Kann, Panov-Botvinnik, Reifir (Spielmann) variation
1. e4 c6 2. d4 d5 3. exd5 cxd5 4. c4 Nf6 5. Nc3 Nc6 6. Bg5 Qb6 
******B14: Caro-Kann, Panov-Botvinnik attack, 5...e6
Caro-Kann, Panov-Botvinnik attack, 5...e6
1. e4 c6 2. d4 d5 3. exd5 cxd5 4. c4 Nf6 5. Nc3 e6 
Caro-Kann, Panov-Botvinnik attack, 5...g6
1. e4 c6 2. d4 d5 3. exd5 cxd5 4. c4 Nf6 5. Nc3 g6 
******B15: Caro-Kann defence
Caro-Kann defence
1. e4 c6 2. d4 d5 3. Nc3
Caro-Kann, Gurgenidze counter-attack
1. e4 c6 2. d4 d5 3. Nc3 b5 
Caro-Kann, Gurgenidze system
1. e4 c6 2. d4 d5 3. Nc3 g6 
Caro-Kann, Rasa-Studier gambit
1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. f3
Caro-Kann defence
1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4
Caro-Kann, Alekhine gambit
1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Nf6 5. Bd3
Caro-Kann, Tartakower (Nimzovich) variation
1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Nf6 5. Nxf6+ exf6 
Caro-Kann, Forgacs variation
1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Nf6 5. Nxf6+ exf6 6. Bc4
******B16: Caro-Kann, Bronstein-Larsen variation
Caro-Kann, Bronstein-Larsen variation
1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Nf6 5. Nxf6+ gxf6 
******B17: Caro-Kann, Steinitz variation
Caro-Kann, Steinitz variation
1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Nd7 
******B18: Caro-Kann, classical variation
Caro-Kann, classical variation
1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Bf5 
Caro-Kann, classical, Flohr variation
1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Bf5 5. Ng3 Bg6 6. Nh3
Caro-Kann, classical, Maroczy attack
1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Bf5 5. Ng3 Bg6 6. f4
Caro-Kann, classical, 6.h4
1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Bf5 5. Ng3 Bg6 6. h4
******B19: Caro-Kann, classical, 7...Nd7
Caro-Kann, classical, 7...Nd7
1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Bf5 5. Ng3 Bg6 6. h4 h6 7. Nf3 Nd7 
Caro-Kann, classical, Spassky variation
1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Bf5 5. Ng3 Bg6 6. h4 h6 7. Nf3 Nd7 8. h5
******B20: Sicilian defence
Sicilian defence
1. e4 c5 
Sicilian, Gloria variation
1. e4 c5 2. c4 d6 3. Nc3 Nc6 4. g3 h5 
Sicilian, Steinitz variation
1. e4 c5 2. g3
Sicilian, wing gambit
1. e4 c5 2. b4
Sicilian, wing gambit, Santasiere variation
1. e4 c5 2. b4 cxb4 3. c4
Sicilian, wing gambit, Marshall variation
1. e4 c5 2. b4 cxb4 3. a3
Sicilian, wing gambit, Marienbad variation
1. e4 c5 2. b4 cxb4 3. a3 d5 4. exd5 Qxd5 5. Bb2
Sicilian, wing gambit, Carlsbad variation
1. e4 c5 2. b4 cxb4 3. a3 bxa3 
Sicilian, Keres variation (2.Ne2)
1. e4 c5 2. Ne2
******B21: Sicilian, Grand Prix attack
Sicilian, Grand Prix attack
1. e4 c5 2. f4
Sicilian, Smith-Morra gambit
1. e4 c5 2. d4
Sicilian, Andreaschek gambit
1. e4 c5 2. d4 cxd4 3. Nf3 e5 4. c3
Sicilian, Smith-Morra gambit, 2...cxd4 3.c3
1. e4 c5 2. d4 cxd4 3. c3
Sicilian, Smith-Morra gambit, Chicago defence
1. e4 c5 2. d4 cxd4 3. c3 dxc3 4. Nxc3 Nc6 5. Nf3 d6 6. Bc4 e6 7. O-O a6 8. Qe2 b5 9. Bb3 Ra7 
******B22: Sicilian, Alapin's variation (2.c3)
Sicilian, Alapin's variation (2.c3)
1. e4 c5 2. c3
Sicilian, 2.c3, Heidenfeld variation
1. e4 c5 2. c3 Nf6 3. e5 Nd5 4. Nf3 Nc6 5. Na3
******B23: Sicilian, closed
Sicilian, closed
1. e4 c5 2. Nc3
Sicilian, closed, Korchnoi variation
1. e4 c5 2. Nc3 e6 3. g3 d5 
Sicilian, closed, 2...Nc6
1. e4 c5 2. Nc3 Nc6 
Sicilian, chameleon variation
1. e4 c5 2. Nc3 Nc6 3. Nge2
Sicilian, Grand Prix attack
1. e4 c5 2. Nc3 Nc6 3. f4
Sicilian, Grand Prix attack, Schofman variation
1. e4 c5 2. Nc3 Nc6 3. f4 g6 4. Nf3 Bg7 5. Bc4 e6 6. f5
******B24: Sicilian, closed
Sicilian, closed
1. e4 c5 2. Nc3 Nc6 3. g3
Sicilian, closed, Smyslov variation
1. e4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. d3 e6 6. Be3 Nd4 7. Nce2
******B25: Sicilian, closed
Sicilian, closed
1. e4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. d3 d6 
Sicilian, closed, 6.Ne2 e5 (Botvinnik)
1. e4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. d3 d6 6. Nge2 e5 
Sicilian, closed, 6.f4
1. e4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. d3 d6 6. f4
Sicilian, closed, 6.f4 e5 (Botvinnik)
1. e4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. d3 d6 6. f4 e5 
******B26: Sicilian, closed, 6.Be3
Sicilian, closed, 6.Be3
1. e4 c5 2. Nc3 Nc6 3. g3 g6 4. Bg2 Bg7 5. d3 d6 6. Be3
******B27: Sicilian defence
Sicilian defence
1. e4 c5 2. Nf3
Sicilian, Stiletto (Althouse) variation
1. e4 c5 2. Nf3 Qa5 
Sicilian, Quinteros variation
1. e4 c5 2. Nf3 Qc7 
Sicilian, Katalimov variation
1. e4 c5 2. Nf3 b6 
Sicilian, Hungarian variation
1. e4 c5 2. Nf3 g6 
Sicilian, Acton extension
1. e4 c5 2. Nf3 g6 3. c4 Bh6 
******B28: Sicilian, O'Kelly variation
Sicilian, O'Kelly variation
1. e4 c5 2. Nf3 a6 
******B29: Sicilian, Nimzovich-Rubinstein variation
Sicilian, Nimzovich-Rubinstein variation
1. e4 c5 2. Nf3 Nf6 
Sicilian, Nimzovich-Rubinstein; Rubinstein counter-gambit
1. e4 c5 2. Nf3 Nf6 3. e5 Nd5 4. Nc3 e6 5. Nxd5 exd5 6. d4 Nc6 
******B30: Sicilian defence
Sicilian defence
1. e4 c5 2. Nf3 Nc6 
Sicilian, Nimzovich-Rossolimo attack (without ...d6)
1. e4 c5 2. Nf3 Nc6 3. Bb5
******B31: Sicilian, Nimzovich-Rossolimo attack (with ...g6, without ...d6)
Sicilian, Nimzovich-Rossolimo attack (with ...g6, without ...d6)
1. e4 c5 2. Nf3 Nc6 3. Bb5 g6 
Sicilian, Nimzovich-Rossolimo attack, Gurgenidze variation
1. e4 c5 2. Nf3 Nc6 3. Bb5 g6 4. O-O Bg7 5. Re1 e5 6. b4
******B32: Sicilian defence
Sicilian defence
1. e4 c5 2. Nf3 Nc6 3. d4
Sicilian, Flohr variation
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 Qc7 
Sicilian, Nimzovich variation
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 d5 
Sicilian, Labourdonnais-Loewenthal variation
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 e5 
Sicilian, Labourdonnais-Loewenthal (Kalashnikov) variation
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 e5 5. Nb5 d6 
******B33: Sicilian defence
Sicilian defence
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 Nf6 
Sicilian, Pelikan (Lasker/Sveshnikov) variation
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e5 
Sicilian, Pelikan, Bird variation
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e5 6. Ndb5 d6 7. Bg5 a6 8. Na3 Be6 
Sicilian, Pelikan, Chelyabinsk variation
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e5 6. Ndb5 d6 7. Bg5 a6 8. Na3 b5 
Sicilian, Sveshnikov variation
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e5 6. Ndb5 d6 7. Bg5 a6 8. Na3 b5 9. Bxf6 gxf6 10. Nd5 f5 
******B34: Sicilian, accelerated fianchetto, exchange variation
Sicilian, accelerated fianchetto, exchange variation
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 g6 5. Nxc6
Sicilian, accelerated fianchetto, modern variation
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 g6 5. Nc3
******B35: Sicilian, accelerated fianchetto, modern variation with Bc4
Sicilian, accelerated fianchetto, modern variation with Bc4
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 g6 5. Nc3 Bg7 6. Be3 Nf6 7. Bc4
******B36: Sicilian, accelerated fianchetto, Maroczy bind
Sicilian, accelerated fianchetto, Maroczy bind
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 g6 5. c4
Sicilian, accelerated fianchetto, Gurgenidze variation
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 g6 5. c4 Nf6 6. Nc3 Nxd4 7. Qxd4 d6 
******B37: Sicilian, accelerated fianchetto, Maroczy bind, 5...Bg7
Sicilian, accelerated fianchetto, Maroczy bind, 5...Bg7
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 g6 5. c4 Bg7 
Sicilian, accelerated fianchetto, Simagin variation
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 g6 5. c4 Bg7 6. Nc2 d6 7. Be2 Nh6 
******B38: Sicilian, accelerated fianchetto, Maroczy bind, 6.Be3
Sicilian, accelerated fianchetto, Maroczy bind, 6.Be3
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 g6 5. c4 Bg7 6. Be3
******B39: Sicilian, accelerated fianchetto, Breyer variation
Sicilian, accelerated fianchetto, Breyer variation
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 g6 5. c4 Bg7 6. Be3 Nf6 7. Nc3 Ng4 
******B40: Sicilian defence
Sicilian defence
1. e4 c5 2. Nf3 e6 
Sicilian, Marshall variation
1. e4 c5 2. Nf3 e6 3. d4 d5 
Sicilian defence
1. e4 c5 2. Nf3 e6 3. d4 cxd4 
Sicilian, Anderssen variation
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nf6 
Sicilian, Pin variation (Sicilian counter-attack)
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Bb4 
Sicilian, Pin, Jaffe variation
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Bb4 6. Bd3 e5 
Sicilian, Pin, Koch variation
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Bb4 6. e5
******B41: Sicilian, Kan variation
Sicilian, Kan variation
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 a6 
Sicilian, Kan, Maroczy bind (Reti variation)
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 a6 5. c4
Sicilian, Kan, Maroczy bind - Bronstein variation
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 a6 5. c4 Nf6 6. Nc3 Bb4 7. Bd3 Nc6 8. Bc2
******B42: Sicilian, Kan, 5.Bd3
Sicilian, Kan, 5.Bd3
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 a6 5. Bd3
Sicilian, Kan, Gipslis variation
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 a6 5. Bd3 Nf6 6. O-O d6 7. c4 g6 
Sicilian, Kan, Polugaievsky variation
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 a6 5. Bd3 Bc5 
Sicilian, Kan, Swiss cheese variation
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 a6 5. Bd3 g6 
******B43: Sicilian, Kan, 5.Nc3
Sicilian, Kan, 5.Nc3
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 a6 5. Nc3
******B44: Sicilian defence
Sicilian defence
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nc6 
Sicilian, Szen (`anti-Taimanov') variation
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nc6 5. Nb5
Sicilian, Szen, hedgehog variation
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nc6 5. Nb5 d6 6. c4 Nf6 7. Nb1-c3 a6 8. Na3 Be7 9. Be2 O-O 10. O-O b6 
Sicilian, Szen variation, Dely-Kasparov gambit
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nc6 5. Nb5 d6 6. c4 Nf6 7. Nb1-c3 a6 8. Na3 d5 
******B45: Sicilian, Taimanov variation
Sicilian, Taimanov variation
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nc6 5. Nc3
Sicilian, Taimanov, American attack
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nc6 5. Nc3 Nf6 6. Ndb5 Bb4 7. Nd6+
******B46: Sicilian, Taimanov variation
Sicilian, Taimanov variation
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nc6 5. Nc3 a6 
******B47: Sicilian, Taimanov (Bastrikov) variation
Sicilian, Taimanov (Bastrikov) variation
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nc6 5. Nc3 Qc7 
******B48: Sicilian, Taimanov variation
Sicilian, Taimanov variation
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nc6 5. Nc3 Qc7 6. Be3
******B49: Sicilian, Taimanov variation
Sicilian, Taimanov variation
1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nc6 5. Nc3 Qc7 6. Be3 a6 7. Be2
******B50: Sicilian
Sicilian
1. e4 c5 2. Nf3 d6 
Sicilian, wing gambit deferred
1. e4 c5 2. Nf3 d6 3. b4
******B51: Sicilian, Canal-Sokolsky (Nimzovich-Rossolimo, Moscow) attack
Sicilian, Canal-Sokolsky (Nimzovich-Rossolimo, Moscow) attack
1. e4 c5 2. Nf3 d6 3. Bb5+
******B52: Sicilian, Canal-Sokolsky attack, 3...Bd7
Sicilian, Canal-Sokolsky attack, 3...Bd7
1. e4 c5 2. Nf3 d6 3. Bb5+ Bd7 
Sicilian, Canal-Sokolsky attack, Bronstein gambit
1. e4 c5 2. Nf3 d6 3. Bb5+ Bd7 4. Bxd7+ Qxd7 5. O-O Nc6 6. c3 Nf6 7. d4
Sicilian, Canal-Sokolsky attack, Sokolsky variation
1. e4 c5 2. Nf3 d6 3. Bb5+ Bd7 4. Bxd7+ Qxd7 5. c4
******B53: Sicilian, Chekhover variation
Sicilian, Chekhover variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Qxd4
Sicilian, Chekhover, Zaitsev variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Qxd4 Nc6 5. Bb5 Qd7 
******B54: Sicilian
Sicilian
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4
Sicilian, Prins (Moscow) variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. f3
******B55: Sicilian, Prins variation, Venice attack
Sicilian, Prins variation, Venice attack
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. f3 e5 6. Bb5+
******B56: Sicilian
Sicilian
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3
Sicilian, Venice attack
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e5 6. Bb5+
Sicilian
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 
******B57: Sicilian, Sozin, not Scheveningen
Sicilian, Sozin, not Scheveningen
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bc4
Sicilian, Magnus Smith trap
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bc4 g6 7. Nxc6 bxc6 8. e5
Sicilian, Sozin, Benko variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bc4 Qb6 
******B58: Sicilian, classical
Sicilian, classical
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 d6 6. Be2
Sicilian, Boleslavsky variation
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 d6 6. Be2 e5 
Sicilian, Boleslavsky, Louma variation
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 d6 6. Be2 e5 7. Nxc6
******B59: Sicilian, Boleslavsky variation, 7.Nb3
Sicilian, Boleslavsky variation, 7.Nb3
1. e4 c5 2. Nf3 Nc6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 d6 6. Be2 e5 7. Nb3
******B60: Sicilian, Richter-Rauzer
Sicilian, Richter-Rauzer
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5
Sicilian, Richter-Rauzer, Bondarevsky variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 g6 
Sicilian, Richter-Rauzer, Larsen variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 Bd7 
******B61: Sicilian, Richter-Rauzer, Larsen variation, 7.Qd2
Sicilian, Richter-Rauzer, Larsen variation, 7.Qd2
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 Bd7 7. Qd2
******B62: Sicilian, Richter-Rauzer, 6...e6
Sicilian, Richter-Rauzer, 6...e6
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 
Sicilian, Richter-Rauzer, Podvebrady variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Nb3
Sicilian, Richter-Rauzer, Margate (Alekhine) variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Bb5
Sicilian, Richter-Rauzer, Richter attack
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Nxc6
Sicilian, Richter-Rauzer, Keres variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Qd3
******B63: Sicilian, Richter-Rauzer, Rauzer attack
Sicilian, Richter-Rauzer, Rauzer attack
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Qd2
Sicilian, Richter-Rauzer, Rauzer attack, 7...Be7
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Qd2 Be7 
******B64: Sicilian, Richter-Rauzer, Rauzer attack, 7...Be7 defence, 9.f4
Sicilian, Richter-Rauzer, Rauzer attack, 7...Be7 defence, 9.f4
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Qd2 Be7 8. O-O-O O-O 9. f4
Sicilian, Richter-Rauzer, Rauzer attack, Geller variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Qd2 Be7 8. O-O-O O-O 9. f4 e5 
******B65: Sicilian, Richter-Rauzer, Rauzer attack, 7...Be7 defence, 9...Nxd4
Sicilian, Richter-Rauzer, Rauzer attack, 7...Be7 defence, 9...Nxd4
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Qd2 Be7 8. O-O-O O-O 9. f4 Nxd4 
Sicilian, Richter-Rauzer, Rauzer attack, 7...Be7 defence, 9...Nxd4
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Qd2 Be7 8. O-O-O O-O 9. f4 Nxd4 10. Qxd4
******B66: Sicilian, Richter-Rauzer, Rauzer attack, 7...a6
Sicilian, Richter-Rauzer, Rauzer attack, 7...a6
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Qd2 a6 
******B67: Sicilian, Richter-Rauzer, Rauzer attack, 7...a6 defence, 8...Bd7
Sicilian, Richter-Rauzer, Rauzer attack, 7...a6 defence, 8...Bd7
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Qd2 a6 8. O-O-O Bd7 
******B68: Sicilian, Richter-Rauzer, Rauzer attack, 7...a6 defence, 9...Be7
Sicilian, Richter-Rauzer, Rauzer attack, 7...a6 defence, 9...Be7
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Qd2 a6 8. O-O-O Bd7 9. f4 Be7 
******B69: Sicilian, Richter-Rauzer, Rauzer attack, 7...a6 defence, 11.Bxf6
Sicilian, Richter-Rauzer, Rauzer attack, 7...a6 defence, 11.Bxf6
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e6 7. Qd2 a6 8. O-O-O Bd7 9. f4 Be7 10. Nf3 b5 11. Bxf6
******B70: Sicilian, dragon variation
Sicilian, dragon variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 
******B71: Sicilian, dragon, Levenfish variation
Sicilian, dragon, Levenfish variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. f4
Sicilian, dragon, Levenfish; Flohr variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. f4 Nbd7 
******B72: Sicilian, dragon, 6.Be3
Sicilian, dragon, 6.Be3
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3
Sicilian, dragon, classical attack
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Be2
Sicilian, dragon, classical, Amsterdam variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Be2 Nc6 8. Qd2
Sicilian, dragon, classical, Grigoriev variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Be2 Nc6 8. Qd2 O-O 9. O-O-O
Sicilian, dragon, classical, Nottingham variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Be2 Nc6 8. Nb3
******B73: Sicilian, dragon, classical, 8.O-O
Sicilian, dragon, classical, 8.O-O
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Be2 Nc6 8. O-O
Sicilian, dragon, classical, Zollner gambit
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Be2 Nc6 8. O-O O-O 9. f4 Qb6 10. e5
Sicilian, dragon, classical, Richter variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Be2 Nc6 8. O-O O-O 9. Qd2
******B74: Sicilian, dragon, classical, 9.Nb3
Sicilian, dragon, classical, 9.Nb3
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Be2 Nc6 8. O-O O-O 9. Nb3
Sicilian, dragon, classical, Stockholm attack
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Be2 Nc6 8. O-O O-O 9. Nb3 Be6 10. f4 Na5 11. f5 Bc4 12. Nxa5 Bxe2 13. Qxe2 Qxa5 14. g4
Sicilian, dragon, classical, Spielmann variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Be2 Nc6 8. O-O O-O 9. Nb3 Be6 10. f4 Na5 11. f5 Bc4 12. Bd3
Sicilian, dragon, classical, Bernard defence
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Be2 Nc6 8. O-O O-O 9. Nb3 Be6 10. f4 Na5 11. f5 Bc4 12. Bd3 Bxd3 13. cxd3 d5 
Sicilian, dragon, classical, Reti-Tartakower variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Be2 Nc6 8. O-O O-O 9. Nb3 Be6 10. f4 Qc8 
Sicilian, dragon, classical, Alekhine variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Be2 Nc6 8. O-O O-O 9. Nb3 a5 
******B75: Sicilian, dragon, Yugoslav attack
Sicilian, dragon, Yugoslav attack
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. f3
******B76: Sicilian, dragon, Yugoslav attack, 7...O-O
Sicilian, dragon, Yugoslav attack, 7...O-O
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. f3 O-O 
Sicilian, dragon, Yugoslav attack, Rauser variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. f3 O-O 8. Qd2 Nc6 9. O-O-O
******B77: Sicilian, dragon, Yugoslav attack, 9.Bc4
Sicilian, dragon, Yugoslav attack, 9.Bc4
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. f3 O-O 8. Qd2 Nc6 9. Bc4
Sicilian, dragon, Yugoslav attack, Byrne variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. f3 O-O 8. Qd2 Nc6 9. Bc4 a5 
Sicilian, dragon, Yugoslav attack, 9...Bd7
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. f3 O-O 8. Qd2 Nc6 9. Bc4 Bd7 
******B78: Sicilian, dragon, Yugoslav attack, 10.O-O-O
Sicilian, dragon, Yugoslav attack, 10.O-O-O
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. f3 O-O 8. Qd2 Nc6 9. Bc4 Bd7 10. O-O-O
******B79: Sicilian, dragon, Yugoslav attack, 12.h4
Sicilian, dragon, Yugoslav attack, 12.h4
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. f3 O-O 8. Qd2 Nc6 9. Bc4 Bd7 10. O-O-O Qa5 11. Bb3 Rfc8 12. h4
******B80: Sicilian, Scheveningen variation
Sicilian, Scheveningen variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 
Sicilian, Scheveningen, English variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Be3 a6 7. Qd2
Sicilian, Scheveningen, Vitolins variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Bb5+
Sicilian, Scheveningen, fianchetto variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. g3
******B81: Sicilian, Scheveningen, Keres attack
Sicilian, Scheveningen, Keres attack
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. g4
******B82: Sicilian, Scheveningen, 6.f4
Sicilian, Scheveningen, 6.f4
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. f4
Sicilian, Scheveningen, Tal variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. f4 Nc6 7. Be3 Be7 8. Qf3
******B83: Sicilian, Scheveningen, 6.Be2
Sicilian, Scheveningen, 6.Be2
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Be2
Sicilian, modern Scheveningen
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Be2 Nc6 
Sicilian, modern Scheveningen, main line
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Be2 Nc6 7. O-O Be7 8. Be3 O-O 9. f4
Sicilian, modern Scheveningen, main line with Nb3
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Be2 Nc6 7. O-O Be7 8. Be3 O-O 9. f4 Bd7 10. Nb3
******B84: Sicilian, Scheveningen (Paulsen), classical variation
Sicilian, Scheveningen (Paulsen), classical variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Be2 a6 
Sicilian, Scheveningen, classical, Nd7 system
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Be2 a6 7. O-O Nbd7 
Sicilian, Scheveningen (Paulsen), classical variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Be2 a6 7. O-O Qc7 
******B85: Sicilian, Scheveningen, classical variation with ...Qc7 and ...Nc6
Sicilian, Scheveningen, classical variation with ...Qc7 and ...Nc6
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Be2 a6 7. O-O Qc7 8. f4 Nc6 
Sicilian, Scheveningen, classical, Maroczy system
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Be2 a6 7. O-O Qc7 8. f4 Nc6 9. Kh1 Be7 10. a4
Sicilian, Scheveningen, classical
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Be2 a6 7. O-O Qc7 8. f4 Nc6 9. Be3
Sicilian, Scheveningen, classical main line
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Be2 a6 7. O-O Qc7 8. f4 Nc6 9. Be3 Be7 10. Qe1 O-O 
******B86: Sicilian, Sozin attack
Sicilian, Sozin attack
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Bc4
******B87: Sicilian, Sozin with ...a6 and ...b5
Sicilian, Sozin with ...a6 and ...b5
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Bc4 a6 7. Bb3 b5 
******B88: Sicilian, Sozin, Leonhardt variation
Sicilian, Sozin, Leonhardt variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Bc4 Nc6 
Sicilian, Sozin, Fischer variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Bc4 Nc6 7. Bb3 Be7 8. Be3 O-O 9. f4
******B89: Sicilian, Sozin, 7.Be3
Sicilian, Sozin, 7.Be3
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Bc4 Nc6 7. Be3
Sicilian, Velimirovic attack
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 e6 6. Bc4 Nc6 7. Be3 Be7 8. Qe2
******B90: Sicilian, Najdorf
Sicilian, Najdorf
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 
Sicilian, Najdorf, Adams attack
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. h3
Sicilian, Najdorf, Lipnitzky attack
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bc4
Sicilian, Najdorf, Byrne (English) attack
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Be3
******B91: Sicilian, Najdorf, Zagreb (fianchetto) variation
Sicilian, Najdorf, Zagreb (fianchetto) variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. g3
******B92: Sicilian, Najdorf, Opovcensky variation
Sicilian, Najdorf, Opovcensky variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Be2
******B93: Sicilian, Najdorf, 6.f4
Sicilian, Najdorf, 6.f4
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. f4
******B94: Sicilian, Najdorf, 6.Bg5
Sicilian, Najdorf, 6.Bg5
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bg5
Sicilian, Najdorf, Ivkov variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bg5 Nbd7 7. Bc4 Qa5 8. Qd2 e6 9. O-O-O b5 10. Bb3 Bb7 11. Rhe1 Nc5 12. e5
******B95: Sicilian, Najdorf, 6...e6
Sicilian, Najdorf, 6...e6
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bg5 e6 
******B96: Sicilian, Najdorf, 7.f4
Sicilian, Najdorf, 7.f4
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bg5 e6 7. f4
Sicilian, Najdorf, Polugayevsky variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bg5 e6 7. f4 b5 
Sicilian, Najdorf, Polugayevsky, Simagin variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bg5 e6 7. f4 b5 8. e5 dxe5 9. fxe5 Qc7 10. Qe2
******B97: Sicilian, Najdorf, 7...Qb6
Sicilian, Najdorf, 7...Qb6
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bg5 e6 7. f4 Qb6 
Sicilian, Najdorf, Poisoned pawn variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bg5 e6 7. f4 Qb6 8. Qd2 Qxb2 9. Rb1 Qa3 
******B98: Sicilian, Najdorf, 7...Be7
Sicilian, Najdorf, 7...Be7
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bg5 e6 7. f4 Be7 
Sicilian, Najdorf, Browne variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bg5 e6 7. f4 Be7 8. Qf3 h6 9. Bh4 Qc7 
Sicilian, Najdorf, Goteborg (Argentine) variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bg5 e6 7. f4 Be7 8. Qf3 h6 9. Bh4 g5 
Sicilian, Najdorf variation
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bg5 e6 7. f4 Be7 8. Qf3 Qc7 
******B99: Sicilian, Najdorf, 7...Be7 main line
Sicilian, Najdorf, 7...Be7 main line
1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bg5 e6 7. f4 Be7 8. Qf3 Qc7 9. O-O-O Nbd7 
******C00: French defence
French defence
1. e4 e6 
French defence, Steiner variation
1. e4 e6 2. c4
French, Reti (Spielmann) variation
1. e4 e6 2. b3
French, Steinitz attack
1. e4 e6 2. e5
French, Labourdonnais variation
1. e4 e6 2. f4
French defence
1. e4 e6 2. Nf3
French, Wing gambit
1. e4 e6 2. Nf3 d5 3. e5 c5 4. b4
French defence
1. e4 e6 2. Nc3
French, Pelikan variation
1. e4 e6 2. Nc3 d5 3. f4
French, Two knights variation
1. e4 e6 2. Nc3 d5 3. Nf3
French, Chigorin variation
1. e4 e6 2. Qe2
French, King's Indian attack
1. e4 e6 2. d3
French, Reversed Philidor formation
1. e4 e6 2. d3 d5 3. Nd2 Nf6 4. Ngf3 Nc6 5. Be2
French defence
1. e4 e6 2. d4
Lengfellner system
1. e4 e6 2. d4 d6 
St. George defence
1. e4 e6 2. d4 a6 
French defence
1. e4 e6 2. d4 d5 
French, Schlechter variation
1. e4 e6 2. d4 d5 3. Bd3
French, Alapin variation
1. e4 e6 2. d4 d5 3. Be3
******C01: French, exchange variation
French, exchange variation
1. e4 e6 2. d4 d5 3. exd5
French, exchange, Svenonius variation
1. e4 e6 2. d4 d5 3. exd5 exd5 4. Nc3 Nf6 5. Bg5
French, exchange, Bogolyubov variation
1. e4 e6 2. d4 d5 3. exd5 exd5 4. Nc3 Nf6 5. Bg5 Nc6 
******C02: French, advance variation
French, advance variation
1. e4 e6 2. d4 d5 3. e5
French, advance, Steinitz variation
1. e4 e6 2. d4 d5 3. e5 c5 4. dxc5
French, advance, Nimzovich variation
1. e4 e6 2. d4 d5 3. e5 c5 4. Qg4
French, advance, Nimzovich system
1. e4 e6 2. d4 d5 3. e5 c5 4. Nf3
French, advance variation
1. e4 e6 2. d4 d5 3. e5 c5 4. c3
French, advance, Wade variation
1. e4 e6 2. d4 d5 3. e5 c5 4. c3 Qb6 5. Nf3 Bd7 
French, advance variation
1. e4 e6 2. d4 d5 3. e5 c5 4. c3 Nc6 
French, advance, Paulsen attack
1. e4 e6 2. d4 d5 3. e5 c5 4. c3 Nc6 5. Nf3
French, advance, Milner-Barry gambit
1. e4 e6 2. d4 d5 3. e5 c5 4. c3 Nc6 5. Nf3 Qb6 6. Bd3
French, advance, Euwe variation
1. e4 e6 2. d4 d5 3. e5 c5 4. c3 Nc6 5. Nf3 Bd7 
******C03: French, Tarrasch
French, Tarrasch
1. e4 e6 2. d4 d5 3. Nd2
French, Tarrasch, Haberditz variation
1. e4 e6 2. d4 d5 3. Nd2 f5 
French, Tarrasch, Guimard variation
1. e4 e6 2. d4 d5 3. Nd2 Nc6 
******C04: French, Tarrasch, Guimard main line
French, Tarrasch, Guimard main line
1. e4 e6 2. d4 d5 3. Nd2 Nc6 4. Ngf3 Nf6 
******C05: French, Tarrasch, closed variation
French, Tarrasch, closed variation
1. e4 e6 2. d4 d5 3. Nd2 Nf6 
French, Tarrasch, Botvinnik variation
1. e4 e6 2. d4 d5 3. Nd2 Nf6 4. e5 Nfd7 5. Bd3 c5 6. c3 b6 
French, Tarrasch, closed variation
1. e4 e6 2. d4 d5 3. Nd2 Nf6 4. e5 Nfd7 5. Bd3 c5 6. c3 Nc6 
******C06: French, Tarrasch, closed variation, main line
French, Tarrasch, closed variation, main line
1. e4 e6 2. d4 d5 3. Nd2 Nf6 4. e5 Nfd7 5. Bd3 c5 6. c3 Nc6 7. Ne2 cxd4 8. cxd4
French, Tarrasch, Leningrad variation
1. e4 e6 2. d4 d5 3. Nd2 Nf6 4. e5 Nfd7 5. Bd3 c5 6. c3 Nc6 7. Ne2 cxd4 8. cxd4 Nb6 
******C07: French, Tarrasch, open variation
French, Tarrasch, open variation
1. e4 e6 2. d4 d5 3. Nd2 c5 
French, Tarrasch, Eliskases variation
1. e4 e6 2. d4 d5 3. Nd2 c5 4. exd5 Qxd5 5. Ngf3 cxd4 6. Bc4 Qd8 
******C08: French, Tarrasch, open, 4.ed ed
French, Tarrasch, open, 4.ed ed
1. e4 e6 2. d4 d5 3. Nd2 c5 4. exd5 exd5 
******C09: French, Tarrasch, open variation, main line
French, Tarrasch, open variation, main line
1. e4 e6 2. d4 d5 3. Nd2 c5 4. exd5 exd5 5. Ngf3 Nc6 
******C10: French, Paulsen variation
French, Paulsen variation
1. e4 e6 2. d4 d5 3. Nc3
French, Marshall variation
1. e4 e6 2. d4 d5 3. Nc3 c5 
French, Rubinstein variation
1. e4 e6 2. d4 d5 3. Nc3 dxe4 
French, Fort Knox variation
1. e4 e6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Bd7 5. Nf3 Bc6 
French, Rubinstein variation
1. e4 e6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Nd7 
French, Rubinstein, Capablanca line
1. e4 e6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Nd7 5. Nf3 Ngf6 6. Nxf6+ Nxf6 7. Ne5
French, Frere (Becker) variation
1. e4 e6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Qd5 
******C11: French defence
French defence
1. e4 e6 2. d4 d5 3. Nc3 Nf6 
French, Swiss variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bd3
French, Henneberger variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Be3
French, Steinitz variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. e5
French, Steinitz, Bradford attack
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. e5 Nfd7 5. f4 c5 6. dxc5 Bxc5 7. Qg4
French, Steinitz variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. e5 Nfd7 5. f4 c5 6. dxc5 Nc6 
French, Steinitz, Brodsky-Jones variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. e5 Nfd7 5. f4 c5 6. dxc5 Nc6 7. a3 Bxc5 8. Qg4 O-O 9. Nf3 f6 
French, Steinitz variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. e5 Nfd7 5. f4 c5 6. Nf3
French, Steinitz, Boleslavsky variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. e5 Nfd7 5. f4 c5 6. Nf3 Nc6 7. Be3
French, Steinitz, Gledhill attack
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. e5 Nfd7 5. Qg4
French, Burn variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 dxe4 
******C12: French, MacCutcheon variation
French, MacCutcheon variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Bb4 
French, MacCutcheon, Bogolyubov variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Bb4 5. exd5 Qxd5 6. Bxf6 gxf6 7. Qd2 Qa5 
French, MacCutcheon, advance variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Bb4 5. e5
French, MacCutcheon, Chigorin variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Bb4 5. e5 h6 6. exf6
French, MacCutcheon, Grigoriev variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Bb4 5. e5 h6 6. exf6 hxg5 7. fxg7 Rg8 8. h4 gxh4 9. Qg4
French, MacCutcheon, Bernstein variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Bb4 5. e5 h6 6. Bh4
French, MacCutcheon, Janowski variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Bb4 5. e5 h6 6. Be3
French, MacCutcheon, Dr. Olland (Dutch) variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Bb4 5. e5 h6 6. Bc1
French, MacCutcheon, Tartakower variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Bb4 5. e5 h6 6. Bd2 Nfd7 
French, MacCutcheon, Lasker variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Bb4 5. e5 h6 6. Bd2 Bxc3 
French, MacCutcheon, Duras variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Bb4 5. e5 h6 6. Bd2 Bxc3 7. bxc3 Ne4 8. Qg4 Kf8 9. Bc1
French, MacCutcheon, Lasker variation, 8...g6
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Bb4 5. e5 h6 6. Bd2 Bxc3 7. bxc3 Ne4 8. Qg4 g6 
******C13: French, classical
French, classical
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 
French, classical, Anderssen variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. Bxf6
French, classical, Anderssen-Richter variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. Bxf6 Bxf6 6. e5 Be7 7. Qg4
French, classical, Vistaneckis (Nimzovich) variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Ng8 
French, classical, Frankfurt variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Ng8 6. Be3 b6 
French, classical, Tartakower variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Ne4 
French, Albin-Alekhine-Chatard attack
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 6. h4
French, Albin-Alekhine-Chatard attack, Maroczy variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 6. h4 a6 
French, Albin-Alekhine-Chatard attack, Breyer variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 6. h4 c5 
French, Albin-Alekhine-Chatard attack, Teichmann variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 6. h4 f6 
French, Albin-Alekhine-Chatard attack, Spielmann variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 6. h4 O-O 
******C14: French, classical variation
French, classical variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 6. Bxe7 Qxe7 
French, classical, Tarrasch variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 6. Bxe7 Qxe7 7. Bd3
French, classical, Rubinstein variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 6. Bxe7 Qxe7 7. Qd2
French, classical, Alapin variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 6. Bxe7 Qxe7 7. Nb5
French, classical, Pollock variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 6. Bxe7 Qxe7 7. Qg4
French, classical, Steinitz variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 6. Bxe7 Qxe7 7. f4
French, classical, Stahlberg variation
1. e4 e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 6. Bxe7 Qxe7 7. f4 O-O 8. Nf3 c5 9. Qd2 Nc6 10. O-O-O c4 
******C15: French, Winawer (Nimzovich) variation
French, Winawer (Nimzovich) variation
1. e4 e6 2. d4 d5 3. Nc3 Bb4 
French, Winawer, Kondratiyev variation
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. Bd3 c5 5. exd5 Qxd5 6. Bd2
French, Winawer, fingerslip variation
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. Bd2
French, Winawer, Alekhine (Maroczy) gambit
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. Nge2
French, Winawer, Alekhine gambit, Alatortsev variation
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. Nge2 dxe4 5. a3 Be7 6. Nxe4 Nf6 7. Ne2-g3 O-O 8. Be2 Nc6 
French, Winawer, Alekhine gambit
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. Nge2 dxe4 5. a3 Bxc3+ 
French, Winawer, Alekhine gambit, Kan variation
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. Nge2 dxe4 5. a3 Bxc3+ 6. Nxc3 Nc6 
******C16: French, Winawer, advance variation
French, Winawer, advance variation
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5
French, Winawer, Petrosian variation
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 Qd7 
******C17: French, Winawer, advance variation
French, Winawer, advance variation
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 c5 
French, Winawer, advance, Bogolyubov variation
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 c5 5. Bd2
French, Winawer, advance, Russian variation
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 c5 5. Qg4
French, Winawer, advance, 5.a3
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 c5 5. a3
French, Winawer, advance, Rauzer variation
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 c5 5. a3 cxd4 6. axb4 dxc3 7. Nf3
******C18: French, Winawer, advance variation
French, Winawer, advance variation
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 c5 5. a3 Bxc3+ 6. bxc3
French, Winawer, classical variation
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 c5 5. a3 Bxc3+ 6. bxc3 Qc7 
******C19: French, Winawer, advance, 6...Ne7
French, Winawer, advance, 6...Ne7
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 c5 5. a3 Bxc3+ 6. bxc3 Ne7 
French, Winawer, advance, Smyslov variation
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 c5 5. a3 Bxc3+ 6. bxc3 Ne7 7. a4
French, Winawer, advance, positional main line
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 c5 5. a3 Bxc3+ 6. bxc3 Ne7 7. Nf3
French, Winawer, advance, poisoned pawn variation
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 c5 5. a3 Bxc3+ 6. bxc3 Ne7 7. Qg4
French, Winawer, advance, poisoned pawn, Euwe-Gligoric variation
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 c5 5. a3 Bxc3+ 6. bxc3 Ne7 7. Qg4 Qc7 8. Qxg7 Rg8 9. Qxh7 cxd4 10. Kd1
French, Winawer, advance, poisoned pawn, Konstantinopolsky variation
1. e4 e6 2. d4 d5 3. Nc3 Bb4 4. e5 c5 5. a3 Bxc3+ 6. bxc3 Ne7 7. Qg4 Qc7 8. Qxg7 Rg8 9. Qxh7 cxd4 10. Ne2
******C20: King's pawn game
King's pawn game
1. e4 e5 
KP, Indian opening
1. e4 e5 2. d3
KP, Mengarini's opening
1. e4 e5 2. a3
KP, King's head opening
1. e4 e5 2. f3
KP, Patzer opening
1. e4 e5 2. Qh5
KP, Napoleon's opening
1. e4 e5 2. Qf3
KP, Lopez opening
1. e4 e5 2. c3
Alapin's opening
1. e4 e5 2. Ne2
******C21: Centre game
Centre game
1. e4 e5 2. d4 exd4 
Centre game, Kieseritsky variation
1. e4 e5 2. d4 exd4 3. Nf3 c5 4. Bc4 b5 
Halasz gambit
1. e4 e5 2. d4 exd4 3. f4
Danish gambit
1. e4 e5 2. d4 exd4 3. c3
Danish gambit, Collijn defence
1. e4 e5 2. d4 exd4 3. c3 dxc3 4. Bc4 cxb2 5. Bxb2 Qe7 
Danish gambit, Schlechter defence
1. e4 e5 2. d4 exd4 3. c3 dxc3 4. Bc4 cxb2 5. Bxb2 d5 
Danish gambit, Soerensen defence
1. e4 e5 2. d4 exd4 3. c3 d5 
Centre game
1. e4 e5 2. d4 exd4 3. Qxd4
******C22: Centre game
Centre game
1. e4 e5 2. d4 exd4 3. Qxd4 Nc6 
Centre game, Paulsen attack
1. e4 e5 2. d4 exd4 3. Qxd4 Nc6 4. Qe3
Centre game, Charousek variation
1. e4 e5 2. d4 exd4 3. Qxd4 Nc6 4. Qe3 Bb4+ 5. c3 Be7 
Centre game, l'Hermet variation
1. e4 e5 2. d4 exd4 3. Qxd4 Nc6 4. Qe3 f5 
Centre game, Berger variation
1. e4 e5 2. d4 exd4 3. Qxd4 Nc6 4. Qe3 Nf6 
Centre game, Kupreichik variation
1. e4 e5 2. d4 exd4 3. Qxd4 Nc6 4. Qe3 Nf6 5. Nc3 Bb4 6. Bd2 O-O 7. O-O-O Re8 8. Bc4 d6 9. Nh3
Centre game, Hall variation
1. e4 e5 2. d4 exd4 3. Qxd4 Nc6 4. Qc4
******C23: Bishop's opening
Bishop's opening
1. e4 e5 2. Bc4
Bishop's opening, Philidor counter-attack
1. e4 e5 2. Bc4 c6 
Bishop's opening, Lisitsyn variation
1. e4 e5 2. Bc4 c6 3. d4 d5 4. exd5 cxd5 5. Bb5+ Bd7 6. Bxd7+ Nxd7 7. dxe5 Nxe5 8. Ne2
Bishop's opening, Calabrese counter-gambit
1. e4 e5 2. Bc4 f5 
Bishop's opening, Calabrese counter-gambit, Jaenisch variation
1. e4 e5 2. Bc4 f5 3. d3
Bishop's opening, Classical variation
1. e4 e5 2. Bc4 Bc5 
Bishop's opening, Lopez gambit
1. e4 e5 2. Bc4 Bc5 3. Qe2 Nc6 4. c3 Nf6 5. f4
Bishop's opening, Philidor variation
1. e4 e5 2. Bc4 Bc5 3. c3
Bishop's opening, Pratt variation
1. e4 e5 2. Bc4 Bc5 3. c3 Nf6 4. d4 exd4 5. e5 d5 6. exf6 dxc4 7. Qh5 O-O 
Bishop's opening, Lewis counter-gambit
1. e4 e5 2. Bc4 Bc5 3. c3 d5 
Bishop's opening, del Rio variation
1. e4 e5 2. Bc4 Bc5 3. c3 Qg5 
Bishop's opening, Lewis gambit
1. e4 e5 2. Bc4 Bc5 3. d4
Bishop's opening, Wing gambit
1. e4 e5 2. Bc4 Bc5 3. b4
Bishop's opening, MacDonnell double gambit
1. e4 e5 2. Bc4 Bc5 3. b4 Bxb4 4. f4
Bishop's opening, Four pawns' gambit
1. e4 e5 2. Bc4 Bc5 3. b4 Bxb4 4. f4 exf4 5. Nf3 Be7 6. d4 Bh4+ 7. g3 fxg3 8. O-O gxh2+ 9. Kh1
******C24: Bishop's opening, Berlin defence
Bishop's opening, Berlin defence
1. e4 e5 2. Bc4 Nf6 
Bishop's opening, Greco gambit
1. e4 e5 2. Bc4 Nf6 3. f4
Bishop's opening, Ponziani gambit
1. e4 e5 2. Bc4 Nf6 3. d4
Bishop's opening, Urusov gambit
1. e4 e5 2. Bc4 Nf6 3. d4 exd4 4. Nf3
Bishop's opening, Urusov gambit, Panov variation
1. e4 e5 2. Bc4 Nf6 3. d4 exd4 4. Nf3 d5 5. exd5 Bb4+ 6. c3 Qe7+ 
******C25: Vienna game
Vienna game
1. e4 e5 2. Nc3
Vienna, Zhuravlev countergambit
1. e4 e5 2. Nc3 Bb4 3. Qg4 Nf6 
Vienna game, Max Lange defence
1. e4 e5 2. Nc3 Nc6 
Vienna, Paulsen variation
1. e4 e5 2. Nc3 Nc6 3. g3
Vienna, Fyfe gambit
1. e4 e5 2. Nc3 Nc6 3. d4
Vienna gambit
1. e4 e5 2. Nc3 Nc6 3. f4
Vienna, Steinitz gambit
1. e4 e5 2. Nc3 Nc6 3. f4 exf4 4. d4
Vienna, Steinitz gambit, Zukertort defence
1. e4 e5 2. Nc3 Nc6 3. f4 exf4 4. d4 Qh4+ 5. Ke2 d5 
Vienna, Steinitz gambit, Fraser-Minckwitz variation
1. e4 e5 2. Nc3 Nc6 3. f4 exf4 4. d4 Qh4+ 5. Ke2 b6 
Vienna gambit
1. e4 e5 2. Nc3 Nc6 3. f4 exf4 4. Nf3
Vienna, Hamppe-Allgaier gambit
1. e4 e5 2. Nc3 Nc6 3. f4 exf4 4. Nf3 g5 5. h4 g4 6. Ng5
Vienna, Hamppe-Allgaier gambit, Alapin variation
1. e4 e5 2. Nc3 Nc6 3. f4 exf4 4. Nf3 g5 5. h4 g4 6. Ng5 d6 
Vienna, Hamppe-Muzio gambit
1. e4 e5 2. Nc3 Nc6 3. f4 exf4 4. Nf3 g5 5. Bc4 g4 6. O-O
Vienna, Hamppe-Muzio, Dubois variation
1. e4 e5 2. Nc3 Nc6 3. f4 exf4 4. Nf3 g5 5. Bc4 g4 6. O-O gxf3 7. Qxf3 Ne5 8. Qxf4 Qf6 
Vienna, Pierce gambit
1. e4 e5 2. Nc3 Nc6 3. f4 exf4 4. Nf3 g5 5. d4
Vienna, Pierce gambit, Rushmere attack
1. e4 e5 2. Nc3 Nc6 3. f4 exf4 4. Nf3 g5 5. d4 g4 6. Bc4 gxf3 7. O-O d5 8. exd5 Bg4 9. dxc6
******C26: Vienna, Falkbeer variation
Vienna, Falkbeer variation
1. e4 e5 2. Nc3 Nf6 
Vienna, Mengarini variation
1. e4 e5 2. Nc3 Nf6 3. a3
Vienna, Paulsen-Mieses variation
1. e4 e5 2. Nc3 Nf6 3. g3
Vienna game
1. e4 e5 2. Nc3 Nf6 3. Bc4
******C27: Vienna game
Vienna game
1. e4 e5 2. Nc3 Nf6 3. Bc4 Nxe4 
Vienna, `Frankenstein-Dracula' variation
1. e4 e5 2. Nc3 Nf6 3. Bc4 Nxe4 4. Qh5 Nd6 5. Bb3 Nc6 6. Nb5 g6 7. Qf3 f5 8. Qd5 Qe7 9. Nxc7+ Kd8 10. Nxa8 b6 
Vienna, Adams' gambit
1. e4 e5 2. Nc3 Nf6 3. Bc4 Nxe4 4. Qh5 Nd6 5. Bb3 Nc6 6. d4
Vienna game
1. e4 e5 2. Nc3 Nf6 3. Bc4 Nxe4 4. Qh5 Nd6 5. Bb3 Be7 
Vienna, Alekhine variation
1. e4 e5 2. Nc3 Nf6 3. Bc4 Nxe4 4. Qh5 Nd6 5. Bb3 Be7 6. Nf3 Nc6 7. Nxe5
Boden-Kieseritsky gambit
1. e4 e5 2. Nc3 Nf6 3. Bc4 Nxe4 4. Nf3
Boden-Kieseritsky gambit, Lichtenhein defence
1. e4 e5 2. Nc3 Nf6 3. Bc4 Nxe4 4. Nf3 d5 
******C28: Vienna game
Vienna game
1. e4 e5 2. Nc3 Nf6 3. Bc4 Nc6 
******C29: Vienna gambit
Vienna gambit
1. e4 e5 2. Nc3 Nf6 3. f4 d5 
Vienna gambit, Kaufmann variation
1. e4 e5 2. Nc3 Nf6 3. f4 d5 4. fxe5 Nxe4 5. Nf3 Bg4 6. Qe2
Vienna gambit, Breyer variation
1. e4 e5 2. Nc3 Nf6 3. f4 d5 4. fxe5 Nxe4 5. Nf3 Be7 
Vienna gambit, Paulsen attack
1. e4 e5 2. Nc3 Nf6 3. f4 d5 4. fxe5 Nxe4 5. Qf3
Vienna gambit, Bardeleben variation
1. e4 e5 2. Nc3 Nf6 3. f4 d5 4. fxe5 Nxe4 5. Qf3 f5 
Vienna gambit, Heyde variation
1. e4 e5 2. Nc3 Nf6 3. f4 d5 4. fxe5 Nxe4 5. Qf3 f5 6. d4
Vienna gambit
1. e4 e5 2. Nc3 Nf6 3. f4 d5 4. fxe5 Nxe4 5. d3
Vienna gambit, Wurzburger trap
1. e4 e5 2. Nc3 Nf6 3. f4 d5 4. fxe5 Nxe4 5. d3 Qh4+ 6. g3 Nxg3 7. Nf3 Qh5 8. Nxd5
Vienna gambit, Steinitz variation
1. e4 e5 2. Nc3 Nf6 3. f4 d5 4. d3
******C30: King's gambit
King's gambit
1. e4 e5 2. f4
King's Gambit Declined, Keene's defence
1. e4 e5 2. f4 Qh4+ 3. g3 Qe7 
King's Gambit Declined, Mafia defence
1. e4 e5 2. f4 c5 
King's Gambit Declined, Norwalde variation
1. e4 e5 2. f4 Qf6 
King's Gambit Declined, Norwalde variation, Buecker gambit
1. e4 e5 2. f4 Qf6 3. Nf3 Qxf4 4. Nc3 Bb4 5. Bc4
King's Gambit Declined, classical variation
1. e4 e5 2. f4 Bc5 
King's Gambit Declined, classical, Svenonius variation
1. e4 e5 2. f4 Bc5 3. Nf3 d6 4. Nc3 Nf6 5. Bc4 Nc6 6. d3 Bg4 7. h3 Bxf3 8. Qxf3 exf4 
King's Gambit Declined, classical, Hanham variation
1. e4 e5 2. f4 Bc5 3. Nf3 d6 4. Nc3 Nd7 
King's Gambit Declined, classical, 4.c3
1. e4 e5 2. f4 Bc5 3. Nf3 d6 4. c3
King's Gambit Declined, classical, Marshall attack
1. e4 e5 2. f4 Bc5 3. Nf3 d6 4. c3 Bg4 5. fxe5 dxe5 6. Qa4+
King's Gambit Declined, classical counter-gambit
1. e4 e5 2. f4 Bc5 3. Nf3 d6 4. c3 f5 
King's Gambit Declined, classical, Reti variation
1. e4 e5 2. f4 Bc5 3. Nf3 d6 4. c3 f5 5. fxe5 dxe5 6. d4 exd4 7. Bc4
King's Gambit Declined, classical, Soldatenkov variation
1. e4 e5 2. f4 Bc5 3. Nf3 d6 4. fxe5
King's Gambit Declined, classical, Heath variation
1. e4 e5 2. f4 Bc5 3. Nf3 d6 4. b4
King's Gambit Declined, 2...Nf6
1. e4 e5 2. f4 Nf6 
******C31: King's Gambit Declined, Falkbeer counter-gambit
King's Gambit Declined, Falkbeer counter-gambit
1. e4 e5 2. f4 d5 
King's Gambit Declined, Falkbeer, Tartakower variation
1. e4 e5 2. f4 d5 3. Nf3
King's Gambit Declined, Falkbeer, Milner-Barry variation
1. e4 e5 2. f4 d5 3. Nc3
King's Gambit Declined, Falkbeer counter-gambit
1. e4 e5 2. f4 d5 3. exd5
King's Gambit Declined, Nimzovich counter-gambit
1. e4 e5 2. f4 d5 3. exd5 c6 
King's Gambit Declined, Falkbeer, 3...e4
1. e4 e5 2. f4 d5 3. exd5 e4 
King's Gambit Declined, Falkbeer, Rubinstein variation
1. e4 e5 2. f4 d5 3. exd5 e4 4. Nc3 Nf6 5. Qe2
King's Gambit Declined, Falkbeer, Nimzovich variation
1. e4 e5 2. f4 d5 3. exd5 e4 4. Bb5+
King's Gambit Declined, Falkbeer, 4.d3
1. e4 e5 2. f4 d5 3. exd5 e4 4. d3
King's Gambit Declined, Falkbeer, Morphy gambit
1. e4 e5 2. f4 d5 3. exd5 e4 4. d3 Nf6 5. Nc3 Bb4 6. Bd2 e3 
******C32: King's Gambit Declined, Falkbeer, 5.de
King's Gambit Declined, Falkbeer, 5.de
1. e4 e5 2. f4 d5 3. exd5 e4 4. d3 Nf6 5. dxe4
King's Gambit Declined, Falkbeer, Alapin variation
1. e4 e5 2. f4 d5 3. exd5 e4 4. d3 Nf6 5. dxe4 Nxe4 6. Nf3 Bc5 7. Qe2 Bf2+ 8. Kd1 Qxd5+ 9. Nfd2
King's Gambit Declined, Falkbeer, main line, 7...Bf5
1. e4 e5 2. f4 d5 3. exd5 e4 4. d3 Nf6 5. dxe4 Nxe4 6. Nf3 Bc5 7. Qe2 Bf5 
King's Gambit Declined, Falkbeer, Tarrasch variation
1. e4 e5 2. f4 d5 3. exd5 e4 4. d3 Nf6 5. dxe4 Nxe4 6. Nf3 Bc5 7. Qe2 Bf5 8. g4 O-O 
King's Gambit Declined, Falkbeer, Charousek gambit
1. e4 e5 2. f4 d5 3. exd5 e4 4. d3 Nf6 5. dxe4 Nxe4 6. Qe2
King's Gambit Declined, Falkbeer, Charousek variation
1. e4 e5 2. f4 d5 3. exd5 e4 4. d3 Nf6 5. dxe4 Nxe4 6. Qe2 Qxd5 7. Nd2 f5 8. g4
King's Gambit Declined, Falkbeer, Keres variation
1. e4 e5 2. f4 d5 3. exd5 e4 4. d3 Nf6 5. Nd2
King's Gambit Declined, Falkbeer, Reti variation
1. e4 e5 2. f4 d5 3. exd5 e4 4. d3 Nf6 5. Qe2
******C33: King's gambit accepted
King's gambit accepted
1. e4 e5 2. f4 exf4 
King's Gambit Accepted, Tumbleweed gambit
1. e4 e5 2. f4 exf4 3. Kf2
King's Gambit Accepted, Orsini gambit
1. e4 e5 2. f4 exf4 3. b3
King's Gambit Accepted, Pawn's gambit (Stamma gambit)
1. e4 e5 2. f4 exf4 3. h4
King's Gambit Accepted, Schurig gambit
1. e4 e5 2. f4 exf4 3. Bd3
King's Gambit Accepted, Carrera (Basman) gambit
1. e4 e5 2. f4 exf4 3. Qe2
King's Gambit Accepted, Villemson (Steinitz) gambit
1. e4 e5 2. f4 exf4 3. d4
King's Gambit Accepted, Keres (Mason-Steinitz) gambit
1. e4 e5 2. f4 exf4 3. Nc3
King's Gambit Accepted, Breyer gambit
1. e4 e5 2. f4 exf4 3. Qf3
King's Gambit Accepted, Lesser bishop's (Petroff-Jaenisch-Tartakower) gambit
1. e4 e5 2. f4 exf4 3. Be2
King's Gambit Accepted, bishop's gambit
1. e4 e5 2. f4 exf4 3. Bc4
King's Gambit Accepted, bishop's gambit, Chigorin's attack
1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 d5 5. Bxd5 g5 6. g3
King's Gambit Accepted, bishop's gambit, Greco variation
1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 Bc5 
King's Gambit Accepted, bishop's gambit, classical defence
1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 g5 
King's Gambit Accepted, bishop's gambit, Grimm attack
1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 g5 5. Nc3 Bg7 6. d4 d6 7. e5
King's Gambit Accepted, bishop's gambit, classical defence
1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 g5 5. Nc3 Bg7 6. d4 Ne7 
King's Gambit Accepted, bishop's gambit, McDonnell attack
1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 g5 5. Nc3 Bg7 6. d4 Ne7 7. g3
King's Gambit Accepted, bishop's gambit, McDonnell attack
1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 g5 5. Nc3 Bg7 6. g3
King's Gambit Accepted, bishop's gambit, Fraser variation
1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 g5 5. Nc3 Bg7 6. g3 fxg3 7. Qf3
King's Gambit Accepted, bishop's gambit, classical defence, Cozio attack
1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 g5 5. Qf3
King's Gambit Accepted, bishop's gambit, Boden defence
1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 Nc6 
King's Gambit Accepted, bishop's gambit, Bryan counter-gambit
1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 b5 
King's Gambit Accepted, bishop's gambit, Bryan counter-gambit
1. e4 e5 2. f4 exf4 3. Bc4 b5 
King's Gambit Accepted, bishop's gambit, Steinitz defence
1. e4 e5 2. f4 exf4 3. Bc4 Ne7 
King's Gambit Accepted, bishop's gambit, Maurian defence
1. e4 e5 2. f4 exf4 3. Bc4 Nc6 
King's Gambit Accepted, bishop's gambit, Ruy Lopez defence
1. e4 e5 2. f4 exf4 3. Bc4 c6 
King's Gambit Accepted, bishop's gambit, Lopez-Gianutio counter-gambit
1. e4 e5 2. f4 exf4 3. Bc4 f5 
King's Gambit Accepted, Lopez-Gianutio counter-gambit, Hein variation
1. e4 e5 2. f4 exf4 3. Bc4 f5 4. Qe2 Qh4+ 5. Kd1 fxe4 6. Nc3 Kd8 
King's Gambit Accepted, bishop's gambit, Bledow variation
1. e4 e5 2. f4 exf4 3. Bc4 d5 
King's Gambit Accepted, bishop's gambit, Gifford variation
1. e4 e5 2. f4 exf4 3. Bc4 d5 4. Bxd5 Qh4+ 5. Kf1 g5 6. g3
King's Gambit Accepted, bishop's gambit, Boren-Svenonius variation
1. e4 e5 2. f4 exf4 3. Bc4 d5 4. Bxd5 Qh4+ 5. Kf1 Bd6 
King's Gambit Accepted, bishop's gambit, Anderssen variation
1. e4 e5 2. f4 exf4 3. Bc4 d5 4. Bxd5 c6 
King's Gambit Accepted, bishop's gambit, Morphy variation
1. e4 e5 2. f4 exf4 3. Bc4 d5 4. Bxd5 Nf6 
King's Gambit Accepted, bishop's gambit, Cozio (Morphy) defence
1. e4 e5 2. f4 exf4 3. Bc4 Nf6 
King's Gambit Accepted, bishop's gambit, Bogolyubov variation
1. e4 e5 2. f4 exf4 3. Bc4 Nf6 4. Nc3
King's Gambit Accepted, bishop's gambit, Paulsen attack
1. e4 e5 2. f4 exf4 3. Bc4 Nf6 4. Nc3 Bb4 5. e5
King's Gambit Accepted, bishop's gambit, Jaenisch variation
1. e4 e5 2. f4 exf4 3. Bc4 Nf6 4. Nc3 c6 
******C34: King's Gambit Accepted
King's Gambit Accepted
1. e4 e5 2. f4 exf4 3. Nf3
King's Gambit Accepted, Bonsch-Osmolovsky variation
1. e4 e5 2. f4 exf4 3. Nf3 Ne7 
King's Gambit Accepted, Gianutio counter-gambit
1. e4 e5 2. f4 exf4 3. Nf3 f5 
King's Gambit Accepted, Fischer defence
1. e4 e5 2. f4 exf4 3. Nf3 d6 
King's Gambit Accepted, Becker defence
1. e4 e5 2. f4 exf4 3. Nf3 h6 
King's Gambit Accepted, Schallop defence
1. e4 e5 2. f4 exf4 3. Nf3 Nf6 
******C35: King's Gambit Accepted, Cunningham defence
King's Gambit Accepted, Cunningham defence
1. e4 e5 2. f4 exf4 3. Nf3 Be7 
King's Gambit Accepted, Cunningham, Bertin gambit
1. e4 e5 2. f4 exf4 3. Nf3 Be7 4. Bc4 Bh4+ 5. g3
King's Gambit Accepted, Cunningham, three pawns gambit
1. e4 e5 2. f4 exf4 3. Nf3 Be7 4. Bc4 Bh4+ 5. g3 fxg3 6. O-O gxh2+ 7. Kh1
King's Gambit Accepted, Cunningham, Euwe defence
1. e4 e5 2. f4 exf4 3. Nf3 Be7 4. Bc4 Nf6 
******C36: King's Gambit Accepted, Abbazia defence (classical defence, modern defence[!])
King's Gambit Accepted, Abbazia defence (classical defence, modern defence[!])
1. e4 e5 2. f4 exf4 3. Nf3 d5 
King's Gambit Accepted, Abbazia defence, modern variation
1. e4 e5 2. f4 exf4 3. Nf3 d5 4. exd5 Nf6 
King's Gambit Accepted, Abbazia defence, Botvinnik variation
1. e4 e5 2. f4 exf4 3. Nf3 d5 4. exd5 Nf6 5. Bb5+ c6 6. dxc6 bxc6 7. Bc4 Nd5 
******C37: King's Gambit Accepted, Quaade gambit
King's Gambit Accepted, Quaade gambit
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Nc3
King's Gambit Accepted, Rosentreter gambit
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. d4
King's Gambit Accepted, Soerensen gambit
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. d4 g4 5. Ne5
King's Gambit Accepted, King's knight's gambit
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4
King's Gambit Accepted, Blachly gambit
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 Nc6 
King's Gambit Accepted, Lolli gambit (wild Muzio gambit)
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. Bxf7+
King's Gambit Accepted, Lolli gambit, Young variation
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. Bxf7+ Kxf7 6. O-O gxf3 7. Qxf3 Qf6 8. d4 Qxd4+ 9. Be3 Qf6 10. Nc3
King's Gambit Accepted, Ghulam Kassim gambit
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. d4
King's Gambit Accepted, MacDonnell gambit
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. Nc3
King's Gambit Accepted, Salvio gambit
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. Ne5
King's Gambit Accepted, Silberschmidt gambit
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. Ne5 Qh4+ 6. Kf1 Nh6 7. d4 f3 
King's Gambit Accepted, Salvio gambit, Anderssen counter-attack
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. Ne5 Qh4+ 6. Kf1 Nh6 7. d4 d6 
King's Gambit Accepted, Cochrane gambit
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. Ne5 Qh4+ 6. Kf1 f3 
King's Gambit Accepted, Herzfeld gambit
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. Ne5 Qh4+ 6. Kf1 Nc6 
King's Gambit Accepted, Muzio gambit
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. O-O
King's Gambit Accepted, Muzio gambit, Paulsen variation
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. O-O gxf3 6. Qxf3 Qf6 7. e5 Qxe5 8. d3 Bh6 9. Nc3 Ne7 10. Bd2 Nbc6 11. Rae1
King's Gambit Accepted, double Muzio gambit
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. O-O gxf3 6. Qxf3 Qf6 7. e5 Qxe5 8. Bxf7+
King's Gambit Accepted, Muzio gambit, From defence
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. O-O gxf3 6. Qxf3 Qe7 
King's Gambit Accepted, Muzio gambit, Holloway defence
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. O-O gxf3 6. Qxf3 Nc6 
King's Gambit Accepted, Muzio gambit, Kling and Horwitz counter-attack
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. O-O Qe7 
King's Gambit Accepted, Muzio gambit, Brentano defence
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 g4 5. O-O d5 
******C38: King's Gambit Accepted
King's Gambit Accepted
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 Bg7 
King's Gambit Accepted, Hanstein gambit
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 Bg7 5. O-O
King's Gambit Accepted, Philidor gambit
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 Bg7 5. h4
King's Gambit Accepted, Greco gambit
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 Bg7 5. h4 h6 6. d4 d6 7. Nc3 c6 8. hxg5 hxg5 9. Rxh8 Bxh8 10. Ne5
King's Gambit Accepted, Philidor gambit, Schultz variation
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. Bc4 Bg7 5. h4 h6 6. d4 d6 7. Qd3
******C39: King's Gambit Accepted
King's Gambit Accepted
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4
King's Gambit Accepted, Allgaier gambit
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ng5
King's Gambit Accepted, Allgaier, Horny defence
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ng5 h6 6. Nxf7 Kxf7 7. Qxg4 Nf6 8. Qxf4 Bd6 
King's Gambit Accepted, Allgaier, Thorold variation
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ng5 h6 6. Nxf7 Kxf7 7. d4
King's Gambit Accepted, Allgaier, Cook variation
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ng5 h6 6. Nxf7 Kxf7 7. d4 d5 8. Bxf4 dxe4 9. Bc4+ Kg7 10. Be5+
King's Gambit Accepted, Allgaier, Blackburne gambit
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ng5 h6 6. Nxf7 Kxf7 7. Nc3
King's Gambit Accepted, Allgaier, Walker attack
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ng5 h6 6. Nxf7 Kxf7 7. Bc4+
King's Gambit Accepted, Allgaier, Urusov attack
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ng5 h6 6. Nxf7 Kxf7 7. Bc4+ d5 8. Bxd5+ Kg7 9. d4
King's Gambit Accepted, Allgaier, Schlechter defence
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ng5 Nf6 
King's Gambit Accepted, Kieseritsky, Paulsen defence
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 Bg7 
King's Gambit Accepted, Kieseritsky, long whip (Stockwhip, classical) defence
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 h5 
King's Gambit Accepted, Kieseritsky, long whip defence, Jaenisch variation
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 h5 6. Bc4 Rh7 7. d4 Bh6 8. Nc3
King's Gambit Accepted, Kieseritsky, Brentano (Campbell) defence
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 d5 
King's Gambit Accepted, Kieseritsky, Brentano defence, Kaplanek variation
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 d5 6. d4 Nf6 7. exd5 Qxd5 8. Nc3 Bb4 9. Kf2
King's Gambit Accepted, Kieseritsky, Brentano defence
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 d5 6. d4 Nf6 7. Bxf4
King's Gambit Accepted, Kieseritsky, Brentano defence, Caro variation
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 d5 6. d4 Nf6 7. Bxf4 Nxe4 8. Nd2
King's Gambit Accepted, Kieseritsky, Salvio (Rosenthal) defence
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 Qe7 
King's Gambit Accepted, Kieseritsky, Salvio defence, Cozio variation
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 Qe7 6. d4 f5 7. Bc4
King's Gambit Accepted, Kieseritsky, Polerio defence
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 Be7 
King's Gambit Accepted, Kieseritsky, Neumann defence
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 Nc6 
King's Gambit Accepted, Kieseritsky, Kolisch defence
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 d6 
King's Gambit Accepted, Kieseritsky, Berlin defence
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 Nf6 
King's Gambit Accepted, Kieseritsky, Berlin defence, Riviere variation
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 Nf6 6. Nxg4 d5 
King's Gambit Accepted, Kieseritsky, Berlin defence, 6.Bc4
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 Nf6 6. Bc4
King's Gambit Accepted, Kieseritsky, Rice gambit
1. e4 e5 2. f4 exf4 3. Nf3 g5 4. h4 g4 5. Ne5 Nf6 6. Bc4 d5 7. exd5 Bd6 8. O-O
******C40: King's knight opening
King's knight opening
1. e4 e5 2. Nf3
Gunderam defence
1. e4 e5 2. Nf3 Qe7 
Greco defence
1. e4 e5 2. Nf3 Qf6 
Damiano's defence
1. e4 e5 2. Nf3 f6 
QP counter-gambit (elephant gambit)
1. e4 e5 2. Nf3 d5 
QP counter-gambit, Maroczy gambit
1. e4 e5 2. Nf3 d5 3. exd5 Bd6 
Latvian counter-gambit
1. e4 e5 2. Nf3 f5 
Latvian, Nimzovich variation
1. e4 e5 2. Nf3 f5 3. Nxe5 Qf6 4. d4 d6 5. Nc4 fxe4 6. Ne3
Latvian, Fraser defence
1. e4 e5 2. Nf3 f5 3. Nxe5 Nc6 
Latvian gambit, 3.Bc4
1. e4 e5 2. Nf3 f5 3. Bc4
Latvian, Behting variation
1. e4 e5 2. Nf3 f5 3. Bc4 fxe4 4. Nxe5 Qg5 5. Nf7 Qxg2 6. Rf1 d5 7. Nxh8 Nf6 
Latvian, Polerio variation
1. e4 e5 2. Nf3 f5 3. Bc4 fxe4 4. Nxe5 d5 
Latvian, corkscrew counter-gambit
1. e4 e5 2. Nf3 f5 3. Bc4 fxe4 4. Nxe5 Nf6 
******C41: Philidor's defence
Philidor's defence
1. e4 e5 2. Nf3 d6 
Philidor, Steinitz variation
1. e4 e5 2. Nf3 d6 3. Bc4 Be7 4. c3
Philidor, Lopez counter-gambit
1. e4 e5 2. Nf3 d6 3. Bc4 f5 
Philidor, Lopez counter-gambit, Jaenisch variation
1. e4 e5 2. Nf3 d6 3. Bc4 f5 4. d4 exd4 5. Ng5 Nh6 6. Nxh7
Philidor's defence
1. e4 e5 2. Nf3 d6 3. d4
Philidor, Philidor counter-gambit
1. e4 e5 2. Nf3 d6 3. d4 f5 
Philidor, Philidor counter-gambit, del Rio attack
1. e4 e5 2. Nf3 d6 3. d4 f5 4. dxe5 fxe4 5. Ng5 d5 6. e6
Philidor, Philidor counter-gambit, Berger variation
1. e4 e5 2. Nf3 d6 3. d4 f5 4. dxe5 fxe4 5. Ng5 d5 6. e6 Bc5 7. Nc3
Philidor, Philidor counter-gambit, Zukertort variation
1. e4 e5 2. Nf3 d6 3. d4 f5 4. Nc3
Philidor, exchange variation
1. e4 e5 2. Nf3 d6 3. d4 exd4 
Philidor, Boden variation
1. e4 e5 2. Nf3 d6 3. d4 exd4 4. Qxd4 Bd7 
Philidor, exchange variation
1. e4 e5 2. Nf3 d6 3. d4 exd4 4. Nxd4
Philidor, Paulsen attack
1. e4 e5 2. Nf3 d6 3. d4 exd4 4. Nxd4 d5 5. exd5
Philidor, exchange variation
1. e4 e5 2. Nf3 d6 3. d4 exd4 4. Nxd4 Nf6 
Philidor, Berger variation
1. e4 e5 2. Nf3 d6 3. d4 exd4 4. Nxd4 Nf6 5. Nc3 Be7 6. Be2 O-O 7. O-O c5 8. Nf3 Nc6 9. Bg5 Be6 10. Re1
Philidor, Larsen variation
1. e4 e5 2. Nf3 d6 3. d4 exd4 4. Nxd4 g6 
Philidor, Nimzovich (Jaenisch) variation
1. e4 e5 2. Nf3 d6 3. d4 Nf6 
Philidor, Improved Hanham variation
1. e4 e5 2. Nf3 d6 3. d4 Nf6 4. Nc3 Nbd7 
Philidor, Nimzovich, Sozin variation
1. e4 e5 2. Nf3 d6 3. d4 Nf6 4. Nc3 Nbd7 5. Bc4 Be7 6. O-O O-O 7. Qe2 c6 8. a4 exd4 
Philidor, Nimzovich, Larobok variation
1. e4 e5 2. Nf3 d6 3. d4 Nf6 4. Nc3 Nbd7 5. Bc4 Be7 6. Ng5 O-O 7. Bxf7+
Philidor, Nimzovich variation
1. e4 e5 2. Nf3 d6 3. d4 Nf6 4. dxe5
Philidor, Nimzovich, Sokolsky variation
1. e4 e5 2. Nf3 d6 3. d4 Nf6 4. dxe5 Nxe4 5. Nbd2
Philidor, Nimzovich, Rellstab variation
1. e4 e5 2. Nf3 d6 3. d4 Nf6 4. dxe5 Nxe4 5. Qd5
Philidor, Nimzovich, Locock variation
1. e4 e5 2. Nf3 d6 3. d4 Nf6 4. Ng5
Philidor, Nimzovich, Klein variation
1. e4 e5 2. Nf3 d6 3. d4 Nf6 4. Bc4
Philidor, Hanham variation
1. e4 e5 2. Nf3 d6 3. d4 Nd7 
Philidor, Hanham, Krause variation
1. e4 e5 2. Nf3 d6 3. d4 Nd7 4. Bc4 c6 5. O-O
Philidor, Hanham, Steiner variation
1. e4 e5 2. Nf3 d6 3. d4 Nd7 4. Bc4 c6 5. O-O Be7 6. dxe5
Philidor, Hanham, Kmoch variation
1. e4 e5 2. Nf3 d6 3. d4 Nd7 4. Bc4 c6 5. Ng5
Philidor, Hanham, Berger variation
1. e4 e5 2. Nf3 d6 3. d4 Nd7 4. Bc4 c6 5. Ng5 Nh6 6. f4 Be7 7. O-O O-O 8. c3 d5 
Philidor, Hanham, Schlechter variation
1. e4 e5 2. Nf3 d6 3. d4 Nd7 4. Bc4 c6 5. Nc3
Philidor, Hanham, Delmar variation
1. e4 e5 2. Nf3 d6 3. d4 Nd7 4. Bc4 c6 5. c3
******C42: Petrov's defence
Petrov's defence
1. e4 e5 2. Nf3 Nf6 
Petrov, French attack
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. d3
Petrov, Kaufmann attack
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. c4
Petrov, Nimzovich attack
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. Nc3
Petrov, Cozio (Lasker) attack
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. Qe2
Petrov, classical attack
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. d4
Petrov, classical attack, Chigorin variation
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. d4 d5 6. Bd3 Be7 7. O-O Nc6 8. Re1
Petrov, classical attack, Berger variation
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. d4 d5 6. Bd3 Be7 7. O-O Nc6 8. Re1 Bg4 9. c3 f5 10. Nbd2
Petrov, classical attack, Krause variation
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. d4 d5 6. Bd3 Be7 7. O-O Nc6 8. Re1 Bg4 9. c3 f5 10. c4
Petrov, classical attack, Maroczy variation
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. d4 d5 6. Bd3 Be7 7. O-O Nc6 8. Re1 Bg4 9. c3 f5 10. c4 Bh4 
Petrov, classical attack, Jaenisch variation
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. d4 d5 6. Bd3 Be7 7. O-O Nc6 8. c4
Petrov, classical attack, Mason variation
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. d4 d5 6. Bd3 Be7 7. O-O O-O 
Petrov, classical attack, Marshall variation
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. d4 d5 6. Bd3 Bd6 
Petrov, classical attack, Tarrasch variation
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. d4 d5 6. Bd3 Bd6 7. O-O O-O 8. c4 Bg4 
Petrov, classical attack, Marshall trap
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. d4 d5 6. Bd3 Bd6 7. O-O O-O 8. c4 Bg4 9. cxd5 f5 10. Re1 Bxh2+ 
Petrov, classical attack, close variation
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. d4 Nf6 
Petrov, Cochrane gambit
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nxf7
Petrov, Paulsen attack
1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nc4
Petrov, Damiano variation
1. e4 e5 2. Nf3 Nf6 3. Nxe5 Nxe4 
Petrov three knights game
1. e4 e5 2. Nf3 Nf6 3. Nc3
Petrov, Italian variation
1. e4 e5 2. Nf3 Nf6 3. Bc4
******C43: Petrov, modern (Steinitz) attack
Petrov, modern (Steinitz) attack
1. e4 e5 2. Nf3 Nf6 3. d4
Petrov, modern attack, main line
1. e4 e5 2. Nf3 Nf6 3. d4 exd4 4. e5 Ne4 5. Qxd4
Petrov, modern attack, Steinitz variation
1. e4 e5 2. Nf3 Nf6 3. d4 exd4 4. e5 Ne4 5. Qe2
Petrov, modern attack, Bardeleben variation
1. e4 e5 2. Nf3 Nf6 3. d4 exd4 4. e5 Ne4 5. Qe2 Nc5 6. Nxd4 Nc6 
Petrov, Urusov gambit
1. e4 e5 2. Nf3 Nf6 3. d4 exd4 4. Bc4
Petrov, modern attack, Symmetrical variation
1. e4 e5 2. Nf3 Nf6 3. d4 Nxe4 
Petrov, modern attack, Trifunovic variation
1. e4 e5 2. Nf3 Nf6 3. d4 Nxe4 4. Bd3 d5 5. Nxe5 Bd6 6. O-O O-O 7. c4 Bxe5 
******C44: King's pawn game
King's pawn game
1. e4 e5 2. Nf3 Nc6 
Irish (Chicago) gambit
1. e4 e5 2. Nf3 Nc6 3. Nxe5 Nxe5 4. d4
Konstantinopolsky opening
1. e4 e5 2. Nf3 Nc6 3. g3
Dresden opening
1. e4 e5 2. Nf3 Nc6 3. c4
Inverted Hungarian
1. e4 e5 2. Nf3 Nc6 3. Be2
Inverted Hanham
1. e4 e5 2. Nf3 Nc6 3. Be2 Nf6 4. d3 d5 5. Nbd2
Tayler opening
1. e4 e5 2. Nf3 Nc6 3. Be2 Nf6 4. d4
Ponziani opening
1. e4 e5 2. Nf3 Nc6 3. c3
Ponziani, Caro variation
1. e4 e5 2. Nf3 Nc6 3. c3 d5 4. Qa4 Bd7 
Ponziani, Leonhardt variation
1. e4 e5 2. Nf3 Nc6 3. c3 d5 4. Qa4 Nf6 
Ponziani, Steinitz variation
1. e4 e5 2. Nf3 Nc6 3. c3 d5 4. Qa4 f6 
Ponziani, Jaenisch counter-attack
1. e4 e5 2. Nf3 Nc6 3. c3 Nf6 
Ponziani, Fraser defence
1. e4 e5 2. Nf3 Nc6 3. c3 Nf6 4. d4 Nxe4 5. d5 Bc5 
Ponziani, Reti variation
1. e4 e5 2. Nf3 Nc6 3. c3 Nge7 
Ponziani, Romanishin variation
1. e4 e5 2. Nf3 Nc6 3. c3 Be7 
Ponziani counter-gambit
1. e4 e5 2. Nf3 Nc6 3. c3 f5 
Ponziani counter-gambit, Schmidt attack
1. e4 e5 2. Nf3 Nc6 3. c3 f5 4. d4 d6 5. d5
Ponziani counter-gambit, Cordel variation
1. e4 e5 2. Nf3 Nc6 3. c3 f5 4. d4 d6 5. d5 fxe4 6. Ng5 Nb8 7. Nxe4 Nf6 8. Bd3 Be7 
Scotch opening
1. e4 e5 2. Nf3 Nc6 3. d4
Scotch, Lolli variation
1. e4 e5 2. Nf3 Nc6 3. d4 Nxd4 
Scotch, Cochrane variation
1. e4 e5 2. Nf3 Nc6 3. d4 Nxd4 4. Nxe5 Ne6 5. Bc4 c6 6. O-O Nf6 7. Nxf7
Scotch, Relfsson gambit ('MacLopez')
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Bb5
Scotch, Goering gambit
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. c3
Scotch, Sea-cadet mate
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. c3 dxc3 5. Nxc3 d6 6. Bc4 Bg4 7. O-O Ne5 8. Nxe5 Bxd1 9. Bxf7+ Ke7 10. Nd5+
Scotch, Goering gambit
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. c3 dxc3 5. Nxc3 Bb4 
Scotch, Goering gambit, Bardeleben variation
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. c3 dxc3 5. Nxc3 Bb4 6. Bc4 Nf6 
Scotch gambit
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Bc4
Scotch gambit, Anderssen (Paulsen, Suhle) counter-attack
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Bc4 Bc5 5. O-O d6 6. c3 Bg4 
Scotch gambit
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Bc4 Bc5 5. Ng5
Scotch gambit, Cochrane-Shumov defence
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Bc4 Bc5 5. Ng5 Nh6 6. Nxf7 Nxf7 7. Bxf7+ Kxf7 8. Qh5+ g6 9. Qxc5 d5 
Scotch gambit, Vitzhum attack
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Bc4 Bc5 5. Ng5 Nh6 6. Qh5
Scotch gambit
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Bc4 Bb4+ 
Scotch gambit, Hanneken variation
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Bc4 Bb4+ 5. c3 dxc3 6. O-O cxb2 7. Bxb2 Nf6 8. Ng5 O-O 9. e5 Nxe5 
Scotch gambit
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Bc4 Bb4+ 5. c3 dxc3 6. bxc3
Scotch gambit, Cochrane variation
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Bc4 Bb4+ 5. c3 dxc3 6. bxc3 Ba5 7. e5
Scotch gambit, Benima defence
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Bc4 Be7 
Scotch gambit, Dubois-Reti defence
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Bc4 Nf6 
******C45: Scotch game
Scotch game
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4
Scotch, Ghulam Kassim variation
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Nxd4 5. Qxd4 d6 6. Bd3
Scotch, Pulling counter-attack
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Qh4 
Scotch, Horwitz attack
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Qh4 5. Nb5
Scotch, Berger variation
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Qh4 5. Nb5 Bb4+ 6. Nd2 Qxe4+ 7. Be2 Qxg2 8. Bf3 Qh3 9. Nxc7+ Kd8 10. Nxa8 Nf6 11. a3
Scotch game
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Qh4 5. Nb5 Bb4+ 6. Bd2
Scotch, Rosenthal variation
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Qh4 5. Nb5 Bb4+ 6. Bd2 Qxe4+ 7. Be2 Kd8 8. O-O Bxd2 9. Nxd2 Qg6 
Scotch, Fraser attack
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Qh4 5. Nf3
Scotch, Steinitz variation
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Qh4 5. Nc3
Scotch, Schmidt variation
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Nf6 
Scotch, Mieses variation
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Nf6 5. Nxc6 bxc6 6. e5
Scotch, Tartakower variation
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Nf6 5. Nxc6 bxc6 6. Nd2
Scotch game
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Bc5 
Scotch, Blackburne attack
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Bc5 5. Be3 Qf6 6. c3 Nge7 7. Qd2
Scotch, Gottschall variation
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Bc5 5. Be3 Qf6 6. c3 Nge7 7. Qd2 d5 8. Nb5 Bxe3 9. Qxe3 O-O 10. Nxc7 Rb8 11. Nxd5 Nxd5 12. exd5 Nb4 
Scotch, Paulsen attack
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Bc5 5. Be3 Qf6 6. c3 Nge7 7. Bb5
Scotch, Paulsen, Gunsberg defence
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Bc5 5. Be3 Qf6 6. c3 Nge7 7. Bb5 Nd8 
Scotch, Meitner variation
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Bc5 5. Be3 Qf6 6. c3 Nge7 7. Nc2
Scotch, Blumenfeld attack
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Bc5 5. Be3 Qf6 6. Nb5
Scotch, Potter variation
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Bc5 5. Nb3
Scotch, Romanishin variation
1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Bc5 5. Nb3 Bb4+ 
******C46: Three knights game
Three knights game
1. e4 e5 2. Nf3 Nc6 3. Nc3
Three knights, Schlechter variation
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bb4 4. Nd5 Nf6 
Three knights, Winawer defence (Gothic defence)
1. e4 e5 2. Nf3 Nc6 3. Nc3 f5 
Three knights, Steinitz variation
1. e4 e5 2. Nf3 Nc6 3. Nc3 g6 
Three knights, Steinitz, Rosenthal variation
1. e4 e5 2. Nf3 Nc6 3. Nc3 g6 4. d4 exd4 5. Nd5
Four knights game
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 
Four knights, Schultze-Mueller gambit
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Nxe5
Four knights, Italian variation
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bc4
Four knights, Gunsberg variation
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. a3
******C47: Four knights, Scotch variation
Four knights, Scotch variation
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. d4
Four knights, Scotch, Krause variation
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. d4 Bb4 5. Nxe5
Four knights, Scotch, 4...exd4
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. d4 exd4 
Four knights, Belgrade gambit
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. d4 exd4 5. Nd5
******C48: Four knights, Spanish variation
Four knights, Spanish variation
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5
Four knights, Ranken variation
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 a6 5. Bxc6
Four knights, Spielmann variation
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 a6 5. Bxc6 dxc6 6. Nxe5 Nxe4 7. Nxe4 Qd4 8. O-O Qxe5 9. Re1 Be6 10. d4 Qd5 
Four knights, Spanish, classical defence
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bc5 
Four knights, Bardeleben variation
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bc5 5. O-O O-O 6. Nxe5 Nxe5 7. d4 Bd6 8. f4 Nc6 9. e5 Bb4 
Four knights, Marshall variation
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bc5 5. O-O O-O 6. Nxe5 Nd4 
Four knights, Rubinstein counter-gambit
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Nd4 
Four knights, Rubinstein counter-gambit, Bogolyubov variation
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Nd4 5. Nxe5 Qe7 6. f4
Four knights, Rubinstein counter-gambit, 5.Be2
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Nd4 5. Be2
Four knights, Rubinstein counter-gambit Maroczy variation
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Nd4 5. Be2 Nxf3+ 6. Bxf3 Bc5 7. O-O O-O 8. d3 d6 9. Na4 Bb6 
Four knights, Rubinstein counter-gambit, exchange variation
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Nd4 5. Nxd4
Four knights, Rubinstein counter-gambit, Henneberger variation
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Nd4 5. O-O
******C49: Four knights, double Ruy Lopez
Four knights, double Ruy Lopez
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 
Four knights, Gunsberg counter-attack
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. Nd5 Nxd5 7. exd5 e4 
Four knights, double Ruy Lopez
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. d3
Four knights, Alatortsev variation
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. d3 Qe7 7. Ne2 d5 
Four knights
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. d3 Bxc3 
Four knights, Janowski variation
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. d3 Bxc3 7. bxc3 d6 8. Re1
Four knights, Svenonius variation
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. d3 Bxc3 7. bxc3 d5 
Four knights, symmetrical variation
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. d3 d6 
Four knights, symmetrical, Metger unpin
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. d3 d6 7. Bg5 Bxc3 8. bxc3 Qe7 
Four knights, symmetrical, Capablanca variation
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. d3 d6 7. Bg5 Bxc3 8. bxc3 Qe7 9. Re1 Nd8 10. d4 Bg4 
Four knights, symmetrical, Pillsbury variation
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. d3 d6 7. Bg5 Ne7 
Four knights, symmetrical, Blake variation
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. d3 d6 7. Bg5 Ne7 8. Nh4 c6 9. Bc4 d5 10. Bb3 Qd6 
Four knights, symmetrical, Tarrasch variation
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. d3 d6 7. Bg5 Be6 
Four knights, symmetrical, Maroczy system
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. d3 d6 7. Ne2
Four knights, Nimzovich (Paulsen) variation
1. e4 e5 2. Nf3 Nc6 3. Nc3 Nf6 4. Bb5 Bb4 5. O-O O-O 6. Bxc6
******C50: King's pawn game
King's pawn game
1. e4 e5 2. Nf3 Nc6 3. Bc4
Blackburne shilling gambit
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nd4 4. Nxe5 Qg5 5. Nxf7 Qxg2 6. Rf1 Qxe4+ 7. Be2 Nf3+ 
Rousseau gambit
1. e4 e5 2. Nf3 Nc6 3. Bc4 f5 
Hungarian defence
1. e4 e5 2. Nf3 Nc6 3. Bc4 Be7 
Hungarian defence, Tartakower variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Be7 4. d4 exd4 5. c3 Nf6 6. e5 Ne4 
Giuoco Piano
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 
Giuoco Piano, four knights variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. Nc3 Nf6 
Giuoco Piano, Jerome gambit
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. Bxf7+
Giuoco Pianissimo
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. d3
Giuoco Pianissimo, Dubois variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. d3 f5 5. Ng5 f4 
Giuoco Pianissimo
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. d3 Nf6 
Giuoco Pianissimo, Italian four knights variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. d3 Nf6 5. Nc3
Giuoco Pianissimo, Canal variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. d3 Nf6 5. Nc3 d6 6. Bg5
******C51: Evans gambit declined
Evans gambit declined
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4
Evans gambit declined, Lange variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bb6 5. b5 Na5 6. Nxe5 Nh6 
Evans gambit declined, Pavlov variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bb6 5. b5 Na5 6. Nxe5 Nh6 7. d4 d6 8. Bxh6 dxe5 9. Bxg7 Rg8 10. Bxf7+ Kxf7 11. Bxe5 Qg5 12. Nd2
Evans gambit declined, Hirschbach variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bb6 5. b5 Na5 6. Nxe5 Qg5 
Evans gambit declined, Vasquez variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bb6 5. b5 Na5 6. Nxe5 Qg5 7. Bxf7+ Ke7 8. Qh5
Evans gambit declined, Hicken variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bb6 5. b5 Na5 6. Nxe5 Qg5 7. Qf3 Qxe5 8. Qxf7+ Kd8 9. Bb2
Evans gambit declined, 5.a4
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bb6 5. a4
Evans gambit declined, Showalter variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bb6 5. a4 a6 6. Nc3
Evans gambit declined, Cordel variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bb6 5. Bb2
Evans counter-gambit
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 d5 
Evans gambit
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 
Evans gambit, normal variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Bc5 6. d4 exd4 7. O-O d6 8. cxd4 Bb6 
Evans gambit, Ulvestad variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Bc5 6. d4 exd4 7. O-O d6 8. cxd4 Bb6 9. d5 Na5 10. Bb2
Evans gambit, Paulsen variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Bc5 6. d4 exd4 7. O-O d6 8. cxd4 Bb6 9. d5 Na5 10. Bb2 Ne7 
Evans gambit, Morphy attack
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Bc5 6. d4 exd4 7. O-O d6 8. cxd4 Bb6 9. Nc3
Evans gambit, Goering attack
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Bc5 6. d4 exd4 7. O-O d6 8. cxd4 Bb6 9. Nc3 Na5 10. Bg5
Evans gambit, Steinitz variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Bc5 6. d4 exd4 7. O-O d6 8. cxd4 Bb6 9. Nc3 Na5 10. Bg5 f6 11. Be3
Evans gambit
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Bc5 6. d4 exd4 7. O-O d6 8. cxd4 Bb6 9. Nc3 Bg4 
Evans gambit, Fraser attack
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Bc5 6. d4 exd4 7. O-O d6 8. cxd4 Bb6 9. Nc3 Bg4 10. Qa4
Evans gambit, Fraser-Mortimer attack
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Bc5 6. d4 exd4 7. O-O d6 8. cxd4 Bb6 9. Nc3 Bg4 10. Qa4 Bd7 11. Qb3 Na5 12. Bxf7+ Kf8 13. Qc2
Evans gambit, Stone-Ware variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Bd6 
Evans gambit, Mayet defence
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Bf8 
Evans gambit, 5...Be7
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Be7 
Evans gambit, Cordel variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Be7 6. d4 Na5 
******C52: Evans gambit
Evans gambit
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 
Evans gambit, compromised defence
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. d4 exd4 7. O-O dxc3 
Evans gambit, compromised defence, Paulsen variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. d4 exd4 7. O-O dxc3 8. Qb3 Qf6 9. e5 Qg6 10. Nxc3 Nge7 11. Ba3
Evans gambit, compromised defence, Potter variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. d4 exd4 7. O-O dxc3 8. Qb3 Qf6 9. e5 Qg6 10. Nxc3 Nge7 11. Rd1
Evans gambit, Leonhardt variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. d4 b5 
Evans gambit
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. d4 d6 
Evans gambit, Tartakower attack
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. d4 d6 7. Qb3
Evans gambit, Levenfish variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. d4 d6 7. Qb3 Qd7 8. dxe5 dxe5 9. O-O Bb6 10. Ba3 Na5 11. Nxe5
Evans gambit, Sokolsky variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. d4 d6 7. Bg5
Evans gambit
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. O-O
Evans gambit, Richardson attack
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. O-O Nf6 7. d4 O-O 8. Nxe5
Evans gambit
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. O-O d6 
Evans gambit, Waller attack
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. O-O d6 7. d4 exd4 8. Qb3
Evans gambit, Lasker defence
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. O-O d6 7. d4 Bb6 
Evans gambit, Sanders-Alapin variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. O-O d6 7. d4 Bd7 
Evans gambit, Alapin-Steinitz variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. b4 Bxb4 5. c3 Ba5 6. O-O d6 7. d4 Bg4 
******C53: Giuoco Piano
Giuoco Piano
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3
Giuoco Piano, LaBourdonnais variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 d6 5. d4 exd4 6. cxd4 Bb6 
Giuoco Piano, close variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Qe7 
Giuoco Piano, centre-holding variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Qe7 5. d4 Bb6 
Giuoco Piano, Tarrasch variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Qe7 5. d4 Bb6 6. O-O Nf6 7. a4 a6 8. Re1 d6 9. h3
Giuoco Piano, Mestel variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Qe7 5. d4 Bb6 6. Bg5
Giuoco Piano, Eisinger variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Qe7 5. d4 Bb6 6. d5 Nb8 7. d6
Giuoco Piano
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 
Giuoco Piano, Bird's attack
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. b4
Giuoco Piano
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4
Giuoco Piano, Ghulam Kassim variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. e5 Ne4 7. Bd5 Nxf2 8. Kxf2 dxc3+ 9. Kg3
Giuoco Piano
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. e5 d5 
Giuoco Piano, Anderssen variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. e5 d5 7. Bb5 Ne4 8. cxd4 Bb4+ 
******C54: Giuoco Piano
Giuoco Piano
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. cxd4
Giuoco Piano, Krause variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. cxd4 Bb4+ 7. Bd2 Nxe4 8. Bxb4 Nxb4 9. Bxf7+ Kxf7 10. Qb3+ d5 11. Ne5+ Kf6 12. f3
Giuoco Piano, Cracow variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. cxd4 Bb4+ 7. Kf1
Giuoco Piano, Greco's attack
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. cxd4 Bb4+ 7. Nc3
Giuoco Piano, Greco variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. cxd4 Bb4+ 7. Nc3 Nxe4 8. O-O Nxc3 
Giuoco Piano, Bernstein variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. cxd4 Bb4+ 7. Nc3 Nxe4 8. O-O Nxc3 9. bxc3 Bxc3 10. Qb3 d5 
Giuoco Piano, Aitken variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. cxd4 Bb4+ 7. Nc3 Nxe4 8. O-O Nxc3 9. bxc3 Bxc3 10. Ba3
Giuoco Piano
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. cxd4 Bb4+ 7. Nc3 Nxe4 8. O-O Bxc3 
Giuoco Piano, Steinitz variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. cxd4 Bb4+ 7. Nc3 Nxe4 8. O-O Bxc3 9. bxc3 d5 10. Ba3
Giuoco Piano, Moeller (Therkatz) attack
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. cxd4 Bb4+ 7. Nc3 Nxe4 8. O-O Bxc3 9. d5
Giuoco Piano, Therkatz-Herzog variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. cxd4 Bb4+ 7. Nc3 Nxe4 8. O-O Bxc3 9. d5 Bf6 10. Re1 Ne7 11. Rxe4 d6 12. Bg5 Bxg5 13. Nxg5 O-O 14. Nxh7
Giuoco Piano, Moeller, bayonet attack
1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 exd4 6. cxd4 Bb4+ 7. Nc3 Nxe4 8. O-O Bxc3 9. d5 Bf6 10. Re1 Ne7 11. Rxe4 d6 12. g4
******C55: Two knights defence
Two knights defence
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 
Giuoco piano, Rosentreter variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. O-O Bc5 5. d4 Bxd4 6. Nxd4 Nxd4 7. Bg5 h6 8. Bh4 g5 9. f4
Giuoco piano
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. O-O Bc5 5. d4 Bxd4 6. Nxd4 Nxd4 7. Bg5 d6 
Giuoco piano, Holzhausen attack
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. O-O Bc5 5. d4 Bxd4 6. Nxd4 Nxd4 7. Bg5 d6 8. f4 Qe7 9. fxe5 dxe5 10. Nc3
Two knights defence (Modern bishop's opening)
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d3
Two knights defence
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4
Two knights defence, Keidanz variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. e5 d5 6. Bb5 Ne4 7. Nxd4 Bc5 8. Nxc6 Bxf2+ 9. Kf1 Qh4 
Two knights defence, Perreux variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. Ng5
Two knights defence
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. O-O
two knights, Max Lange attack
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. O-O Bc5 6. e5
two knights, Max Lange attack, Berger variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. O-O Bc5 6. e5 d5 7. exf6 dxc4 8. Re1+ Be6 9. Ng5 Qd5 10. Nc3 Qf5 11. g4 Qg6 12. Nce4 Bb6 13. f4 O-O-O 
two knights, Max Lange attack, Marshall variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. O-O Bc5 6. e5 d5 7. exf6 dxc4 8. Re1+ Be6 9. Ng5 Qd5 10. Nc3 Qf5 11. Nce4
two knights, Max Lange attack, Rubinstein variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. O-O Bc5 6. e5 d5 7. exf6 dxc4 8. Re1+ Be6 9. Ng5 Qd5 10. Nc3 Qf5 11. Nce4 Bf8 
two knights, Max Lange attack, Loman defence
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. O-O Bc5 6. e5 d5 7. exf6 dxc4 8. Re1+ Be6 9. Ng5 g6 
two knights, Max Lange attack, Schlechter variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. O-O Bc5 6. e5 d5 7. exf6 dxc4 8. Re1+ Be6 9. fxg7
two knights, Max Lange attack, Steinitz variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. O-O Bc5 6. e5 Ng4 
two knights, Max Lange attack, Krause variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. O-O Bc5 6. e5 Ng4 7. c3
******C56: Two knights defence
Two knights defence
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. O-O Nxe4 
two knights defence, Yurdansky attack
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. O-O Nxe4 6. Re1 d5 7. Bxd5 Qxd5 8. Nc3 Qa5 9. Nxe4 Be6 10. Bg5 h6 11. Bh4 g5 12. Nf6+ Ke7 13. b4
two knights defence, Canal variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d4 exd4 5. O-O Nxe4 6. Re1 d5 7. Nc3
******C57: Two knights defence
Two knights defence
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5
two knights defence, Wilkes Barre (Traxler) variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 Bc5 
two knights defence, Ulvestad variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 b5 
two knights defence, Fritz variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Nd4 
two knights defence, Fritz, Gruber variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Nd4 6. c3 b5 7. Bf1 Nxd5 8. Ne4
two knights defence, Lolli attack
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Nxd5 6. d4
two knights defence, Pincus variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Nxd5 6. d4 Bb4+ 
two knights defence, Fegatello attack
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Nxd5 6. Nxf7
two knights defence, Fegatello attack, Leonhardt variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Nxd5 6. Nxf7 Kxf7 7. Qf3+ Ke6 8. Nc3 Ncb4 9. Qe4 c6 10. a3 Na6 11. d4 Nac7 
two knights defence, Fegatello attack, Polerio defence
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Nxd5 6. Nxf7 Kxf7 7. Qf3+ Ke6 8. Nc3 Nce7 
******C58: two knights defence
two knights defence
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 
two knights defence, Kieseritsky variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 6. d3
two knights defence, Yankovich variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 6. d3 h6 7. Nf3 e4 8. Qe2 Nxc4 9. dxc4 Bc5 10. Nfd2
two knights defence, Maroczy variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 6. d3 h6 7. Nf3 e4 8. Qe2 Nxc4 9. dxc4 Be7 
Two knights defence
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 6. Bb5+
two knights defence, Bogolyubov variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 6. Bb5+ c6 7. dxc6 bxc6 8. Qf3
two knights defence, Paoli variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 6. Bb5+ c6 7. dxc6 bxc6 8. Qf3 Qc7 9. Bd3
two knights defence, Colman variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 6. Bb5+ c6 7. dxc6 bxc6 8. Qf3 Rb8 
two knights defence, Blackburne variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 6. Bb5+ c6 7. dxc6 bxc6 8. Qf3 cxb5 
Two knights defence
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 6. Bb5+ c6 7. dxc6 bxc6 8. Be2
******C59: Two knights defence
Two knights defence
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 6. Bb5+ c6 7. dxc6 bxc6 8. Be2 h6 
two knights defence, Knorre variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 6. Bb5+ c6 7. dxc6 bxc6 8. Be2 h6 9. Nf3 e4 10. Ne5 Bd6 11. d4 Qc7 12. Bd2
two knights defence, Goering variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 6. Bb5+ c6 7. dxc6 bxc6 8. Be2 h6 9. Nf3 e4 10. Ne5 Qc7 
two knights defence, Steinitz variation
1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Ng5 d5 5. exd5 Na5 6. Bb5+ c6 7. dxc6 bxc6 8. Be2 h6 9. Nh3
******C60: Ruy Lopez (Spanish opening)
Ruy Lopez (Spanish opening)
1. e4 e5 2. Nf3 Nc6 3. Bb5
Ruy Lopez, Nuernberg variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 f6 
Ruy Lopez, Pollock defence
1. e4 e5 2. Nf3 Nc6 3. Bb5 Na5 
Ruy Lopez, Lucena defence
1. e4 e5 2. Nf3 Nc6 3. Bb5 Be7 
Ruy Lopez, Vinogradov variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 Qe7 
Ruy Lopez, Brentano defence
1. e4 e5 2. Nf3 Nc6 3. Bb5 g5 
Ruy Lopez, fianchetto (Smyslov/Barnes) defence
1. e4 e5 2. Nf3 Nc6 3. Bb5 g6 
Ruy Lopez, Cozio defence
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nge7 
Ruy Lopez, Cozio defence, Paulsen variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nge7 4. Nc3 g6 
******C61: Ruy Lopez, Bird's defence
Ruy Lopez, Bird's defence
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nd4 
Ruy Lopez, Bird's defence, Paulsen variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nd4 4. Nxd4 exd4 5. O-O Ne7 
******C62: Ruy Lopez, old Steinitz defence
Ruy Lopez, old Steinitz defence
1. e4 e5 2. Nf3 Nc6 3. Bb5 d6 
Ruy Lopez, old Steinitz defence, Nimzovich attack
1. e4 e5 2. Nf3 Nc6 3. Bb5 d6 4. d4 Bd7 5. Nc3 Nf6 6. Bxc6
Ruy Lopez, old Steinitz defence, semi-Duras variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 d6 4. d4 Bd7 5. c4
******C63: Ruy Lopez, Schliemann defence
Ruy Lopez, Schliemann defence
1. e4 e5 2. Nf3 Nc6 3. Bb5 f5 
Ruy Lopez, Schliemann defence, Berger variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 f5 4. Nc3
******C64: Ruy Lopez, classical (Cordel) defence
Ruy Lopez, classical (Cordel) defence
1. e4 e5 2. Nf3 Nc6 3. Bb5 Bc5 
Ruy Lopez, classical defence, Zaitsev variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 Bc5 4. O-O Nd4 5. b4
Ruy Lopez, classical defence, 4.c3
1. e4 e5 2. Nf3 Nc6 3. Bb5 Bc5 4. c3
Ruy Lopez, classical defence, Benelux variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 Bc5 4. c3 Nf6 5. O-O O-O 6. d4 Bb6 
Ruy Lopez, classical defence, Charousek variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 Bc5 4. c3 Bb6 
Ruy Lopez, classical defence, Boden variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 Bc5 4. c3 Qe7 
Ruy Lopez, Cordel gambit
1. e4 e5 2. Nf3 Nc6 3. Bb5 Bc5 4. c3 f5 
******C65: Ruy Lopez, Berlin defence
Ruy Lopez, Berlin defence
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 
Ruy Lopez, Berlin defence, Nyholm attack
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. d4 exd4 5. O-O
Ruy Lopez, Berlin defence, Mortimer variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. d3 Ne7 
Ruy Lopez, Berlin defence, Mortimer trap
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. d3 Ne7 5. Nxe5 c6 
Ruy Lopez, Berlin defence, Anderssen variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. d3 d6 5. Bxc6+
Ruy Lopez, Berlin defence, Duras variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. d3 d6 5. c4
Ruy Lopez, Berlin defence, Kaufmann variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. d3 Bc5 5. Be3
Ruy Lopez, Berlin defence, 4.O-O
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O
Ruy Lopez, Berlin defence, Beverwijk variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Bc5 
******C66: Ruy Lopez, Berlin defence, 4.O-O, d6
Ruy Lopez, Berlin defence, 4.O-O, d6
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O d6 
Ruy Lopez, Berlin defence, hedgehog variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O d6 5. d4 Bd7 6. Nc3 Be7 
Ruy Lopez, Berlin defence, Tarrasch trap
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O d6 5. d4 Bd7 6. Nc3 Be7 7. Re1 O-O 
Ruy Lopez, closed Berlin defence, Bernstein variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O d6 5. d4 Bd7 6. Nc3 Be7 7. Bg5
Ruy Lopez, closed Berlin defence, Showalter variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O d6 5. d4 Bd7 6. Nc3 Be7 7. Bxc6
Ruy Lopez, closed Berlin defence, Wolf variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O d6 5. d4 Bd7 6. Nc3 exd4 
Ruy Lopez, closed Berlin defence, Chigorin variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O d6 5. d4 Nd7 
******C67: Ruy Lopez, Berlin defence, open variation
Ruy Lopez, Berlin defence, open variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Nxe4 
Ruy Lopez, open Berlin defence, l'Hermet variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Nxe4 5. d4 Nd6 6. dxe5
Ruy Lopez, open Berlin defence, Showalter variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Nxe4 5. d4 Nd6 6. Ba4
Ruy Lopez, open Berlin defence, 5...Be7
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Nxe4 5. d4 Be7 
Ruy Lopez, Berlin defence, Rio de Janeiro variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Nxe4 5. d4 Be7 6. Qe2 Nd6 7. Bxc6 bxc6 8. dxe5 Nb7 9. Nc3 O-O 10. Re1 Nc5 11. Nd4 Ne6 12. Be3 Nxd4 13. Bxd4 c5 
Ruy Lopez, Berlin defence, Zukertort variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Nxe4 5. d4 Be7 6. Qe2 Nd6 7. Bxc6 bxc6 8. dxe5 Nb7 9. c4
Ruy Lopez, Berlin defence, Pillsbury variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Nxe4 5. d4 Be7 6. Qe2 Nd6 7. Bxc6 bxc6 8. dxe5 Nb7 9. b3
Ruy Lopez, Berlin defence, Winawer attack
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Nxe4 5. d4 Be7 6. Qe2 Nd6 7. Bxc6 bxc6 8. dxe5 Nb7 9. Nd4
Ruy Lopez, Berlin defence, Cordel variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Nxe4 5. d4 Be7 6. Qe2 Nd6 7. Bxc6 bxc6 8. dxe5 Nf5 
Ruy Lopez, Berlin defence, Trifunovic variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Nxe4 5. d4 Be7 6. Qe2 d5 
Ruy Lopez, Berlin defence, Minckwitz variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Nxe4 5. d4 Be7 6. dxe5
Ruy Lopez, Berlin defence, Rosenthal variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Nxe4 5. d4 a6 
******C68: Ruy Lopez, exchange variation
Ruy Lopez, exchange variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Bxc6
Ruy Lopez, exchange, Alekhine variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Bxc6 dxc6 5. d4 exd4 6. Qxd4 Qxd4 7. Nxd4 Bd7 
Ruy Lopez, exchange, Keres variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Bxc6 dxc6 5. Nc3
Ruy Lopez, exchange, Romanovsky variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Bxc6 dxc6 5. Nc3 f6 6. d3
******C69: Ruy Lopez, exchange variation, 5.O-O
Ruy Lopez, exchange variation, 5.O-O
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Bxc6 dxc6 5. O-O
Ruy Lopez, exchange variation, Alapin gambit
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Bxc6 dxc6 5. O-O Bg4 6. h3 h5 
Ruy Lopez, exchange, Gligoric variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Bxc6 dxc6 5. O-O f6 
Ruy Lopez, exchange, Bronstein variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Bxc6 dxc6 5. O-O Qd6 
******C70: Ruy Lopez
Ruy Lopez
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4
Ruy Lopez, fianchetto defence deferred
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 g6 
Ruy Lopez, Cozio defence deferred
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nge7 
Ruy Lopez, Bird's defence deferred
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nd4 
Ruy Lopez, Alapin's defence deferred
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Bb4 
Ruy Lopez, Classical defence deferred
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Bc5 
Ruy Lopez, Caro variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 b5 
Ruy Lopez, Graz variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 b5 5. Bb3 Bc5 
Ruy Lopez, Taimanov (chase/wing/accelerated counterthrust) variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 b5 5. Bb3 Na5 
Ruy Lopez, Schliemann defence deferred
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 f5 
******C71: Ruy Lopez, modern Steinitz defence
Ruy Lopez, modern Steinitz defence
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 d6 
Ruy Lopez, Noah's ark trap
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 d6 5. d4 b5 6. Bb3 Nxd4 7. Nxd4 exd4 8. Qxd4 c5 
Ruy Lopez, modern Steinitz defence, Three knights variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 d6 5. Nc3
Ruy Lopez, modern Steinitz defence, Duras (Keres) variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 d6 5. c4
******C72: Ruy Lopez, modern Steinitz defence, 5.O-O
Ruy Lopez, modern Steinitz defence, 5.O-O
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 d6 5. O-O
******C73: Ruy Lopez, modern Steinitz defence, Richter variation
Ruy Lopez, modern Steinitz defence, Richter variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 d6 5. Bxc6+ bxc6 6. d4
Ruy Lopez, modern Steinitz defence, Alapin variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 d6 5. Bxc6+ bxc6 6. d4 f6 
******C74: Ruy Lopez, modern Steinitz defence
Ruy Lopez, modern Steinitz defence
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 d6 5. c3
Ruy Lopez, modern Steinitz defence, siesta variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 d6 5. c3 f5 
Ruy Lopez, Siesta, Kopayev variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 d6 5. c3 f5 6. exf5 Bxf5 7. O-O
******C75: Ruy Lopez, modern Steinitz defence
Ruy Lopez, modern Steinitz defence
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 d6 5. c3 Bd7 
Ruy Lopez, modern Steinitz defence, Rubinstein variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 d6 5. c3 Bd7 6. d4 Nge7 
******C76: Ruy Lopez, modern Steinitz defence, fianchetto (Bronstein) variation
Ruy Lopez, modern Steinitz defence, fianchetto (Bronstein) variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 d6 5. c3 Bd7 6. d4 g6 
******C77: Ruy Lopez, Morphy defence
Ruy Lopez, Morphy defence
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 
Ruy Lopez, four knights (Tarrasch) variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. Nc3
Ruy Lopez, Treybal (Bayreuth) variation (exchange var. deferred)
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. Bxc6
Ruy Lopez, Wormald (Alapin) attack
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. Qe2
Ruy Lopez, Wormald attack, Gruenfeld variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. Qe2 b5 6. Bb3 Be7 7. d4 d6 8. c3 Bg4 
Ruy Lopez, Anderssen variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. d3
Ruy Lopez, Morphy defence, Duras variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. d3 d6 6. c4
******C78: Ruy Lopez, 5.O-O
Ruy Lopez, 5.O-O
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O
Ruy Lopez, Wing attack
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O b5 6. Bb3 Be7 7. a4
Ruy Lopez, ...b5 & ...d6
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O b5 6. Bb3 d6 
Ruy Lopez, Rabinovich variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O b5 6. Bb3 d6 7. Ng5 d5 8. exd5 Nd4 9. Re1 Bc5 10. Rxe5+ Kf8 
Ruy Lopez, Archangelsk (counterthrust) variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O b5 6. Bb3 Bb7 
Ruy Lopez, Moeller defence
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Bc5 
******C79: Ruy Lopez, Steinitz defence deferred (Russian defence)
Ruy Lopez, Steinitz defence deferred (Russian defence)
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O d6 
Ruy Lopez, Steinitz defence deferred, Lipnitsky variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O d6 6. Bxc6+ bxc6 7. d4 Bg4 
Ruy Lopez, Steinitz defence deferred, Rubinstein variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O d6 6. Bxc6+ bxc6 7. d4 Nxe4 
Ruy Lopez, Steinitz defence deferred, Boleslavsky variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O d6 6. Bxc6+ bxc6 7. d4 Nxe4 8. Re1 f5 9. dxe5 d5 10. Nc3
******C80: Ruy Lopez, open (Tarrasch) defence
Ruy Lopez, open (Tarrasch) defence
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 
Ruy Lopez, open, Tartakower variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. Qe2
Ruy Lopez, open, Knorre variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. Nc3
Ruy Lopez, open, 6.d4
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4
Ruy Lopez, open, Riga variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 exd4 
Ruy Lopez, open, 6.d4 b5
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 
Ruy Lopez, open, Friess attack
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Nxe5
Ruy Lopez, open, Richter variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. d5
Ruy Lopez, open, 7.Bb3
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3
Ruy Lopez, open, Schlechter defence
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. a4 Nxd4 
Ruy Lopez, open, Berger variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. a4 Nxd4 9. Nxd4 exd4 10. Nc3
Ruy Lopez, open, Harksen gambit
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. c4
Ruy Lopez, open, 8.de
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5
Ruy Lopez, open, Zukertort variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Ne7 
Ruy Lopez, open, 8...Be6
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 
Ruy Lopez, open, Bernstein variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. Nbd2
Ruy Lopez, open, Bernstein variation, Karpov gambit
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. Nbd2 Nc5 10. c3 d4 11. Ng5
******C81: Ruy Lopez, open, Howell attack
Ruy Lopez, open, Howell attack
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. Qe2
Ruy Lopez, open, Howell attack, Ekstroem variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. Qe2 Be7 10. Rd1 O-O 11. c4 bxc4 12. Bxc4 Qd7 
Ruy Lopez, open, Howell attack, Adam variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. Qe2 Be7 10. c4
******C82: Ruy Lopez, open, 9.c3
Ruy Lopez, open, 9.c3
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. c3
Ruy Lopez, open, Berlin variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. c3 Nc5 
Ruy Lopez, open, Italian variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. c3 Bc5 
Ruy Lopez, open, St. Petersburg variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. c3 Bc5 10. Nbd2
Ruy Lopez, open, Dilworth variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. c3 Bc5 10. Nbd2 O-O 11. Bc2 Nxf2 
Ruy Lopez, open, Motzko attack
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. c3 Bc5 10. Qd3
Ruy Lopez, open, Motzko attack, Nenarokov variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. c3 Bc5 10. Qd3 Ne7 
******C83: Ruy Lopez, open, classical defence
Ruy Lopez, open, classical defence
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. c3 Be7 
Ruy Lopez, open, Malkin variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. c3 Be7 10. Nbd2 O-O 11. Qe2
Ruy Lopez, open, 9...Be7, 10.Re1
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. c3 Be7 10. Re1
Ruy Lopez, open, Tarrasch trap
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. c3 Be7 10. Re1 O-O 11. Nd4 Qd7 12. Nxe6 fxe6 13. Rxe4
Ruy Lopez, open, Breslau variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 b5 7. Bb3 d5 8. dxe5 Be6 9. c3 Be7 10. Re1 O-O 11. Nd4 Nxe5 
******C84: Ruy Lopez, closed defence
Ruy Lopez, closed defence
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 
Ruy Lopez, closed, centre attack
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. d4
Ruy Lopez, closed, Basque gambit (North Spanish variation)
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. d4 exd4 7. e5 Ne4 8. c3
******C85: Ruy Lopez, Exchange variation doubly deferred (DERLD)
Ruy Lopez, Exchange variation doubly deferred (DERLD)
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Bxc6
******C86: Ruy Lopez, Worrall attack
Ruy Lopez, Worrall attack
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Qe2
Ruy Lopez, Worrall attack, sharp line
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Qe2 b5 7. Bb3 O-O 
Ruy Lopez, Worrall attack, solid line
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Qe2 b5 7. Bb3 d6 
******C87: Ruy Lopez, closed, Averbach variation
Ruy Lopez, closed, Averbach variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 d6 
******C88: Ruy Lopez, closed
Ruy Lopez, closed
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3
Ruy Lopez, closed, Leonhardt variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. c3 Na5 9. Bc2 c5 10. d4 Qc7 11. h3 Nc6 12. d5 Nb8 13. Nbd2 g5 
Ruy Lopez, closed, Balla variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. c3 Na5 9. Bc2 c5 10. d4 Qc7 11. a4
Ruy Lopez, closed, 7...d6, 8.d4
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. d4
Ruy Lopez, Noah's ark trap
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. d4 Nxd4 9. Nxd4 exd4 10. Qxd4 c5 
Ruy Lopez, Trajkovic counter-attack
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 Bb7 
Ruy Lopez, closed, 7...O-O
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 
Ruy Lopez, closed, anti-Marshall 8.a4
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. a4
Ruy Lopez, closed, 8.c3
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3
******C89: Ruy Lopez, Marshall counter-attack
Ruy Lopez, Marshall counter-attack
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d5 
Ruy Lopez, Marshall counter-attack, 11...c6
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d5 9. exd5 Nxd5 10. Nxe5 Nxe5 11. Rxe5 c6 
Ruy Lopez, Marshall, Kevitz variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d5 9. exd5 Nxd5 10. Nxe5 Nxe5 11. Rxe5 c6 12. Bxd5 cxd5 13. d4 Bd6 14. Re3
Ruy Lopez, Marshall, main line, 12.d2d4
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d5 9. exd5 Nxd5 10. Nxe5 Nxe5 11. Rxe5 c6 12. d4
Ruy Lopez, Marshall, main line, 14...Qh3
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d5 9. exd5 Nxd5 10. Nxe5 Nxe5 11. Rxe5 c6 12. d4 Bd6 13. Re1 Qh4 14. g3 Qh3 
Ruy Lopez, Marshall, main line, Spassky variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d5 9. exd5 Nxd5 10. Nxe5 Nxe5 11. Rxe5 c6 12. d4 Bd6 13. Re1 Qh4 14. g3 Qh3 15. Be3 Bg4 16. Qd3 Rae8 17. Nd2 Re6 18. a4 Qh5 
Ruy Lopez, Marshall, Herman Steiner variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d5 9. exd5 e4 
******C90: Ruy Lopez, closed (with ...d6)
Ruy Lopez, closed (with ...d6)
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 
Ruy Lopez, closed, Pilnik variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. d3
Ruy Lopez, closed, Lutikov variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. Bc2
Ruy Lopez, closed, Suetin variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. a3
******C91: Ruy Lopez, closed, 9.d4
Ruy Lopez, closed, 9.d4
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. d4
Ruy Lopez, closed, Bogolyubov variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. d4 Bg4 
******C92: Ruy Lopez, closed, 9.h3
Ruy Lopez, closed, 9.h3
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3
Ruy Lopez, closed, Keres (9...a5) variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 a5 
Ruy Lopez, closed, Kholmov variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Be6 
Ruy Lopez, closed, Ragozin-Petrosian (`Keres') variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Nd7 
Ruy Lopez, closed, Flohr-Zaitsev system (Lenzerheide variation)
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Bb7 
******C93: Ruy Lopez, closed, Smyslov defence
Ruy Lopez, closed, Smyslov defence
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 h6 
******C94: Ruy Lopez, closed, Breyer defence
Ruy Lopez, closed, Breyer defence
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Nb8 
******C95: Ruy Lopez, closed, Breyer, 10.d4
Ruy Lopez, closed, Breyer, 10.d4
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Nb8 10. d4
Ruy Lopez, closed, Breyer, Borisenko variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Nb8 10. d4 Nbd7 
Ruy Lopez, closed, Breyer, Gligoric variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Nb8 10. d4 Nbd7 11. Nbd2 Bb7 12. Bc2 c5 
Ruy Lopez, closed, Breyer, Simagin variation
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Nb8 10. d4 Nbd7 11. Nh4
******C96: Ruy Lopez, closed (8...Na5)
Ruy Lopez, closed (8...Na5)
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Na5 10. Bc2
Ruy Lopez, closed, Rossolimo defence
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Na5 10. Bc2 c6 11. d4 Qc7 
Ruy Lopez, closed (10...c5)
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Na5 10. Bc2 c5 
Ruy Lopez, closed, Borisenko defence
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Na5 10. Bc2 c5 11. d4 Nc6 
Ruy Lopez, closed, Keres (...Nd7) defence
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Na5 10. Bc2 c5 11. d4 Nd7 
******C97: Ruy Lopez, closed, Chigorin defence
Ruy Lopez, closed, Chigorin defence
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Na5 10. Bc2 c5 11. d4 Qc7 
Ruy Lopez, closed, Chigorin, Yugoslav system
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Na5 10. Bc2 c5 11. d4 Qc7 12. Nbd2 Bd7 13. Nf1 Rfe8 14. Ne3 g6 
******C98: Ruy Lopez, closed, Chigorin, 12...Nc6
Ruy Lopez, closed, Chigorin, 12...Nc6
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Na5 10. Bc2 c5 11. d4 Qc7 12. Nbd2 Nc6 
Ruy Lopez, closed, Chigorin, Rauzer attack
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Na5 10. Bc2 c5 11. d4 Qc7 12. Nbd2 Nc6 13. dxc5
******C99: Ruy Lopez, closed, Chigorin, 12...c5d4
Ruy Lopez, closed, Chigorin, 12...c5d4
1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8. c3 d6 9. h3 Na5 10. Bc2 c5 11. d4 Qc7 12. Nbd2 cxd4 13. cxd4
******D00: Queen's pawn game
Queen's pawn game
1. d4 d5 
Queen's pawn, Mason variation
1. d4 d5 2. Bf4
Queen's pawn, Mason variation, Steinitz counter-gambit
1. d4 d5 2. Bf4 c5 
Levitsky attack (Queen's bishop attack)
1. d4 d5 2. Bg5
Blackmar gambit
1. d4 d5 2. e4
Queen's pawn, stonewall attack
1. d4 d5 2. e3 Nf6 3. Bd3
Queen's pawn, Chigorin variation
1. d4 d5 2. Nc3
Queen's pawn, Anti-Veresov
1. d4 d5 2. Nc3 Bg4 
Blackmar-Diemer gambit
1. d4 d5 2. Nc3 Nf6 3. e4
Blackmar-Diemer, Euwe defence
1. d4 d5 2. Nc3 Nf6 3. e4 dxe4 4. f3 exf3 5. Nxf3 e6 
Blackmar-Diemer, Lemberg counter-gambit
1. d4 d5 2. Nc3 Nf6 3. e4 e5 
******D01: Richter-Veresov attack
Richter-Veresov attack
1. d4 d5 2. Nc3 Nf6 3. Bg5
Richter-Veresov attack, Veresov variation
1. d4 d5 2. Nc3 Nf6 3. Bg5 Bf5 4. Bxf6
Richter-Veresov attack, Richter variation
1. d4 d5 2. Nc3 Nf6 3. Bg5 Bf5 4. f3
******D02: Queen's pawn game
Queen's pawn game
1. d4 d5 2. Nf3
Queen's pawn game, Chigorin variation
1. d4 d5 2. Nf3 Nc6 
Queen's pawn game, Krause variation
1. d4 d5 2. Nf3 c5 
Queen's pawn game
1. d4 d5 2. Nf3 Nf6 
Queen's bishop game
1. d4 d5 2. Nf3 Nf6 3. Bf4
******D03: Torre attack (Tartakower variation)
Torre attack (Tartakower variation)
1. d4 d5 2. Nf3 Nf6 3. Bg5
******D04: Queen's pawn game
Queen's pawn game
1. d4 d5 2. Nf3 Nf6 3. e3
******D05: Queen's pawn game
Queen's pawn game
1. d4 d5 2. Nf3 Nf6 3. e3 e6 
Queen's pawn game, Zukertort variation
1. d4 d5 2. Nf3 Nf6 3. e3 e6 4. Nbd2 c5 5. b3
Queen's pawn game
1. d4 d5 2. Nf3 Nf6 3. e3 e6 4. Bd3
Queen's pawn game, Rubinstein (Colle-Zukertort) variation
1. d4 d5 2. Nf3 Nf6 3. e3 e6 4. Bd3 c5 5. b3
Colle system
1. d4 d5 2. Nf3 Nf6 3. e3 e6 4. Bd3 c5 5. c3
******D06: Queen's Gambit
Queen's Gambit
1. d4 d5 2. c4
Queen's Gambit Declined, Grau (Sahovic) defence
1. d4 d5 2. c4 Bf5 
Queen's Gambit Declined, Marshall defence
1. d4 d5 2. c4 Nf6 
Queen's Gambit Declined, symmetrical (Austrian) defence
1. d4 d5 2. c4 c5 
******D07: Queen's Gambit Declined, Chigorin defence
Queen's Gambit Declined, Chigorin defence
1. d4 d5 2. c4 Nc6 
Queen's Gambit Declined, Chigorin defence, Janowski variation
1. d4 d5 2. c4 Nc6 3. Nc3 dxc4 4. Nf3
******D08: Queen's Gambit Declined, Albin counter-gambit
Queen's Gambit Declined, Albin counter-gambit
1. d4 d5 2. c4 e5 
Queen's Gambit Declined, Albin counter-gambit, Lasker trap
1. d4 d5 2. c4 e5 3. dxe5 d4 4. e3 Bb4+ 5. Bd2 dxe3 
Queen's Gambit Declined, Albin counter-gambit
1. d4 d5 2. c4 e5 3. dxe5 d4 4. Nf3
Queen's Gambit Declined, Albin counter-gambit, Alapin variation
1. d4 d5 2. c4 e5 3. dxe5 d4 4. Nf3 Nc6 5. Nbd2
Queen's Gambit Declined, Albin counter-gambit, Krenosz variation
1. d4 d5 2. c4 e5 3. dxe5 d4 4. Nf3 Nc6 5. Nbd2 Bg4 6. h3 Bxf3 7. Nxf3 Bb4+ 8. Bd2 Qe7 
Queen's Gambit Declined, Albin counter-gambit, Janowski variation
1. d4 d5 2. c4 e5 3. dxe5 d4 4. Nf3 Nc6 5. Nbd2 f6 
Queen's Gambit Declined, Albin counter-gambit, Balogh variation
1. d4 d5 2. c4 e5 3. dxe5 d4 4. Nf3 Nc6 5. Nbd2 Qe7 
******D09: Queen's Gambit Declined, Albin counter-gambit, 5.g3
Queen's Gambit Declined, Albin counter-gambit, 5.g3
1. d4 d5 2. c4 e5 3. dxe5 d4 4. Nf3 Nc6 5. g3
******D10: Queen's Gambit Declined Slav defence
Queen's Gambit Declined Slav defence
1. d4 d5 2. c4 c6 
Queen's Gambit Declined Slav defence, Alekhine variation
1. d4 d5 2. c4 c6 3. Nc3 dxc4 4. e4
Queen's Gambit Declined Slav, Winawer counter-gambit
1. d4 d5 2. c4 c6 3. Nc3 e5 
Queen's Gambit Declined Slav defence, exchange variation
1. d4 d5 2. c4 c6 3. cxd5
******D11: Queen's Gambit Declined Slav, 3.Nf3
Queen's Gambit Declined Slav, 3.Nf3
1. d4 d5 2. c4 c6 3. Nf3
Queen's Gambit Declined Slav, Breyer variation
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nbd2
Queen's Gambit Declined Slav, 4.e3
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. e3
******D12: Queen's Gambit Declined Slav, 4.e3 Bf5
Queen's Gambit Declined Slav, 4.e3 Bf5
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. e3 Bf5 
Queen's Gambit Declined Slav, Landau variation
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. e3 Bf5 5. cxd5 cxd5 6. Qb3 Qc8 7. Bd2 e6 8. Na3
Queen's Gambit Declined Slav, exchange variation
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. e3 Bf5 5. cxd5 cxd5 6. Nc3
Queen's Gambit Declined Slav, Amsterdam variation
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. e3 Bf5 5. cxd5 cxd5 6. Nc3 e6 7. Ne5 Nfd7 
******D13: Queen's Gambit Declined Slav, exchange variation
Queen's Gambit Declined Slav, exchange variation
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. cxd5 cxd5 
******D14: Queen's Gambit Declined Slav, exchange variation, 6.Bf4 Bf5
Queen's Gambit Declined Slav, exchange variation, 6.Bf4 Bf5
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. cxd5 cxd5 5. Nc3 Nc6 6. Bf4 Bf5 
Queen's Gambit Declined Slav, exchange, Trifunovic variation
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. cxd5 cxd5 5. Nc3 Nc6 6. Bf4 Bf5 7. e3 e6 8. Qb3 Bb4 
******D15: Queen's Gambit Declined Slav, 4.Nc3
Queen's Gambit Declined Slav, 4.Nc3
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3
Queen's Gambit Declined Slav, Suechting variation
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 Qb6 
Queen's Gambit Declined Slav, Schlechter variation
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 g6 
Queen's Gambit Declined Slav accepted
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 
Queen's Gambit Declined Slav, 5.e3 (Alekhine variation)
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. e3
Queen's Gambit Declined Slav, Slav gambit
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. e4
Queen's Gambit Declined Slav, Tolush-Geller gambit
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. e4 b5 6. e5
******D16: Queen's Gambit Declined Slav accepted, Alapin variation
Queen's Gambit Declined Slav accepted, Alapin variation
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. a4
Queen's Gambit Declined Slav, Smyslov variation
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. a4 Na6 6. e4 Bg4 
Queen's Gambit Declined Slav, Soultanbeieff variation
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. a4 e6 
Queen's Gambit Declined Slav, Steiner variation
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. a4 Bg4 
******D17: Queen's Gambit Declined Slav, Czech defence
Queen's Gambit Declined Slav, Czech defence
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. a4 Bf5 
Queen's Gambit Declined Slav, Krause attack
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. a4 Bf5 6. Ne5
Queen's Gambit Declined Slav, Carlsbad variation
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. a4 Bf5 6. Ne5 Nbd7 7. Nxc4 Qc7 8. g3 e5 
Queen's Gambit Declined Slav, Wiesbaden variation
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. a4 Bf5 6. Ne5 e6 
******D18: Queen's Gambit Declined Slav, Dutch variation
Queen's Gambit Declined Slav, Dutch variation
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. a4 Bf5 6. e3
Queen's Gambit Declined Slav, Dutch, Lasker variation
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. a4 Bf5 6. e3 Na6 
******D19: Queen's Gambit Declined Slav, Dutch variation
Queen's Gambit Declined Slav, Dutch variation
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. a4 Bf5 6. e3 e6 7. Bxc4 Bb4 8. O-O
Queen's Gambit Declined Slav, Dutch variation, main line
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. a4 Bf5 6. e3 e6 7. Bxc4 Bb4 8. O-O O-O 9. Qe2
Queen's Gambit Declined Slav, Dutch, Saemisch variation
1. d4 d5 2. c4 c6 3. Nf3 Nf6 4. Nc3 dxc4 5. a4 Bf5 6. e3 e6 7. Bxc4 Bb4 8. O-O O-O 9. Qe2 Ne4 10. g4
******D20: Queen's gambit accepted
Queen's gambit accepted
1. d4 d5 2. c4 dxc4 
Queen's Gambit Accepted, 3.e4
1. d4 d5 2. c4 dxc4 3. e4
Queen's Gambit Accepted, Linares variation
1. d4 d5 2. c4 dxc4 3. e4 c5 4. d5 Nf6 5. Nc3 b5 
Queen's Gambit Accepted, Schwartz defence
1. d4 d5 2. c4 dxc4 3. e4 f5 
******D21: Queen's Gambit Accepted, 3.Nf3
Queen's Gambit Accepted, 3.Nf3
1. d4 d5 2. c4 dxc4 3. Nf3
Queen's Gambit Accepted, Ericson variation
1. d4 d5 2. c4 dxc4 3. Nf3 b5 
Queen's Gambit Accepted, Alekhine defense, Borisenko-Furman variation
1. d4 d5 2. c4 dxc4 3. Nf3 a6 4. e4
******D22: Queen's Gambit Accepted, Alekhine defence
Queen's Gambit Accepted, Alekhine defence
1. d4 d5 2. c4 dxc4 3. Nf3 a6 
Queen's Gambit Accepted, Alekhine defence, Alatortsev variation
1. d4 d5 2. c4 dxc4 3. Nf3 a6 4. e3 Bg4 5. Bxc4 e6 6. d5
Queen's Gambit Accepted, Haberditz variation
1. d4 d5 2. c4 dxc4 3. Nf3 a6 4. e3 b5 
******D23: Queen's gambit accepted
Queen's gambit accepted
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 
Queen's Gambit Accepted, Mannheim variation
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. Qa4+
******D24: Queen's Gambit Accepted, 4.Nc3
Queen's Gambit Accepted, 4.Nc3
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. Nc3
Queen's Gambit Accepted, Bogolyubov variation
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. Nc3 a6 5. e4
******D25: Queen's Gambit Accepted, 4.e3
Queen's Gambit Accepted, 4.e3
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3
Queen's Gambit Accepted, Smyslov variation
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 g6 
Queen's Gambit Accepted, Janowsky-Larsen variation
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 Bg4 
Queen's Gambit Accepted, Flohr variation
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 Be6 
******D26: Queen's Gambit Accepted, 4...e6
Queen's Gambit Accepted, 4...e6
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 e6 
Queen's Gambit Accepted, classical variation
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 e6 5. Bxc4 c5 
Queen's Gambit Accepted, classical, Furman variation
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 e6 5. Bxc4 c5 6. Qe2 a6 7. dxc5 Bxc5 8. O-O Nc6 9. e4 b5 10. e5
Queen's Gambit Accepted, classical variation, 6.O-O
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 e6 5. Bxc4 c5 6. O-O
Queen's Gambit Accepted, classical, Steinitz variation
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 e6 5. Bxc4 c5 6. O-O cxd4 
******D27: Queen's Gambit Accepted, classical, 6...a6
Queen's Gambit Accepted, classical, 6...a6
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 e6 5. Bxc4 c5 6. O-O a6 
Queen's Gambit Accepted, classical, Rubinstein variation
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 e6 5. Bxc4 c5 6. O-O a6 7. a4
Queen's Gambit Accepted, classical, Geller variation
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 e6 5. Bxc4 c5 6. O-O a6 7. e4
******D28: Queen's Gambit Accepted, classical, 7.Qe2
Queen's Gambit Accepted, classical, 7.Qe2
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 e6 5. Bxc4 c5 6. O-O a6 7. Qe2
Queen's Gambit Accepted, classical, 7...b5
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 e6 5. Bxc4 c5 6. O-O a6 7. Qe2 b5 
Queen's Gambit Accepted, classical, Flohr variation
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 e6 5. Bxc4 c5 6. O-O a6 7. Qe2 b5 8. Bb3 Nc6 9. Rd1 c4 10. Bc2 Nb4 11. Nc3 Nxc2 12. Qxc2 Bb7 13. d5 Qc7 
******D29: Queen's Gambit Accepted, classical, 8...Bb7
Queen's Gambit Accepted, classical, 8...Bb7
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 e6 5. Bxc4 c5 6. O-O a6 7. Qe2 b5 8. Bb3 Bb7 
Queen's Gambit Accepted, classical, Smyslov variation
1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 e6 5. Bxc4 c5 6. O-O a6 7. Qe2 b5 8. Bb3 Bb7 9. Rd1 Nbd7 10. Nc3 Bd6 
******D30: Queen's gambit declined
Queen's gambit declined
1. d4 d5 2. c4 e6 
Queen's Gambit Declined Slav
1. d4 d5 2. c4 e6 3. Nf3 Nf6 4. e3 c6 5. Nbd2
Queen's Gambit Declined, Stonewall variation
1. d4 d5 2. c4 e6 3. Nf3 Nf6 4. e3 c6 5. Nbd2 Ne4 6. Bd3 f5 
Queen's Gambit Declined Slav
1. d4 d5 2. c4 e6 3. Nf3 Nf6 4. e3 c6 5. Nbd2 Nbd7 
Queen's Gambit Declined Slav, Semmering variation
1. d4 d5 2. c4 e6 3. Nf3 Nf6 4. e3 c6 5. Nbd2 Nbd7 6. Bd3 c5 
Queen's Gambit Declined, Spielmann variation
1. d4 d5 2. c4 e6 3. Nf3 Nf6 4. e3 c6 5. Nbd2 g6 
Queen's Gambit Declined
1. d4 d5 2. c4 e6 3. Nf3 Nf6 4. Bg5
Queen's Gambit Declined, Capablanca variation
1. d4 d5 2. c4 e6 3. Nf3 Nf6 4. Bg5 Nbd7 5. e3 c6 6. Nbd2
Queen's Gambit Declined, Vienna variation
1. d4 d5 2. c4 e6 3. Nf3 Nf6 4. Bg5 Bb4+ 
Queen's Gambit Declined, Capablanca-Duras variation
1. d4 d5 2. c4 e6 3. Nf3 Nf6 4. Bg5 h6 
Queen's Gambit Declined, Hastings variation
1. d4 d5 2. c4 e6 3. Nf3 Nf6 4. Bg5 h6 5. Bxf6 Qxf6 6. Nc3 c6 7. Qb3
******D31: Queen's Gambit Declined, 3.Nc3
Queen's Gambit Declined, 3.Nc3
1. d4 d5 2. c4 e6 3. Nc3
Queen's Gambit Declined, Janowski variation
1. d4 d5 2. c4 e6 3. Nc3 a6 
Queen's Gambit Declined, Alapin variation
1. d4 d5 2. c4 e6 3. Nc3 b6 
Queen's Gambit Declined, Charousek (Petrosian) variation
1. d4 d5 2. c4 e6 3. Nc3 Be7 
Queen's Gambit Declined, semi-Slav
1. d4 d5 2. c4 e6 3. Nc3 c6 
Queen's Gambit Declined, semi-Slav, Noteboom variation
1. d4 d5 2. c4 e6 3. Nc3 c6 4. Nf3 dxc4 
Queen's Gambit Declined, semi-Slav, Koomen variation
1. d4 d5 2. c4 e6 3. Nc3 c6 4. Nf3 dxc4 5. a4 Bb4 6. e3 b5 7. Bd2 Qe7 
Queen's Gambit Declined, semi-Slav, Junge variation
1. d4 d5 2. c4 e6 3. Nc3 c6 4. Nf3 dxc4 5. a4 Bb4 6. e3 b5 7. Bd2 Qb6 
Queen's Gambit Declined, semi-Slav, Abrahams variation
1. d4 d5 2. c4 e6 3. Nc3 c6 4. Nf3 dxc4 5. a4 Bb4 6. e3 b5 7. Bd2 a5 
Queen's Gambit Declined, semi-Slav, Marshall gambit
1. d4 d5 2. c4 e6 3. Nc3 c6 4. e4
******D32: Queen's Gambit Declined, Tarrasch defence
Queen's Gambit Declined, Tarrasch defence
1. d4 d5 2. c4 e6 3. Nc3 c5 
Queen's Gambit Declined, Tarrasch, von Hennig-Schara gambit
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 cxd4 
Queen's Gambit Declined, Tarrasch defence, 4.cd ed
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 
Queen's Gambit Declined, Tarrasch defence, Tarrasch gambit
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. dxc5 d4 6. Na4 b5 
Queen's Gambit Declined, Tarrasch defence, Marshall gambit
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. e4
Queen's Gambit Declined, Tarrasch defence
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. Nf3
******D33: Queen's Gambit Declined, Tarrasch, Schlechter-Rubinstein system
Queen's Gambit Declined, Tarrasch, Schlechter-Rubinstein system
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. Nf3 Nc6 6. g3
Queen's Gambit Declined, Tarrasch, Folkestone (Swedish) variation
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. Nf3 Nc6 6. g3 c4 
Queen's Gambit Declined, Tarrasch, Schlechter-Rubinstein system, Rey Ardid variation
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. Nf3 Nc6 6. g3 c4 7. e4
Queen's Gambit Declined, Tarrasch, Prague variation
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. Nf3 Nc6 6. g3 Nf6 
Queen's Gambit Declined, Tarrasch, Wagner variation
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. Nf3 Nc6 6. g3 Nf6 7. Bg2 Bg4 
******D34: Queen's Gambit Declined, Tarrasch, Prague variation, 7...Be7
Queen's Gambit Declined, Tarrasch, Prague variation, 7...Be7
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. Nf3 Nc6 6. g3 Nf6 7. Bg2 Be7 
Queen's Gambit Declined, Tarrasch, Prague variation, Normal position
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. Nf3 Nc6 6. g3 Nf6 7. Bg2 Be7 8. O-O O-O 
Queen's Gambit Declined, Tarrasch, Reti variation
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. Nf3 Nc6 6. g3 Nf6 7. Bg2 Be7 8. O-O O-O 9. dxc5 Bxc5 10. Na4
Queen's Gambit Declined, Tarrasch, Prague variation, 9.Bg5
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. Nf3 Nc6 6. g3 Nf6 7. Bg2 Be7 8. O-O O-O 9. Bg5
Queen's Gambit Declined, Tarrasch, Bogolyubov variation
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. Nf3 Nc6 6. g3 Nf6 7. Bg2 Be7 8. O-O O-O 9. Bg5 Be6 10. Rc1 c4 
Queen's Gambit Declined, Tarrasch, Stoltz variation
1. d4 d5 2. c4 e6 3. Nc3 c5 4. cxd5 exd5 5. Nf3 Nc6 6. g3 Nf6 7. Bg2 Be7 8. O-O O-O 9. Bg5 Be6 10. Rc1 b6 
******D35: Queen's Gambit Declined, 3...Nf6
Queen's Gambit Declined, 3...Nf6
1. d4 d5 2. c4 e6 3. Nc3 Nf6 
Queen's Gambit Declined, Harrwitz attack
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bf4
Queen's Gambit Declined, exchange variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. cxd5
Queen's Gambit Declined, exchange, Saemisch variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. cxd5 exd5 5. Nf3 Nbd7 6. Bf4
Queen's Gambit Declined, exchange, positional line
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. cxd5 exd5 5. Bg5
Queen's Gambit Declined, exchange, chameleon variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. cxd5 exd5 5. Bg5 Be7 6. e3 O-O 7. Bd3 Nbd7 8. Qc2 Re8 9. Nge2 Nf8 10. O-O-O
Queen's Gambit Declined, exchange, positional line, 5...c6
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. cxd5 exd5 5. Bg5 c6 
******D36: Queen's Gambit Declined, exchange, positional line, 6.Qc2
Queen's Gambit Declined, exchange, positional line, 6.Qc2
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. cxd5 exd5 5. Bg5 c6 6. Qc2
******D37: Queen's Gambit Declined, 4.Nf3
Queen's Gambit Declined, 4.Nf3
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3
Queen's Gambit Declined, classical variation (5.Bf4)
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 Be7 5. Bf4
******D38: Queen's Gambit Declined, Ragozin variation
Queen's Gambit Declined, Ragozin variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 Bb4 
******D39: Queen's Gambit Declined, Ragozin, Vienna variation
Queen's Gambit Declined, Ragozin, Vienna variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 Bb4 5. Bg5 dxc4 
******D40: Queen's Gambit Declined, Semi-Tarrasch defence
Queen's Gambit Declined, Semi-Tarrasch defence
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c5 
Queen's Gambit Declined, Semi-Tarrasch, symmetrical variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c5 5. e3 Nc6 6. Bd3 Bd6 7. O-O O-O 
Queen's Gambit Declined, Semi-Tarrasch, Levenfish variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c5 5. e3 Nc6 6. Bd3 Bd6 7. O-O O-O 8. Qe2 Qe7 9. dxc5 Bxc5 10. e4
Queen's Gambit Declined, Semi-Tarrasch defence, Pillsbury variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c5 5. Bg5
******D41: Queen's Gambit Declined, Semi-Tarrasch, 5.cd
Queen's Gambit Declined, Semi-Tarrasch, 5.cd
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c5 5. cxd5
Queen's Gambit Declined, Semi-Tarrasch, Kmoch variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c5 5. cxd5 Nxd5 6. e4 Nxc3 7. bxc3 cxd4 8. cxd4 Bb4+ 9. Bd2 Bxd2+ 10. Qxd2 O-O 11. Bb5
Queen's Gambit Declined, Semi-Tarrasch, San Sebastian variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c5 5. cxd5 Nxd5 6. e4 Nxc3 7. bxc3 cxd4 8. cxd4 Bb4+ 9. Bd2 Qa5 
Queen's Gambit Declined, Semi-Tarrasch with e3
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c5 5. cxd5 Nxd5 6. e3
******D42: Queen's Gambit Declined, Semi-Tarrasch, 7.Bd3
Queen's Gambit Declined, Semi-Tarrasch, 7.Bd3
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c5 5. cxd5 Nxd5 6. e3 Nc6 7. Bd3
******D43: Queen's Gambit Declined semi-Slav
Queen's Gambit Declined semi-Slav
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 
Queen's Gambit Declined semi-Slav, Hastings variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. Bg5 h6 6. Bxf6 Qxf6 7. Qb3
******D44: Queen's Gambit Declined semi-Slav, 5.Bg5 dc
Queen's Gambit Declined semi-Slav, 5.Bg5 dc
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. Bg5 dxc4 
Queen's Gambit Declined semi-Slav, Botvinnik system (anti-Meran)
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. Bg5 dxc4 6. e4
Queen's Gambit Declined semi-Slav, Ekstrom variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. Bg5 dxc4 6. e4 b5 7. e5 h6 8. Bh4 g5 9. exf6 gxh4 10. Ne5
Queen's Gambit Declined semi-Slav, anti-Meran gambit
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. Bg5 dxc4 6. e4 b5 7. e5 h6 8. Bh4 g5 9. Nxg5
Queen's Gambit Declined semi-Slav, anti-Meran, Lilienthal variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. Bg5 dxc4 6. e4 b5 7. e5 h6 8. Bh4 g5 9. Nxg5 hxg5 10. Bxg5 Nbd7 11. g3
Queen's Gambit Declined semi-Slav, anti-Meran, Szabo variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. Bg5 dxc4 6. e4 b5 7. e5 h6 8. Bh4 g5 9. Nxg5 hxg5 10. Bxg5 Nbd7 11. Qf3
Queen's Gambit Declined semi-Slav, anti-Meran, Alatortsev system
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. Bg5 dxc4 6. e4 b5 7. e5 h6 8. Bh4 g5 9. Nxg5 Nd5 
******D45: Queen's Gambit Declined semi-Slav, 5.e3
Queen's Gambit Declined semi-Slav, 5.e3
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3
Queen's Gambit Declined semi-Slav, stonewall defence
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Ne4 6. Bd3 f5 
Queen's Gambit Declined semi-Slav, accelerated Meran (Alekhine variation)
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 a6 
Queen's Gambit Declined semi-Slav, 5...Nd7
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 
Queen's Gambit Declined semi-Slav, Stoltz variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Qc2
Queen's Gambit Declined semi-Slav, Rubinstein (anti-Meran) system
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Ne5
******D46: Queen's Gambit Declined semi-Slav, 6.Bd3
Queen's Gambit Declined semi-Slav, 6.Bd3
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3
Queen's Gambit Declined semi-Slav, Bogolyubov variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 Be7 
Queen's Gambit Declined semi-Slav, Romih variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 Bb4 
Queen's Gambit Declined semi-Slav, Chigorin defence
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 Bd6 
******D47: Queen's Gambit Declined semi-Slav, 7.Bc4
Queen's Gambit Declined semi-Slav, 7.Bc4
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4
Queen's Gambit Declined semi-Slav, Meran variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 
Queen's Gambit Declined semi-Slav, neo-Meran (Lundin variation)
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 8. Bd3 b4 
Queen's Gambit Declined semi-Slav, Meran, Wade variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 8. Bd3 Bb7 
******D48: Queen's Gambit Declined semi-Slav, Meran, 8...a6
Queen's Gambit Declined semi-Slav, Meran, 8...a6
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 8. Bd3 a6 
Queen's Gambit Declined semi-Slav, Meran, Pirc variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 8. Bd3 a6 9. e4 b4 
Queen's Gambit Declined semi-Slav, Meran
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 8. Bd3 a6 9. e4 c5 
Queen's Gambit Declined semi-Slav, Meran, Reynolds' variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 8. Bd3 a6 9. e4 c5 10. d5
Queen's Gambit Declined semi-Slav, Meran, old main line
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 8. Bd3 a6 9. e4 c5 10. e5
******D49: Queen's Gambit Declined semi-Slav, Meran, Blumenfeld variation
Queen's Gambit Declined semi-Slav, Meran, Blumenfeld variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 8. Bd3 a6 9. e4 c5 10. e5 cxd4 11. Nxb5
Queen's Gambit Declined semi-Slav, Meran, Rabinovich variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 8. Bd3 a6 9. e4 c5 10. e5 cxd4 11. Nxb5 Ng4 
Queen's Gambit Declined semi-Slav, Meran, Sozin variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 8. Bd3 a6 9. e4 c5 10. e5 cxd4 11. Nxb5 Nxe5 
Queen's Gambit Declined semi-Slav, Meran, Stahlberg variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 8. Bd3 a6 9. e4 c5 10. e5 cxd4 11. Nxb5 Nxe5 12. Nxe5 axb5 13. Qf3
Queen's Gambit Declined semi-Slav, Meran, Sozin variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 8. Bd3 a6 9. e4 c5 10. e5 cxd4 11. Nxb5 Nxe5 12. Nxe5 axb5 13. O-O
Queen's Gambit Declined semi-Slav, Meran, Rellstab attack
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Nf3 c6 5. e3 Nbd7 6. Bd3 dxc4 7. Bxc4 b5 8. Bd3 a6 9. e4 c5 10. e5 cxd4 11. Nxb5 Nxe5 12. Nxe5 axb5 13. O-O Qd5 14. Qe2 Ba6 15. Bg5
******D50: Queen's Gambit Declined, 4.Bg5
Queen's Gambit Declined, 4.Bg5
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5
Queen's Gambit Declined, Been-Koomen variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 c5 
Queen's Gambit Declined, Semi-Tarrasch, Krause variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 c5 5. Nf3 cxd4 6. Nxd4 e5 7. Ndb5 a6 8. Qa4
Queen's Gambit Declined, Semi-Tarrasch, Primitive Pillsbury variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 c5 5. Nf3 cxd4 6. Qxd4
Queen's Gambit Declined, Semi-Tarrasch
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 c5 5. cxd5
Queen's Gambit Declined, Canal (Venice) variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 c5 5. cxd5 Qb6 
******D51: Queen's Gambit Declined, 4.Bg5 Nbd7
Queen's Gambit Declined, 4.Bg5 Nbd7
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 
Queen's Gambit Declined, Rochlin variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. Nf3 c6 6. Rc1 Qa5 7. Bd2
Queen's Gambit Declined, Alekhine variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. Nf3 c6 6. e4
Queen's Gambit Declined
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. e3
Queen's Gambit Declined, Manhattan variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. e3 Bb4 
Queen's Gambit Declined, 5...c6
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. e3 c6 
Queen's Gambit Declined, Capablanca anti-Cambridge Springs variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. e3 c6 6. a3
******D52: Queen's Gambit Declined
Queen's Gambit Declined
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. e3 c6 6. Nf3
Queen's Gambit Declined, Cambridge Springs defence
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. e3 c6 6. Nf3 Qa5 
Queen's Gambit Declined, Cambridge Springs defence, Bogoljubow variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. e3 c6 6. Nf3 Qa5 7. Nd2 Bb4 8. Qc2
Queen's Gambit Declined, Cambridge Springs defence, Argentine variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. e3 c6 6. Nf3 Qa5 7. Nd2 Bb4 8. Qc2 O-O 9. Bh4
Queen's Gambit Declined, Cambridge Springs defence, Rubinstein variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. e3 c6 6. Nf3 Qa5 7. Nd2 dxc4 
Queen's Gambit Declined, Cambridge Springs defence, Capablanca variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. e3 c6 6. Nf3 Qa5 7. Bxf6
Queen's Gambit Declined, Cambridge Springs defence, 7.cd
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. e3 c6 6. Nf3 Qa5 7. cxd5
Queen's Gambit Declined, Cambridge Springs defence, Yugoslav variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Nbd7 5. e3 c6 6. Nf3 Qa5 7. cxd5 Nxd5 
******D53: Queen's Gambit Declined, 4.Bg5 Be7
Queen's Gambit Declined, 4.Bg5 Be7
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 
Queen's Gambit Declined, Lasker variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 Ne4 
Queen's Gambit Declined, 4.Bg5 Be7, 5.e3 O-O
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 
******D54: Queen's Gambit Declined, Anti-neo-orthodox variation
Queen's Gambit Declined, Anti-neo-orthodox variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Rc1
******D55: Queen's Gambit Declined, 6.Nf3
Queen's Gambit Declined, 6.Nf3
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3
Queen's Gambit Declined, Pillsbury attack
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 b6 7. Bd3 Bb7 8. cxd5 exd5 9. Ne5
Queen's Gambit Declined, Neo-orthodox variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 h6 
Queen's Gambit Declined, Neo-orthodox variation, 7.Bxf6
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 h6 7. Bxf6
Queen's Gambit Declined, Petrosian variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 h6 7. Bxf6 Bxf6 8. Rc1 c6 9. Bd3 Nd7 10. O-O dxc4 11. Bxc4
Queen's Gambit Declined, Neo-orthodox variation, 7.Bh4
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 h6 7. Bh4
******D56: Queen's Gambit Declined, Lasker defence
Queen's Gambit Declined, Lasker defence
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 h6 7. Bh4 Ne4 
Queen's Gambit Declined, Lasker defence, Teichmann variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 h6 7. Bh4 Ne4 8. Bxe7 Qxe7 9. Qc2
Queen's Gambit Declined, Lasker defence, Russian variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 h6 7. Bh4 Ne4 8. Bxe7 Qxe7 9. Qc2 Nf6 10. Bd3 dxc4 11. Bxc4 c5 12. O-O Nc6 13. Rfd1 Bd7 
******D57: Queen's Gambit Declined, Lasker defence, main line
Queen's Gambit Declined, Lasker defence, main line
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 h6 7. Bh4 Ne4 8. Bxe7 Qxe7 9. cxd5 Nxc3 10. bxc3
Queen's Gambit Declined, Lasker defence, Bernstein variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 h6 7. Bh4 Ne4 8. Bxe7 Qxe7 9. cxd5 Nxc3 10. bxc3 exd5 11. Qb3 Qd6 
******D58: Queen's Gambit Declined, Tartakower (Makagonov-Bondarevsky) system
Queen's Gambit Declined, Tartakower (Makagonov-Bondarevsky) system
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 h6 7. Bh4 b6 
******D59: Queen's Gambit Declined, Tartakower (Makagonov-Bondarevsky) system, 8.cd Nxd5
Queen's Gambit Declined, Tartakower (Makagonov-Bondarevsky) system, 8.cd Nxd5
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 h6 7. Bh4 b6 8. cxd5 Nxd5 
Queen's Gambit Declined, Tartakower variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 h6 7. Bh4 b6 8. cxd5 Nxd5 9. Bxe7 Qxe7 10. Nxd5 exd5 11. Rc1 Be6 
******D60: Queen's Gambit Declined, Orthodox defence
Queen's Gambit Declined, Orthodox defence
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 
Queen's Gambit Declined, Orthodox defence, Botvinnik variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Bd3
Queen's Gambit Declined, Orthodox defence, Rauzer variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Qb3
******D61: Queen's Gambit Declined, Orthodox defence, Rubinstein variation
Queen's Gambit Declined, Orthodox defence, Rubinstein variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Qc2
******D62: Queen's Gambit Declined, Orthodox defence, 7.Qc2 c5, 8.cd (Rubinstein)
Queen's Gambit Declined, Orthodox defence, 7.Qc2 c5, 8.cd (Rubinstein)
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Qc2 c5 8. cxd5
******D63: Queen's Gambit Declined, Orthodox defence, 7.Rc1
Queen's Gambit Declined, Orthodox defence, 7.Rc1
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1
Queen's Gambit Declined, Orthodox defence, Pillsbury attack
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 b6 8. cxd5 exd5 9. Bd3
Queen's Gambit Declined, Orthodox defence, Capablanca variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 b6 8. cxd5 exd5 9. Bb5
Queen's Gambit Declined, Orthodox defence, Swiss (Henneberger) variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 a6 
Queen's Gambit Declined, Orthodox defence, Swiss, Karlsbad variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 a6 8. cxd5
Queen's Gambit Declined, Orthodox defence
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 
******D64: Queen's Gambit Declined, Orthodox defence, Rubinstein attack (with Rc1)
Queen's Gambit Declined, Orthodox defence, Rubinstein attack (with Rc1)
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Qc2
Queen's Gambit Declined, Orthodox defence, Rubinstein attack, Wolf variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Qc2 Ne4 
Queen's Gambit Declined, Orthodox defence, Rubinstein attack, Karlsbad variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Qc2 a6 
Queen's Gambit Declined, Orthodox defence, Rubinstein attack, Gruenfeld variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Qc2 a6 9. a3
******D65: Queen's Gambit Declined, Orthodox defence, Rubinstein attack, main line
Queen's Gambit Declined, Orthodox defence, Rubinstein attack, main line
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Qc2 a6 9. cxd5
******D66: Queen's Gambit Declined, Orthodox defence, Bd3 line
Queen's Gambit Declined, Orthodox defence, Bd3 line
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Bd3
Queen's Gambit Declined, Orthodox defence, Bd3 line, fianchetto variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Bd3 dxc4 9. Bxc4 b5 
******D67: Queen's Gambit Declined, Orthodox defence, Bd3 line, Capablanca freeing manoevre
Queen's Gambit Declined, Orthodox defence, Bd3 line, Capablanca freeing manoevre
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Bd3 dxc4 9. Bxc4 Nd5 
Queen's Gambit Declined, Orthodox defence, Bd3 line, Janowski variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Bd3 dxc4 9. Bxc4 Nd5 10. h4
Queen's Gambit Declined, Orthodox defence, Bd3 line
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Bd3 dxc4 9. Bxc4 Nd5 10. Bxe7 Qxe7 
Queen's Gambit Declined, Orthodox defence, Bd3 line, Alekhine variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Bd3 dxc4 9. Bxc4 Nd5 10. Bxe7 Qxe7 11. Ne4
Queen's Gambit Declined, Orthodox defence, Bd3 line, 11.O-O
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Bd3 dxc4 9. Bxc4 Nd5 10. Bxe7 Qxe7 11. O-O
******D68: Queen's Gambit Declined, Orthodox defence, classical variation
Queen's Gambit Declined, Orthodox defence, classical variation
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Bd3 dxc4 9. Bxc4 Nd5 10. Bxe7 Qxe7 11. O-O Nxc3 12. Rxc3 e5 
Queen's Gambit Declined, Orthodox defence, classical, 13.d1b1 (Maroczy)
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Bd3 dxc4 9. Bxc4 Nd5 10. Bxe7 Qxe7 11. O-O Nxc3 12. Rxc3 e5 13. Qb1
Queen's Gambit Declined, Orthodox defence, classical, 13.d1c2 (Vidmar)
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Bd3 dxc4 9. Bxc4 Nd5 10. Bxe7 Qxe7 11. O-O Nxc3 12. Rxc3 e5 13. Qc2
******D69: Queen's Gambit Declined, Orthodox defence, classical, 13.de
Queen's Gambit Declined, Orthodox defence, classical, 13.de
1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 Nbd7 7. Rc1 c6 8. Bd3 dxc4 9. Bxc4 Nd5 10. Bxe7 Qxe7 11. O-O Nxc3 12. Rxc3 e5 13. dxe5 Nxe5 14. Nxe5 Qxe5 
******D70: Neo-Gruenfeld defence
Neo-Gruenfeld defence
1. d4 Nf6 2. c4 g6 3. f3 d5 
Neo-Gruenfeld (Kemeri) defence
1. d4 Nf6 2. c4 g6 3. g3 d5 
******D71: Neo-Gruenfeld, 5.cd
Neo-Gruenfeld, 5.cd
1. d4 Nf6 2. c4 g6 3. g3 d5 4. Bg2 Bg7 5. cxd5 Nxd5 
******D72: Neo-Gruenfeld, 5.cd, main line
Neo-Gruenfeld, 5.cd, main line
1. d4 Nf6 2. c4 g6 3. g3 d5 4. Bg2 Bg7 5. cxd5 Nxd5 6. e4 Nb6 7. Ne2
******D73: Neo-Gruenfeld, 5.Nf3
Neo-Gruenfeld, 5.Nf3
1. d4 Nf6 2. c4 g6 3. g3 d5 4. Bg2 Bg7 5. Nf3
******D74: Neo-Gruenfeld, 6.cd Nxd5, 7.O-O
Neo-Gruenfeld, 6.cd Nxd5, 7.O-O
1. d4 Nf6 2. c4 g6 3. g3 d5 4. Bg2 Bg7 5. Nf3 O-O 6. cxd5 Nxd5 7. O-O
******D75: Neo-Gruenfeld, 6.cd Nxd5, 7.O-O c5, 8.Nc3
Neo-Gruenfeld, 6.cd Nxd5, 7.O-O c5, 8.Nc3
1. d4 Nf6 2. c4 g6 3. g3 d5 4. Bg2 Bg7 5. Nf3 O-O 6. cxd5 Nxd5 7. O-O c5 8. Nc3
Neo-Gruenfeld, 6.cd Nxd5, 7.O-O c5, 8.dc
1. d4 Nf6 2. c4 g6 3. g3 d5 4. Bg2 Bg7 5. Nf3 O-O 6. cxd5 Nxd5 7. O-O c5 8. dxc5
******D76: Neo-Gruenfeld, 6.cd Nxd5, 7.O-O Nb6
Neo-Gruenfeld, 6.cd Nxd5, 7.O-O Nb6
1. d4 Nf6 2. c4 g6 3. g3 d5 4. Bg2 Bg7 5. Nf3 O-O 6. cxd5 Nxd5 7. O-O Nb6 
******D77: Neo-Gruenfeld, 6.O-O
Neo-Gruenfeld, 6.O-O
1. d4 Nf6 2. c4 g6 3. g3 d5 4. Bg2 Bg7 5. Nf3 O-O 6. O-O
******D78: Neo-Gruenfeld, 6.O-O c6
Neo-Gruenfeld, 6.O-O c6
1. d4 Nf6 2. c4 g6 3. g3 d5 4. Bg2 Bg7 5. Nf3 O-O 6. O-O c6 
******D79: Neo-Gruenfeld, 6.O-O, main line
Neo-Gruenfeld, 6.O-O, main line
1. d4 Nf6 2. c4 g6 3. g3 d5 4. Bg2 Bg7 5. Nf3 O-O 6. O-O c6 7. cxd5 cxd5 
******D80: Gruenfeld defence
Gruenfeld defence
1. d4 Nf6 2. c4 g6 3. Nc3 d5 
Gruenfeld, Spike gambit
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. g4
Gruenfeld, Stockholm variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Bg5
Gruenfeld, Lundin variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Bg5 Ne4 5. Nxe4 dxe4 6. Qd2 c5 
******D81: Gruenfeld, Russian variation
Gruenfeld, Russian variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Qb3
******D82: Gruenfeld, 4.Bf4
Gruenfeld, 4.Bf4
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Bf4
******D83: Gruenfeld, Gruenfeld gambit
Gruenfeld, Gruenfeld gambit
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Bf4 Bg7 5. e3 O-O 
Gruenfeld, Gruenfeld gambit, Capablanca variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Bf4 Bg7 5. e3 O-O 6. Rc1
Gruenfeld, Gruenfeld gambit, Botvinnik variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Bf4 Bg7 5. e3 O-O 6. Rc1 c5 7. dxc5 Be6 
******D84: Gruenfeld, Gruenfeld gambit accepted
Gruenfeld, Gruenfeld gambit accepted
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Bf4 Bg7 5. e3 O-O 6. cxd5 Nxd5 7. Nxd5 Qxd5 8. Bxc7
******D85: Gruenfeld, exchange variation
Gruenfeld, exchange variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. cxd5 Nxd5 
Gruenfeld, modern exchange variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. cxd5 Nxd5 5. e4 Nxc3 6. bxc3 Bg7 7. Nf3
******D86: Gruenfeld, exchange, classical variation
Gruenfeld, exchange, classical variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. cxd5 Nxd5 5. e4 Nxc3 6. bxc3 Bg7 7. Bc4
Gruenfeld, exchange, Larsen variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. cxd5 Nxd5 5. e4 Nxc3 6. bxc3 Bg7 7. Bc4 O-O 8. Ne2 Qd7 9. O-O b6 
Gruenfeld, exchange, Simagin's lesser variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. cxd5 Nxd5 5. e4 Nxc3 6. bxc3 Bg7 7. Bc4 O-O 8. Ne2 b6 
Gruenfeld, exchange, Simagin's improved variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. cxd5 Nxd5 5. e4 Nxc3 6. bxc3 Bg7 7. Bc4 O-O 8. Ne2 Nc6 
******D87: Gruenfeld, exchange, Spassky variation
Gruenfeld, exchange, Spassky variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. cxd5 Nxd5 5. e4 Nxc3 6. bxc3 Bg7 7. Bc4 O-O 8. Ne2 c5 
Gruenfeld, exchange, Seville variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. cxd5 Nxd5 5. e4 Nxc3 6. bxc3 Bg7 7. Bc4 O-O 8. Ne2 c5 9. O-O Nc6 10. Be3 Bg4 11. f3 Na5 12. Bxf7+
******D88: Gruenfeld, Spassky variation, main line, 10...cd, 11.cd
Gruenfeld, Spassky variation, main line, 10...cd, 11.cd
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. cxd5 Nxd5 5. e4 Nxc3 6. bxc3 Bg7 7. Bc4 O-O 8. Ne2 c5 9. O-O Nc6 10. Be3 cxd4 11. cxd4
******D89: Gruenfeld, Spassky variation, main line, 13.Bd3
Gruenfeld, Spassky variation, main line, 13.Bd3
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. cxd5 Nxd5 5. e4 Nxc3 6. bxc3 Bg7 7. Bc4 O-O 8. Ne2 c5 9. O-O Nc6 10. Be3 cxd4 11. cxd4 Bg4 12. f3 Na5 13. Bd3 Be6 
Gruenfeld, exchange, Sokolsky variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. cxd5 Nxd5 5. e4 Nxc3 6. bxc3 Bg7 7. Bc4 O-O 8. Ne2 c5 9. O-O Nc6 10. Be3 cxd4 11. cxd4 Bg4 12. f3 Na5 13. Bd3 Be6 14. d5
******D90: Gruenfeld, Three knights variation
Gruenfeld, Three knights variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3
Gruenfeld, Schlechter variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 c6 
Gruenfeld, Three knights variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 
Gruenfeld, Flohr variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Qa4+
******D91: Gruenfeld, 5.Bg5
Gruenfeld, 5.Bg5
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Bg5
******D92: Gruenfeld, 5.Bf4
Gruenfeld, 5.Bf4
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Bf4
******D93: Gruenfeld with Bf4    e3
Gruenfeld with Bf4    e3
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Bf4 O-O 6. e3
******D94: Gruenfeld, 5.e3
Gruenfeld, 5.e3
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. e3
Gruenfeld, Makogonov variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. e3 O-O 6. b4
Gruenfeld, Opovcensky variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. e3 O-O 6. Bd2
Gruenfeld with e3    Bd3
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. e3 O-O 6. Bd3
Gruenfeld, Smyslov defence
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. e3 O-O 6. Bd3 c6 7. O-O Bg4 
Gruenfeld, Flohr defence
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. e3 O-O 6. Bd3 c6 7. O-O Bf5 
******D95: Gruenfeld with e3 & Qb3
Gruenfeld with e3 & Qb3
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. e3 O-O 6. Qb3
Gruenfeld, Botvinnik variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. e3 O-O 6. Qb3 e6 
Gruenfeld, Pachman variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. e3 O-O 6. Qb3 dxc4 7. Bxc4 Nbd7 8. Ng5
******D96: Gruenfeld, Russian variation
Gruenfeld, Russian variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Qb3
******D97: Gruenfeld, Russian variation with e4
Gruenfeld, Russian variation with e4
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Qb3 dxc4 6. Qxc4 O-O 7. e4
Gruenfeld, Russian, Alekhine (Hungarian) variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Qb3 dxc4 6. Qxc4 O-O 7. e4 a6 
Gruenfeld, Russian, Szabo (Boleslavsky) variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Qb3 dxc4 6. Qxc4 O-O 7. e4 c6 
Gruenfeld, Russian, Levenfish variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Qb3 dxc4 6. Qxc4 O-O 7. e4 b6 
Gruenfeld, Russian, Byrne (Simagin) variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Qb3 dxc4 6. Qxc4 O-O 7. e4 Nc6 
Gruenfeld, Russian, Prins variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Qb3 dxc4 6. Qxc4 O-O 7. e4 Na6 
******D98: Gruenfeld, Russian, Smyslov variation
Gruenfeld, Russian, Smyslov variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Qb3 dxc4 6. Qxc4 O-O 7. e4 Bg4 
Gruenfeld, Russian, Keres variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Qb3 dxc4 6. Qxc4 O-O 7. e4 Bg4 8. Be3 Nfd7 9. Be2 Nb6 10. Qd3 Nc6 11. O-O-O
******D99: Gruenfeld defence, Smyslov, main line
Gruenfeld defence, Smyslov, main line
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Qb3 dxc4 6. Qxc4 O-O 7. e4 Bg4 8. Be3 Nfd7 9. Qb3
Gruenfeld defence, Smyslov, Yugoslav variation
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. Qb3 dxc4 6. Qxc4 O-O 7. e4 Bg4 8. Be3 Nfd7 9. Qb3 c5 
******E00: Queen's pawn game
Queen's pawn game
1. d4 Nf6 2. c4 e6 
Neo-Indian (Seirawan) attack
1. d4 Nf6 2. c4 e6 3. Bg5
Catalan opening
1. d4 Nf6 2. c4 e6 3. g3
******E01: Catalan, closed
Catalan, closed
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2
******E02: Catalan, open, 5.Qa4
Catalan, open, 5.Qa4
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 dxc4 5. Qa4+
******E03: Catalan, open, Alekhine variation
Catalan, open, Alekhine variation
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 dxc4 5. Qa4+ Nbd7 6. Qxc4 a6 7. Qc2
Catalan, open, 5.Qa4 Nbd7, 6.Qxc4
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 dxc4 5. Qa4+ Nbd7 6. Qxc4
******E04: Catalan, open, 5.Nf3
Catalan, open, 5.Nf3
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 dxc4 5. Nf3
******E05: Catalan, open, classical line
Catalan, open, classical line
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 dxc4 5. Nf3 Be7 
******E06: Catalan, closed, 5.Nf3
Catalan, closed, 5.Nf3
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 Be7 5. Nf3
******E07: Catalan, closed, 6...Nbd7
Catalan, closed, 6...Nbd7
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 Be7 5. Nf3 O-O 6. O-O Nbd7 
Catalan, closed, Botvinnik variation
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 Be7 5. Nf3 O-O 6. O-O Nbd7 7. Nc3 c6 8. Qd3
******E08: Catalan, closed, 7.Qc2
Catalan, closed, 7.Qc2
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 Be7 5. Nf3 O-O 6. O-O Nbd7 7. Qc2
Catalan, closed, Zagoryansky variation
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 Be7 5. Nf3 O-O 6. O-O Nbd7 7. Qc2 c6 8. Rd1 b6 9. a4
Catalan, closed, Qc2 & b3
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 Be7 5. Nf3 O-O 6. O-O Nbd7 7. Qc2 c6 8. b3
Catalan, closed, Spassky gambit
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 Be7 5. Nf3 O-O 6. O-O Nbd7 7. Qc2 c6 8. b3 b6 9. Rd1 Bb7 10. Nc3 b5 
******E09: Catalan, closed, main line
Catalan, closed, main line
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 Be7 5. Nf3 O-O 6. O-O Nbd7 7. Qc2 c6 8. Nbd2
Catalan, closed, Sokolsky variation
1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 Be7 5. Nf3 O-O 6. O-O Nbd7 7. Qc2 c6 8. Nbd2 b6 9. b3 a5 10. Bb2 Ba6 
******E10: Queen's pawn game
Queen's pawn game
1. d4 Nf6 2. c4 e6 3. Nf3
Blumenfeld counter-gambit
1. d4 Nf6 2. c4 e6 3. Nf3 c5 4. d5 b5 
Blumenfeld counter-gambit accepted
1. d4 Nf6 2. c4 e6 3. Nf3 c5 4. d5 b5 5. dxe6 fxe6 6. cxb5 d5 
Blumenfeld counter-gambit, Dus-Chotimursky variation
1. d4 Nf6 2. c4 e6 3. Nf3 c5 4. d5 b5 5. Bg5
Blumenfeld counter-gambit, Spielmann variation
1. d4 Nf6 2. c4 e6 3. Nf3 c5 4. d5 b5 5. Bg5 exd5 6. cxd5 h6 
Dzindzikhashvili defence
1. d4 Nf6 2. c4 e6 3. Nf3 a6 
Doery defence
1. d4 Nf6 2. c4 e6 3. Nf3 Ne4 
******E11: Bogo-Indian defence
Bogo-Indian defence
1. d4 Nf6 2. c4 e6 3. Nf3 Bb4+ 
Bogo-Indian defence, Gruenfeld variation
1. d4 Nf6 2. c4 e6 3. Nf3 Bb4+ 4. Nbd2
Bogo-Indian defence, Nimzovich variation
1. d4 Nf6 2. c4 e6 3. Nf3 Bb4+ 4. Bd2 Qe7 
Bogo-Indian defence, Monticelli trap
1. d4 Nf6 2. c4 e6 3. Nf3 Bb4+ 4. Bd2 Bxd2+ 5. Qxd2 b6 6. g3 Bb7 7. Bg2 O-O 8. Nc3 Ne4 9. Qc2 Nxc3 10. Ng5
******E12: Queen's Indian defence
Queen's Indian defence
1. d4 Nf6 2. c4 e6 3. Nf3 b6 
Queen's Indian, Miles variation
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. Bf4
Queen's Indian, Petrosian system
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. a3
Queen's Indian, 4.Nc3
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. Nc3
Queen's Indian, 4.Nc3, Botvinnik variation
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. Nc3 Bb7 5. Bg5 h6 6. Bh4 g5 7. Bg3 Nh5 
******E13: Queen's Indian, 4.Nc3, main line
Queen's Indian, 4.Nc3, main line
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. Nc3 Bb7 5. Bg5 h6 6. Bh4 Bb4 
******E14: Queen's Indian, 4.e3
Queen's Indian, 4.e3
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. e3
Queen's Indian, Averbakh variation
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. e3 Bb7 5. Bd3 c5 6. O-O Be7 7. b3 O-O 8. Bb2 cxd4 9. Nxd4
******E15: Queen's Indian, 4.g3
Queen's Indian, 4.g3
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3
Queen's Indian, Nimzovich variation (exaggerated fianchetto)
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Ba6 
Queen's Indian, 4.g3 Bb7
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Bb7 
Queen's Indian, Rubinstein variation
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Bb7 5. Bg2 c5 6. d5 exd5 7. Nh4
Queen's Indian, Buerger variation
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Bb7 5. Bg2 c5 6. d5 exd5 7. Ng5
******E16: Queen's Indian, Capablanca variation
Queen's Indian, Capablanca variation
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Bb7 5. Bg2 Bb4+ 
Queen's Indian, Yates variation
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Bb7 5. Bg2 Bb4+ 6. Bd2 a5 
Queen's Indian, Riumin variation
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Bb7 5. Bg2 Bb4+ 6. Bd2 Be7 
******E17: Queen's Indian, 5.Bg2 Be7
Queen's Indian, 5.Bg2 Be7
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Bb7 5. Bg2 Be7 
Queen's Indian, anti-Queen's Indian system
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Bb7 5. Bg2 Be7 6. Nc3
Queen's Indian, Opovcensky variation
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Bb7 5. Bg2 Be7 6. Nc3 Ne4 7. Bd2
Queen's Indian, old main line, 6.O-O
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Bb7 5. Bg2 Be7 6. O-O
Queen's Indian, Euwe variation
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Bb7 5. Bg2 Be7 6. O-O O-O 7. b3
******E18: Queen's Indian, old main line, 7.Nc3
Queen's Indian, old main line, 7.Nc3
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Bb7 5. Bg2 Be7 6. O-O O-O 7. Nc3
******E19: Queen's Indian, old main line, 9.Qxc3
Queen's Indian, old main line, 9.Qxc3
1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 Bb7 5. Bg2 Be7 6. O-O O-O 7. Nc3 Ne4 8. Qc2 Nxc3 9. Qxc3
******E20: Nimzo-Indian defence
Nimzo-Indian defence
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 
Nimzo-Indian, Kmoch variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. f3
Nimzo-Indian, Mikenas attack
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qd3
Nimzo-Indian, Romanishin-Kasparov (Steiner) system
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. g3
******E21: Nimzo-Indian, three knights variation
Nimzo-Indian, three knights variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Nf3
Nimzo-Indian, three knights, Korchnoi variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Nf3 c5 5. d5
Nimzo-Indian, three knights, Euwe variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Nf3 c5 5. d5 Ne4 
******E22: Nimzo-Indian, Spielmann variation
Nimzo-Indian, Spielmann variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qb3
******E23: Nimzo-Indian, Spielmann, 4...c5, 5.dc Nc6
Nimzo-Indian, Spielmann, 4...c5, 5.dc Nc6
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qb3 c5 5. dxc5 Nc6 
Nimzo-Indian, Spielmann, Karlsbad variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qb3 c5 5. dxc5 Nc6 6. Nf3 Ne4 7. Bd2 Nxd2 
Nimzo-Indian, Spielmann, San Remo variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qb3 c5 5. dxc5 Nc6 6. Nf3 Ne4 7. Bd2 Nxc5 
Nimzo-Indian, Spielmann, Staahlberg variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qb3 c5 5. dxc5 Nc6 6. Nf3 Ne4 7. Bd2 Nxc5 8. Qc2 f5 9. g3
******E24: Nimzo-Indian, Saemisch variation
Nimzo-Indian, Saemisch variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. a3 Bxc3+ 5. bxc3
Nimzo-Indian, Saemisch, Botvinnik variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. a3 Bxc3+ 5. bxc3 c5 6. f3 d5 7. e3 O-O 8. cxd5 Nxd5 
******E25: Nimzo-Indian, Saemisch variation
Nimzo-Indian, Saemisch variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. a3 Bxc3+ 5. bxc3 c5 6. f3 d5 7. cxd5
Nimzo-Indian, Saemisch, Keres variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. a3 Bxc3+ 5. bxc3 c5 6. f3 d5 7. cxd5 Nxd5 8. dxc5
Nimzo-Indian, Saemisch, Romanovsky variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. a3 Bxc3+ 5. bxc3 c5 6. f3 d5 7. cxd5 Nxd5 8. dxc5 f5 
******E26: Nimzo-Indian, Saemisch variation
Nimzo-Indian, Saemisch variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. a3 Bxc3+ 5. bxc3 c5 6. e3
Nimzo-Indian, Saemisch, O'Kelly variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. a3 Bxc3+ 5. bxc3 c5 6. e3 b6 
******E27: Nimzo-Indian, Saemisch variation
Nimzo-Indian, Saemisch variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. a3 Bxc3+ 5. bxc3 O-O 
******E28: Nimzo-Indian, Saemisch variation
Nimzo-Indian, Saemisch variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. a3 Bxc3+ 5. bxc3 O-O 6. e3
******E29: Nimzo-Indian, Saemisch, main line
Nimzo-Indian, Saemisch, main line
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. a3 Bxc3+ 5. bxc3 O-O 6. e3 c5 7. Bd3 Nc6 
Nimzo-Indian, Saemisch, Capablanca variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. a3 Bxc3+ 5. bxc3 O-O 6. e3 c5 7. Bd3 Nc6 8. Ne2 b6 9. e4 Ne8 
******E30: Nimzo-Indian, Leningrad variation
Nimzo-Indian, Leningrad variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Bg5
Nimzo-Indian, Leningrad, ...b5 gambit
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Bg5 h6 5. Bh4 c5 6. d5 b5 
******E31: Nimzo-Indian, Leningrad, main line
Nimzo-Indian, Leningrad, main line
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Bg5 h6 5. Bh4 c5 6. d5 d6 
******E32: Nimzo-Indian, classical variation
Nimzo-Indian, classical variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2
Nimzo-Indian, classical, Adorjan gambit
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2 O-O 5. a3 Bxc3+ 6. Qxc3 b5 
******E33: Nimzo-Indian, classical, 4...Nc6
Nimzo-Indian, classical, 4...Nc6
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2 Nc6 
Nimzo-Indian, classical, Milner-Barry (Zurich) variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2 Nc6 5. Nf3 d6 
******E34: Nimzo-Indian, classical, Noa variation
Nimzo-Indian, classical, Noa variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2 d5 
******E35: Nimzo-Indian, classical, Noa variation, 5.cd ed
Nimzo-Indian, classical, Noa variation, 5.cd ed
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2 d5 5. cxd5 exd5 
******E36: Nimzo-Indian, classical, Noa variation, 5.a3
Nimzo-Indian, classical, Noa variation, 5.a3
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2 d5 5. a3
Nimzo-Indian, classical, Botvinnik variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2 d5 5. a3 Bxc3+ 6. Qxc3 Nc6 
Nimzo-Indian, classical, Noa variation, main line
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2 d5 5. a3 Bxc3+ 6. Qxc3 Ne4 
******E37: Nimzo-Indian, classical, Noa variation, main line, 7.Qc2
Nimzo-Indian, classical, Noa variation, main line, 7.Qc2
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2 d5 5. a3 Bxc3+ 6. Qxc3 Ne4 7. Qc2
Nimzo-Indian, classical, San Remo variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2 d5 5. a3 Bxc3+ 6. Qxc3 Ne4 7. Qc2 Nc6 8. e3 e5 
******E38: Nimzo-Indian, classical, 4...c5
Nimzo-Indian, classical, 4...c5
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2 c5 
******E39: Nimzo-Indian, classical, Pirc variation
Nimzo-Indian, classical, Pirc variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2 c5 5. dxc5 O-O 
******E40: Nimzo-Indian, 4.e3
Nimzo-Indian, 4.e3
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3
Nimzo-Indian, 4.e3, Taimanov variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 Nc6 
******E41: Nimzo-Indian, 4.e3 c5
Nimzo-Indian, 4.e3 c5
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 c5 
Nimzo-Indian, e3, Huebner variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 c5 5. Bd3 Nc6 6. Nf3 Bxc3+ 7. bxc3 d6 
******E42: Nimzo-Indian, 4.e3 c5, 5.Ne2 (Rubinstein)
Nimzo-Indian, 4.e3 c5, 5.Ne2 (Rubinstein)
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 c5 5. Nge2
******E43: Nimzo-Indian, Fischer variation
Nimzo-Indian, Fischer variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 b6 
******E44: Nimzo-Indian, Fischer variation, 5.Ne2
Nimzo-Indian, Fischer variation, 5.Ne2
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 b6 5. Nge2
******E45: Nimzo-Indian, 4.e3, Bronstein (Byrne) variation
Nimzo-Indian, 4.e3, Bronstein (Byrne) variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 b6 5. Nge2 Ba6 
******E46: Nimzo-Indian, 4.e3 O-O
Nimzo-Indian, 4.e3 O-O
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 
Nimzo-Indian, Reshevsky variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nge2
Nimzo-Indian, Simagin variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nge2 d5 6. a3 Bd6 
******E47: Nimzo-Indian, 4.e3 O-O, 5.Bd3
Nimzo-Indian, 4.e3 O-O, 5.Bd3
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Bd3
******E48: Nimzo-Indian, 4.e3 O-O, 5.Bd3 d5
Nimzo-Indian, 4.e3 O-O, 5.Bd3 d5
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Bd3 d5 
******E49: Nimzo-Indian, 4.e3, Botvinnik system
Nimzo-Indian, 4.e3, Botvinnik system
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Bd3 d5 6. a3 Bxc3+ 7. bxc3
******E50: Nimzo-Indian, 4.e3 e8g8, 5.Nf3, without ...d5
Nimzo-Indian, 4.e3 e8g8, 5.Nf3, without ...d5
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3
******E51: Nimzo-Indian, 4.e3 e8g8, 5.Nf3 d7d5
Nimzo-Indian, 4.e3 e8g8, 5.Nf3 d7d5
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3 d5 
Nimzo-Indian, 4.e3, Ragozin variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3 d5 6. Bd3 Nc6 7. O-O dxc4 
******E52: Nimzo-Indian, 4.e3, main line with ...b6
Nimzo-Indian, 4.e3, main line with ...b6
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3 d5 6. Bd3 b6 
******E53: Nimzo-Indian, 4.e3, main line with ...c5
Nimzo-Indian, 4.e3, main line with ...c5
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3 d5 6. Bd3 c5 
Nimzo-Indian, 4.e3, Keres variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3 d5 6. Bd3 c5 7. O-O b6 
Nimzo-Indian, 4.e3, Gligoric system with 7...Nbd7
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3 d5 6. Bd3 c5 7. O-O Nbd7 
******E54: Nimzo-Indian, 4.e3, Gligoric system with 7...dc
Nimzo-Indian, 4.e3, Gligoric system with 7...dc
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3 d5 6. Bd3 c5 7. O-O dxc4 8. Bxc4
Nimzo-Indian, 4.e3, Gligoric system, Smyslov variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3 d5 6. Bd3 c5 7. O-O dxc4 8. Bxc4 Qe7 
******E55: Nimzo-Indian, 4.e3, Gligoric system, Bronstein variation
Nimzo-Indian, 4.e3, Gligoric system, Bronstein variation
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3 d5 6. Bd3 c5 7. O-O dxc4 8. Bxc4 Nbd7 
******E56: Nimzo-Indian, 4.e3, main line with 7...Nc6
Nimzo-Indian, 4.e3, main line with 7...Nc6
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3 d5 6. Bd3 c5 7. O-O Nc6 
******E57: Nimzo-Indian, 4.e3, main line with 8...dc and 9...cd
Nimzo-Indian, 4.e3, main line with 8...dc and 9...cd
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3 d5 6. Bd3 c5 7. O-O Nc6 8. a3 dxc4 9. Bxc4 cxd4 
******E58: Nimzo-Indian, 4.e3, main line with 8...Bxc3
Nimzo-Indian, 4.e3, main line with 8...Bxc3
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3 d5 6. Bd3 c5 7. O-O Nc6 8. a3 Bxc3 9. bxc3
******E59: Nimzo-Indian, 4.e3, main line
Nimzo-Indian, 4.e3, main line
1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. e3 O-O 5. Nf3 d5 6. Bd3 c5 7. O-O Nc6 8. a3 Bxc3 9. bxc3 dxc4 10. Bxc4
******E60: King's Indian defence
King's Indian defence
1. d4 Nf6 2. c4 g6 
King's Indian, 3.Nf3
1. d4 Nf6 2. c4 g6 3. Nf3
Queen's pawn, Mengarini attack
1. d4 Nf6 2. c4 g6 3. Qc2
King's Indian, Anti-Gruenfeld
1. d4 Nf6 2. c4 g6 3. d5
King's Indian, Danube gambit
1. d4 Nf6 2. c4 g6 3. d5 b5 
King's Indian, 3.g3
1. d4 Nf6 2. c4 g6 3. g3
King's Indian, 3.g3, counterthrust variation
1. d4 Nf6 2. c4 g6 3. g3 Bg7 4. Bg2 d5 
******E61: King's Indian defence, 3.Nc3
King's Indian defence, 3.Nc3
1. d4 Nf6 2. c4 g6 3. Nc3
King's Indian, Smyslov system
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. Bg5
******E62: King's Indian, fianchetto variation
King's Indian, fianchetto variation
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3
King's Indian, fianchetto, Larsen system
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 c6 7. O-O Bf5 
King's Indian, fianchetto, Kavalek (Bronstein) variation
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 c6 7. O-O Qa5 
King's Indian, fianchetto with ...Nc6
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 Nc6 
King's Indian, fianchetto, Uhlmann (Szabo) variation
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 Nc6 7. O-O e5 
King's Indian, fianchetto, lesser Simagin (Spassky) variation
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 Nc6 7. O-O Bf5 
King's Indian, fianchetto, Simagin variation
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 Nc6 7. O-O Bg4 
******E63: King's Indian, fianchetto, Panno variation
King's Indian, fianchetto, Panno variation
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 Nc6 7. O-O a6 
******E64: King's Indian, fianchetto, Yugoslav system
King's Indian, fianchetto, Yugoslav system
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 c5 
******E65: King's Indian, fianchetto, Yugoslav, 7.O-O
King's Indian, fianchetto, Yugoslav, 7.O-O
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 c5 7. O-O
******E66: King's Indian, fianchetto, Yugoslav Panno
King's Indian, fianchetto, Yugoslav Panno
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 c5 7. O-O Nc6 8. d5
******E67: King's Indian, fianchetto with ...Nd7
King's Indian, fianchetto with ...Nd7
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 Nbd7 
King's Indian, fianchetto, classical variation
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 Nbd7 7. O-O e5 
******E68: King's Indian, fianchetto, classical variation, 8.e4
King's Indian, fianchetto, classical variation, 8.e4
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 Nbd7 7. O-O e5 8. e4
******E69: King's Indian, fianchetto, classical main line
King's Indian, fianchetto, classical main line
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. Nf3 d6 5. g3 O-O 6. Bg2 Nbd7 7. O-O e5 8. e4 c6 9. h3
******E70: King's Indian, 4.e4
King's Indian, 4.e4
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4
King's Indian, Kramer system
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nge2
King's Indian, accelerated Averbakh system
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Bg5
******E71: King's Indian, Makagonov system (5.h3)
King's Indian, Makagonov system (5.h3)
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. h3
******E72: King's Indian with e4 & g3
King's Indian with e4 & g3
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. g3
King's Indian, Pomar system
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. g3 O-O 6. Bg2 e5 7. Nge2
******E73: King's Indian, 5.Be2
King's Indian, 5.Be2
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Be2
King's Indian, Semi-Averbakh system
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Be2 O-O 6. Be3
King's Indian, Averbakh system
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Be2 O-O 6. Bg5
******E74: King's Indian, Averbakh, 6...c5
King's Indian, Averbakh, 6...c5
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Be2 O-O 6. Bg5 c5 
******E75: King's Indian, Averbakh, main line
King's Indian, Averbakh, main line
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Be2 O-O 6. Bg5 c5 7. d5 e6 
******E76: King's Indian, Four pawns attack
King's Indian, Four pawns attack
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f4
King's Indian, Four pawns attack, dynamic line
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f4 O-O 6. Nf3 c5 7. d5
******E77: King's Indian, Four pawns attack, 6.Be2
King's Indian, Four pawns attack, 6.Be2
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f4 O-O 6. Be2
King's Indian, Six pawns attack
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f4 O-O 6. Be2 c5 7. d5 e6 8. dxe6 fxe6 9. g4 Nc6 10. h4
King's Indian, Four pawns attack
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f4 O-O 6. Be2 c5 7. d5 e6 8. Nf3
King's Indian, Four pawns attack, Florentine gambit
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f4 O-O 6. Be2 c5 7. d5 e6 8. Nf3 exd5 9. e5
******E78: King's Indian, Four pawns attack, with Be2 and Nf3
King's Indian, Four pawns attack, with Be2 and Nf3
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f4 O-O 6. Be2 c5 7. Nf3
******E79: King's Indian, Four pawns attack, main line
King's Indian, Four pawns attack, main line
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f4 O-O 6. Be2 c5 7. Nf3 cxd4 8. Nxd4 Nc6 9. Be3
******E80: King's Indian, Saemisch variation
King's Indian, Saemisch variation
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3
******E81: King's Indian, Saemisch, 5...O-O
King's Indian, Saemisch, 5...O-O
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3 O-O 
King's Indian, Saemisch, Byrne variation
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3 O-O 6. Be3 c6 7. Bd3 a6 
******E82: King's Indian, Saemisch, double fianchetto variation
King's Indian, Saemisch, double fianchetto variation
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3 O-O 6. Be3 b6 
******E83: King's Indian, Saemisch, 6...Nc6
King's Indian, Saemisch, 6...Nc6
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3 O-O 6. Be3 Nc6 
King's Indian, Saemisch, Ruban variation
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3 O-O 6. Be3 Nc6 7. Nge2 Rb8 
King's Indian, Saemisch, Panno formation
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3 O-O 6. Be3 Nc6 7. Nge2 a6 
******E84: King's Indian, Saemisch, Panno main line
King's Indian, Saemisch, Panno main line
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3 O-O 6. Be3 Nc6 7. Nge2 a6 8. Qd2 Rb8 
******E85: King's Indian, Saemisch, orthodox variation
King's Indian, Saemisch, orthodox variation
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3 O-O 6. Be3 e5 
******E86: King's Indian, Saemisch, orthodox, 7.Nge2 c6
King's Indian, Saemisch, orthodox, 7.Nge2 c6
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3 O-O 6. Be3 e5 7. Nge2 c6 
******E87: King's Indian, Saemisch, orthodox, 7.d5
King's Indian, Saemisch, orthodox, 7.d5
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3 O-O 6. Be3 e5 7. d5
King's Indian, Saemisch, orthodox, Bronstein variation
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3 O-O 6. Be3 e5 7. d5 Nh5 8. Qd2 Qh4+ 9. g3 Nxg3 10. Qf2 Nxf1 11. Qxh4 Nxe3 12. Ke2 Nxc4 
******E88: King's Indian, Saemisch, orthodox, 7.d5 c6
King's Indian, Saemisch, orthodox, 7.d5 c6
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3 O-O 6. Be3 e5 7. d5 c6 
******E89: King's Indian, Saemisch, orthodox main line
King's Indian, Saemisch, orthodox main line
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f3 O-O 6. Be3 e5 7. d5 c6 8. Nge2 cxd5 
******E90: King's Indian, 5.Nf3
King's Indian, 5.Nf3
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3
King's Indian, Larsen variation
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be3
King's Indian, Zinnowitz variation
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Bg5
******E91: King's Indian, 6.Be2
King's Indian, 6.Be2
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2
King's Indian, Kazakh variation
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 Na6 
******E92: King's Indian, classical variation
King's Indian, classical variation
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 
King's Indian, Andersson variation
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. dxe5
King's Indian, Gligoric-Taimanov system
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. Be3
King's Indian, Petrosian system
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. d5
King's Indian, Petrosian system, Stein variation
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. d5 a5 
******E93: King's Indian, Petrosian system, main line
King's Indian, Petrosian system, main line
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. d5 Nbd7 
King's Indian, Petrosian system, Keres variation
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. d5 Nbd7 8. Bg5 h6 9. Bh4 g5 10. Bg3 Nh5 11. h4
******E94: King's Indian, orthodox variation
King's Indian, orthodox variation
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. O-O
King's Indian, orthodox, Donner variation
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. O-O c6 
King's Indian, orthodox, 7...Nbd7
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. O-O Nbd7 
******E95: King's Indian, orthodox, 7...Nbd7, 8.Re1
King's Indian, orthodox, 7...Nbd7, 8.Re1
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. O-O Nbd7 8. Re1
******E96: King's Indian, orthodox, 7...Nbd7, main line
King's Indian, orthodox, 7...Nbd7, main line
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. O-O Nbd7 8. Re1 c6 9. Bf1 a5 
******E97: King's Indian, orthodox, Aronin-Taimanov variation (Yugoslav attack / Mar del Plata variation)
King's Indian, orthodox, Aronin-Taimanov variation (Yugoslav attack / Mar del Plata variation)
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. O-O Nc6 
King's Indian, orthodox, Aronin-Taimanov, bayonet attack
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. O-O Nc6 8. d5 Ne7 9. b4
******E98: King's Indian, orthodox, Aronin-Taimanov, 9.Ne1
King's Indian, orthodox, Aronin-Taimanov, 9.Ne1
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. O-O Nc6 8. d5 Ne7 9. Ne1
******E99: King's Indian, orthodox, Aronin-Taimanov, main line
King's Indian, orthodox, Aronin-Taimanov, main line
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. O-O Nc6 8. d5 Ne7 9. Ne1 Nd7 10. f3 f5 
King's Indian, orthodox, Aronin-Taimanov, Benko attack
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3 O-O 6. Be2 e5 7. O-O Nc6 8. d5 Ne7 9. Ne1 Nd7 10. f3 f5 11. g4"""


OPENINGS = []
openings = TEXT.split("******")
openings = [l for l in openings if len(l)]

for opening in openings:
    lines = opening.split("\n")
    title_line = lines[0]
    id = title_line[:3]
    name = title_line[5:]
    mainline = lines[2]
    variant_lines = lines[3:]
    variant_lines = [l for l in variant_lines if len(l)]
    pgn = io.StringIO(mainline)
    game = chess.pgn.read_game(pgn)
    visitor = MoveVisitor()
    game.accept(visitor)
    moves = visitor.moves
    board = chess.Board()
    models = create_move_models(board, moves)
    variants = []
    for i in range(0, len(variant_lines), 2):
        variant_name = variant_lines[i]
        variant_pgn = variant_lines[i + 1]
        variant_pgn = io.StringIO(variant_pgn)
        variant_game = chess.pgn.read_game(variant_pgn)
        visitor = MoveVisitor()
        variant_game.accept(visitor)
        variant_moves = visitor.moves
        variant_board = chess.Board()
        variant_models = create_move_models(variant_board, variant_moves)
        variant = OpeningVariant(variant_name, variant_models)
        variants.append(variant)
    OPENINGS.append(Opening(name, id, models, variants=variants))