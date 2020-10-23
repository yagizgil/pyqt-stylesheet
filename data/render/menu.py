class Menu():

    def __init__(self, text, data):
        self.text = text
        self.data = data

        if self.text == "QMenu":
            self.text = "QMenuBar"
        else:
            pass

        self.write()

    def write(self):
        f = open("a", "w")

        f.write(self.text + " {")

        if self.data.bme["color"] != "":
            f.write("\n   color: {};".format(self.data.bme["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.bme["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.bme["outline"]))

        if self.data.bme["width_value"] != 0 and self.data.bme["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.bme["width_value"], self.data.bme["width_type"]))

        if self.data.bme["height_value"] != 0 and self.data.bme["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.bme["height_value"], self.data.bme["height_type"]))

        if self.data.bme["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.bme["font_family"]))

        if self.data.bme["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.bme["font_size"]))

        if self.data.bme["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.bme["font_weight"]))

        if self.data.bme["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.bme["font_style"]))

        if self.data.bme["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.bme["line_height"]))

        if self.data.bme["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.bme["text_align"]))

        if self.data.bme["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.bme["text_decoration"]))

        if self.data.bme["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.bme["text_transform"]))

        if self.data.bme["background"] != "":
            f.write("\n   background: {};".format(self.data.bme["background"]))

        if self.data.bme["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.bme["background_image"]))

        if self.data.bme["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.bme["background_color"]))

        if self.data.bme["border"] != "":
            f.write("\n   border: {};".format(self.data.bme["border"]))

        if self.data.bme["border_width_value"] != 0 and self.data.bme["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.bme["border_width_value"], self.data.bme["border_width_type"]))

        if self.data.bme["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.bme["border_style"]))

        if self.data.bme["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.bme["border_color"]))

        if self.data.bme["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.bme["border_top"]))

        if self.data.bme["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.bme["border_right"]))

        if self.data.bme["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.bme["border_bottom"]))

        if self.data.bme["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.bme["border_left"]))

        if self.data.bme["border_radius"] != 0 and self.data.bme["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.bme["border_radius"]))

        if self.data.bme["padding_top_value"] != 0 and self.data.bme["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.bme["padding_top_value"], self.data.bme["padding_top_type"]))

        if self.data.bme["padding_right_value"] != 0 and self.data.bme["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.bme["padding_right_value"], self.data.bme["padding_right_type"]))

        if self.data.bme["padding_bottom_value"] != 0 and self.data.bme["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.bme["padding_bottom_value"], self.data.bme["padding_bottom_type"]))

        if self.data.bme["padding_left_value"] != 0 and self.data.bme["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.bme["padding_left_value"], self.data.bme["padding_left_type"]))


        if self.data.bme["margin_top_value"] != 0 and self.data.bme["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.bme["margin_top_value"], self.data.bme["margin_top_type"]))

        if self.data.bme["margin_right_value"] != 0 and self.data.bme["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.bme["margin_right_value"], self.data.bme["margin_right_type"]))

        if self.data.bme["margin_bottom_value"] != 0 and self.data.bme["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.bme["margin_bottom_value"], self.data.bme["margin_bottom_type"]))

        if self.data.bme["margin_left_value"] != 0 and self.data.bme["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.bme["margin_left_value"], self.data.bme["margin_left_type"]))


        f.write("\n}")



        f.write("\n")




        f.write(self.text + ":hover {")

        if self.data.bhover["color"] != "":
            f.write("\n   color: {};".format(self.data.bhover["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.bhover["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.bhover["outline"]))

        if self.data.bhover["width_value"] != 0 and self.data.bhover["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.bhover["width_value"], self.data.bhover["width_type"]))

        if self.data.bhover["height_value"] != 0 and self.data.bhover["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.bhover["height_value"], self.data.bhover["height_type"]))

        if self.data.bhover["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.bhover["font_family"]))

        if self.data.bhover["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.bhover["font_size"]))

        if self.data.bhover["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.bhover["font_weight"]))

        if self.data.bhover["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.bhover["font_style"]))

        if self.data.bhover["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.bhover["line_height"]))

        if self.data.bhover["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.bhover["text_align"]))

        if self.data.bhover["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.bhover["text_decoration"]))

        if self.data.bhover["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.bhover["text_transform"]))

        if self.data.bhover["background"] != "":
            f.write("\n   background: {};".format(self.data.bhover["background"]))

        if self.data.bhover["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.bhover["background_image"]))

        if self.data.bhover["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.bhover["background_color"]))

        if self.data.bhover["border"] != "":
            f.write("\n   border: {};".format(self.data.bhover["border"]))

        if self.data.bhover["border_width_value"] != 0 and self.data.bhover["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.bhover["border_width_value"], self.data.bhover["border_width_type"]))

        if self.data.bhover["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.bhover["border_style"]))

        if self.data.bhover["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.bhover["border_color"]))

        if self.data.bhover["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.bhover["border_top"]))

        if self.data.bhover["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.bhover["border_right"]))

        if self.data.bhover["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.bhover["border_bottom"]))

        if self.data.bhover["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.bhover["border_left"]))

        if self.data.bhover["border_radius"] != 0 and self.data.bhover["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.bhover["border_radius"]))

        if self.data.bhover["padding_top_value"] != 0 and self.data.bhover["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.bhover["padding_top_value"], self.data.bhover["padding_top_type"]))

        if self.data.bhover["padding_right_value"] != 0 and self.data.bhover["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.bhover["padding_right_value"], self.data.bhover["padding_right_type"]))

        if self.data.bhover["padding_bottom_value"] != 0 and self.data.bhover["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.bhover["padding_bottom_value"], self.data.bhover["padding_bottom_type"]))

        if self.data.bhover["padding_left_value"] != 0 and self.data.bhover["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.bhover["padding_left_value"], self.data.bhover["padding_left_type"]))


        if self.data.bhover["margin_top_value"] != 0 and self.data.bhover["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.bhover["margin_top_value"], self.data.bhover["margin_top_type"]))

        if self.data.bhover["margin_right_value"] != 0 and self.data.bhover["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.bhover["margin_right_value"], self.data.bhover["margin_right_type"]))

        if self.data.bhover["margin_bottom_value"] != 0 and self.data.bhover["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.bhover["margin_bottom_value"], self.data.bhover["margin_bottom_type"]))

        if self.data.bhover["margin_left_value"] != 0 and self.data.bhover["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.bhover["margin_left_value"], self.data.bhover["margin_left_type"]))


        f.write("\n}")




        f.write("\n")




        f.write(self.text + "::item {")

        if self.data.bitem["color"] != "":
            f.write("\n   color: {};".format(self.data.bitem["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.bitem["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.bitem["outline"]))

        if self.data.bitem["width_value"] != 0 and self.data.bitem["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.bitem["width_value"], self.data.bitem["width_type"]))

        if self.data.bitem["height_value"] != 0 and self.data.bitem["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.bitem["height_value"], self.data.bitem["height_type"]))

        if self.data.bitem["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.bitem["font_family"]))

        if self.data.bitem["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.bitem["font_size"]))

        if self.data.bitem["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.bitem["font_weight"]))

        if self.data.bitem["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.bitem["font_style"]))

        if self.data.bitem["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.bitem["line_height"]))

        if self.data.bitem["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.bitem["text_align"]))

        if self.data.bitem["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.bitem["text_decoration"]))

        if self.data.bitem["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.bitem["text_transform"]))

        if self.data.bitem["background"] != "":
            f.write("\n   background: {};".format(self.data.bitem["background"]))

        if self.data.bitem["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.bitem["background_image"]))

        if self.data.bitem["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.bitem["background_color"]))

        if self.data.bitem["border"] != "":
            f.write("\n   border: {};".format(self.data.bitem["border"]))

        if self.data.bitem["border_width_value"] != 0 and self.data.bitem["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.bitem["border_width_value"], self.data.bitem["border_width_type"]))

        if self.data.bitem["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.bitem["border_style"]))

        if self.data.bitem["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.bitem["border_color"]))

        if self.data.bitem["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.bitem["border_top"]))

        if self.data.bitem["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.bitem["border_right"]))

        if self.data.bitem["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.bitem["border_bottom"]))

        if self.data.bitem["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.bitem["border_left"]))

        if self.data.bitem["border_radius"] != 0 and self.data.bitem["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.bitem["border_radius"]))

        if self.data.bitem["padding_top_value"] != 0 and self.data.bitem["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.bitem["padding_top_value"], self.data.bitem["padding_top_type"]))

        if self.data.bitem["padding_right_value"] != 0 and self.data.bitem["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.bitem["padding_right_value"], self.data.bitem["padding_right_type"]))

        if self.data.bitem["padding_bottom_value"] != 0 and self.data.bitem["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.bitem["padding_bottom_value"], self.data.bitem["padding_bottom_type"]))

        if self.data.bitem["padding_left_value"] != 0 and self.data.bitem["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.bitem["padding_left_value"], self.data.bitem["padding_left_type"]))


        if self.data.bitem["margin_top_value"] != 0 and self.data.bitem["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.bitem["margin_top_value"], self.data.bitem["margin_top_type"]))

        if self.data.bitem["margin_right_value"] != 0 and self.data.bitem["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.bitem["margin_right_value"], self.data.bitem["margin_right_type"]))

        if self.data.bitem["margin_bottom_value"] != 0 and self.data.bitem["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.bitem["margin_bottom_value"], self.data.bitem["margin_bottom_type"]))

        if self.data.bitem["margin_left_value"] != 0 and self.data.bitem["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.bitem["margin_left_value"], self.data.bitem["margin_left_type"]))


        f.write("\n}")




        f.write("\n")




        f.write(self.text + "::item:selected {")

        if self.data.bitem_selected["color"] != "":
            f.write("\n   color: {};".format(self.data.bitem_selected["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.bitem_selected["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.bitem_selected["outline"]))

        if self.data.bitem_selected["width_value"] != 0 and self.data.bitem_selected["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.bitem_selected["width_value"], self.data.bitem_selected["width_type"]))

        if self.data.bitem_selected["height_value"] != 0 and self.data.bitem_selected["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.bitem_selected["height_value"], self.data.bitem_selected["height_type"]))

        if self.data.bitem_selected["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.bitem_selected["font_family"]))

        if self.data.bitem_selected["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.bitem_selected["font_size"]))

        if self.data.bitem_selected["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.bitem_selected["font_weight"]))

        if self.data.bitem_selected["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.bitem_selected["font_style"]))

        if self.data.bitem_selected["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.bitem_selected["line_height"]))

        if self.data.bitem_selected["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.bitem_selected["text_align"]))

        if self.data.bitem_selected["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.bitem_selected["text_decoration"]))

        if self.data.bitem_selected["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.bitem_selected["text_transform"]))

        if self.data.bitem_selected["background"] != "":
            f.write("\n   background: {};".format(self.data.bitem_selected["background"]))

        if self.data.bitem_selected["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.bitem_selected["background_image"]))

        if self.data.bitem_selected["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.bitem_selected["background_color"]))

        if self.data.bitem_selected["border"] != "":
            f.write("\n   border: {};".format(self.data.bitem_selected["border"]))

        if self.data.bitem_selected["border_width_value"] != 0 and self.data.bitem_selected["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.bitem_selected["border_width_value"], self.data.bitem_selected["border_width_type"]))

        if self.data.bitem_selected["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.bitem_selected["border_style"]))

        if self.data.bitem_selected["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.bitem_selected["border_color"]))

        if self.data.bitem_selected["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.bitem_selected["border_top"]))

        if self.data.bitem_selected["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.bitem_selected["border_right"]))

        if self.data.bitem_selected["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.bitem_selected["border_bottom"]))

        if self.data.bitem_selected["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.bitem_selected["border_left"]))

        if self.data.bitem_selected["border_radius"] != 0 and self.data.bitem_selected["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.bitem_selected["border_radius"]))

        if self.data.bitem_selected["padding_top_value"] != 0 and self.data.bitem_selected["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.bitem_selected["padding_top_value"], self.data.bitem_selected["padding_top_type"]))

        if self.data.bitem_selected["padding_right_value"] != 0 and self.data.bitem_selected["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.bitem_selected["padding_right_value"], self.data.bitem_selected["padding_right_type"]))

        if self.data.bitem_selected["padding_bottom_value"] != 0 and self.data.bitem_selected["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.bitem_selected["padding_bottom_value"], self.data.bitem_selected["padding_bottom_type"]))

        if self.data.bitem_selected["padding_left_value"] != 0 and self.data.bitem_selected["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.bitem_selected["padding_left_value"], self.data.bitem_selected["padding_left_type"]))


        if self.data.bitem_selected["margin_top_value"] != 0 and self.data.bitem_selected["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.bitem_selected["margin_top_value"], self.data.bitem_selected["margin_top_type"]))

        if self.data.bitem_selected["margin_right_value"] != 0 and self.data.bitem_selected["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.bitem_selected["margin_right_value"], self.data.bitem_selected["margin_right_type"]))

        if self.data.bitem_selected["margin_bottom_value"] != 0 and self.data.bitem_selected["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.bitem_selected["margin_bottom_value"], self.data.bitem_selected["margin_bottom_type"]))

        if self.data.bitem_selected["margin_left_value"] != 0 and self.data.bitem_selected["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.bitem_selected["margin_left_value"], self.data.bitem_selected["margin_left_type"]))


        f.write("\n}")




        f.write("\n")




        f.write(self.text + "::item:pressed {")

        if self.data.item_pressed["color"] != "":
            f.write("\n   color: {};".format(self.data.item_pressed["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.item_pressed["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.item_pressed["outline"]))

        if self.data.item_pressed["width_value"] != 0 and self.data.item_pressed["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.item_pressed["width_value"], self.data.item_pressed["width_type"]))

        if self.data.item_pressed["height_value"] != 0 and self.data.item_pressed["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.item_pressed["height_value"], self.data.item_pressed["height_type"]))

        if self.data.item_pressed["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.item_pressed["font_family"]))

        if self.data.item_pressed["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.item_pressed["font_size"]))

        if self.data.item_pressed["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.item_pressed["font_weight"]))

        if self.data.item_pressed["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.item_pressed["font_style"]))

        if self.data.item_pressed["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.item_pressed["line_height"]))

        if self.data.item_pressed["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.item_pressed["text_align"]))

        if self.data.item_pressed["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.item_pressed["text_decoration"]))

        if self.data.item_pressed["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.item_pressed["text_transform"]))

        if self.data.item_pressed["background"] != "":
            f.write("\n   background: {};".format(self.data.item_pressed["background"]))

        if self.data.item_pressed["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.item_pressed["background_image"]))

        if self.data.item_pressed["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.item_pressed["background_color"]))

        if self.data.item_pressed["border"] != "":
            f.write("\n   border: {};".format(self.data.item_pressed["border"]))

        if self.data.item_pressed["border_width_value"] != 0 and self.data.item_pressed["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.item_pressed["border_width_value"], self.data.item_pressed["border_width_type"]))

        if self.data.item_pressed["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.item_pressed["border_style"]))

        if self.data.item_pressed["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.item_pressed["border_color"]))

        if self.data.item_pressed["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.item_pressed["border_top"]))

        if self.data.item_pressed["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.item_pressed["border_right"]))

        if self.data.item_pressed["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.item_pressed["border_bottom"]))

        if self.data.item_pressed["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.item_pressed["border_left"]))

        if self.data.item_pressed["border_radius"] != 0 and self.data.item_pressed["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.item_pressed["border_radius"]))

        if self.data.item_pressed["padding_top_value"] != 0 and self.data.item_pressed["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.item_pressed["padding_top_value"], self.data.item_pressed["padding_top_type"]))

        if self.data.item_pressed["padding_right_value"] != 0 and self.data.item_pressed["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.item_pressed["padding_right_value"], self.data.item_pressed["padding_right_type"]))

        if self.data.item_pressed["padding_bottom_value"] != 0 and self.data.item_pressed["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.item_pressed["padding_bottom_value"], self.data.item_pressed["padding_bottom_type"]))

        if self.data.item_pressed["padding_left_value"] != 0 and self.data.item_pressed["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.item_pressed["padding_left_value"], self.data.item_pressed["padding_left_type"]))


        if self.data.item_pressed["margin_top_value"] != 0 and self.data.item_pressed["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.item_pressed["margin_top_value"], self.data.item_pressed["margin_top_type"]))

        if self.data.item_pressed["margin_right_value"] != 0 and self.data.item_pressed["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.item_pressed["margin_right_value"], self.data.item_pressed["margin_right_type"]))

        if self.data.item_pressed["margin_bottom_value"] != 0 and self.data.item_pressed["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.item_pressed["margin_bottom_value"], self.data.item_pressed["margin_bottom_type"]))

        if self.data.item_pressed["margin_left_value"] != 0 and self.data.item_pressed["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.item_pressed["margin_left_value"], self.data.item_pressed["margin_left_type"]))


        f.write("\n}")




        f.write("\n")



        f.write("QMenu" + " {")

        if self.data.me["color"] != "":
            f.write("\n   color: {};".format(self.data.me["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.me["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.me["outline"]))

        if self.data.me["width_value"] != 0 and self.data.me["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.me["width_value"], self.data.me["width_type"]))

        if self.data.me["height_value"] != 0 and self.data.me["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.me["height_value"], self.data.me["height_type"]))

        if self.data.me["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.me["font_family"]))

        if self.data.me["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.me["font_size"]))

        if self.data.me["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.me["font_weight"]))

        if self.data.me["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.me["font_style"]))

        if self.data.me["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.me["line_height"]))

        if self.data.me["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.me["text_align"]))

        if self.data.me["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.me["text_decoration"]))

        if self.data.me["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.me["text_transform"]))

        if self.data.me["background"] != "":
            f.write("\n   background: {};".format(self.data.me["background"]))

        if self.data.me["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.me["background_image"]))

        if self.data.me["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.me["background_color"]))

        if self.data.me["border"] != "":
            f.write("\n   border: {};".format(self.data.me["border"]))

        if self.data.me["border_width_value"] != 0 and self.data.me["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.me["border_width_value"], self.data.me["border_width_type"]))

        if self.data.me["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.me["border_style"]))

        if self.data.me["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.me["border_color"]))

        if self.data.me["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.me["border_top"]))

        if self.data.me["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.me["border_right"]))

        if self.data.me["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.me["border_bottom"]))

        if self.data.me["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.me["border_left"]))

        if self.data.me["border_radius"] != 0 and self.data.me["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.me["border_radius"]))

        if self.data.me["padding_top_value"] != 0 and self.data.me["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.me["padding_top_value"], self.data.me["padding_top_type"]))

        if self.data.me["padding_right_value"] != 0 and self.data.me["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.me["padding_right_value"], self.data.me["padding_right_type"]))

        if self.data.me["padding_bottom_value"] != 0 and self.data.me["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.me["padding_bottom_value"], self.data.me["padding_bottom_type"]))

        if self.data.me["padding_left_value"] != 0 and self.data.me["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.me["padding_left_value"], self.data.me["padding_left_type"]))


        if self.data.me["margin_top_value"] != 0 and self.data.me["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.me["margin_top_value"], self.data.me["margin_top_type"]))

        if self.data.me["margin_right_value"] != 0 and self.data.me["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.me["margin_right_value"], self.data.me["margin_right_type"]))

        if self.data.me["margin_bottom_value"] != 0 and self.data.me["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.me["margin_bottom_value"], self.data.me["margin_bottom_type"]))

        if self.data.me["margin_left_value"] != 0 and self.data.me["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.me["margin_left_value"], self.data.me["margin_left_type"]))

        f.write("\n}")



        f.write("\n")




        f.write("QMenu" + ":hover {")

        if self.data.hover["color"] != "":
            f.write("\n   color: {};".format(self.data.hover["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.hover["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.hover["outline"]))

        if self.data.hover["width_value"] != 0 and self.data.hover["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.hover["width_value"], self.data.hover["width_type"]))

        if self.data.hover["height_value"] != 0 and self.data.hover["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.hover["height_value"], self.data.hover["height_type"]))

        if self.data.hover["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.hover["font_family"]))

        if self.data.hover["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.hover["font_size"]))

        if self.data.hover["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.hover["font_weight"]))

        if self.data.hover["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.hover["font_style"]))

        if self.data.hover["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.hover["line_height"]))

        if self.data.hover["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.hover["text_align"]))

        if self.data.hover["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.hover["text_decoration"]))

        if self.data.hover["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.hover["text_transform"]))

        if self.data.hover["background"] != "":
            f.write("\n   background: {};".format(self.data.hover["background"]))

        if self.data.hover["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.hover["background_image"]))

        if self.data.hover["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.hover["background_color"]))

        if self.data.hover["border"] != "":
            f.write("\n   border: {};".format(self.data.hover["border"]))

        if self.data.hover["border_width_value"] != 0 and self.data.hover["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.hover["border_width_value"], self.data.hover["border_width_type"]))

        if self.data.hover["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.hover["border_style"]))

        if self.data.hover["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.hover["border_color"]))

        if self.data.hover["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.hover["border_top"]))

        if self.data.hover["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.hover["border_right"]))

        if self.data.hover["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.hover["border_bottom"]))

        if self.data.hover["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.hover["border_left"]))

        if self.data.hover["border_radius"] != 0 and self.data.hover["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.hover["border_radius"]))

        if self.data.hover["padding_top_value"] != 0 and self.data.hover["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.hover["padding_top_value"], self.data.hover["padding_top_type"]))

        if self.data.hover["padding_right_value"] != 0 and self.data.hover["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.hover["padding_right_value"], self.data.hover["padding_right_type"]))

        if self.data.hover["padding_bottom_value"] != 0 and self.data.hover["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.hover["padding_bottom_value"], self.data.hover["padding_bottom_type"]))

        if self.data.hover["padding_left_value"] != 0 and self.data.hover["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.hover["padding_left_value"], self.data.hover["padding_left_type"]))


        if self.data.hover["margin_top_value"] != 0 and self.data.hover["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.hover["margin_top_value"], self.data.hover["margin_top_type"]))

        if self.data.hover["margin_right_value"] != 0 and self.data.hover["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.hover["margin_right_value"], self.data.hover["margin_right_type"]))

        if self.data.hover["margin_bottom_value"] != 0 and self.data.hover["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.hover["margin_bottom_value"], self.data.hover["margin_bottom_type"]))

        if self.data.hover["margin_left_value"] != 0 and self.data.hover["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.hover["margin_left_value"], self.data.hover["margin_left_type"]))


        f.write("\n}")



        f.write("\n")




        f.write("QMenu" + "::item {")

        if self.data.item["color"] != "":
            f.write("\n   color: {};".format(self.data.item["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.item["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.item["outline"]))

        if self.data.item["width_value"] != 0 and self.data.item["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.item["width_value"], self.data.item["width_type"]))

        if self.data.item["height_value"] != 0 and self.data.item["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.item["height_value"], self.data.item["height_type"]))

        if self.data.item["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.item["font_family"]))

        if self.data.item["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.item["font_size"]))

        if self.data.item["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.item["font_weight"]))

        if self.data.item["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.item["font_style"]))

        if self.data.item["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.item["line_height"]))

        if self.data.item["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.item["text_align"]))

        if self.data.item["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.item["text_decoration"]))

        if self.data.item["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.item["text_transform"]))

        if self.data.item["background"] != "":
            f.write("\n   background: {};".format(self.data.item["background"]))

        if self.data.item["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.item["background_image"]))

        if self.data.item["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.item["background_color"]))

        if self.data.item["border"] != "":
            f.write("\n   border: {};".format(self.data.item["border"]))

        if self.data.item["border_width_value"] != 0 and self.data.item["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.item["border_width_value"], self.data.item["border_width_type"]))

        if self.data.item["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.item["border_style"]))

        if self.data.item["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.item["border_color"]))

        if self.data.item["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.item["border_top"]))

        if self.data.item["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.item["border_right"]))

        if self.data.item["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.item["border_bottom"]))

        if self.data.item["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.item["border_left"]))

        if self.data.item["border_radius"] != 0 and self.data.item["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.item["border_radius"]))

        if self.data.item["padding_top_value"] != 0 and self.data.item["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.item["padding_top_value"], self.data.item["padding_top_type"]))

        if self.data.item["padding_right_value"] != 0 and self.data.item["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.item["padding_right_value"], self.data.item["padding_right_type"]))

        if self.data.item["padding_bottom_value"] != 0 and self.data.item["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.item["padding_bottom_value"], self.data.item["padding_bottom_type"]))

        if self.data.item["padding_left_value"] != 0 and self.data.item["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.item["padding_left_value"], self.data.item["padding_left_type"]))


        if self.data.item["margin_top_value"] != 0 and self.data.item["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.item["margin_top_value"], self.data.item["margin_top_type"]))

        if self.data.item["margin_right_value"] != 0 and self.data.item["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.item["margin_right_value"], self.data.item["margin_right_type"]))

        if self.data.item["margin_bottom_value"] != 0 and self.data.item["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.item["margin_bottom_value"], self.data.item["margin_bottom_type"]))

        if self.data.item["margin_left_value"] != 0 and self.data.item["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.item["margin_left_value"], self.data.item["margin_left_type"]))


        f.write("\n}")





        f.write("\n")




        f.write("QMenu" + "::seperator {")

        if self.data.seperator["color"] != "":
            f.write("\n   color: {};".format(self.data.seperator["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.seperator["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.seperator["outline"]))

        if self.data.seperator["width_value"] != 0 and self.data.seperator["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.seperator["width_value"], self.data.seperator["width_type"]))

        if self.data.seperator["height_value"] != 0 and self.data.seperator["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.seperator["height_value"], self.data.seperator["height_type"]))

        if self.data.seperator["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.seperator["font_family"]))

        if self.data.seperator["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.seperator["font_size"]))

        if self.data.seperator["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.seperator["font_weight"]))

        if self.data.seperator["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.seperator["font_style"]))

        if self.data.seperator["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.seperator["line_height"]))

        if self.data.seperator["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.seperator["text_align"]))

        if self.data.seperator["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.seperator["text_decoration"]))

        if self.data.seperator["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.seperator["text_transform"]))

        if self.data.seperator["background"] != "":
            f.write("\n   background: {};".format(self.data.seperator["background"]))

        if self.data.seperator["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.seperator["background_image"]))

        if self.data.seperator["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.seperator["background_color"]))

        if self.data.seperator["border"] != "":
            f.write("\n   border: {};".format(self.data.seperator["border"]))

        if self.data.seperator["border_width_value"] != 0 and self.data.seperator["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.seperator["border_width_value"], self.data.seperator["border_width_type"]))

        if self.data.seperator["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.seperator["border_style"]))

        if self.data.seperator["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.seperator["border_color"]))

        if self.data.seperator["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.seperator["border_top"]))

        if self.data.seperator["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.seperator["border_right"]))

        if self.data.seperator["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.seperator["border_bottom"]))

        if self.data.seperator["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.seperator["border_left"]))

        if self.data.seperator["border_radius"] != 0 and self.data.seperator["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.seperator["border_radius"]))

        if self.data.seperator["padding_top_value"] != 0 and self.data.seperator["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.seperator["padding_top_value"], self.data.seperator["padding_top_type"]))

        if self.data.seperator["padding_right_value"] != 0 and self.data.seperator["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.seperator["padding_right_value"], self.data.seperator["padding_right_type"]))

        if self.data.seperator["padding_bottom_value"] != 0 and self.data.seperator["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.seperator["padding_bottom_value"], self.data.seperator["padding_bottom_type"]))

        if self.data.seperator["padding_left_value"] != 0 and self.data.seperator["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.seperator["padding_left_value"], self.data.seperator["padding_left_type"]))


        if self.data.seperator["margin_top_value"] != 0 and self.data.seperator["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.seperator["margin_top_value"], self.data.seperator["margin_top_type"]))

        if self.data.seperator["margin_right_value"] != 0 and self.data.seperator["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.seperator["margin_right_value"], self.data.seperator["margin_right_type"]))

        if self.data.seperator["margin_bottom_value"] != 0 and self.data.seperator["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.seperator["margin_bottom_value"], self.data.seperator["margin_bottom_type"]))

        if self.data.seperator["margin_left_value"] != 0 and self.data.seperator["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.seperator["margin_left_value"], self.data.seperator["margin_left_type"]))


        f.write("\n}")





        f.write("\n")




        f.write("QMenu" + "::item:selected {")

        if self.data.item_selected["color"] != "":
            f.write("\n   color: {};".format(self.data.item_selected["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.item_selected["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.item_selected["outline"]))

        if self.data.item_selected["width_value"] != 0 and self.data.item_selected["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.item_selected["width_value"], self.data.item_selected["width_type"]))

        if self.data.item_selected["height_value"] != 0 and self.data.item_selected["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.item_selected["height_value"], self.data.item_selected["height_type"]))

        if self.data.item_selected["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.item_selected["font_family"]))

        if self.data.item_selected["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.item_selected["font_size"]))

        if self.data.item_selected["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.item_selected["font_weight"]))

        if self.data.item_selected["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.item_selected["font_style"]))

        if self.data.item_selected["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.item_selected["line_height"]))

        if self.data.item_selected["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.item_selected["text_align"]))

        if self.data.item_selected["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.item_selected["text_decoration"]))

        if self.data.item_selected["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.item_selected["text_transform"]))

        if self.data.item_selected["background"] != "":
            f.write("\n   background: {};".format(self.data.item_selected["background"]))

        if self.data.item_selected["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.item_selected["background_image"]))

        if self.data.item_selected["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.item_selected["background_color"]))

        if self.data.item_selected["border"] != "":
            f.write("\n   border: {};".format(self.data.item_selected["border"]))

        if self.data.item_selected["border_width_value"] != 0 and self.data.item_selected["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.item_selected["border_width_value"], self.data.item_selected["border_width_type"]))

        if self.data.item_selected["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.item_selected["border_style"]))

        if self.data.item_selected["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.item_selected["border_color"]))

        if self.data.item_selected["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.item_selected["border_top"]))

        if self.data.item_selected["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.item_selected["border_right"]))

        if self.data.item_selected["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.item_selected["border_bottom"]))

        if self.data.item_selected["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.item_selected["border_left"]))

        if self.data.item_selected["border_radius"] != 0 and self.data.item_selected["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.item_selected["border_radius"]))

        if self.data.item_selected["padding_top_value"] != 0 and self.data.item_selected["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.item_selected["padding_top_value"], self.data.item_selected["padding_top_type"]))

        if self.data.item_selected["padding_right_value"] != 0 and self.data.item_selected["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.item_selected["padding_right_value"], self.data.item_selected["padding_right_type"]))

        if self.data.item_selected["padding_bottom_value"] != 0 and self.data.item_selected["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.item_selected["padding_bottom_value"], self.data.item_selected["padding_bottom_type"]))

        if self.data.item_selected["padding_left_value"] != 0 and self.data.item_selected["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.item_selected["padding_left_value"], self.data.item_selected["padding_left_type"]))


        if self.data.item_selected["margin_top_value"] != 0 and self.data.item_selected["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.item_selected["margin_top_value"], self.data.item_selected["margin_top_type"]))

        if self.data.item_selected["margin_right_value"] != 0 and self.data.item_selected["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.item_selected["margin_right_value"], self.data.item_selected["margin_right_type"]))

        if self.data.item_selected["margin_bottom_value"] != 0 and self.data.item_selected["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.item_selected["margin_bottom_value"], self.data.item_selected["margin_bottom_type"]))

        if self.data.item_selected["margin_left_value"] != 0 and self.data.item_selected["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.item_selected["margin_left_value"], self.data.item_selected["margin_left_type"]))


        f.write("\n}")



        f.write("\n")




        f.write("QMenu" + "::indicator {")

        if self.data.indicator["color"] != "":
            f.write("\n   color: {};".format(self.data.indicator["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.indicator["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.indicator["outline"]))

        if self.data.indicator["width_value"] != 0 and self.data.indicator["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.indicator["width_value"], self.data.indicator["width_type"]))

        if self.data.indicator["height_value"] != 0 and self.data.indicator["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.indicator["height_value"], self.data.indicator["height_type"]))

        if self.data.indicator["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.indicator["font_family"]))

        if self.data.indicator["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.indicator["font_size"]))

        if self.data.indicator["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.indicator["font_weight"]))

        if self.data.indicator["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.indicator["font_style"]))

        if self.data.indicator["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.indicator["line_height"]))

        if self.data.indicator["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.indicator["text_align"]))

        if self.data.indicator["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.indicator["text_decoration"]))

        if self.data.indicator["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.indicator["text_transform"]))

        if self.data.indicator["background"] != "":
            f.write("\n   background: {};".format(self.data.indicator["background"]))

        if self.data.indicator["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.indicator["background_image"]))

        if self.data.indicator["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.indicator["background_color"]))

        if self.data.indicator["border"] != "":
            f.write("\n   border: {};".format(self.data.indicator["border"]))

        if self.data.indicator["border_width_value"] != 0 and self.data.indicator["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.indicator["border_width_value"], self.data.indicator["border_width_type"]))

        if self.data.indicator["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.indicator["border_style"]))

        if self.data.indicator["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.indicator["border_color"]))

        if self.data.indicator["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.indicator["border_top"]))

        if self.data.indicator["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.indicator["border_right"]))

        if self.data.indicator["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.indicator["border_bottom"]))

        if self.data.indicator["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.indicator["border_left"]))

        if self.data.indicator["border_radius"] != 0 and self.data.indicator["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.indicator["border_radius"]))

        if self.data.indicator["padding_top_value"] != 0 and self.data.indicator["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator["padding_top_value"], self.data.indicator["padding_top_type"]))

        if self.data.indicator["padding_right_value"] != 0 and self.data.indicator["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.indicator["padding_right_value"], self.data.indicator["padding_right_type"]))

        if self.data.indicator["padding_bottom_value"] != 0 and self.data.indicator["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.indicator["padding_bottom_value"], self.data.indicator["padding_bottom_type"]))

        if self.data.indicator["padding_left_value"] != 0 and self.data.indicator["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.indicator["padding_left_value"], self.data.indicator["padding_left_type"]))


        if self.data.indicator["margin_top_value"] != 0 and self.data.indicator["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator["margin_top_value"], self.data.indicator["margin_top_type"]))

        if self.data.indicator["margin_right_value"] != 0 and self.data.indicator["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.indicator["margin_right_value"], self.data.indicator["margin_right_type"]))

        if self.data.indicator["margin_bottom_value"] != 0 and self.data.indicator["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.indicator["margin_bottom_value"], self.data.indicator["margin_bottom_type"]))

        if self.data.indicator["margin_left_value"] != 0 and self.data.indicator["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.indicator["margin_left_value"], self.data.indicator["margin_left_type"]))


        f.write("\n}")







        f.write("\n")




        f.write("QMenu" + "::indicator:exclusive:checked {")

        if self.data.indicator_exclusive_checked["color"] != "":
            f.write("\n   color: {};".format(self.data.indicator_exclusive_checked["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.indicator_exclusive_checked["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.indicator_exclusive_checked["outline"]))

        if self.data.indicator_exclusive_checked["width_value"] != 0 and self.data.indicator_exclusive_checked["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.indicator_exclusive_checked["width_value"], self.data.indicator_exclusive_checked["width_type"]))

        if self.data.indicator_exclusive_checked["height_value"] != 0 and self.data.indicator_exclusive_checked["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.indicator_exclusive_checked["height_value"], self.data.indicator_exclusive_checked["height_type"]))

        if self.data.indicator_exclusive_checked["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.indicator_exclusive_checked["font_family"]))

        if self.data.indicator_exclusive_checked["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.indicator_exclusive_checked["font_size"]))

        if self.data.indicator_exclusive_checked["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.indicator_exclusive_checked["font_weight"]))

        if self.data.indicator_exclusive_checked["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.indicator_exclusive_checked["font_style"]))

        if self.data.indicator_exclusive_checked["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.indicator_exclusive_checked["line_height"]))

        if self.data.indicator_exclusive_checked["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.indicator_exclusive_checked["text_align"]))

        if self.data.indicator_exclusive_checked["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.indicator_exclusive_checked["text_decoration"]))

        if self.data.indicator_exclusive_checked["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.indicator_exclusive_checked["text_transform"]))

        if self.data.indicator_exclusive_checked["background"] != "":
            f.write("\n   background: {};".format(self.data.indicator_exclusive_checked["background"]))

        if self.data.indicator_exclusive_checked["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.indicator_exclusive_checked["background_image"]))

        if self.data.indicator_exclusive_checked["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.indicator_exclusive_checked["background_color"]))

        if self.data.indicator_exclusive_checked["border"] != "":
            f.write("\n   border: {};".format(self.data.indicator_exclusive_checked["border"]))

        if self.data.indicator_exclusive_checked["border_width_value"] != 0 and self.data.indicator_exclusive_checked["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.indicator_exclusive_checked["border_width_value"], self.data.indicator_exclusive_checked["border_width_type"]))

        if self.data.indicator_exclusive_checked["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.indicator_exclusive_checked["border_style"]))

        if self.data.indicator_exclusive_checked["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.indicator_exclusive_checked["border_color"]))

        if self.data.indicator_exclusive_checked["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.indicator_exclusive_checked["border_top"]))

        if self.data.indicator_exclusive_checked["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.indicator_exclusive_checked["border_right"]))

        if self.data.indicator_exclusive_checked["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.indicator_exclusive_checked["border_bottom"]))

        if self.data.indicator_exclusive_checked["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.indicator_exclusive_checked["border_left"]))

        if self.data.indicator_exclusive_checked["border_radius"] != 0 and self.data.indicator_exclusive_checked["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.indicator_exclusive_checked["border_radius"]))

        if self.data.indicator_exclusive_checked["padding_top_value"] != 0 and self.data.indicator_exclusive_checked["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_exclusive_checked["padding_top_value"], self.data.indicator_exclusive_checked["padding_top_type"]))

        if self.data.indicator_exclusive_checked["padding_right_value"] != 0 and self.data.indicator_exclusive_checked["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.indicator_exclusive_checked["padding_right_value"], self.data.indicator_exclusive_checked["padding_right_type"]))

        if self.data.indicator_exclusive_checked["padding_bottom_value"] != 0 and self.data.indicator_exclusive_checked["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.indicator_exclusive_checked["padding_bottom_value"], self.data.indicator_exclusive_checked["padding_bottom_type"]))

        if self.data.indicator_exclusive_checked["padding_left_value"] != 0 and self.data.indicator_exclusive_checked["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.indicator_exclusive_checked["padding_left_value"], self.data.indicator_exclusive_checked["padding_left_type"]))


        if self.data.indicator_exclusive_checked["margin_top_value"] != 0 and self.data.indicator_exclusive_checked["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_exclusive_checked["margin_top_value"], self.data.indicator_exclusive_checked["margin_top_type"]))

        if self.data.indicator_exclusive_checked["margin_right_value"] != 0 and self.data.indicator_exclusive_checked["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.indicator_exclusive_checked["margin_right_value"], self.data.indicator_exclusive_checked["margin_right_type"]))

        if self.data.indicator_exclusive_checked["margin_bottom_value"] != 0 and self.data.indicator_exclusive_checked["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.indicator_exclusive_checked["margin_bottom_value"], self.data.indicator_exclusive_checked["margin_bottom_type"]))

        if self.data.indicator_exclusive_checked["margin_left_value"] != 0 and self.data.indicator_exclusive_checked["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.indicator_exclusive_checked["margin_left_value"], self.data.indicator_exclusive_checked["margin_left_type"]))


        f.write("\n}")



        f.write("\n")




        f.write("QMenu" + "::indicator:exclusive:checked:selected {")

        if self.data.indicator_exclusive_checked_selected["color"] != "":
            f.write("\n   color: {};".format(self.data.indicator_exclusive_checked_selected["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.indicator_exclusive_checked_selected["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.indicator_exclusive_checked_selected["outline"]))

        if self.data.indicator_exclusive_checked_selected["width_value"] != 0 and self.data.indicator_exclusive_checked_selected["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.indicator_exclusive_checked_selected["width_value"], self.data.indicator_exclusive_checked_selected["width_type"]))

        if self.data.indicator_exclusive_checked_selected["height_value"] != 0 and self.data.indicator_exclusive_checked_selected["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.indicator_exclusive_checked_selected["height_value"], self.data.indicator_exclusive_checked_selected["height_type"]))

        if self.data.indicator_exclusive_checked_selected["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.indicator_exclusive_checked_selected["font_family"]))

        if self.data.indicator_exclusive_checked_selected["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.indicator_exclusive_checked_selected["font_size"]))

        if self.data.indicator_exclusive_checked_selected["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.indicator_exclusive_checked_selected["font_weight"]))

        if self.data.indicator_exclusive_checked_selected["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.indicator_exclusive_checked_selected["font_style"]))

        if self.data.indicator_exclusive_checked_selected["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.indicator_exclusive_checked_selected["line_height"]))

        if self.data.indicator_exclusive_checked_selected["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.indicator_exclusive_checked_selected["text_align"]))

        if self.data.indicator_exclusive_checked_selected["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.indicator_exclusive_checked_selected["text_decoration"]))

        if self.data.indicator_exclusive_checked_selected["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.indicator_exclusive_checked_selected["text_transform"]))

        if self.data.indicator_exclusive_checked_selected["background"] != "":
            f.write("\n   background: {};".format(self.data.indicator_exclusive_checked_selected["background"]))

        if self.data.indicator_exclusive_checked_selected["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.indicator_exclusive_checked_selected["background_image"]))

        if self.data.indicator_exclusive_checked_selected["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.indicator_exclusive_checked_selected["background_color"]))

        if self.data.indicator_exclusive_checked_selected["border"] != "":
            f.write("\n   border: {};".format(self.data.indicator_exclusive_checked_selected["border"]))

        if self.data.indicator_exclusive_checked_selected["border_width_value"] != 0 and self.data.indicator_exclusive_checked_selected["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.indicator_exclusive_checked_selected["border_width_value"], self.data.indicator_exclusive_checked_selected["border_width_type"]))

        if self.data.indicator_exclusive_checked_selected["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.indicator_exclusive_checked_selected["border_style"]))

        if self.data.indicator_exclusive_checked_selected["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.indicator_exclusive_checked_selected["border_color"]))

        if self.data.indicator_exclusive_checked_selected["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.indicator_exclusive_checked_selected["border_top"]))

        if self.data.indicator_exclusive_checked_selected["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.indicator_exclusive_checked_selected["border_right"]))

        if self.data.indicator_exclusive_checked_selected["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.indicator_exclusive_checked_selected["border_bottom"]))

        if self.data.indicator_exclusive_checked_selected["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.indicator_exclusive_checked_selected["border_left"]))

        if self.data.indicator_exclusive_checked_selected["border_radius"] != 0 and self.data.indicator_exclusive_checked_selected["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.indicator_exclusive_checked_selected["border_radius"]))

        if self.data.indicator_exclusive_checked_selected["padding_top_value"] != 0 and self.data.indicator_exclusive_checked_selected["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_exclusive_checked_selected["padding_top_value"], self.data.indicator_exclusive_checked_selected["padding_top_type"]))

        if self.data.indicator_exclusive_checked_selected["padding_right_value"] != 0 and self.data.indicator_exclusive_checked_selected["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.indicator_exclusive_checked_selected["padding_right_value"], self.data.indicator_exclusive_checked_selected["padding_right_type"]))

        if self.data.indicator_exclusive_checked_selected["padding_bottom_value"] != 0 and self.data.indicator_exclusive_checked_selected["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.indicator_exclusive_checked_selected["padding_bottom_value"], self.data.indicator_exclusive_checked_selected["padding_bottom_type"]))

        if self.data.indicator_exclusive_checked_selected["padding_left_value"] != 0 and self.data.indicator_exclusive_checked_selected["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.indicator_exclusive_checked_selected["padding_left_value"], self.data.indicator_exclusive_checked_selected["padding_left_type"]))


        if self.data.indicator_exclusive_checked_selected["margin_top_value"] != 0 and self.data.indicator_exclusive_checked_selected["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_exclusive_checked_selected["margin_top_value"], self.data.indicator_exclusive_checked_selected["margin_top_type"]))

        if self.data.indicator_exclusive_checked_selected["margin_right_value"] != 0 and self.data.indicator_exclusive_checked_selected["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.indicator_exclusive_checked_selected["margin_right_value"], self.data.indicator_exclusive_checked_selected["margin_right_type"]))

        if self.data.indicator_exclusive_checked_selected["margin_bottom_value"] != 0 and self.data.indicator_exclusive_checked_selected["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.indicator_exclusive_checked_selected["margin_bottom_value"], self.data.indicator_exclusive_checked_selected["margin_bottom_type"]))

        if self.data.indicator_exclusive_checked_selected["margin_left_value"] != 0 and self.data.indicator_exclusive_checked_selected["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.indicator_exclusive_checked_selected["margin_left_value"], self.data.indicator_exclusive_checked_selected["margin_left_type"]))


        f.write("\n}")




        f.write("\n")




        f.write("QMenu" + "::indicator:exclusive:unchecked {")

        if self.data.indicator_exclusive_unchecked["color"] != "":
            f.write("\n   color: {};".format(self.data.indicator_exclusive_unchecked["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.indicator_exclusive_unchecked["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.indicator_exclusive_unchecked["outline"]))

        if self.data.indicator_exclusive_unchecked["width_value"] != 0 and self.data.indicator_exclusive_unchecked["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.indicator_exclusive_unchecked["width_value"], self.data.indicator_exclusive_unchecked["width_type"]))

        if self.data.indicator_exclusive_unchecked["height_value"] != 0 and self.data.indicator_exclusive_unchecked["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.indicator_exclusive_unchecked["height_value"], self.data.indicator_exclusive_unchecked["height_type"]))

        if self.data.indicator_exclusive_unchecked["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.indicator_exclusive_unchecked["font_family"]))

        if self.data.indicator_exclusive_unchecked["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.indicator_exclusive_unchecked["font_size"]))

        if self.data.indicator_exclusive_unchecked["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.indicator_exclusive_unchecked["font_weight"]))

        if self.data.indicator_exclusive_unchecked["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.indicator_exclusive_unchecked["font_style"]))

        if self.data.indicator_exclusive_unchecked["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.indicator_exclusive_unchecked["line_height"]))

        if self.data.indicator_exclusive_unchecked["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.indicator_exclusive_unchecked["text_align"]))

        if self.data.indicator_exclusive_unchecked["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.indicator_exclusive_unchecked["text_decoration"]))

        if self.data.indicator_exclusive_unchecked["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.indicator_exclusive_unchecked["text_transform"]))

        if self.data.indicator_exclusive_unchecked["background"] != "":
            f.write("\n   background: {};".format(self.data.indicator_exclusive_unchecked["background"]))

        if self.data.indicator_exclusive_unchecked["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.indicator_exclusive_unchecked["background_image"]))

        if self.data.indicator_exclusive_unchecked["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.indicator_exclusive_unchecked["background_color"]))

        if self.data.indicator_exclusive_unchecked["border"] != "":
            f.write("\n   border: {};".format(self.data.indicator_exclusive_unchecked["border"]))

        if self.data.indicator_exclusive_unchecked["border_width_value"] != 0 and self.data.indicator_exclusive_unchecked["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.indicator_exclusive_unchecked["border_width_value"], self.data.indicator_exclusive_unchecked["border_width_type"]))

        if self.data.indicator_exclusive_unchecked["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.indicator_exclusive_unchecked["border_style"]))

        if self.data.indicator_exclusive_unchecked["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.indicator_exclusive_unchecked["border_color"]))

        if self.data.indicator_exclusive_unchecked["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.indicator_exclusive_unchecked["border_top"]))

        if self.data.indicator_exclusive_unchecked["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.indicator_exclusive_unchecked["border_right"]))

        if self.data.indicator_exclusive_unchecked["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.indicator_exclusive_unchecked["border_bottom"]))

        if self.data.indicator_exclusive_unchecked["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.indicator_exclusive_unchecked["border_left"]))

        if self.data.indicator_exclusive_unchecked["border_radius"] != 0 and self.data.indicator_exclusive_unchecked["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.indicator_exclusive_unchecked["border_radius"]))

        if self.data.indicator_exclusive_unchecked["padding_top_value"] != 0 and self.data.indicator_exclusive_unchecked["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_exclusive_unchecked["padding_top_value"], self.data.indicator_exclusive_unchecked["padding_top_type"]))

        if self.data.indicator_exclusive_unchecked["padding_right_value"] != 0 and self.data.indicator_exclusive_unchecked["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.indicator_exclusive_unchecked["padding_right_value"], self.data.indicator_exclusive_unchecked["padding_right_type"]))

        if self.data.indicator_exclusive_unchecked["padding_bottom_value"] != 0 and self.data.indicator_exclusive_unchecked["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.indicator_exclusive_unchecked["padding_bottom_value"], self.data.indicator_exclusive_unchecked["padding_bottom_type"]))

        if self.data.indicator_exclusive_unchecked["padding_left_value"] != 0 and self.data.indicator_exclusive_unchecked["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.indicator_exclusive_unchecked["padding_left_value"], self.data.indicator_exclusive_unchecked["padding_left_type"]))


        if self.data.indicator_exclusive_unchecked["margin_top_value"] != 0 and self.data.indicator_exclusive_unchecked["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_exclusive_unchecked["margin_top_value"], self.data.indicator_exclusive_unchecked["margin_top_type"]))

        if self.data.indicator_exclusive_unchecked["margin_right_value"] != 0 and self.data.indicator_exclusive_unchecked["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.indicator_exclusive_unchecked["margin_right_value"], self.data.indicator_exclusive_unchecked["margin_right_type"]))

        if self.data.indicator_exclusive_unchecked["margin_bottom_value"] != 0 and self.data.indicator_exclusive_unchecked["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.indicator_exclusive_unchecked["margin_bottom_value"], self.data.indicator_exclusive_unchecked["margin_bottom_type"]))

        if self.data.indicator_exclusive_unchecked["margin_left_value"] != 0 and self.data.indicator_exclusive_unchecked["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.indicator_exclusive_unchecked["margin_left_value"], self.data.indicator_exclusive_unchecked["margin_left_type"]))


        f.write("\n}")





        f.write("\n")




        f.write("QMenu" + "::indicator:exclusive:unchecked:selected {")

        if self.data.indicator_exclusive_unchecked_selected["color"] != "":
            f.write("\n   color: {};".format(self.data.indicator_exclusive_unchecked_selected["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.indicator_exclusive_unchecked_selected["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.indicator_exclusive_unchecked_selected["outline"]))

        if self.data.indicator_exclusive_unchecked_selected["width_value"] != 0 and self.data.indicator_exclusive_unchecked_selected["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.indicator_exclusive_unchecked_selected["width_value"], self.data.indicator_exclusive_unchecked_selected["width_type"]))

        if self.data.indicator_exclusive_unchecked_selected["height_value"] != 0 and self.data.indicator_exclusive_unchecked_selected["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.indicator_exclusive_unchecked_selected["height_value"], self.data.indicator_exclusive_unchecked_selected["height_type"]))

        if self.data.indicator_exclusive_unchecked_selected["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.indicator_exclusive_unchecked_selected["font_family"]))

        if self.data.indicator_exclusive_unchecked_selected["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.indicator_exclusive_unchecked_selected["font_size"]))

        if self.data.indicator_exclusive_unchecked_selected["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.indicator_exclusive_unchecked_selected["font_weight"]))

        if self.data.indicator_exclusive_unchecked_selected["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.indicator_exclusive_unchecked_selected["font_style"]))

        if self.data.indicator_exclusive_unchecked_selected["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.indicator_exclusive_unchecked_selected["line_height"]))

        if self.data.indicator_exclusive_unchecked_selected["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.indicator_exclusive_unchecked_selected["text_align"]))

        if self.data.indicator_exclusive_unchecked_selected["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.indicator_exclusive_unchecked_selected["text_decoration"]))

        if self.data.indicator_exclusive_unchecked_selected["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.indicator_exclusive_unchecked_selected["text_transform"]))

        if self.data.indicator_exclusive_unchecked_selected["background"] != "":
            f.write("\n   background: {};".format(self.data.indicator_exclusive_unchecked_selected["background"]))

        if self.data.indicator_exclusive_unchecked_selected["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.indicator_exclusive_unchecked_selected["background_image"]))

        if self.data.indicator_exclusive_unchecked_selected["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.indicator_exclusive_unchecked_selected["background_color"]))

        if self.data.indicator_exclusive_unchecked_selected["border"] != "":
            f.write("\n   border: {};".format(self.data.indicator_exclusive_unchecked_selected["border"]))

        if self.data.indicator_exclusive_unchecked_selected["border_width_value"] != 0 and self.data.indicator_exclusive_unchecked_selected["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.indicator_exclusive_unchecked_selected["border_width_value"], self.data.indicator_exclusive_unchecked_selected["border_width_type"]))

        if self.data.indicator_exclusive_unchecked_selected["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.indicator_exclusive_unchecked_selected["border_style"]))

        if self.data.indicator_exclusive_unchecked_selected["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.indicator_exclusive_unchecked_selected["border_color"]))

        if self.data.indicator_exclusive_unchecked_selected["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.indicator_exclusive_unchecked_selected["border_top"]))

        if self.data.indicator_exclusive_unchecked_selected["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.indicator_exclusive_unchecked_selected["border_right"]))

        if self.data.indicator_exclusive_unchecked_selected["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.indicator_exclusive_unchecked_selected["border_bottom"]))

        if self.data.indicator_exclusive_unchecked_selected["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.indicator_exclusive_unchecked_selected["border_left"]))

        if self.data.indicator_exclusive_unchecked_selected["border_radius"] != 0 and self.data.indicator_exclusive_unchecked_selected["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.indicator_exclusive_unchecked_selected["border_radius"]))

        if self.data.indicator_exclusive_unchecked_selected["padding_top_value"] != 0 and self.data.indicator_exclusive_unchecked_selected["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_exclusive_unchecked_selected["padding_top_value"], self.data.indicator_exclusive_unchecked_selected["padding_top_type"]))

        if self.data.indicator_exclusive_unchecked_selected["padding_right_value"] != 0 and self.data.indicator_exclusive_unchecked_selected["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.indicator_exclusive_unchecked_selected["padding_right_value"], self.data.indicator_exclusive_unchecked_selected["padding_right_type"]))

        if self.data.indicator_exclusive_unchecked_selected["padding_bottom_value"] != 0 and self.data.indicator_exclusive_unchecked_selected["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.indicator_exclusive_unchecked_selected["padding_bottom_value"], self.data.indicator_exclusive_unchecked_selected["padding_bottom_type"]))

        if self.data.indicator_exclusive_unchecked_selected["padding_left_value"] != 0 and self.data.indicator_exclusive_unchecked_selected["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.indicator_exclusive_unchecked_selected["padding_left_value"], self.data.indicator_exclusive_unchecked_selected["padding_left_type"]))


        if self.data.indicator_exclusive_unchecked_selected["margin_top_value"] != 0 and self.data.indicator_exclusive_unchecked_selected["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_exclusive_unchecked_selected["margin_top_value"], self.data.indicator_exclusive_unchecked_selected["margin_top_type"]))

        if self.data.indicator_exclusive_unchecked_selected["margin_right_value"] != 0 and self.data.indicator_exclusive_unchecked_selected["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.indicator_exclusive_unchecked_selected["margin_right_value"], self.data.indicator_exclusive_unchecked_selected["margin_right_type"]))

        if self.data.indicator_exclusive_unchecked_selected["margin_bottom_value"] != 0 and self.data.indicator_exclusive_unchecked_selected["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.indicator_exclusive_unchecked_selected["margin_bottom_value"], self.data.indicator_exclusive_unchecked_selected["margin_bottom_type"]))

        if self.data.indicator_exclusive_unchecked_selected["margin_left_value"] != 0 and self.data.indicator_exclusive_unchecked_selected["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.indicator_exclusive_unchecked_selected["margin_left_value"], self.data.indicator_exclusive_unchecked_selected["margin_left_type"]))


        f.write("\n}")




        f.write("\n")




        f.write("QMenu" + "::indicator:non-exclusive:checked {")

        if self.data.indicator_non_exclusive_checked["color"] != "":
            f.write("\n   color: {};".format(self.data.indicator_non_exclusive_checked["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.indicator_non_exclusive_checked["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.indicator_non_exclusive_checked["outline"]))

        if self.data.indicator_non_exclusive_checked["width_value"] != 0 and self.data.indicator_non_exclusive_checked["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.indicator_non_exclusive_checked["width_value"], self.data.indicator_non_exclusive_checked["width_type"]))

        if self.data.indicator_non_exclusive_checked["height_value"] != 0 and self.data.indicator_non_exclusive_checked["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.indicator_non_exclusive_checked["height_value"], self.data.indicator_non_exclusive_checked["height_type"]))

        if self.data.indicator_non_exclusive_checked["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.indicator_non_exclusive_checked["font_family"]))

        if self.data.indicator_non_exclusive_checked["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.indicator_non_exclusive_checked["font_size"]))

        if self.data.indicator_non_exclusive_checked["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.indicator_non_exclusive_checked["font_weight"]))

        if self.data.indicator_non_exclusive_checked["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.indicator_non_exclusive_checked["font_style"]))

        if self.data.indicator_non_exclusive_checked["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.indicator_non_exclusive_checked["line_height"]))

        if self.data.indicator_non_exclusive_checked["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.indicator_non_exclusive_checked["text_align"]))

        if self.data.indicator_non_exclusive_checked["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.indicator_non_exclusive_checked["text_decoration"]))

        if self.data.indicator_non_exclusive_checked["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.indicator_non_exclusive_checked["text_transform"]))

        if self.data.indicator_non_exclusive_checked["background"] != "":
            f.write("\n   background: {};".format(self.data.indicator_non_exclusive_checked["background"]))

        if self.data.indicator_non_exclusive_checked["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.indicator_non_exclusive_checked["background_image"]))

        if self.data.indicator_non_exclusive_checked["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.indicator_non_exclusive_checked["background_color"]))

        if self.data.indicator_non_exclusive_checked["border"] != "":
            f.write("\n   border: {};".format(self.data.indicator_non_exclusive_checked["border"]))

        if self.data.indicator_non_exclusive_checked["border_width_value"] != 0 and self.data.indicator_non_exclusive_checked["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.indicator_non_exclusive_checked["border_width_value"], self.data.indicator_non_exclusive_checked["border_width_type"]))

        if self.data.indicator_non_exclusive_checked["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.indicator_non_exclusive_checked["border_style"]))

        if self.data.indicator_non_exclusive_checked["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.indicator_non_exclusive_checked["border_color"]))

        if self.data.indicator_non_exclusive_checked["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.indicator_non_exclusive_checked["border_top"]))

        if self.data.indicator_non_exclusive_checked["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.indicator_non_exclusive_checked["border_right"]))

        if self.data.indicator_non_exclusive_checked["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.indicator_non_exclusive_checked["border_bottom"]))

        if self.data.indicator_non_exclusive_checked["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.indicator_non_exclusive_checked["border_left"]))

        if self.data.indicator_non_exclusive_checked["border_radius"] != 0 and self.data.indicator_non_exclusive_checked["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.indicator_non_exclusive_checked["border_radius"]))

        if self.data.indicator_non_exclusive_checked["padding_top_value"] != 0 and self.data.indicator_non_exclusive_checked["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_non_exclusive_checked["padding_top_value"], self.data.indicator_non_exclusive_checked["padding_top_type"]))

        if self.data.indicator_non_exclusive_checked["padding_right_value"] != 0 and self.data.indicator_non_exclusive_checked["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.indicator_non_exclusive_checked["padding_right_value"], self.data.indicator_non_exclusive_checked["padding_right_type"]))

        if self.data.indicator_non_exclusive_checked["padding_bottom_value"] != 0 and self.data.indicator_non_exclusive_checked["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.indicator_non_exclusive_checked["padding_bottom_value"], self.data.indicator_non_exclusive_checked["padding_bottom_type"]))

        if self.data.indicator_non_exclusive_checked["padding_left_value"] != 0 and self.data.indicator_non_exclusive_checked["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.indicator_non_exclusive_checked["padding_left_value"], self.data.indicator_non_exclusive_checked["padding_left_type"]))


        if self.data.indicator_non_exclusive_checked["margin_top_value"] != 0 and self.data.indicator_non_exclusive_checked["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_non_exclusive_checked["margin_top_value"], self.data.indicator_non_exclusive_checked["margin_top_type"]))

        if self.data.indicator_non_exclusive_checked["margin_right_value"] != 0 and self.data.indicator_non_exclusive_checked["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.indicator_non_exclusive_checked["margin_right_value"], self.data.indicator_non_exclusive_checked["margin_right_type"]))

        if self.data.indicator_non_exclusive_checked["margin_bottom_value"] != 0 and self.data.indicator_non_exclusive_checked["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.indicator_non_exclusive_checked["margin_bottom_value"], self.data.indicator_non_exclusive_checked["margin_bottom_type"]))

        if self.data.indicator_non_exclusive_checked["margin_left_value"] != 0 and self.data.indicator_non_exclusive_checked["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.indicator_non_exclusive_checked["margin_left_value"], self.data.indicator_non_exclusive_checked["margin_left_type"]))


        f.write("\n}")



        f.write("\n")




        f.write("QMenu" + "::indicator:non-exclusive:checked:selected {")

        if self.data.indicator_non_exclusive_checked_selected["color"] != "":
            f.write("\n   color: {};".format(self.data.indicator_non_exclusive_checked_selected["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.indicator_non_exclusive_checked_selected["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.indicator_non_exclusive_checked_selected["outline"]))

        if self.data.indicator_non_exclusive_checked_selected["width_value"] != 0 and self.data.indicator_non_exclusive_checked_selected["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.indicator_non_exclusive_checked_selected["width_value"], self.data.indicator_non_exclusive_checked_selected["width_type"]))

        if self.data.indicator_non_exclusive_checked_selected["height_value"] != 0 and self.data.indicator_non_exclusive_checked_selected["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.indicator_non_exclusive_checked_selected["height_value"], self.data.indicator_non_exclusive_checked_selected["height_type"]))

        if self.data.indicator_non_exclusive_checked_selected["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.indicator_non_exclusive_checked_selected["font_family"]))

        if self.data.indicator_non_exclusive_checked_selected["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.indicator_non_exclusive_checked_selected["font_size"]))

        if self.data.indicator_non_exclusive_checked_selected["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.indicator_non_exclusive_checked_selected["font_weight"]))

        if self.data.indicator_non_exclusive_checked_selected["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.indicator_non_exclusive_checked_selected["font_style"]))

        if self.data.indicator_non_exclusive_checked_selected["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.indicator_non_exclusive_checked_selected["line_height"]))

        if self.data.indicator_non_exclusive_checked_selected["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.indicator_non_exclusive_checked_selected["text_align"]))

        if self.data.indicator_non_exclusive_checked_selected["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.indicator_non_exclusive_checked_selected["text_decoration"]))

        if self.data.indicator_non_exclusive_checked_selected["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.indicator_non_exclusive_checked_selected["text_transform"]))

        if self.data.indicator_non_exclusive_checked_selected["background"] != "":
            f.write("\n   background: {};".format(self.data.indicator_non_exclusive_checked_selected["background"]))

        if self.data.indicator_non_exclusive_checked_selected["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.indicator_non_exclusive_checked_selected["background_image"]))

        if self.data.indicator_non_exclusive_checked_selected["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.indicator_non_exclusive_checked_selected["background_color"]))

        if self.data.indicator_non_exclusive_checked_selected["border"] != "":
            f.write("\n   border: {};".format(self.data.indicator_non_exclusive_checked_selected["border"]))

        if self.data.indicator_non_exclusive_checked_selected["border_width_value"] != 0 and self.data.indicator_non_exclusive_checked_selected["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.indicator_non_exclusive_checked_selected["border_width_value"], self.data.indicator_non_exclusive_checked_selected["border_width_type"]))

        if self.data.indicator_non_exclusive_checked_selected["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.indicator_non_exclusive_checked_selected["border_style"]))

        if self.data.indicator_non_exclusive_checked_selected["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.indicator_non_exclusive_checked_selected["border_color"]))

        if self.data.indicator_non_exclusive_checked_selected["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.indicator_non_exclusive_checked_selected["border_top"]))

        if self.data.indicator_non_exclusive_checked_selected["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.indicator_non_exclusive_checked_selected["border_right"]))

        if self.data.indicator_non_exclusive_checked_selected["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.indicator_non_exclusive_checked_selected["border_bottom"]))

        if self.data.indicator_non_exclusive_checked_selected["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.indicator_non_exclusive_checked_selected["border_left"]))

        if self.data.indicator_non_exclusive_checked_selected["border_radius"] != 0 and self.data.indicator_non_exclusive_checked_selected["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.indicator_non_exclusive_checked_selected["border_radius"]))

        if self.data.indicator_non_exclusive_checked_selected["padding_top_value"] != 0 and self.data.indicator_non_exclusive_checked_selected["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_non_exclusive_checked_selected["padding_top_value"], self.data.indicator_non_exclusive_checked_selected["padding_top_type"]))

        if self.data.indicator_non_exclusive_checked_selected["padding_right_value"] != 0 and self.data.indicator_non_exclusive_checked_selected["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.indicator_non_exclusive_checked_selected["padding_right_value"], self.data.indicator_non_exclusive_checked_selected["padding_right_type"]))

        if self.data.indicator_non_exclusive_checked_selected["padding_bottom_value"] != 0 and self.data.indicator_non_exclusive_checked_selected["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.indicator_non_exclusive_checked_selected["padding_bottom_value"], self.data.indicator_non_exclusive_checked_selected["padding_bottom_type"]))

        if self.data.indicator_non_exclusive_checked_selected["padding_left_value"] != 0 and self.data.indicator_non_exclusive_checked_selected["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.indicator_non_exclusive_checked_selected["padding_left_value"], self.data.indicator_non_exclusive_checked_selected["padding_left_type"]))


        if self.data.indicator_non_exclusive_checked_selected["margin_top_value"] != 0 and self.data.indicator_non_exclusive_checked_selected["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_non_exclusive_checked_selected["margin_top_value"], self.data.indicator_non_exclusive_checked_selected["margin_top_type"]))

        if self.data.indicator_non_exclusive_checked_selected["margin_right_value"] != 0 and self.data.indicator_non_exclusive_checked_selected["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.indicator_non_exclusive_checked_selected["margin_right_value"], self.data.indicator_non_exclusive_checked_selected["margin_right_type"]))

        if self.data.indicator_non_exclusive_checked_selected["margin_bottom_value"] != 0 and self.data.indicator_non_exclusive_checked_selected["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.indicator_non_exclusive_checked_selected["margin_bottom_value"], self.data.indicator_non_exclusive_checked_selected["margin_bottom_type"]))

        if self.data.indicator_non_exclusive_checked_selected["margin_left_value"] != 0 and self.data.indicator_non_exclusive_checked_selected["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.indicator_non_exclusive_checked_selected["margin_left_value"], self.data.indicator_non_exclusive_checked_selected["margin_left_type"]))


        f.write("\n}")




        f.write("\n")




        f.write("QMenu" + "::indicator:non-exclusive:unchecked {")

        if self.data.indicator_non_exclusive_unchecked["color"] != "":
            f.write("\n   color: {};".format(self.data.indicator_non_exclusive_unchecked["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.indicator_non_exclusive_unchecked["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.indicator_non_exclusive_unchecked["outline"]))

        if self.data.indicator_non_exclusive_unchecked["width_value"] != 0 and self.data.indicator_non_exclusive_unchecked["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.indicator_non_exclusive_unchecked["width_value"], self.data.indicator_non_exclusive_unchecked["width_type"]))

        if self.data.indicator_non_exclusive_unchecked["height_value"] != 0 and self.data.indicator_non_exclusive_unchecked["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.indicator_non_exclusive_unchecked["height_value"], self.data.indicator_non_exclusive_unchecked["height_type"]))

        if self.data.indicator_non_exclusive_unchecked["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.indicator_non_exclusive_unchecked["font_family"]))

        if self.data.indicator_non_exclusive_unchecked["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.indicator_non_exclusive_unchecked["font_size"]))

        if self.data.indicator_non_exclusive_unchecked["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.indicator_non_exclusive_unchecked["font_weight"]))

        if self.data.indicator_non_exclusive_unchecked["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.indicator_non_exclusive_unchecked["font_style"]))

        if self.data.indicator_non_exclusive_unchecked["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.indicator_non_exclusive_unchecked["line_height"]))

        if self.data.indicator_non_exclusive_unchecked["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.indicator_non_exclusive_unchecked["text_align"]))

        if self.data.indicator_non_exclusive_unchecked["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.indicator_non_exclusive_unchecked["text_decoration"]))

        if self.data.indicator_non_exclusive_unchecked["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.indicator_non_exclusive_unchecked["text_transform"]))

        if self.data.indicator_non_exclusive_unchecked["background"] != "":
            f.write("\n   background: {};".format(self.data.indicator_non_exclusive_unchecked["background"]))

        if self.data.indicator_non_exclusive_unchecked["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.indicator_non_exclusive_unchecked["background_image"]))

        if self.data.indicator_non_exclusive_unchecked["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.indicator_non_exclusive_unchecked["background_color"]))

        if self.data.indicator_non_exclusive_unchecked["border"] != "":
            f.write("\n   border: {};".format(self.data.indicator_non_exclusive_unchecked["border"]))

        if self.data.indicator_non_exclusive_unchecked["border_width_value"] != 0 and self.data.indicator_non_exclusive_unchecked["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.indicator_non_exclusive_unchecked["border_width_value"], self.data.indicator_non_exclusive_unchecked["border_width_type"]))

        if self.data.indicator_non_exclusive_unchecked["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.indicator_non_exclusive_unchecked["border_style"]))

        if self.data.indicator_non_exclusive_unchecked["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.indicator_non_exclusive_unchecked["border_color"]))

        if self.data.indicator_non_exclusive_unchecked["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.indicator_non_exclusive_unchecked["border_top"]))

        if self.data.indicator_non_exclusive_unchecked["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.indicator_non_exclusive_unchecked["border_right"]))

        if self.data.indicator_non_exclusive_unchecked["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.indicator_non_exclusive_unchecked["border_bottom"]))

        if self.data.indicator_non_exclusive_unchecked["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.indicator_non_exclusive_unchecked["border_left"]))

        if self.data.indicator_non_exclusive_unchecked["border_radius"] != 0 and self.data.indicator_non_exclusive_unchecked["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.indicator_non_exclusive_unchecked["border_radius"]))

        if self.data.indicator_non_exclusive_unchecked["padding_top_value"] != 0 and self.data.indicator_non_exclusive_unchecked["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_non_exclusive_unchecked["padding_top_value"], self.data.indicator_non_exclusive_unchecked["padding_top_type"]))

        if self.data.indicator_non_exclusive_unchecked["padding_right_value"] != 0 and self.data.indicator_non_exclusive_unchecked["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.indicator_non_exclusive_unchecked["padding_right_value"], self.data.indicator_non_exclusive_unchecked["padding_right_type"]))

        if self.data.indicator_non_exclusive_unchecked["padding_bottom_value"] != 0 and self.data.indicator_non_exclusive_unchecked["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.indicator_non_exclusive_unchecked["padding_bottom_value"], self.data.indicator_non_exclusive_unchecked["padding_bottom_type"]))

        if self.data.indicator_non_exclusive_unchecked["padding_left_value"] != 0 and self.data.indicator_non_exclusive_unchecked["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.indicator_non_exclusive_unchecked["padding_left_value"], self.data.indicator_non_exclusive_unchecked["padding_left_type"]))


        if self.data.indicator_non_exclusive_unchecked["margin_top_value"] != 0 and self.data.indicator_non_exclusive_unchecked["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_non_exclusive_unchecked["margin_top_value"], self.data.indicator_non_exclusive_unchecked["margin_top_type"]))

        if self.data.indicator_non_exclusive_unchecked["margin_right_value"] != 0 and self.data.indicator_non_exclusive_unchecked["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.indicator_non_exclusive_unchecked["margin_right_value"], self.data.indicator_non_exclusive_unchecked["margin_right_type"]))

        if self.data.indicator_non_exclusive_unchecked["margin_bottom_value"] != 0 and self.data.indicator_non_exclusive_unchecked["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.indicator_non_exclusive_unchecked["margin_bottom_value"], self.data.indicator_non_exclusive_unchecked["margin_bottom_type"]))

        if self.data.indicator_non_exclusive_unchecked["margin_left_value"] != 0 and self.data.indicator_non_exclusive_unchecked["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.indicator_non_exclusive_unchecked["margin_left_value"], self.data.indicator_non_exclusive_unchecked["margin_left_type"]))


        f.write("\n}")





        f.write("\n")




        f.write("QMenu" + "::indicator:non-exclusive:unchecked:selected {")

        if self.data.indicator_non_exclusive_unchecked_selected["color"] != "":
            f.write("\n   color: {};".format(self.data.indicator_non_exclusive_unchecked_selected["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.indicator_non_exclusive_unchecked_selected["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.indicator_non_exclusive_unchecked_selected["outline"]))

        if self.data.indicator_non_exclusive_unchecked_selected["width_value"] != 0 and self.data.indicator_non_exclusive_unchecked_selected["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.indicator_non_exclusive_unchecked_selected["width_value"], self.data.indicator_non_exclusive_unchecked_selected["width_type"]))

        if self.data.indicator_non_exclusive_unchecked_selected["height_value"] != 0 and self.data.indicator_non_exclusive_unchecked_selected["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.indicator_non_exclusive_unchecked_selected["height_value"], self.data.indicator_non_exclusive_unchecked_selected["height_type"]))

        if self.data.indicator_non_exclusive_unchecked_selected["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.indicator_non_exclusive_unchecked_selected["font_family"]))

        if self.data.indicator_non_exclusive_unchecked_selected["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.indicator_non_exclusive_unchecked_selected["font_size"]))

        if self.data.indicator_non_exclusive_unchecked_selected["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.indicator_non_exclusive_unchecked_selected["font_weight"]))

        if self.data.indicator_non_exclusive_unchecked_selected["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.indicator_non_exclusive_unchecked_selected["font_style"]))

        if self.data.indicator_non_exclusive_unchecked_selected["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.indicator_non_exclusive_unchecked_selected["line_height"]))

        if self.data.indicator_non_exclusive_unchecked_selected["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.indicator_non_exclusive_unchecked_selected["text_align"]))

        if self.data.indicator_non_exclusive_unchecked_selected["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.indicator_non_exclusive_unchecked_selected["text_decoration"]))

        if self.data.indicator_non_exclusive_unchecked_selected["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.indicator_non_exclusive_unchecked_selected["text_transform"]))

        if self.data.indicator_non_exclusive_unchecked_selected["background"] != "":
            f.write("\n   background: {};".format(self.data.indicator_non_exclusive_unchecked_selected["background"]))

        if self.data.indicator_non_exclusive_unchecked_selected["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.indicator_non_exclusive_unchecked_selected["background_image"]))

        if self.data.indicator_non_exclusive_unchecked_selected["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.indicator_non_exclusive_unchecked_selected["background_color"]))

        if self.data.indicator_non_exclusive_unchecked_selected["border"] != "":
            f.write("\n   border: {};".format(self.data.indicator_non_exclusive_unchecked_selected["border"]))

        if self.data.indicator_non_exclusive_unchecked_selected["border_width_value"] != 0 and self.data.indicator_non_exclusive_unchecked_selected["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.indicator_non_exclusive_unchecked_selected["border_width_value"], self.data.indicator_non_exclusive_unchecked_selected["border_width_type"]))

        if self.data.indicator_non_exclusive_unchecked_selected["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.indicator_non_exclusive_unchecked_selected["border_style"]))

        if self.data.indicator_non_exclusive_unchecked_selected["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.indicator_non_exclusive_unchecked_selected["border_color"]))

        if self.data.indicator_non_exclusive_unchecked_selected["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.indicator_non_exclusive_unchecked_selected["border_top"]))

        if self.data.indicator_non_exclusive_unchecked_selected["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.indicator_non_exclusive_unchecked_selected["border_right"]))

        if self.data.indicator_non_exclusive_unchecked_selected["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.indicator_non_exclusive_unchecked_selected["border_bottom"]))

        if self.data.indicator_non_exclusive_unchecked_selected["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.indicator_non_exclusive_unchecked_selected["border_left"]))

        if self.data.indicator_non_exclusive_unchecked_selected["border_radius"] != 0 and self.data.indicator_non_exclusive_unchecked_selected["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.indicator_non_exclusive_unchecked_selected["border_radius"]))

        if self.data.indicator_non_exclusive_unchecked_selected["padding_top_value"] != 0 and self.data.indicator_non_exclusive_unchecked_selected["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_non_exclusive_unchecked_selected["padding_top_value"], self.data.indicator_non_exclusive_unchecked_selected["padding_top_type"]))

        if self.data.indicator_non_exclusive_unchecked_selected["padding_right_value"] != 0 and self.data.indicator_non_exclusive_unchecked_selected["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.indicator_non_exclusive_unchecked_selected["padding_right_value"], self.data.indicator_non_exclusive_unchecked_selected["padding_right_type"]))

        if self.data.indicator_non_exclusive_unchecked_selected["padding_bottom_value"] != 0 and self.data.indicator_non_exclusive_unchecked_selected["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.indicator_non_exclusive_unchecked_selected["padding_bottom_value"], self.data.indicator_non_exclusive_unchecked_selected["padding_bottom_type"]))

        if self.data.indicator_non_exclusive_unchecked_selected["padding_left_value"] != 0 and self.data.indicator_non_exclusive_unchecked_selected["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.indicator_non_exclusive_unchecked_selected["padding_left_value"], self.data.indicator_non_exclusive_unchecked_selected["padding_left_type"]))


        if self.data.indicator_non_exclusive_unchecked_selected["margin_top_value"] != 0 and self.data.indicator_non_exclusive_unchecked_selected["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.indicator_non_exclusive_unchecked_selected["margin_top_value"], self.data.indicator_non_exclusive_unchecked_selected["margin_top_type"]))

        if self.data.indicator_non_exclusive_unchecked_selected["margin_right_value"] != 0 and self.data.indicator_non_exclusive_unchecked_selected["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.indicator_non_exclusive_unchecked_selected["margin_right_value"], self.data.indicator_non_exclusive_unchecked_selected["margin_right_type"]))

        if self.data.indicator_non_exclusive_unchecked_selected["margin_bottom_value"] != 0 and self.data.indicator_non_exclusive_unchecked_selected["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.indicator_non_exclusive_unchecked_selected["margin_bottom_value"], self.data.indicator_non_exclusive_unchecked_selected["margin_bottom_type"]))

        if self.data.indicator_non_exclusive_unchecked_selected["margin_left_value"] != 0 and self.data.indicator_non_exclusive_unchecked_selected["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.indicator_non_exclusive_unchecked_selected["margin_left_value"], self.data.indicator_non_exclusive_unchecked_selected["margin_left_type"]))


        f.write("\n}")
