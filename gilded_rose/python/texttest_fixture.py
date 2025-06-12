# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import * # Importa Item e GildedRose

if __name__ == "__main__":
    print ("OMGHAI!")

    # Lista de itens para teste
    items = [
             Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
             Item(name="Aged Brie", sell_in=2, quality=0),
             Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
             Item(name="Conjured Mana Cake", sell_in=3, quality=6),
            ]

    days = 2 # Número padrão de dias para simulação
    import sys
    if len(sys.argv) > 1:
        # Permite especificar o número de dias via argumento de linha de comando
        days = int(sys.argv[1]) + 1

    # Simula a passagem dos dias e atualiza a qualidade dos itens
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item) # Mostra o estado atual do item
        print("")
        GildedRose(items).update_quality() # Atualiza a qualidade dos itens
