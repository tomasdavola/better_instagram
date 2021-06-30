Hi!, this is my first pip package so sorry if its rough around the edges,

The BetterInstagram package is an 'API like' package used to get information about a users account on instagram(even if they're private)

I say 'API like' because its technically not an API at all although I structured it like one, in reality it acts like a bunch of webscraping macros which is running in the background(don't tell the feds).

More functions coming soon which will make this more powerful than public acount APIs.

Hope you enjoy! and feel free to message me if u have feedback.

github: oyas4572

email: third4572@gmail.com

discord: tms#472

pypi: oyas

note: chrome is needed for this package(driver will come with the package)


Usage
=====

  from better_instagram import better_instagram as bi


Documentation
=========
login(username,password):
Activates browser and logs you in to access private accounts
    login(username="leomessi",password="Goat1234")


    getUser(username):
Accesses a user's account and extracts their basic information,(returns a dictionary). You can use this function without logging in but Instagram may force a login on smaller accounts.
    ->print(getuser("leomessi"))
    {'username': 'leomessi', 'name': 'Leo Messi', 'biography': 'Bienvenidos a la cuenta oficial de Instagram de Leo Messi / Welcome to the official Leo Messi Instagram account', 'posts': '731', 'followers': '224m', 'following': '236', 'is_verified': True, 'website': 'messi.com', 'are_you_following': True, 'url': 'https://www.instagram.com/leomessi/}


ChangeLog
=========

0.2 (WIP)
 * Converting to class to remove global variables.
 * Adding getposts(), getfollowers() and getfollowing()

0.1 (30-06-2021)
 * Can access basic account information for both private and public instagram accounts



ily if u read this far.