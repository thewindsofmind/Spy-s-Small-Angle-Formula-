import math

def estimate_object_size(image_width_pixels, image_height_pixels, focal_length_mm, altitude_meters, angle_of_view_degrees):
    """
    Estimates the physical size of an object in an aerial/satellite image.

    Args:
        image_width_pixels (int): Width of the image in pixels.
        image_height_pixels (int): Height of the image in pixels.
        focal_length_mm (float): Focal length of the camera lens in millimeters.
        altitude_meters (float): Altitude of the image capture in meters.
        angle_of_view_degrees (float): Angle of view of the camera in degrees.

    Returns:
        tuple: (object_width_meters, object_height_meters) - Estimated width and height of the object in meters.
    """

    # Convert focal length from mm to meters
    focal_length_meters = focal_length_mm / 1000.0

    # Convert angle of view to radians
    angle_of_view_radians = math.radians(angle_of_view_degrees)

    # Calculate the ground sample distance (GSD) using the correct formula
    gsd_width = (2 * altitude_meters * math.tan(angle_of_view_radians / 2)) / image_width_pixels
    gsd_height = (2 * altitude_meters * math.tan(angle_of_view_radians / 2)) / image_height_pixels

    # Calculate object size in meters
    object_width_meters = image_width_pixels * gsd_width
    object_height_meters = image_height_pixels * gsd_height

    return object_width_meters, object_height_meters


if __name__ == "__main__":
    # Get user inputs
    image_width = int(input("Enter image width in pixels: "))
    image_height = int(input("Enter image height in pixels: "))
    focal_length = float(input("Enter camera lens focal length in millimeters: "))
    altitude = float(input("Enter image capture altitude in meters: "))
    angle_view = float(input("Enter camera angle of view in degrees: "))

    # Estimate object size
    object_size = estimate_object_size(image_width, image_height, focal_length, altitude, angle_view)

    if object_size:
        width, height = object_size
        print(f"Estimated object width: {width:.2f} meters")
        print(f"Estimated object height: {height:.2f} meters")
