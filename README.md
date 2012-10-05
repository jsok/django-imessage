iMessage SMS database browsing web app
======================================

What?
-----
iOS stores all your SMS/Messages in a sqlite database. This gets downloaded to your computer each time you backup/sync your phone via iTunes.

This is a django app which allows you to drop your SMS database into it, fire it up and have all your messages in a nice browseable web app.

Why?
----
Why not? iOS will only show the most recent 100 or so messages on the screen, to view older ones you need to hit "Load Earlier Messages" and wait. Too bad if you want to see messages from last month, or even last year! With this app you can see them all and search them.

How?
----
The SMS database has been analysed by many and its schema is well known. I've taken some of this info and used it to convince django's ORM into reading it.

Setup
-----
Requirements are:
 - django 1.4
 - pytz (for timezone info)

1. edit `core/settings.py` and set your TIME_ZONE.
2. Then drop your SMS database in `db/sms.db`.
3. run `manage.py syncdb`
4. `manage.py runserver`
5. Point your browser at the admin page `http://localhost:8000/admin`, where you can browse your messages.

Future TODO
-----------
 - A frontend which remotely resembles Messages.app to browse your SMSes
 - Some way of searching your messages
 - Group chat isn't yet supported
