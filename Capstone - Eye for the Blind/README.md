# Introduction
Welcome to the capstone project on Eye for Blind.


According to the World Health Organization (WHO), it has been reported that there are approximately 285 million visually impaired people worldwide, and out of these 285 million, 39 million are totally blind. It becomes extremely tough for them to carry out daily activities, one of which is reading. From reading a newspaper or a magazine to reading an important text message from your bank, it becomes tough for them.


Suppose you went trekking recently with your family and enjoyed a lot there. You clicked thousands of pictures, including those of the nature, hills and forests. You want to share your experience with a friend, but unfortunately, he is not able to view these photos, as he is blind. However, you want to show him what this place exactly looks like from up there, as it is one of his favourite trekking places. How will you be able to share your experience with him?

 

Have you ever seen a blind person operate Facebook, YouTube, etc, on their phone? Have you ever wondered how blind people can easily scroll through the news feed and understand what other people have shared on their timelines?

 

In 2010, Facebook launched a special feature that can help the blind operate Facebook on their mobile phones. The feature helped blind individuals understand what they are typing. With the help of this feature, whenever a person taps on a particular alphabet on the keypad, the application responds by speaking out that particular alphabet. Also, the feature could explain to the blind person the contents of an image that their friends have posted on Facebook. So, if someone posted a picture with their dog, this Facebook application would speak out its contents.

# Problem statement
To create a deep learning model that can explain the content of an image in the form of speech through caption generation with the attention mechanism on the Flickr8K data set 

This type of model is a use case for blind people so that they can understand any image with the help of speech. The caption generated through a CNN-RNN model will be converted to speech using a text-to-speech library. 

 

This problem statement is an application of both deep learning and natural language processing. The features of an image will be extracted by the CNN-based encoder, and this will be decoded by an RNN model.


The project is an extended application of Show, Attend and Tell: Neural Image Caption Generation with Visual Attention.paper.

 

The data set is taken from the Kaggle website and consists of a sentence-based image description having a list of 8,000 images that are each paired with five different captions, which provide clear descriptions of the salient entities and events of the image.