
### New BAND users

1. Go to [band.embl ](https://band.embl.de/#/eosc-landingpage)
    - We recommend using Chrome or Firefox browsers. Please avoid using IE as it is not supported. Safari and Opera may be ok as well, but they are not thoroughly tested.

2. Agree to the Terms of Use and Privacy Notice and click the “Login” button.
    - We recommend Google authentication.

3. After entering your credentials, check your emails for a confirmation email. It will typically take a maximum of 5 mins. Please also check your spam folder.
    - Do not try to use the BAND before you receive the confirmation email.
    - Please contact <cbbcssupport@embl.de> if you do not receive your confirmation email within 10 mins. 

4. Once you receive your confirmation email, go back to band.embl.de and log in again.

5. You will be automatically redirected to the “Launch desktop” page after successful login.

6. Please choose the following desired configurations (CPUs, Memory, GPUs, Screen resolution, and desktop running time).
    - No. of CPUs = 1
    - Memory (gb) = 2
    - No. of GPUs = 0
    - Resolution = your preference
    - Time (days) = 1

7. Click "Launch Desktop"

    - If you encounter an error launching a desktop, please contact us at <cbbcssupport@embl.de>.
    - One user is only allowed to have 1 running desktop.

8. Your desktop will be available in the ”Running Desktop” section if the launch is successful.
    - If this is your first time using the BAND, you may see a red error message appear after clicking “Go to Desktop”. If you see it, please simply stop the desktop and re-launch. The error is due to system and network limitations. It will go away, and the performance of your desktop will be optimal from your second desktop onwards.

    - If the “Go to desktop” button is greyed out, it means there are not enough resources available for your request. In this case, you have two options:
        1) Stop your desktop and adjust your configurations. Lower the requested number of  CPU, Memory, or GPU and launch again.
        2) Wait until other users release their desktops so that more resources become available. The “Show Desktop” will automatically become clickable once there are enough resources.

9. Click “Go to desktop” to view your desktop in a new browser tab.
    - Click “SSH to Desktop” if you prefer a command-line interface.

10. Once your desktop appears in a new tab, you can access all the available software from the Application menu on the top left of your screen.

11. After using your desktop, close the browser tab and click the “Stop desktop” button from the launch screen. 

### Existing BAND users

1. Go to [band.embl ](https://band.embl.de/#/eosc-landingpage)
2. Click “Login” from the menu and then continue from step 5 above.

### Launch skimage/napari

To execute the below steps you need to open a terminal window:

![terminal](/figures/BAND_Terminal.png)

...and you also need to open an Application:

![applications](/figures/BAND_Applications.png)


1. Open a Terminal and execute

        - cd Documents # go to the Document folder
        - mkdir skimage-napari-tutorial # create a folder called skimage-napari-tutorial
        - cd skimage-napari-tutorial
        - wget [https://neubias.github.io/training-resources/functions/OpenIJTIFF.py]()

2. Go to "Applications Places->Programming->JupyterLab". Select 'napari.tensorflow' Kernel

3. Save the jupyter note-book file in skimage-napari-tutorial folder

        File>Save Notebook As …> Documents/skimage-napari-tutorial/”FileName”.ipynb

4. We have napari from the menu. Or if you prefer to start napari within Jupyter, just type  "%gui qt5" and ignore the warnings.

### BAND tipps

1. Do not run the “skill ” command, which may affect your running session and do not “scancel” the slurm job running your desktop session.
2. Do not use any .bashrc in your home directory. It will cause the guacamole connection error.
3. DO NOT store large files in /home, move or download large files to  /scratch. If /home is full, BAND will break. THIS IS IMPORTANT.
4. Refer to [User guide](https://docs.google.com/document/d/1TZBUsNIciGMH_g4aFj2Lu_upISxh5TV9FBMrvNDWmc8/edit) for copy & paste instructions
5. Use pure Google accounts or accounts that purely managed by Google. Account linking, for example, login with Hotmail with account linking to Google may not work.
6. User data stored in /home and /scratch persists between desktop sessions. Stop desktop will not lose data.
7. Recommend to log in to BAND at least once before the course. This is to give enough time to fix issues if there are any.