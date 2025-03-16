import os
import random
import string
import base64
from bs4 import BeautifulSoup
import re

"""Générer une chaîne aléatoire de longueur spécifiée."""
def random_string(length=10):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

"""Convertir une image en chaîne base64."""
def image_to_base64(image_path):
    try:
        print(f"Tentative de conversion en base64 de l'image : {image_path}")
        with open(image_path, 'rb') as image_file:
            image_content = image_file.read()
        return base64.b64encode(image_content).decode()
    except Exception as e:
        print(f"Erreur lors de la conversion en base64 : {e}")
        return None

print("Lecture des fichiers d'entrée...")
with open('input.html', 'r', encoding='utf-8') as f:
    html_content = f.read()
with open('input.css', 'r', encoding='utf-8') as f:
    css_content = f.read()
print("Fichiers lus avec succès.")

print("Analyse du contenu HTML...")
soup = BeautifulSoup(html_content, 'html.parser')
print("Analyse du HTML terminée.")

print("Suppression des balises <iframe>, <script>, et <link>...")
for tag in soup.find_all(['iframe', 'script']):
    tag.decompose()
for link_tag in soup.find_all('link', {'as': 'script'}):
    link_tag.decompose()
print("Suppression terminée.")

print("Traitement des images...")
images_folder = 'inputImages'  
for img_tag in soup.find_all('img', src=True):
    image_url = img_tag['src']
    image_name = os.path.basename(image_url)
    local_image_path = os.path.join(images_folder, image_name)

    if os.path.exists(local_image_path):
        img_base64 = image_to_base64(local_image_path)
        if img_base64:
            img_tag['src'] = f'data:image;base64,{img_base64}'
            # Supprimer les attributs inutiles comme 'alt', 'title', etc.
            for attr in ['alt', 'title'] + [attr for attr in img_tag.attrs if attr.startswith('data-')]:
                if attr in img_tag.attrs:
                    del img_tag[attr]
    else:
        print(f"Aucune image correspondante trouvée pour : {image_url}")
print("Traitement des images terminé.")

# Remplacer les noms de classe, id et data- dans le HTML
print("Remplacement des noms de classe, id et data- dans le HTML...")
name_mapping = {}
for tag in soup.find_all(True):
    for attr_name in ['class', 'id'] + [attr for attr in tag.attrs if attr.startswith('data-')]:
        old_names = tag.get(attr_name)
        if old_names:
            if not isinstance(old_names, list):
                old_names = [old_names]
            new_names = [name_mapping.setdefault(old_name, random_string()) for old_name in old_names]
            tag[attr_name] = ' '.join(new_names) if isinstance(old_names, list) else new_names[0]
print("Remplacement dans le HTML terminé.")

# Remplacer les noms de classe et id dans le CSS
print("Remplacement des noms de classe et id dans le CSS...")
def replacer(match):
    return '.' + name_mapping.get(match.group(1), match.group(1))

css_content = re.sub(r'\.([a-zA-Z_][a-zA-Z_0-9\-]*)', replacer, css_content)

def replacer(match):
    return '#' + name_mapping.get(match.group(1), match.group(1))

css_content = re.sub(r'#([a-zA-Z_][a-zA-Z_0-9\-]*)', replacer, css_content)
print("Remplacement dans le CSS terminé.")

# Écrire les fichiers de sortie
print("Écriture des fichiers de sortie...")
with open('output.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
with open('output.css', 'w', encoding='utf-8') as f:
    f.write(css_content)
print("Écriture terminée. Les noms ont été remplacés et les images traitées avec succès !")
