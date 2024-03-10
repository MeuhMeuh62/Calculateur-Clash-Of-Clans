hdv = int(input("Niveau hdv ?"))

# Or à décimale reset
Or = 0
# Élixir à décimale reset
El = 0
# Temps seconde à décimale reset
Tps = 0
# Expérience à décimale reset
Exp = 0


# DÉFENCES

# Aigle Artilleur
A1 = 0
# Arc-X
A2 = 0
# Canon
A3 = 0
# Défense Anti-Aérienne
A4 = 0
# Mortier
A5= 0
# Catapulte erratique
A6 = 0
# Monolithe
A7 = 0
# Propulseur d'Air
A8 = 0
# Tour à Bombes
A9 = 0
# Tour d'Archer
A10 = 0
# Tour de l'enfer
A11 = 0
# Tour de Sorciers
A12 = 0
# Tour runique
A13 = 0
# Tesla
A14 = 0
# Remparts
A15 = 0


# ARMÉE

# Camp militaire
B1 = 0
# Caserne
B2= 0
# Caserne noire
B3 = 0
# Laboratoire
B4 = 0
# Usine de sorts
B5 = 0
# Usine de sorts noirs
B6 = 0
# Atelier
B7 = 0
# Animalerie
B8 = 0


# RESSOURCES

# Château de clan
C1 = 0
# Mine d'or
C2 = 0
# Réserve d'or
C3 = 0
# Extracteur d'élixir
C4 = 0
# Réservoir d'élixir
C5 = 0
# Foreuse d'élixir noir
C6 = 0
# Réservoir d'élixir noir
C7 = 0


# TROUPES

# Barbare
D1 = 0
# Archer
D2 = 0
# Géant
D3 = 0
# Gobelin
D4 = 0
# Sapeur
D5 = 0
# Ballon
D6 = 0
# Sorcier
D7 = 0
# Guérisseuse
D8 = 0
# Dragon
D9 = 0
# P.E.K.K.A
D10 = 0
# Bébé dragon
D11 = 0
# Mineur
D12 = 0
# Electro-dragon
D13 = 0
# Yéti
D14 = 0
# Chevaucheur de dragon
D15 = 0
# Electro-titanide
D16 = 0


# TROUPES NOIRES

# Gargouille
E1 = 0
# Chevaucheur de cochon
E2 = 0
# Valkyrie
E3 = 0
# Golem
E4 = 0
# Sorcière
E5 = 0
# Molosse de lave
E6 = 0
# Bouliste
E7 = 0
# Golem de glace
E8 = 0
# Chasseuse de tête
E9 = 0


# LES HÉROS

# Roi des barbares
F1 = 0
# Reine des archers
F2 = 0
# Championne royale
F3 = 0
# Grand gardien
F4 = 0


# LES FAMILIERS

# L.A.S.S.I
G1 = 0
# Electro-chouette
G2 = 0
# Yak robuste
G3 = 0
# Licorne
G4 = 0
# Flocon
G5 = 0
# Pablo
G6 = 0
# Lézard létal
G7 = 0
# Phénix
G8 = 0


# SORTS

# Foudre
H1 = 0
# Guérison
H2 = 0
# Rage
H3 = 0
# Saut
H4 = 0
# Gel
H5 = 0
# Clonage
H6 = 0
# Invisibilité
H7 = 0
# RAppel
H8 = 0


# SORTS NOIRS

# Empoisonnement
I1 = 0
# Sismique
I2 = 0
# Precipitation
I3 = 0
# Squelettique
I4 = 0
# Chauves-souris
I5 = 0


# ENGEINS DE SIÈGE

# Démolisseur
J1 = 0
# Dirigeable de combat
J2 = 0
# Broyeur de pierres
J3 = 0
# Caserne de siège
J4 = 0
# Lance-bûches
J5 = 0
# Catapulte d'esprits
J6 = 0
# Foreuse de combat
J7 = 0


# SUPER TROUPES

# Super barbare
K1 = 0
# Super géant
K2 = 0
# Gobelin furtif
K3 = 0
# Super saeur
K4 = 0
# Dragon de l'enfer
K5 = 0
# Super sorcière
K6 = 0
# Super archer
K7 = 0
# Super gargouille
K8 = 0
# Super valkyrie
K9 = 0
# Super sorcier
K10 = 0
# Molosse de glace
K11 = 0
# Ballon à propulsion
K12 = 0
# Super bouliste
K13 = 0
# Super dragon
K14 = 0
# Super mineur
K15 = 0


# PIÈGES

# Piège à ressort
L1 = 0
# Bombe
L2 = 0
# Bombe Géante
L3 = 0 
# Bombe aérienne
L4 = 0
# Mine chercheuse
L5 = 0
# Piège squelettique
L6 = 0
# Piège tornade
L7 = 0


# BÂTIMENTS

if hdv >= 1:
    A3 = A3 + 2

    B1 = B1 + 1
    B2 = B2 + 1

    C2 = C2 + 1
    C3 = C3 + 1
    C4 = C4 + 1
    C5 = C5 + 1
if hdv >= 2:
    A10 = A10 + 1

    C2 = C2 + 1
    C4 = C4 + 1
if hdv >= 3:
    A5 = A5 + 1
    
    B1 = B1 + 1
    B4 = B4 + 1

    C1 = C1 + 1
    C2 = C2 + 1
    C3 = C3 + 1
    C4 = C4 + 1
    C5 = C5 + 1

    L2 = L2 + 2
if hdv >= 4:
    A4 = A4 + 1
    A10 = A10 + 1

    C2 = C2 + 1
    C4 = C4 + 1

    L1 = L1 + 2
if hdv >= 5:
    A3 = A3 + 1
    A10 = A10 + 1
    A12 = A12 + 1
    
    B1 = B1 + 1
    B5 = B5 + 1

    C2 = C2 + 1
    C4 = C4 + 1

    L2 = L2 + 2
    L4 = L4 + 2
if hdv >= 6:
    A4 = A4 + 1
    A5 = A5 + 1
    A8 = A8 + 1
    A12 = A12 + 1

    C2 = C2 + 1
    C4 = C4 + 1

    L1 = L1 + 2
    L3 = L3 + 1
if hdv >= 7:
    A3 = A3 + 2
    A4 = A4 + 1
    A5 = A5 + 1
    A10 = A10 + 1
    A14 = A14 + 2

    B1 = B1 + 1
    B3 = B3 + 1

    C6 = C6 + 1
    C7 = C7 + 1

    L2 = L2 + 2
    L3 = L3 + 1
    L5 = L5 + 1
if hdv >= 8:
    A9 = A9 + 1
    A10 = A10 + 1
    A12 = A12 + 1
    A14 = A14 + 1

    B6 = B6 + 1

    C3 = C3 + 1
    C5 = C5 + 1
    C6 = C6 + 1

    L1 = L1 + 2
    L3 = L3 + 1
    L4 = L4 + 2
    L5 = L5 + 1
    L6 = L6 + 2
if hdv >= 9:
    A2 = A2 + 2
    A4 = A4 + 1
    A5 = A5 + 1
    A8 = A8 + 1
    A10 = A10 + 1
    A12 = A12 + 1
    A14 = A14 + 1

    C2 = C2 + 1
    C3 = C3 + 1
    C4 = C4 + 1
    C5 = C5 + 1
    C6 = C6 + 1

    L3 = L3 + 1
    L5 = L5 + 2
if hdv >= 10:
    A2 = A2 + 1
    A3 = A3 + 1
    A9 = A9 + 1
    A10 = A10 + 1
    A11 = A11 + 2

    L3 = L3 + 1
    L4 = L4 + 1
    L5 = L5 + 1
    L6 = L6 + 1
if hdv >= 11:
    A1 = A1 + 1
    A2 = A2 + 1
    A3 = A3 + 1
    A10 = A10 + 1
    A12 = A12 + 1

    L7 = L7 + 1
if hdv >= 12:
    A11 = A11 + 1
    A14 = A14 + 1

    B7 = B7 + 1

    L1 = L1 + 2
    L3 = L3 + 1
    L4 = L4 + 1
    L5 = L5 + 1
if hdv >= 13:
    A6 = A6 + 2

    L1 = L1 + 1
    L2 = L2 + 1
    L5 = L5 + 1
if hdv >= 14:
    B8 = B8 + 1

    L2 = L2 + 1
    L3 = L3 + 1
    L4 = L4 + 1
    L5 = L5 + 1
    L6 = L6 + 1
if hdv >= 15:
    A7 = A7 + 1
    A13 = A13 + 2


# A
#f intègre la variable A1 dans le print sans besoin de + str(A1)

print(f"A1 = {A1}")
print(f"A2 = {A2}")
print(f"A3 = {A3}")
print(f"A4 = {A4}")
print(f"A5 = {A5}")
print(f"A6 = {A6}")


FoisA1 = 0
A1total = A1
FoisA2 = 0
A2total = A2
FoisA3 = 0
A3total = A3
FoisA4 = 0
A4total = A4
FoisA5 = 0
A5total = A5
FoisA6 = 0
A6total = A6

while A1 > 0:
    nivA1 = 0
    nivA1 = int(input(f"Niveau de votre Aigle Artilleur n°{FoisA1}/{A1total}"))
    if hdv >= 11:
        if nivA1 == 0:
            Or = Or + 6000000
            Tps = Tps + 432000
            Exp = Exp + 657
            nivA1 = nivA1 + 1
        if nivA1 == 1:
            Or = Or + 8000000
            Tps = Tps + 734400
            Exp = Exp + 856
            nivA1 = nivA1 + 1
    if hdv >= 12:
        if nivA1 == 2:
            Or = Or + 11000000
            Tps = Tps +  950400
            Exp = Exp + 974
            nivA1 = nivA1 + 1
    if hdv >= 13:
        if nivA1 == 3:
            Or = Or + 15000000
            Tps = Tps + 1296000
            Exp = Exp + 1138
            nivA1 = nivA1 + 1
    if hdv >= 14:
        if nivA1 == 4:
            Or = Or + 19000000
            Tps = Tps + 1641600
            Exp = Exp + 1281
    A1 = A1 - 1
while A2 > 0:
    nivA2 = 0
    FoisA2 = FoisA2 + 1
    nivA2 = int(input(f"Niveau de votre Arc-X n°{FoisA2}/{A2total}"))
    if hdv >= 9:
        if nivA2 == 0:
            Or = Or + 1000000
            Tps = Tps + 172800
            Exp = Exp + 415
            nivA2 = nivA2 + 1
        if nivA2 == 1:
            Or = Or + 1600000
            Tps = Tps + 345600
            Exp = Exp + 587
            nivA2 = nivA2 + 1
        if nivA2 == 2:
            Or = Or + 2400000
            Tps = Tps + 432000
            Exp = Exp + 657
            nivA2 = nivA2 + 1
    if hdv >= 10:
        if nivA2 == 3:
            Or = Or + 3400000
            Tps = Tps + 453600
            Exp = Exp + 673
            nivA2 = nivA2 + 1
    if hdv >= 11:
        if nivA2 == 4:
            Or = Or + 4900000
            Tps = Tps + 540000
            Exp = Exp + 734
            nivA2 = nivA2 + 1
    if hdv >= 12:
        if nivA2 == 5:
            Or = Or + 7400000
            Tps = Tps + 842400
            Exp = Exp + 917
            nivA2 = nivA2 + 1
    if hdv >= 13:
        if nivA2 == 6:
            Or = Or + 10400000
            Tps = Tps + 1036800
            Exp = Exp + 1018
            nivA2 = nivA2 + 1
        if nivA2 == 7:
            Or = Or + 12900000
            Tps = Tps + 1101600
            Exp = Exp + 1049
            nivA2 = nivA2 + 1
    if hdv >= 14:
        if nivA2 == 8:
            Or = Or + 17400000
            Tps = Tps + 1555200
            Exp = Exp + 1247
            nivA2 = nivA2 + 1
    if hdv >= 15:
        if nivA2 == 9:
            Or = Or + 20000000
            Tps = Tps + 1641600
            Exp = Exp + 1281
    A2 = A2 - 1
while A3 > 0:
    nivA3 = 0
    FoisA3 = FoisA3 + 1
    nivA3 = int(input(f"Niveau de votre Canon n°{FoisA3}/{A3total} --------- "))
    if hdv >= 1:
        if nivA3 == 0:
            Or = Or + 250
            Tps = Tps + 10
            Exp = Exp + 3
            nivA3 = nivA3 + 1
    if hdv >= 2:
        if nivA3 == 1:
            Or = Or + 1000
            Tps = Tps + 120
            Exp = Exp + 10
            nivA3 = nivA3 + 1
        if nivA3 == 2:
            Or = Or + 4000
            Tps = Tps + 600
            Exp = Exp + 24
            nivA3 = nivA3 + 1
    if hdv >= 3:
        if nivA3 == 3:
            Or = Or + 16000
            Tps = Tps + 2700
            Exp = Exp + 51
            nivA3 = nivA3 + 1
    if hdv >= 4:
        if nivA3 == 4:
            Or = Or + 50000
            Tps = Tps + 7200
            Exp = Exp + 84
            nivA3 = nivA3 + 1
    if hdv >= 5:
        if nivA3 == 5:
            Or = Or + 100000
            Tps = Tps + 14400
            Exp = Exp + 120
            nivA3 = nivA3 + 1
    if hdv >= 6:
        if nivA3 == 6:
            Or = Or + 200000
            Tps = Tps + 28800
            Exp = Exp + 169
            nivA3 = nivA3 + 1
    if hdv >= 7:
        if nivA3 == 7:
            Or = Or + 300000
            Tps = Tps + 36000
            Exp = Exp + 189
            nivA3 = nivA3 + 1
    if hdv >= 8:
        if nivA3 == 8:
            Or = Or + 500000
            Tps = Tps + 43200
            Exp = Exp + 207
            nivA3 = nivA3 + 1
        if nivA3 == 9:
            Or = Or + 700000
            Tps = Tps + 64800
            Exp = Exp + 254
            nivA3 = nivA3 + 1
    if hdv >= 9:
        if nivA3 == 10:
            Or = Or + 1000000
            Tps = Tps + 86400
            Exp = Exp + 293
            nivA3 = nivA3 + 1
    if hdv >= 10:
        if nivA3 == 11:
            Or = Or + 1200000
            Tps = Tps + 108000
            Exp = Exp + 328
            nivA3 = nivA3 + 1
        if nivA3 == 12:
            Or = Or + 1700000
            Tps = Tps + 194400
            Exp = Exp + 440
            nivA3 = nivA3 + 1
    if hdv >= 11:
        if nivA3 == 13:
            Or = Or + 2100000
            Tps = Tps + 259200
            Exp = Exp + 509
            nivA3 = nivA3 + 1
        if nivA3 == 14:
            Or = Or + 3200000
            Tps = Tps + 367200
            Exp = Exp + 605
            nivA3 = nivA3 + 1
    if hdv >= 12:
        if nivA3 == 15:
            Or = Or + 4900000
            Tps = Tps + 540000
            Exp = Exp + 734
            nivA3 = nivA3 + 1
        if nivA3 == 16:
            Or = Or + 6300000
            Tps = Tps + 734400
            Exp = Exp + 856
            nivA3 = nivA3 + 1
    if hdv >= 13:
        if nivA3 == 17:
            Or = Or + 8200000
            Tps = Tps + 942000
            Exp = Exp + 985
            nivA3 = nivA3 + 1
        if nivA3 == 18:
            Or = Or + 9800000
            Tps = Tps + 1036800
            Exp = Exp + 1018
            nivA3 = nivA3 + 1
    if hdv >= 14:
        if nivA3 == 19:
            Or = Or + 16500000
            Tps = Tps + 1404000
            Exp = Exp + 1184
            nivA3 = nivA3 + 1
    if hdv >= 15:
        if nivA3 == 20:
            Or = Or + 18000000
            Tps = Tps + 1468800
            Exp = Exp + 1211
            nivA3 = nivA3 + 1
    A3 = A3 - 1
while A4 > 0:
    nivA4 = 0
    FoisA4 = FoisA4 + 1
    nivA4= int(input(f"Niveau de votre Défence Anti-Aérienne n°{FoisA4}/{A4total} --- "))
    if hdv >= 4:
        if nivA4 == 0:
            Or = Or + 22000
            Tps = Tps + 10800
            Exp = Exp + 103
            nivA4 = nivA4 + 1
        if nivA4 == 1:
            Or = Or + 90000
            Tps = Tps + 43200
            Exp = Exp + 207
            nivA4 = nivA4 + 1
    if hdv >= 5:
        if nivA4 == 2:
            Or = Or + 270000
            Tps = Tps + 57600
            Exp = Exp + 240
            nivA4 = nivA4 + 1
    if hdv >= 6:
        if nivA4 == 3:
            Or = Or + 50000
            Tps = Tps + 86400
            Exp = Exp + 293
            nivA4 = nivA4 + 1
    if hdv >= 7:
        if nivA4 == 4:
            Or = Or + 1000000
            Tps = Tps + 129600
            Exp = Exp + 360
            nivA4 = nivA4 + 1
    if hdv >= 8:
        if nivA4 == 5:
            Or = Or + 1350000
            Tps = Tps + 172800
            Exp = Exp + 415
            nivA4 = nivA4 + 1
    if hdv >= 9:
        if nivA4 == 6:
            Or = Or + 1750000
            Tps = Tps + 259200
            Exp = Exp + 509
            nivA4 = nivA4 + 1
    if hdv >= 10:
        if nivA4 == 7:
            Or = Or + 3000000
            Tps = Tps + 367200
            Exp = Exp + 587
            nivA4 = nivA4 + 1
    if hdv >= 11:
        if nivA4 == 8:
            Or = Or + 4200000
            Tps = Tps + 540000
            Exp = Exp + 734
            nivA4 = nivA4 + 1
    if hdv >= 12:
        if nivA4 == 9:
            Or = Or + 6500000
            Tps = Tps + 842400
            Exp = Exp + 917
            nivA4 = nivA4 + 1
    if hdv >= 13:
        if nivA4 == 10:
            Or = Or + 10500000
            Tps = Tps + 1036800
            Exp = Exp + 1018
            nivA4 = nivA4 + 1
    if hdv >= 14:
        if nivA4 == 11:
            Or = Or + 17000000
            Tps = Tps + 1468800
            Exp = Exp + 1211
            nivA4 = nivA4 + 1
    if hdv >= 15:
        if nivA4 == 12:
            Or = Or + 19500000
            Tps = Tps + 1555200
            Exp = Exp + 1247
            nivA4 = nivA4 + 1
    A4 = A4 - 1
while A5 > 0:
    nivA5 = 0
    FoisA5 = FoisA5 + 1
    nivA5 = int(input(f"Niveau de votre Mortier n°{FoisA5}/{A5total}"))
    if hdv >= 3:
        if nivA5 == 0:
            Or = Or + 5000
            Tps = Tps + 10800
            Exp = Exp + 103
            nivA5 = nivA5 + 1
    if hdv >= 4:
        if nivA5 == 1:
            Or = Or + 25000
            Tps = Tps + 21600
            Exp = Exp + 146
            nivA5 = nivA5 + 1
    if hdv >= 5:
        if nivA5 == 2:
            Or = Or + 100000
            Tps = Tps + 43200
            Exp = Exp + 207
            nivA5 = nivA5 + 1
    if hdv >= 6:
        if nivA5 == 3:
            Or = Or + 200000
            Tps = Tps + 86400
            Exp = Exp + 293
            nivA5 = nivA5 + 1
    if hdv >= 7:
        if nivA5 == 4:
            Or = Or + 400000
            Tps = Tps + 172800
            Exp = Exp + 415
            nivA5 = nivA5 + 1
    if hdv >= 8:
        if nivA5 == 5:
            Or = Or + 750000
            Tps = Tps + 216000
            Exp = Exp + 464
            nivA5 = nivA5 + 1
    if hdv >= 9:
        if nivA5 == 6:
            Or = Or + 1500000
            Tps = Tps + 259200
            Exp = Exp + 509
            nivA5 = nivA5 + 1
    if hdv >= 10:
        if nivA5 == 7:
            Or = Or + 2500000
            Tps = Tps + 280800
            Exp = Exp + 529
            nivA5 = nivA5 + 1
        if nivA5 == 8:
            Or = Or + 3500000
            Tps = Tps + 367200
            Exp = Exp + 605
            nivA5 = nivA5 + 1
    if hdv >= 11:
        if nivA5 == 9:
            Or = Or + 4800000
            Tps = Tps + 475200
            Exp = Exp + 689
            nivA5 = nivA5 + 1
        if nivA5 == 10:
            Or = Or + 6500000
            Tps = Tps + 734400
            Exp = Exp + 856
            nivA5 = nivA5 + 1
    if hdv >= 12:
        if nivA5 == 11:
            Or = Or + 7200000
            Tps = Tps + 842400
            Exp = Exp + 917
            nivA5 = nivA5 + 1
    if hdv >= 13:
        if nivA5 == 12:
            Or = Or + 9800000
            Tps = Tps + 1036800
            Exp = Exp + 1018
            nivA5 = nivA5 + 1
    if hdv >= 14:
        if nivA5 == 13:
            Or = Or + 16500000
            Tps = Tps + 1468800
            Exp = Exp + 1211
            nivA5 = nivA5 + 1
    if hdv >= 15:
        if nivA5 == 14:
            Or = Or + 19000000
            Tps = Tps + 1555200
            Exp = Exp + 1247
            nivA5 = nivA5 + 1
    A5 = A5 - 1
while A6 > 0:
    nivA6 = 0
    FoisA6 = FoisA6 + 1
    nivA6 = int(input(f"Niveau de votre Catapulte erratique n°{FoisA6}/{A6total}"))
    if hdv >= 13:
        if nivA6 == 0:
            Or = Or + 11200000
            Tps = Tps + 972000
            Exp = Exp + 985
            nivA6 = nivA6 + 1
        if nivA6 == 1:
            Or = Or + 12800000
            Tps = Tps + 1101600
            Exp = Exp + 1049
            nivA6 = nivA6 + 1





print(Tps)
Minutes = Tps // 60
Secondes = Tps % 60
Heures = Minutes // 60
Minutes = Minutes % 60
Jours = Heures // 24
Heures = Heures % 24
Semaines = Jours // 7
Jours = Jours % 7
print("Semaines : ", Semaines)
print("Jours : ", Jours)
print("Heures : ", Heures)
print("Minutes : ", Minutes)
print("Secondes :", Secondes)

ouvriers = int(input("Nombre d'ouvriers disponibles ?"))
JoursTT = Semaines * 7 + Jours
JoursTTos = Jours // ouvriers
JoursTToj = Jours % ouvriers
print(JoursTTos)
print(JoursTToj)
JoursTTo = JoursTTos + JoursTToj
print(Jours)
Semaines = JoursTTo // 7
Jours = JoursTTo % 7
print("Semaines : ", Semaines)
print("Jours : ", Jours)