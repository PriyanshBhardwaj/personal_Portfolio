import streamlit as st
import os
from PIL import Image
import helper

def main():
    st.set_page_config(
        page_title="Priyansh Portfolio",
        page_icon="📚",
        layout="wide"
    )

    # Main page layout with columns and gap
    col1, col2 = st.columns([2, 5])
    col1.write("")
    # col1.write("")  # Create a gap between columns


    ## Left side

    # Column 1: Profile Picture
    col1.image("assets/PortfolioImage.jpg", width=250)


    #contact
    col1.subheader("**Contact**")
    col1.write("Email: priyanshb11@gmail.com")
    col1.write("Mobile: +91 9667541649")


    #social Media
    social_media = {
        "Linkedin": "https://www.linkedin.com/in/priyansh-bhardwaj-25964317a",
        "GitHub": "https://github.com/PriyanshBhardwaj?tab=repositories"
    }

    # col1.write('#')         #to add vertical space
    cols = col1.columns(len(social_media))
    for index, (platform, link)in enumerate(social_media.items()):
        cols[index].write(f"[{platform}]({link})")
    

    #Resume
    col1.write('#')     #for adding vertical space
    with open('resume/PriyanshResume.pdf', "rb") as resume:
        Resume_byte = resume.read()

    col1.download_button(
        label = "**Download Resume**",
        help = "Click on this button to download my resume",
        type = "primary",
        data = Resume_byte,
        file_name = "Priyansh_Resume.pdf",
        mime="application/octet_stream"
    )


    ## Right side

    # Column 2: Main Content
    col2.title("Priyansh Bhardwaj")
    col2.subheader("**AI Engineer**")
    

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