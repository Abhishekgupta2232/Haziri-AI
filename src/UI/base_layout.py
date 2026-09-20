import streamlit as st


def style_base_layout_home():
    st.markdown(
        """
          <style>
            .stApp{
                background: #ECFDF5 !important;
            
            }
            
            .stApp div[data-testid="stColumn"]{
                background-color:#FFFFFF !important;
                padding: 2.5rem !important;
                border-radius: 3rem !important;
                
                
            }
            /* Center everything inside card */
            div[data-testid="stColumn"] > div {
             align-items: center !important;
            }
            /* Center heading */
            div[data-testid="stColumn"] h2{
                  text-align: center !important;
                  width: 100% !important;
            }
                
            }
          </style>
         
     """,
        unsafe_allow_html=True,
    )


def style_base_layout_dashboard():
    st.markdown(
        """
          <style>
            .stApp{
                background: #E0E3FF !important;
            
            }
          </style>
         
     """,
        unsafe_allow_html=True,
    )


def style_base_layout():
    st.markdown(
        """
        <style>

           @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');
           @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300..700&display=swap');

            
          }

          .block-container{
              padding-top:1.5rem !important;
          
          }
          h1{
              font-family: "Space Grotesk", sans-serif !important;
              font-size: 3rem !important;
              line-height:1.1 !important;
              margin-bottom : 0rem !important;
              color: #000000 !important;
          
          
          
          }
          
           
         h2{
               font-family: "Space Grotesk", sans-serif !important;
               font-size: 2rem !important;
               line-height:1.1 !important;
               margin-bottom : 0rem !important;
               color: #000000 !important;    
                    
                    
          }
          
          h3, h4 , p  {
              font-family: "Outfit", sans-serif 
              
          }
          
          button[kind="secondary"]{
              border-radius: 1.5rem !important;
              background: #0D9488 !important;
              color: white !important;
              padding: 10px 20px !important;
              border: none !important;
              transition: transform 0.25s ease-in-out !important;
              
          }
          
          button[kind="tertiary"]{
                        border-radius: 1.5rem !important;
                        background: #F59E0B !important;
                        color: white !important;
                        padding: 10px 20px !important;
                        border: none !important;
                        transition: transform 0.25s ease-in-out !important;
                        
         }
         
         button[kind="primary"]{
                       border-radius: 1.5rem !important;
                       background: #6366F1 !important;
                       color: white !important;
                       padding: 10px 20px !important;
                       border: none !important;
                       transition: transform 0.25s ease-in-out !important;
                       
         }
         
         button:hover{
             transform: scale(1.05)
         }
         
         /* Text input labels */
          div[data-testid="stTextInput"] label,
           div[data-testid="stTextInput"] label p {
            color: #000000 !important;
         }

          
           
           
        </style>
         
     """,
        unsafe_allow_html=True,
    )
