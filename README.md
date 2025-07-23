# Streamlit Image Gallery Enhanced 🖼️✨

[![PyPI version](https://badge.fury.io/py/streamlit-image-gallery-enhanced.svg)](https://badge.fury.io/py/streamlit-image-gallery-enhanced)
[![Python](https://img.shields.io/pypi/pyversions/streamlit-image-gallery-enhanced.svg)](https://pypi.org/project/streamlit-image-gallery-enhanced/)

An enhanced Streamlit component for displaying images in a responsive grid with **hover effects**, **click callbacks**, and **modern HTML structure**.

## 🚀 Features

- ✨ **Hover effects** with smooth transitions
- 👆 **Click callbacks** - get the index of clicked images
- 🎨 **No Material-UI dependency** - pure HTML/CSS
- 📱 **Responsive grid layout** using CSS Grid
- 🖼️ **Fixed image dimensions** with object-fit cover
- 🎯 **Clickable titles** below each image
- ⚡ **Lightweight** - 22KB smaller than Material-UI version
- 🔧 **Customizable** gap, columns, and dimensions

## 📦 Installation

```bash
pip install streamlit-image-gallery-enhanced
```

## 🎯 Quick Start

```python
import streamlit as st
from streamlit_image_gallery_enhanced import streamlit_image_gallery

# Define your images
images = [
    {
        "src": "https://images.unsplash.com/photo-1718439111428-f6ef86aae18d",
        "title": "Beautiful Flowers"
    },
    {
        "src": "https://images.unsplash.com/photo-1718554517666-2978ede88574", 
        "title": "Cute Bird"
    },
    # Add more images...
]

# Display gallery with click callback
clicked_index = streamlit_image_gallery(
    images=images,
    max_cols=3,
    gap=10,
    key="gallery"
)

# Handle clicks
if clicked_index is not None:
    st.write(f"You clicked: {images[clicked_index]['title']}")
```

## 🎨 Advanced Usage

### Custom Styling
```python
streamlit_image_gallery(
    images=images,
    max_cols=4,          # Maximum columns
    max_rows=2,          # Maximum rows  
    gap=15,              # Gap between images
    max_width=800,       # Container max width
    key="my_gallery"     # Unique key for state
)
```

### Image Structure
```python
images = [
    {
        "src": "https://example.com/image.jpg",  # Required: image URL
        "title": "Image Title"                   # Required: image title
    }
]
```

## ✨ What's New in Enhanced Version

### 🎨 Visual Improvements
- **Hover Effects**: Light blue background (`#f0f8ff`) on hover
- **Smooth Transitions**: 0.2s ease animations  
- **Fixed Dimensions**: 150px height, 100% width with object-fit cover
- **Clean Titles**: Clickable text below images (no overlay)

### 🏗️ Technical Improvements  
- **Pure HTML**: No Material-UI dependency (22KB smaller)
- **CSS Grid**: Modern responsive layout
- **React State**: Proper hover state management
- **Click Callbacks**: Returns image index to Python

### 🎯 Interactive Features
- **Both image and title clickable**
- **Index tracking** for click handling
- **Keyboard accessible**
- **Touch-friendly** for mobile

## 🔧 Component Structure

```html
<div style="display: grid; grid-template-columns: repeat(cols, 1fr);">
  <div> <!-- Container with hover effects -->
    <img style="height: 150px; width: 100%; object-fit: cover;" />
    <p>Title Text</p>
  </div>
</div>
```

## 📋 API Reference

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `images` | `List[Dict]` | **Required** | List of image dictionaries |
| `max_cols` | `int` | `2` | Maximum number of columns |
| `max_rows` | `int` | `2` | Maximum number of rows |
| `gap` | `int` | `10` | Gap between images (px) |
| `max_width` | `int` | `400` | Container max width (px) |
| `key` | `str` | `None` | Unique component key |

### Returns

- `int | None`: Index of clicked image (0-based), or `None` if no click

## 🎨 Styling Examples

### Large Gallery
```python
streamlit_image_gallery(
    images=images,
    max_cols=5,
    max_rows=3, 
    gap=20,
    max_width=1200
)
```

### Compact Gallery
```python
streamlit_image_gallery(
    images=images,
    max_cols=2,
    gap=5,
    max_width=300
)
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License - see LICENSE file for details.

## 🙏 Acknowledgments

Based on the original [streamlit-image-gallery](https://github.com/virtUOS/streamlit-image-gallery) by virtUOS, enhanced with modern features and improved UX.
