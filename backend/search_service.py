### These are fake placeholder scenes to use while I test functions and stuff
scenes = [
    {
        "scene_id": "S1A_001",
        "platform": "Sentinel-1",
        "beam_mode": "IW",
        "resolution": 10.0,
        "downloadable": True,
    },
    {
        "scene_id": "S1A_002",
        "platform": "Sentinel-1",
        "beam_mode": "EW",
        "resolution": 25.0,
        "downloadable": True,
    },
    {
        "scene_id": "ALOS_001",
        "platform": "ALOS",
        "beam_mode": "FBS",
        "resolution": 12.5,
        "downloadable": False,
    },
    {
        "scene_id": "S1B_001",
        "platform": "Sentinel-1",
        "beam_mode": "IW",
        "resolution": 10.0,
        "downloadable": True,
    },
]


def filter_scenes_by_platform(scenes: list[dict], platform: str) -> list[dict]:
    matching_scenes = []
    for scene in scenes:
        if scene["platform"] == platform:
            matching_scenes.append(scene)
    return matching_scenes


def search_scenes(
    scenes: list[dict], platform: str, beam_mode: str, downloadable: bool
) -> list[dict]:
    matching_scenes = []
    for scene in scenes:
        if (
            scene["platform"] == platform
            and scene["beam_mode"] == beam_mode
            and scene["downloadable"] == downloadable
        ):
            matching_scenes.append(scene)
    return matching_scenes


searched_scenes = search_scenes(scenes, "Sentinel-1", "EW", downloadable=True)
print(searched_scenes)
