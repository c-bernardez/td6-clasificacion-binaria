import pandas as pd
import random

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

mushrooms_renamed['season'] = mushrooms_renamed['season'].replace({
    's': 'spring', 
    'u': 'summer', 
    'a': 'autumn', 
    'w': 'winter'
})


#filling out nulls
cap_surface_set = {'fibrous', 'grooves', 'scaly', 'smooth', 'dry', 'shiny', 'leathery', 'silky', 'sticky', 'wrinkled', 'fleshy'}
gill_spacing_set = {'close', 'distant', 'none'}
ring_type_set = {'cobwebby', 'evanescent', 'flaring', 'grooved', 'large', 'pendant', 'sheathing', 'zone', 'scaly', 'movable', 'none'}
veil_type_set = {'partial', 'universal'}
gill_attachment_set = {'adnate', 'adnexed', 'decurrent', 'free', 'sinuate', 'pores', 'none'}
stem_root_set = {'bulbous', 'swollen', 'club', 'cup', 'equal', 'rhizomorphs', 'rooted'}

# Function to fill nulls only
def fill_null_with_random(column, value_set):
    mushrooms_renamed[column] = mushrooms_renamed[column].apply(
        lambda x: x if pd.notnull(x) else random.choice(list(value_set))
    )

# Apply the function for each column
fill_null_with_random('cap-surface', cap_surface_set)
fill_null_with_random('gill-spacing', gill_spacing_set)
fill_null_with_random('ring-type', ring_type_set)
fill_null_with_random('veil-type', veil_type_set)
fill_null_with_random('gill-attachment', gill_attachment_set)
fill_null_with_random('stem-root', stem_root_set)


#output file
mushrooms_renamed.to_csv('mushrooms_v2.csv', index=False)



#check there are no nulls
null_columns_set = set()       
null_rows = mushrooms_renamed[mushrooms_renamed.isnull().any(axis=1)]
for index, row in null_rows.iterrows():
    null_columns = row[row.isnull()].index.tolist()  # Get the columns with null values
    null_columns_set.update(null_columns)  # Add the columns to the set (automatically handles duplicates)

# Print the unique columns with null values
print(f"Columns with null values: {null_columns_set}")

# Optionally, count the number of rows with null values
print(f"Number of rows with null values: {len(null_rows)}")