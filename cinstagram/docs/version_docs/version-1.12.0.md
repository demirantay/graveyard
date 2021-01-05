# `Version 1.10.0`

# Design Summary

In this version first and foremost I ported all of the app to Django because I knew flask would take to much time to build this app with. And I figured it would be the time to port it since it would be so hard to do in the future due to the size o the project.

# Frontend Updates

- I have already built the prealpha version templates in earlier versions so I did not update or built anything new in this version.

# Backend Updates

- First I ported all of the app to django instead of flask

- I have added a big `settings` model for the module:
  ```
  `class CinstagramUserSettings:
    id = primary key -- auto incrementing
    settings_owner = one-to-many reference to CinstagramUser
    profile_photo = image
    full_name = text
    username = text
    personal_url = text
    bio = text
    email = text
    phone_number = int
    gender = text

    # Email & Sms -- settings
    feedback_emails = bool
    reminder_emails = bool
    product_emails = bool
    news_emails = bool
    sms_messages = bool

    # Privacy & Security -- settings
    private_account = bool
    turn_off_comments = bool
  ```

- Fixed all of the necessary little bit details in the forms such as the needed `{% csrf token %}`s ... etc. Fixed url paths to other templates. As a note for the future the templates signaling and alerting system for the user is terrible. I just used `alert()` function of javascript's API for a temporary hold for the "wrong/empty input" alerts for the form validation. That needs to be improved.

- I coded the:
  - edit profile (`profile_settings_edit_profile`)
  - change password (`profile_settings_change_password`)
  - email and sms (`profile_settings_email_sms`)
  - privacy and security (`profile_settings_privacy_security`)

  view's pre-alpha phase. Since it is just in the pre-alpha I did not care a lot for tests, design principles such as DRY ...etc. There are a LOT of repetitive code. All of them will be fixed and the code will be improved a lot in the future versions.

# DevOps Updates

- At this version, there is no deployment or anything related to sysadmin stuff. I am just developing the app locally.

# Mobile Updates

- There are no mobile support at this version so no there are no updates.
