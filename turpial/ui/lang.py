# -*- coding: utf-8 -*-

# Module to handle i18n

import os
import gettext

# Initialize gettext
gettext_domain = 'turpial'
# localedir definition in development mode
if os.path.isdir(os.path.join(os.path.dirname(__file__), '..', 'i18n')):
    localedir = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'i18n'))
    trans = gettext.install(gettext_domain, localedir)
    log.debug('LOCALEDIR: %s' % localedir)
else:
    trans = gettext.install(gettext_domain)

STRINGS = {
    'welcome': _('Welcome!'),
    'twitter': 'Twitter',
    'identica': 'Identi.ca',
    'add_new_account': _('Add a new account'),
    'to_start_using_turpial': _('to start using Turpial'),
    'you_have_accounts_registered': _('You have accounts registered, now'),
    'add_some_columns': _('add some columns'),
    'update_status': _('Update status'),
    'send_direct_message': _('Send direct message'),
    'settings': _('Settings'),
    'preferences': _('Preferences'),
    'about_turpial': _('About Turpial'),
    'search': _('Search'),
    'account': _('Account'),
    'accounts': _('Accounts'),
    'columns': _('Columns'),
    'authorize_turpial': _('Authorize Turpial'),
    'type_the_pin': _('Type the PIN'),
    'save': _('Save'),
    'copy_the_pin': _('Authorize Turpial and copy the PIN in the text box'),
    'user_profile': _("User Profile"),
    'bio': _("Bio"),
    'location': _("Location"),
    'web': _("Web"),
    'tweets': _('Tweets'),
    'following': _('Following'),
    'followers': _('Followers'),
    'favorites': _('Favorites'),
    'criteria': _('Criteria'),
    'criteria_tooltip': _('Use hashtags, mentions or any text you want as search criteria'),
    'select_friend_to_send_message': _('Select friend to send message'),
    'friend': _('Friend'),
    'select': _('Select'),
    'load_friends_list': _('Load friends list'),
    'whats_happening': _("What's happening?"),
    'upload_image': _("Upload image"),
    'short_urls': _("Short URLs"),
    'update': _('Update'),
    'delete_column': _("Delete Column"),
    'now': _("now"),
    'retweeted_by': _("Retweeted by"),
    'new': _('New'),
    'delete': _('Delete'),
    'relogin': _('Relogin'),
    'register_a_new_account': _('Register a new account'),
    'delete_an_existing_account': _('Delete an existing account'),
    'register_a_twitter_account': _('Register a Twitter account'),
    'register_an_identica_account': _('Register an Identi.ca account'),
    'no_registered_accounts': _('No registered accounts'),
    'error_registering_new_account': _('Error registering new account'),
    'broadcast': _('Broadcast'),
    'you_can_not_submit_an_empty_message': _("You can not submit an empty message"),
    'message_too_long_it_looks_like_a_testament': _("Message too long, it looks like a testament"),
    'view_conversation': _("View conversation"),
    'hide_conversation': _("Hide conversation"),
    'reply': _('Reply'),
    'quote': _('Quote'),
    'retweet': _('Retweet'),
    'mark_as_favorite': _('Mark as favorite'),
    'remove_from_favorites': _('Remove from favorites'),
    'reply_to': _('Reply to'),
    'quoting': _('Quoting'),
    'confirm_retweet': _('Confirm Retweet'),
    'do_you_want_to_retweet_status': _('Do you want to retweet this status to all your friends?'),
    'confirm_delete': _('Confirm Delete'),
    'do_you_want_to_delete_status': _('Do you want to delete this status?'),
    'do_you_want_to_delete_direct_message': _('Do you want to delete this direct message?'),
    'loading': _('Loading...'),
    'status_repeated': _('Status repeated'),
    'status_deleted': _('Status deleted'),
    'direct_message_deleted': _('Direct message deleted'),
    'status_marked_as_favorite': _('Status marked as favorite'),
    'status_removed_from_favorites': _('Status removed from favorites'),
    'send_message_to': _('Send message to'),
    'follow': _('Follow'),
    'follow_requested': _('Follow requested'),
    'unfollow': _('Unfollow'),
    'mute': _("Mute"),
    'unmute': _("Unmute"),
    'block': _("Block"),
    'report_as_spam': _("Report as spam"),
    'this_is_you': _("This is you!"),
    'conversation': _("Conversation"),
    'quit': _('Quit'),
    'in_progress': _("In progress..."),
    'select_one_account_to_post': _("Select one account to post"),
    'image_preview': _("Image Preview"),
    'confirm_discard': _('Confirm Discard'),
    'do_you_want_to_discard_message': _('Do you want to discard this message?'),
    'info': _('Info'),
    'recent': _('Recent'),
    'empty_message': _('Empty message'),
    'select_account': _('Select account'),
    'delete_account_confirm': _("Do you really want to delete the account %s?"),
    'messages_queue': _('Messages queue'),
    'delete_selected_message': _('Delete selected message'),
    'delete_all': _('Delete all'),
    'delete_all_messages_in_queue': _('Delete all messages in queue'),
    'message': _('Message'),
    'delete_message_from_queue_confirm': _('Do you want to delete this message from the queue?'),
    'clear_message_queue_confirm': _('Do you want to clear the queue?'),
    'messages_will_be_send': _('Messages will be send every %s as long as Turpial remain open'),
    'next_message_should_be_posted_at': _('Next message should be posted at'),
    'add_to_queue': _('Add to Queue'),
    'about_description': _('Microblogging client written in Python'),
    'you_are_now_following': _("You are now following @%s"),
    'you_are_no_longer_following': _("You are no longer following @%s"),
    'has_been_reported_as_spam': _("@%s has been reported as spam"),
    'has_been_blocked': _("@%s has been blocked"),
    'has_been_muted': _("@%s has been muted"),
    'has_been_unmuted': _("@%s has been unmuted"),
    'message_from_queue_has_been_posted': _('Message from queue has been posted'),
    'close': _('Close'),
    'general': _('General'),
    'notifications': _('Notifications'),
    'services': _('Services'),
    'web_browser': _('Web Browser'),
    'filters': _('Filters'),
    'proxy': _('Proxy'),
    'advanced': _('Advanced'),
    'general_tab_description': _("Adjust update frecuency and other general parameters"),
    'notifications_tab_description': _("Select the notifications you want to receive from Turpial"),
    'web_browser_tab_description': _('Setup your favorite web browser to open links'),
    'services_tab_description': _("Select your preferred service to short URLs and upload images"),
    'proxy_tab_description': _("Proxy settings for Turpial (Need Restart)"),
    'advanced_tab_description': _("Advanced options. Please, keep away unless you know what you are doing"),
    'update_frecuency': _("Update frecuency"),
    'queue_frecuency': _("Queue frecuency"),
    'statuses_per_column': _("Statuses per column"),
    'minimize_on_close': _("Minimize on close"),
    'notify_on_updates': _("Notify on updates"),
    'notify_on_actions': _("Notify on actions"),
    'sound_on_login': _("Sound on login"),
    'sound_on_updates': _("Sound on updates"),
    'use_default_browser': _("Use default browser"),
    'set_custom_browser': _("Set custom browser"),
    'command': _("Command"),
    'clean_cache': _("Clean cache"),
    'delete_all_files_in_cache': _("Delete all files in cache"),
    'restore_config_to_default': _("Restore configuration to default"),
    'restore_config': _("Restore config"),
    'socket_timeout': _("Socket timeout"),
    'show_avatars': _("Show user avatars"),
    'type': _("Type"),
    'host': _("Host"),
    'port': _("Port"),
    'with_authentication': _("With authentication"),
    'username': _("Username"),
    'password': _("Password"),
    'filters': _("Filters"),
    'add_filter': _("Add filter"),
    'create_a_new_filter': _("Create a new filter"),
    'delete_selected_filter': _("Delete selected filter"),
    'delete_all_filters': _("Delete all filters"),
    'clear_filters_confirm': _('Do you want to clear all the filters?'),


    #'no_registered_columns': ,
    #'reply_status': _('Reply status'),
    #'add_account': _('Add account'),
    #'columns': _('Columns'),
    #'column': _("Column"),
    #'create_account': _('Create Account'),
    #'login': _('Login'),
    #'add': _('Add'),
    #'retweeted': _('Retweeted'),
    #'redent': _('Redent'),
    #'redented': _('Redented'),
    #'favorited': _('Favorited'),
    #'show_all': _('Show all'),
    #'tweet': _('Tweet'),
    #'new_tweet': _('New Tweet'),
    #'new_tweets': _('New Tweets'),
    #'dent': _('Dent'),
    #'dents': _('Dents'),
    #'new_dent': _('New Dent'),
    #'new_dents': _('New Dents'),
    #'posts': _('Posts'),
    #'user_and_password': _('User and password'),
    #'protocol': _('Protocol'),
    #'signin': _('Sign In'),
    #'save': _('Save'),
    #'ok': _('Ok'),
    #'accept': _('Accept'),
    #'cancel': _('Cancel'),
    #'public_timeline': _('Public Timeline'),
    #'saving': _('Saving...'),
    #'connecting': _('Connecting...'),
    #'authenticating': _('Authenticating...'),
    #'authorizing': _('Authorizing...'),
    #'secure_auth': _('Secure Authentication'),
    #'login_cancelled': _('Login cancelled by user'),
    #'invalid_pin': _('You must write a valid PIN'),
    #'delete_column_confirm': _("Do you really want to delete the column "),
    #'fields_cant_be_empty': _("Fields can't be empty"),
    #'from': _("from"),
    #'people': _("people"),
    #'person': _("person"),
    #'no_column_yet': _("There are no available columns because I'm still logging in"),
    #'retweeting': _("Retweeting..."),
    #'unretweeting': _("Undoing retweet..."),
    #'retweet_successfully_undone': _("Retweet successfully undone"),
    #'adding_to_fav': _("Adding to favorites..."),
    #'removing_from_fav': _("Removing from favorites..."),
    #'deleting': _("Deleting..."),
    #'short': _("Short"),
    #'image': _("Image"),
    #'updating_status': _("Updating status..."),
    #'error_posting_to': _("Error posting to %s"),
    #'manual_update': _("Manual Update"),
    #'logged_in': _("Logged In"),
    #'message': _("Message"),
    #'requested': _("Requested"),
    #'add_friend': _('Add friend'),
    #'loading_friends': _('Loading friends...'),
    #'friends': _('friends'),
    #'friend': _('friend'),
    #'friends_loaded_successfully': _('Friends loaded successfully'),
    #'shorting_urls': _('Shorting URLs...'),
    #'direct_messages': _('Direct Messages'),
    #'direct_message': _('Direct Message'),
    #'can_send_message_to_one_account': _("Wait! I just can send messages to \
    #one account at once"),
    #'sending_message': _('Sending message...'),
    #'direct_message_sent_successfully': _('Direct message sent successfully'),
    
    #'restore_config_warning': _('This action will close Turpial and will \
    #delete your current config (you must start Turpial again). Do you want to \
    #continue?'),
    #'view_profile': _('View profile'),
    #'search_profile_in': ('Search profile in'),
    #'profiles': _('Profiles'),
    #'sound': _('Sound'),
    #'notificate': _('Notificate'),
    #'confirm_undo_retweet': _('Confirm Undo Retweet'),
    #'do_you_want_to_undo_repeat_status': _('Do you want to undo this repeat?'),
    #'confirm_unfollow': _('Confirm Unfollow'),
    #'do_you_want_to_unfollow_user': _('Do you want to unfollow @%s?'),
    #'error_loading_image': _('Error loading image'),
    #'credentials_could_not_be_empty': _('Credentials could not be empty'),
    #'file_not_found': _("File not found"),
    #'i_couldnt_update_status': _("Oh oh... I couldn't update your status"),
    #'url_already_short': _('URL already short'),
    #'no_url_to_short': _('There are no URLs to short'),
    #'couldnt_shrink_urls': _("Oops... I couldn't shrink all URLs"),
    #'this_search_support_advanced_operators': _('This search supports advanced operators like:'),
    #'for_more_information_visit': _('For more information visit'),
    #'twitter_search_documentation': _('Twitter Search Documentation'),
    #'error_loading_profile': _('Error loading profile'),
    #'reply_message_to': _('Reply message to'),
    #'less_than_a_minute': _('Less than a minute'),
    #'minute_ago': _('minute ago'),
    #'minutes_ago': _('minutes ago'),
    #'hour_ago': _('hour ago'),
    #'hours_ago': _('hours ago'),
}

class i18n:
    @staticmethod
    def get(key):
        try:
            return STRINGS[key]
        except KeyError:
            return key
