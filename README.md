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

Links:
    Login/Register links only appear when no user logged in.
    Both links when clicked work correctly.
    Request Commission/Profile/Logout only appear when user logged in.
    All links work correctly when clicked on.
    Link to homepage in top left works when clicked on.

### Login Page

Testing form validation:
    Entering nothing, or missing required field (email, password): Form will not submit. Boxes are highlighted red by bootstrap.
    Entering correct username/wrong password, correct password/wrong username, wrong password/wrong username: Error message at top of screen. Does not submit.
    Entering correct username/correct password will log user in and dispay javascript popup.

Clicking sign up link works correctly
Clicking reset password link works correctly

### Reset Password Page

Form validation:
    Tested entering email address not in database: moves to password reset sent message.
    Tested entering email address in database: does not work as expected. Results in 405 'method not allowed' error.

Known issue:
    User cannot navigate back to main site from the django page without using the back button.

### Register Account Page

Form validation:
    Entering no info in form or missing required field(username, either password): form does not submit. Red highlights around boxes with required info.
    Entering username that already exists: error message appears and form does not submit.
    Using email that is in database: error message appears and form does not submit.
    Entering mismatching passwords: error message appears and form does not submit.
    Entering email that already exists: error message appears and form does not submit.
    Entering correct information in all fields: form submits and javascript popup appears. User is redirected.

Known issue:
    Email address is not required. Form will submit when email field is left blank.

### Request Commission Page

Form validation:
    Entering no info or missing required field(name, description): form does not submit. Required fields highlighted.
    Entering valid info to required fields: form submits, user redirected to profile page.

Known issue:
    Commission type dropdown defaults to Statue.

### Commission Page

Link:
    Link to payment page works when clicked on.

### Profile Page

Links:
    All links to individual commissions work when clicked on.
    Link to request commission page only appears when no commissions have been made.
    Link to request commission page works when clicked on.