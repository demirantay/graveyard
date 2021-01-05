# `Version 1.10.0`

# Design Summary

In this version I implemented a extremely basic CRUD implementation to the login,
signup system to the site. The code written extremely poorly because I just wanted to quickly have a working prototype. The passwords doesn't even have hashing at the moment.

# Frontend Updates

- Updated the templated for the temporary control panel since I needed a new control form for the new `User` class

# Backend Updates

- I have added a new model called the `User` the tables definition looks like this: code is (# pseudo-code)
  ```
  class User:
    id = primary key - auto incrementing
    email = string column
    full_name = string column
    username = string column
    password = string column
  ```

- Created a signup system in the `auth.signup` view. The algorithm for it is inefficient there is no data structure to store the data efficiently I will change it later on.

- Created a login system in the `auth.login` view. To be honest i do not know what algorithm does `flask`s .filter() function use. it can be a brute force and a O(n). I will need to change it to divide and conquer and bump the speed to O(logn)

- Fixed the templates in signup and login system and connected both to their respective view functions. However the data that is being transmitted through the forms are still not encrypted "I NEED TO FIX IT"


- Important: The security literally does not exist at the moment I just stored the password in normal string. It is intentional I am going to encrypt it in the future versions I just wanted build a working simple prototype fast.

- Added a little update form for the `User` class in temporary control panel to create mock-users on the go while developing the app.



# DevOps Updates

- At this version, there is no deployment or anything related to sysadmin stuff. I am just developing the app locally.

# Mobile Updates

- There are no mobile support at this version so no there are no updates.
