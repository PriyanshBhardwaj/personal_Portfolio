import streamlit as st
import os
from PIL import Image
import helper

def main():
    st.set_page_config(
        page_title="Your_name Portfolio",
        page_icon="📚",
        layout="wide"
    )

    #Removing the default Menu Button and Streamlit Icon(at bottom left) from web page
    hide_default_format = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
    st.markdown(hide_default_format, unsafe_allow_html=True)

    # Main page layout with columns and gap
    col1, col2 = st.columns([2, 5])
    col1.write("")  # Create a gap between columns


    ## Left side

    # Column 1: Profile Picture
    col1.image("assets/your_profile_picture.jpg", width=250)


    #contact
    col1.subheader("**Contact**")
    col1.write("Email: your_email@xyz.com")
    col1.write("Mobile: --number--")


    #social Media
    social_media = {
        "Linkedin": "linkedin-id-url",
        "GitHub": "github-repo-url"
    }

    # col1.write('#')         #to add vertical space
    cols = col1.columns(len(social_media))
    for index, (platform, link)in enumerate(social_media.items()):
        cols[index].write(f"[{platform}]({link})")
    

    #Resume
    col1.write('#')     #for adding vertical space
    with open('resume/your-resume.pdf', "rb") as resume:
        Resume_byte = resume.read()

    col1.download_button(
        label = "**Download Resume**",
        help = "Click on this button to download my resume",
        type = "primary",
        data = Resume_byte,
        file_name = "your_name_Resume.pdf",     #the resume will be downloaded by this file name
        mime="application/octet_stream"
    )


    ## Right side

    # Column 2: Main Content
    col2.title("Full Name")
    col2.subheader("**Designation**")
    

    # about me
    helper.AboutMe(col2)
    

    #Education
    helper.Education(col2)


    #Skills
    helper.Skills(col2)
    

    #Experience
    helper.Experience(col2)


    ##Projects
    helper.Projects(col2)

    

    ##trainings and certificates
    helper.trainings_and_certificates(col2)

    


    ##Accomplishments
    helper.Accomplishments(col2)



if __name__ == "__main__":
    main()