import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

while True:
    if mc.events.pollChatPosts():
        pos = mc.player.getTilePos()
        mc.postToChat(f"{pos.x,pos.y,pos.z}")
        print(f"{pos.x,pos.y,pos.z}")
