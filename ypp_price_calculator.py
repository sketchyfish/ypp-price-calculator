#!/usr/bin/python


"""
Add these back to the list below when done: 'Iron', 'Hemp oil', 'Varnish', 'Lacquer', "Kraken's ink", 'Madder', "Old man's beard",
          'Yarrow', 'Sassafras', 'Iris root', 'Weld', 'Broom flower', 'Lobelia', 'Pokeweed berries',
          'Indigo', 'Elderberries', 'Cowslip', 'Lily of the Valley', 'Nettle', 'Butterfly weed',
          'Tellurium', 'Cubanite', 'Serandite', 'Gold nuggets', 'Red dye', "Kraken's Blood",
          'Yellow dye', 'Blue dye', 'Green dye', 'Red paint', 'Tan paint', 'White paint', 'Black paint',
          'Grey paint', 'Yellow paint', 'Pink paint', 'Violet paint', 'Purple paint', 'Navy paint',
          'Blue paint', 'Aqua paint', 'Lime paint', 'Green paint', 'Orange paint', 'Maroon paint',
          'Brown paint', 'Gold paint', 'Rose paint', 'Lavender paint', 'Mint paint', 'Light green paint',
          'Magenta paint', 'Lemon paint', 'Peach paint', 'Light blue paint', 'Persimmon paint', 'Red enamel',
"""

list_b = ['Green paint', 'Orange paint', 'Maroon paint', 'Brown paint', 'Gold paint', 'Rose paint',
          'Lavender paint', 'Mint paint', 'Light green paint', 'Magenta paint', 'Lemon paint',
          'Peach paint', 'Light blue paint', 'Persimmon paint', 'Red enamel','Orange enamel',
          'Yellow enamel', 'Green enamel', 'Blue enamel', 'Purple enamel', 'White enamel',
          'Black enamel', 'Tan enamel', 'Grey enamel', 'Pink enamel', 'Violet enamel', 'Navy enamel',
          'Aqua enamel', 'Lime enamel', 'Maroon enamel', 'Brown enamel', 'Gold enamel', 'Rose enamel',
          'Lavender enamel', 'Mint enamel', 'Light green enamel', 'Magenta enamel', 'Lemon enamel',
          'Peach enamel', 'Light blue enamel', 'Persimmon enamel']

list_a = []
list_c = []



def main():
    for each_item in list_b:
        print("What is your buy price for %s?") % (each_item)
        a = raw_input("Type price and hit enter: ")
        a = str(a)
        if len(a) <= 2:
            print(" \n")
            a = int(a)
            a += 15
            b = "Your use cost for " + each_item + " should be " + str(a) + "."
            list_a.append(b)
            print(" \n")
            a *= 5
            list_c.append("You should sell " + each_item + " for " + str(a))
            for all_items in list_a:
                print(" \n")
            for the_items in list_c:
                x = all_items + " " + the_items
                print(x)
                print(" \n")
                
        elif len(a) == 3:
            print(" \n")
            a = int(a)
            a += 70
            b = "Your use cost for " + each_item + " should be " + str(a) + "."
            list_a.append(b)
            print(" \n")
            a *= 5
            list_c.append("You should sell " + each_item + " for " + str(a))
            for all_items in list_a:
                print(" \n")
            for the_items in list_c:
                x = all_items + " " + the_items
                print(x)
                print(" \n")
        else:
            print(" \n")
            a = int(a)
            a += 150
            b = "Your use cost for " + each_item + " should be " + str(a) + "."
            list_a.append(b)
            print(" \n")
            a *= 5
            list_c.append("You should sell " + each_item + " for " + str(a))
            for all_items in list_a:
                print(" \n")
            for the_items in list_c:
                x = all_items + " " + the_items
                print(x)
                print(" \n")
main()
