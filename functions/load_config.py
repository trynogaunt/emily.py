import json

with open('config.json', 'r') as config:
    data_config = json.load(config)
    prefix = data_config['Prefix']
    not_in_help =data_config["No_help_command"]
    bot_name = data_config['Name']
    bot_token = data_config['Token']
    database_name = data_config['Database']['Name']
    database_host = data_config['Database']['Host']
    database_user = data_config['Database']['User']
    database_mdp = data_config['Database']['Mdp']