"""OmniSciDB test configuration module."""
import ibis
import pytest

OMNISCIDB_HOST = '127.0.0.1'
OMNISCIDB_PORT = 16274
OMNISCIDB_DATABASE = 'omnisci'
OMNISCIDB_USER = 'admin'
OMNISCIDB_PASSWORD = 'HyperInteractive'
OMNISCIDB_PROTOCOL = 'binary'

EXT_OMNISCIDB_HOST = 'metis.mapd.com'
EXT_OMNISCIDB_PORT = 443
EXT_OMNISCIDB_DATABASE = 'mapd'
EXT_OMNISCIDB_USER = 'demouser'
EXT_OMNISCIDB_PASSWORD = 'HyperInteractive'
EXT_OMNISCIDB_PROTOCOL = 'https'


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
        database=OMNISCIDB_DATABASE,
        protocol=OMNISCIDB_PROTOCOL
    )
    return omnisci_client


@pytest.fixture(scope='module')
def con_external():
    """Define a connection fixture.
    Returns
    -------
    ibis.omniscidb.OmniSciDBClient
    """
    omnisci_client = ibis.omniscidb.connect(
        user=EXT_OMNISCIDB_USER,
        password=EXT_OMNISCIDB_PASSWORD,
        host=EXT_OMNISCIDB_HOST,
        port=EXT_OMNISCIDB_PORT,
        database=EXT_OMNISCIDB_DATABASE,
        protocol=EXT_OMNISCIDB_PROTOCOL
    )
    return omnisci_client
