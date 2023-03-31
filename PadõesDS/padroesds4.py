class Pato:
    def grasnar(self):
        print("Quack, quack!")
    
    def voar(self):
        print("Voando em V")


class Galinha:
    def cacarejar(self):
        print("Có, có!")

        
class AdaptadorPato(Galinha):
    def __init__(self, pato):
        self.pato = pato
    
    def cacarejar(self):
        self.pato.grasnar()


class AdaptadorPatoDemo:
    def main(self):
        pato = Pato()
        adaptador = AdaptadorPato(pato)
        
        print("O pato diz:")
        pato.grasnar()
        pato.voar()
        
        print("\nO adaptador de pato como galinha diz:")
        adaptador.cacarejar()

if __name__ == "__main__":
    demo = AdaptadorPatoDemo()
    demo.main()