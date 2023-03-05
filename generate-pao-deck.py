import genanki
import csv

pao_model = genanki.Model(
        6677382317,
        'PAO',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[
            {
            'name': 'Card 1',
            'qfmt': '{{Question}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ],
        css="""
            .card {
                font-family: arial;
                font-size: 18px;
                text-align: left;
                line-height:1.45;
                text-align:center;
            }
    """
)

pao_deck = genanki.Deck(
    1184186832,
    'PAO')

with open('pao.csv' , newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader) # skip the header row
    for row in reader:
        number = row[0]
        person = row[1]
        action = row[2]
        object = row[3]

        person_note = genanki.Note(
            model=pao_model,
            fields=[number + ' Person', person  + f'<br><br><strong>({person}</strong> {action} {object})']
        )

        action_note = genanki.Note(
            model=pao_model,
            fields=[number + ' Action', action + f'<br><br>({person} <strong>{action}</strong> {object})']
        )

        object_note = genanki.Note(
            model=pao_model,
            fields=[number + ' Object', object  + f'<br><br>({person} {action} <strong>{object}</strong>)']
        )

        pao_deck.add_note(person_note)
        pao_deck.add_note(action_note)
        pao_deck.add_note(object_note)

genanki.Package(pao_deck).write_to_file('pao.apkg')