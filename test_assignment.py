from assignment import read_config_file,write_config_file,set_environment_variables
import os
import json


class TestAssignment:
    def test_yaml(self):
        """test the yaml file to dictionary conversion"""
        output = read_config_file('assignament_yaml.yaml')
        exp_output = {'host': 'localhost', 'port': 5432, 'username': 'myuser', 'password': 'mypassword', 'database_name': 'mydb'}
        assert output == exp_output
    def test_conf(self):
        """test the conf file to dictionary conversion"""

        output = read_config_file('assignment_conf.conf')
        exp_output = {'host': 'localhost', 'port': '5432', 'username': 'myuser', 'password': 'mypassword', 'database_name': 'mydb'}
        assert output == exp_output
    def test_cfg(self):
        """test the cfg file to dictionary conversion"""

        output = read_config_file('assignment_cfg.cfg')
        exp_output =  {'host': 'localhost', 'port': '5432', 'username': 'myuser', 'password': 'mypassword', 'database_name': 'mydb'}
        assert output == exp_output
    def test_write_config(self):
        """test write_config function"""

        config =  {'host': 'localhost', 'port': '5432', 'username': 'myuser', 'password': 'mypassword', 'database_name': 'mydb'}
        write_config_file('example.env', config, format='env')
        write_config_file('example.json', config, format='json')
        # open the JSON file
        with open('example.json') as f:
            data = json.load(f)
        assert data == config
        with open('example.env') as f:
            data = f.readlines()
        exp_data = ['host=localhost\n', 'port=5432\n', 'username=myuser\n', 'password=mypassword\n', 'database_name=mydb\n']
        assert data == exp_data
    def test_set_environment(self):
        """test set_environment function"""
        config =  {'host': 'localhost', 'port': '5432'}
        set_environment_variables(config)
        assert os.environ['host'] == 'localhost'
        assert os.environ['port'] == '5432'




