import pandas as pd

mushrooms_og = pd.read_csv('mushroom.csv')
mushrooms_renamed = mushrooms_og.copy()

#drop 
mushrooms_renamed = mushrooms_renamed.drop(columns=['gill-color'])
mushrooms_renamed = mushrooms_renamed.drop(columns=['stem-surface'])
mushrooms_renamed = mushrooms_renamed.drop(columns=['stem-color'])
mushrooms_renamed = mushrooms_renamed.drop(columns=['veil-color'])
mushrooms_renamed = mushrooms_renamed.drop(columns=['spore-print-color'])

#replacements
mushrooms_renamed['class'] = mushrooms_renamed['class'].replace({
    'e': 1, 
    'p': 0
})

mushrooms_renamed['cap-shape'] = mushrooms_renamed['cap-shape'].replace({
    'b': 'bell', 
    'c': 'conical',
    'x': 'convex',
    'f': 'flat',
    's': 'sunken',
    'p': 'spherical',
    'o': 'others'
})

mushrooms_renamed['cap-surface'] = mushrooms_renamed['cap-surface'].replace({
    'i': 'fibrous', 
    'g': 'grooves', 
    'y': 'scaly', 
    's': 'smooth',
    'd': 'dry', 
    'h': 'shiny', 
    'l': 'leathery', 
    'k': 'silky',
    't': 'sticky', 
    'w': 'wrinkled', 
    'e': 'fleshy'
})

mushrooms_renamed['cap-color'] = mushrooms_renamed['cap-color'].replace({
    'n': 'brown', 
    'b': 'buff', 
    'g': 'gray', 
    'r': 'green', 
    'p': 'pink', 
    'u': 'purple', 
    'e': 'red', 
    'w': 'white',
    'y': 'yellow', 
    'l': 'blue', 
    'o': 'orange', 
    'k': 'black'
})

mushrooms_renamed['does-bruise-or-bleed'] = mushrooms_renamed['does-bruise-or-bleed'].replace({
    't': 1,
    'f': 0
})

mushrooms_renamed['gill-attachment'] = mushrooms_renamed['gill-attachment'].replace({
    'a': 'adnate',
    'x': 'adnexed',
    'd': 'decurrent',
    'e': 'free',
    's': 'sinuate',
    'p': 'pores',
    'f': 'none',
    '?': 'unknown'
})

mushrooms_renamed['gill-spacing'] = mushrooms_renamed['gill-spacing'].replace({
    'c': 'close',
    'd': 'distant',
    'f': 'none'
})

mushrooms_renamed['stem-root'] = mushrooms_renamed['stem-root'].replace({
    'b': 'bulbous',
    's': 'swollen',
    'c': 'club', 
    'u': 'cup',
    'e': 'equal',
    'z': 'rhizomorphs',
    'r': 'rooted'
})

mushrooms_renamed['veil-type'] = mushrooms_renamed['veil-type'].replace({
    'p': 'partial',
    'u': 'universal',
})

mushrooms_renamed['has-ring'] = mushrooms_renamed['has-ring'].replace({
    't': 1,
    'f': 0
})

mushrooms_renamed['ring-type'] = mushrooms_renamed['ring-type'].replace({
    'c': 'cobwebby', 
    'e': 'evanescent', 
    'r': 'flaring', 
    'g': 'grooved',
    'l': 'large', 
    'p': 'pendant', 
    's': 'sheathing', 
    'z': 'zone',
    'y': 'scaly', 
    'm': 'movable', 
    'f': 'none', 
    '?': 'unknown'
})

# Replace values in the 'habitat' column
mushrooms_renamed['habitat'] = mushrooms_renamed['habitat'].replace({
    'g': 'grasses', 
    'l': 'leaves', 
    'm': 'meadows', 
    'p': 'paths', 
    'h': 'heaths', 
    'u': 'urban', 
    'w': 'waste', 
    'd': 'woods'
})

# Replace values in the 'season' column
mushrooms_renamed['season'] = mushrooms_renamed['season'].replace({
    's': 'spring', 
    'u': 'summer', 
    'a': 'autumn', 
    'w': 'winter'
})

mushrooms_renamed.to_csv('mushrooms_v2.csv', index=False)


            
