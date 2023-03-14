from neptune_utils.endpoints import Endpoints
from neptune_utils.batch_utils import BatchUtils


def get_endpoint(url):
    endpoints = Endpoints(neptune_endpoint=url)
    return endpoints


def batch_update_nodes(endpoints, rows, batch_size=50):
    batch = BatchUtils(endpoints)
    batch.upsert_vertices(batch_size=batch_size, rows=rows)
    batch.close()


def batch_update_edges(endpoints, rows, batch_size=50):
    batch = BatchUtils(endpoints)
    batch.upsert_edges(batch_size=batch_size, rows=rows)
    batch.close()
