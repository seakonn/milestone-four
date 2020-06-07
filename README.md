# Full Stack Frameworks Project

This project is an website for requesting commissions of art projects. The goal was to make a site utilising the Django web framework. Users should be able to login/register with the site, interact with the site's backend database via the website and be able to gain additional functionality by completing monetary transactions.

This is the fourth project as part of my [Code Institute](https://codeinstitute.net/) online diploma course.

---

## User Experience Design

### User Stories

These are potential actions that users of the website would want to perform. 

* As a user, I would like login/logout/register to the site.
* As a user, I would like to request an art commission.
* As a user, I would like to pay for my commission so I can receive it.

---

### Wireframes

![Homepage](static/wireframes/homepage.jpg "Homepage")

![Request Commissions](static/wireframes/request.jpg "Request Commissions")

![Profile Page](static/wireframes/profile.jpg "Profile Page")

## Database

Need to be able to store information commission requests recieved via forms on the site.

## Testing

### Base Html Page

This contains the navbar and footer amongst other things.

Login/Register links only appear when no user logged in.
Both links when clicked work correctly.
Request Commission/Profile/Logout only appear when user logged in.
All links work correctly when clicked on.

### Login Page

Testing form validation:
    Entering nothing, only email, only password will not let the form submit. Boxes are highlighted red by bootstrap.
    Entering correct username/wrong password, correct password/wrong username, wrong password/wrong username will result in error message at top of screen.
    Entering correct username/correct password will log user in and dispay javascript popup.

Clicking sign up link works correctly
Clicking reset password link works correctly

### Reset Password Page

Tested entering email address not in database, moves to password reset sent message.
Tested entering email address in database, does not work as expected. Results in 405 'method not allowed' error.

Known issue: User cannot navigate back to main site from the django page without using the back button.