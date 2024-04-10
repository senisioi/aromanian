'''
Several ways of writing Aromanian

- DIARO / stc: [ăâî/d̦/ľ/ń/ș/ț], Caragiu-Marioțeanu
- bal: [ăâî/dz/ľ/ń/ș/ț], Iancu Ballamaci
- cun: [ããã/dz/lj/nj/sh/ts], Tiberiu Cunia
- wikipedia: [l'] instead of [ľ] 
- book: [ăâ/ddz/l’/ñ/ș/ț]
- extra symbols: [dh/ δ, th/ θ, gh/ γ]

- DIARO standard: [a/ A, ă/ Ă, â/ Â, e/ E, i/ I, o/ O, u/ U; b/ B, c/ C, d/ D, d/ D, f/ F, g/ G, h/
H, j/ J, l/ L, ľ/ Ľ, m/ M, n/ N, ń/ Ń, p/ P, r/ R, s/ S, ş/ Ş, t/ T, ț, Ț, v/ V, y/ Y, z/ Z]
'''

import sys

# order does not matter here
book2DIARO = [
    ("dz",   "d̦"),
    ("Dz",   "D̦"),
    ("l'",   "ľ"),
    ("l’",   "ľ"),
    ("L'",   "Ľ"),
    ("L’",   "Ľ"),
    ("ñ",    "ń"),
    ("ş",    "ș"),
    ("ţ",    "ț"),
    ("Ş",    "Ș"),
    ("Ţ",    "Ț"),
    ("γ",    "y"),
    ("Γ",    "Y"),
    ]

book2cunia = [
    ("Ă",   "Ã"),
    ("Î",   "Ã"),
    ("î",   "ã"),
    ("ă",   "ã"),
    ("Â",   "Ã"),
    ("â",   "ã"),
    ("l'",   "lj"),
    ("l’",   "lj"),
    ("L'I",   "LJI"),
    ("L’I",   "LJI"),
    ("L'",   "Lj"),
    ("L’",   "Lj"),
    ("ñ",    "nj"),
    ("ş",    "sh"),
    ("ţ",    "ts"),
    ("ŞI",    "SHI"),
    ("Ş",    "Sh"),
    ("Ţ",    "Ts"),
    ("ș",    "sh"),
    ("ț",    "ts"),
    ("Ș",    "Sh"),
    ("Ț",    "Ts"),
    ("γ",    "y"),
    ("Γ",    "Y"),
    ]

book2Greek = [
    ("ge",   "τζε"),
    ("Ge",   "Τζε"),
    ("gi",   "τζι"),
    ("Gi",   "Τζι"),
    ("ce",   "τσε"),
    ("Ce",   "Τσε"),
    ("ci",   "τσι"),
    ("Ci",   "Τσι"),
    ("ch",   "κ"),
    ("Ch",   "Κ"),
    ("gh",   "γ"),
    ("Gh",   "Γ"),
    ("dh",   "δ"),
    ("Dh",   "Δ"),
    ("th",   "θ"),
    ("Th",   "Θ"),
    ("l'",   "λ"),
    ("l’",   "λ"),
    ("L'",   "Λ"),
    ("L’",   "Λ"),
    ("u",    "ου"),
    ("U",    "Ου"),
    ("ñ",    "ν"),
    ("ş",    "σ"),
    ("ţ",    "τσ"),
    ("Ş",    "Σ"),
    ("Ţ",    "Τσ"),
    ("a",    "α"),
    ("A",    "Α"),
    ("ă",    "α"),
    ("Ă",    "Α"),
    ("â",    "α"),
    ("Â",    "Α"),
    ("e",    "ε"),
    ("E",    "Ε"),
    ("i",    "ι"),
    ("I",    "Ι"),
    ("o",    "ο"),
    ("O",    "Ο"),
    ("u",    "υ"),
    ("U",    "Υ"),
    ("b",    "β"),
    ("B",    "Β"),
    ("c",    "κ"),
    ("C",    "Κ"),
    ("d",    "δ"),
    ("D",    "Δ"),
    ("f",    "φ"),
    ("F",    "Φ"),
    ("g",    "γ"),
    ("G",    "Γ"),
    ("h",    "χ"),
    ("H",    "Χ"),
    ("j",    "ζ"),
    ("J",    "Ζ"),
    ("l",    "λ"),
    ("L",    "Λ"),
    ("m",    "μ"),
    ("M",    "Μ"),
    ("n",    "ν"),
    ("N",    "Ν"),
    ("ń",    "ν"),
    ("Ń",    "Ν"),
    ("p",    "π"),
    ("P",    "Π"),
    ("r",    "ρ"),
    ("R",    "Ρ"),
    ("s",    "σ"),
    ("S",    "Σ"),
    ("ș",    "σ"),
    ("Ș",    "Σ"),
    ("t",    "τ"),
    ("T",    "Τ"),
    ("ț",    "τσ"),
    ("Ț",    "Τσ"),
    ("v",    "β"),
    ("V",    "Β"),
    ("y",    "ι"),
    ("Y",    "Ι"),
    ("z",    "ζ"),
    ("Z",    "Ζ"),
    ("j",    "ζ"),
    ]

# to improve
cunia2DIARO = [
    ("Ã",   "Î"),
    ("ã",   "î"),
    ("lj",   "ľ"),
    ("Lj'",  "Ľ"),
    ("nj",   "ń"),
    ("sh",   "ș"),
    ("ts",   "ț")
    ]


def replace(text, maps):
    for pair in maps:
        text = text.replace(pair[0], pair[1])
    return text


def apply(in_fis, mapping, suffix):
    with open(in_fis, 'r', encoding='utf-8') as fin:
        text = fin.read()
    replaced = replace(text, mapping)
    out_fis = in_fis + "_" + suffix
    with open(out_fis, 'w', encoding='utf-8') as fout:
        fout.write(replaced)


mapping = {"book2DIARO": book2DIARO, "book2Greek": book2Greek, "book2cunia": book2cunia}

print('run as python book2DIARO.py "path_to_data" "mapping" "suffix [std, greek, cunia]" ')
print(f"mappings {mapping.keys()}")


apply(in_fis=sys.argv[1], mapping=mapping[sys.argv[2]], suffix=sys.argv[3])
print('Done!')


#apply(in_fis = 'dataset/unsplit/corpus.rup.rup', mapping=book2DIARO, suffix = 'std')
#apply(in_fis = 'dataset/unsplit/corpus.rup.rup', mapping=book2Greek, suffix = 'greek')
#apply(in_fis = 'dataset/unsplit/corpus.rup.rup', mapping=book2cunia, suffix = 'cunia')

#apply(in_fis = 'dataset/unsplit/all.ro-rup', mapping=book2DIARO, suffix = 'std')
#apply(in_fis = 'dataset/unsplit/corpus.rup', mapping=book2DIARO, suffix = 'std')
#apply(in_fis = 'dataset/Tales.test.rup', mapping=book2DIARO, suffix = 'std')
#apply(in_fis = 'dataset/Tales.valid.rup', mapping=book2DIARO, suffix = 'std')
#apply(in_fis = 'dataset/Tales.train.rup', mapping=book2DIARO, suffix = 'std')

#apply(in_fis = 'dataset/unsplit/all.ro-rup', mapping=book2cunia, suffix = 'cun')
#apply(in_fis = 'dataset/unsplit/corpus.rup', mapping=book2cunia, suffix = 'cun')
#apply(in_fis = 'dataset/Tales.test.rup', mapping=book2cunia, suffix = 'cun')
#apply(in_fis = 'dataset/Tales.valid.rup', mapping=book2cunia, suffix = 'cun')
#apply(in_fis = 'dataset/Tales.train.rup', mapping=book2cunia, suffix = 'cun')
