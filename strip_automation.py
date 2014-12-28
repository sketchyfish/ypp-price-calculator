#!/usr/bin/python

"""
This code uses .strip formatting once to remove the \n and another time to remove the \t from the below lists.
For readability, the script uses a print("\n") to add a new line between the two lists
"""

island_list = ['Armstrong Island', 'Atchafalaya Island', 'Immokalee Island', 'Moultrie Island', 'Sho-ke Island', 'Sirius Island',
               'Tumult Island', 'The Beaufort Islands', "Messier's Crown", 'Nunataq Island', 'Paollu Island', 'Qaniit Island',
               'Ancoraggio Island', 'Fluke Island', 'Kakraphoon Island', 'Eagle Archipelago', 'Cambium Island', "Hubble's Eye",
               'Ilha da Aguia', 'Ix Chel', 'Manu Island', 'Admiral Island', 'Basset Island', 'Bryher Island', 'Cromwell Island',
               'Hook Shelf', 'Isle of Kent', 'Lincoln Island', 'Wensleydale', 'Anegada Island', 'Barnard Island', 'The Lowland Hundred',
               'Lyonesse Island', 'Myvatn Island', 'Arakoua Island', 'Aten Island', 'Barbary Island', 'Caravanserai Island',
               'Kasidim Island', 'Kiwara Island', 'Terjit Island', 'Tichka Plateau', 'Aimuari Island', 'Chachapoya Island',
               'Matariki Island', 'Pukru Island', 'Quetzal Island', 'Saiph Island', 'Toba Island', 'Albatross Island', 'Ambush Island',
               'Deadlight Dunes', 'Gauntlet Island', "Jack's Last Gift", 'Mirage Island', 'Scurvy Reef', 'Blackthorpe Island', 'Cook Island',
               'Descartes Isle', 'Fowler Island', 'Greenwich Island', 'Halley Island', 'Spaniel Island', 'Starfish Island', 'Ventress Island',
               'Accompong Island', 'Gallows Island', 'Iocane Island', 'Maia Island', 'Morgana Island', 'Paihia Island', 'Umbarten Island',
               'Auk Island', 'Cryo Island', 'Hoarfrost Island', 'Amity Island', 'Bowditch Island', 'Hinga Island', 'Penobscot Island', 'Rowes Island',
               'Scrimshaw Island', 'Squibnocket Island', 'Wissahickon Island', 'Ashkelon Arch', 'Kashgar Island', 'Morannon Island', 'Alkaid Island',
               'Doyle Island', "Edgar's Choice", 'Isle of Keris', 'Marlowe Island', "McGuffin's Isle", 'Sayers Rock']


commodity_list = [['Hemp', 'Hemp oil', 'Iron', "Kraken's ink", 'Lacquer', 'Stone', 'Sugar cane', 'Varnish', 'Wood', '', 'Broom flower', 'Butterfly weed',
                   'Cowslip', 'Elderberries', 'Indigo', 'Iris root', 'Lily of the valley', 'Lobelia', 'Madder', 'Nettle', "Old man's beard", 'Pokeweed berries',
                   'Sassafras', 'Weld', 'Yarrow', '', 'Chalcocite', 'Cubanite', 'Gold nugget', 'Lorandite', 'Leushite', 'Masuyite', 'Papagoite',
                   'Serandite', 'Sincosite', 'Tellurium', 'Thorianite', '', 'Bananas', 'Carambolas', 'Coconuts', 'Durians', 'Limes', 'Mangos',
                   'Passion fruit', 'Pineapples', 'Pomegranates', 'Rambutan', 'Amber gems', 'Amethyst gems', 'Beryl gems', 'Coral gems',
                   'Diamonds', 'Emeralds', 'Jade gems', 'Jasper gems', 'Jet gems', 'Lapis lazuli gems', '  ', 'Moonstones', 'Opals', 'Pearls',
                   'Quartz gems', 'Rubies', 'Sapphires', 'Tigereye gems', 'Topaz gems', 'Gold nuggets (mineral)', '', 'Swill', 'Grog', 'Fine rum',
                   'Small, medium, and large cannon balls', 'Lifeboats', '', 'Aqua cloth', 'Black cloth', 'Blue cloth', 'Brown cloth', 'Gold cloth',
                   'Green cloth', 'Grey cloth', 'Lavender cloth', 'Light green cloth', 'Lime cloth', 'Magenta cloth', 'Maroon cloth', 'Mint cloth',
                   'Navy cloth', 'Orange cloth', 'Pink cloth', 'Purple cloth', 'Red cloth', 'Rose cloth', 'Tan cloth', 'Violet cloth', 'White cloth',
                   'Yellow cloth', 'Fine aqua cloth', 'Fine black cloth', 'Fine blue cloth', 'Fine brown cloth', 'Fine gold cloth', 'Fine green cloth',
                   'Fine grey cloth', 'Fine lavender cloth', 'Fine light green cloth', 'Fine lime cloth', 'Fine magenta cloth', 'Fine maroon cloth',
                   'Fine mint cloth', '    ', 'Fine navy cloth', 'Fine orange cloth', 'Fine pink cloth', 'Fine purple cloth', 'Fine red cloth', 'Fine rose cloth',
                   'Fine tan cloth', 'Fine violet cloth', 'Fine white cloth', 'Fine yellow cloth', 'Sail cloth', '', 'Blue dye', 'Green dye',
                   "Kraken's blood", 'Red dye', 'Yellow dye', '', 'Aqua enamel', 'Black enamel', 'Blue enamel', 'Brown enamel', 'Gold enamel',
                   'Green enamel', 'Grey enamel', 'Lavender enamel', 'Light green enamel', 'Lime enamel', 'Magenta enamel', 'Maroon enamel', 'Mint enamel',
                   'Navy enamel', 'Orange enamel', 'Pink enamel', 'Purple enamel', 'Red enamel', 'Rose enamel', 'Tan enamel', 'Violet enamel', 'White enamel',
                   'Yellow enamel', '', 'Aqua paint', 'Black paint', 'Blue paint', 'Brown paint', 'Gold paint', 'Green paint', 'Grey paint', 'Lavender paint',
                   'Light green paint', 'Lime paint', 'Magenta paint', 'Maroon paint', 'Mint paint', 'Navy paint', 'Orange paint', 'Pink paint',
                   'Purple paint', 'Red paint', 'Rose paint', 'Tan paint', 'Violet paint', 'White paint', 'Yellow paint']]
newi_list = []
newc_list = []

for each_item in island_list:
    b = each_item.strip("\n")
    c = b.strip("\t")
    newi_list.append(c)
for each_item in commodity_list:
    b = each_item.strip("\n")
    c = b.strip("\t")
    newc_list.append(c)

print(newi_list)
print("\n")
print(newc_list)
