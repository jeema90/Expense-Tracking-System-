
from backend import db_helper
def test_get_expenses_for_date_15():
    date=db_helper.get_expenses_for_date("2024-08-15")
    assert len(date)==1
    assert date[0]['amount']==10.0
    assert date[0]['category'] =='Shopping'
    assert date[0]['notes']=='Bought potatoes'

def test_get_expenses_for_date_16():
    date = db_helper.get_expenses_for_date("999-08-15")
    assert len(date) == 0

    #def test_insert_expense():
    #ins=db_helper.insert_expense("2024-08-16",100,"food","pizza")
    #assert len(ins)==1
    #assert ins[0]['amount'] == 100
    #assert ins[0]['category'] == 'food'
    #assert ins[0]['notes'] == 'pizza'

