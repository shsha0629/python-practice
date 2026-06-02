import streamlit as st
import pandas as pd

@st.cache_data
def load_marketing():
    marketing = pd.read_csv('./marketing_campaign_dataset.xls')

    marketing['Acquisition_Cost'] = (
            marketing['Acquisition_Cost']
            .str.replace('[$,]', '', regex=True)
            .astype(float)
        )
    marketing['Date'] = pd.to_datetime(marketing['Date'])

    return marketing

df = load_marketing()

st.title("📣 마케팅 캠페인 대시보드")
st.write(f"전체 데이터: {len(df):,}행")