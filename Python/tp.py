from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

while True:
    # Récupère les nouveaux messages du chat
    posts = mc.events.pollChatPosts()
    for post in posts:
        msg = post.message.strip()
        
        # Si le message commence par "!tp"
        if msg.startswith("!tp"):
            try:
                # Ex: "!tp -16 0 -8"
                _, x, y, z = msg.split()
                x, y, z = int(x), int(y), int(z)
                
                # Téléporte le joueur à la position donnée
                mc.player.setTilePos(x, y, z)
                mc.postToChat(f"🎃 Téléporté à ({x}, {y}, {z}) !")
            
            except ValueError:
                mc.postToChat("❌ Utilise la commande comme ceci : !tp x y z")
    
    sleep(0.1)
