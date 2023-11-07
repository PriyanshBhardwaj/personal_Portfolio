import streamlit as st
import os
from PIL import Image

def AboutMe(col):
    col.write('#')
    col.subheader("**About Me**")
    col.write("Passionate AI Engineer with a strong devotion to the realm of artificial intelligence.\
                 As an AI enthusiast, I bring a wealth of experience in cutting-edge fields, including Computer Vision and Natural Language Processing (NLP).\
                 My technical acumen is complemented by a diverse set of soft skills essential for a software engineer, including adept team and project management.\
                 My unwavering commitment to AI innovation and a track record of solving complex challenges make me a valuable addition to any AI-driven project.\
                 I'm ready to drive progress and make a tangible impact in the world of AI."
                )


def Education(col):
    col.write('#')
    col.subheader("**📖 Education**")
    col.subheader("Modern Institute of Technology and Research Centre, Alwar\
                    \n**B.Tech**")
    col.write("Aug 2018 - Sep 2022")
    col.write("CGPA - 8.95")


def Skills(col):
    col.write('#')
    col.subheader("**👨‍💻 Skills**", divider = "gray")
    col.write('''
        - **Advance Technologies:** NLP, LLM, Computer Vision, Chatbots
        - **AI Technologies:** Machine Learning, Deep Learning, Data Analysis
        - **AI Libraries:** TensorFlow, PyTorch, OpenCV, Streamlit
        - **Languages:** Python, Javascipt, C, C++, Java
        - **Databases:** MySQL, NoSQL, MongoDB
        - **Others:** Docker, MATLAB
        - **Soft Skills:** Communication Skills, Problem-Solving, Adaptability, Teamwork and Collaboration, Attention to Detail
                ''')


def Experience(col2):
    col2.write('#')
    col2.subheader("**💼 Experience**", divider="gray")
    # col2.write("---")

    #1st experience
    col2.subheader("AI Engineer intern\
                    \nOrganisation - Signzy\
                    \nWork tenure - Sep 2021: Feb 2022")
    col2.write("Worked on new and existing AI products, optimised them, worked with frontend and backend team on several projects, worked on business related problems, took complete ownership of various projects.")

    #2nd Experience
    # col2.write('#')
    col2.subheader("AI Engineer trainee\
                    \nOrganisation - Signzy\
                    \nWork tenure - March 2022 : June 2022")
    col2.write("Worked on various live AI and backend projects, worked with different teams within the organisation, interacted with clients, and improved various soft skills.")

    #3rd experience
    # col2.write('#')
    col2.subheader("Smart India Hackathon 2022 Grand Finalist at ISRO\
                    \nAug 2022")
    col2.write("Grand Finalist of SIH 2022 at ISRO, Ahmedabad. Our problem statement was to predict the variations in TEC, Total Electron Count, in the ionosphere due to various space effects and propose an early warning system.")

    #4th experience
    # col2.write('#')
    col2.subheader("Sabbatical leave - Sep 2022 : Sep 2023")
    col2.write("Took 1 year sabbatical leave to prepare for the UPSC exam. During this time I learned the importance of consistency, hard work and dedication that helped me to become a better version of myself which will help me in life wherever I go.")



def Projects(col2):
    col2.write('#')
    col2.subheader("**📈 Projects**", divider="gray")
    col2.write("**Change project from the buttons provided below**\
                \n**You can check more of my projects on my LinkedIn profile.**")
    col2.write("**Please play the video for the project's demo**")
    


    #creating diff columns for buttons and videos
    col21, col22, col23 = col2.columns([0.12,2,0.1])
    # col21.write("")

    # images = [os.path.join("projects/",image) for image in os.listdir("projects")]
    # print(images)

    videos = [os.path.join("project_videos/",video) for video in os.listdir("project_videos")]
    videos.sort()
    # print("\n\n", videos)
    

    #index for looping video directory
    if 'index' not in st.session_state:
        st.session_state.index = 0


    #left and right arrow buttons
    for i in range(13):      #for alligning arrow buttons
        col21.write("#")
    reduce_index = col21.button("＜", help="Click here to change project")

    for i in range(13):      #for alligning arrow buttons
        col23.write("#")
    increase_index = col23.button("＞", help="Click here to change project")


    #updating index
    if reduce_index:
        if st.session_state.index == 0:
            st.session_state.index = len(videos)-1
        else:
            st.session_state.index -= 1
        # print(st.session_state.index)

    if increase_index:
        if st.session_state.index == len(videos)-1:
            st.session_state.index = 0
        else:
            st.session_state.index += 1
        # print(st.session_state.index)


    #project description and title
    project_title = ["Photo to Story: Unleash the Power of Imagination", "Smart Chatbot: Your Intelligent Conversational Companion", "Virtual Canvas: Unleash Your Inner Artist, Virtually", "Head/Helmet (Hardhat) Detection: Ensuring Safety, Anytime, Anywhere"]

    project_description = [
            '''[Visit here for a live demo on your browser](https://photo-to-story.streamlit.app/)\
            \n\nTech Stack - LLM : Falcon 7B\
            \n\nIntroducing Photo to Story, where your photos come to life as captivating short stories.\
             We leverage the incredible capabilities of Falcon 7B, a large language model(LLM), to transform your images into intriguing narratives.\
             Watch as your snapshots evolve into vivid tales, breathing life into your cherished memories. With Photo to Story, the possibilities are as endless as your imagination,\
             making every photo a gateway to a world of storytelling magic."''',

             '''
                Tech Stack - NLP, LLM: Falcon 7B, huggingface\
                \n\nOur Smart Chatbot is more than just a chatbot – it's your conversational companion. Powered by advanced NLP functionality and a large language model, falcon 7b, it generates responses to user input with unparalleled accuracy.\
                 While it's currently under development and not yet deployed, we're committed to enhancing its capabilities to provide even more accurate real-time information.\
                 The future of chatbots is here with Smart Chatbot, and it's only getting smarter.
             ''',
            
            '''[Visit here for more details](https://www.linkedin.com/posts/priyansh-bhardwaj-25964317a_opencv-computervision-machinelearning-activity-6832030873106436096-yRO2/)\
                \n\nTech Stack - Computer Vision, OpenCV, MediaPipe\
                \n\nExperience the future of digital art with Virtual Canvas. This innovative project allows you to paint directly on your computer screen, all without the need for any software installation.\
                 Simply use your fingers to interact with a live video feed, where a dynamic color palette appears at the top of your screen. Hover your fingers in the air to select your preferred colors and paint freely on the live video feed.\
                 With the freedom to choose any color and create wherever your inspiration strikes, Virtual Canvas is your gateway to artistic expression like never before.''',

            '''[Visit here for more details](https://www.linkedin.com/posts/priyansh-bhardwaj-25964317a_deeplearning-machinelearning-datascience-activity-6822594941420736512-SA0B/)\
                \n\nTech Stack - YOLOv4\
                \n\nOur project prioritizes safety by utilizing YOLO (You Only Look Once) to detect helmet gears in real-time. It counts helmets, confirms if they're worn, and can do so for multiple individuals.\
                 Versatile for live video, recorded video, and photos. It's your safety solution for every scenario, including identifying helmets on bike riders with a simple training tweak.'''
    ]

    col22.subheader(project_title[st.session_state.index])
    col22.write(project_description[st.session_state.index])

    
    # project videos in Centre
    # col22.image(images[st.session_state.index], use_column_width=True)

    video_file = open(videos[st.session_state.index], 'rb')
    video_bytes = video_file.read()

    col22.video(video_bytes)



def trainings_and_certificates(col2):
    col2.write('#')
    col2.subheader("**📄 Trainings and certificates**", divider="gray")
    col2.write("**Please select any certificate from drop down menu to view.**\
                \n**You can also visit the certificate in browser by clicking on the link provided.**")

    #certificate
    certificates = {
        "Convolutional Neural Networks in TensorFlow": "[Convolutional Neural Networks in TensorFlow](https://www.coursera.org/account/accomplishments/certificate/S5NCR6GXRMKJ)",
        "Introduction to TensorFlow for Artificial Intelligence, Machine Learning, and Deep Learning": "[Introduction to TensorFlow for Artificial Intelligence, Machine Learning, and Deep Learning](https://www.coursera.org/account/accomplishments/certificate/MD7Q7YVH5K8P)",
        "Sequence Models": "[Sequence Models](https://www.coursera.org/account/accomplishments/certificate/3GTWEDJCVUPH)",
        "Convolutional Neural Networks": "[Convolutional Neural Networks](https://www.coursera.org/account/accomplishments/certificate/BBCYZEAGUWUF)",
        "Structuring Machine Learning Projects": "[Structuring Machine Learning Projects](https://www.coursera.org/account/accomplishments/certificate/P6YNP6MZZDWZ)",
        "Improving Deep Neural Networks: Hyperparameter tuning, Regularization, and Optimization": "[Improving Deep Neural Networks: Hyperparameter tuning, Regularization, and Optimization](https://www.coursera.org/account/accomplishments/certificate/LWG55XKW6RB2)",
        "Neural Networks and Deep Learning": "[Neural Networks and Deep Learning](https://www.coursera.org/account/accomplishments/certificate/SUQYZDH275VN)",
        "Getting Started with AWS Machine Learning": "[Getting Started with AWS Machine Learning](https://www.coursera.org/account/accomplishments/certificate/6N8EUWAZWFUD)",
        "Python for Machine Learning": "[Python for Machine Learning](https://olympus1.mygreatlearning.com/course_certificate/SROVWFYK)",
        "Machine Learning by Andrew Ng": "[Machine Learning by Andrew Ng](https://www.coursera.org/account/accomplishments/certificate/8BJ5N92HYJMR)"
    }

    #certificate names
    certificates_names = [
        "Convolutional Neural Networks in TensorFlow",
        "Introduction to TensorFlow for Artificial Intelligence, Machine Learning, and Deep Learning",
        "Sequence Models",
        "Convolutional Neural Networks",
        "Structuring Machine Learning Projects",
        "Improving Deep Neural Networks: Hyperparameter tuning, Regularization, and Optimization",
        "Neural Networks and Deep Learning",
        "Getting Started with AWS Machine Learning",
        "Python for Machine Learning",
        "Machine Learning by Andrew Ng"
    ]

    #certificate images
    certificate_images = [os.path.join("certificates/",image) for image in os.listdir("certificates")]
    certificate_images.sort()
    # print('\n\n', certificate_images)

    # for cert_index in range(len(certificates)):
    trainings = col2.selectbox("Select certificate", options=certificates_names)

    if trainings:
        col2.write(f"{certificates[trainings]}")

        #getting index of selected certificate for displaying certificate
        cert_index = list(certificates.keys()).index(trainings)

        image = Image.open(certificate_images[cert_index])
        col2.image(image, width = 600)



def Accomplishments(col2):
    col2.write("#")
    col2.subheader("**🏆 Accomplishments**", divider="gray")

    with st.container():
        col2.subheader("[**Deep Learning Specialization**](https://www.coursera.org/account/accomplishments/specialization/certificate/BAXZWV4U9LXV)")

        col2.write("The specialization is having 5 courses covering the basics of Deep\
                    Learning to advance.\
                    It covers a variety of topics from Neural Networks to CNN to RNN and covers fields such as Computer Vision and NLP.")
        
        col2.subheader("[**Microsoft Al Classroom Series**](https://drive.google.com/file/d/1GAvTItnAX-sU_qfh6F_-EoFbybTMtrlR/view)")
        col2.write("Got certified with AI 900 exam certificate.\
                    It covers the basics of data science, machine learning, and understanding of cognitive services to build intelligent solutions using azure.")
    