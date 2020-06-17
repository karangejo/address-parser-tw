
## Set Up

Clone the repo and run the following in a terminal:

```bash
virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
```
You will need to install a version of the chromedriver that matches the installed version on your machine from https://chromedriver.chromium.org/downloads and place it in the same directory.

Then you can load the script interactively or modify it!


## Pipeline

original dataset is testing_ds_20200529.csv

1) AddressTreeExtract.py has already generated the AddressTree.json

2) run parseAddresses.py to extract an address_obj and produce a new csv called extracted.csv

3) run AddressMatcher.py to test if address_obj matches the AddressTree and produce new csv called matched.csv

So far only about 30% of addresses match..