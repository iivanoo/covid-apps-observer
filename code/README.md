# Running the code   

## Requirements

The only requirement of this project is a working `Python 3` installation (version >3.5 should be enough).
At the moment the code has been tested only on MacOS Catalina 10.15 running the following version of Python

```Shell
Python 3.7.3 (default, Sep 18 2019, 14:29:06)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
```

## Install

Run the following commands in your Terminal to download the ``covid-apps-observer`` source code and to 
install the needed dependencies:

```Shell
$ # Clone the source code of covid-apps-observer 
$ git clone https://github.com/iivanoo/covid-apps-observer.git

$ # Move into the project's directory
$ cd covid-apps-observer

$ # Setup the virtual environment for the project, so that you do not interfere with the other 
$ # Python configurations in your machine
$ virtualenv -p python3 venv
$ # Activate the just created virtual environment
$ source venv/bin/activate

$ # Install all the required packages needed by covid-apps-observer
$ python -m pip install -r requirements.txt
```

## Usage

After all requirements are correctly installed, check the contents of the ``data/apps.json`` file. It contains a minimal set of metadata referring to the Android apps you want to analyze. The ``data/apps.json`` has the following structure:

```js
[
    {
        "id": "com.company.app", // the Package identifier of the app to be analyze
        "store_country": "it", // the country of the Google Play store page of the app
        "store_lang": "it", // the language of the Google Play store page of the app
        "latest_crawled_version": "1.5", // [not needed in the first run, it is automatically generated], 
        // it is the last version of the app crawled by covid-apps-observer 
        "latest_crawl": 1588275552 // [not needed in the first run, it is automatically generated], 
        // it is the timestamp in which the app has been crawled the last time 
    },
    // ...
]
```

If you want to analyze different apps, you will need to do the following:

* Modify the ``data/apps.json`` file according to your needs
* Delete all contents of the ``data`` folder (but not the ``data/apps.json`` file you just modified)

The rest is automatically managed by the tool.

Finally, you can launch the covid-apps-observer by running its main script as shown below.

```Shell
$ python covid-apps-observer.py
```

This will take quite some time in the first run since it will download the following data _for each_ Android app specified in the ``apps.json`` file, specifically:
* the Google Play metadata (i.e., what you see when you browse the Google Play webpage of a mobile app)
* the latest ``NUM_REVIEWS`` user reviews of the app (as specified in the ``configuration.py`` file)
* the APK file of the app

Moreover, a set of analyses is also executed for extracting and aggregating other information about the apps, such as their Android activities, used libraries, etc.

## Contributions

Any feedback, questions, and improvements about the project are very welcome, feel free to create an issue or pull request directly in this GitHub repository. 

## License

This software is licensed under the MIT License.