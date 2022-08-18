Set up MySQL database using Shell or TERMINAL
	% myslsh //Opens MYSQL shell in MacOS TERMINAL
	\sql    //if Shell is in JS mode
	\connect root@localhost     //create session
	SHOW DATABASES;         //list current databases
	
	CREATE DATABASE mailroom CHARACTER SET UTF8MB4;     
	CREATE USER 'root'@'localhost' IDENTIFIED BY 'mountain123';
	GRANT ALL PRIVILEGES ON auditrater.* TO 'root'@'localhost';


In main project folder - mail_project
	Check python && pip version and upgrade if needed
		python3 --version 
		python3 -m --upgrade
		pip3 --version
		pip3 install --upgrade pip

    If you want to setup a venv to keep dependencies at project level
        Start a venv
            python3 -m venv venv
        Activate venv
            source venv/bin/activate

	Install packages
		Using requirements.txt
			pip3 freeze > requirements.txt
	
	Create SuperUser
		python3 manage.py createsuperuser
		Username: root
		Password: mountain123

	CD into mail_project
		python3 manage.py runserver
		localhost:8000/mailroom/
