# Manhattan-College-Class-Registration-Automator

## Overview

AutoReg is a python GUI based program that allows Manhattan College students to register for their desired courses as soon as the registration portal time opens. This program automates the registration process so that actual registration time happens in milliseconds, increasing the probability of successfully registering for all your desired classes. 



## Installation

If you want to use this program to register for your own classes, check out the '**How to Use/How it Works**' section.


The program itself uses the Selenium Python Package to interact with the Chrome browser.

If you want to create/modify the code, use the package manager [pip](https://pip.pypa.io/en/stable/) to install Selenium.



```bash

pip install selenium

```



## How to Use/How it Works:

The program uses the Selenium package alongside a ChromeDriver to interact with the Chrome Browser to automate the class registration process. If you want to use the program you need to download the following two files:

* AutoReg executable file found in this repo. Currently there is a Mac and Windows version of the program.



* ChromeDriver executable file for your version of Chrome. That file can be downloaded [here](https://chromedriver.chromium.org/downloads); Make sure you download the correct driver for your version of Chrome (You can check your '**About Google Chrome**' option in the **Chrome** tab to check your version; EX: Version 75.x.xxxx.xxx). Once downloaded, unzip the file.
**If you update your version of Chrome, REMEMBER to update the ChromeDriver as well**


**FOR MAC**


Use Chrome when downloading the AutoReg program for your Mac computer. When downloading the zip file, the Chrome browser will give you a warning before saving the file on your computer (The warning is there because AutoReg is a raw executable program). Select the **'Keep'** option to save the program on your computer.

<img src= "/README Photos/Mac/Screen Shot 2019-08-13 at 6.04.26 PM.png" width = 320>

Once the zip file is downloaded, proceed to unzip the file. Once unzipped, the program executable file should be displayed on your computer. 

To run the program right-click on the executable file and select the **'Open'** option from the drop-down menu. **Do NOT double click on the executable file to open. Doing so will NOT allow you to open the file because of Apple's GATEKEEPER software in MacOS.** A warning will pop-up because AutoReg was created by an 'unidentified developer'; Click the **"Run"** button. The program should open.


After the AutoReg program is open, you will need to enter your Manhattan College credentials as well as the CRN numbers for the classes you want to register for. You will also need to enter the filepath for the ChromeDriver that was downloaded. To do this right-click on the unzipped ChromeDriver executable file and press and hold the **"Option"** key on the Mac keyboard. Click on the '**Copy 'chromedriver' as Pathname**' option. You can then proceed to open the AutoReg file. When open, paste the pathname into the 'Pathname' entry field. Paste using **COMMAND + V**.

<img src= "/README Photos/Mac/Screen Shot 2019-08-13 at 5.43.59 PM.png" width = 320>
<img src= "/README Photos/Mac/Screen Shot 2019-08-13 at 5.47.30 PM.png" width = 480>

**FOR WINDOWS**


Use Chrome when downloading the AutoReg program for your WINDOWS computer. After you download the zip file, proceed to unzip the file. After the file is unzipped, you can proceed to run the AutoReg executable file. Before the program begins to run, Windows Smart Defender might pop-up with a warning. To bypass this warning just click the **"More info"** button and proceed to click on **"Run Anyways"**. The AutoReg program should then open.

<img src= "/README Photos/Windows/Capture04.PNG" width = 320>

After the AutoReg program is open, you will need to enter your Manhattan College credentials as well as the CRN numbers for the classes you want to register for. You will also need to enter the filepath for the ChromeDriver that was downloaded. To do this select and right-click the unzipped ChromeDriver executable file. Select the **"Properties"** option from the drop-down menu. Once selected, a new window should pop-up with the file properties. Navigate to the **"Security"** tab in the window. There you can copy the filepath from the **Object Name** field. Copy and paste it into the FilePath entry field in the AutoReg program. Paste using **CTRL + V**.

<img src= "/README Photos/Windows/Capture05.PNG" width = 400>




The AutoReg program will use the entered information and input them into their respective fields on the Chrome Browser (Similar to Auto-fill), however it's done with the full registration process and data entry happens in milliseconds; **A user would only need to input the info into the program beforehand, and then just press the 'Run Bot' button. The program will handle everything from start to finish** (Ex: Logging In, Navigating, Button Clicks, etc).


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



Please make sure to update tests as appropriate.



## License

[MIT](https://choosealicense.com/licenses/mit/)
