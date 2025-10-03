import streamlit as st
from datetime import datetime
from streamlit_gsheets import GSheetsConnection
import traceback
import time
import pandas as pd

ADMIN_EMAILS = ["edisonportillal@gmail.com", "edisonportillaluna@gmail.com", "pro.talento10@gmail.com"]

st.set_page_config(page_title="One - Encuestas", 
    page_icon=":one:", 
    layout="wide"
    )

def login_screen():
    st.header("Encuestas One.")
    st.subheader("Por favor, inicia sesión.")
    st.button("Log in with Google", on_click=st.login)

if not st.user.is_logged_in:
    #pg = st.navigation([st.Page(login_screen)])
    # with st.form("login_form", border=True):
    #     st.header("Ingreso de Encuestas")
    #     submitted = st.form_submit_button("Iniciar Sesión", on_click=st.login)
    #     st.stop()
    login_screen()
    st.stop()

else:
    if st.user.email in ADMIN_EMAILS:
        st.session_state.role = "admin"
    else:
        st.session_state.role = "user"

    st.sidebar.header(f"Bienvenido, {st.user.name}!")
    st.sidebar.button("Cerrar sesión", on_click=st.logout)

    gastos = st.Page(["pages/formulario.py", "pages/solo_lectura_info.py"], title="Analisis de encuestas")
    solo_lectura = st.Page("pages/formulario.py", title="Ingreso de Encuestas")

    admon_pages = [gastos, solo_lectura]
    user_pages = [solo_lectura]

    page_dict = admon_pages if st.session_state.role == "admin" else user_pages
    pg = st.navigation(page_dict)

pg.run()

