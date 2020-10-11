try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources
import json
import static


def get_mapped_commands() -> dict:
    """Returns dictionary of mapped commands from mapped_commands_full.json"""
    json_txt = pkg_resources.read_text(static, "mapped_commands_full.json")
    return json.loads(json_txt)
