*** Korean Drama Multi-Label Facial Emotion Recognition Dataset ***

!!! Please use this dataset for non-commercial research only. Any other use is strictly prohibited. !!!

This dataset is used in the following conference paper:

Heeryon Cho, Woo Kyu Kang, Younsoo Park, Sungeu Chae, and Seong-joon Kim, "Multi-label Facial Emotion Recognition Using Korean Drama Video Clips," in Proceedings of the 2022 IEEE International Conference on Big Data and Smart Computing (BigComp-22), IEEE, January 17-20, 2022, Daegu, South Korea.

This dataset contains 38,817 colored cropped face images tagged with 23 emotion labels. If we include 'neutral' emotion, then the total number of emotion labbels is 24. The following lists the 24 emotion labels.

[affectionate, amused, angry, anxious, ashamed, bored, depressed, disappointed, disgusted, fearful, fluttered, fulfilled, guilty, happy, jealous, moved, passionate, peaceful, sad, smitten, surprised, sympathetic, upset, neutral (24)]

This dataset includes 19,800 images tagged with one label, 18,134 images tagged with two labels (i.e., multi-label), 875 images tagged with three labels, and 8 images tagged with four labels. 

While existing facial emotion recognition dataset predominantly captures Western (i.e., non-Asian) faces, our dataset covers various Korean (Asian) faces with wide age range, making this a valuable Asian multi-label facial emotion recognition dataset. 

We created three different kinds of datasets using the 38,317 images and labels.

- 6 basic emotion classification dataset (6 emotions)

- 22 emotion classification dataset (22 emotions)

- multi-label classification dataset (24 emotions)

All three datasets are split into train/validation/test data.

All datasets are provided in tfrecord format.

You can use the following code to analyze the dataset.

https://github.com/heeryoncho/facial_emotion_recognition_using_K-drama_dataset/blob/main/show_images_analyze_labels.ipynb

The codes used in the evaluation experiments in the BigComp 2022 conference paper can be found at:

https://github.com/heeryoncho/facial_emotion_recognition_using_K-drama_dataset

For inquiries, please contact: heeryon@cau.ac.kr (Heeryon Cho)

---
This research and the creation of the dataset was supported by the Ministry of Education of South Korea and the National Research Foundation of South Korea (NRF-2017S1A6A3A01078538).