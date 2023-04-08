from instagram_private_api import Client, ClientCompatPatch
from instagram_private_api import Client, ClientCompatPatch, ClientError, ClientLoginError

user_name = 'your_username'
password = 'your_password'

api = Client(user_name, password)
# results = api.user_info('leadz03')


# Get the user ID of the user with username 'example_user'
# user_id = api.username_info('leadz03')['user']['pk']
profile_url = api.username_info('selenagomez')['user']['hd_profile_pic_url_info']['url']
print(profile_url)
# Alternatively, you can get a Profile object for the user and call get_id
# profile = api.get_profile('leadz03')
# user_id = profile.get_id()

# Print the user ID
# info  = ClientCompatPatch.user(user_id)
# info = api.user_info(user_id)
# print(info)


# items = [item for item in results.get('feed_items', [])
#          if item.get('media_or_ad')]
# for item in items:
#     # Manually patch the entity to match the public api as closely as possible, optional
#     # To automatically patch entities, initialise the Client with auto_patch=True
#     ClientCompatPatch.media(item['media_or_ad'])
#     print(item['media_or_ad']['code'])