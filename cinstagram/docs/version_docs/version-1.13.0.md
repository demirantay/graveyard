# `Version 1.13.0`

# Design Summary

In this version all of the code is written in a extremely repetitive and inefficient way, however this was intentional. I did not want to spend time on the design aspect of the application since this is just a demo/pre-alpha stage of the application. I will re-iterate all of the code and make it better with SOLID, DRY, KISS, YAGNI principles.

Also I do want to note that this module of the application is extremely large, it is because this is one of the main core modules of the application. The reason that it is a core module is because essentially this module is the application itself. If you think about it instagram is just a big CRUD of photos and profile viewing (stalking :D ). And this module provides all of those features. To give an example for scalability or modularity reasons we can move the "about", "help_centre" apps job sections or other things to separate applications and buy host names such as "module_name.cinstagram.com" ... etc. But you cannot delete this module from the application.


# Frontend Updates

- I have already built the prealpha version templates in earlier versions so I did not update or built anything new in this version.

# Backend Updates

- I have added the modules necessary for the module in an earlier version that I forgot to document (1.11.0). Even though the models were not built in this version I still need to document them here for clarifying their use cases in views and templates of the app:
  ```
  class UserPhoto:
      id = primary key -- auto incrementing
      user = foreign key reference to CinstagramUser model
      photo = image
      creation_date = date field
      caption = text
      location = text

  class UserPhotoComment:
      id = primary key -- auto incrementing
      comment_owner = foreign key reference to CinstagramUser model
      comment_owner_settings = foreign key reference to CinstagramUserSettings
      commented_photo = foreign key reference to UserPhoto model
      comment = text
      creation_date = date field

  class UserPhotoLike:
      id = primary key -- auto incrementing
      like_owner = foreign key reference to CinstagramUser model
      like_owner_settings = foreign key reference to CinstagramUserSettings
      liked_photo = foreign key reference to UserPhoto model

  class UserPhotoBookmark:
      id = primary key -- auto incrementing
      bookmark_owner = foreign key reference to CinstagramUser model
      bookmarked_photo = foreign key reference to UserPhoto model
      bookmark_date = date field

  class UserFollowing:
      # followed account
      followed_id = int
      followed_user = foreign key reference to CinstagramUser model
      followed_user_settings = foreign key reference to CinstagramUserSettings

      # follower account
      follower_id = int
      follower_user = foreign key reference to CinstagramUser model
      follower_user_settings = foreign key reference to CinstagramUserSettings

  ```

- Fixed all of the necessary little bit details in the forms such as the needed `{% csrf token %}`s ... etc. Fixed url paths to other templates. As a note for the future the templates signaling and alerting system for the user is terrible. I just used `alert()` function of javascript's API for a temporary hold for the "+" (load more content) buttons, and did not put anything for the form validation, did not put any filtering options to the photos ... etc. . Those details needs to be improved.

- I coded these views:
  - Single post page: (`profile_single_post_page`)
  - Single post's likers page:  (`profile_post_likers`)
  - Followers page: (`profile_followers`)
  - Following page: (`profile_following`)
  - Profile's overview of posts: (`profile_posts_page`)
  - Profile's overview of saved posts: (`profile_saved`)
  - Profile's overview of tagged posts: (`profile_tagged`)
  - Other users single post page: (`other_users_profile_single_post_page`)
  - Other users single post's likers page: (`other_users_profile_post_likers`)
  - Other users followers page: (`other_users_profile_followers`)
  - Other users following page: (`other_users_profile_following`)
  - Other users profile overview: (`other_users_profile_posts_page`)
  - Other users profiles saved posts: (`other_users_profile_saved`)
  - Other users profiles tagged posts: (`other_users_profile_tagged`)

- You can find all of the newly added templates under the `~/cinstagram/templates/profile/*.html`

  view's pre-alpha phase. Since it is just in the pre-alpha I did not care a lot for tests, design principles such as DRY ...etc. There are a LOT of repetitive code. All of them will be fixed and the code will be improved a lot in the future versions.

# DevOps Updates

- At this version, there is no deployment or anything related to sysadmin stuff. I am just developing the app locally.

# Mobile Updates

- There are no mobile support at this version so no there are no updates.
