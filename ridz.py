import emoji
emoji_list = ["smiling_face_with_hearts","smiling_face_with_heart-eyes","smiling_face","smiling_cat_with_heart-eyes",
"see-no-evil_monkey","heart_with_ribbon","sparkling_heart","growing_heart",
              "hand_with_index_finger_and_thumb_crossed","heart_hands","couple_with_heart","people_hugging"]
for i in emoji_list:
    i = ":"+i+":"
    print(f"Haanji {emoji.emojize(i)}")