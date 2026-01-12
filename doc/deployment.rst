===========
Déploiement
===========

Fonctionnement global
---------------------

Le déploiement est entièrement automatisé via **GitHub Actions**. À chaque push sur la branche ``main``, le workflow effectue les actions suivantes :

1. **Build** de l'image Docker de l'application.
2. **Push** de l'image sur le registre Docker (Docker Hub).
3. **Déploiement** de la nouvelle image sur **AWS Elastic Container Service (ECS)**.

Configuration requise
---------------------

Pour que le workflow GitHub Actions et l'application fonctionnent, vous devez configurer les variables suivantes :

1. Secrets GitHub (Settings > Secrets and variables > Actions)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ces variables sont indispensables pour que la pipeline puisse communiquer avec AWS et Docker Hub :

+-------------------------+-------------------------------------------------------+
| Secret                  | Description                                           |
+=========================+=======================================================+
| ``AWS_ACCESS_KEY_ID``   | Identifiant de la clé d'accès AWS pour le déploiement.|
+-------------------------+-------------------------------------------------------+
| ``AWS_SECRET_ACCESS_KEY``| Clé d'accès secrète AWS.                              |
+-------------------------+-------------------------------------------------------+
| ``DOCKER_USERNAME``     | Identifiant de votre compte Docker Hub.               |
+-------------------------+-------------------------------------------------------+
| ``DOCKER_PASSWORD``     | Mot de passe ou Token d'accès Docker Hub.             |
+-------------------------+-------------------------------------------------------+

2. Environnement de Production (AWS ECS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Les variables suivantes doivent être définies directement dans l'environnement d'exécution sur AWS (Task Definition) :

+-------------------+------------------------------------------------------------------------------------+
| Variable          | Description                                                                        |
+===================+====================================================================================+
| ``SENTRY_DSN``    | **Obligatoire.** URL de configuration fournie par Sentry pour le monitoring.       |
+-------------------+------------------------------------------------------------------------------------+
| ``SECRET_KEY``    | La clé secrète Django (doit être différente de celle de développement).            |
+-------------------+------------------------------------------------------------------------------------+
| ``DEBUG``         | Doit être définie sur ``0`` (False) en production.                                 |
+-------------------+------------------------------------------------------------------------------------+
| ``ALLOWED_HOSTS`` | Liste des domaines autorisés.                                                      |
+-------------------+------------------------------------------------------------------------------------+

Étapes pour effectuer le déploiement
------------------------------------

1. **Préparation :** Assurez-vous que les secrets listés ci-dessus sont bien configurés dans les paramètres du dépôt GitHub.
2. **Validation :** Vérifiez que votre code passe les tests en local (``pytest``) et respecte les normes de linting (``flake8``, ``isort``).
3. **Déclenchement :** Poussez vos modifications sur la branche principale :

.. code-block:: bash

   git push origin master

4. **Pipeline CI/CD :** Rendez-vous dans l'onglet **Actions** de GitHub pour suivre l'avancement du build puis connectez-vous à la console **AWS ECS** pour confirmer que le service a mis à jour les conteneurs (Tasks) avec la nouvelle image.

5. **Vérification finale :** Accédez à l'URL de production et vérifiez sur votre tableau de bord **Sentry** que l'application communique correctement.
