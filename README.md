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
- 'cd' into app-backend/api
-  Create a virtual environment and install the dependencies specified in the "app-backend/api/requirements.txt" file. 
-  Run the following commands: 
``` bash
python manage.py migrate # Do it only for the first time (to set up the Django Backend DBs) .
python manage.py runserver # Start the server.
```

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
