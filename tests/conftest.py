"""OmniSciDB test configuration module."""
import pytest

import ibis

OMNISCIDB_HOST = '127.0.0.1'
OMNISCIDB_PORT = 6274
OMNISCIDB_DATABASE = 'omnisci'
OMNISCIDB_USER = 'admin'
OMNISCIDB_PASSWORD = 'HyperInteractive'
OMNISCIDB_PROTOCOL = 'binary'


@pytest.fixture(scope='module')
def con():
    """Define a connection fixture.
    Returns
    -------
    ibis.omniscidb.OmniSciDBClient
    """
    omnisci_client = ibis.omniscidb.connect(
        user=OMNISCIDB_USER,
        password=OMNISCIDB_PASSWORD,
        host=OMNISCIDB_HOST,
        port=OMNISCIDB_PORT,
        database=OMNISCIDB_DATABASE
    )
    return omnisci_client
