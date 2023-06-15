import pickle


def add_note(note):
    try:
        with open('записник.pickle', 'rb') as file:
            notes = pickle.load(file)
    except FileNotFoundError:
        notes = []

    notes.append(note)

    with open('записник.pickle', 'wb') as file:
        pickle.dump(notes, file)

    print("Запис додано.")


def read_all_notes():
    try:
        with open('записник.pickle', 'rb') as file:
            notes = pickle.load(file)

        if not notes:
            print("Записи відсутні.")
        else:
            for і, note in enumerate(notes, 1):
                print(f"Запис #{і}:")
                for keys, article in note.items():
                    print(f"{keys}: {article}")
                print()
    except FileNotFoundError:
        print("Записи відсутні.")


def delete_notes():
    try:
        with open('записник.pickle', 'wb') as file:
            pickle.dump([], file)

        print("Записи очищено.")
    except FileNotFoundError:
        print("Записи відсутні.")


# Приклад використання:
add_note({'Назва': 'Приклад', 'Текст': 'Це приклад запису в записнику.'})
add_note({'Назва': 'Інший запис', 'Текст': 'Це інший запис в записнику.'})

read_all_notes()

delete_notes()
