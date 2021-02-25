## interactive_story_1_with_email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "valid"}
    - utter_ask_location
* restaurant_search{"location": "Agra"}
    - slot{"location": "Agra"}
    - action_validate_location
    - slot{"location_valid": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "299"}
    - slot{"budget": "299"}
    - action_search_restaurants
    - slot{"location": "Agra"}
    - utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"emailid": "ankitmhjn5@gmail.com"}
    - slot{"emailid": "ankitmhjn5@gmail.com"}
    - action_send_details
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_2_no_email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "valid"}
    - utter_ask_location
* restaurant_search{"location": "bhopal"}
    - slot{"location": "bhopal"}
    - action_validate_location
    - slot{"location_valid": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "300"}
    - slot{"budget": "300"}
    - action_search_restaurants
    - slot{"location": "bhopal"}
    - utter_ask_details
* deny
    - utter_no_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_3_with_invalid_cuisine_valid_location
* greet
    - utter_greet
* restaurant_search{"cuisine": "Korean", "location": "bikaner"}
    - slot{"cuisine": "Korean"}
    - slot{"location": "bikaner"}
    - action_validate_location
    - slot{"location_valid": "valid"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "invalid"}
    - utter_invalid_cuisine
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "300"}
    - slot{"budget": "300"}
    - action_search_restaurants
    - slot{"location": "bikaner"}
    - utter_ask_details
* goodbye
    - utter_goodbye
    - action_restart


## interactive_story_4_invalid_location_and_goodbye
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_validate_location
    - slot{"location_valid": "invalid"}
    - utter_invalid_location
    - utter_ask_location
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_5_abuse
* greet
    - utter_greet
* abuse
    - utter_reply_abuse
    - action_restart

## interactive_story_6_invalid_cuisine_no_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "gujrati"}
    - slot{"cuisine": "gujrati"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "invalid"}
    - utter_invalid_cuisine
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "701"}
    - slot{"budget": "701"}
    - utter_ask_location
* restaurant_search{"location": "bhilai"}
    - slot{"location": "bhilai"}
    - action_validate_location
    - slot{"location_valid": "valid"}
    - action_search_restaurants
    - slot{"location": "bhilai"}
    - utter_ask_details
* deny
    - utter_no_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_7_valid_cuisine_and_location
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"location_valid": "valid"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "300"}
    - slot{"budget": "300"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_ask_details
* ask_email{"emailid": "ankitmhjn5@gmail.com"}
    - slot{"emailid": "ankitmhjn5@gmail.com"}
    - action_send_details
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_8_invalid_cuisine_valid_location
* greet
    - utter_greet
* restaurant_search{"cuisine": "odiya"}
    - slot{"cuisine": "odiya"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "invalid"}
    - utter_invalid_cuisine
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "299"}
    - slot{"budget": "299"}
    - utter_ask_location
* restaurant_search{"location": "thane"}
    - slot{"location": "thane"}
    - action_validate_location
    - slot{"location_valid": "valid"}
    - action_search_restaurants
    - slot{"location": "thane"}
    - utter_ask_details
* deny
    - utter_no_email
* goodbye
    - utter_goodbye
    - action_restart
    

## interactive_story_9_invalid_location_invalid_cuisine_abuse
* greet
    - utter_greet
* restaurant_search{"cuisine": "hyderabadi", "location": "india"}
    - slot{"cuisine": "hyderabadi"}
    - slot{"location": "india"}
    - action_validate_location
    - slot{"location_valid": "invalid"}
    - utter_invalid_location
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location_valid": "valid"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "invalid"}
    - utter_invalid_cuisine
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
* abuse
    - utter_reply_abuse
    - action_restart

## interactive_story_10_invalid_location_invalid_cuisine_email_reply_abuse
* greet
    - utter_greet
* restaurant_search{"cuisine": "japanese", "location": "allahabad"}
    - slot{"cuisine": "japanese"}
    - slot{"location": "allahabad"}
    - action_validate_location
    - slot{"location_valid": "invalid"}
    - utter_invalid_location
    - utter_ask_location
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - action_validate_location
    - slot{"location_valid": "valid"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "invalid"}
    - utter_invalid_cuisine
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "300"}
    - slot{"budget": "300"}
    - action_search_restaurants
    - slot{"location": "agra"}
    - utter_ask_details
* abuse
    - utter_reply_abuse
    - action_restart

## interactive_story_11_chat_start_abuse
* abuse
    - utter_reply_abuse
    - action_restart

## interactive_story_12_complete_path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "valid"}
    - utter_ask_location
* restaurant_search{"location": "aligarh"}
    - slot{"location": "aligarh"}
    - action_validate_location
    - slot{"location_valid": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "299"}
    - slot{"budget": "299"}
    - action_search_restaurants
    - slot{"location": "aligarh"}
    - utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"emailid": "ankitmhjn5@gmail.com"}
    - slot{"emailid": "ankitmhjn5@gmail.com"}
    - action_send_details
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_13_invalid_loc_multiple_times
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - action_validate_location
    - slot{"location_valid": "invalid"}
    - utter_invalid_location
    - utter_ask_location
* restaurant_search{"location": "risikesh"}
    - slot{"location": "risikesh"}
    - action_validate_location
    - slot{"location_valid": "invalid"}
    - utter_invalid_location
    - utter_ask_location
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - action_validate_location
    - slot{"location_valid": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "299"}
    - slot{"budget": "299"}
    - action_search_restaurants
    - slot{"location": "agra"}
    - utter_ask_details
* ask_email{"emailid": "ankitmhjn5@gmail.com"}
    - slot{"emailid": "ankitmhjn5@gmail.com"}
    - action_send_details
* thank
    - utter_goodbye
    - action_restart

## interactive_story_14_ask_about_bot_and_ask_help_to_search
* about_bot
    - utter_bot_job
* user_require_help
    - utter_help_user_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "korean"}
    - slot{"cuisine": "korean"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "invalid"}
    - utter_invalid_cuisine
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "300"}
    - slot{"budget": "300"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"location_valid": "valid"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_ask_details
* ask_email{"emailid": "ankitmhjn5@gmail.com"}
    - slot{"emailid": "ankitmhjn5@gmail.com"}
    - action_send_details
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_15_ask_about_bot_ask_search_help_no_email
* about_bot
    - utter_bot_job
* user_require_help
    - utter_help_user_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "300"}
    - slot{"budget": "300"}
    - utter_ask_location
* restaurant_search{"location": "Bhubaneswar"}
    - slot{"location": "Bhubaneswar"}
    - action_validate_location
    - slot{"location_valid": "valid"}
    - action_search_restaurants
    - slot{"location": "Bhubaneswar"}
    - utter_ask_details
* deny
    - utter_no_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_16_ask_bot_to_help_invalid_loc_multiple_times_email
* about_bot
    - utter_bot_job
* user_require_help
    - utter_help_user_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "299"}
    - slot{"budget": "299"}
    - utter_ask_location
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - action_validate_location
    - slot{"location_valid": "invalid"}
    - utter_invalid_location
    - utter_ask_location
* restaurant_search{"location": "risikesh"}
    - slot{"location": "risikesh"}
    - action_validate_location
    - slot{"location_valid": "invalid"}
    - utter_invalid_location
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"location_valid": "valid"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_ask_details
* ask_email{"emailid": "ankitmhjn5@gmail.com"}
    - slot{"emailid": "ankitmhjn5@gmail.com"}
    - action_send_details
* affirm
    - utter_affirm_reply
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_17
* user_require_help
    - utter_help_user_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "299"}
    - slot{"budget": "299"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"location_valid": "valid"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"emailid": "ankitmhjn5@gmail.com"}
    - slot{"emailid": "ankitmhjn5@gmail.com"}
    - action_send_details
* thank
    - utter_affirm_reply
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_18_error_sending email
* restaurant_search{"cuisine": "Mexican", "location": "Mumbai"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Mumbai"}
    - action_validate_location
    - slot{"location_valid": "valid"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "299"}
    - slot{"budget": "299"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_details
* ask_email{"emailid": "ankitmhjn5@gmail.com"}
    - slot{"emailid": "ankitmhjn5@gmail.com"}
    - action_send_details
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_19_invalid_cuisine_invalid_loc_error_email_sending
* restaurant_search{"cuisine": "maaaaxican", "location": "batala"}
    - slot{"cuisine": "maaaaxican"}
    - slot{"location": "batala"}
    - action_validate_location
    - slot{"location_valid": "invalid"}
    - utter_invalid_location
    - utter_ask_location
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - action_validate_location
    - slot{"location_valid": "valid"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "invalid"}
    - utter_invalid_cuisine
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "300"}
    - slot{"budget": "300"}
    - action_search_restaurants
    - slot{"location": "agra"}
    - utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"emailid": "ankitmhjn5@gmail.com"}
    - slot{"emailid": "ankitmhjn5@gmail.com"}
    - action_send_details
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_20_ask_hel_from_bot_email_sending_error
* ask_bot_job
    - utter_bot_job
* user_require_help
    - utter_help_user_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "299"}
    - slot{"budget": "299"}
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_validate_location
    - slot{"location_valid": "valid"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"emailid": "ankitmhjn5@gmail.com"}
    - slot{"emailid": "ankitmhjn5@gmail.com"}
    - action_send_details
* goodbye
    - utter_goodbye
    - action_restart


## interactive_story_21_valid_loc_no_restaurant_found_user_enter_location_again
* restaurant_search{"location": "amravati"}
    - slot{"location": "amravati"}
    - action_validate_location
    - slot{"location_valid": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "300"}
    - slot{"budget": "300"}
    - action_search_restaurants
    - slot{"location": "amravati"}
    - utter_ask_details
* ask_email{"emailid": "ankitmhjn5@gmail.com"}
    - slot{"emailid": "ankitmhjn5@gmail.com"}
    - action_send_details
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_22_complete_path
* restaurant_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "valid"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"location_valid": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "300"}
    - slot{"budget": "300"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_ask_details
* ask_email{"emailid": "ankitmhjn5@gmail.com"}
    - slot{"emailid": "ankitmhjn5@gmail.com"}
    - action_send_details
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_23_no_email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "valid"}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location_valid": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "299"}
    - slot{"budget": "299"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_details
* deny
    - utter_no_email
    - action_restart

## interactive_story_24_valid_cuisine_invalid_location_with_email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "valid"}
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_location
    - slot{"location_valid": "invalid"}
    - utter_invalid_location
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"location_valid": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "300"}
    - slot{"budget": "300"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"emailid": "ankitmhjn5@gmail.com"}
    - slot{"emailid": "ankitmhjn5@gmail.com"}
    - action_send_details
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_validate_location
    - slot{"location_valid": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"is_cuisine_valid": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "299"}
    - slot{"budget": "299"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"emailid": "ankitmhjn5@gmail.com"}
    - slot{"emailid": "ankitmhjn5@gmail.com"}
    - action_send_details
* goodbye
    - utter_goodbye
    - action_restart
