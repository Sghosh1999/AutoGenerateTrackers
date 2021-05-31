import streamlit as st
import os
import base64
import time
import pandas as pd
import daily_gen
import group_trackers


def main():


    # Sidebar
    activities = ["Home", "Generate Daily Trackers", "Generate Multi User Trcakers"]
    choice = st.sidebar.selectbox("Choose Activity", activities)

    if choice == "Home":
        st.title("Dailt Trcaker ++ :sunglasses:")
        
    if choice == "Generate Daily Trackers":
        daily_gen.main()

    if choice == "Generate Multi User Trcakers":
        group_trackers.main()

        


if __name__ == '__main__':
    main()
