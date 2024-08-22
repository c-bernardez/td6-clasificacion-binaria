import pandas as pd
import random

random.seed(42)

mushrooms_og = pd.read_csv('mushroom.csv')
mushrooms_renamed = mushrooms_og.copy()

#sampling
rows_to_delete = mushrooms_renamed.sample(n=15000, random_state=42).index
mushrooms_renamed = mushrooms_renamed.drop(index=rows_to_delete)

#filling out nulls
cap_surface_set = {'f', 'g', 'y', 's', 'd', 'h', 'l', 'k', 't', 'w', 'e'}
gill_spacing_set = {'c', 'd', 'f'}
ring_type_set = {'c', 'e', 'r', 'g', 'l', 'p', 's', 'z', 'y', 'm', 'f'}
veil_type_set = {'p', 'u'}
gill_attachment_set = {'a', 'x', 'd', 'e', 's', 'p', 'f'}
stem_root_set = {'b', 's', 'c', 'u', 'e', 'z', 'r'}

def fill_null_with_random(column, value_set):
    mushrooms_renamed[column] = mushrooms_renamed[column].apply(
        lambda x: x if pd.notnull(x) else random.choice(list(value_set))
    )

fill_null_with_random('cap-surface', cap_surface_set)
fill_null_with_random('gill-spacing', gill_spacing_set)
fill_null_with_random('ring-type', ring_type_set)
fill_null_with_random('veil-type', veil_type_set)
fill_null_with_random('gill-attachment', gill_attachment_set)
fill_null_with_random('stem-root', stem_root_set)

mushrooms_renamed.to_csv('mushrooms_small.csv', index=False)