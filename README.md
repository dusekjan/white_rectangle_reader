# White Rectangle Reader
Tool schopny z dodanych obrazku vyriznout pouze bile obdelniky a slepit je pod sebe do jednoho ci vice .png souboru.
Napriklad najde v ramci print screen bile pole v nemz jsou noty/akordy a pripravi je pro tisk.

## Instalace a spuštění
1. **Vytvoření a aktivace virtuálního prostředí (venv):**

```zsh
python3 -m venv venv
source venv/bin/activate
```

2. **Instalace závislostí:**

```zsh
pip install -r requirements.txt
```

3. **Registrace kernelu pro Jupyter: (volitelné)**

```zsh
python -m ipykernel install --user --name=venv --display-name "White Rectangle Python (venv)"
```

5. **Spuštění Jupyter Notebooku:**

```zsh
jupyter notebook
```

6. **Výběr virtuálního prostředí (White Rectangle Python (venc)) skrze UI Jupyter notebooku.**

## Workflow
1. Vložte obrázky do složky `pictures/`.
2. Spusťte notebook `white_rectangle_reader.ipynb`.
3. Výsledné obrázky najdete ve složce `vysledek/`.

## Závislosti
- Pillow
- opencv-python
- Jupyter
