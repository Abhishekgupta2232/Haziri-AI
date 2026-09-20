import streamlit as st
from supabase import client, create_client

supabase: client = create_client(
    
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_SECRET_KEY"]
)