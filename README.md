# BackDoor


Ce projet est une implémentation simple d'une backdoor en Python, permettant à un utilisateur distant d'exécuter des commandes sur un ordinateur cible à distance.

## Fonctionnalités

- **Connexion client-serveur:** Le projet utilise des sockets pour établir une connexion entre un client et un serveur, permettant ainsi la communication bidirectionnelle.
- **Exécution de commandes système:** Le serveur peut recevoir des commandes de la part du client et les exécuter sur l'ordinateur cible. Cela permet à l'utilisateur distant de contrôler l'ordinateur à distance.
- **Fonctionnalités supplémentaires:**
  - Le serveur peut récupérer des informations système telles que la plateforme et le répertoire actuel.
  - Le serveur peut changer de répertoire de travail sur l'ordinateur cible.
  - Le serveur peut télécharger des fichiers de l'ordinateur cible.
  - Le serveur peut capturer des captures d'écran de l'ordinateur cible.

## Structure du projet

Le projet est composé de deux fichiers Python :
- `serveur.py`: Le code du serveur qui s'exécute sur l'ordinateur cible. Il attend les connexions entrantes des clients et exécute les commandes reçues.
- `client.py`: Le code du client qui s'exécute sur l'ordinateur de l'utilisateur distant. Il se connecte au serveur et envoie des commandes à exécuter.

## Utilisation

1. **Exécuter le serveur :**
   - Exécutez le fichier `serveur.py` sur l'ordinateur cible en utilisant Python.
   - Assurez-vous que le port spécifié dans le fichier est accessible depuis l'extérieur si vous prévoyez d'accéder à distance.

2. **Exécuter le client :**
   - Exécutez le fichier `client.py` sur l'ordinateur de l'utilisateur distant en utilisant Python.
   - Spécifiez l'adresse IP et le port du serveur auquel vous souhaitez vous connecter.

3. **Envoyer des commandes :**
   - Une fois connecté, vous pouvez envoyer des commandes au serveur depuis le client en utilisant la syntaxe appropriée.
   - Par exemple, vous pouvez taper `ls` pour lister les fichiers dans le répertoire actuel, `cd <répertoire>` pour changer de répertoire, `dl <fichier>` pour télécharger un fichier, ou `capture <nom>` pour capturer un écran.

4. **Fermer la connexion :**
   - Pour quitter la session, vous pouvez fermer le client et le serveur en appuyant sur Ctrl+C ou en fermant les fenêtres de console.

## Sécurité

Il est important de noter que ce projet est à des fins éducatives et de recherche uniquement. L'utilisation de cette backdoor sans consentement approprié peut violer les lois sur la vie privée et la sécurité informatique. Assurez-vous d'utiliser ce projet uniquement de manière légale et éthique, et avec le consentement explicite des parties concernées.

## Contributions

Les contributions sous forme de suggestions, de rapports de bogues ou de demandes de fonctionnalités sont les bienvenues. N'hésitez pas à ouvrir une issue ou à soumettre une pull request sur GitHub.

