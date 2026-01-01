# sd-artist-wildcards
Artist Wildcards Script for Stable Diffusion A1111/Forge WebUI

# Artist Wildcards (WebUI Forge)

A lightweight WebUI Forge / A1111 script that randomly selects artist tags from a comma-separated list, optionally applies weights, and appends the result directly to your prompt at generation time.

---

## ✨ Features

- Randomly selects a configurable number of artists
- Optional per-artist weighting `(artist:weight)`
- Automatic weight normalization (caps total at 2.0)
- Deterministic results via seed control
- Works in **txt2img** and **img2img**
- No prompt syntax hacks or wildcards required

---

## 📦 Installation

1. Navigate to your WebUI Forge install directory: webui_forge/scripts/
2. Download and save `batman_artist_wildcards.py` to this folder
3. **Fully restart** WebUI Forge (close and relaunch the program).

---

## 🧭 Where to Find It

- Open **txt2img** or **img2img**
- Scroll to the **bottom of the page**
- Expand the section titled: Artist Wildcards

---

## 🛠 Usage

### Inputs

- **Artist Tags**  
Comma-separated list of artists  
    - The file `Danbooru Artists.xlsx` contains a comprehensive lists of artists you can use to get started

- **Min Artists / Max Artists**  
Controls how many artists are randomly selected.

- **Random Weights**  
If enabled, each artist receives a random weight.

- **Min / Max Weight**  
Range for generated weights.

- **Seed**
- `-1` = random every run
- Any other number = deterministic output

---


This string is automatically appended to your existing prompt.

---

## ⚠ Notes

- If no artists are provided, the script does nothing.
- Weight normalization prevents extreme over-biasing.
- Script does not modify negative prompts.


