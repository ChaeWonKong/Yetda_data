import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import csv

# Use a service account
cred = credentials.Certificate(
    './config/yetda-d4506-firebase-adminsdk-ai9kq-97df4de6f8.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


# Writing Data to DB
def write_present(row):
    tags = row[3:]
    refined_tags = []
    for tag in tags:
        if len(tag):
            refined_tags.append(tag)

    doc_ref = db.collection(u'presents').document(row[0])
    doc_ref.set({
        u'id': int(row[0]),
        u'name': row[1],
        u'price': int(row[2]) if row[2] else 0,
        u'tags': refined_tags
    })


def write_question(row):
    doc_ref = db.collection(u'question').document(row[0])
    doc_ref.set({
        u'id': int(row[0]),
        u'tag': row[1],
        u'question': row[2]
    })


# Read All Data from present list csv
with open("raw_data/presents.csv", "r", encoding="utf-8", newline="") as rf:
    reader = csv.reader(rf)
    for row in reader:
        if row[0] == "id":
            continue
        write_present(row)

    rf.close()

# Read All Data from question list csv
with open("raw_data/questions.csv", "r", encoding="utf-8", newline="") as rf:
    reader = csv.reader(rf)
    for row in reader:
        if row[0] == 'id':
            continue
        write_question(row)

    rf.close()

# Read all data from DB
presents_ref = db.collection(u'presents')
docs = presents_ref.stream()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))
