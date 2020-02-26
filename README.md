# flaskapp
new app








Create DB: 
1. set up models.py with a schema of the  tables 
2. import it into the app.py

3. add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

4.have the database know about the app
    DB.init_app(app)

5. Open Flask shell, create DB (ones)
 DB.create_all() - creates empty DB

6. Import schema from the flask shell: 
    from web_app.models import * 

7. Create fake users 
    u1=User(name='Ma', id=1123)

8. Add entries  to the DB 
    DB.session.add(u1)

9. Commit changes 
    DB.session.commit()


