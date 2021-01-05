# Cinstagram Clone

## `Discuss`

The thing is I cannot discuss an idea that already exists, Instead of discussing the application, I can reverse engineer all of it's features to the bones. But the main idea is to be structured with your development/work cycle so that everything does not get mingled together.

<br>
<br>

## `Design`

Normally in a normal application dev-cycle there would be a plan section where we would design the site starting from the wireframes -> design -> frontend -> backend -> devpops -> deployment ... etc. But since the designs are already ready, I will just start from the frontend step.

The most important thing to remember is to do the easy thing first. For example pages like home page, programmer panel, bot control panel ... etc. are "container" pages (which holds nearly all of the applications of te site) so they should be built at last.

<br>
<br>

## `Plan`

Instagram is a huge application to clone, it is not just some basic CRUD application. Forutentally most of the applications are small and compact enough or defined-well-enough to be modulirized from the others. Try to do the following in versions:

### Front-end

---
- [x] Help Centre app pages
- [x] About app pages
---
- [x] API-web
- [x] Signup/Login
- [x] Profile Settings
---
- [x] Photo Video Upload
- [x] Public Profile
- [x] Private Profile
---
- [x] Chat
- [x] Search
---
- [x] explore
- [x] Home
---
- Start using frontend framework: probably react (module the elements)
---
- [ ] react:: help centre app pages
- [ ] react:: About app pages
- [ ] react:: API-web
---
- [ ] react:: Signup/Login
- [ ] react:: Profile Settings
---
- [ ] react:: Photo Video Upload
- [ ] react:: Public Profile
---
- [ ] react:: Private Profile
---
- [ ] react:: Chat
---
- [ ] react:: Home
- [ ] react:: Search
---
- [ ] react:: explore


<br>

### Back-end

---
- [x] Basic Programmer Panel (key verification)
- [x] Admin Panel
---
- [x]  Basic Configuration
- [x]  Basic URL Pathing system
---
- [ ] Basic Help Centre
    - Note: There are lots of pages but they are not static it is just one big
      CRUD app, you can use drop-view for headers instead of that weird shift
---
- [ ] Basic About app
  - Note: Index about use, jobs CRUD app, necessary legal parts
---
- [ ] Basic API WEB-CRUD info app
  - Note: this is not the API creation it is just web app part of it
---
- [ ]  Basic Signup system
- [ ]  basic login sys
---
- [ ] Basic Profile Settings app
  - Note: edit, profile, change password, authorized applications, email and sms, manage contacts, privacy and ecurity, login activity
---
- [ ] Basic Photo & Video upload app
---
- [ ] Basic Public Profile
---
- [ ] Basic Private Profile App
  - note: (follow, unfollow ... etc. funcitonality)
---
- [ ] Basic Chat app
---
- [ ] Basic Home app
---
- [ ] Basic Search Indexes app (this is on the navbar on web page it is note explore)
  - Note: Account Search, Tag search (shop, travel, sports), location serach, hashtag search
---
- [ ] Basic Explore app
  - Note: Explore index, person search , hashtag search, tag search
---
- [ ] secure all of the features above
  - Note: This is the end of the normal basic version now we start improving it
---
- [ ] Fully-finish configuration
- [ ] URL pathing system
---
- [ ] Fully-finish Help Centre
---
- [ ] Fully-finish About app
---
- [ ] Fully-finish signup system
- [ ] Fully-finish login system
---
- [ ] Fully finish Profile Settings app
---
- [ ] Fully finish Photo-video upload
---
- [ ] Fully finish public profile
---
- [ ] fully finish private profile
---
- [ ] Fully finish chat section
---
- [ ] Fully finish Home App
---
- [ ] Fully finish search indexes
---
- [ ] Fully finish explore app
---
- [ ] Fully finish admin panel
---
- [ ] Fully finish programmer panel
---
- [ ] Fully-finish API section
- [ ] Write Bots for:
  - Note: the reason there are specific bots are becasue I want to test out each feature and if it will break under a lot of request, the magnitude of data will be controlled thorugh bot control panel in admin panel
  - __admin bot__: from time to time delees bad users post, suspends their accoutns ... etc.
  - __bad bot__  : intentianlly bad user to get caught to the admin
  -  __user:bot__: try to mimick real personalities for example use real isntagrams real pages and photographies to create virtual clones of those people. For example joe rogan-clone uploads every post that joe rogan uploads but in a timely manner, changes it settings, logs in, logs out, chats with other bots ... etc.
  - __hacker bot__: intentionally tries to hack the site ddos attacks ... etc.
---
- [ ] add the specific bot control panel: add shit like how many bots of each bot you want at a certain point in time ... etc.
---
- [ ] Do the Security Fully
---
- [ ] Scalability. (most important thing, how to scale so that storing and serving billions of images in a day is not a problem)
---
- [ ] Keep maintaining the bugs, all application ... etc. start native part

<br>

### Native

---
- [ ] Basic Programmer Panel (key verification)
- [ ] Admin Panel
---
- [ ]  Basic Configuration
- [ ]  Basic URL Pathing system
---
- [ ] Basic Help Centre
    - Note: There are lots of pages but they are not static it is just one big
      CRUD app, you can use drop-view for headers instead of that weird shift
---
- [ ] Basic About app
  - Note: Index about use, jobs CRUD app, necessary legal parts
---
- [ ] Basic Press app
  - Note: Info center, our story, brand assets
---
- [ ] Basic API WEB-CRUD info app
  - Note: this is not the API creation it is just web app part of it
---
- [ ]  Basic Signup system
- [ ]  basic login sys
---
- [ ] Basic Profile Settings app
  - Note: edit, profile, change password, authorized applications, email and sms, manage contacts, privacy and ecurity, login activity
---
- [ ] Basic Photo & Video upload app
---
- [ ] Basic Public Profile
---
- [ ] Basic Private Profile App
  - note: (follow, unfollow ... etc. funcitonality)
---
- [ ] Basic Chat app
---
- [ ] Basic Home app
---
- [ ] Basic Search Indexes app (this is on the navbar on web page it is note explore)
  - Note: Account Search, Tag search (shop, travel, sports), location serach, hashtag search
---
- [ ] Basic Explore app
  - Note: Explore index, person search , hashtag search, tag search
---
- [ ] secure all of the features above
  - Note: This is the end of the normal basic version now we start improving it
---
- [ ] Fully-finish configuration
- [ ] URL pathing system
---
- [ ] Fully-finish Help Centre
---
- [ ] Fully-finish About app
---
- [ ] Fully-finish Press app
---
- [ ] Fully-finish signup system
- [ ] Fully-finish login system
---
- [ ] Fully finish Profile Settings app
---
- [ ] Fully finish Photo-video upload
---
- [ ] Fully finish public profile
---
- [ ] fully finish private profile
---
- [ ] Fully finish chat section
---
- [ ] Fully finish Home App
---
- [ ] Fully finish search indexes
---
- [ ] Fully finish explore app
---
- [ ] Fully finish admin panel
---
- [ ] Fully finish programmer panel
---
- [ ] Do the Security Fully
---
- [ ] Scalability. (most important thing, how to scale so that storing and serving billions of images in a day is not a problem)
----
- [ ] Keep maintaining the bugs, all application ... etc. start native part

<br>

### Deployment

... it will come more once i learn more about devops

- [ ] Learn about deployment etc. I do not know the specifics of DevOPS I will update it once I got more info on DevOPS.
- [ ] Try to ask for funds from different various companies, IRC chats etc. if no figure something out.
---
- [ ] Check if it scales right use the bot contorl panel to handle 4 billion
requests spread out to a monthly basis. See if the site can handle it. This has been the entire goal of this project
---
