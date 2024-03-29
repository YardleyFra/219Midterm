from calculator.trigonometry import sine, cosine, tangent

def test_sine():
    assert sine(30) == 0.5

def test_cosine():
    assert cosine(60) == 0.5

def test_tangent():
    assert tangent(45) == 1
