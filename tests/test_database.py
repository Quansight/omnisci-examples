
def test_db_connection_local(con):
    assert con.user == 'admin'


def test_db_connection_external(con_external):
    """Test the connection to the external database"""
    assert con_external.user == 'demouser'


def test_db_table_exists(con_external):
    """test the external db table exists
    For the ibis-vega-transform notebooks
    """
    # get the list of tables in the external db
    db_table_names = con_external.list_tables()
    # ensure the table we need is included
    assert "flights_donotmodify" in db_table_names
    assert "tweets_nov_feb" in db_table_names
