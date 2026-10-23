notes = []


def afficher_menu():
    print("=== CARNET DE NOTES ===")
    print("1. Ajouter une note")
    print("2. Voir les notes")
    print("3. Quitter")


def ajouter_note(texte):
    notes.append(texte)
    print("Note ajoutee :", texte)


def voir_notes():
    if not notes:
        print("Aucune note.")
    else:
        for numero, note in enumerate(notes, start=1):
            print(numero, "-", note)


afficher_menu()
ajouter_note("Apprendre les Issues")
ajouter_note("Apprendre les Projects")
voir_notes()

comment 