# Intelistyle Task
A SRR (server-side rendered) SPA (single page application) made as part of the Intelistyle recruitment process.

# Task description: 
_The task is to build a (single page) website that one can search for a garment (e.g. black dress) and it should display the garments that match the search criteria.
The website should load garments from this file: https://s3-eu-west-1.amazonaws.com/stylr-ai-engine-srv-data/srv/data/archive/zalando-women-07-10-2017/garment_items.jl_

### Tech stack: 
Back-end: DRF as a microservice for the S3 file. <br>
Front-end: Nuxt.js (Vue.js with SSR + Vuex + Vue-router)

### Tech stack in practice: 
 - The back-end creates has own database instance based on the loaded S3 file (_NOTE: the provided URL gave me an access denial so I created artificial data_).
 - Back-end is designed in a RESTful API fashion and gives paginated results from the DB query upon the HTTP endpoint call. It is also where the search feature logic resides.
 - It has two main endpoints: `api/garments` which returns ALL garments and `api/search` which returns only the garments with a given search query. (_There's also `api/garments/{GARMENT_ID}` endpoint avaiable that can be used and explored in the browsable API but I haven't used it on the front-end since the garment's "details" view was not in required to be implemented in this challenge_ ) 
 - Front-end is a server-side rendered Nuxt.js app - it has its own pre-configured Node.js server which handles the Vue.js SPA - this improves the SEO results compared to the "plain" SPA Vue.js / React.js apps. 
 - Front-end has two views: 'main' (index.vue) and 'search' (searchResults.vue).   
 - On the main view front-end calls the backend for ALL the garments and receives a paginated JSON response. 
 - On the search view front-end calls the `api/search/q="SEARCH_QUERY"` back-end endpoint and receives paginated response for the given search query.  

# Public URL to the app: <br> https://secret-brook-72301.herokuapp.com
URL to the backend API/Microservice the app uses: https://intelistyle-task-api.herokuapp.com/api/

-------
# How to set up locally: 
## Back-end 
#### Basic setup: 
- 'cd' into app-backend/api
-  Create a virtual environment and install the dependencies specified in the "app-backend/api/requirements.txt" file. 
-  Run the following commands: 
``` bash
python manage.py migrate # Do it only for the first time (to set up the Django Backend DBs) .
python manage.py runserver # Start the server.
```
- navigate to 'localhost:8000/api/'
- In order to be able to do the write and delete operations in the api view, do the following:
- Run the following command in terminal in 'app-backend/api' directory :
```bash
   python manage.py createsuperuser 
   # and then go answer the questions the terminal prompts you with
```
- navigate to 'localhost:8000/admin/' and login with your newly created credentials 
- navigate back to 'localhost:8000/api/' and notice how now you're able to do full CRUD of operations.   
#### Loading the S3 file: 
- remember to have "jsonfiles" python package installed (will install itself when pip installing from the requirements.txt file)
- inside api/api there's a file called "load_db_data.py". This file handles converting the data to an appropriate format and structure for django to be later loaded into the backend's database (see this django docs page: https://docs.djangoproject.com/en/2.2/howto/initial-data/) 
- Inside the file, remember to provide your own path to your big ".jl" file:
```python
   #REMEMBER to change this variable to yours '.jl' file's path.
   jsonl_file_path = os.path.join(os.path.dirname(BASE_DIR), "garment_items.jl") # CHANGE IF REPRODUCING WITH OWN DATA FILE
```
- run the file.
- Run two terminal commands from django-admin CLI (within the directory of your manage.py file, i.e. 'app-backend/api') : 
```bash
   python manage.py loaddata DB_LOAD-image_items.json
   python manage.py loaddata DB_LOAD-garment_items.json
```
- run django server (_python manage.py runserver_) and see all the data in your api.   

#### AWS S3 support: 
At the bottom of this project's Django's settings.py file you can see: 
```python
AWS_ACCESS_KEY_ID = os.environ.get('INTELISTYLE_TASK_AWS_ACCESS_KEY_ID') # Remember to provide your own env variable !
AWS_SECRET_ACCESS_KEY = os.environ.get('INTELISTYLE_TASK_AWS_SECRET_ACCESS_KEY')  # Remember to provide your own env variable !
AWS_STORAGE_BUCKET_NAME = 'intelistyle-task'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_PUBLIC_MEDIA_LOCATION = 'media/public'
DEFAULT_FILE_STORAGE = 'api.storage_backends.PublicMediaStorage'
```
- If you wish to ignore setting up AWS3, remove/comment out that section of code
- Otherwise, remember to provide your own env variables for AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. 



## Front-end
- cd into app-frontend
- Run the following commmands: (_Remember to have Node/NPM installed on your machine_)
``` bash
# install dependencies
$ npm run install

# serve with hot reload at localhost:3000
$ npm run dev 

```
- in _app-frontend/nuxt.config.js_ swap the env values to "http://localhost:8000/api/" to make calls to your local backend instead of the public one I deployed 

```javascript
// Instead of this:
env: {
    apiBaseUrl:
      process.env.BASE_URL || 'https://intelistyle-task-api.herokuapp.com/api/'
  },
// Replace it with this:
env: {
    apiBaseUrl:
      process.env.BASE_URL || 'https://localhost:8000/api/'
  },
// This can be automated by tweaking nuxt.config.js to have a 'dev' and 'production' env variable but I left it as something to consider.
```
