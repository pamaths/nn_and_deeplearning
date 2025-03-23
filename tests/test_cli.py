from pyproject.main_cli import main

def test_cli():
    # Test the CLI such: 
    #   main(['--value', 200])
    output = main([])
    assert output is None


