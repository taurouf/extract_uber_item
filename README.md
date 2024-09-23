# Menu Extraction Script

## Description

Ce projet contient un script Python pour extraire des informations à partir de pages web, telles que les URLs d'images et d'autres données HTML. Il permet de télécharger le contenu d'une page web, d'extraire des images ou d'autres éléments, et de sauvegarder les résultats dans des fichiers CSV ou JSON.

### Fonctionnalités :
- Télécharge le contenu HTML d'une page web à partir d'une URL donnée.
- Extrait les URLs d'images présentes sur la page (y compris celles encodées en Base64).
- Sauvegarde les données extraites dans des fichiers au format CSV ou JSON.
- Gestion des erreurs et des requêtes HTTP avec `try-except`.

## Prérequis

Avant d'utiliser ce script, assurez-vous que vous avez Python 3 installé sur votre machine. Le script nécessite les bibliothèques suivantes :

- **requests** : pour envoyer des requêtes HTTP et télécharger les pages web.
- **beautifulsoup4** : pour analyser et extraire les informations des fichiers HTML.

## Installation

1. Clonez ce dépôt ou téléchargez le fichier `menu-extraction-script.py`.
2. Installez les dépendances nécessaires en utilisant `pip`. Exécutez la commande suivante dans votre terminal :

    ```bash
    pip install requests beautifulsoup4
    ```

## Utilisation

1. Modifiez l'URL dans le script pour spécifier la page que vous souhaitez télécharger et analyser. Vous pouvez modifier l'appel à la fonction `download_html()` pour indiquer l'URL de votre choix :

    ```python
    download_html('https://example.com', 'page.html')
    ```

2. Ensuite, exécutez le script en utilisant la commande suivante :

    ```bash
    python menu-extraction-script.py
    ```

3. Les fichiers extraits (comme le fichier HTML ou les données CSV/JSON) seront enregistrés dans le répertoire courant.

### Options personnalisées

- **Modification des éléments à extraire** :
    - Par défaut, le script est configuré pour extraire les URLs des images. Si vous souhaitez extraire d'autres types de données (comme du texte ou des liens), vous pouvez ajuster la logique de parsing avec `BeautifulSoup`. Modifiez les sélecteurs de balises HTML dans la fonction `extract_image_url()`.

- **Sauvegarde des données** :
    - Les données extraites peuvent être sauvegardées dans différents formats (CSV ou JSON). Assurez-vous d'adapter les appels aux fonctions d'écriture des fichiers selon vos besoins.

## Exemple d'exécution

Pour télécharger une page et extraire les URLs des images, voici un exemple simple d'utilisation :

```bash
python menu-extraction-script.py
```

Le script téléchargera le fichier HTML à partir de l'URL que vous avez indiquée et sauvegardera les résultats dans un fichier CSV ou JSON.

## Structure du Projet

Le script contient les fonctions suivantes :

- `download_html(url, filename)` : Télécharge le contenu d'une page web et l'enregistre dans un fichier.
- `extract_image_url(item, base_url)` : Extrait l'URL des images, même si elles sont encodées en Base64.
- **Autres fonctions** : Vous pouvez ajouter ou personnaliser des fonctions pour extraire d'autres types d'éléments HTML.

## Gestion des erreurs

Le script utilise des blocs `try-except` pour capturer les erreurs liées aux requêtes HTTP, comme les erreurs de connexion ou les URL invalides. En cas d'échec de téléchargement ou d'extraction, un message d'erreur approprié sera affiché.

## Auteurs

- **Votre Nom** - Développeur principal du script.

## Licence

Ce projet est sous licence libre (vous pouvez indiquer la licence de votre choix, ex : MIT, GPL, etc.).

---

Tu peux adapter ce **README** pour inclure plus de détails spécifiques à ton projet ou pour fournir plus d'exemples d'utilisation si besoin. Si tu as besoin de clarifications supplémentaires ou d'ajouter quelque chose, n'hésite pas !
