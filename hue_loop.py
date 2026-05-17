import os
import argparse
from PIL import Image

def create_hue_loop_gif(image_path, output_gif_path, total_frames, duration_ms, side_by_side):
    if not os.path.exists(image_path):
        print(f"Error: '{image_path}' not found. Please provide a valid file path.")
        return

    # Load original image and convert to RGB
    orig_img = Image.open(image_path).convert('RGB')
    width, height = orig_img.size

    # Create the original static image in HSV format for calculations
    orig_hsv = orig_img.convert('HSV')
    h_orig, s_orig, v_orig = orig_hsv.split()

    frames = []

    # Shift hue from 0 to 255 (Pillow scales 0-360 degrees into a 0-255 byte value)
    for frame_idx in range(total_frames):
        # Calculate hue shift for this frame to make a perfect circle loop
        hue_shift = int((frame_idx / total_frames) * 256)

        # Shift the hue channel
        h_shifted = h_orig.point(lambda p: (p + hue_shift) % 256)

        # Merge channels back and convert back to RGB
        shifted_hsv = Image.merge('HSV', (h_shifted, s_orig, v_orig))
        shifted_rgb = shifted_hsv.convert('RGB')

        if side_by_side:
            # Create a blank double-wide canvas for side-by-side images
            combined_frame = Image.new('RGB', (width * 2, height))
            # Paste original image on the left, shifted image on the right
            combined_frame.paste(orig_img, (0, 0))
            combined_frame.paste(shifted_rgb, (width, 0))
            frames.append(combined_frame)
        else:
            # Only use the animated hue shifting image
            frames.append(shifted_rgb)

    # Save frames as a perfectly looping GIF
    frames.save(
        output_gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration_ms,
        loop=0  # 0 means loop infinitely
    )
    print(f"Success! Perfect loop GIF saved as: {output_gif_path}")

if __name__ == "__main__":
    # Setup argparse to handle defaults and optional flags
    parser = argparse.ArgumentParser(description="Create a perfectly looping hue-shifting GIF.")

    parser.add_argument("-i", "--input", default="input.jpg", help="Path to input image (default: input.jpg)")
    parser.add_argument("-o", "--output", default="perfect_hue_loop.gif", help="Path to output GIF (default: perfect_hue_loop.gif)")
    parser.add_argument("-f", "--frames", type=int, default=45, help="Total animation frames (default: 45)")
    parser.add_argument("-d", "--duration", type=int, default=40, help="Frame duration in ms (default: 40)")
    parser.add_argument("-s", "--side-by-side", action="store_true", help="Put original static image side-by-side with animated image (default: False)")

    args = parser.parse_args()

    create_hue_loop_gif(
        image_path=args.input,
        output_gif_path=args.output,
        total_frames=args.frames,
        duration_ms=args.duration,
        side_by_side=args.side_by_side
    )
