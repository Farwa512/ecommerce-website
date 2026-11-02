# Ecommerce Website

A Flask e-commerce website with user login, product catalogue, search, shopping cart and Stripe payment (test mode). Data is stored in MySQL.

## Requirements

- Python 3.12
- MySQL 8
- git
- Optional: Stripe test keys (only needed for the payment page)

Python packages are listed in requirements.txt (Flask, Flask-SQLAlchemy, PyMySQL, Flask-Login, stripe, gunicorn).

## Run the website locally

1. Get the code and switch to the dev branch:

        git clone https://github.com/Farwa512/ecommerce-website.git
        cd ecommerce-website
        git checkout dev

2. Create a virtual environment and install the packages:

        python3 -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt

3. Create a database and a database user (use your own password):

        sudo mysql -e "CREATE DATABASE ecommerce_local; CREATE USER 'local_user'@'localhost' IDENTIFIED BY '<password>'; GRANT ALL PRIVILEGES ON ecommerce_local.* TO 'local_user'@'localhost'; FLUSH PRIVILEGES;"

4. Create a file named .env in the project folder:

        DATABASE_URL=mysql+pymysql://local_user:<password>@localhost/ecommerce_local
        SECRET_KEY=<any long random text>

   For payments, add STRIPE_SECRET_KEY and STRIPE_PUBLISHABLE_KEY (Stripe test keys). The .env file is listed in .gitignore and must never be committed.

5. Load the settings and start the server:

        set -a
        source .env
        set +a
        gunicorn -b 127.0.0.1:5001 app:app

   The tables are created automatically on the first start.

6. Open http://127.0.0.1:5001 in a browser, or check from the terminal:

        curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:5001/

   The answer should be 200.

## Create the first admin

Register a normal account on the /register page, then make it an admin:

    sudo mysql ecommerce_local -e "UPDATE user SET role='admin' WHERE email='<your email>';"

## Branches

- master: stable code
- dev: development work. Changes are tested on dev and merged into master with a pull request.
