# -*- coding: utf-8 -*-

class GildedRose(object):
    # Nomes dos itens especiais para deixar claro.
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"

    # Limites de qualidade.
    MAX_QUALITY = 50
    MIN_QUALITY = 0

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # "Sulfuras" é um item lendário: sua qualidade e prazo de venda nunca mudam.
            if item.name == self.SULFURAS:
                continue # Pula para o próximo item.

            # Lógica de atualização de qualidade ANTES de decrementar o prazo de venda.
            if item.name == self.AGED_BRIE:
                # "Aged Brie" aumenta sua qualidade com o tempo.
                if item.quality < self.MAX_QUALITY:
                    item.quality = item.quality + 1
            elif item.name == self.BACKSTAGE_PASSES:
                # "Backstage passes" aumentam a qualidade à medida que o show se aproxima.
                if item.quality < self.MAX_QUALITY:
                    item.quality = item.quality + 1
                    # Aumento adicional de qualidade perto da data do show.
                    if item.sell_in < 11: # 10 dias ou menos.
                        if item.quality < self.MAX_QUALITY:
                            item.quality = item.quality + 1
                    if item.sell_in < 6:  # 5 dias ou menos.
                        if item.quality < self.MAX_QUALITY:
                            item.quality = item.quality + 1
            else:
                # Itens comuns: qualidade diminui.
                if item.quality > self.MIN_QUALITY:
                    item.quality = item.quality - 1

            # Decrementa o prazo de venda para todos os itens (exceto "Sulfuras").
            item.sell_in = item.sell_in - 1

            # Lógica de atualização de qualidade APÓS o prazo de venda expirar (sell_in < 0).
            if item.sell_in < 0:
                if item.name == self.AGED_BRIE:
                    # "Aged Brie" continua a melhorar mesmo após o prazo.
                    if item.quality < self.MAX_QUALITY:
                        item.quality = item.quality + 1
                elif item.name == self.BACKSTAGE_PASSES:
                    # "Backstage passes" perdem todo o valor após o show.
                    item.quality = 0
                else:
                    # Itens comuns: qualidade diminui duas vezes mais rápido.
                    if item.quality > self.MIN_QUALITY:
                        item.quality = item.quality - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
