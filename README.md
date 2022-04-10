# recsys_project
RecSys project: flask

Install requirements:
```commandline
pip install requirements.txt
pip install requirements-dev.txt
```

To obtain data:
```
dvc init
dvc pull -r my_gdrive_remote
```

Build docker image and run:
```commandline
docker build -t <IMAGE_NAME> .
docker run -p 5000:5000 -v <ABSOLUTE_PATH_LOCAL>:/app/res <IMAGE_NAME>
```
where <ABSOLUTE_PATH_LOCAL> is an absolute path to folder on your machine that will contain result.txt file for batch predictions.

Go to 
```commandline
http://127.0.0.1:5000
```
to get predictions.