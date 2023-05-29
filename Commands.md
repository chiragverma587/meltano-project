1. Launched EC2 instance with Linux and done the configuration.
2. Installing python,pip and git:
    ### sudo yum install python
    ### sudo yum install pip
    ### sudo yum install git
4. Instaling docker and running the docker service:
    ### sudo yum install docker
    ### sudo usermod -a -G docker ec2-user
    ### id ec2-user
    ### newgrp docker
    ### sudo systemctl start docker.service
6. Installing meltano:
    ### pip install "meltano"
5. Creating meltano project:
    ### meltano init my-meltano-project
6. Navigate to the my-meltano_project directory:
    ### cd my-meltano-project
7. Added Pokeapi Extractor:
    ### meltano add extractor tap-pokeapi
8. Configured the extractor:
    ### meltano config tap-pokeapi set --interactive
9. Specified pokemon name in “airbyte_config.pokemon_name” as "ivysaur"
10. Selecting the columns to be retrieved:
    ### meltano select tap-pokeapi --list --all
    ### meltano select tap-pokeapi pokemon name
    ### meltano select tap-pokeapi pokemon moves
11. Added CSV loader:
    ### meltano add loader target-csv --variant meltanolabs
12. Verifying the yml file:
    ### cat meltano.yml
14. Running the extractor loader flow:
    ### meltano run tap-pokeapi target-csv
14. The Pokemon.csv file is created in my-meltano-project directory.
Moved the csv file to s3 bucket(meltano-project) :
    ### aws s3 cp pokemon.csv s3://meltano-project
