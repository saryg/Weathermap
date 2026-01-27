def addWeatherWarnings(image, weather_warning_data):
    draw = ImageDraw.Draw(image)
    y = 970 if len(weather_warning_data) == 1 else 950
    x = 0
    current_y = y
    icon_path = settings.icon_path + "warning.png"  # "warning_no_transparency.png"
    small_font_size = settings.SMALL_FONT
    smaller_font_size = settings.SMALLER_FONT
    icon_size = settings.MED_ICON_SIZE
    font_colour = "black"
    for index, warning_data in enumerate(weather_warning_data):
        if warning_data["type"] != "Advisory" and "blight" not in warning_data["headline"].lower():
            # "Blight":
            text_str = f"{warning_data['level']} {warning_data['headline']}"
            # {warning_data['type']} {warning_data['status']}"
            y_offset, icon_start_x, text_start_x = placeIconAndData(
                draw,
                image,
                current_y,
                0,
                settings.map_display_width,
                icon_path,
                text_str,
                icon_size,
                small_font_size,
                font_colour,
            )
            current_y += y_offset - 27
            onset = prs.parse(warning_data["onset"])
            onset_str = f"{onset:%H:%M} {onset:%d/%m}"
            expiry = prs.parse(warning_data["expiry"])
            expiry_str = f"{expiry:%H:%M} {expiry:%d/%m}"
            text_str = f"{onset_str} - {expiry_str}"
            centred_x, w, h = centreTextHorizontally(
                draw=draw,
                font=small_font_size,
                text=text_str,
                x_start=0,
                x_end=settings.map_display_width,
            )
            draw.text(
                (text_start_x, current_y),
                text_str,
                fill="black",
                font=small_font_size,
                stroke_width=2,
                stroke_fill="white",
            )
            current_y += y_offset
    return image
    draw = ImageDraw.Draw(image)
    y = 970 if len(weather_warning_data) == 1 else 950
    current_y = y
    icon_path = settings.icon_path + "warning.png"  # "warning_no_transparency.png"
    small_font_size = settings.SMALL_FONT
    smaller_font_size = settings.SMALLER_FONT
    icon_size = settings.MED_ICON_SIZE
    font_colour = "black"
    for warning in range(len(weather_warning_data)):
        if (
            weather_warning_data[warning]["type"] != "Advisory"
            and "blight"
            not in weather_warning_data[warning]["headline"].lower()
        ):  # "Blight":
            text_str = (
                f"{weather_warning_data[warning]['level']} "
                f"{weather_warning_data[warning]['headline']}"
            )  # {weather_warning_data[warning]['type']} {weather_warning_data[warning]['status']}"
            y_offset, icon_start_x, text_start_x = placeIconAndData(
                draw,
                image,
                current_y,
                0,
                settings.map_display_width,
                icon_path,
                text_str,
                icon_size,
                small_font_size,
                font_colour,
            )
            current_y += y_offset - 27
            onset = prs.parse(weather_warning_data[warning]["onset"])
            onset_str = f"{onset:%H:%M} {onset:%d/%m}"
            expiry = prs.parse(weather_warning_data[warning]["expiry"])
            expiry_str = f"{expiry:%H:%M} {expiry:%d/%m}"
            text_str = f"{onset_str} - {expiry_str}"
            centred_x, w, h = centreTextHorizontally(
                draw=draw,
                font=small_font_size,
                text=text_str,
                x_start=0,
                x_end=settings.map_display_width,
            )
            draw.text(
                (text_start_x, current_y),
                text_str,
                fill="black",
                font=small_font_size,
                stroke_width=2,
                stroke_fill="white",
            )
            current_y += y_offset
    return image
    draw = ImageDraw.Draw(image)
    y = 970 if len(weather_warning_data) == 1 else 950
    x = 0
    current_y = y
    icon_path = settings.icon_path + "warning.png"  # "warning_no_transparency.png"
    small_font_size = settings.SMALL_FONT
    smaller_font_size = settings.SMALLER_FONT
    icon_size = settings.MED_ICON_SIZE
    font_colour = "black"

    for warning in range(len(weather_warning_data)):
        if (
            weather_warning_data[warning]["type"] != "Advisory"
            and "blight" not in weather_warning_data[warning]["headline"].lower()
        ):
            #"Blight":
            text_str = (
                f"{weather_warning_data[warning]['level']} "
                f"{weather_warning_data[warning]['headline']}"
            )
            #{weather_warning_data[warning]['type']} {weather_warning_data[warning]['status']}"
            y_offset, icon_start_x, text_start_x = placeIconAndData(
                draw,
                image,
                current_y,
                0,
                settings.map_display_width,
                icon_path,
                text_str,
                icon_size,
                small_font_size,
                font_colour,
            )
            current_y += y_offset - 27

            onset = prs.parse(weather_warning_data[warning]["onset"])
            onset_str = f"{onset:%H:%M} {onset:%d/%m}"

            expiry = prs.parse(weather_warning_data[warning]["expiry"])
            expiry_str = f"{expiry:%H:%M} {expiry:%d/%m}"

            text_str = f"{onset_str} - {expiry_str}"

            centred_x, w, h = centreTextHorizontally(
                draw=draw,
                font=small_font_size,
                text=text_str,
                x_start=0,
                x_end=settings.map_display_width,
            )

            draw.text(
                (text_start_x, current_y),
                text_str,
                fill="black",
                font=small_font_size,
                stroke_width=2,
                stroke_fill="white",
            )
            current_y += y_offset

    return image
