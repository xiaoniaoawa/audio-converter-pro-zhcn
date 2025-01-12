
# Convertisseur Audio (.m4a en .mp3)

Ce projet a pour objectif de convertir des fichiers audio au format `.m4a` en `.mp3` en utilisant **Python** et la bibliothèque **pydub** (qui dépend de ffmpeg).

---

## Index
- [Prérequis](#prérequis)
- [Installation](#installation)
  - [Configurer un environnement virtuel](#configurer-un-environnement-virtuel)
- [Utilisation](#utilisation)
  - [Exemple de conversion d'un fichier](#exemple-de-conversion-dun-fichier)
  - [Exemple de conversion de plusieurs fichiers dans un répertoire](#exemple-de-conversion-de-plusieurs-fichiers-dans-un-répertoire)
- [Journaux et barre de progression](#journaux-et-barre-de-progression)
- [Autres remarques](#autres-remarques)
- [Contribuer](#contribuer)
- [Licence](#licence)

---

## Prérequis

- Python 3.8 ou version ultérieure
- ffmpeg installé sur le système :

### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

### Windows
- Téléchargez-le depuis le [site officiel de ffmpeg](https://ffmpeg.org/) ou utilisez le gestionnaire **Chocolatey**.
- Assurez-vous que l'exécutable `ffmpeg` est dans votre PATH.

### macOS
```bash
brew install ffmpeg
```

---

## Installation

Clonez le dépôt (ou téléchargez le ZIP) :
```bash
git clone https://github.com/usuario/audio-converter-pro-pro.git
```

Naviguez jusqu'au dossier du projet :
```bash
cd audio-converter-pro-pro
```

### Dépendances Python

Installez les dépendances depuis `requirements.txt` :
```bash
pip install -r requirements.txt
```

Les principales dépendances sont :
- **pydub** – bibliothèque Python facilitant les opérations audio.
- Autres listées dans `requirements.txt`.

---

### Configurer un environnement virtuel

Il est recommandé de créer et d'activer un environnement virtuel avant d'installer les dépendances (pour éviter les conflits avec d'autres bibliothèques installées globalement).

```bash
python -m venv venv
```

Activez l'environnement virtuel :

- **Linux/Mac** :
    ```bash
    source venv/bin/activate
    ```
- **Windows** :
    ```bash
    venv\Scripts\activate
    ```

Ensuite, installez les dépendances dans l'environnement virtuel :
```bash
pip install -r requirements.txt
```

---

## Utilisation

Le script principal de ce projet est `convert_m4a_to_mp3.py`, qui peut être exécuté directement via la ligne de commande.

Il accepte comme arguments :
1. `<input_path>` : Chemin vers un fichier `.m4a` ou un répertoire contenant plusieurs fichiers `.m4a`.
2. `[output_directory]` (optionnel) : Répertoire où seront générés les fichiers `.mp3`.

### Exemple de conversion d'un fichier

Dans le même dossier :
```bash
python convert_m4a_to_mp3.py "C:\musics\track1.m4a"
```

Vers un répertoire de destination spécifique :
```bash
python convert_m4a_to_mp3.py "C:\musics\track1.m4a" "C:\output_mp3"
```

### Exemple de conversion de plusieurs fichiers dans un répertoire

Dans le même dossier :
```bash
python convert_m4a_to_mp3.py "C:\musics"
```

Vers un autre répertoire :
```bash
python convert_m4a_to_mp3.py "C:\musics" "C:\output_mp3"
```

---

## Journaux et barre de progression

Le script affiche :
- **Barre de progression** : affiche l'indice du fichier actuel, le nombre total de fichiers et le pourcentage complété.
- Nom du fichier d'entrée et du fichier de sortie généré (ou erreur, en cas d'échec).
- Temps de traitement de chaque fichier (en secondes).
- **Résumé final** : total des réussites, des échecs et du temps d'exécution total.

### Exemple de sortie :
```
Démarrage de la conversion de 3 fichier(s) .m4a dans 'C:\musics'...

[1/3] |█████--------------|  33.3%  track1.m4a -> track1.mp3 : OK | temps : 2.37s
[2/3] |██████████---------|  66.7%  track2.m4a -> track2.mp3 : OK | temps : 3.10s
[3/3] |██████████████████-| 100.0%  track3.m4a -> ERREUR: ...

Conversion terminée !
 - Réussites : 2
 - Échecs    : 1
 - Total     : 3
Temps total d'exécution : 12.45s.
```

---

## Autres remarques

- Si vous rencontrez des problèmes avec les barres inversées (`\`), utilisez des guillemets pour les chemins contenant des espaces ou des caractères spéciaux.
- Si vous souhaitez des extensions différentes ou un autre format de sortie, vous pouvez adapter le code pour utiliser :
    ```python
    AudioSegment.from_file(input_file, format="m4a").export(output_file, format="mp3")
    ```
    Avec d'autres paramètres (bitrate, canaux, etc.).

---

## Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir des **issues** ou à envoyer des **pull requests**.

1. Forkez le projet.
2. Créez une branche pour votre contribution :
    ```bash
    git checkout -b feature/votre-contribution
    ```
3. Validez vos modifications :
    ```bash
    git commit -m "Ajout d'une nouvelle fonctionnalité"
    ```
4. Poussez la branche :
    ```bash
    git push origin feature/votre-contribution
    ```
5. Ouvrez une **Pull Request** en expliquant la modification proposée.

---

## Licence

Ce projet est distribué sous la licence MIT. Vous êtes libre de l'utiliser, le modifier et le distribuer.

**Auteur** : Lucas Albuquerque
**Contact** : lucas.albuquerque.gk@gmail.com
