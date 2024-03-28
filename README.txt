Pour l'installation, ouvrez le terminal ou l'invite de commande de votre ordinateur.

Vérifier que python3 soit installé et dans la bonne version:
> python3 -V
La réponse doit être:
Python 3.9.5

Sinon installer python

Ensuite vérifier que le module pyinstaller soit installé:
> pip3 list
Une liste de module va s'afficher, si vous ne trouver pyinstaller installez le:
> pip3 install pyinstaller

Ensuite aller à l'emplacement où ce fichier et installer l'application:
> pyinstaller CryptageHuffman.py --onefile

Voilà vous pouvez lancer votre application qui se trouve dans le fichier dist.