class VisualStimulusRegistry:
    """The 10 specific images listed on the user interface screen."""
    
    IMAGES = {
        1: "RED_SQUARE",
        2: "BLUE_CIRCLE",
        3: "GREEN_TRIANGLE",
        4: "YELLOW_STAR",
        5: "PURPLE_HEXAGON",
        6: "ORANGE_CROSS",
        7: "BLACK_DIAMOND",
        8: "WHITE_SPHERE",
        9: "PINK_ARROW",
        10: "CYAN_CYLINDER"
    }

    @classmethod
    def get_name(cls, image_id: int) -> str:
        return cls.IMAGES.get(image_id, "INVALID_SELECTION")
