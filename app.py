import streamlit as st
import requests
import json

st.header(f"SOLSEA Explorer")
st.sidebar.header("Filters")

collection = st.sidebar.text_input("NFT Collection ID")

params = {}

if collection:
    params["nft_collection"] = collection

r = requests.get("https://api.all.art/v1/solana/", params=params)
response = r.json()

for asset in response["data"]:
    if asset["Title"]:
        st.write(asset["Title"])
    else:
        st.write(
            f"{asset['nft_collection']['Title']}"
        )

    if asset["Preview_URL"].endswith(".mp4") or asset["Preview_URL"].endswith(".mov"):
        st.video(asset["Preview_URL"])
    else:
        st.image(asset["Preview_URL"])

# st.write(r.json())
