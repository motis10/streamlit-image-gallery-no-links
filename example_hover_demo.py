import streamlit as st
from streamlit_image_gallery import streamlit_image_gallery

st.title("🎨 Image Gallery with Hover Effects")
st.write("**Hover over any image to see the beautiful color transition!**")

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
    {
        "src": 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4',
        "title": 'Mountains',
    },
]

st.markdown("""
### ✨ Hover Features:
- 🎨 **Light blue background** on hover (`#f0f8ff`)
- ⚡ **Smooth transition** (0.2s ease)
- 👆 **Pointer cursor** for better UX
- 📊 **Index tracking** - click to see which image you selected

### 🏗️ Technical Details:
- Uses **React state** to track hover
- **CSS transitions** for smooth effects
- **onMouseEnter/onMouseLeave** event handlers
- **Inline styling** with dynamic color changes
""")

st.subheader("Interactive Gallery:")

# Use the gallery with hover and click functionality
clicked_index = streamlit_image_gallery(
    images=images, 
    max_cols=3, 
    gap=10,
    key="hover_gallery"
)

# Show results
if clicked_index is not None:
    st.success(f"🎯 You clicked on image #{clicked_index}: **{images[clicked_index]['title']}**")
    st.write(f"Image URL: `{images[clicked_index]['src']}`")
else:
    st.info("✨ Hover over images to see the effect, then click to select!") 