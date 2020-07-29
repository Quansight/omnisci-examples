
def test_db_connection(con):
    assert con.user == 'admin'
