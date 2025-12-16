import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time

# Connexion à Minecraft
mc = minecraft.Minecraft.create()
mc.player.setPos(0,0,0)
mc.postToChat("Chasse aux bonbons lancée !")

# --- Liste de toutes les coordonnées possibles ---
coord_list = [
    (-38, 0, -7), (-34, 0, -12), (-34, 0, 5), (-28, 0, 6),
    (-22, 0, 10), (-22, 0, -7), (-16, 0, -5), (-28, 21, 5),
    (-17, 21, 10), (-26, 21, 5), (-27, 21, -6), (-19, 21, -10),
    (-24, 10, -5), (-25, 11, 7), (-32, 14, -9), (-20, 0, 10),
    (-16, 0, -8), (-18, 9, -5), (-11, 10, 5), (-14, 10, 0),
    (-19, 21, -6), (-11, 21, -4)
]

# --- Choisit aléatoirement des positions uniques ---
coord = random.sample(coord_list, 10)
total_bonbons = len(coord)

# --- Enlève tous les anciens blocs sur ces positions ---
for x, y, z in coord_list:
    mc.setBlock(x, y, z, block.AIR)

# --- Place les bonbons (panneaux à trouver) ---
for x, y, z in coord:
    mc.setBlock(x, y, z, block.SIGN_STANDING)

# --- Variables de jeu ---
visited_coords = []
nbr_bonbon = 0
find_all = False

# --- Boucle principale du jeu ---
while True:
    pos = mc.player.getTilePos()
    current_pos = (pos.x, pos.y, pos.z)

    # Si le joueur trouve un bonbon
    if current_pos in coord and current_pos not in visited_coords:
        mc.setBlock(pos.x, pos.y, pos.z, block.AIR)
        mc.postToChat("Bonbon récupéré !")
        visited_coords.append(current_pos)
        coord.remove(current_pos)
        nbr_bonbon += 1

    # Si tous les bonbons sont trouvés
    if nbr_bonbon == total_bonbons and not find_all:
        mc.postToChat("Vous avez tout trouvé !")
        find_all = True

    # Condition de victoire (porte magique)
    if pos.x == -27 and pos.y == 21 and (pos.z == 2 or pos.z == 3) and find_all:
        mc.postToChat("Tu as gagné ! Félicitations")
        mc.player.setPos(-30, 0, 16)
        break

    time.sleep(0.1)
