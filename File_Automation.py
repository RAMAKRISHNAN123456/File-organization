import os
import streamlit as st

def filecreater(path):
    extensions = []
    files = os.listdir(path)

    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1][1:]
            if ext:
                folder_path = os.path.join(path, ext)
                if folder_path not in extensions:
                    extensions.append(folder_path)

    for folder in extensions:
        os.makedirs(folder, exist_ok=True)

        for file in files:
            if os.path.splitext(file)[1][1:] == os.path.basename(folder):
                old_path = os.path.join(path, file)
                new_path = os.path.join(folder, file)
                if os.path.exists(old_path):
                    os.rename(old_path, new_path)

# -------- Streamlit UI --------
st.set_page_config(page_title="File Organizer", page_icon="📂")

st.title("📂 File Organizer using Streamlit")
st.write("Organize files into folders based on file extension")

path = st.text_input(
    "Enter Folder Path",
    placeholder="C:\\Users\\Admin\\OneDrive\\Desktop\\New folder"
)

if st.button("Organize Files"):
    if path and os.path.exists(path):
        try:
            filecreater(path)
            st.success("✅ Files organized successfully!")
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter a valid folder path")