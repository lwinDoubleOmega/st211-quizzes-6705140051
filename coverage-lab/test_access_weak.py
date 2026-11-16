from access import check_access

def test_admin_active():
    assert check_access("admin", True) == "granted"

def test_admin_inactive():
    assert check_access("user", False) == "denied"