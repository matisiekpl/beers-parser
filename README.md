# Beers Parser 🍺
Beer styles parser for wiki.piwo.org

## Goal
The goal is to automatically fetch beer styles from https://wiki.piwo.org/Zestawienie_styl%C3%B3w_piw_(tabela) into useful `JSON` file

## Example
```json
{
  "name": "Lite American Lager",
  "og_min": 1.028,
  "og_max": 1.04,
  "fg_min": 0.998,
  "fg_max": 1.008,
  "ibu_min": 8.0,
  "ibu_max": 12.0,
  "srm_min": 2.0,
  "srm_max": 3.0,
  "abv_min": 2.8,
  "abv_max": 4.2,
  "sections": [
    {
      "label": "Aromat",
      "value": "Brak ,albo bardzo delikatny zapach słodowy, aczkolwiek może występować zapach zbożowy, słodki albo kukurydzany. Aromat chmielowy może występować w przedziale od braku zapachu do delikatnego zapachu chmielowego, obecność chmielowych zapachów korzenny (spicy) albo kwiatowych. Niski poziom wpływu zapachów drożdżowych (zielone jabłka, [[DMS]], albo owocowych)  są opcjonalne, ale akceptowane. Brak [[diacetyl|dwuacetylu]]."
    },
    {
      "label": "Wygląd",
      "value": "Od bardzo blado słomkowego do blado żółtego koloru. Biała gęsta piana, krótko utrzymująca się. Bardzo  klarowne."
    }
  ]
}
```

## Runing
```bash
git clone https://github.com/matisiekpl/beers-parser.git
cd beers-parser
pip install -r requirements.txt
python main.py # dumps beers list into beers.json
```
