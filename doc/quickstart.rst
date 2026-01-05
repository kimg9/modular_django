Guide de démarrage rapide
=========================

Pour lancer l'application localement en mode développement :

1. **Appliquer les migrations :**
   .. code-block:: bash

      python manage.py migrate

2. **Créer un super-utilisateur :**
   .. code-block:: bash

      python manage.py createsuperuser

3. **Lancer le serveur :**
   .. code-block:: bash

      python manage.py runserver

L'application sera disponible sur ``http://127.0.0.1:8000/``.