import streamlit as st
import pandas as pd

# Ensure required dependencies are installed
try:
    import micropip
except ModuleNotFoundError:
    import subprocess
    subprocess.run(["pip", "install", "micropip"], check=True)
    import micropip

# Load the dataset
file_path = "/mnt/data/2024 Perennial List.xlsx"
df = pd.read_excel(file_path, sheet_name="Report1")

# Sample common names dictionary
common_names = {
    "MAZUS REPTANS": "Creeping Mazus",
    "AJUGA BLACK SCALLOP": "Black Scallop Bugleweed",
    "AJUGA BURGANDY GLOW": "Burgundy Glow Bugleweed",
    "AJUGA CHOCOLATE CHIP": "Chocolate Chip Bugleweed",
    "AJUGA CORDIAL CANARY": "Cordial Canary Bugleweed"
}

# Sample care instructions dictionary (can be expanded)
care_instructions = {
    "MAZUS REPTANS": "Full sun to partial shade, moist soil, fast-spreading groundcover.",
    "AJUGA BLACK SCALLOP": "Partial to full shade, well-drained soil, low maintenance.",
    "AJUGA BURGANDY GLOW": "Partial shade, prefers moist but well-drained soil.",
    "AJUGA CHOCOLATE CHIP": "Shade to partial sun, tolerates drought once established.",
    "AJUGA CORDIAL CANARY": "Thrives in shade, requires moderate watering."
}

# Placeholder images dictionary (can be updated with actual URLs)
image_links = {
    "MAZUS REPTANS": "https://example.com/mazus.jpg",
    "AJUGA BLACK SCALLOP": "https://example.com/ajuga_black_scallop.jpg",
    "AJUGA BURGANDY GLOW": "https://example.com/ajuga_burgandy_glow.jpg",
    "AJUGA CHOCOLATE CHIP": "https://example.com/ajuga_chocolate_chip.jpg",
    "AJUGA CORDIAL CANARY": "https://example.com/ajuga_cordial_canary.jpg"
}

# Streamlit App
st.title("Perennial Plant Catalog")
st.write("Browse a list of perennial plants with care instructions and photos.")

# Search bar
search_query = st.text_input("Search for a plant:").strip().lower()
filtered_df = df[df["Item Description"].str.lower().str.contains(search_query, na=False)] if search_query else df

# Dropdown to select plant
if not filtered_df.empty:
    plant_name = st.selectbox("Select a plant:", filtered_df["Item Description"].unique())
    common_name = common_names.get(plant_name, "Common name not available.")
    care_text = care_instructions.get(plant_name, "Care instructions not available.")
    image_url = image_links.get(plant_name, "https://via.placeholder.com/150")
    
    # Display plant details
    st.subheader(f"{plant_name} ({common_name})")
    st.image(image_url, caption=plant_name)
    st.write(f"**Care Instructions:** {care_text}")
else:
    st.write("No matching plants found.")

st.write("\n\nMore plants coming soon!")