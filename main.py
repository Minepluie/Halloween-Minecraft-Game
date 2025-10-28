import os
import subprocess
import threading
import collections
import collections.abc
collections.Iterable = collections.abc.Iterable

# --- Chemin vers le dossier du serveur ---
server_dir = "server"
os.chdir(server_dir)

# --- Lancer le serveur Minecraft en arrière-plan avec flush des logs ---
server_process = subprocess.Popen(
    ["stdbuf", "-oL", "java", "-Xms512M", "-Xmx1024M", "-jar", "spigot.jar", "nogui"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True
)

# Revenir au dossier principal
os.chdir("..")
print("Serveur Minecraft lancé en arrière-plan !")

# --- Fonction qui surveille les logs et déclenche le mini-jeu ---
def monitor_server():
    mini_game_launched = False
    for line in iter(server_process.stdout.readline, ''):
        print(line, end="")  # affichage en direct
        with open(f"{server_dir}/server.log", "a") as f:
            f.write(line)

        # Détecte la première connexion d'un joueur
        if "logged in" in line and not mini_game_launched:
            print("Un joueur vient de se connecter ! Lancement du mini-jeu...")
            threading.Thread(target=launch_async_task, daemon=True).start()
            mini_game_launched = True

# --- Fonction qui lance le mini-jeu ---
def launch_async_task():
    subprocess.Popen(["python3", "Python/main.py"])

# --- Lancer le thread de surveillance ---
threading.Thread(target=monitor_server, daemon=False).start()

# --- Garder le script principal actif tant que le serveur tourne ---
try:
    server_process.wait()
except KeyboardInterrupt:
    print("Arrêt du serveur et du script principal...")
    server_process.terminate()
