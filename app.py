# Em Python, usamos 'input()' para ler dados e 'print()' para exibir
# Para converter a entrada para número, usamos 'int()'

class ItemMagico:
    # O construtor em Python se chama __init__
    def __init__(self, tipo, dano, resistencia):
        self.tipo = tipo
        self.dano = dano
        self.resistencia = resistencia

    def calcular_dano(self):
        # Lógica: se for arma, dano dobra
        if self.tipo == 'arma':
            return self.dano * 2
        else:
            return self.dano

# Lendo as entradas do usuário
tipo_item = input()
dano_item = int(input())
resistencia_item = int(input())

# Criando o objeto (instanciando a classe)
item_personalizado = ItemMagico(tipo_item, dano_item, resistencia_item)

# Exibindo os atributos
print(f"Tipo: {item_personalizado.tipo}")
print(f"Dano: {item_personalizado.dano}")
print(f"Resistencia: {item_personalizado.resistencia}")

# Calculando e exibindo o dano em combate
dano_total = item_personalizado.calcular_dano()
print(f"Dano em combate: {dano_total}")
