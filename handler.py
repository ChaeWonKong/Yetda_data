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
def write_db(row):
    tags = row[3:]
    refined_tags = []
    for tag in tags:
        if len(tag):
            refined_tags.append(tag)

    doc_ref = db.collection(u'presents').document(row[0])
    doc_ref.set({
        u'name': row[1],
        u'price': int(row[2]) if row[2] else 0,
        u'tags': refined_tags
    })


# Read All Data from csv
with open("raw_data/yetda_sample_list.csv", "r", encoding="utf-8", newline="") as rf:
    reader = csv.reader(rf)
    for row in reader:
        if row[0] == "id":
            continue
        write_db(row)

    rf.close()

# Read all data from DB
presents_ref = db.collection(u'presents')
docs = presents_ref.stream()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))
