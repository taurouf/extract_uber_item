from urllib.parse import urljoin
import requests
import re
import json
import csv
from bs4 import BeautifulSoup
import traceback

def download_html(url, filename='page.html'):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Vérifie si la requête a réussi
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f"Le contenu HTML a été téléchargé avec succès depuis {url}.")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors du téléchargement de la page : {e}")
        return False

def extract_image_url(item, base_url):
    """
    Fonction pour extraire l'URL de l'image, en tenant compte des images encodées en Base64 avec srcb64.
    """
    image_tag = item.find('img')
    if image_tag:
        # Chercher les attributs courants et spécifiques au lazy loading
        image_url = image_tag.get('src') or image_tag.get('data-src') or image_tag.get('data-lazy') or image_tag.get('data-original')

        # Gestion des images encodées avec srcb64
        if image_url and 'srcb64=' in image_url:
            # Construit l'URL complète pour Uber Eats en tenant compte du pattern d'Uber Eats
            image_url = urljoin(base_url, image_url)
        elif image_url and not image_url.startswith('http'):  # Si c'est une URL relative
            image_url = urljoin(base_url, image_url)  # Compléter l'URL avec la base URL

        return image_url
    return ''

def extract_menu_items(html_content, base_url):
    soup = BeautifulSoup(html_content, 'html.parser')
    script_tag = soup.find('script', type='application/ld+json')
    if not script_tag:
        print("Aucune balise script avec application/ld+json trouvée.")
        return []

    try:
        json_data = json.loads(script_tag.string)
        print("Données JSON extraites avec succès.")
    except json.JSONDecodeError:
        print("Erreur lors du décodage JSON. Contenu de la balise script:")
        print(script_tag.string)
        return []

    menu_sections = json_data.get('hasMenu', {}).get('hasMenuSection', [])
    if not menu_sections:
        print("Aucune section de menu trouvée dans les données JSON.")
        print("Structure JSON:")
        print(json.dumps(json_data, indent=2))
        return []

    menu_items = []
    for section in menu_sections:
        section_name = section.get('name', '')
        items = section.get('hasMenuItem', [])
        for item in items:
            name = item.get('name', '')
            description = item.get('description', '')
            price = item.get('offers', {}).get('price', '')
            image_url = item.get('image', '')

            # Si l'image URL est vide, on cherche l'image potentiellement dans une balise lazy-loaded ou avec srcb64
            if not image_url:
                image_url = extract_image_url(soup, base_url)

            menu_items.append({
                'name': name,
                'tags': section_name,
                'description': description,
                'price': price,
                'image_url': image_url
            })

    print(f"Nombre d'éléments de menu extraits : {len(menu_items)}")
    return menu_items

def save_to_csv(menu_items, filename='menu_items.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'tags', 'description', 'price', 'image_url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for item in menu_items:
            writer.writerow(item)

try:
    url = input("Entrez l'URL de la page : ")
    
    # Télécharger le contenu HTML de l'URL
    if download_html(url):
        # Lire le contenu HTML du fichier téléchargé
        with open('page.html', 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Extraire les éléments du menu en utilisant l'URL de base
        menu_items = extract_menu_items(html_content, url)

        if menu_items:
            # Sauvegarder les résultats dans un fichier CSV
            save_to_csv(menu_items)
            print(f"Extraction terminée. {len(menu_items)} éléments de menu ont été extraits et sauvegardés dans menu_items.csv")
        else:
            print("Aucun élément de menu n'a été extrait.")
    else:
        print("Échec du téléchargement de la page.")

except Exception as e:
    print("Une erreur inattendue s'est produite:")
    print(traceback.format_exc())
