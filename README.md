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

* AutoReg executable file found in this repo (Currently only runs on Mac computers, but a Windows version is coming soon).



* ChromeDriver executable file for your version of Chrome. That file can be downloaded [here](https://chromedriver.chromium.org/downloads); Make sure you download the correct driver for your version of Chrome (You can check your '**About Google Chrome**' option in the **Chrome** tab to check your version; EX: Version 75.x.xxxx.xxx). Once downloaded, unzip the file.



When the ChromeDriver is unzipped, right-click the unzipped file. Press and hold the '**option**' key on your Mac keyboard, and click on the '**Copy 'chromedriver' as Pathname**' option. You can then proceed to open the AutoReg file. When open, paste the pathname into the 'Pathname' entry field, then continue to input you Manhattan College Login credentials as well as the CRN's of the desired classes you want to register for (You can enter up to 4). When all the info is entered, you can click the '**Run Bot**' button. Chrome should automatically open and begin to register your classes. **If registration is not yet open, the program will refresh the page until the registration opens**.



The AutoReg program will use the entered information and input them into their respective fields on the Chrome Browser (Similar to Auto-fill), however it's done with the full registration process and data entry happens in milliseconds; **A user would only need to input the info into the program beforehand, and then just press the 'Run Bot' button. The program will handle everything from start to finish** (Ex: Logging In, Navigating, Button Clicks, etc).



## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



Please make sure to update tests as appropriate.



## License

[MIT](https://choosealicense.com/licenses/mit/)