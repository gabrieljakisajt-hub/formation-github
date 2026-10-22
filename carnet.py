def afficher_menu():
    print("=== CARNET DE NOTES ===")
    print("1. Ajouter une note")
    print("2. Voir les notes")
    print("3. Quitter")


afficher_menu()


notes = []


def afficher_menu():
    print("=== CARNET DE NOTES ===")
    print("1. Ajouter une note")
    print("2. Voir les notes")
    print("3. Quitter")


def ajouter_note(texte):
    notes.append(texte)
    print("Note ajoutee :", texte)


afficher_menu()
ajouter_note("Apprendre les Issues")