  

To setup a Galaxy server locally, we will first clone the Galaxy github repository, make a few small edits to the galaxy.yaml configuration file, and then start the server.

1. Clone the github repository with ```release_23.2``` branch.

        git clone -b release_23.2 https://github.com/galaxyproject/galaxy.git
        cd galaxy

2. Add yourself as admin user in ```config/galaxy.yaml```

        cp config/galaxy.yml.sample config/galaxy.yml

3. open the ```galaxy.yml``` file with your favorite editor and edit the following line with your email address:

    > admin_users: user@example.org
.
4. Start Galaxy

		sh run.sh

5. Galaxy will now install all its requirements, which may take a few minutes, when all is finished installing, you should see something like this in your screen:

	> Starting server in PID 9560.\
	> serving on http://localhost:8080
    
6. Open Galaxy
- Open a web browser
- Navigate to ```localhost:8080``` to access Galaxy

7. Register an account on Galaxy using the email address you added to the ```config/galaxy.yml``` file. Once logged in, verify that you have a menu item named ```Admin``` in your top menu bar.

8. Pull Galaxy tools from toolshed
    - Click on the ```Admin``` menu.
    - On the left pane, click on ```Install and Uninstall``` under the ```Tool Management``` section.
    - Search for the tools via the ```Search Repositories`` text box on top of the main window.
    - Click on the repository name to expand it. 
    - Click ```Install``` to install the tool into your local Galaxy.