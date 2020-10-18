source ../venv/bin/activate
python ./covid_apps_observer.py -i ../data/data_community -an "Ivano Malavolta" -ae ivanomalavolta@gmail.com -rt "COVID-related Android apps by the community"
python ./covid_apps_observer.py -i ../data/data_nl_custom -an "Ivano Malavolta" -ae ivanomalavolta@gmail.com -rt "COVID-related Android apps - custom search for the Dutch store"
python bulk_analysis.py -i ../data -an "Ivano Malavolta" -ae ivanomalavolta@gmail.com
