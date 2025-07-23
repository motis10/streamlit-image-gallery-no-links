import {
  StreamlitComponentBase,
  withStreamlitConnection,
  Streamlit,
} from "streamlit-component-lib";
import React, { ReactNode } from "react";
// Removed Material-UI imports - using regular HTML elements

interface Image {
  src: string,
  title: string
}

class StreamlitGallery extends StreamlitComponentBase {
  private imageListElement: HTMLDivElement | null | undefined;

  // Arguments that are passed to the plugin in Python are accessible
  // via `this.props.args`.
  private images: Image[] = this.props.args["images"];

  // State to track hover for each image
  state = {
    hoveredIndex: -1
  };

  private maxWidth = this.props.args["max_width"] ?? 400;

  private gap = this.props.args["gap"] ?? 10;

  private maxCols = this.props.args["max_cols"] ?? 2;
  private maxRows = this.props.args["max_rows"] ?? 2;

    public render = (): ReactNode => {
    const numberImages = this.images.length;
    const cols = Math.min(numberImages, this.maxCols);

    return (
      <div
        style={{
          display: 'grid',
          gridTemplateColumns: `repeat(${cols}, 1fr)`,
          gap: `${this.gap}px`,
          maxWidth: this.maxWidth,
          width: '100%',
          margin: '0 auto'
        }}
        ref={(element) => { this.imageListElement = element }}
      >
        {this.images.map((image, index) => (
          <div
            key={image.src}
            onClick={(event) => this.openImage(event, index)}
            onMouseEnter={() => this.setState({ hoveredIndex: index })}
            onMouseLeave={() => this.setState({ hoveredIndex: -1 })}
            style={{
              display: 'flex',
              flexDirection: 'column',
              overflow: 'hidden',
              borderRadius: '4px',
              backgroundColor: this.state.hoveredIndex === index ? '#f0f8ff' : 'transparent',
              transition: 'background-color 0.2s ease',
              cursor: 'pointer'
            }}
          >
            <img
              src={image.src}
              alt={image.title}
              style={{
                cursor: "pointer",
                display: 'block',
                height: '150px',
                width: '100%',
                margin: '0 auto',
                objectFit: 'cover'
              }}
              loading="lazy"
            />
            <p
              style={{
                cursor: "pointer",
                margin: "0",
                padding: "12px",
                textAlign: "center",
                fontSize: "14px",
                fontWeight: "500",
                color: "#333",
                borderRadius: "0 0 4px 4px"
              }}
            >
              {image.title}
            </p>
          </div>
        ))}
      </div>
    )
  }

  private openImage = (event: React.MouseEvent<HTMLElement>, index: number) => {
    Streamlit.setComponentValue(index);
  }
}

export default withStreamlitConnection(StreamlitGallery);
