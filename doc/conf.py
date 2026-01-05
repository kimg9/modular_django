# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


project = 'django_oc_lettings'
copyright = '2026, Kim Gemo, OpenClassrooms, Guy King, Colin Meldrum, Ranga Gonnage'
author = 'Kim Gemo, OpenClassrooms, Guy King, Colin Meldrum, Ranga Gonnage'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Automatic génération of models docs ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
import os
import sys
import django

# -- Configuration du chemin vers le code source ---------------------------
# On remonte d'un niveau pour atteindre la racine du projet Django
sys.path.insert(0, os.path.abspath('..'))

# On indique à Sphinx quel fichier settings utiliser
os.environ['DJANGO_SETTINGS_MODULE'] = 'oc_lettings_site.settings'

# On initialise Django pour que Sphinx puisse importer les modèles/vues
django.setup()

# -- Configuration générale ------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',      # Génère la doc à partir des docstrings
    'sphinx.ext.viewcode',     # Ajoute des liens vers le code source
    'sphinx.ext.napoleon',     # Supporte le style Google/NumPy pour les docstrings
    'sphinx.ext.githubpages',  # Utile pour le déploiement sur GitHub Pages
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

