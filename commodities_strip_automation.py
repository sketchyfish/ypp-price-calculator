#!/usr/bin/python

new_list = ['Iron\n', 'Hemp oil\n', 'Varnish\n', 'Lacquer\n', "Kraken's ink\n", 'Madder\n', "Old man's beard\n",
            'Yarrow\n', 'Sassafras\n', 'Iris root\n', 'Weld\n', 'Broom flower\n', 'Lobelia\n', 'Pokeweed berries\n',
            'Indigo\n', 'Elderberries\n', 'Cowslip\n', 'Lily of the Valley\n', 'Nettle\n', 'Butterfly weed\n',
            'Tellurium\n', 'Cubanite\n', 'Serandite\n', 'Gold nuggets\n', 'Red dye\n', "Kraken's Blood\n",
            'Yellow dye\n', 'Blue dye\n', 'Green dye\n', 'Red paint\n', 'Tan paint\n', 'White paint\n', 'Black paint\n',
            'Grey paint\n', 'Yellow paint\n', 'Pink paint\n', 'Violet paint\n', 'Purple paint\n', 'Navy paint\n',
            'Blue paint\n', 'Aqua paint\n', 'Lime paint\n', 'Green paint\n', 'Orange paint\n', 'Maroon paint\n',
            'Brown paint\n', 'Gold paint\n', 'Rose paint\n', 'Lavender paint\n', 'Mint paint\n', 'Light green paint\n',
            'Magenta paint\n', 'Lemon paint\n', 'Peach paint\n', 'Light blue paint\n', 'Persimmon paint\n', 'Red enamel\n',
            'Orange enamel\n', 'Yellow enamel\n', 'Green enamel\n', 'Blue enamel\n', 'Purple enamel\n', 'White enamel\n',
            'Black enamel\n', 'Tan enamel\n', 'Grey enamel\n', 'Pink enamel\n', 'Violet enamel\n', 'Navy enamel\n',
            'Aqua enamel\n', 'Lime enamel\n', 'Maroon enamel\n', 'Brown enamel\n', 'Gold enamel\n', 'Rose enamel\n',
            'Lavender enamel\n', 'Mint enamel\n', 'Light green enamel\n', 'Magenta enamel\n', 'Lemon enamel\n',
            'Peach enamel\n', 'Light blue enamel\n', 'Persimmon enamel']

newi_list = []

for each_item in new_list:
    b = each_item.strip("\n")
    c = b.strip("\t")
    newi_list.append(c)

print(newi_list)
print("\n")
