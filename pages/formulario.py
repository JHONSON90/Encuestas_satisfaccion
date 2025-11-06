import streamlit as st
from datetime import datetime
from streamlit_gsheets import GSheetsConnection
import traceback
import time
import pandas as pd


conn = st.connection("gsheets", type=GSheetsConnection)


st.title("Encuestas ONE")

try:
    df = conn.read(worksheet="EmpoPasto", ttl=0)
    placeholder = st.empty()
    placeholder.success("Conexión exitosa!!")
    time.sleep(2)
    placeholder.empty()
except Exception as e:
    placeholder = st.empty()
    placeholder.error(f"Error al conectar con Google Sheets: {str(e)}")
    placeholder.error(f"Traceback: {traceback.format_exc()}")
    time.sleep(2)
    placeholder.empty()

def inicializar_estado():
    if "encuesta_data" not in st.session_state:
        st.session_state.encuesta_data = {
            "Nombre" : "",
            "Telefono" : 0,
            "Direccion" : "",
            "Barrio" : "",
            "Estrato" : 0,
            "Fecha" : datetime.now().date(),
            "Codigo" : 0,
            "Tipo" : "Residencial",
            "Edad" : 0,

            'pregunta1': 0, 'pregunta2': 0, 'pregunta3': '',
            'pregunta4': 'SI', 'pregunta4_1': 0, 'pregunta4_2': 0, 'pregunta4_3': 0,
            'pregunta5': 'SI', 'pregunta5_1': 0, 'pregunta5_2': 0,
            'pregunta6': 'SI', 'pregunta6_1': 0,
            'pregunta7': 'SI', 'pregunta7_1': 0,
            'pregunta8': 0, 'pregunta9': 'SI', 'pregunta9_1': 0,
            'pregunta10': 0, 'pregunta11': 'SI', 'pregunta11_1': 0,
            'pregunta12': 0, 'pregunta13': 0, 'pregunta14': 0, 'pregunta14_1': '',
            'pregunta15': 'SI', 'pregunta15_1': '',
            'pregunta16': 0, 'pregunta16_1': '',
            'pregunta17': [], 'pregunta17_1': '',
            'pregunta18': [], 'pregunta18_1': '',
            'pregunta19': 'SI', 'pregunta19_1': [],
            'pregunta20': 0, 'pregunta21': 0,
            'pregunta22': '',
            'pregunta23': 'Leni Valentina Patiño',
        }


DEFAULT_STATE = {
    "Nombre" : "",
    "Telefono" : 0, # Usaremos 0 como valor inicial para number_input
    "Direccion" : "",
    "Barrio" : "",
    "Estrato" : 0,
    "Fecha" : datetime.now().date(),
    "Codigo" : 0,
    "Tipo" : "Residencial",
    "Edad" : 0,
    'pregunta1': 0, 'pregunta2': 0, 'pregunta3': '',
    'pregunta4': 'SI', 'pregunta4_1': 0, 'pregunta4_2': 0, 'pregunta4_3': 0,
    'pregunta5': 'SI', 'pregunta5_1': 0, 'pregunta5_2': 0,
    'pregunta6': 'SI', 'pregunta6_1': 0,
    'pregunta7': 'SI', 'pregunta7_1': 0,
    'pregunta8': 0, 'pregunta9': 'SI', 'pregunta9_1': 0,
    'pregunta10': 0, 'pregunta11': 'SI', 'pregunta11_1': 0,
    'pregunta12': 0, 'pregunta13': 0, 'pregunta14': 0, 'pregunta14_1': '',
    'pregunta15': 'SI', 'pregunta15_1': '',
    'pregunta16': 0, 'pregunta16_1': '',
    'pregunta17': [], 'pregunta17_1': '',
    'pregunta18': [], 'pregunta18_1': '',
    'pregunta19': 'SI', 'pregunta19_1': [],
    'pregunta20': 0, 'pregunta21': 0,
    'pregunta22': '',
    'pregunta23': 'Leni Valentina Patiño',
}
KEYS_TO_RESET = list(DEFAULT_STATE.keys())

if "state_initialized" not in st.session_state:
    for key, value in DEFAULT_STATE.items():
        st.session_state[key] = value
    st.session_state["state_initialized"] = True

def clear_state_and_rerun():
    for key in KEYS_TO_RESET:
        if key in st.session_state:
            del st.session_state[key]
    if "state_initialized" in st.session_state:
        del st.session_state["state_initialized"]
        
    st.success("Respuesta agregada exitosamente y formulario limpiado.")
    time.sleep(2)
    st.rerun()


@st.dialog("Agregar Encuestas", width="medium")
def agregar_encuesta():
    st.text_input("Nombres y Apellidos", value=st.session_state['Nombre'], key='Nombre')
    st.number_input("Telefono", value=st.session_state['Telefono'], key='Telefono')
    st.text_input("Direccion", value=st.session_state['Direccion'], key='Direccion')
    st.text_input("Barrio", value=st.session_state['Barrio'], key='Barrio')
    st.number_input("Estrato", value=st.session_state['Estrato'], key='Estrato')
    st.date_input("Fecha", value=datetime.now(), key='Fecha')
    st.number_input("Codigo", value=st.session_state['Codigo'], key='Codigo')
    st.radio("Tipo", ["Residencial", "Comercial"], horizontal=True, key='Tipo', index=0)
    st.number_input("Edad", value=st.session_state['Edad'], key='Edad')

    st.radio("1 ¿Usted considera que el tiempo de entrega de su factura, hasta la fecha límite de pago de la misma, es adecuado?", [0,5,4,3,2,1], horizontal=True, key='pregunta1', index=0)
    st.radio("2 ¿Cómo califica la información contenida en la factura de pago en términos de facilidad para comprenderla?", [0,5,4,3,2,1], horizontal=True, key='pregunta2', index=0)
    st.text_input("2.1 Si la respuesta es 1 o 2 Especifique su razón principal:", key='pregunta2_1')
    st.radio("3 ¿Conoce los sitios de pago de su factura?", ["SI", "NO"],horizontal=True, key='pregunta3', index=0)
    st.text("4 La atención que Usted recibe en nuestros puntos, ha sido:")
    st.radio("4.1 Amable", [0,5,4,3,2,1], horizontal=True, key='pregunta4_1', index=0)
    st.radio("4.2 Ágil", [0,5,4,3,2,1], horizontal=True, key='pregunta4_2', index=0)
    st.radio("4.3 Oportuna", [0,5,4,3,2,1], horizontal=True, key='pregunta4_3', index=0)
    st.radio("5 ¿Durante el año pasado, Usted presentó una petición, una queja, reclamo, sugerencia o una denuncia (PQRS)?", ["SI", "NO"],horizontal=True, key='pregunta5', index=0)
    st.radio("5.1 ¿La orientación que recibió a su trámite, fue:", [0,5,4,3,2,1], horizontal=True, key='pregunta5_1', index=0)
    st.radio("5.2 ¿Cómo califica la respuesta a su PQRS?", [0,5,4,3,2,1], horizontal=True, key='pregunta5_2', index=0)
    st.radio("6 ¿Ha solicitado revisión interna en su inmueble?", ["SI", "NO"],horizontal=True, key='pregunta6', index=0)
    st.radio("6.1 Si la respuesta es SI ¿cómo califica la atención recibida?", [0,5,4,3,2,1], horizontal=True, key='pregunta6_1', index=0)
    st.radio("7 ¿Durante el año 2024 le suspendieron el servicio de acueducto?", ["SI", "NO"],horizontal=True, key='pregunta7', index=0)
    st.radio("7.1 Si la respuesta es SI   y teniendo en cuenta que, por normatividad, EMPOPASTO cuenta con 24 horas hábiles para la reinstalación del servicio ¿Cómo califica usted el tiempo entre la suspensión y la reinstalación?", [0,5,4,3,2,1], horizontal=True, key='pregunta7_1', index=0)
    st.radio("8 Califique si las Instalaciones de Empopasto S.A. E.S.P. son adecuadas para atender a los usuarios.", [0,5,4,3,2,1], horizontal=True, key='pregunta8', index=0)
    st.radio("9 ¿Usted se ha comunicado con EMPOPASTO a través del canal telefónico? Línea 116", ["SI", "NO"],horizontal=True, key='pregunta9', index=0)
    st.radio("9.1 Si la respuesta es SI ¿cómo califica la atención recibida?", [0,5,4,3,2,1], horizontal=True, key='pregunta9_1', index=0)
    st.radio("10 ¿Cómo califica la calidad de agua que recibe de EMPOPASTO?", [0,5,4,3,2,1], horizontal=True, key='pregunta10', index=0)
    st.radio("11 ¿Empopasto le brinda información de manera anticipada sobre las suspensiones del servicio en su sector? ", ["SI", "NO"],horizontal=True, key='pregunta11', index=0)
    st.radio("11.1 Si la respuesta es Si, califique si la información y el tiempo de aviso previo a la suspensión del servicio de agua son adecuados", [0,5,4,3,2,1], horizontal=True, key='pregunta11_1', index=0)
    st.radio("12 Considera Usted, que la continuidad del servicio que presta EMPOPASTO es:", [0,5,4,3,2,1], horizontal=True, key='pregunta12', index=0)
    st.radio("13 La presión de agua en su inmueble o en su vivienda es?", [0,5,4,3,2,1], horizontal=True, key='pregunta13', index=0)
    st.radio("14 ¿Cómo califica la oportunidad y organización de los trabajos realizados cuando se presenta un daño de acueducto o alcantarillado?", [0,5,4,3,2,1], horizontal=True, key='pregunta14', index=0)
    st.text_input("14.1 Si la respuesta es 1 o 2 Especifique su razón principal:", key='pregunta14_1')
    st.radio("15 Se ha visto afectado por los trabajos adelantados por EMPOPASTO?", ["SI", "NO"],horizontal=True, key='pregunta15', index=0)
    st.text_input("15.1 Si la respuesta es Si, especifique su respuesta", key='pregunta15_1')
    st.radio("16 ¿Cómo califica la labor de mantenimiento y limpieza en cámaras y sumideros para evitar taponamientos y reboses?", [0,5,4,3,2,1], horizontal=True, key='pregunta16', index=0)
    st.text_input("16.1 Si la respuesta es 1 o 2 Especifique su razón principal:", key='pregunta16_1')
    st.multiselect("17. ¿A través de qué medio se entera de las noticias de EMPOPASTO? (Puede marcar más de una opción)", options=["Prensa", "Radio", "TV", "Factura", "Redes Sociales", "Pagina Web", "Email", "Otro"], key='pregunta17')
    st.text_input("17.1 Si la respuesta es Otro. Especifique cual:", key='pregunta17_1')
    st.multiselect("18 ¿A través de qué medio le gustaría recibir la información de EMPOPASTO? (Puede marcar más de una opción)", options=["Prensa", "Radio", "TV", "Factura", "Redes Sociales", "Pagina Web", "Email", "Otro"], key='pregunta18')
    st.text_input("18.1 Si la respuesta es Otro. Especifique cual:", key='pregunta18_1')
    st.radio("19 ¿Conoce los servicios que presta EMPOPASTO en su página Web?", ["SI", "NO"],horizontal=True, key='pregunta19', index=0)
    st.multiselect("19.1 ¿Cuál ha utilizado?  (Puede marcar más de una opción)", options=["Pago de factura", "Requisitos para tramites", "Consulta Factura", "Puntos de Pago", "PQRSD", "Laboratorio de Agua", "Geoportal", "Laboratorio de Medidores"], key='pregunta19_1')
    st.radio("20 ¿Cómo califica usted las actividades que realiza Empopasto de carácter social y ambiental, que benefician y mejoran la calidad de vida de la comunidad?", [0,5,4,3,2,1], horizontal=True, key='pregunta20', index=0)
    st.radio("21 ¿Cómo considera usted la gestión actual de EMPOPASTO?", [0,5,4,3,2,1], horizontal=True, key='pregunta21', index=0)
    st.text_input("22 Que sugerencias tiene para Empopasto", key='pregunta22')
    st.radio("23 Encuestadora", ["Leni Valentina Patiño", "Daniela Sofia Coral Escobar", "Maritza Patiño", "Amalia Coral", "Monica Patiño", "Leidy Ximena Lasso", "Luisa María Arteaga Lasso", "Edison Portilla Luna", "Milena Lucero"],horizontal=True, key='pregunta23', index=0)

    if st.button("Agregar Respuestas", type="primary"):
        df = conn.read(worksheet="EmpoPasto", ttl=0)
        new_row = pd.DataFrame({
            'Nombre': [st.session_state['Nombre']],
            'Telefono': [st.session_state['Telefono']],
            'Direccion': [st.session_state['Direccion']],
            'Barrio': [st.session_state['Barrio']],
            'Estrato': [st.session_state['Estrato']],
            'Fecha': [st.session_state['Fecha']],
            'Codigo': [st.session_state['Codigo']],
            "Tipo": [st.session_state['Tipo']],
            'Edad': [st.session_state['Edad']],
            'pregunta1': [st.session_state['pregunta1']],
            'pregunta2': [st.session_state['pregunta2']],
            'pregunta3': [st.session_state['pregunta3']],
            'pregunta4': [st.session_state['pregunta4']],
            'pregunta4_1': [st.session_state['pregunta4_1']],
            'pregunta4_2': [st.session_state['pregunta4_2']],
            'pregunta4_3': [st.session_state['pregunta4_3']],
            'pregunta5': [st.session_state['pregunta5']],
            'pregunta5_1': [st.session_state['pregunta5_1']],
            'pregunta5_2': [st.session_state['pregunta5_2']],
            'pregunta6': [st.session_state['pregunta6']],
            'pregunta6_1': [st.session_state['pregunta6_1']],
            'pregunta7': [st.session_state['pregunta7']],
            'pregunta7_1': [st.session_state['pregunta7_1']],
            'pregunta8': [st.session_state['pregunta8']],
            'pregunta9': [st.session_state['pregunta9']],
            'pregunta9_1': [st.session_state['pregunta9_1']],
            'pregunta10': [st.session_state['pregunta10']],
            'pregunta11': [st.session_state['pregunta11']],
            'pregunta11_1': [st.session_state['pregunta11_1']],
            'pregunta12': [st.session_state['pregunta12']],
            'pregunta13': [st.session_state['pregunta13']],
            'pregunta14': [st.session_state['pregunta14']],
            'pregunta14_1': [st.session_state['pregunta14_1']],
            'pregunta15': [st.session_state['pregunta15']],
            'pregunta15_1': [st.session_state['pregunta15_1']],
            'pregunta16': [st.session_state['pregunta16']],
            'pregunta16_1': [st.session_state['pregunta16_1']],
            'pregunta17': [st.session_state['pregunta17']],
            'pregunta17_1': [st.session_state['pregunta17_1']],
            'pregunta18': [st.session_state['pregunta18']],
            'pregunta18_1': [st.session_state['pregunta18_1']],
            'pregunta19': [st.session_state['pregunta19']],
            'pregunta19_1': [st.session_state['pregunta19_1']],
            'pregunta20': [st.session_state['pregunta20']],
            'pregunta21': [st.session_state['pregunta21']],
            'pregunta22': [st.session_state['pregunta22']],
            'pregunta23': [st.session_state['pregunta23']],
        })
        df = pd.concat([df, new_row], ignore_index= True)
        conn.update(worksheet = "EmpoPasto", data = df)
        st.success("Respuesta agregada exitosamente!!")
        time.sleep(2)
        clear_state_and_rerun()

if st.button("Encuesta de Empopasto", type="primary"):
    agregar_encuesta()

col1, col2 = st.columns(2)
col1.metric("Total Encuestas", len(df), border=True)
col2.metric("Encuestas Restantes", 600 - len(df), border=True)

encuestadores = df.groupby("pregunta23")["Nombre"].count()
encuestados = df.groupby("Nombre")["pregunta23"].count()
encuestasxbarrioyestrato = df.groupby(["Barrio", "Estrato"]).size()

col3, col4, col5 = st.columns(3)
with col3:
    st.subheader("Encuestadores")
    st.write(encuestadores)
with col4:
    st.subheader("Encuestados")
    st.write(encuestados)
with col5:
    st.subheader("Encuestas por Barrio y Estrato")
    st.write(encuestasxbarrioyestrato)

st.subheader("Seguimiento por estrato")
st.write(df.groupby("Estrato").size())