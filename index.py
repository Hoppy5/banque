class Compte:
    def __init__(self, nom, solde):
        self.nom = nom
        self.solde = solde

class Banque:
    def __init__(self):
        self.comptes = {}

    def creer_compte(self, nom, solde):
        if nom not in self.comptes:
            self.comptes[nom] = Compte(nom, solde)
            print("Le compte {} a été créé avec succès.".format(nom))
        else:
            print("Ce nom de compte est déjà utilisé.")

    def verifier_solde(self, nom):
        if nom in self.comptes:
            print("Le solde du compte {} est de {}.".format(nom, self.comptes[nom].solde))
        else:
            print("Ce compte n'existe pas.")

    def deposer_argent(self, nom, montant):
        if nom in self.comptes:
            self.comptes[nom].solde += montant
            print("{} a été déposé avec succès dans le compte {}.".format(montant, nom))
        else:
            print("Ce compte n'existe pas.")

    def retirer_argent(self, nom, montant):
        if nom in self.comptes:
            if self.comptes[nom].solde >= montant:
                self.comptes[nom].solde -= montant
                print("{} a été retiré avec succès du compte {}.".format(montant, nom))
            else:
                print("Fonds insuffisants.")
        else:
            print("Ce compte n'existe pas.")

    def fermer_compte(self, nom):
        if nom in self.comptes:
            del self.comptes[nom]
            print("Le compte {} a été fermé avec succès.".format(nom))
        else:
            print("Ce compte n'existe pas.")

# Interface utilisateur
banque = Banque()
while True:
    print("\n1. S'authentifier")
    print("2. Créer un compte client")
    print("3. Vérifier le solde")
    print("4. Déposer de l'argent")
    print("5. Retirer de l'argent")
    print("6. Fermer un compte")
    print("7. Quitter l'interface")
    choix = input("Choisissez une option : ")

    if choix == "1":
        # Ajoutez ici l'authentification de l'utilisateur
        print("Authentification en cours...")
    elif choix == "2":
        nom = input("Entrez le nom du nouveau compte : ")
        solde = float(input("Entrez le solde initial : "))
        banque.creer_compte(nom, solde)
    elif choix == "3":
        nom = input("Entrez le nom du compte : ")
        banque.verifier_solde(nom)
    elif choix == "4":
        nom = input("Entrez le nom du compte : ")
        montant = float(input("Entrez le montant à déposer : "))
        banque.deposer_argent(nom, montant)
    elif choix == "5":
        nom = input("Entrez le nom du compte : ")
        montant = float(input("Entrez le montant à retirer : "))
        banque.retirer_argent(nom, montant)
    elif choix == "6":
        nom = input("Entrez le nom du compte à fermer : ")
        banque.fermer_compte(nom)
    elif choix == "7":
        print("Merci, à bientôt !")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")
