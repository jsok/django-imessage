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

You can find the database in your iOS backup:
`~/Library/Application Support/Mobile Sync/Backup/<device id>/3d0d7e5fb2ce288813306e4d4636395e047a3d28`

Screenshot
----------
![Screenshot](https://raw.github.com/jsok/django-imessage/master/screenshot.png)

Setup
-----
Requirements are:
 - django 1.4
 - pytz (for timezone info)
 - [UiUIKit 2.1](http://code.google.com/p/iphone-universal/)

1. edit `core/settings.py` and set your TIME_ZONE.
2. Then drop your SMS database in `db/sms.db` (rename it).
3. Unzip UiUIKit into `static/UiUIKit`
4. run `manage.py syncdb`
5. `manage.py runserver`
6. Point your browser at `http://localhost:8000/messages`, where you can browse your messages.

Future TODO
-----------
 - Messages.app style timestamps (supressed timestamps when messages are received within a given time delta)
 - Some way of searching your messages
 - Group chat isn't yet supported
