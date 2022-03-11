hdv = int(input("Niveau hôtel de ville"))

# A1 = Aigle artilleur
A1 = 0
# A2 = Arc-X
A2 = 0
# A3 = Canon
A3 = 0
# A4 = Défense anti-aérienne
A4 = 0
# A5 = Catapulte erratique
A5 = 0
# A6 = Propulseur d'air
A6 = 0
# A7 = Tour à bombes
A7 = 0
# A8 = Tour d'archer
A8 = 0
# A9 = Tour de l'enfer
A9 = 0
# A10 = Tour de sorciers
A10 = 0
# A11 = Tesla
A11 = 0

# B1 = Piège à ressort
B1 = 0
# B2 = Bombe
B2 = 0
# B3 = Bombe géante
B3 = 0
# B4 = Bombe aérienne
B4 = 0
# B5 = Mine chercheuse
B5 = 0
# B6 = Piège squelettique
B6 = 0
# B7 = Piège tornade
B7 = 0

# R1 = Remparts
R1 = 0

# C1 = Camp militaire
C1 = 0
# C2 = Caserne
C2 = 0
# C3 = Caserne noire
C3 = 0
# C4 = Laboratoire
C4 = 0
# C5 = Usine de sorts
C5 = 0
# C6 = Usine de sorts noirs
C6 = 0
# C7 = Atelier
C7 = 0
# C8 = Animalerie
C8 = 0

# D1 = Château de clan
D1 = 0
# D2 = Mine d'or
D2 = 0
# D3 = Réserve d'or
D3 = 0
# D4 = Extracteur d'élixir
D4 = 0
# D5 = Réservevoir d'élexir
D5 = 0
# D6 = Foreuse d'élexir noir
D6 = 0
# D7 = Réservoir d'élexir noir
D7 = 0

if 0 < hdv < 15:
    if hdv >= 1:
        A3 = A3 + 2
        C1 = C1 + 1
        C2 = C2 + 1
        D2 = D2 + 1
        D3 = D3 + 1
        D4 = D4 + 1
        D5 = D5 + 1
        if hdv >= 2:
            A8 = A8 + 1
            R1 = R1 + 25
            C2 = C2 + 1
            D2 = D2 + 1
            D4 = D4 + 1
            if hdv >= 3:
                B2 = B2 + 2
                R1 = R1 + 25
                C1 = C1 + 1
                C4 = C4 + 1
                D1 = D1 + 1
                D2 = D2 + 1
                D3 = D3 + 1
                D4 = D4 + 1
                D5 = D5 + 1
                if hdv >= 4:
                    A4 = A4 + 1
                    A8 = A8 + 1
                    B1 = B1 + 2
                    R1 = R1 + 25
                    C2 = C2 + 1
                    D2 = D2 + 1
                    D4 = D4 + 1
                    if hdv >= 5:
                        A3 = A3 + 1
                        A8 = A8 + 1
                        A10 = A10 + 1
                        B2 = B2 + 2
                        R1 = R1 + 25
                        C1 = C1 + 1
                        C5 = C5 + 1
                        D2 = D2 + 1
                        D4 = D4 + 1
                        if hdv >= 6:
                            A4 = A4 + 1
                            A6 = A6 + 1
                            A10 = A10 + 1
                            A11 = A11 + 1
                            B1 = B1 + 2
                            B3 = B3 + 1
                            B4 = B4 + 2
                            R1 = R1 + 25
                            D2 = D2 + 1
                            D4 = D4 + 1
                            if hdv >= 7:
                                A3 = A3 + 2
                                A4 = A4 + 1
                                A8 = A8 + 1
                                A11 = A11 + 1
                                B2 = B2 + 2
                                B3 = B3 + 1
                                B5 = B5 + 1
                                R1 = R1 + 50
                                C1 = C1 + 1
                                C2 = C2 + 1
                                C3 = C3 + 1
                                D6 = D6 + 1
                                D7 = D7 + 1
                                if hdv >= 8:
                                    A7 = A7 + 1
                                    A8 = A8 + 1
                                    A10 = A10 + 1
                                    A11 = A11 + 1
                                    B1 = B1 + 2
                                    B3 = B3 + 1
                                    B4 = B4 + 2
                                    B5 = B5 + 1
                                    B6 = B6 + 2
                                    R1 = R1 + 50
                                    C3 = C3 + 1
                                    C6 = C6 + 1
                                    D3 = D3 + 1
                                    D5 = D5 + 1
                                    D6 = D6 + 1
                                    if hdv >= 9:
                                        A2 = A2 + 2
                                        A4 = A4 + 1
                                        A6 = A6 + 1
                                        A8 = A8 + 1
                                        A10 = A10 + 1
                                        A11 = A11 + 1
                                        B3 = B3 + 1
                                        B5 = B5 + 2
                                        R1 = R1 + 25
                                        D2 = D2 + 1
                                        D3 = D3 + 1
                                        D4 = D4 + 1
                                        D5 = D5 + 1
                                        D6 = D6 + 1
                                        if hdv >= 10:
                                            A2 = A2 + 1
                                            A3 = A3 + 1
                                            A7 = A7 + 1
                                            A8 = A8 + 1
                                            A9 = A9 + 2
                                            B3 = B3 + 1
                                            B4 = B4 + 1
                                            B5 = B5 + 1
                                            B6 = B6 + 1
                                            R1 = R1 + 25
                                            if hdv >= 11:
                                                A1 = A1 + 1
                                                A2 = A2 + 1
                                                A3 = A3 + 1
                                                A8 = A8 + 1
                                                A10 = A10 + 1
                                                B7 = B7 + 1
                                                R1 = R1 + 25
                                                if hdv >= 12:
                                                    A9 = A9 + 1
                                                    A11 = A11 + 1
                                                    B1 = B1 + 2
                                                    B3 = B3 + 1
                                                    B4 = B4 + 1
                                                    B5 = B5 + 1
                                                    C7 = C7 + 1
                                                    if hdv >= 13:
                                                        A5 = A5 + 2
                                                        B1 = B1 + 1
                                                        B2 = B2 + 1
                                                        B5 = B5 + 1
                                                        if hdv >= 14:
                                                            B2 = B2 + 1
                                                            B3 = B3 + 1
                                                            B4 = B4 + 1
                                                            B5 = B5 + 1
                                                            B6 = B6 + 1
                                                            R1 = R1 + 25
                                                            C8 = C8 + 1
if A1 > 0:
    A1n1 = int(input("Niveau Aigle Artilleur = 1 ?"))
    A1n2 = int(input("Niveau Aigle Artilleur = 2 ?"))
    A1n3 = int(input("Niveau Aigle Artilleur = 3 ?"))
    A1n4 = int(input("Niveau Aigle Artilleur = 4 ?"))
    A1n5 = int(input("Niveau Aigle Artilleur = 5 ?"))
if A2 > 0:
    A2n1 = int(input("Niveau Arc-X = 1 ?"))
    A2n2 = int(input("Niveau Arc-X = 2 ?"))
    A2n3 = int(input("Niveau Arc-X = 3 ?"))
    A2n4 = int(input("Niveau Arc-X = 4 ?"))
    A2n5 = int(input("Niveau Arc-X = 5 ?"))
    A2n6 = int(input("Niveau Arc-X = 6 ?"))
    A2n7 = int(input("Niveau Arc-X = 7 ?"))
    A2n8 = int(input("Niveau Arc-X = 8 ?"))
    A2n9 = int(input("Niveau Arc-X = 9 ?"))
if A3 > 0:
    A3n1 = int(input("Niveau Canon = 1 ?"))
    A3n2 = int(input("Niveau Canon = 2 ?"))
    A3n3 = int(input("Niveau Canon = 3 ?"))
    A3n4 = int(input("Niveau Canon = 4 ?"))
    A3n5 = int(input("Niveau Canon = 5 ?"))
    A3n6 = int(input("Niveau Canon = 6 ?"))
    A3n7 = int(input("Niveau Canon = 7 ?"))
    A3n8 = int(input("Niveau Canon = 8 ?"))
    A3n9 = int(input("Niveau Canon = 9 ?"))
    A3n10 = int(input("Niveau Canon = 10 ?"))
    A3n11 = int(input("Niveau Canon = 11 ?"))
    A3n12 = int(input("Niveau Canon = 12 ?"))
    A3n13 = int(input("Niveau Canon = 13 ?"))
    A3n14 = int(input("Niveau Canon = 14 ?"))
    A3n15 = int(input("Niveau Canon = 15 ?"))
    A3n16 = int(input("Niveau Canon = 16 ?"))
    A3n17 = int(input("Niveau Canon = 17 ?"))
    A3n18 = int(input("Niveau Canon = 18 ?"))
    A3n19 = int(input("Niveau Canon = 19 ?"))
    A3n20 = int(input("Niveau Canon = 20 ?"))
if A4 > 0:
    A3n1 = int(input("Niveau Défence Anti-Aérienne = 1 ?"))
