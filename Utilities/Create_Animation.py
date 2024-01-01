import sys
from PIL import Image

figure_filenames = sys.argv[1:]  # Get the figure filenames from command line arguments
figures = []

for filename in figure_filenames:
    figure = Image.open(filename)
    figures.append(figure)

output_filename = "protein_interaction.gif"  
figures[0].save(
    output_filename,
    save_all=True,
    append_images=figures[1:], # Append all remaining figures 
    duration=200, 
    loop=0 
)

print(f"Saved animation to {output_filename}")

# Open the terminal:
# python Create_Animation.py interaction1.png interaction2.png interaction3.png


"""An improved script for creating a GIF file"""
import sys
from PIL import Image

def create_ppi_animation(figure_paths, output_filename="ppi_animation.gif", duration=200, loop=0):
    """Creates an animated GIF from a series of protein-protein interaction figures."""

    figures = []
    for figure_path in figure_paths:
        try:
            figure = Image.open(figure_path)
            figures.append(figure)
        except FileNotFoundError:
            print(f"Error: Figure file not found: {figure_path}")

    if not figures:
        print("No valid figures found. Animation not created.")
        return

    figures[0].save(
        output_filename,
        save_all=True,
        append_images=figures[1:], 
        duration=duration,
        loop=loop
    )

if __name__ == "__main__":
    figure_paths = sys.argv[1:]  
    create_ppi_animation(figure_paths)

# Open the terminal:
# python Create_Animation.py interaction1.png interaction2.png interaction3.png
