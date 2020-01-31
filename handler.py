import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate(
    './config/yetda-d4506-firebase-adminsdk-ai9kq-97df4de6f8.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

gift_list = db.collection(u'giftList')
docs = gift_list.stream()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))
