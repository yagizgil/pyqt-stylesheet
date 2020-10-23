class TabWidget():

    def __init__(self, text, data):
        self.text = text
        self.data = data

        self.write()

    def write(self):
        f = open("a", "w")
        f.write(self.text + " {")

        if self.data.wme["color"] != "":
            f.write("\n   color: {};".format(self.data.wme["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.wme["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.wme["outline"]))

        if self.data.wme["width_value"] != 0 and self.data.wme["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.wme["width_value"], self.data.wme["width_type"]))

        if self.data.wme["height_value"] != 0 and self.data.wme["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.wme["height_value"], self.data.wme["height_type"]))

        if self.data.wme["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.wme["font_family"]))

        if self.data.wme["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.wme["font_size"]))

        if self.data.wme["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.wme["font_weight"]))

        if self.data.wme["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.wme["font_style"]))

        if self.data.wme["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.wme["line_height"]))

        if self.data.wme["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.wme["text_align"]))

        if self.data.wme["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.wme["text_decoration"]))

        if self.data.wme["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.wme["text_transform"]))

        if self.data.wme["background"] != "":
            f.write("\n   background: {};".format(self.data.wme["background"]))

        if self.data.wme["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.wme["background_image"]))

        if self.data.wme["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.wme["background_color"]))

        if self.data.wme["border"] != "":
            f.write("\n   border: {};".format(self.data.wme["border"]))

        if self.data.wme["border_width_value"] != 0 and self.data.wme["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.wme["border_width_value"], self.data.wme["border_width_type"]))

        if self.data.wme["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.wme["border_style"]))

        if self.data.wme["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.wme["border_color"]))

        if self.data.wme["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.wme["border_top"]))

        if self.data.wme["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.wme["border_right"]))

        if self.data.wme["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.wme["border_bottom"]))

        if self.data.wme["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.wme["border_left"]))

        if self.data.wme["border_radius"] != 0 and self.data.wme["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.wme["border_radius"]))

        if self.data.wme["padding_top_value"] != 0 and self.data.wme["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.wme["padding_top_value"], self.data.wme["padding_top_type"]))

        if self.data.wme["padding_right_value"] != 0 and self.data.wme["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.wme["padding_right_value"], self.data.wme["padding_right_type"]))

        if self.data.wme["padding_bottom_value"] != 0 and self.data.wme["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.wme["padding_bottom_value"], self.data.wme["padding_bottom_type"]))

        if self.data.wme["padding_left_value"] != 0 and self.data.wme["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.wme["padding_left_value"], self.data.wme["padding_left_type"]))


        if self.data.wme["margin_top_value"] != 0 and self.data.wme["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.wme["margin_top_value"], self.data.wme["margin_top_type"]))

        if self.data.wme["margin_right_value"] != 0 and self.data.wme["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.wme["margin_right_value"], self.data.wme["margin_right_type"]))

        if self.data.wme["margin_bottom_value"] != 0 and self.data.wme["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.wme["margin_bottom_value"], self.data.wme["margin_bottom_type"]))

        if self.data.wme["margin_left_value"] != 0 and self.data.wme["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.wme["margin_left_value"], self.data.wme["margin_left_type"]))

        f.write("\n}")



        f.write("\n")




        f.write(self.text + ":hover {")

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




        f.write(self.text + "::pane {")

        if self.data.pane["color"] != "":
            f.write("\n   color: {};".format(self.data.pane["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.pane["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.pane["outline"]))

        if self.data.pane["width_value"] != 0 and self.data.pane["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.pane["width_value"], self.data.pane["width_type"]))

        if self.data.pane["height_value"] != 0 and self.data.pane["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.pane["height_value"], self.data.pane["height_type"]))

        if self.data.pane["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.pane["font_family"]))

        if self.data.pane["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.pane["font_size"]))

        if self.data.pane["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.pane["font_weight"]))

        if self.data.pane["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.pane["font_style"]))

        if self.data.pane["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.pane["line_height"]))

        if self.data.pane["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.pane["text_align"]))

        if self.data.pane["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.pane["text_decoration"]))

        if self.data.pane["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.pane["text_transform"]))

        if self.data.pane["background"] != "":
            f.write("\n   background: {};".format(self.data.pane["background"]))

        if self.data.pane["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.pane["background_image"]))

        if self.data.pane["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.pane["background_color"]))

        if self.data.pane["border"] != "":
            f.write("\n   border: {};".format(self.data.pane["border"]))

        if self.data.pane["border_width_value"] != 0 and self.data.pane["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.pane["border_width_value"], self.data.pane["border_width_type"]))

        if self.data.pane["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.pane["border_style"]))

        if self.data.pane["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.pane["border_color"]))

        if self.data.pane["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.pane["border_top"]))

        if self.data.pane["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.pane["border_right"]))

        if self.data.pane["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.pane["border_bottom"]))

        if self.data.pane["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.pane["border_left"]))

        if self.data.pane["border_radius"] != 0 and self.data.pane["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.pane["border_radius"]))

        if self.data.pane["padding_top_value"] != 0 and self.data.pane["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.pane["padding_top_value"], self.data.pane["padding_top_type"]))

        if self.data.pane["padding_right_value"] != 0 and self.data.pane["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.pane["padding_right_value"], self.data.pane["padding_right_type"]))

        if self.data.pane["padding_bottom_value"] != 0 and self.data.pane["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.pane["padding_bottom_value"], self.data.pane["padding_bottom_type"]))

        if self.data.pane["padding_left_value"] != 0 and self.data.pane["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.pane["padding_left_value"], self.data.pane["padding_left_type"]))


        if self.data.pane["margin_top_value"] != 0 and self.data.pane["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.pane["margin_top_value"], self.data.pane["margin_top_type"]))

        if self.data.pane["margin_right_value"] != 0 and self.data.pane["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.pane["margin_right_value"], self.data.pane["margin_right_type"]))

        if self.data.pane["margin_bottom_value"] != 0 and self.data.pane["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.pane["margin_bottom_value"], self.data.pane["margin_bottom_type"]))

        if self.data.pane["margin_left_value"] != 0 and self.data.pane["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.pane["margin_left_value"], self.data.pane["margin_left_type"]))


        f.write("\n}")






        f.write("\n")




        f.write(self.text + "::tab-bar {")

        if self.data.tab_bar["color"] != "":
            f.write("\n   color: {};".format(self.data.tab_bar["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.tab_bar["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.tab_bar["outline"]))

        if self.data.tab_bar["width_value"] != 0 and self.data.tab_bar["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.tab_bar["width_value"], self.data.tab_bar["width_type"]))

        if self.data.tab_bar["height_value"] != 0 and self.data.tab_bar["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.tab_bar["height_value"], self.data.tab_bar["height_type"]))

        if self.data.tab_bar["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.tab_bar["font_family"]))

        if self.data.tab_bar["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.tab_bar["font_size"]))

        if self.data.tab_bar["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.tab_bar["font_weight"]))

        if self.data.tab_bar["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.tab_bar["font_style"]))

        if self.data.tab_bar["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.tab_bar["line_height"]))

        if self.data.tab_bar["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.tab_bar["text_align"]))

        if self.data.tab_bar["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.tab_bar["text_decoration"]))

        if self.data.tab_bar["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.tab_bar["text_transform"]))

        if self.data.tab_bar["background"] != "":
            f.write("\n   background: {};".format(self.data.tab_bar["background"]))

        if self.data.tab_bar["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.tab_bar["background_image"]))

        if self.data.tab_bar["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.tab_bar["background_color"]))

        if self.data.tab_bar["border"] != "":
            f.write("\n   border: {};".format(self.data.tab_bar["border"]))

        if self.data.tab_bar["border_width_value"] != 0 and self.data.tab_bar["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.tab_bar["border_width_value"], self.data.tab_bar["border_width_type"]))

        if self.data.tab_bar["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.tab_bar["border_style"]))

        if self.data.tab_bar["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.tab_bar["border_color"]))

        if self.data.tab_bar["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.tab_bar["border_top"]))

        if self.data.tab_bar["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.tab_bar["border_right"]))

        if self.data.tab_bar["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.tab_bar["border_bottom"]))

        if self.data.tab_bar["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.tab_bar["border_left"]))

        if self.data.tab_bar["border_radius"] != 0 and self.data.tab_bar["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.tab_bar["border_radius"]))

        if self.data.tab_bar["padding_top_value"] != 0 and self.data.tab_bar["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_bar["padding_top_value"], self.data.tab_bar["padding_top_type"]))

        if self.data.tab_bar["padding_right_value"] != 0 and self.data.tab_bar["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.tab_bar["padding_right_value"], self.data.tab_bar["padding_right_type"]))

        if self.data.tab_bar["padding_bottom_value"] != 0 and self.data.tab_bar["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.tab_bar["padding_bottom_value"], self.data.tab_bar["padding_bottom_type"]))

        if self.data.tab_bar["padding_left_value"] != 0 and self.data.tab_bar["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.tab_bar["padding_left_value"], self.data.tab_bar["padding_left_type"]))


        if self.data.tab_bar["margin_top_value"] != 0 and self.data.tab_bar["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_bar["margin_top_value"], self.data.tab_bar["margin_top_type"]))

        if self.data.tab_bar["margin_right_value"] != 0 and self.data.tab_bar["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.tab_bar["margin_right_value"], self.data.tab_bar["margin_right_type"]))

        if self.data.tab_bar["margin_bottom_value"] != 0 and self.data.tab_bar["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.tab_bar["margin_bottom_value"], self.data.tab_bar["margin_bottom_type"]))

        if self.data.tab_bar["margin_left_value"] != 0 and self.data.tab_bar["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.tab_bar["margin_left_value"], self.data.tab_bar["margin_left_type"]))


        f.write("\n}")







        f.write("\n")




        f.write(self.text + "::tab-bar:top {")

        if self.data.tab_bar_top["color"] != "":
            f.write("\n   color: {};".format(self.data.tab_bar_top["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.tab_bar_top["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.tab_bar_top["outline"]))

        if self.data.tab_bar_top["width_value"] != 0 and self.data.tab_bar_top["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.tab_bar_top["width_value"], self.data.tab_bar_top["width_type"]))

        if self.data.tab_bar_top["height_value"] != 0 and self.data.tab_bar_top["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.tab_bar_top["height_value"], self.data.tab_bar_top["height_type"]))

        if self.data.tab_bar_top["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.tab_bar_top["font_family"]))

        if self.data.tab_bar_top["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.tab_bar_top["font_size"]))

        if self.data.tab_bar_top["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.tab_bar_top["font_weight"]))

        if self.data.tab_bar_top["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.tab_bar_top["font_style"]))

        if self.data.tab_bar_top["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.tab_bar_top["line_height"]))

        if self.data.tab_bar_top["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.tab_bar_top["text_align"]))

        if self.data.tab_bar_top["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.tab_bar_top["text_decoration"]))

        if self.data.tab_bar_top["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.tab_bar_top["text_transform"]))

        if self.data.tab_bar_top["background"] != "":
            f.write("\n   background: {};".format(self.data.tab_bar_top["background"]))

        if self.data.tab_bar_top["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.tab_bar_top["background_image"]))

        if self.data.tab_bar_top["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.tab_bar_top["background_color"]))

        if self.data.tab_bar_top["border"] != "":
            f.write("\n   border: {};".format(self.data.tab_bar_top["border"]))

        if self.data.tab_bar_top["border_width_value"] != 0 and self.data.tab_bar_top["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.tab_bar_top["border_width_value"], self.data.tab_bar_top["border_width_type"]))

        if self.data.tab_bar_top["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.tab_bar_top["border_style"]))

        if self.data.tab_bar_top["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.tab_bar_top["border_color"]))

        if self.data.tab_bar_top["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.tab_bar_top["border_top"]))

        if self.data.tab_bar_top["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.tab_bar_top["border_right"]))

        if self.data.tab_bar_top["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.tab_bar_top["border_bottom"]))

        if self.data.tab_bar_top["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.tab_bar_top["border_left"]))

        if self.data.tab_bar_top["border_radius"] != 0 and self.data.tab_bar_top["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.tab_bar_top["border_radius"]))

        if self.data.tab_bar_top["padding_top_value"] != 0 and self.data.tab_bar_top["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_bar_top["padding_top_value"], self.data.tab_bar_top["padding_top_type"]))

        if self.data.tab_bar_top["padding_right_value"] != 0 and self.data.tab_bar_top["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.tab_bar_top["padding_right_value"], self.data.tab_bar_top["padding_right_type"]))

        if self.data.tab_bar_top["padding_bottom_value"] != 0 and self.data.tab_bar_top["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.tab_bar_top["padding_bottom_value"], self.data.tab_bar_top["padding_bottom_type"]))

        if self.data.tab_bar_top["padding_left_value"] != 0 and self.data.tab_bar_top["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.tab_bar_top["padding_left_value"], self.data.tab_bar_top["padding_left_type"]))


        if self.data.tab_bar_top["margin_top_value"] != 0 and self.data.tab_bar_top["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_bar_top["margin_top_value"], self.data.tab_bar_top["margin_top_type"]))

        if self.data.tab_bar_top["margin_right_value"] != 0 and self.data.tab_bar_top["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.tab_bar_top["margin_right_value"], self.data.tab_bar_top["margin_right_type"]))

        if self.data.tab_bar_top["margin_bottom_value"] != 0 and self.data.tab_bar_top["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.tab_bar_top["margin_bottom_value"], self.data.tab_bar_top["margin_bottom_type"]))

        if self.data.tab_bar_top["margin_left_value"] != 0 and self.data.tab_bar_top["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.tab_bar_top["margin_left_value"], self.data.tab_bar_top["margin_left_type"]))


        f.write("\n}")








        f.write("\n")




        f.write(self.text + "::tab-bar:right {")

        if self.data.tab_bar_right["color"] != "":
            f.write("\n   color: {};".format(self.data.tab_bar_right["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.tab_bar_right["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.tab_bar_right["outline"]))

        if self.data.tab_bar_right["width_value"] != 0 and self.data.tab_bar_right["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.tab_bar_right["width_value"], self.data.tab_bar_right["width_type"]))

        if self.data.tab_bar_right["height_value"] != 0 and self.data.tab_bar_right["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.tab_bar_right["height_value"], self.data.tab_bar_right["height_type"]))

        if self.data.tab_bar_right["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.tab_bar_right["font_family"]))

        if self.data.tab_bar_right["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.tab_bar_right["font_size"]))

        if self.data.tab_bar_right["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.tab_bar_right["font_weight"]))

        if self.data.tab_bar_right["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.tab_bar_right["font_style"]))

        if self.data.tab_bar_right["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.tab_bar_right["line_height"]))

        if self.data.tab_bar_right["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.tab_bar_right["text_align"]))

        if self.data.tab_bar_right["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.tab_bar_right["text_decoration"]))

        if self.data.tab_bar_right["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.tab_bar_right["text_transform"]))

        if self.data.tab_bar_right["background"] != "":
            f.write("\n   background: {};".format(self.data.tab_bar_right["background"]))

        if self.data.tab_bar_right["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.tab_bar_right["background_image"]))

        if self.data.tab_bar_right["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.tab_bar_right["background_color"]))

        if self.data.tab_bar_right["border"] != "":
            f.write("\n   border: {};".format(self.data.tab_bar_right["border"]))

        if self.data.tab_bar_right["border_width_value"] != 0 and self.data.tab_bar_right["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.tab_bar_right["border_width_value"], self.data.tab_bar_right["border_width_type"]))

        if self.data.tab_bar_right["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.tab_bar_right["border_style"]))

        if self.data.tab_bar_right["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.tab_bar_right["border_color"]))

        if self.data.tab_bar_right["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.tab_bar_right["border_top"]))

        if self.data.tab_bar_right["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.tab_bar_right["border_right"]))

        if self.data.tab_bar_right["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.tab_bar_right["border_bottom"]))

        if self.data.tab_bar_right["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.tab_bar_right["border_left"]))

        if self.data.tab_bar_right["border_radius"] != 0 and self.data.tab_bar_right["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.tab_bar_right["border_radius"]))

        if self.data.tab_bar_right["padding_top_value"] != 0 and self.data.tab_bar_right["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_bar_right["padding_top_value"], self.data.tab_bar_right["padding_top_type"]))

        if self.data.tab_bar_right["padding_right_value"] != 0 and self.data.tab_bar_right["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.tab_bar_right["padding_right_value"], self.data.tab_bar_right["padding_right_type"]))

        if self.data.tab_bar_right["padding_bottom_value"] != 0 and self.data.tab_bar_right["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.tab_bar_right["padding_bottom_value"], self.data.tab_bar_right["padding_bottom_type"]))

        if self.data.tab_bar_right["padding_left_value"] != 0 and self.data.tab_bar_right["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.tab_bar_right["padding_left_value"], self.data.tab_bar_right["padding_left_type"]))


        if self.data.tab_bar_right["margin_top_value"] != 0 and self.data.tab_bar_right["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_bar_right["margin_top_value"], self.data.tab_bar_right["margin_top_type"]))

        if self.data.tab_bar_right["margin_right_value"] != 0 and self.data.tab_bar_right["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.tab_bar_right["margin_right_value"], self.data.tab_bar_right["margin_right_type"]))

        if self.data.tab_bar_right["margin_bottom_value"] != 0 and self.data.tab_bar_right["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.tab_bar_right["margin_bottom_value"], self.data.tab_bar_right["margin_bottom_type"]))

        if self.data.tab_bar_right["margin_left_value"] != 0 and self.data.tab_bar_right["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.tab_bar_right["margin_left_value"], self.data.tab_bar_right["margin_left_type"]))


        f.write("\n}")








        f.write("\n")




        f.write(self.text + "::tab-bar:bottom {")

        if self.data.tab_bar_bottom["color"] != "":
            f.write("\n   color: {};".format(self.data.tab_bar_bottom["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.tab_bar_bottom["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.tab_bar_bottom["outline"]))

        if self.data.tab_bar_bottom["width_value"] != 0 and self.data.tab_bar_bottom["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.tab_bar_bottom["width_value"], self.data.tab_bar_bottom["width_type"]))

        if self.data.tab_bar_bottom["height_value"] != 0 and self.data.tab_bar_bottom["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.tab_bar_bottom["height_value"], self.data.tab_bar_bottom["height_type"]))

        if self.data.tab_bar_bottom["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.tab_bar_bottom["font_family"]))

        if self.data.tab_bar_bottom["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.tab_bar_bottom["font_size"]))

        if self.data.tab_bar_bottom["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.tab_bar_bottom["font_weight"]))

        if self.data.tab_bar_bottom["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.tab_bar_bottom["font_style"]))

        if self.data.tab_bar_bottom["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.tab_bar_bottom["line_height"]))

        if self.data.tab_bar_bottom["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.tab_bar_bottom["text_align"]))

        if self.data.tab_bar_bottom["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.tab_bar_bottom["text_decoration"]))

        if self.data.tab_bar_bottom["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.tab_bar_bottom["text_transform"]))

        if self.data.tab_bar_bottom["background"] != "":
            f.write("\n   background: {};".format(self.data.tab_bar_bottom["background"]))

        if self.data.tab_bar_bottom["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.tab_bar_bottom["background_image"]))

        if self.data.tab_bar_bottom["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.tab_bar_bottom["background_color"]))

        if self.data.tab_bar_bottom["border"] != "":
            f.write("\n   border: {};".format(self.data.tab_bar_bottom["border"]))

        if self.data.tab_bar_bottom["border_width_value"] != 0 and self.data.tab_bar_bottom["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.tab_bar_bottom["border_width_value"], self.data.tab_bar_bottom["border_width_type"]))

        if self.data.tab_bar_bottom["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.tab_bar_bottom["border_style"]))

        if self.data.tab_bar_bottom["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.tab_bar_bottom["border_color"]))

        if self.data.tab_bar_bottom["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.tab_bar_bottom["border_top"]))

        if self.data.tab_bar_bottom["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.tab_bar_bottom["border_right"]))

        if self.data.tab_bar_bottom["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.tab_bar_bottom["border_bottom"]))

        if self.data.tab_bar_bottom["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.tab_bar_bottom["border_left"]))

        if self.data.tab_bar_bottom["border_radius"] != 0 and self.data.tab_bar_bottom["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.tab_bar_bottom["border_radius"]))

        if self.data.tab_bar_bottom["padding_top_value"] != 0 and self.data.tab_bar_bottom["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_bar_bottom["padding_top_value"], self.data.tab_bar_bottom["padding_top_type"]))

        if self.data.tab_bar_bottom["padding_right_value"] != 0 and self.data.tab_bar_bottom["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.tab_bar_bottom["padding_right_value"], self.data.tab_bar_bottom["padding_right_type"]))

        if self.data.tab_bar_bottom["padding_bottom_value"] != 0 and self.data.tab_bar_bottom["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.tab_bar_bottom["padding_bottom_value"], self.data.tab_bar_bottom["padding_bottom_type"]))

        if self.data.tab_bar_bottom["padding_left_value"] != 0 and self.data.tab_bar_bottom["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.tab_bar_bottom["padding_left_value"], self.data.tab_bar_bottom["padding_left_type"]))


        if self.data.tab_bar_bottom["margin_top_value"] != 0 and self.data.tab_bar_bottom["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_bar_bottom["margin_top_value"], self.data.tab_bar_bottom["margin_top_type"]))

        if self.data.tab_bar_bottom["margin_right_value"] != 0 and self.data.tab_bar_bottom["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.tab_bar_bottom["margin_right_value"], self.data.tab_bar_bottom["margin_right_type"]))

        if self.data.tab_bar_bottom["margin_bottom_value"] != 0 and self.data.tab_bar_bottom["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.tab_bar_bottom["margin_bottom_value"], self.data.tab_bar_bottom["margin_bottom_type"]))

        if self.data.tab_bar_bottom["margin_left_value"] != 0 and self.data.tab_bar_bottom["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.tab_bar_bottom["margin_left_value"], self.data.tab_bar_bottom["margin_left_type"]))


        f.write("\n}")




        f.write("\n")




        f.write(self.text + "::tab-bar:left {")

        if self.data.tab_bar_left["color"] != "":
            f.write("\n   color: {};".format(self.data.tab_bar_left["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.tab_bar_left["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.tab_bar_left["outline"]))

        if self.data.tab_bar_left["width_value"] != 0 and self.data.tab_bar_left["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.tab_bar_left["width_value"], self.data.tab_bar_left["width_type"]))

        if self.data.tab_bar_left["height_value"] != 0 and self.data.tab_bar_left["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.tab_bar_left["height_value"], self.data.tab_bar_left["height_type"]))

        if self.data.tab_bar_left["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.tab_bar_left["font_family"]))

        if self.data.tab_bar_left["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.tab_bar_left["font_size"]))

        if self.data.tab_bar_left["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.tab_bar_left["font_weight"]))

        if self.data.tab_bar_left["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.tab_bar_left["font_style"]))

        if self.data.tab_bar_left["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.tab_bar_left["line_height"]))

        if self.data.tab_bar_left["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.tab_bar_left["text_align"]))

        if self.data.tab_bar_left["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.tab_bar_left["text_decoration"]))

        if self.data.tab_bar_left["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.tab_bar_left["text_transform"]))

        if self.data.tab_bar_left["background"] != "":
            f.write("\n   background: {};".format(self.data.tab_bar_left["background"]))

        if self.data.tab_bar_left["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.tab_bar_left["background_image"]))

        if self.data.tab_bar_left["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.tab_bar_left["background_color"]))

        if self.data.tab_bar_left["border"] != "":
            f.write("\n   border: {};".format(self.data.tab_bar_left["border"]))

        if self.data.tab_bar_left["border_width_value"] != 0 and self.data.tab_bar_left["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.tab_bar_left["border_width_value"], self.data.tab_bar_left["border_width_type"]))

        if self.data.tab_bar_left["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.tab_bar_left["border_style"]))

        if self.data.tab_bar_left["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.tab_bar_left["border_color"]))

        if self.data.tab_bar_left["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.tab_bar_left["border_top"]))

        if self.data.tab_bar_left["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.tab_bar_left["border_right"]))

        if self.data.tab_bar_left["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.tab_bar_left["border_bottom"]))

        if self.data.tab_bar_left["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.tab_bar_left["border_left"]))

        if self.data.tab_bar_left["border_radius"] != 0 and self.data.tab_bar_left["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.tab_bar_left["border_radius"]))

        if self.data.tab_bar_left["padding_top_value"] != 0 and self.data.tab_bar_left["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_bar_left["padding_top_value"], self.data.tab_bar_left["padding_top_type"]))

        if self.data.tab_bar_left["padding_right_value"] != 0 and self.data.tab_bar_left["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.tab_bar_left["padding_right_value"], self.data.tab_bar_left["padding_right_type"]))

        if self.data.tab_bar_left["padding_bottom_value"] != 0 and self.data.tab_bar_left["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.tab_bar_left["padding_bottom_value"], self.data.tab_bar_left["padding_bottom_type"]))

        if self.data.tab_bar_left["padding_left_value"] != 0 and self.data.tab_bar_left["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.tab_bar_left["padding_left_value"], self.data.tab_bar_left["padding_left_type"]))


        if self.data.tab_bar_left["margin_top_value"] != 0 and self.data.tab_bar_left["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_bar_left["margin_top_value"], self.data.tab_bar_left["margin_top_type"]))

        if self.data.tab_bar_left["margin_right_value"] != 0 and self.data.tab_bar_left["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.tab_bar_left["margin_right_value"], self.data.tab_bar_left["margin_right_type"]))

        if self.data.tab_bar_left["margin_bottom_value"] != 0 and self.data.tab_bar_left["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.tab_bar_left["margin_bottom_value"], self.data.tab_bar_left["margin_bottom_type"]))

        if self.data.tab_bar_left["margin_left_value"] != 0 and self.data.tab_bar_left["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.tab_bar_left["margin_left_value"], self.data.tab_bar_left["margin_left_type"]))


        f.write("\n}")




        f.write("\n")




        f.write("QTabBar" + " {")

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




        f.write("QTabBar" + "::tab {")

        if self.data.tab["color"] != "":
            f.write("\n   color: {};".format(self.data.tab["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.tab["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.tab["outline"]))

        if self.data.tab["width_value"] != 0 and self.data.tab["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.tab["width_value"], self.data.tab["width_type"]))

        if self.data.tab["height_value"] != 0 and self.data.tab["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.tab["height_value"], self.data.tab["height_type"]))

        if self.data.tab["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.tab["font_family"]))

        if self.data.tab["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.tab["font_size"]))

        if self.data.tab["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.tab["font_weight"]))

        if self.data.tab["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.tab["font_style"]))

        if self.data.tab["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.tab["line_height"]))

        if self.data.tab["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.tab["text_align"]))

        if self.data.tab["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.tab["text_decoration"]))

        if self.data.tab["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.tab["text_transform"]))

        if self.data.tab["background"] != "":
            f.write("\n   background: {};".format(self.data.tab["background"]))

        if self.data.tab["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.tab["background_image"]))

        if self.data.tab["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.tab["background_color"]))

        if self.data.tab["border"] != "":
            f.write("\n   border: {};".format(self.data.tab["border"]))

        if self.data.tab["border_width_value"] != 0 and self.data.tab["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.tab["border_width_value"], self.data.tab["border_width_type"]))

        if self.data.tab["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.tab["border_style"]))

        if self.data.tab["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.tab["border_color"]))

        if self.data.tab["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.tab["border_top"]))

        if self.data.tab["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.tab["border_right"]))

        if self.data.tab["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.tab["border_bottom"]))

        if self.data.tab["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.tab["border_left"]))

        if self.data.tab["border_radius"] != 0 and self.data.tab["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.tab["border_radius"]))

        if self.data.tab["padding_top_value"] != 0 and self.data.tab["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab["padding_top_value"], self.data.tab["padding_top_type"]))

        if self.data.tab["padding_right_value"] != 0 and self.data.tab["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.tab["padding_right_value"], self.data.tab["padding_right_type"]))

        if self.data.tab["padding_bottom_value"] != 0 and self.data.tab["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.tab["padding_bottom_value"], self.data.tab["padding_bottom_type"]))

        if self.data.tab["padding_left_value"] != 0 and self.data.tab["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.tab["padding_left_value"], self.data.tab["padding_left_type"]))


        if self.data.tab["margin_top_value"] != 0 and self.data.tab["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab["margin_top_value"], self.data.tab["margin_top_type"]))

        if self.data.tab["margin_right_value"] != 0 and self.data.tab["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.tab["margin_right_value"], self.data.tab["margin_right_type"]))

        if self.data.tab["margin_bottom_value"] != 0 and self.data.tab["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.tab["margin_bottom_value"], self.data.tab["margin_bottom_type"]))

        if self.data.tab["margin_left_value"] != 0 and self.data.tab["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.tab["margin_left_value"], self.data.tab["margin_left_type"]))


        f.write("\n}")








        f.write("\n")




        f.write("QTabBar" + "::tear {")

        if self.data.tear["color"] != "":
            f.write("\n   color: {};".format(self.data.tear["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.tear["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.tear["outline"]))

        if self.data.tear["width_value"] != 0 and self.data.tear["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.tear["width_value"], self.data.tear["width_type"]))

        if self.data.tear["height_value"] != 0 and self.data.tear["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.tear["height_value"], self.data.tear["height_type"]))

        if self.data.tear["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.tear["font_family"]))

        if self.data.tear["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.tear["font_size"]))

        if self.data.tear["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.tear["font_weight"]))

        if self.data.tear["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.tear["font_style"]))

        if self.data.tear["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.tear["line_height"]))

        if self.data.tear["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.tear["text_align"]))

        if self.data.tear["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.tear["text_decoration"]))

        if self.data.tear["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.tear["text_transform"]))

        if self.data.tear["background"] != "":
            f.write("\n   background: {};".format(self.data.tear["background"]))

        if self.data.tear["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.tear["background_image"]))

        if self.data.tear["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.tear["background_color"]))

        if self.data.tear["border"] != "":
            f.write("\n   border: {};".format(self.data.tear["border"]))

        if self.data.tear["border_width_value"] != 0 and self.data.tear["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.tear["border_width_value"], self.data.tear["border_width_type"]))

        if self.data.tear["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.tear["border_style"]))

        if self.data.tear["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.tear["border_color"]))

        if self.data.tear["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.tear["border_top"]))

        if self.data.tear["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.tear["border_right"]))

        if self.data.tear["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.tear["border_bottom"]))

        if self.data.tear["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.tear["border_left"]))

        if self.data.tear["border_radius"] != 0 and self.data.tear["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.tear["border_radius"]))

        if self.data.tear["padding_top_value"] != 0 and self.data.tear["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tear["padding_top_value"], self.data.tear["padding_top_type"]))

        if self.data.tear["padding_right_value"] != 0 and self.data.tear["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.tear["padding_right_value"], self.data.tear["padding_right_type"]))

        if self.data.tear["padding_bottom_value"] != 0 and self.data.tear["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.tear["padding_bottom_value"], self.data.tear["padding_bottom_type"]))

        if self.data.tear["padding_left_value"] != 0 and self.data.tear["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.tear["padding_left_value"], self.data.tear["padding_left_type"]))


        if self.data.tear["margin_top_value"] != 0 and self.data.tear["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tear["margin_top_value"], self.data.tear["margin_top_type"]))

        if self.data.tear["margin_right_value"] != 0 and self.data.tear["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.tear["margin_right_value"], self.data.tear["margin_right_type"]))

        if self.data.tear["margin_bottom_value"] != 0 and self.data.tear["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.tear["margin_bottom_value"], self.data.tear["margin_bottom_type"]))

        if self.data.tear["margin_left_value"] != 0 and self.data.tear["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.tear["margin_left_value"], self.data.tear["margin_left_type"]))


        f.write("\n}")







        f.write("\n")




        f.write("QTabBar" + "::scroller {")

        if self.data.scroller["color"] != "":
            f.write("\n   color: {};".format(self.data.scroller["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.scroller["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.scroller["outline"]))

        if self.data.scroller["width_value"] != 0 and self.data.scroller["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.scroller["width_value"], self.data.scroller["width_type"]))

        if self.data.scroller["height_value"] != 0 and self.data.scroller["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.scroller["height_value"], self.data.scroller["height_type"]))

        if self.data.scroller["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.scroller["font_family"]))

        if self.data.scroller["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.scroller["font_size"]))

        if self.data.scroller["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.scroller["font_weight"]))

        if self.data.scroller["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.scroller["font_style"]))

        if self.data.scroller["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.scroller["line_height"]))

        if self.data.scroller["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.scroller["text_align"]))

        if self.data.scroller["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.scroller["text_decoration"]))

        if self.data.scroller["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.scroller["text_transform"]))

        if self.data.scroller["background"] != "":
            f.write("\n   background: {};".format(self.data.scroller["background"]))

        if self.data.scroller["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.scroller["background_image"]))

        if self.data.scroller["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.scroller["background_color"]))

        if self.data.scroller["border"] != "":
            f.write("\n   border: {};".format(self.data.scroller["border"]))

        if self.data.scroller["border_width_value"] != 0 and self.data.scroller["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.scroller["border_width_value"], self.data.scroller["border_width_type"]))

        if self.data.scroller["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.scroller["border_style"]))

        if self.data.scroller["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.scroller["border_color"]))

        if self.data.scroller["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.scroller["border_top"]))

        if self.data.scroller["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.scroller["border_right"]))

        if self.data.scroller["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.scroller["border_bottom"]))

        if self.data.scroller["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.scroller["border_left"]))

        if self.data.scroller["border_radius"] != 0 and self.data.scroller["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.scroller["border_radius"]))

        if self.data.scroller["padding_top_value"] != 0 and self.data.scroller["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.scroller["padding_top_value"], self.data.scroller["padding_top_type"]))

        if self.data.scroller["padding_right_value"] != 0 and self.data.scroller["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.scroller["padding_right_value"], self.data.scroller["padding_right_type"]))

        if self.data.scroller["padding_bottom_value"] != 0 and self.data.scroller["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.scroller["padding_bottom_value"], self.data.scroller["padding_bottom_type"]))

        if self.data.scroller["padding_left_value"] != 0 and self.data.scroller["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.scroller["padding_left_value"], self.data.scroller["padding_left_type"]))


        if self.data.scroller["margin_top_value"] != 0 and self.data.scroller["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.scroller["margin_top_value"], self.data.scroller["margin_top_type"]))

        if self.data.scroller["margin_right_value"] != 0 and self.data.scroller["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.scroller["margin_right_value"], self.data.scroller["margin_right_type"]))

        if self.data.scroller["margin_bottom_value"] != 0 and self.data.scroller["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.scroller["margin_bottom_value"], self.data.scroller["margin_bottom_type"]))

        if self.data.scroller["margin_left_value"] != 0 and self.data.scroller["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.scroller["margin_left_value"], self.data.scroller["margin_left_type"]))


        f.write("\n}")






        f.write("\n")




        f.write("QTabBar" + "::tab:hover {")

        if self.data.tab_hover["color"] != "":
            f.write("\n   color: {};".format(self.data.tab_hover["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.tab_hover["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.tab_hover["outline"]))

        if self.data.tab_hover["width_value"] != 0 and self.data.tab_hover["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.tab_hover["width_value"], self.data.tab_hover["width_type"]))

        if self.data.tab_hover["height_value"] != 0 and self.data.tab_hover["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.tab_hover["height_value"], self.data.tab_hover["height_type"]))

        if self.data.tab_hover["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.tab_hover["font_family"]))

        if self.data.tab_hover["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.tab_hover["font_size"]))

        if self.data.tab_hover["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.tab_hover["font_weight"]))

        if self.data.tab_hover["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.tab_hover["font_style"]))

        if self.data.tab_hover["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.tab_hover["line_height"]))

        if self.data.tab_hover["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.tab_hover["text_align"]))

        if self.data.tab_hover["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.tab_hover["text_decoration"]))

        if self.data.tab_hover["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.tab_hover["text_transform"]))

        if self.data.tab_hover["background"] != "":
            f.write("\n   background: {};".format(self.data.tab_hover["background"]))

        if self.data.tab_hover["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.tab_hover["background_image"]))

        if self.data.tab_hover["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.tab_hover["background_color"]))

        if self.data.tab_hover["border"] != "":
            f.write("\n   border: {};".format(self.data.tab_hover["border"]))

        if self.data.tab_hover["border_width_value"] != 0 and self.data.tab_hover["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.tab_hover["border_width_value"], self.data.tab_hover["border_width_type"]))

        if self.data.tab_hover["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.tab_hover["border_style"]))

        if self.data.tab_hover["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.tab_hover["border_color"]))

        if self.data.tab_hover["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.tab_hover["border_top"]))

        if self.data.tab_hover["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.tab_hover["border_right"]))

        if self.data.tab_hover["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.tab_hover["border_bottom"]))

        if self.data.tab_hover["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.tab_hover["border_left"]))

        if self.data.tab_hover["border_radius"] != 0 and self.data.tab_hover["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.tab_hover["border_radius"]))

        if self.data.tab_hover["padding_top_value"] != 0 and self.data.tab_hover["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_hover["padding_top_value"], self.data.tab_hover["padding_top_type"]))

        if self.data.tab_hover["padding_right_value"] != 0 and self.data.tab_hover["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.tab_hover["padding_right_value"], self.data.tab_hover["padding_right_type"]))

        if self.data.tab_hover["padding_bottom_value"] != 0 and self.data.tab_hover["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.tab_hover["padding_bottom_value"], self.data.tab_hover["padding_bottom_type"]))

        if self.data.tab_hover["padding_left_value"] != 0 and self.data.tab_hover["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.tab_hover["padding_left_value"], self.data.tab_hover["padding_left_type"]))


        if self.data.tab_hover["margin_top_value"] != 0 and self.data.tab_hover["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_hover["margin_top_value"], self.data.tab_hover["margin_top_type"]))

        if self.data.tab_hover["margin_right_value"] != 0 and self.data.tab_hover["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.tab_hover["margin_right_value"], self.data.tab_hover["margin_right_type"]))

        if self.data.tab_hover["margin_bottom_value"] != 0 and self.data.tab_hover["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.tab_hover["margin_bottom_value"], self.data.tab_hover["margin_bottom_type"]))

        if self.data.tab_hover["margin_left_value"] != 0 and self.data.tab_hover["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.tab_hover["margin_left_value"], self.data.tab_hover["margin_left_type"]))


        f.write("\n}")








        f.write("\n")




        f.write("QTabBar" + "::tab:selected {")

        if self.data.tab_selected["color"] != "":
            f.write("\n   color: {};".format(self.data.tab_selected["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.tab_selected["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.tab_selected["outline"]))

        if self.data.tab_selected["width_value"] != 0 and self.data.tab_selected["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.tab_selected["width_value"], self.data.tab_selected["width_type"]))

        if self.data.tab_selected["height_value"] != 0 and self.data.tab_selected["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.tab_selected["height_value"], self.data.tab_selected["height_type"]))

        if self.data.tab_selected["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.tab_selected["font_family"]))

        if self.data.tab_selected["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.tab_selected["font_size"]))

        if self.data.tab_selected["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.tab_selected["font_weight"]))

        if self.data.tab_selected["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.tab_selected["font_style"]))

        if self.data.tab_selected["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.tab_selected["line_height"]))

        if self.data.tab_selected["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.tab_selected["text_align"]))

        if self.data.tab_selected["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.tab_selected["text_decoration"]))

        if self.data.tab_selected["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.tab_selected["text_transform"]))

        if self.data.tab_selected["background"] != "":
            f.write("\n   background: {};".format(self.data.tab_selected["background"]))

        if self.data.tab_selected["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.tab_selected["background_image"]))

        if self.data.tab_selected["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.tab_selected["background_color"]))

        if self.data.tab_selected["border"] != "":
            f.write("\n   border: {};".format(self.data.tab_selected["border"]))

        if self.data.tab_selected["border_width_value"] != 0 and self.data.tab_selected["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.tab_selected["border_width_value"], self.data.tab_selected["border_width_type"]))

        if self.data.tab_selected["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.tab_selected["border_style"]))

        if self.data.tab_selected["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.tab_selected["border_color"]))

        if self.data.tab_selected["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.tab_selected["border_top"]))

        if self.data.tab_selected["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.tab_selected["border_right"]))

        if self.data.tab_selected["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.tab_selected["border_bottom"]))

        if self.data.tab_selected["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.tab_selected["border_left"]))

        if self.data.tab_selected["border_radius"] != 0 and self.data.tab_selected["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.tab_selected["border_radius"]))

        if self.data.tab_selected["padding_top_value"] != 0 and self.data.tab_selected["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_selected["padding_top_value"], self.data.tab_selected["padding_top_type"]))

        if self.data.tab_selected["padding_right_value"] != 0 and self.data.tab_selected["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.tab_selected["padding_right_value"], self.data.tab_selected["padding_right_type"]))

        if self.data.tab_selected["padding_bottom_value"] != 0 and self.data.tab_selected["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.tab_selected["padding_bottom_value"], self.data.tab_selected["padding_bottom_type"]))

        if self.data.tab_selected["padding_left_value"] != 0 and self.data.tab_selected["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.tab_selected["padding_left_value"], self.data.tab_selected["padding_left_type"]))


        if self.data.tab_selected["margin_top_value"] != 0 and self.data.tab_selected["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_selected["margin_top_value"], self.data.tab_selected["margin_top_type"]))

        if self.data.tab_selected["margin_right_value"] != 0 and self.data.tab_selected["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.tab_selected["margin_right_value"], self.data.tab_selected["margin_right_type"]))

        if self.data.tab_selected["margin_bottom_value"] != 0 and self.data.tab_selected["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.tab_selected["margin_bottom_value"], self.data.tab_selected["margin_bottom_type"]))

        if self.data.tab_selected["margin_left_value"] != 0 and self.data.tab_selected["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.tab_selected["margin_left_value"], self.data.tab_selected["margin_left_type"]))


        f.write("\n}")






        f.write("\n")




        f.write("QTabBar" + "::tab:!selected {")

        if self.data.tab_u_selected["color"] != "":
            f.write("\n   color: {};".format(self.data.tab_u_selected["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.tab_u_selected["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.tab_u_selected["outline"]))

        if self.data.tab_u_selected["width_value"] != 0 and self.data.tab_u_selected["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.tab_u_selected["width_value"], self.data.tab_u_selected["width_type"]))

        if self.data.tab_u_selected["height_value"] != 0 and self.data.tab_u_selected["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.tab_u_selected["height_value"], self.data.tab_u_selected["height_type"]))

        if self.data.tab_u_selected["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.tab_u_selected["font_family"]))

        if self.data.tab_u_selected["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.tab_u_selected["font_size"]))

        if self.data.tab_u_selected["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.tab_u_selected["font_weight"]))

        if self.data.tab_u_selected["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.tab_u_selected["font_style"]))

        if self.data.tab_u_selected["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.tab_u_selected["line_height"]))

        if self.data.tab_u_selected["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.tab_u_selected["text_align"]))

        if self.data.tab_u_selected["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.tab_u_selected["text_decoration"]))

        if self.data.tab_u_selected["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.tab_u_selected["text_transform"]))

        if self.data.tab_u_selected["background"] != "":
            f.write("\n   background: {};".format(self.data.tab_u_selected["background"]))

        if self.data.tab_u_selected["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.tab_u_selected["background_image"]))

        if self.data.tab_u_selected["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.tab_u_selected["background_color"]))

        if self.data.tab_u_selected["border"] != "":
            f.write("\n   border: {};".format(self.data.tab_u_selected["border"]))

        if self.data.tab_u_selected["border_width_value"] != 0 and self.data.tab_u_selected["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.tab_u_selected["border_width_value"], self.data.tab_u_selected["border_width_type"]))

        if self.data.tab_u_selected["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.tab_u_selected["border_style"]))

        if self.data.tab_u_selected["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.tab_u_selected["border_color"]))

        if self.data.tab_u_selected["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.tab_u_selected["border_top"]))

        if self.data.tab_u_selected["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.tab_u_selected["border_right"]))

        if self.data.tab_u_selected["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.tab_u_selected["border_bottom"]))

        if self.data.tab_u_selected["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.tab_u_selected["border_left"]))

        if self.data.tab_u_selected["border_radius"] != 0 and self.data.tab_u_selected["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.tab_u_selected["border_radius"]))

        if self.data.tab_u_selected["padding_top_value"] != 0 and self.data.tab_u_selected["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_u_selected["padding_top_value"], self.data.tab_u_selected["padding_top_type"]))

        if self.data.tab_u_selected["padding_right_value"] != 0 and self.data.tab_u_selected["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.tab_u_selected["padding_right_value"], self.data.tab_u_selected["padding_right_type"]))

        if self.data.tab_u_selected["padding_bottom_value"] != 0 and self.data.tab_u_selected["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.tab_u_selected["padding_bottom_value"], self.data.tab_u_selected["padding_bottom_type"]))

        if self.data.tab_u_selected["padding_left_value"] != 0 and self.data.tab_u_selected["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.tab_u_selected["padding_left_value"], self.data.tab_u_selected["padding_left_type"]))


        if self.data.tab_u_selected["margin_top_value"] != 0 and self.data.tab_u_selected["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_u_selected["margin_top_value"], self.data.tab_u_selected["margin_top_type"]))

        if self.data.tab_u_selected["margin_right_value"] != 0 and self.data.tab_u_selected["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.tab_u_selected["margin_right_value"], self.data.tab_u_selected["margin_right_type"]))

        if self.data.tab_u_selected["margin_bottom_value"] != 0 and self.data.tab_u_selected["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.tab_u_selected["margin_bottom_value"], self.data.tab_u_selected["margin_bottom_type"]))

        if self.data.tab_u_selected["margin_left_value"] != 0 and self.data.tab_u_selected["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.tab_u_selected["margin_left_value"], self.data.tab_u_selected["margin_left_type"]))


        f.write("\n}")







        f.write("\n")




        f.write("QTabBar" + "::tab:!selected:hover {")

        if self.data.tab_u_selected_hover["color"] != "":
            f.write("\n   color: {};".format(self.data.tab_u_selected_hover["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.tab_u_selected_hover["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.tab_u_selected_hover["outline"]))

        if self.data.tab_u_selected_hover["width_value"] != 0 and self.data.tab_u_selected_hover["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.tab_u_selected_hover["width_value"], self.data.tab_u_selected_hover["width_type"]))

        if self.data.tab_u_selected_hover["height_value"] != 0 and self.data.tab_u_selected_hover["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.tab_u_selected_hover["height_value"], self.data.tab_u_selected_hover["height_type"]))

        if self.data.tab_u_selected_hover["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.tab_u_selected_hover["font_family"]))

        if self.data.tab_u_selected_hover["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.tab_u_selected_hover["font_size"]))

        if self.data.tab_u_selected_hover["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.tab_u_selected_hover["font_weight"]))

        if self.data.tab_u_selected_hover["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.tab_u_selected_hover["font_style"]))

        if self.data.tab_u_selected_hover["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.tab_u_selected_hover["line_height"]))

        if self.data.tab_u_selected_hover["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.tab_u_selected_hover["text_align"]))

        if self.data.tab_u_selected_hover["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.tab_u_selected_hover["text_decoration"]))

        if self.data.tab_u_selected_hover["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.tab_u_selected_hover["text_transform"]))

        if self.data.tab_u_selected_hover["background"] != "":
            f.write("\n   background: {};".format(self.data.tab_u_selected_hover["background"]))

        if self.data.tab_u_selected_hover["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.tab_u_selected_hover["background_image"]))

        if self.data.tab_u_selected_hover["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.tab_u_selected_hover["background_color"]))

        if self.data.tab_u_selected_hover["border"] != "":
            f.write("\n   border: {};".format(self.data.tab_u_selected_hover["border"]))

        if self.data.tab_u_selected_hover["border_width_value"] != 0 and self.data.tab_u_selected_hover["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.tab_u_selected_hover["border_width_value"], self.data.tab_u_selected_hover["border_width_type"]))

        if self.data.tab_u_selected_hover["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.tab_u_selected_hover["border_style"]))

        if self.data.tab_u_selected_hover["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.tab_u_selected_hover["border_color"]))

        if self.data.tab_u_selected_hover["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.tab_u_selected_hover["border_top"]))

        if self.data.tab_u_selected_hover["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.tab_u_selected_hover["border_right"]))

        if self.data.tab_u_selected_hover["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.tab_u_selected_hover["border_bottom"]))

        if self.data.tab_u_selected_hover["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.tab_u_selected_hover["border_left"]))

        if self.data.tab_u_selected_hover["border_radius"] != 0 and self.data.tab_u_selected_hover["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.tab_u_selected_hover["border_radius"]))

        if self.data.tab_u_selected_hover["padding_top_value"] != 0 and self.data.tab_u_selected_hover["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_u_selected_hover["padding_top_value"], self.data.tab_u_selected_hover["padding_top_type"]))

        if self.data.tab_u_selected_hover["padding_right_value"] != 0 and self.data.tab_u_selected_hover["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.tab_u_selected_hover["padding_right_value"], self.data.tab_u_selected_hover["padding_right_type"]))

        if self.data.tab_u_selected_hover["padding_bottom_value"] != 0 and self.data.tab_u_selected_hover["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.tab_u_selected_hover["padding_bottom_value"], self.data.tab_u_selected_hover["padding_bottom_type"]))

        if self.data.tab_u_selected_hover["padding_left_value"] != 0 and self.data.tab_u_selected_hover["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.tab_u_selected_hover["padding_left_value"], self.data.tab_u_selected_hover["padding_left_type"]))


        if self.data.tab_u_selected_hover["margin_top_value"] != 0 and self.data.tab_u_selected_hover["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_u_selected_hover["margin_top_value"], self.data.tab_u_selected_hover["margin_top_type"]))

        if self.data.tab_u_selected_hover["margin_right_value"] != 0 and self.data.tab_u_selected_hover["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.tab_u_selected_hover["margin_right_value"], self.data.tab_u_selected_hover["margin_right_type"]))

        if self.data.tab_u_selected_hover["margin_bottom_value"] != 0 and self.data.tab_u_selected_hover["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.tab_u_selected_hover["margin_bottom_value"], self.data.tab_u_selected_hover["margin_bottom_type"]))

        if self.data.tab_u_selected_hover["margin_left_value"] != 0 and self.data.tab_u_selected_hover["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.tab_u_selected_hover["margin_left_value"], self.data.tab_u_selected_hover["margin_left_type"]))


        f.write("\n}")




        f.write("\n")




        f.write("QTabBar" + "::tab:first {")

        if self.data.tab_first["color"] != "":
            f.write("\n   color: {};".format(self.data.tab_first["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.tab_first["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.tab_first["outline"]))

        if self.data.tab_first["width_value"] != 0 and self.data.tab_first["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.tab_first["width_value"], self.data.tab_first["width_type"]))

        if self.data.tab_first["height_value"] != 0 and self.data.tab_first["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.tab_first["height_value"], self.data.tab_first["height_type"]))

        if self.data.tab_first["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.tab_first["font_family"]))

        if self.data.tab_first["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.tab_first["font_size"]))

        if self.data.tab_first["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.tab_first["font_weight"]))

        if self.data.tab_first["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.tab_first["font_style"]))

        if self.data.tab_first["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.tab_first["line_height"]))

        if self.data.tab_first["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.tab_first["text_align"]))

        if self.data.tab_first["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.tab_first["text_decoration"]))

        if self.data.tab_first["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.tab_first["text_transform"]))

        if self.data.tab_first["background"] != "":
            f.write("\n   background: {};".format(self.data.tab_first["background"]))

        if self.data.tab_first["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.tab_first["background_image"]))

        if self.data.tab_first["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.tab_first["background_color"]))

        if self.data.tab_first["border"] != "":
            f.write("\n   border: {};".format(self.data.tab_first["border"]))

        if self.data.tab_first["border_width_value"] != 0 and self.data.tab_first["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.tab_first["border_width_value"], self.data.tab_first["border_width_type"]))

        if self.data.tab_first["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.tab_first["border_style"]))

        if self.data.tab_first["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.tab_first["border_color"]))

        if self.data.tab_first["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.tab_first["border_top"]))

        if self.data.tab_first["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.tab_first["border_right"]))

        if self.data.tab_first["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.tab_first["border_bottom"]))

        if self.data.tab_first["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.tab_first["border_left"]))

        if self.data.tab_first["border_radius"] != 0 and self.data.tab_first["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.tab_first["border_radius"]))

        if self.data.tab_first["padding_top_value"] != 0 and self.data.tab_first["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_first["padding_top_value"], self.data.tab_first["padding_top_type"]))

        if self.data.tab_first["padding_right_value"] != 0 and self.data.tab_first["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.tab_first["padding_right_value"], self.data.tab_first["padding_right_type"]))

        if self.data.tab_first["padding_bottom_value"] != 0 and self.data.tab_first["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.tab_first["padding_bottom_value"], self.data.tab_first["padding_bottom_type"]))

        if self.data.tab_first["padding_left_value"] != 0 and self.data.tab_first["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.tab_first["padding_left_value"], self.data.tab_first["padding_left_type"]))


        if self.data.tab_first["margin_top_value"] != 0 and self.data.tab_first["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_first["margin_top_value"], self.data.tab_first["margin_top_type"]))

        if self.data.tab_first["margin_right_value"] != 0 and self.data.tab_first["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.tab_first["margin_right_value"], self.data.tab_first["margin_right_type"]))

        if self.data.tab_first["margin_bottom_value"] != 0 and self.data.tab_first["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.tab_first["margin_bottom_value"], self.data.tab_first["margin_bottom_type"]))

        if self.data.tab_first["margin_left_value"] != 0 and self.data.tab_first["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.tab_first["margin_left_value"], self.data.tab_first["margin_left_type"]))


        f.write("\n}")







        f.write("\n")




        f.write("QTabBar" + "::tab:first:selected {")

        if self.data.tab_first_selected["color"] != "":
            f.write("\n   color: {};".format(self.data.tab_first_selected["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.tab_first_selected["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.tab_first_selected["outline"]))

        if self.data.tab_first_selected["width_value"] != 0 and self.data.tab_first_selected["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.tab_first_selected["width_value"], self.data.tab_first_selected["width_type"]))

        if self.data.tab_first_selected["height_value"] != 0 and self.data.tab_first_selected["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.tab_first_selected["height_value"], self.data.tab_first_selected["height_type"]))

        if self.data.tab_first_selected["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.tab_first_selected["font_family"]))

        if self.data.tab_first_selected["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.tab_first_selected["font_size"]))

        if self.data.tab_first_selected["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.tab_first_selected["font_weight"]))

        if self.data.tab_first_selected["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.tab_first_selected["font_style"]))

        if self.data.tab_first_selected["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.tab_first_selected["line_height"]))

        if self.data.tab_first_selected["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.tab_first_selected["text_align"]))

        if self.data.tab_first_selected["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.tab_first_selected["text_decoration"]))

        if self.data.tab_first_selected["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.tab_first_selected["text_transform"]))

        if self.data.tab_first_selected["background"] != "":
            f.write("\n   background: {};".format(self.data.tab_first_selected["background"]))

        if self.data.tab_first_selected["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.tab_first_selected["background_image"]))

        if self.data.tab_first_selected["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.tab_first_selected["background_color"]))

        if self.data.tab_first_selected["border"] != "":
            f.write("\n   border: {};".format(self.data.tab_first_selected["border"]))

        if self.data.tab_first_selected["border_width_value"] != 0 and self.data.tab_first_selected["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.tab_first_selected["border_width_value"], self.data.tab_first_selected["border_width_type"]))

        if self.data.tab_first_selected["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.tab_first_selected["border_style"]))

        if self.data.tab_first_selected["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.tab_first_selected["border_color"]))

        if self.data.tab_first_selected["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.tab_first_selected["border_top"]))

        if self.data.tab_first_selected["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.tab_first_selected["border_right"]))

        if self.data.tab_first_selected["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.tab_first_selected["border_bottom"]))

        if self.data.tab_first_selected["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.tab_first_selected["border_left"]))

        if self.data.tab_first_selected["border_radius"] != 0 and self.data.tab_first_selected["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.tab_first_selected["border_radius"]))

        if self.data.tab_first_selected["padding_top_value"] != 0 and self.data.tab_first_selected["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_first_selected["padding_top_value"], self.data.tab_first_selected["padding_top_type"]))

        if self.data.tab_first_selected["padding_right_value"] != 0 and self.data.tab_first_selected["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.tab_first_selected["padding_right_value"], self.data.tab_first_selected["padding_right_type"]))

        if self.data.tab_first_selected["padding_bottom_value"] != 0 and self.data.tab_first_selected["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.tab_first_selected["padding_bottom_value"], self.data.tab_first_selected["padding_bottom_type"]))

        if self.data.tab_first_selected["padding_left_value"] != 0 and self.data.tab_first_selected["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.tab_first_selected["padding_left_value"], self.data.tab_first_selected["padding_left_type"]))


        if self.data.tab_first_selected["margin_top_value"] != 0 and self.data.tab_first_selected["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_first_selected["margin_top_value"], self.data.tab_first_selected["margin_top_type"]))

        if self.data.tab_first_selected["margin_right_value"] != 0 and self.data.tab_first_selected["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.tab_first_selected["margin_right_value"], self.data.tab_first_selected["margin_right_type"]))

        if self.data.tab_first_selected["margin_bottom_value"] != 0 and self.data.tab_first_selected["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.tab_first_selected["margin_bottom_value"], self.data.tab_first_selected["margin_bottom_type"]))

        if self.data.tab_first_selected["margin_left_value"] != 0 and self.data.tab_first_selected["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.tab_first_selected["margin_left_value"], self.data.tab_first_selected["margin_left_type"]))


        f.write("\n}")




        f.write("\n")




        f.write("QTabBar" + "::tab:last {")

        if self.data.tab_last["color"] != "":
            f.write("\n   color: {};".format(self.data.tab_last["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.tab_last["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.tab_last["outline"]))

        if self.data.tab_last["width_value"] != 0 and self.data.tab_last["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.tab_last["width_value"], self.data.tab_last["width_type"]))

        if self.data.tab_last["height_value"] != 0 and self.data.tab_last["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.tab_last["height_value"], self.data.tab_last["height_type"]))

        if self.data.tab_last["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.tab_last["font_family"]))

        if self.data.tab_last["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.tab_last["font_size"]))

        if self.data.tab_last["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.tab_last["font_weight"]))

        if self.data.tab_last["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.tab_last["font_style"]))

        if self.data.tab_last["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.tab_last["line_height"]))

        if self.data.tab_last["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.tab_last["text_align"]))

        if self.data.tab_last["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.tab_last["text_decoration"]))

        if self.data.tab_last["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.tab_last["text_transform"]))

        if self.data.tab_last["background"] != "":
            f.write("\n   background: {};".format(self.data.tab_last["background"]))

        if self.data.tab_last["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.tab_last["background_image"]))

        if self.data.tab_last["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.tab_last["background_color"]))

        if self.data.tab_last["border"] != "":
            f.write("\n   border: {};".format(self.data.tab_last["border"]))

        if self.data.tab_last["border_width_value"] != 0 and self.data.tab_last["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.tab_last["border_width_value"], self.data.tab_last["border_width_type"]))

        if self.data.tab_last["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.tab_last["border_style"]))

        if self.data.tab_last["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.tab_last["border_color"]))

        if self.data.tab_last["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.tab_last["border_top"]))

        if self.data.tab_last["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.tab_last["border_right"]))

        if self.data.tab_last["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.tab_last["border_bottom"]))

        if self.data.tab_last["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.tab_last["border_left"]))

        if self.data.tab_last["border_radius"] != 0 and self.data.tab_last["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.tab_last["border_radius"]))

        if self.data.tab_last["padding_top_value"] != 0 and self.data.tab_last["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_last["padding_top_value"], self.data.tab_last["padding_top_type"]))

        if self.data.tab_last["padding_right_value"] != 0 and self.data.tab_last["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.tab_last["padding_right_value"], self.data.tab_last["padding_right_type"]))

        if self.data.tab_last["padding_bottom_value"] != 0 and self.data.tab_last["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.tab_last["padding_bottom_value"], self.data.tab_last["padding_bottom_type"]))

        if self.data.tab_last["padding_left_value"] != 0 and self.data.tab_last["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.tab_last["padding_left_value"], self.data.tab_last["padding_left_type"]))


        if self.data.tab_last["margin_top_value"] != 0 and self.data.tab_last["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_last["margin_top_value"], self.data.tab_last["margin_top_type"]))

        if self.data.tab_last["margin_right_value"] != 0 and self.data.tab_last["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.tab_last["margin_right_value"], self.data.tab_last["margin_right_type"]))

        if self.data.tab_last["margin_bottom_value"] != 0 and self.data.tab_last["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.tab_last["margin_bottom_value"], self.data.tab_last["margin_bottom_type"]))

        if self.data.tab_last["margin_left_value"] != 0 and self.data.tab_last["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.tab_last["margin_left_value"], self.data.tab_last["margin_left_type"]))


        f.write("\n}")








        f.write("\n")




        f.write("QTabBar" + "::tab:last:selected {")

        if self.data.tab_last_selected["color"] != "":
            f.write("\n   color: {};".format(self.data.tab_last_selected["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.tab_last_selected["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.tab_last_selected["outline"]))

        if self.data.tab_last_selected["width_value"] != 0 and self.data.tab_last_selected["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.tab_last_selected["width_value"], self.data.tab_last_selected["width_type"]))

        if self.data.tab_last_selected["height_value"] != 0 and self.data.tab_last_selected["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.tab_last_selected["height_value"], self.data.tab_last_selected["height_type"]))

        if self.data.tab_last_selected["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.tab_last_selected["font_family"]))

        if self.data.tab_last_selected["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.tab_last_selected["font_size"]))

        if self.data.tab_last_selected["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.tab_last_selected["font_weight"]))

        if self.data.tab_last_selected["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.tab_last_selected["font_style"]))

        if self.data.tab_last_selected["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.tab_last_selected["line_height"]))

        if self.data.tab_last_selected["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.tab_last_selected["text_align"]))

        if self.data.tab_last_selected["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.tab_last_selected["text_decoration"]))

        if self.data.tab_last_selected["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.tab_last_selected["text_transform"]))

        if self.data.tab_last_selected["background"] != "":
            f.write("\n   background: {};".format(self.data.tab_last_selected["background"]))

        if self.data.tab_last_selected["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.tab_last_selected["background_image"]))

        if self.data.tab_last_selected["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.tab_last_selected["background_color"]))

        if self.data.tab_last_selected["border"] != "":
            f.write("\n   border: {};".format(self.data.tab_last_selected["border"]))

        if self.data.tab_last_selected["border_width_value"] != 0 and self.data.tab_last_selected["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.tab_last_selected["border_width_value"], self.data.tab_last_selected["border_width_type"]))

        if self.data.tab_last_selected["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.tab_last_selected["border_style"]))

        if self.data.tab_last_selected["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.tab_last_selected["border_color"]))

        if self.data.tab_last_selected["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.tab_last_selected["border_top"]))

        if self.data.tab_last_selected["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.tab_last_selected["border_right"]))

        if self.data.tab_last_selected["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.tab_last_selected["border_bottom"]))

        if self.data.tab_last_selected["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.tab_last_selected["border_left"]))

        if self.data.tab_last_selected["border_radius"] != 0 and self.data.tab_last_selected["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.tab_last_selected["border_radius"]))

        if self.data.tab_last_selected["padding_top_value"] != 0 and self.data.tab_last_selected["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_last_selected["padding_top_value"], self.data.tab_last_selected["padding_top_type"]))

        if self.data.tab_last_selected["padding_right_value"] != 0 and self.data.tab_last_selected["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.tab_last_selected["padding_right_value"], self.data.tab_last_selected["padding_right_type"]))

        if self.data.tab_last_selected["padding_bottom_value"] != 0 and self.data.tab_last_selected["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.tab_last_selected["padding_bottom_value"], self.data.tab_last_selected["padding_bottom_type"]))

        if self.data.tab_last_selected["padding_left_value"] != 0 and self.data.tab_last_selected["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.tab_last_selected["padding_left_value"], self.data.tab_last_selected["padding_left_type"]))


        if self.data.tab_last_selected["margin_top_value"] != 0 and self.data.tab_last_selected["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_last_selected["margin_top_value"], self.data.tab_last_selected["margin_top_type"]))

        if self.data.tab_last_selected["margin_right_value"] != 0 and self.data.tab_last_selected["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.tab_last_selected["margin_right_value"], self.data.tab_last_selected["margin_right_type"]))

        if self.data.tab_last_selected["margin_bottom_value"] != 0 and self.data.tab_last_selected["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.tab_last_selected["margin_bottom_value"], self.data.tab_last_selected["margin_bottom_type"]))

        if self.data.tab_last_selected["margin_left_value"] != 0 and self.data.tab_last_selected["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.tab_last_selected["margin_left_value"], self.data.tab_last_selected["margin_left_type"]))


        f.write("\n}")






        f.write("\n")




        f.write("QTabBar" + "::tab:top {")

        if self.data.tab_top["color"] != "":
            f.write("\n   color: {};".format(self.data.tab_top["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.tab_top["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.tab_top["outline"]))

        if self.data.tab_top["width_value"] != 0 and self.data.tab_top["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.tab_top["width_value"], self.data.tab_top["width_type"]))

        if self.data.tab_top["height_value"] != 0 and self.data.tab_top["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.tab_top["height_value"], self.data.tab_top["height_type"]))

        if self.data.tab_top["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.tab_top["font_family"]))

        if self.data.tab_top["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.tab_top["font_size"]))

        if self.data.tab_top["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.tab_top["font_weight"]))

        if self.data.tab_top["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.tab_top["font_style"]))

        if self.data.tab_top["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.tab_top["line_height"]))

        if self.data.tab_top["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.tab_top["text_align"]))

        if self.data.tab_top["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.tab_top["text_decoration"]))

        if self.data.tab_top["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.tab_top["text_transform"]))

        if self.data.tab_top["background"] != "":
            f.write("\n   background: {};".format(self.data.tab_top["background"]))

        if self.data.tab_top["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.tab_top["background_image"]))

        if self.data.tab_top["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.tab_top["background_color"]))

        if self.data.tab_top["border"] != "":
            f.write("\n   border: {};".format(self.data.tab_top["border"]))

        if self.data.tab_top["border_width_value"] != 0 and self.data.tab_top["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.tab_top["border_width_value"], self.data.tab_top["border_width_type"]))

        if self.data.tab_top["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.tab_top["border_style"]))

        if self.data.tab_top["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.tab_top["border_color"]))

        if self.data.tab_top["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.tab_top["border_top"]))

        if self.data.tab_top["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.tab_top["border_right"]))

        if self.data.tab_top["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.tab_top["border_bottom"]))

        if self.data.tab_top["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.tab_top["border_left"]))

        if self.data.tab_top["border_radius"] != 0 and self.data.tab_top["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.tab_top["border_radius"]))

        if self.data.tab_top["padding_top_value"] != 0 and self.data.tab_top["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_top["padding_top_value"], self.data.tab_top["padding_top_type"]))

        if self.data.tab_top["padding_right_value"] != 0 and self.data.tab_top["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.tab_top["padding_right_value"], self.data.tab_top["padding_right_type"]))

        if self.data.tab_top["padding_bottom_value"] != 0 and self.data.tab_top["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.tab_top["padding_bottom_value"], self.data.tab_top["padding_bottom_type"]))

        if self.data.tab_top["padding_left_value"] != 0 and self.data.tab_top["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.tab_top["padding_left_value"], self.data.tab_top["padding_left_type"]))


        if self.data.tab_top["margin_top_value"] != 0 and self.data.tab_top["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_top["margin_top_value"], self.data.tab_top["margin_top_type"]))

        if self.data.tab_top["margin_right_value"] != 0 and self.data.tab_top["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.tab_top["margin_right_value"], self.data.tab_top["margin_right_type"]))

        if self.data.tab_top["margin_bottom_value"] != 0 and self.data.tab_top["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.tab_top["margin_bottom_value"], self.data.tab_top["margin_bottom_type"]))

        if self.data.tab_top["margin_left_value"] != 0 and self.data.tab_top["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.tab_top["margin_left_value"], self.data.tab_top["margin_left_type"]))


        f.write("\n}")




        f.write("\n")




        f.write("QTabBar" + "::tab:top:selected {")

        if self.data.tab_top_selected["color"] != "":
            f.write("\n   color: {};".format(self.data.tab_top_selected["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.tab_top_selected["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.tab_top_selected["outline"]))

        if self.data.tab_top_selected["width_value"] != 0 and self.data.tab_top_selected["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.tab_top_selected["width_value"], self.data.tab_top_selected["width_type"]))

        if self.data.tab_top_selected["height_value"] != 0 and self.data.tab_top_selected["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.tab_top_selected["height_value"], self.data.tab_top_selected["height_type"]))

        if self.data.tab_top_selected["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.tab_top_selected["font_family"]))

        if self.data.tab_top_selected["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.tab_top_selected["font_size"]))

        if self.data.tab_top_selected["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.tab_top_selected["font_weight"]))

        if self.data.tab_top_selected["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.tab_top_selected["font_style"]))

        if self.data.tab_top_selected["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.tab_top_selected["line_height"]))

        if self.data.tab_top_selected["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.tab_top_selected["text_align"]))

        if self.data.tab_top_selected["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.tab_top_selected["text_decoration"]))

        if self.data.tab_top_selected["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.tab_top_selected["text_transform"]))

        if self.data.tab_top_selected["background"] != "":
            f.write("\n   background: {};".format(self.data.tab_top_selected["background"]))

        if self.data.tab_top_selected["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.tab_top_selected["background_image"]))

        if self.data.tab_top_selected["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.tab_top_selected["background_color"]))

        if self.data.tab_top_selected["border"] != "":
            f.write("\n   border: {};".format(self.data.tab_top_selected["border"]))

        if self.data.tab_top_selected["border_width_value"] != 0 and self.data.tab_top_selected["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.tab_top_selected["border_width_value"], self.data.tab_top_selected["border_width_type"]))

        if self.data.tab_top_selected["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.tab_top_selected["border_style"]))

        if self.data.tab_top_selected["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.tab_top_selected["border_color"]))

        if self.data.tab_top_selected["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.tab_top_selected["border_top"]))

        if self.data.tab_top_selected["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.tab_top_selected["border_right"]))

        if self.data.tab_top_selected["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.tab_top_selected["border_bottom"]))

        if self.data.tab_top_selected["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.tab_top_selected["border_left"]))

        if self.data.tab_top_selected["border_radius"] != 0 and self.data.tab_top_selected["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.tab_top_selected["border_radius"]))

        if self.data.tab_top_selected["padding_top_value"] != 0 and self.data.tab_top_selected["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_top_selected["padding_top_value"], self.data.tab_top_selected["padding_top_type"]))

        if self.data.tab_top_selected["padding_right_value"] != 0 and self.data.tab_top_selected["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.tab_top_selected["padding_right_value"], self.data.tab_top_selected["padding_right_type"]))

        if self.data.tab_top_selected["padding_bottom_value"] != 0 and self.data.tab_top_selected["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.tab_top_selected["padding_bottom_value"], self.data.tab_top_selected["padding_bottom_type"]))

        if self.data.tab_top_selected["padding_left_value"] != 0 and self.data.tab_top_selected["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.tab_top_selected["padding_left_value"], self.data.tab_top_selected["padding_left_type"]))


        if self.data.tab_top_selected["margin_top_value"] != 0 and self.data.tab_top_selected["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_top_selected["margin_top_value"], self.data.tab_top_selected["margin_top_type"]))

        if self.data.tab_top_selected["margin_right_value"] != 0 and self.data.tab_top_selected["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.tab_top_selected["margin_right_value"], self.data.tab_top_selected["margin_right_type"]))

        if self.data.tab_top_selected["margin_bottom_value"] != 0 and self.data.tab_top_selected["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.tab_top_selected["margin_bottom_value"], self.data.tab_top_selected["margin_bottom_type"]))

        if self.data.tab_top_selected["margin_left_value"] != 0 and self.data.tab_top_selected["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.tab_top_selected["margin_left_value"], self.data.tab_top_selected["margin_left_type"]))


        f.write("\n}")







        f.write("\n")




        f.write("QTabBar" + "::tab:top:!selected {")

        if self.data.tab_top_u_selected["color"] != "":
            f.write("\n   color: {};".format(self.data.tab_top_u_selected["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.tab_top_u_selected["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.tab_top_u_selected["outline"]))

        if self.data.tab_top_u_selected["width_value"] != 0 and self.data.tab_top_u_selected["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.tab_top_u_selected["width_value"], self.data.tab_top_u_selected["width_type"]))

        if self.data.tab_top_u_selected["height_value"] != 0 and self.data.tab_top_u_selected["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.tab_top_u_selected["height_value"], self.data.tab_top_u_selected["height_type"]))

        if self.data.tab_top_u_selected["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.tab_top_u_selected["font_family"]))

        if self.data.tab_top_u_selected["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.tab_top_u_selected["font_size"]))

        if self.data.tab_top_u_selected["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.tab_top_u_selected["font_weight"]))

        if self.data.tab_top_u_selected["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.tab_top_u_selected["font_style"]))

        if self.data.tab_top_u_selected["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.tab_top_u_selected["line_height"]))

        if self.data.tab_top_u_selected["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.tab_top_u_selected["text_align"]))

        if self.data.tab_top_u_selected["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.tab_top_u_selected["text_decoration"]))

        if self.data.tab_top_u_selected["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.tab_top_u_selected["text_transform"]))

        if self.data.tab_top_u_selected["background"] != "":
            f.write("\n   background: {};".format(self.data.tab_top_u_selected["background"]))

        if self.data.tab_top_u_selected["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.tab_top_u_selected["background_image"]))

        if self.data.tab_top_u_selected["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.tab_top_u_selected["background_color"]))

        if self.data.tab_top_u_selected["border"] != "":
            f.write("\n   border: {};".format(self.data.tab_top_u_selected["border"]))

        if self.data.tab_top_u_selected["border_width_value"] != 0 and self.data.tab_top_u_selected["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.tab_top_u_selected["border_width_value"], self.data.tab_top_u_selected["border_width_type"]))

        if self.data.tab_top_u_selected["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.tab_top_u_selected["border_style"]))

        if self.data.tab_top_u_selected["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.tab_top_u_selected["border_color"]))

        if self.data.tab_top_u_selected["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.tab_top_u_selected["border_top"]))

        if self.data.tab_top_u_selected["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.tab_top_u_selected["border_right"]))

        if self.data.tab_top_u_selected["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.tab_top_u_selected["border_bottom"]))

        if self.data.tab_top_u_selected["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.tab_top_u_selected["border_left"]))

        if self.data.tab_top_u_selected["border_radius"] != 0 and self.data.tab_top_u_selected["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.tab_top_u_selected["border_radius"]))

        if self.data.tab_top_u_selected["padding_top_value"] != 0 and self.data.tab_top_u_selected["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_top_u_selected["padding_top_value"], self.data.tab_top_u_selected["padding_top_type"]))

        if self.data.tab_top_u_selected["padding_right_value"] != 0 and self.data.tab_top_u_selected["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.tab_top_u_selected["padding_right_value"], self.data.tab_top_u_selected["padding_right_type"]))

        if self.data.tab_top_u_selected["padding_bottom_value"] != 0 and self.data.tab_top_u_selected["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.tab_top_u_selected["padding_bottom_value"], self.data.tab_top_u_selected["padding_bottom_type"]))

        if self.data.tab_top_u_selected["padding_left_value"] != 0 and self.data.tab_top_u_selected["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.tab_top_u_selected["padding_left_value"], self.data.tab_top_u_selected["padding_left_type"]))


        if self.data.tab_top_u_selected["margin_top_value"] != 0 and self.data.tab_top_u_selected["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_top_u_selected["margin_top_value"], self.data.tab_top_u_selected["margin_top_type"]))

        if self.data.tab_top_u_selected["margin_right_value"] != 0 and self.data.tab_top_u_selected["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.tab_top_u_selected["margin_right_value"], self.data.tab_top_u_selected["margin_right_type"]))

        if self.data.tab_top_u_selected["margin_bottom_value"] != 0 and self.data.tab_top_u_selected["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.tab_top_u_selected["margin_bottom_value"], self.data.tab_top_u_selected["margin_bottom_type"]))

        if self.data.tab_top_u_selected["margin_left_value"] != 0 and self.data.tab_top_u_selected["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.tab_top_u_selected["margin_left_value"], self.data.tab_top_u_selected["margin_left_type"]))


        f.write("\n}")






        f.write("\n")




        f.write("QTabBar" + "::tab:right {")

        if self.data.tab_right["color"] != "":
            f.write("\n   color: {};".format(self.data.tab_right["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.tab_right["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.tab_right["outline"]))

        if self.data.tab_right["width_value"] != 0 and self.data.tab_right["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.tab_right["width_value"], self.data.tab_right["width_type"]))

        if self.data.tab_right["height_value"] != 0 and self.data.tab_right["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.tab_right["height_value"], self.data.tab_right["height_type"]))

        if self.data.tab_right["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.tab_right["font_family"]))

        if self.data.tab_right["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.tab_right["font_size"]))

        if self.data.tab_right["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.tab_right["font_weight"]))

        if self.data.tab_right["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.tab_right["font_style"]))

        if self.data.tab_right["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.tab_right["line_height"]))

        if self.data.tab_right["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.tab_right["text_align"]))

        if self.data.tab_right["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.tab_right["text_decoration"]))

        if self.data.tab_right["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.tab_right["text_transform"]))

        if self.data.tab_right["background"] != "":
            f.write("\n   background: {};".format(self.data.tab_right["background"]))

        if self.data.tab_right["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.tab_right["background_image"]))

        if self.data.tab_right["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.tab_right["background_color"]))

        if self.data.tab_right["border"] != "":
            f.write("\n   border: {};".format(self.data.tab_right["border"]))

        if self.data.tab_right["border_width_value"] != 0 and self.data.tab_right["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.tab_right["border_width_value"], self.data.tab_right["border_width_type"]))

        if self.data.tab_right["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.tab_right["border_style"]))

        if self.data.tab_right["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.tab_right["border_color"]))

        if self.data.tab_right["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.tab_right["border_top"]))

        if self.data.tab_right["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.tab_right["border_right"]))

        if self.data.tab_right["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.tab_right["border_bottom"]))

        if self.data.tab_right["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.tab_right["border_left"]))

        if self.data.tab_right["border_radius"] != 0 and self.data.tab_right["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.tab_right["border_radius"]))

        if self.data.tab_right["padding_top_value"] != 0 and self.data.tab_right["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_right["padding_top_value"], self.data.tab_right["padding_top_type"]))

        if self.data.tab_right["padding_right_value"] != 0 and self.data.tab_right["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.tab_right["padding_right_value"], self.data.tab_right["padding_right_type"]))

        if self.data.tab_right["padding_bottom_value"] != 0 and self.data.tab_right["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.tab_right["padding_bottom_value"], self.data.tab_right["padding_bottom_type"]))

        if self.data.tab_right["padding_left_value"] != 0 and self.data.tab_right["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.tab_right["padding_left_value"], self.data.tab_right["padding_left_type"]))


        if self.data.tab_right["margin_top_value"] != 0 and self.data.tab_right["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_right["margin_top_value"], self.data.tab_right["margin_top_type"]))

        if self.data.tab_right["margin_right_value"] != 0 and self.data.tab_right["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.tab_right["margin_right_value"], self.data.tab_right["margin_right_type"]))

        if self.data.tab_right["margin_bottom_value"] != 0 and self.data.tab_right["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.tab_right["margin_bottom_value"], self.data.tab_right["margin_bottom_type"]))

        if self.data.tab_right["margin_left_value"] != 0 and self.data.tab_right["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.tab_right["margin_left_value"], self.data.tab_right["margin_left_type"]))


        f.write("\n}")




        f.write("\n")




        f.write("QTabBar" + "::tab:right:selected {")

        if self.data.tab_right_selected["color"] != "":
            f.write("\n   color: {};".format(self.data.tab_right_selected["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.tab_right_selected["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.tab_right_selected["outline"]))

        if self.data.tab_right_selected["width_value"] != 0 and self.data.tab_right_selected["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.tab_right_selected["width_value"], self.data.tab_right_selected["width_type"]))

        if self.data.tab_right_selected["height_value"] != 0 and self.data.tab_right_selected["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.tab_right_selected["height_value"], self.data.tab_right_selected["height_type"]))

        if self.data.tab_right_selected["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.tab_right_selected["font_family"]))

        if self.data.tab_right_selected["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.tab_right_selected["font_size"]))

        if self.data.tab_right_selected["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.tab_right_selected["font_weight"]))

        if self.data.tab_right_selected["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.tab_right_selected["font_style"]))

        if self.data.tab_right_selected["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.tab_right_selected["line_height"]))

        if self.data.tab_right_selected["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.tab_right_selected["text_align"]))

        if self.data.tab_right_selected["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.tab_right_selected["text_decoration"]))

        if self.data.tab_right_selected["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.tab_right_selected["text_transform"]))

        if self.data.tab_right_selected["background"] != "":
            f.write("\n   background: {};".format(self.data.tab_right_selected["background"]))

        if self.data.tab_right_selected["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.tab_right_selected["background_image"]))

        if self.data.tab_right_selected["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.tab_right_selected["background_color"]))

        if self.data.tab_right_selected["border"] != "":
            f.write("\n   border: {};".format(self.data.tab_right_selected["border"]))

        if self.data.tab_right_selected["border_width_value"] != 0 and self.data.tab_right_selected["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.tab_right_selected["border_width_value"], self.data.tab_right_selected["border_width_type"]))

        if self.data.tab_right_selected["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.tab_right_selected["border_style"]))

        if self.data.tab_right_selected["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.tab_right_selected["border_color"]))

        if self.data.tab_right_selected["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.tab_right_selected["border_top"]))

        if self.data.tab_right_selected["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.tab_right_selected["border_right"]))

        if self.data.tab_right_selected["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.tab_right_selected["border_bottom"]))

        if self.data.tab_right_selected["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.tab_right_selected["border_left"]))

        if self.data.tab_right_selected["border_radius"] != 0 and self.data.tab_right_selected["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.tab_right_selected["border_radius"]))

        if self.data.tab_right_selected["padding_top_value"] != 0 and self.data.tab_right_selected["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_right_selected["padding_top_value"], self.data.tab_right_selected["padding_top_type"]))

        if self.data.tab_right_selected["padding_right_value"] != 0 and self.data.tab_right_selected["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.tab_right_selected["padding_right_value"], self.data.tab_right_selected["padding_right_type"]))

        if self.data.tab_right_selected["padding_bottom_value"] != 0 and self.data.tab_right_selected["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.tab_right_selected["padding_bottom_value"], self.data.tab_right_selected["padding_bottom_type"]))

        if self.data.tab_right_selected["padding_left_value"] != 0 and self.data.tab_right_selected["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.tab_right_selected["padding_left_value"], self.data.tab_right_selected["padding_left_type"]))


        if self.data.tab_right_selected["margin_top_value"] != 0 and self.data.tab_right_selected["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_right_selected["margin_top_value"], self.data.tab_right_selected["margin_top_type"]))

        if self.data.tab_right_selected["margin_right_value"] != 0 and self.data.tab_right_selected["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.tab_right_selected["margin_right_value"], self.data.tab_right_selected["margin_right_type"]))

        if self.data.tab_right_selected["margin_bottom_value"] != 0 and self.data.tab_right_selected["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.tab_right_selected["margin_bottom_value"], self.data.tab_right_selected["margin_bottom_type"]))

        if self.data.tab_right_selected["margin_left_value"] != 0 and self.data.tab_right_selected["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.tab_right_selected["margin_left_value"], self.data.tab_right_selected["margin_left_type"]))


        f.write("\n}")







        f.write("\n")




        f.write("QTabBar" + "::tab:right:!selected {")

        if self.data.tab_right_u_selected["color"] != "":
            f.write("\n   color: {};".format(self.data.tab_right_u_selected["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.tab_right_u_selected["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.tab_right_u_selected["outline"]))

        if self.data.tab_right_u_selected["width_value"] != 0 and self.data.tab_right_u_selected["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.tab_right_u_selected["width_value"], self.data.tab_right_u_selected["width_type"]))

        if self.data.tab_right_u_selected["height_value"] != 0 and self.data.tab_right_u_selected["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.tab_right_u_selected["height_value"], self.data.tab_right_u_selected["height_type"]))

        if self.data.tab_right_u_selected["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.tab_right_u_selected["font_family"]))

        if self.data.tab_right_u_selected["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.tab_right_u_selected["font_size"]))

        if self.data.tab_right_u_selected["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.tab_right_u_selected["font_weight"]))

        if self.data.tab_right_u_selected["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.tab_right_u_selected["font_style"]))

        if self.data.tab_right_u_selected["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.tab_right_u_selected["line_height"]))

        if self.data.tab_right_u_selected["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.tab_right_u_selected["text_align"]))

        if self.data.tab_right_u_selected["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.tab_right_u_selected["text_decoration"]))

        if self.data.tab_right_u_selected["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.tab_right_u_selected["text_transform"]))

        if self.data.tab_right_u_selected["background"] != "":
            f.write("\n   background: {};".format(self.data.tab_right_u_selected["background"]))

        if self.data.tab_right_u_selected["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.tab_right_u_selected["background_image"]))

        if self.data.tab_right_u_selected["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.tab_right_u_selected["background_color"]))

        if self.data.tab_right_u_selected["border"] != "":
            f.write("\n   border: {};".format(self.data.tab_right_u_selected["border"]))

        if self.data.tab_right_u_selected["border_width_value"] != 0 and self.data.tab_right_u_selected["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.tab_right_u_selected["border_width_value"], self.data.tab_right_u_selected["border_width_type"]))

        if self.data.tab_right_u_selected["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.tab_right_u_selected["border_style"]))

        if self.data.tab_right_u_selected["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.tab_right_u_selected["border_color"]))

        if self.data.tab_right_u_selected["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.tab_right_u_selected["border_top"]))

        if self.data.tab_right_u_selected["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.tab_right_u_selected["border_right"]))

        if self.data.tab_right_u_selected["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.tab_right_u_selected["border_bottom"]))

        if self.data.tab_right_u_selected["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.tab_right_u_selected["border_left"]))

        if self.data.tab_right_u_selected["border_radius"] != 0 and self.data.tab_right_u_selected["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.tab_right_u_selected["border_radius"]))

        if self.data.tab_right_u_selected["padding_top_value"] != 0 and self.data.tab_right_u_selected["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_right_u_selected["padding_top_value"], self.data.tab_right_u_selected["padding_top_type"]))

        if self.data.tab_right_u_selected["padding_right_value"] != 0 and self.data.tab_right_u_selected["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.tab_right_u_selected["padding_right_value"], self.data.tab_right_u_selected["padding_right_type"]))

        if self.data.tab_right_u_selected["padding_bottom_value"] != 0 and self.data.tab_right_u_selected["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.tab_right_u_selected["padding_bottom_value"], self.data.tab_right_u_selected["padding_bottom_type"]))

        if self.data.tab_right_u_selected["padding_left_value"] != 0 and self.data.tab_right_u_selected["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.tab_right_u_selected["padding_left_value"], self.data.tab_right_u_selected["padding_left_type"]))


        if self.data.tab_right_u_selected["margin_top_value"] != 0 and self.data.tab_right_u_selected["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_right_u_selected["margin_top_value"], self.data.tab_right_u_selected["margin_top_type"]))

        if self.data.tab_right_u_selected["margin_right_value"] != 0 and self.data.tab_right_u_selected["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.tab_right_u_selected["margin_right_value"], self.data.tab_right_u_selected["margin_right_type"]))

        if self.data.tab_right_u_selected["margin_bottom_value"] != 0 and self.data.tab_right_u_selected["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.tab_right_u_selected["margin_bottom_value"], self.data.tab_right_u_selected["margin_bottom_type"]))

        if self.data.tab_right_u_selected["margin_left_value"] != 0 and self.data.tab_right_u_selected["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.tab_right_u_selected["margin_left_value"], self.data.tab_right_u_selected["margin_left_type"]))


        f.write("\n}")




        f.write("\n")




        f.write("QTabBar" + "::tab:bottom {")

        if self.data.tab_bottom["color"] != "":
            f.write("\n   color: {};".format(self.data.tab_bottom["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.tab_bottom["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.tab_bottom["outline"]))

        if self.data.tab_bottom["width_value"] != 0 and self.data.tab_bottom["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.tab_bottom["width_value"], self.data.tab_bottom["width_type"]))

        if self.data.tab_bottom["height_value"] != 0 and self.data.tab_bottom["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.tab_bottom["height_value"], self.data.tab_bottom["height_type"]))

        if self.data.tab_bottom["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.tab_bottom["font_family"]))

        if self.data.tab_bottom["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.tab_bottom["font_size"]))

        if self.data.tab_bottom["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.tab_bottom["font_weight"]))

        if self.data.tab_bottom["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.tab_bottom["font_style"]))

        if self.data.tab_bottom["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.tab_bottom["line_height"]))

        if self.data.tab_bottom["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.tab_bottom["text_align"]))

        if self.data.tab_bottom["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.tab_bottom["text_decoration"]))

        if self.data.tab_bottom["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.tab_bottom["text_transform"]))

        if self.data.tab_bottom["background"] != "":
            f.write("\n   background: {};".format(self.data.tab_bottom["background"]))

        if self.data.tab_bottom["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.tab_bottom["background_image"]))

        if self.data.tab_bottom["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.tab_bottom["background_color"]))

        if self.data.tab_bottom["border"] != "":
            f.write("\n   border: {};".format(self.data.tab_bottom["border"]))

        if self.data.tab_bottom["border_width_value"] != 0 and self.data.tab_bottom["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.tab_bottom["border_width_value"], self.data.tab_bottom["border_width_type"]))

        if self.data.tab_bottom["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.tab_bottom["border_style"]))

        if self.data.tab_bottom["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.tab_bottom["border_color"]))

        if self.data.tab_bottom["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.tab_bottom["border_top"]))

        if self.data.tab_bottom["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.tab_bottom["border_right"]))

        if self.data.tab_bottom["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.tab_bottom["border_bottom"]))

        if self.data.tab_bottom["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.tab_bottom["border_left"]))

        if self.data.tab_bottom["border_radius"] != 0 and self.data.tab_bottom["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.tab_bottom["border_radius"]))

        if self.data.tab_bottom["padding_top_value"] != 0 and self.data.tab_bottom["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_bottom["padding_top_value"], self.data.tab_bottom["padding_top_type"]))

        if self.data.tab_bottom["padding_right_value"] != 0 and self.data.tab_bottom["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.tab_bottom["padding_right_value"], self.data.tab_bottom["padding_right_type"]))

        if self.data.tab_bottom["padding_bottom_value"] != 0 and self.data.tab_bottom["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.tab_bottom["padding_bottom_value"], self.data.tab_bottom["padding_bottom_type"]))

        if self.data.tab_bottom["padding_left_value"] != 0 and self.data.tab_bottom["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.tab_bottom["padding_left_value"], self.data.tab_bottom["padding_left_type"]))


        if self.data.tab_bottom["margin_top_value"] != 0 and self.data.tab_bottom["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_bottom["margin_top_value"], self.data.tab_bottom["margin_top_type"]))

        if self.data.tab_bottom["margin_right_value"] != 0 and self.data.tab_bottom["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.tab_bottom["margin_right_value"], self.data.tab_bottom["margin_right_type"]))

        if self.data.tab_bottom["margin_bottom_value"] != 0 and self.data.tab_bottom["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.tab_bottom["margin_bottom_value"], self.data.tab_bottom["margin_bottom_type"]))

        if self.data.tab_bottom["margin_left_value"] != 0 and self.data.tab_bottom["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.tab_bottom["margin_left_value"], self.data.tab_bottom["margin_left_type"]))


        f.write("\n}")




        f.write("\n")




        f.write("QTabBar" + "::tab:bottom:selected {")

        if self.data.tab_bottom_selected["color"] != "":
            f.write("\n   color: {};".format(self.data.tab_bottom_selected["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.tab_bottom_selected["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.tab_bottom_selected["outline"]))

        if self.data.tab_bottom_selected["width_value"] != 0 and self.data.tab_bottom_selected["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.tab_bottom_selected["width_value"], self.data.tab_bottom_selected["width_type"]))

        if self.data.tab_bottom_selected["height_value"] != 0 and self.data.tab_bottom_selected["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.tab_bottom_selected["height_value"], self.data.tab_bottom_selected["height_type"]))

        if self.data.tab_bottom_selected["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.tab_bottom_selected["font_family"]))

        if self.data.tab_bottom_selected["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.tab_bottom_selected["font_size"]))

        if self.data.tab_bottom_selected["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.tab_bottom_selected["font_weight"]))

        if self.data.tab_bottom_selected["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.tab_bottom_selected["font_style"]))

        if self.data.tab_bottom_selected["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.tab_bottom_selected["line_height"]))

        if self.data.tab_bottom_selected["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.tab_bottom_selected["text_align"]))

        if self.data.tab_bottom_selected["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.tab_bottom_selected["text_decoration"]))

        if self.data.tab_bottom_selected["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.tab_bottom_selected["text_transform"]))

        if self.data.tab_bottom_selected["background"] != "":
            f.write("\n   background: {};".format(self.data.tab_bottom_selected["background"]))

        if self.data.tab_bottom_selected["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.tab_bottom_selected["background_image"]))

        if self.data.tab_bottom_selected["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.tab_bottom_selected["background_color"]))

        if self.data.tab_bottom_selected["border"] != "":
            f.write("\n   border: {};".format(self.data.tab_bottom_selected["border"]))

        if self.data.tab_bottom_selected["border_width_value"] != 0 and self.data.tab_bottom_selected["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.tab_bottom_selected["border_width_value"], self.data.tab_bottom_selected["border_width_type"]))

        if self.data.tab_bottom_selected["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.tab_bottom_selected["border_style"]))

        if self.data.tab_bottom_selected["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.tab_bottom_selected["border_color"]))

        if self.data.tab_bottom_selected["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.tab_bottom_selected["border_top"]))

        if self.data.tab_bottom_selected["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.tab_bottom_selected["border_right"]))

        if self.data.tab_bottom_selected["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.tab_bottom_selected["border_bottom"]))

        if self.data.tab_bottom_selected["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.tab_bottom_selected["border_left"]))

        if self.data.tab_bottom_selected["border_radius"] != 0 and self.data.tab_bottom_selected["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.tab_bottom_selected["border_radius"]))

        if self.data.tab_bottom_selected["padding_top_value"] != 0 and self.data.tab_bottom_selected["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_bottom_selected["padding_top_value"], self.data.tab_bottom_selected["padding_top_type"]))

        if self.data.tab_bottom_selected["padding_right_value"] != 0 and self.data.tab_bottom_selected["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.tab_bottom_selected["padding_right_value"], self.data.tab_bottom_selected["padding_right_type"]))

        if self.data.tab_bottom_selected["padding_bottom_value"] != 0 and self.data.tab_bottom_selected["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.tab_bottom_selected["padding_bottom_value"], self.data.tab_bottom_selected["padding_bottom_type"]))

        if self.data.tab_bottom_selected["padding_left_value"] != 0 and self.data.tab_bottom_selected["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.tab_bottom_selected["padding_left_value"], self.data.tab_bottom_selected["padding_left_type"]))


        if self.data.tab_bottom_selected["margin_top_value"] != 0 and self.data.tab_bottom_selected["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_bottom_selected["margin_top_value"], self.data.tab_bottom_selected["margin_top_type"]))

        if self.data.tab_bottom_selected["margin_right_value"] != 0 and self.data.tab_bottom_selected["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.tab_bottom_selected["margin_right_value"], self.data.tab_bottom_selected["margin_right_type"]))

        if self.data.tab_bottom_selected["margin_bottom_value"] != 0 and self.data.tab_bottom_selected["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.tab_bottom_selected["margin_bottom_value"], self.data.tab_bottom_selected["margin_bottom_type"]))

        if self.data.tab_bottom_selected["margin_left_value"] != 0 and self.data.tab_bottom_selected["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.tab_bottom_selected["margin_left_value"], self.data.tab_bottom_selected["margin_left_type"]))


        f.write("\n}")







        f.write("\n")




        f.write("QTabBar" + "::tab:bottom:!selected {")

        if self.data.tab_bottom_u_selected["color"] != "":
            f.write("\n   color: {};".format(self.data.tab_bottom_u_selected["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.tab_bottom_u_selected["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.tab_bottom_u_selected["outline"]))

        if self.data.tab_bottom_u_selected["width_value"] != 0 and self.data.tab_bottom_u_selected["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.tab_bottom_u_selected["width_value"], self.data.tab_bottom_u_selected["width_type"]))

        if self.data.tab_bottom_u_selected["height_value"] != 0 and self.data.tab_bottom_u_selected["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.tab_bottom_u_selected["height_value"], self.data.tab_bottom_u_selected["height_type"]))

        if self.data.tab_bottom_u_selected["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.tab_bottom_u_selected["font_family"]))

        if self.data.tab_bottom_u_selected["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.tab_bottom_u_selected["font_size"]))

        if self.data.tab_bottom_u_selected["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.tab_bottom_u_selected["font_weight"]))

        if self.data.tab_bottom_u_selected["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.tab_bottom_u_selected["font_style"]))

        if self.data.tab_bottom_u_selected["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.tab_bottom_u_selected["line_height"]))

        if self.data.tab_bottom_u_selected["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.tab_bottom_u_selected["text_align"]))

        if self.data.tab_bottom_u_selected["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.tab_bottom_u_selected["text_decoration"]))

        if self.data.tab_bottom_u_selected["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.tab_bottom_u_selected["text_transform"]))

        if self.data.tab_bottom_u_selected["background"] != "":
            f.write("\n   background: {};".format(self.data.tab_bottom_u_selected["background"]))

        if self.data.tab_bottom_u_selected["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.tab_bottom_u_selected["background_image"]))

        if self.data.tab_bottom_u_selected["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.tab_bottom_u_selected["background_color"]))

        if self.data.tab_bottom_u_selected["border"] != "":
            f.write("\n   border: {};".format(self.data.tab_bottom_u_selected["border"]))

        if self.data.tab_bottom_u_selected["border_width_value"] != 0 and self.data.tab_bottom_u_selected["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.tab_bottom_u_selected["border_width_value"], self.data.tab_bottom_u_selected["border_width_type"]))

        if self.data.tab_bottom_u_selected["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.tab_bottom_u_selected["border_style"]))

        if self.data.tab_bottom_u_selected["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.tab_bottom_u_selected["border_color"]))

        if self.data.tab_bottom_u_selected["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.tab_bottom_u_selected["border_top"]))

        if self.data.tab_bottom_u_selected["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.tab_bottom_u_selected["border_right"]))

        if self.data.tab_bottom_u_selected["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.tab_bottom_u_selected["border_bottom"]))

        if self.data.tab_bottom_u_selected["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.tab_bottom_u_selected["border_left"]))

        if self.data.tab_bottom_u_selected["border_radius"] != 0 and self.data.tab_bottom_u_selected["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.tab_bottom_u_selected["border_radius"]))

        if self.data.tab_bottom_u_selected["padding_top_value"] != 0 and self.data.tab_bottom_u_selected["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_bottom_u_selected["padding_top_value"], self.data.tab_bottom_u_selected["padding_top_type"]))

        if self.data.tab_bottom_u_selected["padding_right_value"] != 0 and self.data.tab_bottom_u_selected["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.tab_bottom_u_selected["padding_right_value"], self.data.tab_bottom_u_selected["padding_right_type"]))

        if self.data.tab_bottom_u_selected["padding_bottom_value"] != 0 and self.data.tab_bottom_u_selected["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.tab_bottom_u_selected["padding_bottom_value"], self.data.tab_bottom_u_selected["padding_bottom_type"]))

        if self.data.tab_bottom_u_selected["padding_left_value"] != 0 and self.data.tab_bottom_u_selected["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.tab_bottom_u_selected["padding_left_value"], self.data.tab_bottom_u_selected["padding_left_type"]))


        if self.data.tab_bottom_u_selected["margin_top_value"] != 0 and self.data.tab_bottom_u_selected["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_bottom_u_selected["margin_top_value"], self.data.tab_bottom_u_selected["margin_top_type"]))

        if self.data.tab_bottom_u_selected["margin_right_value"] != 0 and self.data.tab_bottom_u_selected["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.tab_bottom_u_selected["margin_right_value"], self.data.tab_bottom_u_selected["margin_right_type"]))

        if self.data.tab_bottom_u_selected["margin_bottom_value"] != 0 and self.data.tab_bottom_u_selected["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.tab_bottom_u_selected["margin_bottom_value"], self.data.tab_bottom_u_selected["margin_bottom_type"]))

        if self.data.tab_bottom_u_selected["margin_left_value"] != 0 and self.data.tab_bottom_u_selected["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.tab_bottom_u_selected["margin_left_value"], self.data.tab_bottom_u_selected["margin_left_type"]))


        f.write("\n}")




        f.write("\n")




        f.write("QTabBar" + "::tab:left {")

        if self.data.tab_left["color"] != "":
            f.write("\n   color: {};".format(self.data.tab_left["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.tab_left["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.tab_left["outline"]))

        if self.data.tab_left["width_value"] != 0 and self.data.tab_left["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.tab_left["width_value"], self.data.tab_left["width_type"]))

        if self.data.tab_left["height_value"] != 0 and self.data.tab_left["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.tab_left["height_value"], self.data.tab_left["height_type"]))

        if self.data.tab_left["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.tab_left["font_family"]))

        if self.data.tab_left["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.tab_left["font_size"]))

        if self.data.tab_left["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.tab_left["font_weight"]))

        if self.data.tab_left["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.tab_left["font_style"]))

        if self.data.tab_left["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.tab_left["line_height"]))

        if self.data.tab_left["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.tab_left["text_align"]))

        if self.data.tab_left["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.tab_left["text_decoration"]))

        if self.data.tab_left["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.tab_left["text_transform"]))

        if self.data.tab_left["background"] != "":
            f.write("\n   background: {};".format(self.data.tab_left["background"]))

        if self.data.tab_left["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.tab_left["background_image"]))

        if self.data.tab_left["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.tab_left["background_color"]))

        if self.data.tab_left["border"] != "":
            f.write("\n   border: {};".format(self.data.tab_left["border"]))

        if self.data.tab_left["border_width_value"] != 0 and self.data.tab_left["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.tab_left["border_width_value"], self.data.tab_left["border_width_type"]))

        if self.data.tab_left["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.tab_left["border_style"]))

        if self.data.tab_left["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.tab_left["border_color"]))

        if self.data.tab_left["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.tab_left["border_top"]))

        if self.data.tab_left["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.tab_left["border_right"]))

        if self.data.tab_left["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.tab_left["border_bottom"]))

        if self.data.tab_left["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.tab_left["border_left"]))

        if self.data.tab_left["border_radius"] != 0 and self.data.tab_left["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.tab_left["border_radius"]))

        if self.data.tab_left["padding_top_value"] != 0 and self.data.tab_left["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_left["padding_top_value"], self.data.tab_left["padding_top_type"]))

        if self.data.tab_left["padding_right_value"] != 0 and self.data.tab_left["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.tab_left["padding_right_value"], self.data.tab_left["padding_right_type"]))

        if self.data.tab_left["padding_bottom_value"] != 0 and self.data.tab_left["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.tab_left["padding_bottom_value"], self.data.tab_left["padding_bottom_type"]))

        if self.data.tab_left["padding_left_value"] != 0 and self.data.tab_left["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.tab_left["padding_left_value"], self.data.tab_left["padding_left_type"]))


        if self.data.tab_left["margin_top_value"] != 0 and self.data.tab_left["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_left["margin_top_value"], self.data.tab_left["margin_top_type"]))

        if self.data.tab_left["margin_right_value"] != 0 and self.data.tab_left["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.tab_left["margin_right_value"], self.data.tab_left["margin_right_type"]))

        if self.data.tab_left["margin_bottom_value"] != 0 and self.data.tab_left["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.tab_left["margin_bottom_value"], self.data.tab_left["margin_bottom_type"]))

        if self.data.tab_left["margin_left_value"] != 0 and self.data.tab_left["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.tab_left["margin_left_value"], self.data.tab_left["margin_left_type"]))


        f.write("\n}")




        f.write("\n")




        f.write("QTabBar" + "::tab:left:selected {")

        if self.data.tab_left_selected["color"] != "":
            f.write("\n   color: {};".format(self.data.tab_left_selected["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.tab_left_selected["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.tab_left_selected["outline"]))

        if self.data.tab_left_selected["width_value"] != 0 and self.data.tab_left_selected["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.tab_left_selected["width_value"], self.data.tab_left_selected["width_type"]))

        if self.data.tab_left_selected["height_value"] != 0 and self.data.tab_left_selected["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.tab_left_selected["height_value"], self.data.tab_left_selected["height_type"]))

        if self.data.tab_left_selected["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.tab_left_selected["font_family"]))

        if self.data.tab_left_selected["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.tab_left_selected["font_size"]))

        if self.data.tab_left_selected["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.tab_left_selected["font_weight"]))

        if self.data.tab_left_selected["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.tab_left_selected["font_style"]))

        if self.data.tab_left_selected["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.tab_left_selected["line_height"]))

        if self.data.tab_left_selected["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.tab_left_selected["text_align"]))

        if self.data.tab_left_selected["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.tab_left_selected["text_decoration"]))

        if self.data.tab_left_selected["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.tab_left_selected["text_transform"]))

        if self.data.tab_left_selected["background"] != "":
            f.write("\n   background: {};".format(self.data.tab_left_selected["background"]))

        if self.data.tab_left_selected["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.tab_left_selected["background_image"]))

        if self.data.tab_left_selected["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.tab_left_selected["background_color"]))

        if self.data.tab_left_selected["border"] != "":
            f.write("\n   border: {};".format(self.data.tab_left_selected["border"]))

        if self.data.tab_left_selected["border_width_value"] != 0 and self.data.tab_left_selected["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.tab_left_selected["border_width_value"], self.data.tab_left_selected["border_width_type"]))

        if self.data.tab_left_selected["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.tab_left_selected["border_style"]))

        if self.data.tab_left_selected["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.tab_left_selected["border_color"]))

        if self.data.tab_left_selected["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.tab_left_selected["border_top"]))

        if self.data.tab_left_selected["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.tab_left_selected["border_right"]))

        if self.data.tab_left_selected["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.tab_left_selected["border_bottom"]))

        if self.data.tab_left_selected["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.tab_left_selected["border_left"]))

        if self.data.tab_left_selected["border_radius"] != 0 and self.data.tab_left_selected["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.tab_left_selected["border_radius"]))

        if self.data.tab_left_selected["padding_top_value"] != 0 and self.data.tab_left_selected["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_left_selected["padding_top_value"], self.data.tab_left_selected["padding_top_type"]))

        if self.data.tab_left_selected["padding_right_value"] != 0 and self.data.tab_left_selected["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.tab_left_selected["padding_right_value"], self.data.tab_left_selected["padding_right_type"]))

        if self.data.tab_left_selected["padding_bottom_value"] != 0 and self.data.tab_left_selected["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.tab_left_selected["padding_bottom_value"], self.data.tab_left_selected["padding_bottom_type"]))

        if self.data.tab_left_selected["padding_left_value"] != 0 and self.data.tab_left_selected["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.tab_left_selected["padding_left_value"], self.data.tab_left_selected["padding_left_type"]))


        if self.data.tab_left_selected["margin_top_value"] != 0 and self.data.tab_left_selected["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_left_selected["margin_top_value"], self.data.tab_left_selected["margin_top_type"]))

        if self.data.tab_left_selected["margin_right_value"] != 0 and self.data.tab_left_selected["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.tab_left_selected["margin_right_value"], self.data.tab_left_selected["margin_right_type"]))

        if self.data.tab_left_selected["margin_bottom_value"] != 0 and self.data.tab_left_selected["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.tab_left_selected["margin_bottom_value"], self.data.tab_left_selected["margin_bottom_type"]))

        if self.data.tab_left_selected["margin_left_value"] != 0 and self.data.tab_left_selected["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.tab_left_selected["margin_left_value"], self.data.tab_left_selected["margin_left_type"]))


        f.write("\n}")







        f.write("\n")




        f.write("QTabBar" + "::tab:left:!selected {")

        if self.data.tab_left_u_selected["color"] != "":
            f.write("\n   color: {};".format(self.data.tab_left_u_selected["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.tab_left_u_selected["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.tab_left_u_selected["outline"]))

        if self.data.tab_left_u_selected["width_value"] != 0 and self.data.tab_left_u_selected["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.tab_left_u_selected["width_value"], self.data.tab_left_u_selected["width_type"]))

        if self.data.tab_left_u_selected["height_value"] != 0 and self.data.tab_left_u_selected["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.tab_left_u_selected["height_value"], self.data.tab_left_u_selected["height_type"]))

        if self.data.tab_left_u_selected["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.tab_left_u_selected["font_family"]))

        if self.data.tab_left_u_selected["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.tab_left_u_selected["font_size"]))

        if self.data.tab_left_u_selected["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.tab_left_u_selected["font_weight"]))

        if self.data.tab_left_u_selected["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.tab_left_u_selected["font_style"]))

        if self.data.tab_left_u_selected["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.tab_left_u_selected["line_height"]))

        if self.data.tab_left_u_selected["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.tab_left_u_selected["text_align"]))

        if self.data.tab_left_u_selected["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.tab_left_u_selected["text_decoration"]))

        if self.data.tab_left_u_selected["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.tab_left_u_selected["text_transform"]))

        if self.data.tab_left_u_selected["background"] != "":
            f.write("\n   background: {};".format(self.data.tab_left_u_selected["background"]))

        if self.data.tab_left_u_selected["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.tab_left_u_selected["background_image"]))

        if self.data.tab_left_u_selected["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.tab_left_u_selected["background_color"]))

        if self.data.tab_left_u_selected["border"] != "":
            f.write("\n   border: {};".format(self.data.tab_left_u_selected["border"]))

        if self.data.tab_left_u_selected["border_width_value"] != 0 and self.data.tab_left_u_selected["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.tab_left_u_selected["border_width_value"], self.data.tab_left_u_selected["border_width_type"]))

        if self.data.tab_left_u_selected["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.tab_left_u_selected["border_style"]))

        if self.data.tab_left_u_selected["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.tab_left_u_selected["border_color"]))

        if self.data.tab_left_u_selected["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.tab_left_u_selected["border_top"]))

        if self.data.tab_left_u_selected["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.tab_left_u_selected["border_right"]))

        if self.data.tab_left_u_selected["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.tab_left_u_selected["border_bottom"]))

        if self.data.tab_left_u_selected["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.tab_left_u_selected["border_left"]))

        if self.data.tab_left_u_selected["border_radius"] != 0 and self.data.tab_left_u_selected["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.tab_left_u_selected["border_radius"]))

        if self.data.tab_left_u_selected["padding_top_value"] != 0 and self.data.tab_left_u_selected["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_left_u_selected["padding_top_value"], self.data.tab_left_u_selected["padding_top_type"]))

        if self.data.tab_left_u_selected["padding_right_value"] != 0 and self.data.tab_left_u_selected["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.tab_left_u_selected["padding_right_value"], self.data.tab_left_u_selected["padding_right_type"]))

        if self.data.tab_left_u_selected["padding_bottom_value"] != 0 and self.data.tab_left_u_selected["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.tab_left_u_selected["padding_bottom_value"], self.data.tab_left_u_selected["padding_bottom_type"]))

        if self.data.tab_left_u_selected["padding_left_value"] != 0 and self.data.tab_left_u_selected["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.tab_left_u_selected["padding_left_value"], self.data.tab_left_u_selected["padding_left_type"]))


        if self.data.tab_left_u_selected["margin_top_value"] != 0 and self.data.tab_left_u_selected["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.tab_left_u_selected["margin_top_value"], self.data.tab_left_u_selected["margin_top_type"]))

        if self.data.tab_left_u_selected["margin_right_value"] != 0 and self.data.tab_left_u_selected["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.tab_left_u_selected["margin_right_value"], self.data.tab_left_u_selected["margin_right_type"]))

        if self.data.tab_left_u_selected["margin_bottom_value"] != 0 and self.data.tab_left_u_selected["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.tab_left_u_selected["margin_bottom_value"], self.data.tab_left_u_selected["margin_bottom_type"]))

        if self.data.tab_left_u_selected["margin_left_value"] != 0 and self.data.tab_left_u_selected["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.tab_left_u_selected["margin_left_value"], self.data.tab_left_u_selected["margin_left_type"]))


        f.write("\n}")






        f.write("\n")




        f.write("QTabBar" + "::close-button {")

        if self.data.close_button["color"] != "":
            f.write("\n   color: {};".format(self.data.close_button["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.close_button["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.close_button["outline"]))

        if self.data.close_button["width_value"] != 0 and self.data.close_button["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.close_button["width_value"], self.data.close_button["width_type"]))

        if self.data.close_button["height_value"] != 0 and self.data.close_button["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.close_button["height_value"], self.data.close_button["height_type"]))

        if self.data.close_button["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.close_button["font_family"]))

        if self.data.close_button["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.close_button["font_size"]))

        if self.data.close_button["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.close_button["font_weight"]))

        if self.data.close_button["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.close_button["font_style"]))

        if self.data.close_button["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.close_button["line_height"]))

        if self.data.close_button["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.close_button["text_align"]))

        if self.data.close_button["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.close_button["text_decoration"]))

        if self.data.close_button["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.close_button["text_transform"]))

        if self.data.close_button["background"] != "":
            f.write("\n   background: {};".format(self.data.close_button["background"]))

        if self.data.close_button["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.close_button["background_image"]))

        if self.data.close_button["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.close_button["background_color"]))

        if self.data.close_button["border"] != "":
            f.write("\n   border: {};".format(self.data.close_button["border"]))

        if self.data.close_button["border_width_value"] != 0 and self.data.close_button["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.close_button["border_width_value"], self.data.close_button["border_width_type"]))

        if self.data.close_button["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.close_button["border_style"]))

        if self.data.close_button["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.close_button["border_color"]))

        if self.data.close_button["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.close_button["border_top"]))

        if self.data.close_button["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.close_button["border_right"]))

        if self.data.close_button["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.close_button["border_bottom"]))

        if self.data.close_button["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.close_button["border_left"]))

        if self.data.close_button["border_radius"] != 0 and self.data.close_button["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.close_button["border_radius"]))

        if self.data.close_button["padding_top_value"] != 0 and self.data.close_button["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.close_button["padding_top_value"], self.data.close_button["padding_top_type"]))

        if self.data.close_button["padding_right_value"] != 0 and self.data.close_button["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.close_button["padding_right_value"], self.data.close_button["padding_right_type"]))

        if self.data.close_button["padding_bottom_value"] != 0 and self.data.close_button["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.close_button["padding_bottom_value"], self.data.close_button["padding_bottom_type"]))

        if self.data.close_button["padding_left_value"] != 0 and self.data.close_button["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.close_button["padding_left_value"], self.data.close_button["padding_left_type"]))


        if self.data.close_button["margin_top_value"] != 0 and self.data.close_button["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.close_button["margin_top_value"], self.data.close_button["margin_top_type"]))

        if self.data.close_button["margin_right_value"] != 0 and self.data.close_button["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.close_button["margin_right_value"], self.data.close_button["margin_right_type"]))

        if self.data.close_button["margin_bottom_value"] != 0 and self.data.close_button["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.close_button["margin_bottom_value"], self.data.close_button["margin_bottom_type"]))

        if self.data.close_button["margin_left_value"] != 0 and self.data.close_button["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.close_button["margin_left_value"], self.data.close_button["margin_left_type"]))


        f.write("\n}")






        f.write("\n")




        f.write("QTabBar" + "::close-button:hover {")

        if self.data.close_button_hover["color"] != "":
            f.write("\n   color: {};".format(self.data.close_button_hover["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.close_button_hover["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.close_button_hover["outline"]))

        if self.data.close_button_hover["width_value"] != 0 and self.data.close_button_hover["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.close_button_hover["width_value"], self.data.close_button_hover["width_type"]))

        if self.data.close_button_hover["height_value"] != 0 and self.data.close_button_hover["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.close_button_hover["height_value"], self.data.close_button_hover["height_type"]))

        if self.data.close_button_hover["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.close_button_hover["font_family"]))

        if self.data.close_button_hover["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.close_button_hover["font_size"]))

        if self.data.close_button_hover["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.close_button_hover["font_weight"]))

        if self.data.close_button_hover["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.close_button_hover["font_style"]))

        if self.data.close_button_hover["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.close_button_hover["line_height"]))

        if self.data.close_button_hover["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.close_button_hover["text_align"]))

        if self.data.close_button_hover["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.close_button_hover["text_decoration"]))

        if self.data.close_button_hover["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.close_button_hover["text_transform"]))

        if self.data.close_button_hover["background"] != "":
            f.write("\n   background: {};".format(self.data.close_button_hover["background"]))

        if self.data.close_button_hover["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.close_button_hover["background_image"]))

        if self.data.close_button_hover["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.close_button_hover["background_color"]))

        if self.data.close_button_hover["border"] != "":
            f.write("\n   border: {};".format(self.data.close_button_hover["border"]))

        if self.data.close_button_hover["border_width_value"] != 0 and self.data.close_button_hover["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.close_button_hover["border_width_value"], self.data.close_button_hover["border_width_type"]))

        if self.data.close_button_hover["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.close_button_hover["border_style"]))

        if self.data.close_button_hover["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.close_button_hover["border_color"]))

        if self.data.close_button_hover["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.close_button_hover["border_top"]))

        if self.data.close_button_hover["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.close_button_hover["border_right"]))

        if self.data.close_button_hover["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.close_button_hover["border_bottom"]))

        if self.data.close_button_hover["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.close_button_hover["border_left"]))

        if self.data.close_button_hover["border_radius"] != 0 and self.data.close_button_hover["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.close_button_hover["border_radius"]))

        if self.data.close_button_hover["padding_top_value"] != 0 and self.data.close_button_hover["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.close_button_hover["padding_top_value"], self.data.close_button_hover["padding_top_type"]))

        if self.data.close_button_hover["padding_right_value"] != 0 and self.data.close_button_hover["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.close_button_hover["padding_right_value"], self.data.close_button_hover["padding_right_type"]))

        if self.data.close_button_hover["padding_bottom_value"] != 0 and self.data.close_button_hover["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.close_button_hover["padding_bottom_value"], self.data.close_button_hover["padding_bottom_type"]))

        if self.data.close_button_hover["padding_left_value"] != 0 and self.data.close_button_hover["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.close_button_hover["padding_left_value"], self.data.close_button_hover["padding_left_type"]))


        if self.data.close_button_hover["margin_top_value"] != 0 and self.data.close_button_hover["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.close_button_hover["margin_top_value"], self.data.close_button_hover["margin_top_type"]))

        if self.data.close_button_hover["margin_right_value"] != 0 and self.data.close_button_hover["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.close_button_hover["margin_right_value"], self.data.close_button_hover["margin_right_type"]))

        if self.data.close_button_hover["margin_bottom_value"] != 0 and self.data.close_button_hover["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.close_button_hover["margin_bottom_value"], self.data.close_button_hover["margin_bottom_type"]))

        if self.data.close_button_hover["margin_left_value"] != 0 and self.data.close_button_hover["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.close_button_hover["margin_left_value"], self.data.close_button_hover["margin_left_type"]))


        f.write("\n}")





        f.write("\n")




        f.write("QTabBar" + " QToolButton {")

        if self.data.qtoolbutton["color"] != "":
            f.write("\n   color: {};".format(self.data.qtoolbutton["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.qtoolbutton["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.qtoolbutton["outline"]))

        if self.data.qtoolbutton["width_value"] != 0 and self.data.qtoolbutton["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.qtoolbutton["width_value"], self.data.qtoolbutton["width_type"]))

        if self.data.qtoolbutton["height_value"] != 0 and self.data.qtoolbutton["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.qtoolbutton["height_value"], self.data.qtoolbutton["height_type"]))

        if self.data.qtoolbutton["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.qtoolbutton["font_family"]))

        if self.data.qtoolbutton["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.qtoolbutton["font_size"]))

        if self.data.qtoolbutton["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.qtoolbutton["font_weight"]))

        if self.data.qtoolbutton["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.qtoolbutton["font_style"]))

        if self.data.qtoolbutton["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.qtoolbutton["line_height"]))

        if self.data.qtoolbutton["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.qtoolbutton["text_align"]))

        if self.data.qtoolbutton["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.qtoolbutton["text_decoration"]))

        if self.data.qtoolbutton["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.qtoolbutton["text_transform"]))

        if self.data.qtoolbutton["background"] != "":
            f.write("\n   background: {};".format(self.data.qtoolbutton["background"]))

        if self.data.qtoolbutton["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.qtoolbutton["background_image"]))

        if self.data.qtoolbutton["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.qtoolbutton["background_color"]))

        if self.data.qtoolbutton["border"] != "":
            f.write("\n   border: {};".format(self.data.qtoolbutton["border"]))

        if self.data.qtoolbutton["border_width_value"] != 0 and self.data.qtoolbutton["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.qtoolbutton["border_width_value"], self.data.qtoolbutton["border_width_type"]))

        if self.data.qtoolbutton["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.qtoolbutton["border_style"]))

        if self.data.qtoolbutton["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.qtoolbutton["border_color"]))

        if self.data.qtoolbutton["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.qtoolbutton["border_top"]))

        if self.data.qtoolbutton["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.qtoolbutton["border_right"]))

        if self.data.qtoolbutton["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.qtoolbutton["border_bottom"]))

        if self.data.qtoolbutton["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.qtoolbutton["border_left"]))

        if self.data.qtoolbutton["border_radius"] != 0 and self.data.qtoolbutton["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.qtoolbutton["border_radius"]))

        if self.data.qtoolbutton["padding_top_value"] != 0 and self.data.qtoolbutton["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.qtoolbutton["padding_top_value"], self.data.qtoolbutton["padding_top_type"]))

        if self.data.qtoolbutton["padding_right_value"] != 0 and self.data.qtoolbutton["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.qtoolbutton["padding_right_value"], self.data.qtoolbutton["padding_right_type"]))

        if self.data.qtoolbutton["padding_bottom_value"] != 0 and self.data.qtoolbutton["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.qtoolbutton["padding_bottom_value"], self.data.qtoolbutton["padding_bottom_type"]))

        if self.data.qtoolbutton["padding_left_value"] != 0 and self.data.qtoolbutton["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.qtoolbutton["padding_left_value"], self.data.qtoolbutton["padding_left_type"]))


        if self.data.qtoolbutton["margin_top_value"] != 0 and self.data.qtoolbutton["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.qtoolbutton["margin_top_value"], self.data.qtoolbutton["margin_top_type"]))

        if self.data.qtoolbutton["margin_right_value"] != 0 and self.data.qtoolbutton["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.qtoolbutton["margin_right_value"], self.data.qtoolbutton["margin_right_type"]))

        if self.data.qtoolbutton["margin_bottom_value"] != 0 and self.data.qtoolbutton["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.qtoolbutton["margin_bottom_value"], self.data.qtoolbutton["margin_bottom_type"]))

        if self.data.qtoolbutton["margin_left_value"] != 0 and self.data.qtoolbutton["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.qtoolbutton["margin_left_value"], self.data.qtoolbutton["margin_left_type"]))


        f.write("\n}")




        f.write("\n")




        f.write("QTabBar" + " QToolButton::right-arrow {")

        if self.data.qtoolbutton_right_arrow["color"] != "":
            f.write("\n   color: {};".format(self.data.qtoolbutton_right_arrow["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.qtoolbutton_right_arrow["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.qtoolbutton_right_arrow["outline"]))

        if self.data.qtoolbutton_right_arrow["width_value"] != 0 and self.data.qtoolbutton_right_arrow["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.qtoolbutton_right_arrow["width_value"], self.data.qtoolbutton_right_arrow["width_type"]))

        if self.data.qtoolbutton_right_arrow["height_value"] != 0 and self.data.qtoolbutton_right_arrow["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.qtoolbutton_right_arrow["height_value"], self.data.qtoolbutton_right_arrow["height_type"]))

        if self.data.qtoolbutton_right_arrow["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.qtoolbutton_right_arrow["font_family"]))

        if self.data.qtoolbutton_right_arrow["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.qtoolbutton_right_arrow["font_size"]))

        if self.data.qtoolbutton_right_arrow["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.qtoolbutton_right_arrow["font_weight"]))

        if self.data.qtoolbutton_right_arrow["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.qtoolbutton_right_arrow["font_style"]))

        if self.data.qtoolbutton_right_arrow["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.qtoolbutton_right_arrow["line_height"]))

        if self.data.qtoolbutton_right_arrow["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.qtoolbutton_right_arrow["text_align"]))

        if self.data.qtoolbutton_right_arrow["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.qtoolbutton_right_arrow["text_decoration"]))

        if self.data.qtoolbutton_right_arrow["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.qtoolbutton_right_arrow["text_transform"]))

        if self.data.qtoolbutton_right_arrow["background"] != "":
            f.write("\n   background: {};".format(self.data.qtoolbutton_right_arrow["background"]))

        if self.data.qtoolbutton_right_arrow["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.qtoolbutton_right_arrow["background_image"]))

        if self.data.qtoolbutton_right_arrow["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.qtoolbutton_right_arrow["background_color"]))

        if self.data.qtoolbutton_right_arrow["border"] != "":
            f.write("\n   border: {};".format(self.data.qtoolbutton_right_arrow["border"]))

        if self.data.qtoolbutton_right_arrow["border_width_value"] != 0 and self.data.qtoolbutton_right_arrow["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.qtoolbutton_right_arrow["border_width_value"], self.data.qtoolbutton_right_arrow["border_width_type"]))

        if self.data.qtoolbutton_right_arrow["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.qtoolbutton_right_arrow["border_style"]))

        if self.data.qtoolbutton_right_arrow["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.qtoolbutton_right_arrow["border_color"]))

        if self.data.qtoolbutton_right_arrow["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.qtoolbutton_right_arrow["border_top"]))

        if self.data.qtoolbutton_right_arrow["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.qtoolbutton_right_arrow["border_right"]))

        if self.data.qtoolbutton_right_arrow["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.qtoolbutton_right_arrow["border_bottom"]))

        if self.data.qtoolbutton_right_arrow["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.qtoolbutton_right_arrow["border_left"]))

        if self.data.qtoolbutton_right_arrow["border_radius"] != 0 and self.data.qtoolbutton_right_arrow["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.qtoolbutton_right_arrow["border_radius"]))

        if self.data.qtoolbutton_right_arrow["padding_top_value"] != 0 and self.data.qtoolbutton_right_arrow["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.qtoolbutton_right_arrow["padding_top_value"], self.data.qtoolbutton_right_arrow["padding_top_type"]))

        if self.data.qtoolbutton_right_arrow["padding_right_value"] != 0 and self.data.qtoolbutton_right_arrow["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.qtoolbutton_right_arrow["padding_right_value"], self.data.qtoolbutton_right_arrow["padding_right_type"]))

        if self.data.qtoolbutton_right_arrow["padding_bottom_value"] != 0 and self.data.qtoolbutton_right_arrow["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.qtoolbutton_right_arrow["padding_bottom_value"], self.data.qtoolbutton_right_arrow["padding_bottom_type"]))

        if self.data.qtoolbutton_right_arrow["padding_left_value"] != 0 and self.data.qtoolbutton_right_arrow["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.qtoolbutton_right_arrow["padding_left_value"], self.data.qtoolbutton_right_arrow["padding_left_type"]))


        if self.data.qtoolbutton_right_arrow["margin_top_value"] != 0 and self.data.qtoolbutton_right_arrow["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.qtoolbutton_right_arrow["margin_top_value"], self.data.qtoolbutton_right_arrow["margin_top_type"]))

        if self.data.qtoolbutton_right_arrow["margin_right_value"] != 0 and self.data.qtoolbutton_right_arrow["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.qtoolbutton_right_arrow["margin_right_value"], self.data.qtoolbutton_right_arrow["margin_right_type"]))

        if self.data.qtoolbutton_right_arrow["margin_bottom_value"] != 0 and self.data.qtoolbutton_right_arrow["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.qtoolbutton_right_arrow["margin_bottom_value"], self.data.qtoolbutton_right_arrow["margin_bottom_type"]))

        if self.data.qtoolbutton_right_arrow["margin_left_value"] != 0 and self.data.qtoolbutton_right_arrow["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.qtoolbutton_right_arrow["margin_left_value"], self.data.qtoolbutton_right_arrow["margin_left_type"]))


        f.write("\n}")




        f.write("\n")




        f.write("QTabBar" + " QToolButton::left-arrow {")

        if self.data.qtoolbutton_left_arrow["color"] != "":
            f.write("\n   color: {};".format(self.data.qtoolbutton_left_arrow["color"]))

        if self.data.me["image"] != "":
            f.write('\n  image: url("{}");'.format(self.data.qtoolbutton_left_arrow["image"]))

        if self.data.me["outline"] != "":
             f.write("\n   outline: {};".format(self.data.qtoolbutton_left_arrow["outline"]))

        if self.data.qtoolbutton_left_arrow["width_value"] != 0 and self.data.qtoolbutton_left_arrow["width_value"] != "0":
            f.write("\n   width: {}{};".format(self.data.qtoolbutton_left_arrow["width_value"], self.data.qtoolbutton_left_arrow["width_type"]))

        if self.data.qtoolbutton_left_arrow["height_value"] != 0 and self.data.qtoolbutton_left_arrow["height_value"] != "0":
            f.write("\n   height: {}{};".format(self.data.qtoolbutton_left_arrow["height_value"], self.data.qtoolbutton_left_arrow["height_type"]))

        if self.data.qtoolbutton_left_arrow["font_family"] != "":
            f.write("\n   font-family: {};".format(self.data.qtoolbutton_left_arrow["font_family"]))

        if self.data.qtoolbutton_left_arrow["font_size"] != "":
            f.write("\n   font-size: {};".format(self.data.qtoolbutton_left_arrow["font_size"]))

        if self.data.qtoolbutton_left_arrow["font_weight"] != "normal":
            f.write("\n   font-weight: {};".format(self.data.qtoolbutton_left_arrow["font_weight"]))

        if self.data.qtoolbutton_left_arrow["font_style"] != "normal":
            f.write("\n   font-style: {};".format(self.data.qtoolbutton_left_arrow["font_style"]))

        if self.data.qtoolbutton_left_arrow["line_height"] != "":
            f.write("\n   line-height: {};".format(self.data.qtoolbutton_left_arrow["line_height"]))

        if self.data.qtoolbutton_left_arrow["text_align"] != "left":
            f.write("\n   text-align: {};".format(self.data.qtoolbutton_left_arrow["text_align"]))

        if self.data.qtoolbutton_left_arrow["text_decoration"] != "":
            f.write("\n   text-decoration: {};".format(self.data.qtoolbutton_left_arrow["text_decoration"]))

        if self.data.qtoolbutton_left_arrow["text_transform"] != "":
            f.write("\n   text-transform: {};".format(self.data.qtoolbutton_left_arrow["text_transform"]))

        if self.data.qtoolbutton_left_arrow["background"] != "":
            f.write("\n   background: {};".format(self.data.qtoolbutton_left_arrow["background"]))

        if self.data.qtoolbutton_left_arrow["background_image"] != "":
            f.write('\n   background-image: url("{}");'.format(self.data.qtoolbutton_left_arrow["background_image"]))

        if self.data.qtoolbutton_left_arrow["background_color"] != "":
            f.write("\n   background-color: {};".format(self.data.qtoolbutton_left_arrow["background_color"]))

        if self.data.qtoolbutton_left_arrow["border"] != "":
            f.write("\n   border: {};".format(self.data.qtoolbutton_left_arrow["border"]))

        if self.data.qtoolbutton_left_arrow["border_width_value"] != 0 and self.data.qtoolbutton_left_arrow["border_width_value"] != "0":
            f.write("\n   border-width: {}{};".format(self.data.qtoolbutton_left_arrow["border_width_value"], self.data.qtoolbutton_left_arrow["border_width_type"]))

        if self.data.qtoolbutton_left_arrow["border_style"] != "":
            f.write("\n   border-style: {};".format(self.data.qtoolbutton_left_arrow["border_style"]))

        if self.data.qtoolbutton_left_arrow["border_color"] != "":
            f.write("\n   border-color: {};".format(self.data.qtoolbutton_left_arrow["border_color"]))

        if self.data.qtoolbutton_left_arrow["border_top"] != "":
            f.write("\n   border-top: {};".format(self.data.qtoolbutton_left_arrow["border_top"]))

        if self.data.qtoolbutton_left_arrow["border_right"] != "":
            f.write("\n   border-right: {};".format(self.data.qtoolbutton_left_arrow["border_right"]))

        if self.data.qtoolbutton_left_arrow["border_bottom"] != "":
            f.write("\n   border-bottom: {};".format(self.data.qtoolbutton_left_arrow["border_bottom"]))

        if self.data.qtoolbutton_left_arrow["border_left"] != "":
            f.write("\n   border-left: {};".format(self.data.qtoolbutton_left_arrow["border_left"]))

        if self.data.qtoolbutton_left_arrow["border_radius"] != 0 and self.data.qtoolbutton_left_arrow["border_radius"] != "0":
            f.write("\n   border-radius: {};".format(self.data.qtoolbutton_left_arrow["border_radius"]))

        if self.data.qtoolbutton_left_arrow["padding_top_value"] != 0 and self.data.qtoolbutton_left_arrow["padding_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.qtoolbutton_left_arrow["padding_top_value"], self.data.qtoolbutton_left_arrow["padding_top_type"]))

        if self.data.qtoolbutton_left_arrow["padding_right_value"] != 0 and self.data.qtoolbutton_left_arrow["padding_right_value"] != "0":
            f.write("\n   padding-right: {}{};".format(self.data.qtoolbutton_left_arrow["padding_right_value"], self.data.qtoolbutton_left_arrow["padding_right_type"]))

        if self.data.qtoolbutton_left_arrow["padding_bottom_value"] != 0 and self.data.qtoolbutton_left_arrow["padding_bottom_value"] != "0":
            f.write("\n   padding-bottom: {}{};".format(self.data.qtoolbutton_left_arrow["padding_bottom_value"], self.data.qtoolbutton_left_arrow["padding_bottom_type"]))

        if self.data.qtoolbutton_left_arrow["padding_left_value"] != 0 and self.data.qtoolbutton_left_arrow["padding_left_value"] != "0":
            f.write("\n   padding-left: {}{};".format(self.data.qtoolbutton_left_arrow["padding_left_value"], self.data.qtoolbutton_left_arrow["padding_left_type"]))


        if self.data.qtoolbutton_left_arrow["margin_top_value"] != 0 and self.data.qtoolbutton_left_arrow["margin_top_value"] != "0":
            f.write("\n   padding-top: {}{};".format(self.data.qtoolbutton_left_arrow["margin_top_value"], self.data.qtoolbutton_left_arrow["margin_top_type"]))

        if self.data.qtoolbutton_left_arrow["margin_right_value"] != 0 and self.data.qtoolbutton_left_arrow["margin_right_value"] != "0":
            f.write("\n   margin-right: {}{};".format(self.data.qtoolbutton_left_arrow["margin_right_value"], self.data.qtoolbutton_left_arrow["margin_right_type"]))

        if self.data.qtoolbutton_left_arrow["margin_bottom_value"] != 0 and self.data.qtoolbutton_left_arrow["margin_bottom_value"] != "0":
            f.write("\n   margin-bottom: {}{};".format(self.data.qtoolbutton_left_arrow["margin_bottom_value"], self.data.qtoolbutton_left_arrow["margin_bottom_type"]))

        if self.data.qtoolbutton_left_arrow["margin_left_value"] != 0 and self.data.qtoolbutton_left_arrow["margin_left_value"] != "0":
            f.write("\n   margin-left: {}{};".format(self.data.qtoolbutton_left_arrow["margin_left_value"], self.data.qtoolbutton_left_arrow["margin_left_type"]))


        f.write("\n}")
