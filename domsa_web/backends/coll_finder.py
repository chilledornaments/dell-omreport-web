from domsa_web import app, client, db

def get_mongo_collections():
    colls = []
    for c in db.collection_names():
        colls.append(c)

    return colls