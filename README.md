# DJango-GoogleCalendar
Integrating Google Calendar in DJango

To test the app -> run the following command in cmd
    curl --verbose -L -d "user_name=MananS" http://localhost:8000/rest/v1/calendar/init | python -m json.tool

This will redirect you to a google authentication page, as I have currently used personal credentials, they wont work for you, but with suitable credentials and after giving permission, the app will access your calendar and list all events in it.
