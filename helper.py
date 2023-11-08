import streamlit as st
import os
from PIL import Image

def AboutMe(col):
    col.write('#')
    col.subheader("**About Me**")
    col.write("Your brief introduction")


def Education(col):
    col.write('#')
    col.subheader("**📖 Education**")
    col.subheader("College/University\
                    \n**Degree**")
    col.write("Duration")
    col.write("CGPA - your cgpa / percentage")


def Skills(col):
    col.write('#')
    col.subheader("**👨‍💻 Skills**", divider = "gray")        #you can also change the colour of divider or remove it. visit streamlit documentation for more details.
    col.write('''
        - Write all your skills
        - adding a '-' before a line will make it a bullet point.
        - it looks good and you dont have to include a '\n'.
                ''')


def Experience(col2):
    col2.write('#')
    col2.subheader("**💼 Experience**", divider="gray")
    # col2.write("---")

    #1st experience
    col2.subheader("Title / Designation\
                    \nOrganisation\
                    \nWork tenure")
    col2.write("Short Description")

    #2nd Experience
    
    #add more experiences


def Projects(col2):
    col2.write('#')
    col2.subheader("**📈 Projects**", divider="gray")
    col2.write("**Change project from the buttons provided below**\
                \n**You can check more of my projects on my LinkedIn profile.**")
    col2.write("**Please play the video for the project's demo**")
    


    #creating diff columns for buttons and videos
    col21, col22, col23 = col2.columns([0.12,2,0.1])
    # col21.write("")

    #if you want to add images instead of videos then create a folder "projects" and add your images in it.
    #uncomment the below line and comment the videos section

    # images = [os.path.join("projects/",image) for image in os.listdir("projects")]
    # print(images)

    #videos
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
    project_title = ["Project 1 title", "Project 2 title", "add more projects"]

    project_description = [
            '''[Project 1 Link title if any](link of project)\
            \n\nTech Stack - \
            \n\nProject 1 Description"''',
            
            '''[Project 2 link title if any](link of project)\
                \n\nTech Stack - \
                \n\nProject 2 description''',
            
            '''
                add more
            '''
            ]

    col22.subheader(project_title[st.session_state.index])
    col22.write(project_description[st.session_state.index])

    
    # project videos in Centre
    # col22.image(images[st.session_state.index], use_column_width=True)

    #displaying videos
    video_file = open(videos[st.session_state.index], 'rb')
    video_bytes = video_file.read()

    col22.video(video_bytes)


    #displaying images
    # project_image = Image.open(images[index])
    # col22.image(project_image, width = 600)




def trainings_and_certificates(col2):
    col2.write('#')
    col2.subheader("**📄 Trainings and certificates**", divider="gray")
    col2.write("**Please select any certificate from drop down menu to view.**\
                \n**You can also visit the certificate in browser by clicking on the link provided.**")

    #certificate
    certificates = {
        "Cerificate 1 name (it will work as a key)": "[certificate 1 name (for link title)](certificate 1 link)",
        #add more certificates in same manner
        }

    #certificate names
    certificates_names = [
        "certificate 1 name",
        # add more certificates in same manner
        ]

    #certificate images
    certificate_images = [os.path.join("certificates/",image) for image in os.listdir("certificates")]
    certificate_images.sort()
    # print('\n\n', certificate_images)

    # for cert_index in range(len(certificates)):
    trainings = col2.selectbox("Select certificate", options=certificates_names)

    if trainings:
        col2.write(f"{certificates[trainings]}")    #it will write the link of selected certificate

        #getting index of selected certificate for displaying certificate
        cert_index = list(certificates.keys()).index(trainings)

        #displaying certificate
        image = Image.open(certificate_images[cert_index])
        col2.image(image, width = 600)



def Accomplishments(col2):
    col2.write("#")
    col2.subheader("**🏆 Accomplishments**", divider="gray")

    with st.container():
        #Accomplishment 1
        col2.subheader("[**Accomplishment 1 title**](Accomplishment 1 link)")

        col2.write("Brief Description")
        
        #add other in same manner