import streamlit as st
from streamlit_image_gallery import streamlit_image_gallery

st.title("HTML-Based Image Gallery")
st.write("Now using regular HTML elements instead of Material-UI components!")

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
]

st.subheader("Gallery Structure:")
st.markdown("""
**HTML Structure now used:**
```html
<div style="display: grid; grid-template-columns: repeat(cols, 1fr); gap: Xpx;">
  <div style="display: flex; flex-direction: column;">
    <img src="..." />
    <p>Title Text</p>
  </div>
  <!-- More image items... -->
</div>
```

**Benefits:**
- ✅ No Material-UI dependency
- ✅ Lighter bundle size (-22KB)
- ✅ Full control over styling
- ✅ Standard HTML elements: `div`, `img`, `p`
- ✅ CSS Grid for responsive layout
""")

st.subheader("Interactive Gallery:")

# Use the gallery with callback
clicked_index = streamlit_image_gallery(
    images=images, 
    max_cols=3, 
    gap=8,
    key="html_gallery"
)

# Show results
if clicked_index is not None:
    st.success(f"Clicked image #{clicked_index}: {images[clicked_index]['title']}")
else:
    st.info("Click on any image or title to see the index!") 