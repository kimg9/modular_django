Déploiement et Gestion
======================

L'application est conteneurisée et déployée sur **AWS ECS (Elastic Container Service)**.

Infrastructure
--------------
* **Registre :** Amazon ECR (Elastic Container Registry) pour stocker les images Docker.
* **Service :** AWS ECS avec le type de lancement **Fargate** (Serverless).
* **Load Balancer :** Un ALB (Application Load Balancer) distribue le trafic.

Procédure de mise à jour
------------------------
1. Builder l'image Docker localement ou via CI.
2. Pousser l'image sur Amazon ECR.
3. Créer une nouvelle révision de la *Task Definition*.
4. Mettre à jour le service ECS pour déployer la nouvelle tâche.