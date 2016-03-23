#!venv/bin python
"""Unit tests for the prj_to_be_tested.authentcation module."""


from unittest import TestCase
from mock import patch
import project.auth as auth


class StandAloneTests(TestCase):
    """Test the stand-alone module functions."""


    @patch('__builtin__.open')
    def test_login(self, mock_open):
        """Test the login function."""
        mock_open.return_value.read.return_value = \
            "Yunxi|Li\n"
        self.assertTrue(auth.login('Yunxi', 'Li'))
        
    ########## uncomment the following lines if you want to have a 100% coverage ##########    
    #@patch('__builtin__.open')
    #def test_login_bad_creds(self, mock_open):
    #    """Test the login function when bad creds are passed."""
    #    mock_open.return_value.read.return_value = \
    #        "Yunxi|Li"
    #    self.assertFalse(auth.login('Yunxi', 'li'))

    #@patch('__builtin__.open')
    #def test_login_error(self, mock_open):
    #    """Test the login function when an error happens."""
    #    mock_open.side_effect = IOError()
    #    self.assertFalse(auth.login('Yunxi', 'Li'))
    ######################## end ########################################################

# end of file
