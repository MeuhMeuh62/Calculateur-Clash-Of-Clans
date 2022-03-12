hdv = int(input("Niveau hôtel de ville"))

CoutOr = 0
CoutElixir = 0
TempsH = 0
TempsM = 0
TempsS = 0

# A1 = Aigle artilleur
A1 = 0
# A2 = Arc-X
A2 = 0
# A3 = Canon
A3 = 0
# A4 = Défense anti-aérienne
A4 = 0
# A10 = Mortier
A12 = 0
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
                A12 = A12 + 1
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
                            A12 = A12 + 1
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
                                A12 = A12 + 1
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
                                    A12 = A12 + 1
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
    if hdv >= 11:
        A1n1 = int(input("Niveau Aigle Artilleur = 1 ?"))
        CoutOr = A1n1 * 8000000 + CoutOr
        TempsH = A1n1 * 168 + TempsH
        A1n2 = int(input("Niveau Aigle Artilleur = 2 ?")) + A1n1
        CoutOr = A1n2 * 10000000 + CoutOr
        TempsH = A1n2 * 240 + TempsH
        if hdv >= 12:
            A1n3 = int(input("Niveau Aigle Artilleur = 3 ?")) + A1n2
            CoutOr = A1n3 * 12000000 + CoutOr
            TempsH = A1n3 * 336 + TempsH
            if hdv >= 13:
                A1n4 = int(input("Niveau Aigle Artilleur = 4 ?")) + A1n3
                CoutOr = A1n4 * 18000000 + CoutOr
                TempsH = A1n4 * 432 + TempsH
                if hdv >= 14:
                    A1n5 = int(input("Niveau Aigle Artilleur = 5 ?")) + A1n4
                    CoutOr = A1n5 * 20000000 + CoutOr
                    TempsH = A1n5 * 480 + TempsH
"""
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
    A4n1 = int(input("Niveau Défence Anti-Aérienne = 1 ?"))
    A4n2 = int(input("Niveau Défence Anti-Aérienne = 2 ?"))
    A4n3 = int(input("Niveau Défence Anti-Aérienne = 3 ?"))
    A4n4 = int(input("Niveau Défence Anti-Aérienne = 4 ?"))
    A4n5 = int(input("Niveau Défence Anti-Aérienne = 5 ?"))
    A4n6 = int(input("Niveau Défence Anti-Aérienne = 6 ?"))
    A4n7 = int(input("Niveau Défence Anti-Aérienne = 7 ?"))
    A4n8 = int(input("Niveau Défence Anti-Aérienne = 8 ?"))
    A4n9 = int(input("Niveau Défence Anti-Aérienne = 9 ?"))
    A4n10 = int(input("Niveau Défence Anti-Aérienne = 10 ?"))
    A4n11 = int(input("Niveau Défence Anti-Aérienne = 11 ?"))
    A4n12 = int(input("Niveau Défence Anti-Aérienne = 12 ?"))
if A5 > 0:
    A5n1 = int(input("Niveau Catapulte erratique = 1 ?"))
    A5n2 = int(input("Niveau Catapulte erratique = 2 ?"))
    A5n3 = int(input("Niveau Catapulte erratique = 3 ?"))
if A6 > 0:
    A6n1 = int(input("Niveau Propuseur d'air = 1 ?"))
    A6n2 = int(input("Niveau Propuseur d'air = 2 ?"))
    A6n3 = int(input("Niveau Propuseur d'air = 3 ?"))
    A6n4 = int(input("Niveau Propuseur d'air = 4 ?"))
    A6n5 = int(input("Niveau Propuseur d'air = 5 ?"))
    A6n6 = int(input("Niveau Propuseur d'air = 6 ?"))
    A6n7 = int(input("Niveau Propuseur d'air = 7 ?"))
if A7 > 0:
    A7n1 = int(input("Niveau Tour à bombes = 1 ?"))
    A7n2 = int(input("Niveau Tour à bombes = 2 ?"))
    A7n3 = int(input("Niveau Tour à bombes = 3 "))
    A7n4 = int(input("Niveau Tour à bombes = 4 ?"))
    A7n5 = int(input("Niveau Tour à bombes = 5 ?"))
    A7n6 = int(input("Niveau Tour à bombes = 6 ?"))
    A7n7 = int(input("Niveau Tour à bombes = 7 ?"))
    A7n8 = int(input("Niveau Tour à bombes = 8 ?"))
    A7n9 = int(input("Niveau Tour à bombes = 9 ?"))
if A8 > 0:
    A8n1 = int(input("Niveau Tour d'archers = 1 ?"))
    A8n2 = int(input("Niveau Tour d'archers = 2 ?"))
    A8n3 = int(input("Niveau Tour d'archers = 3 ?"))
    A8n4 = int(input("Niveau Tour d'archers = 4 ?"))
    A8n5 = int(input("Niveau Tour d'archers = 5 ?"))
    A8n6 = int(input("Niveau Tour d'archers = 6 ?"))
    A8n7 = int(input("Niveau Tour d'archers = 7 ?"))
    A8n8 = int(input("Niveau Tour d'archers = 8 ?"))
    A8n9 = int(input("Niveau Tour d'archers = 9 ?"))
    A8n10 = int(input("Niveau Tour d'archers = 10 ?"))
    A8n11 = int(input("Niveau Tour d'archers = 11 ?"))
    A8n12 = int(input("Niveau Tour d'archers = 12 ?"))
    A8n13 = int(input("Niveau Tour d'archers = 13 ?"))
    A8n14 = int(input("Niveau Tour d'archers = 14 ?"))
    A8n15 = int(input("Niveau Tour d'archers = 15 ?"))
    A8n16 = int(input("Niveau Tour d'archers = 16 ?"))
    A8n17 = int(input("Niveau Tour d'archers = 17 ?"))
    A8n18 = int(input("Niveau Tour d'archers = 18 ?"))
    A8n19 = int(input("Niveau Tour d'archers = 19 ?"))
    A8n20 = int(input("Niveau Tour d'archers = 20 ?"))
if A9 > 0:
    A9n1 = int(input("Niveau tour de l'enfer = 1 ?"))
    A9n2 = int(input("Niveau tour de l'enfer = 2 ?"))
    A9n3 = int(input("Niveau tour de l'enfer = 3 ?"))
    A9n4 = int(input("Niveau tour de l'enfer = 4 ?"))
    A9n5 = int(input("Niveau tour de l'enfer = 5 ?"))
    A9n6 = int(input("Niveau tour de l'enfer = 6 ?"))
    A9n7 = int(input("Niveau tour de l'enfer = 7 ?"))
    A9n8 = int(input("Niveau tour de l'enfer = 8 ?"))
if A10 > 0:
    A10n1 = int(input("Niveau Tour de sorciers = 1 ?"))
    A10n2 = int(input("Niveau Tour de sorciers = 2 ?"))
    A10n3 = int(input("Niveau Tour de sorciers = 3 ?"))
    A10n4 = int(input("Niveau Tour de sorciers = 4 ?"))
    A10n5 = int(input("Niveau Tour de sorciers = 5 ?"))
    A10n6 = int(input("Niveau Tour de sorciers = 6 ?"))
    A10n7 = int(input("Niveau Tour de sorciers = 7 ?"))
    A10n8 = int(input("Niveau Tour de sorciers = 8 ?"))
    A10n9 = int(input("Niveau Tour de sorciers = 9 ?"))
    A10n10 = int(input("Niveau Tour de sorciers = 10 ?"))
    A10n11 = int(input("Niveau Tour de sorciers = 11 ?"))
    A10n12 = int(input("Niveau Tour de sorciers = 12 ?"))
    A10n13 = int(input("Niveau Tour de sorciers = 13 ?"))
    A10n14 = int(input("Niveau Tour de sorciers = 14 ?"))
if A11 > 0:
    A11n1 = int(input("Niveau Tesla = 1 ?"))
    A11n2 = int(input("Niveau Tesla = 2 ?"))
    A11n3 = int(input("Niveau Tesla = 3 ?"))
    A11n4 = int(input("Niveau Tesla = 4 ?"))
    A11n5 = int(input("Niveau Tesla = 5 ?"))
    A11n6 = int(input("Niveau Tesla = 6 ?"))
    A11n7 = int(input("Niveau Tesla = 7 ?"))
    A11n8 = int(input("Niveau Tesla = 8 ?"))
    A11n9 = int(input("Niveau Tesla = 9 ?"))
    A11n10 = int(input("Niveau Tesla = 10 ?"))
    A11n11 = int(input("Niveau Tesla = 11 ?"))
    A11n12 = int(input("Niveau Tesla = 12 ?"))
    A11n13 = int(input("Niveau Tesla = 13 ?"))
if A12 > 0:
    A12n1 = int(input("Niveau Mortier = 1 ?"))
    A12n2 = int(input("Niveau Mortier = 2 ?"))
    A12n3 = int(input("Niveau Mortier = 3 ?"))
    A12n4 = int(input("Niveau Mortier = 4 ?"))
    A12n5 = int(input("Niveau Mortier = 5 ?"))
    A12n6 = int(input("Niveau Mortier = 6 ?"))
    A12n7 = int(input("Niveau Mortier = 7 ?"))
    A12n8 = int(input("Niveau Mortier = 8 ?"))
    A12n9 = int(input("Niveau Mortier = 9 ?"))
    A12n10 = int(input("Niveau Mortier = 10 ?"))
    A12n11 = int(input("Niveau Mortier = 11 ?"))
    A12n12 = int(input("Niveau Mortier = 12 ?"))
    A12n13 = int(input("Niveau Mortier = 13 ?"))
    A12n14 = int(input("Niveau Mortier = 14 ?"))
"""

print("Tu deveras payer : " + str(CoutOr))
print("Ca prendras : " + str(TempsH) + " heures.")
