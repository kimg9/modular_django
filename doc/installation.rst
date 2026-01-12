============
Installation
============

Prérequis
---------

* Compte GitHub avec accès en lecture au repository
* Git CLI
* SQLite3 CLI
* Interpréteur Python, version 3.6 ou supérieure

Étapes d'installation
---------------------

1. **Cloner le dépôt :**

   .. code-block:: bash

      git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git
      cd Python-OC-Lettings-FR

2. **Créer et activer l'environnement virtuel :**

   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate  # Sur Windows: .\venv\Scripts\Activate.ps1

3. **Installer les dépendances :**

   .. code-block:: bash

      pip install --requirement requirements.txt

4. **Lancer l'application :**

   .. code-block:: bash

      python manage.py runserver

L'application sera alors disponible sur http://localhost:8000. 
Vous pouvez vous connecter à l'interface d'administration avec l'utilisateur ``admin`` et le mot de passe ``Abc1234!``.