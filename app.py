import streamlit as st
import requests
import json

st.header(f"SOLSEA Explorer")

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

r = requests.get("https://api.all.art/v1/solana/", params=params)
response = r.json()

for asset in response["data"]:
    if asset["Title"]:
        st.write(asset["Title"])
        st.write(asset["Description"])
    else:
        st.write(
            f"{asset['nft_collection']['Title']}"
        )

    if asset["Preview_URL"].endswith(".mp4") or asset["Preview_URL"].endswith(".mov") or asset["Preview_URL"].endswith(".m4v") or asset["Preview_URL"].endswith(".avi") or asset["Preview_URL"].endswith(".mpg") or asset["Preview_URL"].endswith(".mpeg"):
        st.video(asset["Preview_URL"])
    else:
        st.image(asset["Preview_URL"])

# st.write(r.json())
