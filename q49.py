# You have a dictionary default_settings = {'theme': 'light', 'language': 'English'} and a user-specific dictionary user_settings = {'theme': 'dark', 'font_size': '14px'}. Explain how you would combine these two dictionaries so that user_settings overrides the default settings where applicable. Use the update() method, the merge, in place merge operator

default_settings = {"theme": "light", "language": "English"}
user_settings = {"theme": "dark", "font_size": "14px"}

default_settings.update(user_settings)
print(default_settings)

new_settings = default_settings | user_settings  # merge operator
print(new_settings)

default_settings |= user_settings  # in place merge operator
print(default_settings)
