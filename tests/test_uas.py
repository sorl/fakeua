import uas


def test_chrome():
    assert type(uas.chrome()) == str

def test_firefox():
    assert type(uas.firefox()) == str

def test_bot():
    assert type(uas.bot()) == str

def test_os():
    assert type(uas._os("")) == str

def test_BOTS():
    assert type(uas.BOTS) == tuple
    for bot in uas.BOTS:
        assert type(bot) == str
