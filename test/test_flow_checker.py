import flow_checker

def test_check_period():
    assert flow_checker.check_period("28/1/2024", 30) == "Menstruation starts on 2024-01-28 and it ends on 2024-02-27, Fertile window is from 2024-02-10 to 2024-02-15, Ovulation occurs on 2024-02-13 and ends 12 to 24 hours after."