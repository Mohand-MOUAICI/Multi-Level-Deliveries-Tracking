#!/usr/bin/env python3

import os
import subprocess

# Liste de commandes à exécuter
commands = [
    "sudo apt-get update",

    "sudo apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release git",

    "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg",

    """echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null""",

    "sudo apt-get update",
    "sudo apt-get install -y docker-ce docker-ce-cli containerd.io",

    "sudo docker run hello-world",

    """sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose""",
    "sudo chmod +x /usr/local/bin/docker-compose",

    "docker-compose --version",

    "git clone https://github.com/eclipse/ditto.git",
    "cd ditto/deployment/docker && docker-compose up -d",
]

# Exécute chaque commande dans l'ordre
for command in commands:
    try:
        print(f"Exécution de la commande: {command}")
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Une erreur est survenue lors de l'exécution de la commande: {command}")
        print(f"Erreur: {str(e)}")
        break

print("Installation terminée.")
