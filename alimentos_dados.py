# Dados de alimentos categorizados
# Formato: Categoria -> "Nome": (Kcal/100g, Carb/100g, Prot/100g, Gord/100g, Medidas, IG)
# IG (Índice Glicêmico): Baixo <= 55 | Médio 56-69 | Alto >= 70 (0 para sem impacto/traços)
dados = {
    "Cereais, Pães e Massas": {
        "Arroz Branco (cozido)": (128, 28.1, 2.5, 0.2, {"Colher cheia": 25}, 73),
        "Arroz Integral (cozido)": (112, 23.5, 2.6, 1.0, {"Colher cheia": 25}, 50),
        "Macarrão (cozido)": (157, 31.0, 5.8, 0.9, {"Pegador": 40}, 50),
        "Pão Francês": (299, 58.0, 9.0, 3.0, {"Unidade": 50}, 85),
        "Pão de Forma Integral": (248, 42.0, 11.0, 3.5, {"Fatia": 25}, 60),
        "Pão de Forma Branco": (265, 50.0, 8.0, 3.5, {"Fatia": 25}, 75),
        "Tapioca (goma)": (240, 60.0, 0.0, 0.0, {"Colher sopa": 20}, 90),
        "Aveia em Flocos": (389, 66.0, 17.0, 7.0, {"Colher sopa": 15}, 55),
        "Cuscuz de Milho (cozido)": (113, 25.3, 2.2, 0.7, {"Pedaço médio": 100}, 65),
        "Milho Verde (cozido)": (108, 23.4, 3.3, 1.5, {"Espiga": 100}, 55)
    },
    "Tubérculos e Raízes": {
        "Batata Inglesa (cozida)": (87, 20.0, 1.9, 0.1, {"Unidade média": 150}, 85),
        "Batata Doce (cozida)": (86, 20.1, 1.6, 0.1, {"Rodela grossa": 60}, 50),
        "Mandioca / Macaxeira (cozida)": (125, 30.1, 0.6, 0.3, {"Pedaço médio": 60}, 60),
        "Inhame (cozido)": (97, 23.5, 1.5, 0.2, {"Pedaço médio": 70}, 51)
    },
    "Leguminosas": {
        "Feijão Carioca (cozido)": (76, 14.0, 4.8, 0.5, {"Concha média": 86}, 35),
        "Feijão Preto (cozido)": (77, 14.0, 4.5, 0.5, {"Concha média": 86}, 30),
        "Feijão Fradinho (cozido)": (116, 20.9, 8.8, 0.9, {"Concha média": 86}, 40),
        "Grão de Bico (cozido)": (164, 27.4, 8.9, 2.6, {"Colher cheia": 20}, 28),
        "Lentilha (cozida)": (116, 20.1, 9.0, 0.4, {"Concha média": 86}, 29)
    },
    "Carnes e Aves": {
        "Peito de Frango (grelhado)": (165, 0.0, 31.0, 3.6, {"Filé médio": 120}, 0),
        "Sobrecoxa de Frango (assada s/ pele)": (195, 0.0, 24.0, 11.0, {"Unidade": 100}, 0),
        "Carne Moída (Patinho refogado)": (219, 0.0, 32.0, 9.0, {"Colher sopa": 25}, 0),
        "Alcatra (Grelhada)": (241, 0.0, 31.9, 11.6, {"Bife médio": 120}, 0),
        "Picanha (Assada com gordura)": (289, 0.0, 25.0, 20.0, {"Fatia": 100}, 0),
        "Músculo (Cozido)": (194, 0.0, 31.0, 7.0, {"Pedaço": 50}, 0),
        "Fígado de Boi (Grelhado)": (225, 4.0, 30.0, 9.0, {"Bife": 100}, 0),
        "Carne de Porco (Lombo assado)": (212, 0.0, 29.0, 10.0, {"Fatia": 100}, 0)
    },
    "Embutidos": {
        "Linguiça Calabresa": (300, 2.0, 14.0, 26.0, {"Unidade": 120}, 0),
        "Salsicha": (290, 4.0, 12.0, 25.0, {"Unidade": 50}, 0)
    },
    "Peixes e Frutos do Mar": {
        "Peixe Tilápia (grelhado)": (128, 0.0, 26.0, 2.0, {"Filé": 120}, 0),
        "Peixe Salmão (grelhado)": (206, 0.0, 22.0, 13.0, {"Filé": 120}, 0),
        "Atum em conserva (água)": (116, 0.0, 26.0, 1.0, {"Lata drenada": 120}, 0),
        "Atum em conserva (óleo)": (198, 0.0, 26.0, 8.0, {"Lata drenada": 120}, 0),
        "Camarão (cozido)": (99, 0.0, 24.0, 0.3, {"Unidade média": 10}, 0)
    },
    "Ovos e Laticínios": {
        "Ovo de Galinha (cozido)": (155, 1.1, 13.0, 11.0, {"Unidade": 50}, 0),
        "Ovo Frito (com óleo)": (196, 1.0, 14.0, 15.0, {"Unidade": 50}, 0),
        "Clara de Ovo (cozida)": (52, 0.7, 11.0, 0.2, {"Unidade (de um ovo)": 30}, 0),
        "Gema de Ovo (cozida)": (322, 3.6, 16.0, 27.0, {"Unidade (de um ovo)": 20}, 0),
        "Queijo Mussarela": (300, 3.1, 22.0, 22.0, {"Fatia": 15}, 0),
        "Queijo Prato": (346, 2.0, 22.0, 27.0, {"Fatia": 15}, 0),
        "Queijo Minas Frescal": (243, 2.5, 16.0, 19.0, {"Fatia grossa": 30}, 0),
        "Queijo Coalho": (330, 2.0, 25.0, 24.0, {"Espeto": 40}, 0),
        "Requeijão Tradicional": (257, 3.0, 10.0, 23.0, {"Colher sopa": 30}, 0),
        "Requeijão Light": (175, 4.0, 12.0, 12.0, {"Colher sopa": 30}, 0),
        "Leite Integral": (62, 5.0, 3.2, 3.2, {"Copo": 200}, 30),
        "Leite Desnatado": (35, 5.0, 3.4, 0.0, {"Copo": 200}, 32),
        "Iogurte Natural Integral": (61, 4.7, 3.5, 3.3, {"Pote": 170}, 35),
        "Iogurte Natural Desnatado": (41, 6.0, 4.0, 0.1, {"Pote": 170}, 33)
    },
    "Frutas": {
        "Banana Prata": (98, 26.0, 1.3, 0.1, {"Unidade": 70}, 51),
        "Banana Nanica": (92, 24.0, 1.4, 0.1, {"Unidade": 90}, 55),
        "Maçã Fuji": (52, 14.0, 0.3, 0.2, {"Unidade": 150}, 38),
        "Laranja Pêra": (37, 8.9, 1.0, 0.1, {"Unidade": 130}, 42),
        "Mamão Papaya": (43, 11.0, 0.5, 0.1, {"Metade": 150}, 58),
        "Mamão Formosa": (32, 8.0, 0.4, 0.1, {"Fatia": 150}, 58),
        "Uva Itália": (68, 17.0, 0.6, 0.2, {"Cacho peq": 100}, 59),
        "Abacate": (160, 8.5, 2.0, 15.0, {"Colher sopa": 30}, 15),
        "Morangos": (32, 7.7, 0.7, 0.3, {"Unidade media": 12}, 40),
        "Melancia": (30, 7.6, 0.6, 0.2, {"Fatia": 200}, 72),
        "Abacaxi": (50, 13.0, 0.5, 0.1, {"Rodela grossa": 75}, 59),
        "Manga Tommy": (60, 15.0, 0.8, 0.3, {"Unidade": 300}, 51),
        "Goiaba Branca": (68, 14.0, 2.6, 0.9, {"Unidade": 120}, 29),
        "Pera": (57, 15.0, 0.4, 0.1, {"Unidade": 120}, 38),
        "Maracujá (Polpa)": (97, 23.0, 2.2, 0.7, {"Unidade": 50}, 27),
        "Coco Seco (Polpa)": (354, 15.0, 3.3, 33.0, {"Pedaço": 30}, 40),
        "Limão": (22, 7.0, 0.4, 0.1, {"Unidade": 40}, 20)
    },
    "Hortaliças e Folhas": {
        "Tomate": (18, 3.9, 0.9, 0.2, {"Unidade": 100}, 15),
        "Cebola": (40, 9.0, 1.1, 0.1, {"Unidade": 80}, 15),
        "Alho": (149, 33.0, 6.4, 0.5, {"Dente": 3}, 15),
        "Cenoura (Cozida)": (35, 8.0, 0.8, 0.2, {"Colher sopa": 20}, 41),
        "Cenoura (Crua)": (41, 9.6, 0.9, 0.2, {"Unidade media": 100}, 16),
        "Brócolis (Cozido)": (35, 7.2, 2.4, 0.4, {"Xícara": 80}, 15),
        "Couve-Flor (Cozida)": (25, 5.0, 2.0, 0.3, {"Xícara": 80}, 15),
        "Couve Manteiga (Refogada)": (90, 8.0, 3.0, 5.0, {"Colher sopa": 20}, 15),
        "Alface": (15, 2.9, 1.4, 0.2, {"Folha": 10}, 15),
        "Rúcula": (25, 3.7, 2.6, 0.7, {"Folha": 2}, 15),
        "Espinafre (Cozido)": (23, 3.8, 2.9, 0.3, {"Xícara": 80}, 15),
        "Repolho (Cru)": (25, 5.8, 1.3, 0.1, {"Xícara": 70}, 10),
        "Beterraba (Cozida)": (43, 10.0, 1.6, 0.2, {"Unidade media": 120}, 64),
        "Abobrinha (Cozida)": (15, 3.1, 1.1, 0.3, {"Rodela": 15}, 15),
        "Berinjela (Cozida)": (24, 5.7, 1.0, 0.2, {"Rodela": 20}, 15),
        "Quiabo (Refogado)": (33, 7.5, 1.9, 0.2, {"Colher sopa": 25}, 20),
        "Chuchu (Cozido)": (19, 4.5, 0.8, 0.1, {"Colher sopa": 25}, 15)
    },
    "Gorduras e Oleaginosas": {
        "Azeite de Oliva": (884, 0.0, 0.0, 100.0, {"Colher de sopa": 13, "Fio de azeite (~3g)": 3}, 0),
        "Manteiga": (717, 0.1, 0.9, 81.0, {"Colher de sopa rasa": 10}, 0),
        "Óleo de Soja": (884, 0.0, 0.0, 100.0, {"Colher de sopa": 13}, 0),
        "Óleo de Coco": (862, 0.0, 0.0, 100.0, {"Colher de sopa": 13}, 0),
        "Banha de Porco": (900, 0.0, 0.0, 100.0, {"Colher de sopa": 13}, 0),
        "Castanha de Caju (Torrada)": (553, 30.0, 18.0, 44.0, {"Unidade": 2.5}, 22),
        "Castanha do Pará": (656, 12.0, 14.0, 66.0, {"Unidade": 5}, 15),
        "Amendoim (Torrado)": (567, 16.0, 26.0, 49.0, {"Colher de sopa": 15}, 14),
        "Pasta de Amendoim (Integral)": (588, 20.0, 25.0, 50.0, {"Colher de sopa": 15}, 14),
        "Amêndoas": (579, 21.0, 21.0, 50.0, {"Unidade": 1}, 15),
        "Nozes": (654, 14.0, 15.0, 65.0, {"Unidade": 3}, 15)
    },
    "Doces e Açúcares": {
        "Açúcar Refinado": (387, 100.0, 0.0, 0.0, {"Colher de sopa": 15}, 65),
        "Açúcar Mascavo": (380, 98.0, 0.0, 0.0, {"Colher de sopa": 15}, 65),
        "Mel de Abelha": (304, 82.0, 0.3, 0.0, {"Colher de sopa": 20}, 60),
        "Leite Condensado": (321, 54.0, 7.0, 8.0, {"Colher de sopa": 20}, 61),
        "Creme de Leite (Lata)": (240, 3.0, 2.0, 25.0, {"Colher de sopa": 15}, 30),
        "Doce de Leite": (315, 60.0, 7.0, 7.0, {"Colher de sopa": 20}, 61)
    },
    "Suplementos": {
        "Whey Protein Concentrado": (400, 10.0, 80.0, 5.0, {"Scoop": 30}, 20),
        "Whey Protein Isolado": (380, 3.0, 90.0, 1.0, {"Scoop": 30}, 15),
        "Creatina": (0, 0.0, 0.0, 0.0, {"Scoop/Colher Chá": 3}, 0)
    }
}
