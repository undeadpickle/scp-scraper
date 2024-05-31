import streamlit as st
import pandas as pd
from scrape_scp import scrape_scp_website

# Title of the app
st.title("SCP Foundation Scraper")

# Sidebar for configuration
st.sidebar.header("Configuration")
series_options = {
    "Series I": "http://scp-wiki.wikidot.com/scp-series",
    "Series II": "http://scp-wiki.wikidot.com/scp-series-2",
    "Series III": "http://scp-wiki.wikidot.com/scp-series-3",
    # Add more series as needed
}
series_choice = st.sidebar.selectbox(
    "Select SCP Series to scrape:", list(series_options.keys())
)

# Display selected series URL
url = series_options[series_choice]
st.sidebar.write(f"URL to scrape: {url}")

# Scrape the website when the button is clicked
if st.sidebar.button("Scrape Website"):
    try:
        data = scrape_scp_website(url)
        st.sidebar.success(f"Successfully scraped the website: {url}")
        if data:
            st.write("### SCP Articles found on the website:")
            for entry in data:
                st.write(entry)

            # Export to CSV option
            df = pd.DataFrame(data, columns=["SCP Articles"])
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name="scp_articles.csv",
                mime="text/csv",
            )
        else:
            st.warning(
                "No SCP articles found. Please check the URL or try a different page."
            )
    except Exception as e:
        st.sidebar.error(f"Error: {e}")

# Instructions
st.write(
    """
### Instructions:
1. Select the SCP Series to scrape from the sidebar.
2. Click the "Scrape Website" button to extract SCP articles.
3. View the results below and optionally download the data as a CSV file.
"""
)

# Run the app
if __name__ == "__main__":
    st.write(
        "Configure the scraping options from the sidebar and execute the scraping process."
    )
