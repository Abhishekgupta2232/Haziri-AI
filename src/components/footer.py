import streamlit as st

def footer_home():
    
    st.markdown(f"""
              <div style= "display: flex; flex-direction:column; align-items: center; justify-content: center; margin-bottom:1px; margin-top: 1px;">  
                <p style= "font-weight:bold ; color:black;"> Created with ❤️ by Abhishek Gupta </p>
                
             </div>  
                
                
                """, unsafe_allow_html=True)