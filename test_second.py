import second

def test_add():
    assert second.add(7,3)==10
    assert second.add(7)==9
    assert second.add(5)==7

def test_product():
    assert second.product(2,3)==6
    assert second.product(2)==4
    assert second.product(4)==8


