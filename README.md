# scraperFlaskApp
After cloning, create a virtual environment and install the requirements. For Linux and Mac users:

    $ virtualenv env
    $ source env/bin/activate
    (env) $ pip install Flask PyMongo flask-pymongo

If you are on Windows, then use the following commands instead:

    $ virtualenv venv
    $ env\Scripts\activate
    (env) $ pip install Flask PyMongo flask-pymongo

Running
-------

To run the server use the following command:

    (venv) $ python rest.py
     * Running on http://127.0.0.1:5000/
     * Restarting with reloader

Then from a different terminal window you can send requests.
