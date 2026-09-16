import streamlit as st

def header_home():
    logo_url = "https://static.vecteezy.com/system/resources/previews/014/467/176/large_2x/recruitment-accepted-illustration-3d-png.png"
    st.markdown(f"""
              <div style= "display: flex; flex-direction:column; align-items: center; justify-content: center; margin-bottom:1px; margin-top: px;">  
                <img src="{logo_url}" style= " height:150px;"/>
                <h1 style= 'text-align: center; color: #000000'> Haziri AI </h1>
                
             </div>  
                
                
                """, unsafe_allow_html=True)
 