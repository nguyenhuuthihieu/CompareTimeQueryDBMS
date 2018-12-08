from arango import ArangoClient
import subprocess

args = ['net', 'start', 'ArangoDB']

def restart_arangodb():
    args[1] = 'start'
    subprocess.run(args)
    args[1] = 'stop'
    subprocess.run(args)
    args[1] = 'start'
    subprocess.run(args)

def arangoDBConnect(aql):
    # restart_arangodb()
    client = ArangoClient()
    db = client.db('_system', username='root', password='')
    cursor = db.aql.execute(
        aql,
        batch_size=100
    )
    stats = cursor.statistics()

    return stats['execution_time']
