from arango import ArangoClient

def arangoDBConnect(aql):
    client = ArangoClient()
    db = client.db('_system', username='root', password='')
    cursor = db.aql.execute(
        aql,
        batch_size=100
    )
    stats = cursor.statistics()

    return stats['execution_time']
