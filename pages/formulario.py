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

@st.dialog("Agregar Encuestas", width="medium")
def agregar_encuesta():
    Nombre = st.text_input("Nombres y Apellidos")
    Telefono = st.number_input("Telefono")
    Direccion = st.text_input("Direccion")
    Barrio = st.text_input("Barrio")
    Estrato = st.number_input("Estrato", min_value=0, max_value=6)
    Fecha = st.date_input("Fecha", value=datetime.now())
    Codigo = st.number_input("Codigo")
    Tipo = st.radio("Tipo", ["Residencial", "Comercial"])
    Edad = st.number_input("Edad")

    pregunta1 = st.radio("1 ¿Usted considera que el tiempo de entrega de su factura, hasta la fecha límite de pago de la misma, es adecuado?", [0,5,4,3,2,1], horizontal=True)
    pregunta2 = st.radio("2 ¿Cómo califica la información contenida en la factura de pago en términos de facilidad para comprenderla?", [0,5,4,3,2,1], horizontal=True)
    pregunta3 = st.text_input("2.1 Si la respuesta es 1 o 2 Especifique su razón principal:")
    pregunta4 = st.radio("3 ¿Conoce los sitios de pago de su factura?", ["SI", "NO"],horizontal=True)
    st.text("4 La atención que Usted recibe en nuestros puntos, ha sido:")
    pregunta4_1 = st.radio("4.1 Amable", [0,5,4,3,2,1], horizontal=True)
    pregunta4_2 = st.radio("4.2 Ágil", [0,5,4,3,2,1], horizontal=True)
    pregunta4_3 = st.radio("4.3 Oportuna", [0,5,4,3,2,1], horizontal=True)
    pregunta5 = st.radio("5 ¿Durante el año pasado, Usted presentó una petición, una queja, reclamo, sugerencia o una denuncia (PQRS)?", ["SI", "NO"],horizontal=True)
    pregunta5_1 = st.radio("5.1 ¿La orientación que recibió a su trámite, fue:", [0,5,4,3,2,1], horizontal=True)
    pregunta5_2 = st.radio("5.2 ¿Cómo califica la respuesta a su PQRS?", [0,5,4,3,2,1], horizontal=True)
    pregunta6 = st.radio("6 ¿Ha solicitado revisión interna en su inmueble?", ["SI", "NO"],horizontal=True)
    pregunta6_1 = st.radio("6.1 Si la respuesta es SI ¿cómo califica la atención recibida?", [0,5,4,3,2,1], horizontal=True)
    pregunta7 = st.radio("7 ¿Durante el año 2024 le suspendieron el servicio de acueducto?", ["SI", "NO"],horizontal=True)
    pregunta7_1 = st.radio("7.1 Si la respuesta es SI   y teniendo en cuenta que, por normatividad, EMPOPASTO cuenta con 24 horas hábiles para la reinstalación del servicio ¿Cómo califica usted el tiempo entre la suspensión y la reinstalación?", [0,5,4,3,2,1], horizontal=True)
    pregunta8 =  st.radio("8 Califique si las Instalaciones de Empopasto S.A. E.S.P. son adecuadas para atender a los usuarios.", [0,5,4,3,2,1], horizontal=True)
    pregunta9 = st.radio("9 ¿Usted se ha comunicado con EMPOPASTO a través del canal telefónico? Línea 116", ["SI", "NO"],horizontal=True)
    pregunta9_1 = st.radio("9.1 Si la respuesta es SI ¿cómo califica la atención recibida?", [0,5,4,3,2,1], horizontal=True)
    pregunta10 = st.radio("10 ¿Cómo califica la calidad de agua que recibe de EMPOPASTO?", [0,5,4,3,2,1], horizontal=True)
    pregunta11 = st.radio("11 ¿Empopasto le brinda información de manera anticipada sobre las suspensiones del servicio en su sector? ", ["SI", "NO"],horizontal=True)
    pregunta11_1 = st.radio("11.1 Si la respuesta es Si, califique si la información y el tiempo de aviso previo a la suspensión del servicio de agua son adecuados", [0,5,4,3,2,1], horizontal=True)
    pregunta12 = st.radio("12 Considera Usted, que la continuidad del servicio que presta EMPOPASTO es:", [0,5,4,3,2,1], horizontal=True)
    pregunta13 = st.radio("13 La presión de agua en su inmueble o en su vivienda es?", [0,5,4,3,2,1], horizontal=True)
    pregunta14 = st.radio("14 ¿Cómo califica la oportunidad y organización de los trabajos realizados cuando se presenta un daño de acueducto o alcantarillado?", [0,5,4,3,2,1], horizontal=True)
    pregunta14_1 = st.text_input("14.1 Si la respuesta es 1 o 2 Especifique su razón principal:")
    pregunta15 = st.radio("15 Se ha visto afectado por los trabajos adelantados por EMPOPASTO?", ["SI", "NO"],horizontal=True)
    pregunta15_1 = st.text_input("15.1 Si la respuesta es Si, especifique su respuesta")
    pregunta16 = st.radio("16 ¿Cómo califica la labor de mantenimiento y limpieza en cámaras y sumideros para evitar taponamientos y reboses?", [0,5,4,3,2,1], horizontal=True)
    pregunta16_1 = st.text_input("16.1 Si la respuesta es 1 o 2 Especifique su razón principal:")
    pregunta17 = st.multiselect("17. ¿A través de qué medio se entera de las noticias de EMPOPASTO? (Puede marcar más de una opción)", options=["Prensa", "Radio", "TV", "Factura", "Redes Sociales", "Pagina Web", "Email", "Otro"])
    pregunta17_1 = st.text_input("17.1 Si la respuesta es Otro. Especifique cual:")
    pregunta18 = st.multiselect("18 ¿A través de qué medio le gustaría recibir la información de EMPOPASTO? (Puede marcar más de una opción)", options=["Prensa", "Radio", "TV", "Factura", "Redes Sociales", "Pagina Web", "Email", "Otro"])
    pregunta18_1 = st.text_input("18.1 Si la respuesta es Otro. Especifique cual: ")
    pregunta19 = st.radio("19 ¿Conoce los servicios que presta EMPOPASTO en su página Web?", ["SI", "NO"],horizontal=True)
    pregunta19_1 = st.multiselect("19.1 ¿Cuál ha utilizado?  (Puede marcar más de una opción)", options=["Pago de factura", "Requisitos para tramites", "Consulta Factura", "Puntos de Pago", "PQRSD", "Laboratorio de Agua", "Geoportal", "Laboratorio de Medidores"])
    pregunta20 = st.radio("20 ¿Cómo califica usted las actividades que realiza Empopasto de carácter social y ambiental, que benefician y mejoran la calidad de vida de la comunidad?", [0,5,4,3,2,1], horizontal=True)
    pregunta21 = st.radio("21 ¿Cómo considera usted la gestión actual de EMPOPASTO?", [0,5,4,3,2,1], horizontal=True)
    pregunta22 = st.text_input("22 Que sugerencias tiene para Empopasto")
    pregunta23 = st.radio("23 Encuestadora", ["Leni Valentina Patiño", "Daniela Sofia Coral Escobar", "Maritza Patiño", "Amalia Coral", "Monica Patiño", "Leidy Ximena Lasso", "Luisa María Arteaga Lasso", "Edison Portilla Luna", "Milena Lucero"],horizontal=True)

    if st.button("Agregar Respuestas"):
        df = conn.read(worksheet="EmpoPasto", ttl=0)
        new_row = pd.DataFrame({
            'Nombre': [Nombre],
            'Telefono': [Telefono],
            'Direccion': [Direccion],
            'Barrio': [Barrio],
            'Estrato': [Estrato],
            'Fecha': [Fecha],
            'Codigo': [Codigo],
            "Tipo": [Tipo],
            'Edad': [Edad],
            'pregunta1': [pregunta1],
            'pregunta2': [pregunta2],
            'pregunta3': [pregunta3],
            'pregunta4': [pregunta4],
            'pregunta4_1': [pregunta4_1],
            'pregunta4_2': [pregunta4_2],
            'pregunta4_3': [pregunta4_3],
            'pregunta5': [pregunta5],
            'pregunta5_1': [pregunta5_1],
            'pregunta5_2': [pregunta5_2],
            'pregunta6': [pregunta6],
            'pregunta6_1': [pregunta6_1],
            'pregunta7': [pregunta7],
            'pregunta7_1': [pregunta7_1],
            'pregunta8': [pregunta8],
            'pregunta9': [pregunta9],
            'pregunta9_1': [pregunta9_1],
            'pregunta10': [pregunta10],
            'pregunta11': [pregunta11],
            'pregunta11_1': [pregunta11_1],
            'pregunta12': [pregunta12],
            'pregunta13': [pregunta13],
            'pregunta14': [pregunta14],
            'pregunta14_1': [pregunta14_1],
            'pregunta15': [pregunta15],
            'pregunta15_1': [pregunta15_1],
            'pregunta16': [pregunta16],
            'pregunta16_1': [pregunta16_1],
            'pregunta17': [pregunta17],
            'pregunta17_1': [pregunta17_1],
            'pregunta18': [pregunta18],
            'pregunta18_1': [pregunta18_1],
            'pregunta19': [pregunta19],
            'pregunta19_1': [pregunta19_1],
            'pregunta20': [pregunta20],
            'pregunta21': [pregunta21],
            'pregunta22': [pregunta22],
            'pregunta23': [pregunta23],
        })
        df = pd.concat([df, new_row], ignore_index= True)
        conn.update(worksheet = "EmpoPasto", data = df)
        st.success("Respuesta agregada exitosamente!!")
        time.sleep(2)
        st.rerun()

if st.button("Encuesta de Empopasto", type="primary"):
    agregar_encuesta()

col1, col2 = st.columns(2)
col1.metric("Total Encuestas", len(df), border=True)
col2.metric("Encuestas Restantes", 600 - len(df), border=True)

encuestadores = df.groupby("pregunta23")["Nombre"].count()
encuestados = df.groupby("Nombre")["pregunta23"].count()

col3, col4 = st.columns(2)
with col3:
    st.subheader("Encuestadores")
    st.write(encuestadores)
with col4:
    st.subheader("Encuestados")
    st.write(encuestados)
