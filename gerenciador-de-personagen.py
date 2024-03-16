# Definindo a classe Personagem
class Personagem:
    # Método construtor
    def __init__(self, nome, descricao, link_imagem, programa, animador):
        self.nome = nome
        self.descricao = descricao
        self.link_imagem = link_imagem
        self.programa = programa
        self.animador = animador

# Criando instâncias de personagens
mickey = Personagem("Mickey Mouse", "Rato antropomórfico", "https://wallpapers.com/images/hd/mickey-mouse-disney-z87kwkhqxqipcwh1.jpg", "Disney", "Walt Disney")
pateta = Personagem("Pateta", "Cão antropomórfico", "https://img.olhardigital.com.br/wp-content/uploads/2021/05/Pateta.jpg", "Disney", "Walt Disney")

# Exibindo informações dos personagens
print("Informações do Mickey Mouse:")
print("Nome:", mickey.nome)
print("Descrição:", mickey.descricao)
print("Link da imagem:", mickey.link_imagem)
print("Programa:", mickey.programa)
print("Animador:", mickey.animador)
print("\n")
print("Informações do Pateta:")
print("Nome:", pateta.nome)
print("Descrição:", pateta.descricao)
print("Link da imagem:", pateta.link_imagem)
print("Programa:", pateta.programa)
print("Animador:", pateta.animador)
