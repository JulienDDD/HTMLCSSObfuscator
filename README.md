# README - HTMLCSS Obfuscator

## Description

Ce script a été développé il y a environ 5 ans pour des projets personnels. Il permet de traiter des fichiers HTML et CSS en effectuant plusieurs opérations :

- Lecture et analyse du contenu HTML
- Suppression des balises `<iframe>`, `<script>` et `<link>`
- Conversion des images locales en base64 pour une intégration directe dans le HTML
- Remplacement des noms de classes, d'identifiants (`id`) et des attributs `data-` dans le HTML et CSS par des chaînes aléatoires

## Prérequis

Avant d'exécuter ce script, assurez-vous d'avoir installé les dépendances nécessaires. Ce script utilise les bibliothèques suivantes :

- `beautifulsoup4`

Vous pouvez les installer avec la commande :

```bash
pip install beautifulsoup4
```

## Utilisation

1. Placez vos fichiers d'entrée (`input.html` et `input.css`) dans le même répertoire que le script.
2. Assurez-vous que les images référencées dans le HTML sont situées dans un dossier `inputImages`.
3. Exécutez le script avec :

```bash
python script.py
```

4. Les fichiers modifiés seront générés sous les noms `output.html` et `output.css`.

## Fonctionnalités détaillées

- **Lecture des fichiers** : Le script ouvre et lit les fichiers `input.html` et `input.css`.
- **Suppression des balises sensibles** : Élimine les `<iframe>`, `<script>` et certaines `<link>`.
- **Encodage des images en base64** : Convertit les images locales en format base64 pour un affichage inline.
- **Anonymisation des classes et identifiants** : Remplace les noms de classes, identifiants et attributs `data-` par des chaînes aléatoires dans le HTML et le CSS.

## Notes

Ce script a été initialement conçu pour des projets personnels et n'a pas été maintenu ou mis à jour récemment. Il peut nécessiter des ajustements selon les besoins actuels.

## Auteur

Julien Das Dores

## Licence

Aucune licence spécifique, utilisation libre mais sans garantie.

