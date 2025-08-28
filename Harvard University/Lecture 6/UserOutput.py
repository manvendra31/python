from UserInput import squ

def test_squ(monkeypatch, capsys):
    # Simulate user input "5"
    monkeypatch.setattr('builtins.input', lambda _: "5")

    # Call the function
    squ()

    # Capture printed output
    captured = capsys.readouterr()

    # Check if output contains the correct result
    assert "25" in captured.out
