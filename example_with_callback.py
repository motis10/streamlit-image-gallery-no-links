import streamlit as st
from streamlit_image_gallery import streamlit_image_gallery

# Sample images
images = [
    {
        "src": 'https://images.unsplash.com/photo-1718439111428-f6ef86aae18d',
        "title": 'White Flowers',
    },
    {
        "src": 'https://images.unsplash.com/photo-1718554517666-2978ede88574',
        "title": 'Bird',
    },
    {
        "src": 'https://images.unsplash.com/photo-1711526637497-bd9ecfc68567',
        "title": 'Sky',
    },
    {
        "src": 'https://images.unsplash.com/photo-1717207300523-434099274ff0',
        "title": 'Sunset',
    },
    {
        "src": 'https://images.unsplash.com/photo-1592417817098-8fd3d9eb14a5',
        "title": 'Food',
    },
]

st.subheader("Interactive Image Gallery")
st.write("Click on any image to see its index!")

# Use the component with a unique key to capture return values
clicked_index = streamlit_image_gallery(images=images, key="gallery")

# Display information about the clicked image
if clicked_index is not None:
    st.success(f"You clicked on image #{clicked_index}!")
    st.write(f"**Title:** {images[clicked_index]['title']}")
    st.write(f"**Source:** {images[clicked_index]['src']}")
    
    # You can now use this index for any logic you need
    if clicked_index == 0:
        st.info("You clicked on the first image!")
    elif clicked_index == len(images) - 1:
        st.info("You clicked on the last image!")
    else:
        st.info(f"You clicked on image {clicked_index + 1} out of {len(images)}")
else:
    st.info("Click on an image to see its details") 