import streamlit as st
import requests

st.set_page_config(layout="wide")
st.header("Solsea NFT Explorer")

st.sidebar.title("Solsea NFT Explorer")
title = st.sidebar.text_input("NFT Title")
description = st.sidebar.text_input("NFT Description")
collection = st.sidebar.text_input("NFT Collection ID")

params = {}

if collection:
    params["nft_collection"] = collection

if title:
    params["Title"] = title

if description:
    params["Description"] = description

response = requests.get("https://api.all.art/v1/solana/", params=params).json()

for asset in response["data"]:
    if asset["Title"]:
        st.write(asset["Title"])
        st.write(asset["Description"])
    else:
        st.write(f"{asset['nft_collection']['Title']}")

    if asset["Preview_URL"].endswith(".mp4") or asset["Preview_URL"].endswith(".mov") or asset["Preview_URL"].endswith(".gif") or asset["Preview_URL"].endswith(".png") or asset["Preview_URL"].endswith(".jpg") or asset["Preview_URL"].endswith(".svg"):
        st.video(asset["Preview_URL"])
    else:
        st.image(asset["Preview_URL"])

    st.write("---")
